# -*- coding: utf-8 -*-
"""One-off targeted harvest of 2026 conference proceedings.

Why: the original CVF channel silently missed CVPR2026 (12 MB ?day=all page
timed out at 30s AND the 2026 page layout changed from <dd class="auth"> to
per-author query_author forms). This script:

  1. CVF CVPR2026 (new-layout parsing, long timeout) -> candidates + authoritative
     venue_links.json entries ({venue:'CVPR', year:2026, ee:<official html>}).
  2. DBLP re-sweep of all major venue keys, keeping ONLY year>=2026 records,
     to catch proceedings indexed after the first harvest.

Writes data/candidates_new.json (replacing it with ONLY the new finds) and
updates data/venue_links.json for CVF-official entries.
Then run: merge_candidates.py -> generate.py
"""
import json, os, re, time, urllib.request, urllib.parse

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
OUT = os.path.join(ROOT, "data", "candidates_new.json")
VENUE_LINKS = os.path.join(ROOT, "data", "venue_links.json")

from raw_data import RAW as EXISTING
from collect_candidates import (
    norm, relevant, dblp_authors, get_json, DBLP_VENUE_KEYS, CVF_BASE,
)
from lib_common import atomic_dump

SEEN = {norm(t) for (t, *_) in EXISTING}
new_cands = []
try:
    with open(VENUE_LINKS, encoding="utf-8") as f:
        vlinks = json.load(f)
except (OSError, json.JSONDecodeError):
    vlinks = {}
vl_added = 0


def harvest_cvf_2026():
    global vl_added
    url = f"{CVF_BASE}/CVPR2026?day=all"
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    html = urllib.request.urlopen(req, timeout=300).read().decode("utf-8", "ignore")
    chunks = re.split(r'<dt class="ptitle">', html)[1:]
    print(f"CVF CVPR2026: {len(chunks)} papers on page")
    n_new = n_hall = 0
    for ch in chunks:
        am = re.search(r'<a[^>]*href="([^"]+)"[^>]*>(.*?)</a>', ch, re.S)
        if not am:
            continue
        title = re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", am.group(2))).strip()
        if "hallucinat" not in title.lower():
            continue
        n_hall += 1
        if not relevant(title, "CVPR"):
            print(f"  off-topic skip: {title}")
            continue
        href = am.group(1)
        if href.startswith("/"):
            href = CVF_BASE + href
        names = re.findall(r'name="query_author"\s+value="([^"]+)"', ch)
        if not names:
            old = re.search(r'<dd class="auth">(.*?)</dd>', ch, re.S)
            names = [re.sub(r"<[^>]+>", "", old.group(1)).strip()] if old else []
        if len(names) > 2:
            authors = (names[0].split()[-1] if names[0].split() else names[0]) + " et al."
        else:
            authors = " and ".join(names) or "CVF"
        key = norm(title)
        # authoritative official venue mapping regardless of dedup status
        if key not in vlinks or not vlinks.get(key):
            vlinks[key] = {"venue": "CVPR", "year": 2026, "ee": href}
            vl_added += 1
        if key in SEEN:
            continue
        SEEN.add(key)
        new_cands.append({
            "title": title, "authors": authors, "url": href,
            "year": 2026, "source": "CVF:CVPR",
        })
        n_new += 1
    print(f"CVF CVPR2026: hallucination-in-title={n_hall}, new={n_new}, venue_links added={vl_added}")


def harvest_dblp_2026():
    total = 0
    for vk in DBLP_VENUE_KEYS:
        q = urllib.parse.quote(f"hallucinat venue:{vk}")
        u = f"https://dblp.org/search/publ/api?q={q}&format=json&h=1000"
        d = get_json(u)
        if not d:
            print(f"  DBLP {vk}: query failed; skip")
            continue
        hits = d.get("result", {}).get("hits", {}).get("hit", [])
        n = 0
        for h in hits:
            info = h["info"]
            t = info.get("title", {})
            title = t.get("text", t) if isinstance(t, dict) else t
            title = title.strip().rstrip(".")
            year = int(info.get("year", 0))
            if year < 2026:
                continue
            if not relevant(title, vk):
                continue
            key = norm(title)
            if key in SEEN:
                continue
            SEEN.add(key)
            ee = info.get("ee", "") or ""
            new_cands.append({
                "title": title, "authors": dblp_authors(info), "url": ee,
                "year": year, "source": f"DBLP:{vk}",
            })
            n += 1
        if n:
            print(f"  DBLP {vk}: +{n} new 2026")
        time.sleep(1.5)
        total += n
    print(f"DBLP 2026 sweep -> {total} new")


def main():
    harvest_cvf_2026()
    harvest_dblp_2026()
    atomic_dump(OUT, new_cands, indent=1)
    atomic_dump(VENUE_LINKS, vlinks, indent=1)
    print(f"\nTOTAL new candidates: {len(new_cands)} -> {OUT}")
    print(f"venue_links updated: +{vl_added}")


if __name__ == "__main__":
    main()
