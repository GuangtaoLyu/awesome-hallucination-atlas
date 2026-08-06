"""Rebuild data/venue_years.json from the committed data/papers.json.

Disaster-recovery / one-off tool. venue_years.json is the committed
cold-checkout fallback for the paper *year* used by generate.py when the
gitignored enrichment cache (data/venue_links.json) is absent, so a fresh
clone / CI checkout always reproduces the correct conference years.

Run:  python scripts/rebuild_venue_years.py
"""
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
from lib_common import norm_title  # noqa: E402


def main():
    ppath = os.path.join(ROOT, "data", "papers.json")
    data = json.load(open(ppath, encoding="utf-8"))
    papers = data["papers"] if isinstance(data, dict) and "papers" in data else data

    out = {}
    for p in papers:
        t = (p.get("title") or "").strip()
        y = p.get("year")
        if t and y:
            out[norm_title(t)] = int(y)

    opath = os.path.join(ROOT, "data", "venue_years.json")
    with open(opath, "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=0, sort_keys=True)
    print(f"wrote {opath}: {len(out)} entries")


if __name__ == "__main__":
    main()
