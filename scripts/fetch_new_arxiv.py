#!/usr/bin/env python3
"""arXiv harvest for the hallucination research DB.

Two modes:
  * Recent (default): fetches the newest hallucination preprints within
    RECENT_DAYS and merges new candidates into data/incremental.json.
  * Backfill (--from YYYYMMDD [--to YYYYMMDD]): paginates ALL matching
    preprints in the date range and merges new candidates. Used for a
    one-time catch-up of older papers the manual list missed.

De-duplication is against data/papers.json (norm_title) and against
already-harvested entries. The incremental file is always *merged*
(cumulative), never overwritten, so earlier harvests are preserved.

Run:
  python scripts/fetch_new_arxiv.py                  # recent only
  python scripts/fetch_new_arxiv.py --from 20240101  # backfill since 2024-01-01
  python scripts/fetch_new_arxiv.py --from 20240101 --count  # dry run (no write)
"""
import os
import re
import sys
import json
import time
import html
import argparse
import unicodedata
import urllib.parse
import xml.etree.ElementTree as ET
from datetime import datetime, timedelta, timezone

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
DATA = os.path.join(ROOT, "data")

sys.path.insert(0, HERE)
from code_common import http_get, norm_title, atomic_dump  # noqa: E402

# Topic-relevance gate: reuse the canonical OFF_TOPIC filter from
# collect_candidates.py so backfilled arXiv papers obey the SAME cleaning
# rules as the manually-curated library (drop classic CV-synthesis /
# medical-human / psychology "hallucination" senses). An LLM/VLM marker in
# the title overrides the hit (avoids false positives like "clinical
# hallucinations in LVLMs" or "hallucination scale for LLMs").
try:
    from collect_candidates import OFF_TOPIC as _OFF_TOPIC
except Exception:
    _OFF_TOPIC = None

_AI_MARKER = re.compile(
    r"\b(llm|llms|mllm|mllms|lvlm|lvlms|vlm|vlms|gpt|chatgpt)\b|"
    r"large language model|language model|multimodal|vision.?language|"
    r"chain.?of.?thought", re.I)


def is_offtopic(title, summary=None):
    if _OFF_TOPIC is None or not _OFF_TOPIC.search(title):
        return False
    if _AI_MARKER.search(title):   # clearly about AI/ML model behaviour
        return False
    return True


NS = {"a": "http://www.w3.org/2005/Atom"}

# Field used to match "hallucination":
#   "ti:"   -> title only   : high precision (DEFAULT — avoids pulling in
#                             classic CV tasks / unrelated papers that merely
#                             co-mention the word in abstract or comments)
#   "all:"  -> anywhere     : high recall, more noise (opt-in via --broad)
ARXIV_FIELD = "ti"
ARXIV_QUERY = (
    f"{ARXIV_FIELD}:hallucination AND "
    "(cat:cs.CL OR cat:cs.CV OR cat:cs.AI OR cat:cs.MM)"
)
# Recall policy: ONLY papers whose TITLE contains "hallucination" are admitted.
# The arXiv query uses ti:hallucination (title field) and process() re-enforces
# the same rule in code, so synonym / paraphrase queries ("factual
# consistency", "faithful", ...) are intentionally NOT used — we never pull in
# work that doesn't name "hallucination" in its title.
MAX_RESULTS = 200
RECENT_DAYS = 21          # recent-mode window (submittedDate, newest-first)
PAGE_DELAY = 3            # seconds between paginated API calls (arXiv politeness)
MAX_PAGES = 200           # safety cap (~40k results)


def fnorm(t):
    """Fold accents / compatibility chars (ö->o, ²->2, fullwidth->halfwidth)
    on top of norm_title so near-identical titles like 'SchröMind' vs
    'SchroMind' or 'P²-DPO' vs 'P$^2$-DPO' collide as the same paper."""
    if not t:
        return ""
    s = unicodedata.normalize("NFKD", t)
    s = "".join(c for c in s if not unicodedata.combining(c))
    return norm_title(s)


