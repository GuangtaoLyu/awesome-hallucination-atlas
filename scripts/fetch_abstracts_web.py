"""Crawl missing abstracts from each paper's own publisher/conference site.

The Crossref pass (enrich_abstracts.py) already filled ~45%. This script
targets the papers that are STILL missing an abstract and routes each to the
site that actually hosts it:

  * ACL / EMNLP / NAACL / EACL / COLING / TACL / AACL / SemEval / LREC / workshops
        -> ACL Anthology HTML  (abstract lives in the `paperAbstract` div)
  * CVPR / ICCV / ECCV / WACV
        -> CVF openaccess HTML  (`<div id="abstract">`)
  * NeurIPS
        -> papers.nips.cc  `<... id="abstract">` page
  * ICLR / TMLR / OpenReview-hosted
        -> OpenReview API note (`content.abstract`)
  * anything still on arXiv (id present but no cached abstract)
        -> arXiv API `summary`

Output: merges into data/abstracts_extra.json (norm_title -> abstract),
the very file generate.py reads. Existing entries are preserved. Resumable:
reruns only touch papers still missing an abstract. 403/rate-limit is treated
as "skip for now" so a later rerun (after the IP cools down) can fill gaps.

Usage:
  python scripts/fetch_abstracts_web.py            # fill all missing
  python scripts/fetch_abstracts_web.py --limit 20 # test on first 20 missing
  python scripts/fetch_abstracts_web.py --force    # re-crawl everything
Then:  python scripts/generate.py
"""
import argparse
import json
import os
import re
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from code_common import (DATA, norm_title, load_papers, load_json, save_json,
                         http_get)

ABS_CACHE = os.path.join(DATA, "abstracts.json")        # arxiv-id -> {abstract}
OUT = os.path.join(DATA, "abstracts_extra.json")         # norm_title -> abstract

ARXIV_VENUES = {"ACL", "EMNLP", "NAACL", "EACL", "COLING", "TACL", "AACL",
                "LREC", "SEMEVAL", "TACL", "CONLL"}
CVF_VENUES = {"CVPR", "ICCV", "ECCV", "WACV"}


# ----------------------------------------------------------- html helpers
def _strip(html):
    t = re.sub(r"<[^>]+>", " ", html)
    t = re.sub(r"&amp;", "&", t)
    t = re.sub(r"&lt;", "<", t)
    t = re.sub(r"&gt;", ">", t)
    t = re.sub(r"\s+", " ", t).strip()
    return t


def _balanced_block(htm, marker):
    """Return inner HTML of the tag that matches `marker` (a compiled regex
    anchored at an opening tag), balancing <div>..</div> nesting."""
    m = marker.search(htm)
    if not m:
        return None
    i = htm.find(">", m.start()) + 1
    depth = 1
    k = i
    n = len(htm)
    while k < n:
        lt = htm.find("<", k)
        if lt < 0:
            break
        if htm.startswith("</div", lt, lt + 6):
            depth -= 1
        elif htm.startswith("<div", lt, lt + 5):
            depth += 1
        if depth == 0:
            return htm[i:lt]
        k = lt + 1
    return htm[i:]


def _anthology(htm):
    # Anthology uses UNQUOTED attributes: id=paperAbstract
    blk = _balanced_block(htm, re.compile(r'<div[^>]*id=paperAbstract', re.I))
    if blk:
        t = _strip(blk)
        if len(t) > 40:
            return t
    # fallback: any div whose class mentions abstract
    blk = _balanced_block(htm, re.compile(r'<div[^>]*class=[^>]*abstract', re.I))
    if blk:
        t = _strip(blk)
        if len(t) > 40:
            return t
    return None


def _simple_id(htm, idval):
    blk = _balanced_block(htm, re.compile(r'<div[^>]*id=%s' % re.escape(idval), re.I))
    return _strip(blk) if blk else None


# ----------------------------------------------------------- per-source
def anthology_id(p):
    for f in ("venue_url", "url"):
        s = p.get(f) or ""
        m = re.search(r"aclanthology\.org/([0-9]{4}\.[a-z0-9.\-]+)", s)
        if m:
            return m.group(1)
    # ACL Anthology DOIs: 10.18653/v1/<id>
    m = re.search(r"10\.18653/v1/([0-9]{4}\.[a-z0-9.\-]+)", p.get("doi") or "")
    if m:
        return m.group(1)
    return None


