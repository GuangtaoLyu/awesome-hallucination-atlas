# -*- coding: utf-8 -*-
"""
Fetch real abstracts from the arXiv export API for all papers with arXiv links.
Results cached in data/abstracts.json  ->  {arxiv_id: {"title":..., "abstract":...}}
Re-running only fetches missing IDs (incremental).
"""
import json
import os
import re
import time
import urllib.parse
import xml.etree.ElementTree as ET

from raw_data import RAW

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
CACHE = os.path.join(ROOT, "data", "abstracts.json")
FOUND_LINKS = os.path.join(ROOT, "data", "found_links.json")

NS = {"a": "http://www.w3.org/2005/Atom"}
BATCH = 50
API = "https://export.arxiv.org/api/query"


from lib_common import arxiv_id, atomic_dump
from code_common import http_get, load_json


def load_cache():
    return load_json(CACHE, {})


def fetch_batch(ids):
    q = urllib.parse.urlencode({"id_list": ",".join(ids), "max_results": len(ids)})
    txt = http_get(f"{API}?{q}", timeout=60, retries=5)
    root = ET.fromstring(txt)
    out = {}
    for entry in root.findall("a:entry", NS):
        eid = entry.findtext("a:id", "", NS)
        m = re.search(r"abs/(\d{4}\.\d{4,5})", eid)
        if not m:
            continue
        title = re.sub(r"\s+", " ", entry.findtext("a:title", "", NS)).strip()
        abstract = re.sub(r"\s+", " ", entry.findtext("a:summary", "", NS)).strip()
        published = entry.findtext("a:published", "", NS)
        if abstract:
            out[m.group(1)] = {"title": title, "abstract": abstract, "published": published}
    return out


def main():
    ids = []
    for _, _, url, _ in RAW:
        i = arxiv_id(url)
        if i and i not in ids:
            ids.append(i)
    # also include urls recovered by enrich_links.py (data/found_links.json)
    if os.path.exists(FOUND_LINKS):
        with open(FOUND_LINKS, encoding="utf-8") as f:
            for u in json.load(f).values():
                i = arxiv_id(u)
                if i and i not in ids:
                    ids.append(i)
    cache = load_cache()
    # entries fetched before the "published" field existed need a re-fetch
    missing = [i for i in ids if i not in cache or "published" not in cache[i]]
    print(f"total arxiv ids: {len(ids)}, cached: {len(ids) - len(missing)}, to fetch: {len(missing)}")

    for k in range(0, len(missing), BATCH):
        chunk = missing[k:k + BATCH]
        try:
            got = fetch_batch(chunk)
            cache.update(got)
            print(f"batch {k // BATCH + 1}: requested {len(chunk)}, got {len(got)}")
        except Exception as e:
            print(f"batch {k // BATCH + 1} FAILED: {e}")
        time.sleep(3)  # arXiv API courtesy delay

    os.makedirs(os.path.dirname(CACHE), exist_ok=True)
    atomic_dump(CACHE, cache, indent=1)
    print(f"cache saved: {len(cache)} abstracts -> {CACHE}")


if __name__ == "__main__":
    main()
