# -*- coding: utf-8 -*-
"""
Upgrade arXiv-preprint papers to formal conference / journal venues.

Two complementary, resilient signals (both with retry/backoff; transient
5xx/429/timeout errors are NEVER cached as negatives):

  Pass A — arXiv journal_ref / doi (authoritative, batched, few requests).
           When a paper is published, arXiv often records where (journal_ref)
           and its DOI. We parse the canonical venue + year from that text.

  Pass B — DBLP title search (canonical venue names + CCF ratings + ee links),
           the project's gold source. Used for papers Pass A did not resolve.

Resolved venues are cached and never re-queried. Cached-negative preprints
("" — not yet formally published) are skipped on normal runs. Pass `--force`
(e.g. the bi-monthly big update) to re-query cached negatives, so papers that
got published since the last run are picked up.

Results are written into data/venue_links.json keyed by norm_title, which
generate.py already consumes. Run generate.py afterwards to rebuild artifacts.

Usage: python update_arxiv_venues.py [limit]
"""
import json
import os
import re
import sys
import time
import urllib.parse
import xml.etree.ElementTree as ET
from difflib import SequenceMatcher

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
PAPERS = os.path.join(ROOT, "docs", "papers.json")
VENUE_LINKS = os.path.join(ROOT, "data", "venue_links.json")
CROSSREF_CACHE = os.path.join(ROOT, "data", "crossref_cache.json")

# Descriptive UA (DBLP's API guidance asks for an identifiable project +
# contact). A generic/fake browser UA is more likely to be throttled.
UA = {"User-Agent": "awesome-hallucination-atlas/1.0 "
      "(+https://github.com/GuangtaoLyu/awesome-hallucination-atlas)"}
NS = {"a": "http://www.w3.org/2005/Atom", "ar": "http://arxiv.org/schemas/atom"}


class TransientError(Exception):
    """Raised on 5xx / 429 / timeout — caller should retry."""


from lib_common import norm_title as norm, parse_venue, atomic_dump
from code_common import http_get, load_json, TransientError


# Venue resolution now lives in lib_common.VENUE_PATTERNS (single source of
# truth, shared with generate.py's Crossref fallback). parse_venue is imported
# from lib_common so the two scripts can never drift apart again.


# parse_venue is imported from lib_common (see import line above).


def arxiv_batch(ids):
    """Return {arxiv_id: (journal_ref, doi)} via batched id_list queries."""
    out = {}
    chunks = [ids[i:i + 25] for i in range(0, len(ids), 25)]
    for ch in chunks:
        q = urllib.parse.urlencode({"id_list": ",".join(ch), "max_results": len(ch)})
        for attempt in range(4):
            try:
                xml = http_get(f"https://export.arxiv.org/api/query?{q}",
                               headers=UA, retries=4)
                root = ET.fromstring(xml)
                for e in root.findall("a:entry", NS):
                    aid_url = e.findtext("a:id", "", NS) or ""
                    m = re.search(r"abs/(\d{4}\.\d{4,5})", aid_url)
                    if not m:
                        continue
                    jr = (e.findtext("ar:journal_ref", default="", namespaces=NS) or "").strip()
                    doi = (e.findtext("ar:doi", default="", namespaces=NS) or "").strip()
                    out[m.group(1)] = (jr, doi)
                break
            except TransientError:
                if attempt < 3:
                    time.sleep(5)
                    continue
                # leave missing for this chunk; will stay arXiv
        time.sleep(3)
    return out


