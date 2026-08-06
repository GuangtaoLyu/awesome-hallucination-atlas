"""Rebuild data/venue_links.json as a COMMITTED seed cache from the already
committed data/papers.json.

Why: venue_links.json is the enrichment cache that carries each paper's
resolved conference/journal venue, year and external link. It was gitignored
and lost, so a clean checkout (or CI cache miss) fell back to arXiv years and
"arXiv"/"其他" venue names. Papers with a real venue_url in papers.json are
exactly the ones that used to be resolved, so we rebuild them as a seed that
the pipeline can restore on a cold checkout and incrementally extend.

Usage: python rebuild_venue_links.py <repo_root>
"""
import json
import os
import re
import sys

REPO = sys.argv[1] if len(sys.argv) > 1 else os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(REPO, "scripts"))
from lib_common import norm_title  # noqa: E402

ARXIVISH = re.compile(r"arxiv|其他|未标注", re.I)


def strip_year(v):
    return re.sub(r"\s+(?:19|20)\d{2}[a-z]?\s*$", "", v or "").strip()


def main():
    papers = json.load(open(os.path.join(REPO, "data", "papers.json"), encoding="utf-8"))["papers"]
    links = {}
    for p in papers:
        if ARXIVISH.search(p.get("venue") or ""):
            continue
        k = norm_title(p["title"])
        links[k] = {
            "venue": strip_year(p["venue"]),
            "year": int(p["year"]),
            "ee": p.get("venue_url", ""),
        }
    out = os.path.join(REPO, "data", "venue_links.json")
    json.dump(links, open(out, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(f"Wrote {len(links)} entries to data/venue_links.json")


if __name__ == "__main__":
    main()
