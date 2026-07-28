# -*- coding: utf-8 -*-
"""
Enrichment pipeline (incremental, cached):

1. resolve_missing_urls : papers without any URL -> search arXiv by title,
   accept only high-similarity matches       -> data/found_links.json
2. dblp_venues : query DBLP for the official (non-CoRR) publication record
   of every paper -> real venue (CVPR/NeurIPS/...), official year and
   official link (ee/DOI)                    -> data/venue_links.json

NOTE: code-link discovery lives entirely in scripts/fetch_code.py -- a precise
multi-source finder (abstract GitHub links + Semantic Scholar `code` + GitHub
`in:readme <arxiv_id>` scored by title/acronym overlap + `in:name <acronym>` +
GitHub code search + ACL Anthology / OpenReview / Zenodo). It owns the
data/code_links.json cache; this module no longer writes it.

All results are caches keyed by normalized title; generate.py merges them.
Negative results are cached too ("" value) so re-runs skip them.
"""
import json
import os
import re
import time
import urllib.parse
import xml.etree.ElementTree as ET
from difflib import SequenceMatcher

from raw_data import RAW
from lib_common import norm_title, atomic_dump
from code_common import http_get, load_json, TransientError

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
FOUND_LINKS = os.path.join(ROOT, "data", "found_links.json")
CODE_LINKS = os.path.join(ROOT, "data", "code_links.json")
ABS_CACHE = os.path.join(ROOT, "data", "abstracts.json")
VENUE_LINKS = os.path.join(ROOT, "data", "venue_links.json")

NS = {"a": "http://www.w3.org/2005/Atom"}
UA = {"User-Agent": "awesome-hallu-bot/1.0"}


# ------------------------------------------------ 1. missing paper URLs
def resolve_missing_urls():
    cache = load_json(FOUND_LINKS)
    targets = [(t, a) for t, a, url, y in RAW if not url]
    todo = [(t, a) for t, a in targets if norm_title(t) not in cache]
    print(f"[urls] papers without url: {len(targets)}, to search: {len(todo)}")

    for i, (title, _) in enumerate(todo, 1):
        key = norm_title(title)
        try:
            # quote full title for phrase search
            q = urllib.parse.urlencode({
                "search_query": 'ti:"%s"' % title.replace('"', ""),
                "max_results": 3,
            })
            xml = http_get(f"https://export.arxiv.org/api/query?{q}",
                           headers=UA, timeout=30)
            root = ET.fromstring(xml)
            best = ("", 0.0)
            for entry in root.findall("a:entry", NS):
                et = re.sub(r"\s+", " ", entry.findtext("a:title", "", NS)).strip()
                sim = SequenceMatcher(None, norm_title(et), key).ratio()
                if sim > best[1]:
                    m = re.search(r"abs/(\d{4}\.\d{4,5})", entry.findtext("a:id", "", NS))
                    if m:
                        best = (f"https://arxiv.org/abs/{m.group(1)}", sim)
            cache[key] = best[0] if best[1] >= 0.92 else ""
            status = cache[key] or f"no-match(best={best[1]:.2f})"
            print(f"[urls] {i}/{len(todo)} {title[:50]}... -> {status}")
        except Exception as e:
            print(f"[urls] {i}/{len(todo)} FAILED {title[:40]}: {e}")
        time.sleep(3)
    atomic_dump(FOUND_LINKS, cache, indent=1)
    hit = sum(1 for v in cache.values() if v)
    print(f"[urls] resolved {hit}/{len(cache)}")


# ------------------------------------------------ 2. code links from abstracts
# REMOVED: abstract GitHub extraction now lives in scripts/fetch_code.py
# (abstract_links), which owns data/code_links.json. Keeping it here too would
# double-write the cache. Run `python scripts/fetch_code.py` to populate it.


# ------------------------------------------------ 4. DBLP official venues
def dblp_venues():
    """Look up the official (non-arXiv/CoRR) publication record on DBLP.

    Cached: key -> {"venue": "CVPR", "year": 2024, "ee": "https://doi.org/..."}
            or "" when no formal venue record exists (negative cache).
    """
    cache = load_json(VENUE_LINKS)
    seen = set()
    todo = []
    for t, a, url, y in RAW:
        key = norm_title(t)
        if key in seen or key in cache:
            continue
        seen.add(key)
        todo.append((t, key))
    print(f"[venue] papers to look up on DBLP: {len(todo)}")

    for i, (title, key) in enumerate(todo, 1):
        try:
            # strip punctuation: DBLP's query parser 500s on some special chars
            clean_q = re.sub(r"[^\w\s]", " ", title)
            clean_q = re.sub(r"\s+", " ", clean_q).strip()
            q = urllib.parse.urlencode({"q": clean_q, "format": "json", "h": 10})
            data = json.loads(http_get(f"https://dblp.org/search/publ/api?{q}",
                                       headers=UA))
            hits = data.get("result", {}).get("hits", {}).get("hit", []) or []
            best = ""
            for h in hits:
                info = h.get("info", {})
                ht = re.sub(r"\.\s*$", "", info.get("title", ""))
                if SequenceMatcher(None, norm_title(ht), key).ratio() < 0.92:
                    continue
                venue = info.get("venue", "")
                if isinstance(venue, list):
                    venue = venue[0] if venue else ""
                if not venue or venue == "CoRR":   # skip the arXiv record
                    continue
                ee = info.get("ee", "")
                if isinstance(ee, list):
                    ee = ee[0] if ee else ""
                best = {"venue": venue, "year": int(info.get("year", 0) or 0), "ee": ee}
                break
            cache[key] = best  # "" = negative cache
            label = f"{best['venue']} {best['year']}" if best else "no formal venue"
            print(f"[venue] {i}/{len(todo)} {title[:48]:50s} -> {label}")
        except Exception as e:
            print(f"[venue] {i}/{len(todo)} FAILED {title[:40]}: {e}")
            if "429" in str(e) or "403" in str(e) or isinstance(e, TransientError):
                print("[venue] rate-limited, saving progress and waiting 60s...")
                atomic_dump(VENUE_LINKS, cache, indent=1)
                time.sleep(60)
        if i % 25 == 0:
            atomic_dump(VENUE_LINKS, cache, indent=1)
        time.sleep(2)  # DBLP courtesy delay
    atomic_dump(VENUE_LINKS, cache, indent=1)
    hit = sum(1 for v in cache.values() if v)
    print(f"[venue] formal venue found: {hit}/{len(cache)}")


if __name__ == "__main__":
    import sys
    steps = sys.argv[1:] or ["urls", "venue"]
    if "urls" in steps:
        resolve_missing_urls()
    if "venue" in steps:
        dblp_venues()