def load_existing():
    """Return (folded-title set, arxiv-id set) of papers already in the DB."""
    path = os.path.join(DATA, "papers.json")
    if not os.path.exists(path):
        return set(), set()
    with open(path, encoding="utf-8") as f:
        papers = json.load(f)["papers"]
    titles = {fnorm(p.get("title", "")) for p in papers}
    ids = set()
    for p in papers:
        m = re.search(r"arxiv\.org/abs/(\d{4}\.\d{4,5})", str(p.get("url", "")))
        if m:
            ids.add(m.group(1))
    return titles, ids


def load_abs_cache():
    abspath = os.path.join(DATA, "abstracts.json")
    if os.path.exists(abspath):
        try:
            with open(abspath, encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            return {}
    return {}


def harvest(q=None, start=0, from_date=None, to_date=None):
    query = q or ARXIV_QUERY
    if from_date or to_date:
        lo = from_date or "200001010000"
        hi = to_date or datetime.now(timezone.utc).strftime("%Y%m%d%H%M")
        query += f" AND submittedDate:[{lo} TO {hi}]"
    params = {
        "search_query": query,
        "sortBy": "submittedDate",
        "sortOrder": "descending",
        "max_results": MAX_RESULTS,
        "start": start,
    }
    url = "https://export.arxiv.org/api/query?" + urllib.parse.urlencode(params)
    xml = http_get(url)
    root = ET.fromstring(xml)
    return root.findall("a:entry", NS)


def _clean_text(s):
    """Decode arXiv HTML entities (&quot; &apos; &amp;) and NFKC-normalize
    (² -> 2, fullwidth -> halfwidth) so titles/abstracts are comparable and
    the norm_title dedup key is not polluted by entity artifacts."""
    if not s:
        return ""
    s = html.unescape(s)
    s = unicodedata.normalize("NFKC", s)
    return " ".join(s.split())


def parse_entry(e):
    title = _clean_text(e.find("a:title", NS).text)
    summary = _clean_text(e.find("a:summary", NS).text)
    published = (e.find("a:published", NS).text or "")[:10]
    id_url = e.find("a:id", NS).text or ""
    m = re.search(r"(\d{4}\.\d{4,5})(v\d+)?$", id_url)
    aid = m.group(1) if m else None
    authors = ", ".join(
        a.find("a:name", NS).text for a in e.findall("a:author", NS)
        if a.find("a:name", NS) is not None
    )
    arxiv_url = f"https://arxiv.org/abs/{aid}" if aid else id_url
    return title, summary, published, aid, authors, arxiv_url


def process(entries, existing_titles, existing_ids, abs_cache, cutoff=None,
            gate=None):
    """Return candidate list [title, authors, url, year]; also fills abs_cache.
    Skips a paper if its folded title OR its arXiv id already exists in the DB
    (same arXiv id === same paper, even across title renames / unicode variants).
    `gate` is the relevance filter (default is_offtopic)."""
    if gate is None:
        gate = is_offtopic
    candidates = []
    seen_new = set()
    skipped = 0
    for e in entries:
        title, summary, published, aid, authors, arxiv_url = parse_entry(e)
        if cutoff and published and published < cutoff:
            continue
        # Hard rule: the TITLE must contain "hallucination" (hallucinated /
        # hallucinating also count). No synonym recall — papers whose title
        # uses a different word are excluded regardless of query mode.
        if "hallucinat" not in (title or "").lower():
            continue
        nt = fnorm(title)
        if not nt or nt in existing_titles or nt in seen_new:
            continue
        if aid and aid in existing_ids:   # same arXiv id == same paper
            continue
        if gate(title, summary):         # not a model-hallucination paper
            skipped += 1
            continue
        seen_new.add(nt)
        year = int(published[:4]) if published else 2026
        candidates.append([title, authors, arxiv_url, year])
        if aid:
            cur = abs_cache.get(aid, {})
            cur["abstract"] = summary
            cur["published"] = published
            abs_cache[aid] = cur
    if skipped:
        print(f"[fetch_new_arxiv] dropped {skipped} off-topic/relevant "
              f"candidate(s)")
    return candidates


def merge_incremental(candidates):
    inc_path = os.path.join(DATA, "incremental.json")
    merged = {}
    if os.path.exists(inc_path):
        try:
            with open(inc_path, encoding="utf-8") as f:
                data = json.load(f)
            for it in data:
                if isinstance(it, (list, tuple)) and len(it) >= 4:
                    merged[fnorm(it[0])] = [str(it[0]), str(it[1]),
                                            str(it[2]), int(it[3])]
        except Exception:
            merged = {}
    for c in candidates:
        merged[fnorm(c[0])] = c
    ordered = list(merged.values())
    atomic_dump(inc_path, ordered, indent=2)
    return len(ordered)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--from", dest="from_date",
                    help="backfill lower bound YYYYMMDD (inclusive)")
    ap.add_argument("--to", dest="to_date",
                    help="backfill upper bound YYYYMMDD (inclusive, default now)")
    ap.add_argument("--count", action="store_true",
                    help="dry run: print candidate count, write nothing")
    ap.add_argument("--broad", action="store_true",
                    help="use all:hallucination (title+abstract+comments) for "
                         "high recall; DEFAULT is ti:hallucination (title only, "
                         "high precision — skips classic CV tasks that merely "
                         "co-mention the word)")
    args = ap.parse_args()

    if args.broad:
        global ARXIV_QUERY
        ARXIV_QUERY = ("all:hallucination AND "
                       "(cat:cs.CL OR cat:cs.CV OR cat:cs.AI OR cat:cs.MM)")

    existing_titles, existing_ids = load_existing()
    abs_cache = load_abs_cache()

    if args.from_date:
        # ---- backfill mode (paginated, full date range) ----
        entries = []
        start = 0
        pages = 0
        while pages < MAX_PAGES:
            page = harvest(start=start, from_date=args.from_date,
                           to_date=args.to_date)
            if not page:
                break
            entries.extend(page)
            if len(page) < MAX_RESULTS:
                break
            start += MAX_RESULTS
            pages += 1
            time.sleep(PAGE_DELAY)
        print(f"[fetch_new_arxiv] backfill: fetched {len(entries)} entries "
              f"from {args.from_date}..{args.to_date or 'now'}")
        candidates = process(entries, existing_titles, existing_ids,
                             abs_cache, cutoff=None)
    else:
        # ---- recent mode (last RECENT_DAYS, no pagination needed) ----
        try:
            entries = harvest()
        except Exception as ex:  # network / rate-limit
            # NOTE: do NOT wipe incremental.json on a transient failure — that
            # would destroy the historical backfill. Preserve existing data and
            # let the next scheduled run retry.
            print(f"[fetch_new_arxiv] arXiv unreachable: {ex!r}; "
                  f"keeping existing incremental.json, skipping.",
                  file=sys.stderr)
            return
        cutoff = (datetime.now(timezone.utc) - timedelta(days=RECENT_DAYS)).strftime("%Y-%m-%d")
        candidates = process(entries, existing_titles, existing_ids,
                             abs_cache, cutoff=cutoff)

    if args.count:
        yr = {}
        for c in candidates:
            yr[c[3]] = yr.get(c[3], 0) + 1
        print(f"[fetch_new_arxiv] DRY RUN: {len(candidates)} new candidate(s) "
              f"by year {dict(sorted(yr.items()))}")
        return

    total = merge_incremental(candidates)
    atomic_dump(os.path.join(DATA, "abstracts.json"), abs_cache, indent=2)
    print(f"[fetch_new_arxiv] {len(candidates)} new candidate(s); "
          f"{total} total in data/incremental.json")


if __name__ == "__main__":
    main()
