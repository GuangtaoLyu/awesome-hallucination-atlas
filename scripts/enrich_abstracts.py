#!/usr/bin/env python3
"""Enrich missing abstracts from Crossref (DOI-based).

For papers that already have a DOI link but no abstract text, query the
Crossref REST API, parse the JATS abstract into plain text, and cache it in
data/abstracts_extra.json keyed by normalized title (consumed by generate.py).

Safe & resumable:
  - only touches papers lacking an abstract AND carrying a doi.org link;
  - writes incrementally every 20 papers;
  - retries/backsoff on 429/5xx/timeout and NEVER caches a transient error;
  - re-running skips DOIs/keys already cached.

Usage:  python enrich_abstracts.py [limit]
"""
import json
import os
import re
import sys
import time
import urllib.parse

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PAPERS = os.path.join(ROOT, "data", "papers.json")
EXTRA = os.path.join(ROOT, "data", "abstracts_extra.json")
UA = {"User-Agent": "hallucination-lib-enrich/1.0 (mailto:research@example.com)"}


from lib_common import norm_title as norm
from code_common import http_get, load_json, atomic_dump, TransientError


def strip_jats(xml):
    """JATS XML -> plain text."""
    if not xml:
        return ""
    txt = re.sub(r"</?jats:[^>]+>", " ", xml)
    txt = re.sub(r"<[^>]+>", " ", txt)
    txt = (txt.replace("&lt;", "<").replace("&gt;", ">")
              .replace("&amp;", "&").replace("&quot;", '"'))
    txt = re.sub(r"\s+", " ", txt).strip()
    return txt


def doi_from_url(u):
    m = re.search(r"10\.\d{4,9}/[^\s)]+", u)
    return m.group(0).rstrip(".") if m else None


def main():
    papers = load_json(PAPERS).get("papers", [])
    extra = load_json(EXTRA)
    cached_keys = set(extra.keys())

    targets = []
    for p in papers:
        if p.get("abstract"):
            continue
        u = p.get("url", "")
        doi = doi_from_url(u)
        if not doi:
            continue
        k = norm(p["title"])
        if k in cached_keys:
            continue
        targets.append((k, doi, p["title"]))

    limit = int(sys.argv[1]) if len(sys.argv) > 1 else len(targets)
    targets = targets[:limit]
    print(f"candidates (no abstract + DOI): {len(targets)} (cap={limit})")

    done = 0
    for i, (k, doi, title) in enumerate(targets, 1):
        try:
            data = json.loads(http_get(
                "https://api.crossref.org/works/" + urllib.parse.quote(doi, safe=""),
                headers=UA, timeout=40, retries=6,
            ))
            abs_xml = data.get("message", {}).get("abstract", "")
            text = strip_jats(abs_xml)
        except TransientError:
            text = ""
        except Exception as e:
            text = ""
            print(f"  [{i}] ERR {doi}: {e}")
        if text:
            extra[k] = text
            done += 1
            print(f"  [{i}/{len(targets)}] + {doi}  ({len(text)} chars)  {title[:55]}")
        else:
            print(f"  [{i}/{len(targets)}] . no abstract for {doi}")
        if i % 20 == 0:
            atomic_dump(EXTRA, extra, indent=1)
        time.sleep(1.0)

    atomic_dump(EXTRA, extra, indent=1)
    print(f"Done. Newly enriched abstracts this run: {done}/{len(targets)}")
    print(f"Total cached in abstracts_extra.json: {len(extra)}")


if __name__ == "__main__":
    main()