def fetch_anthology(p):
    aid = anthology_id(p)
    if not aid:
        return None
    try:
        return _anthology(http_get(f"https://aclanthology.org/{aid}/"))
    except Exception:  # noqa: BLE001
        return None


def fetch_cvf(p):
    for f in ("venue_url", "url"):
        if "openaccess.thecvf.com" in (p.get(f) or ""):
            try:
                return _simple_id(http_get(p[f]), "abstract")
            except Exception:  # noqa: BLE001
                return None
    return None


def fetch_neurips(p):
    for f in ("venue_url", "url"):
        if "nips.cc" in (p.get(f) or ""):
            try:
                return _simple_id(http_get(p[f]), "abstract")
            except Exception:  # noqa: BLE001
                return None
    return None


def fetch_openreview(p):
    m = re.search(r"openreview\.net/(?:forum|pdf)\?id=([A-Za-z0-9]+)",
                  (p.get("url") or "") + " " + (p.get("venue_url") or ""))
    if not m:
        return None
    try:
        j = json.loads(http_get(f"https://api.openreview.net/notes?id={m.group(1)}"))
        for n in j.get("notes") or []:
            a = (n.get("content") or {}).get("abstract")
            if isinstance(a, dict):
                a = a.get("value") or a.get("url")
            if a and len(str(a)) > 40:
                return str(a).strip()
    except Exception:  # noqa: BLE001
        return None
    return None


def fetch_arxiv(p):
    aid = None
    for f in ("url", "venue_url"):
        m = re.search(r"arxiv\.org/abs/(\d{4}\.\d{4,5})", p.get(f) or "")
        if m:
            aid = m.group(1)
            break
    if not aid:
        return None
    try:
        import urllib.parse
        u = ("https://export.arxiv.org/api/query?id_list=" + aid)
        x = http_get(u)
        m = re.search(r"<summary>(.*?)</summary>", x, re.S)
        if m:
            return _strip(m.group(1))
    except Exception:  # noqa: BLE001
        return None
    return None


def route(p):
    v = (p.get("venue") or "").upper()
    vb = v.split()[0] if v else ""
    if anthology_id(p) or vb in ARXIV_VENUES:
        return fetch_anthology
    if vb in CVF_VENUES:
        return fetch_cvf
    if "NIPS.CC" in (p.get("venue_url") or "").upper() or vb == "NEURIPS":
        return fetch_neurips
    if "OPENREVIEW" in ((p.get("url") or "") + (p.get("venue_url") or "")).upper():
        return fetch_openreview
    if "arxiv.org" in ((p.get("url") or "") + (p.get("venue_url") or "")).lower():
        return fetch_arxiv
    return None


# ----------------------------------------------------------- driver
def has_abstract(p, arxiv, extra):
    aid = None
    for f in ("url", "venue_url"):
        m = re.search(r"arxiv\.org/abs/(\d{4}\.\d{4,5})", p.get(f) or "")
        if m:
            aid = m.group(1)
            break
    if aid and (arxiv.get(aid) or {}).get("abstract"):
        return True
    if extra.get(norm_title(p["title"])):
        return True
    return bool(p.get("abstract"))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--limit", type=int, default=0)
    ap.add_argument("--force", action="store_true")
    args = ap.parse_args()

    papers = load_papers()
    arxiv = load_json(ABS_CACHE, {})
    extra = {} if args.force else load_json(OUT, {})

    targets = [p for p in papers if args.force or not has_abstract(p, arxiv, extra)]
    if args.limit:
        targets = targets[:args.limit]

    print(f"[abs] {len(targets)} papers missing an abstract to crawl")
    found = 0
    for i, p in enumerate(targets, 1):
        fn = route(p)
        text = fn(p) if fn else None
        if text:
            text = re.sub(r"^\s*abstract\s+", "", text, flags=re.I).strip()
        if text and len(text) > 40:
            extra[norm_title(p["title"])] = text
            found += 1
            print(f"  {i}/{len(targets)} + [{ (p.get('venue') or '')[:12] }] {text[:55]}...")
        else:
            print(f"  {i}/{len(targets)} . {p['title'][:45]}")
        save_json(OUT, extra)          # incremental / resumable
        time.sleep(0.6)

    print(f"[abs] done. +{found} new abstracts; abstracts_extra.json now has "
          f"{len(extra)} entries. Run: python scripts/generate.py")


if __name__ == "__main__":
    main()
