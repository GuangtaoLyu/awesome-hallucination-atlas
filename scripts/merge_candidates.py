# -*- coding: utf-8 -*-
"""Merge data/candidates_new.json into data/seed.json.

Single source of truth: data/seed.json is a JSON array of
[title, authors, url, year] records (raw_data.RAW is just a compatibility
shim over it). We dedupe candidates against existing entries (by normalized
title, plus arXiv ID and DOI as secondary keys) and rebuild the file grouped
by year (descending), keeping existing entries' relative order and appending
new ones per year.
"""
import json
import re
import os

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
CAND = os.path.join(ROOT, "data", "candidates_new.json")
OUT = os.path.join(ROOT, "data", "seed.json")

from raw_data import RAW
from collect_candidates import OFF_TOPIC

ARXIV_RE = re.compile(r"arxiv\.org/abs/(\d{4}\.\d{4,5})")
DOI_RE = re.compile(r"doi\.org/(10\.\S+)", re.I)


from lib_common import norm_title as norm


from lib_common import arxiv_id


def doi(url):
    m = DOI_RE.search(url or "")
    return m.group(1) if m else None


# ---- build existing keys / ids for dedup ----
# Also drop existing entries that are off-topic (medical / CV super-resolution
# "hallucination"), so the file is clean regardless of when they entered.
existing_keys = set()
existing_arxiv = set()
existing_doi = set()
clean_raw = []
dropped_existing = 0
for t, a, u, y in RAW:
    if OFF_TOPIC.search(t):
        dropped_existing += 1
        continue
    clean_raw.append((t, a, u, y))
    existing_keys.add(norm(t))
    if arxiv_id(u):
        existing_arxiv.add(arxiv_id(u))
    if doi(u):
        existing_doi.add(doi(u).lower())

with open(CAND, encoding="utf-8") as f:
    cands = json.load(f)

new_rows = []
seen_keys = set(existing_keys)
seen_arxiv = set(existing_arxiv)
seen_doi = set(existing_doi)
skipped = 0
for c in cands:
    title = (c.get("title") or "").strip().rstrip(".")
    if not title:
        skipped += 1
        continue
    # HARD GATE: title must contain the stem "hallucinat" (covers the verb
    # forms too — e.g. "MLLMs Hallucinate ..."), and must not be an off-topic
    # (medical / CV super-resolution) use of the word.
    if "hallucinat" not in title.lower() or OFF_TOPIC.search(title):
        skipped += 1
        continue
    key = norm(title)
    aid = arxiv_id(c.get("url", ""))
    did = doi(c.get("url", ""))
    if key in seen_keys or (aid and aid in seen_arxiv) or (did and did.lower() in seen_doi):
        skipped += 1
        continue
    year = int(c.get("year") or 0)
    # recover year from arxiv id if journal year missing
    if (year < 2020) and aid:
        year = 2000 + int(aid[:2])
    if year < 2020:
        # out of scope or unparseable year -> still keep but flag
        year = year or 2020
    seen_keys.add(key)
    if aid:
        seen_arxiv.add(aid)
    if did:
        seen_doi.add(did.lower())
    authors = (c.get("authors") or "Unknown").replace('"', "'")
    url = (c.get("url") or "").strip()
    new_rows.append((title, authors, url, year))

# ---- merge: existing first, then new, grouped by year (descending) ----
by_year = {}
for t, a, u, y in clean_raw:
    by_year.setdefault(y, []).append((t, a, u, y))
for t, a, u, y in new_rows:
    by_year.setdefault(y, []).append((t, a, u, y))

# ---- emit ----
merged = []
for y in sorted(by_year.keys(), reverse=True):
    for t, a, u, y_ in by_year[y]:
        merged.append([t, a, u, y_])
with open(OUT, "w", encoding="utf-8") as f:
    json.dump(merged, f, ensure_ascii=False, indent=1)

print(f"existing (after off-topic drop): {len(clean_raw)}  (dropped {dropped_existing} off-topic from existing)")
print(f"candidates: {len(cands)}, skipped(dup/off-topic/empty): {skipped}, added: {len(new_rows)}")
print(f"merged total: {len(clean_raw) + len(new_rows)}")
by_year_count = {y: len(v) for y, v in by_year.items()}
print("by year:", dict(sorted(by_year_count.items(), reverse=True)))