def crossref_lookup(doi):
    """Resolve venue + year from a DOI via Crossref. Returns
    {venue, year} or None. Used as a fallback when arXiv journal_ref gave a
    DOI but no mappable venue name, and DBLP hasn't been queried yet."""
    url = "https://api.crossref.org/works/" + urllib.parse.quote(doi)
    try:
        data = json.loads(http_get(url, headers=UA, retries=3, timeout=30))
    except Exception:
        return None
    msg = data.get("message", {})
    ct = msg.get("container-title") or []
    ctitle = ct[0] if ct else ""
    venue, yr = parse_venue(ctitle)
    if not venue:
        for f in ("event", "book-title"):
            t = msg.get(f)
            if isinstance(t, list):
                t = t[0] if t else ""
            elif isinstance(t, dict):
                # Crossref may return a structured object instead of a string;
                # fall back to its title/name field.
                t = t.get("title") or t.get("name") or ""
            if not isinstance(t, str):
                t = ""
            if not t:
                continue
            v, y = parse_venue(t)
            if v:
                venue, yr = v, y
                break
    year = yr
    if not year:
        dp = msg.get("published", {}).get("date-parts", [[""]])
        try:
            year = int(dp[0][0]) if dp and dp[0] else None
        except Exception:
            year = None
    if not venue:
        return None
    return {"venue": venue, "year": year}


def dblp_lookup(title):
    """Return {venue, year, ee} for the first non-CoRR DBLP hit, else None.
    Raises TransientError on API failure (caller retries)."""
    clean_q = re.sub(r"[^\w\s]", " ", title)
    clean_q = re.sub(r"\s+", " ", clean_q).strip()
    q = urllib.parse.urlencode({"q": clean_q, "format": "json", "h": 10})
    data = json.loads(http_get(f"https://dblp.org/search/publ/api?{q}", retries=5))
    hits = data.get("result", {}).get("hits", {}).get("hit", []) or []
    key = norm(title)
    for h in hits:
        info = h.get("info", {})
        ht = re.sub(r"\.\s*$", "", info.get("title", ""))
        if SequenceMatcher(None, norm(ht), key).ratio() < 0.92:
            continue
        venue = info.get("venue", "")
        if isinstance(venue, list):
            venue = venue[0] if venue else ""
        if not venue or venue == "CoRR":   # skip the arXiv record
            continue
        ee = info.get("ee", "")
        if isinstance(ee, list):
            ee = ee[0] if ee else ""
        return {"venue": venue, "year": int(info.get("year", 0) or 0), "ee": ee}
    return None


def main():
    force = "--force" in sys.argv
    rest = [a for a in sys.argv[1:] if a != "--force"]
    limit = int(rest[0]) if rest else 10 ** 9
    papers = load_json(PAPERS).get("papers", [])
    ax = [p for p in papers if "arXiv" in (p.get("venue") or "")]
    cache = load_json(VENUE_LINKS)
    crossref = load_json(CROSSREF_CACHE)
    print(f"arXiv-preprint papers: {len(ax)}; already formal in cache: "
          f"{sum(1 for p in ax if cache.get(norm(p['title']))) }")

    # Pass A: fetch all arXiv journal_ref/doi in a few batched requests.
    ids = []
    id_to_key = {}
    for p in ax:
        m = re.search(r"(\d{4}\.\d{4,5})", p.get("url", "") or "")
        if m:
            ids.append(m.group(1))
            id_to_key[m.group(1)] = norm(p["title"])
    print(f"Pass A: fetching arXiv metadata for {len(ids)} ids (batched)...")
    jr_map = arxiv_batch(ids)
    print(f"Pass A: {sum(1 for v in jr_map.values() if v[0] or v[1])} papers have journal_ref/doi")

    todo = ax[:limit]
    found = 0
    # Circuit breaker: if DBLP keeps responding with transient errors (usually
    # HTTP 429 rate-limiting from the shared CI runner IP), stop hammering it and
    # let the run finish + push with whatever we have. Without this, a broad
    # 429 storm made the pipeline retry forever and the weekly job never pushed.
    consecutive_transient = 0
    DBLP_BREAK = 8
    dblp_shutoff = False
    for i, p in enumerate(todo, 1):
        title = p["title"]
        key = norm(title)
        # Incremental: a resolved venue never changes, and cached negatives
        # (preprints not yet formally published) are skipped unless --force
        # re-checks them. Only never-cached preprints are queried.
        if key in cache and (cache[key] or not force):
            continue
        rec = None
        src = ""

        # Pass A — journal_ref / doi
        m = re.search(r"(\d{4}\.\d{4,5})", p.get("url", "") or "")
        aid = m.group(1) if m else None
        jr, doi = jr_map.get(aid, ("", ""))
        has_ref = bool(jr or doi)
        if jr:
            venue, yr = parse_venue(jr)
            if venue:
                rec = {"venue": venue, "year": yr or p["year"],
                       "ee": (f"https://doi.org/{doi}" if doi else "")}
                src = "arxiv:jr"
        if not rec and doi:
            # Prefer cached Crossref container-title; otherwise query live and
            # cache the result (even a miss) so we don't re-hit the API forever.
            if doi in crossref:
                venue, yr = parse_venue(crossref[doi])
                if venue:
                    rec = {"venue": venue, "year": yr or p["year"],
                           "ee": f"https://doi.org/{doi}"}
                    src = "arxiv:doi+xref"
            else:
                cr = crossref_lookup(doi)
                if cr and cr.get("venue"):
                    rec = {"venue": cr["venue"],
                           "year": cr["year"] or p["year"],
                           "ee": f"https://doi.org/{doi}"}
                    src = "crossref"
                    crossref[doi] = (f"{cr['venue']} {cr['year']}"
                                     if cr.get("year") else cr["venue"])
                else:
                    crossref[doi] = ""

        # Pass B — DBLP title search
        transient = False
        if not rec:
            if dblp_shutoff:
                # DBLP is broadly rate-limiting this run; skip remaining DBLP
                # queries so the pipeline still completes and pushes. Papers we
                # skip here stay UNCACHED and are retried on the next run.
                pass
            else:
                for attempt in range(4):
                    try:
                        best = dblp_lookup(title)
                        if best:
                            rec = best
                            src = "dblp"
                        consecutive_transient = 0
                        break
                    except TransientError:
                        consecutive_transient += 1
                        if consecutive_transient >= DBLP_BREAK:
                            dblp_shutoff = True
                            print(f"  [dblp] rate-limited {consecutive_transient}x "
                                  f"consecutively; skipping remaining DBLP queries "
                                  f"this run (will retry next time).")
                            break
                        if attempt < 3:
                            time.sleep(5 * (attempt + 1))
                            continue
                        transient = True   # exhausted retries on a transient failure
                    except Exception:
                        break
                time.sleep(2)

        if rec:
            cache[key] = rec
            found += 1
            print(f"[{i}/{len(todo)}] {src:11s} {title[:40]:42s} -> "
                  f"{rec['venue']} {rec['year']}")
        elif not transient and not dblp_shutoff and not has_ref and (key not in cache or not cache.get(key)):
            # genuine negative (clean query, no formal venue, no journal_ref/doi)
            # -> cache "" so we don't re-query forever. Transient failures and
            # papers that HAVE a journal_ref/doi (but an unmapped venue) are left
            # UNCACHED, so a later run (or a VENUE_MATCH extension) can recover.
            # When DBLP was shut off by rate-limiting we also leave the paper
            # uncached, so it is retried next run instead of being permanently
            # marked negative.
            cache[key] = ""
    if i % 25 == 0:
        atomic_dump(VENUE_LINKS, cache, indent=1)
    atomic_dump(VENUE_LINKS, cache, indent=1)
    atomic_dump(CROSSREF_CACHE, crossref, indent=1)
    if dblp_shutoff:
        print("WARNING: DBLP was rate-limiting this run; remaining preprints "
              "were skipped and will be retried next run. The dataset is "
              "unchanged for venues, but the pipeline still completed.")
    print(f"Done. Newly resolved this run: {found}/{len(todo)}; "
          f"total formal among arXiv: "
          f"{sum(1 for p in ax if cache.get(norm(p['title']))) }")


if __name__ == "__main__":
    main()
