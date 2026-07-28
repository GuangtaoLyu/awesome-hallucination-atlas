"""Shared helpers for the code-link crawlers.

Key invariant: every crawler keys its output by ``norm_title(title)`` so that
``generate.py`` (which does ``code_links.get(norm_title(title), "")``) can read it
directly. ``normale_title`` is imported from ``lib_common`` (single source of truth).
"""
import json
import os
import re
import ssl
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from difflib import SequenceMatcher

# SECURITY: we verify TLS certificates by default (the standard, safe
# behaviour). arXiv / ACL Anthology / OpenReview / GitHub / CVF all present
# certificates that chain to the system CA bundle, so disabling verification
# was an unjustified MITM risk. If a specific crawl host ever serves a
# certificate that does NOT chain to the system bundle, handle it at the call
# site by passing a custom context — never disable verification process-wide.
_SSL = ssl.create_default_context()

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PAPERS = os.path.join(ROOT, "data", "papers.json")
DATA = os.path.join(ROOT, "data")


from lib_common import norm_title, atomic_dump  # noqa: E402  (re-exported for backward compat)


def load_json(path, default=None):
    if os.path.exists(path):
        with open(path, encoding="utf-8") as f:
            return json.load(f)
    return default if default is not None else {}


def save_json(path, obj):
    # Atomic + crash-safe (a killed process never truncates the cumulative
    # code-link / abstract caches). indent=1 keeps them human-diffable.
    atomic_dump(path, obj, indent=1)


def load_papers():
    with open(PAPERS, encoding="utf-8") as f:
        d = json.load(f)
    return d.get("papers", d) if isinstance(d, dict) else d


def title_sim(a, b):
    return SequenceMatcher(None, norm_title(a), norm_title(b)).ratio()


class TransientError(Exception):
    """Raised when a network request fails after all retries (5xx / 429 /
    timeout). Callers may catch it to skip/retry a single item without
    aborting the whole crawl.
    """
    pass


def http_get(url, headers=None, timeout=30, retries=5, backoff=6):
    """GET with retry + 429/503 exponential backoff. Returns decoded text.

    On persistent failure (incl. exhausted rate-limit retries) raises
    TransientError so callers can distinguish transient network errors from
    permanent ones (e.g. a 404).
    """
    h = {"User-Agent": "halu-code-crawler/1.0", **(headers or {})}
    last = None
    for i in range(retries):
        try:
            req = urllib.request.Request(url, headers=h)
            with urllib.request.urlopen(req, timeout=timeout, context=_SSL) as r:
                return r.read().decode("utf-8", "ignore")
        except urllib.error.HTTPError as e:
            last = e
            if e.code in (403, 429, 503):
                # fail fast on rate-limit so a bulk crawl doesn't stall:
                # at most 2 extra retries, honour Retry-After if present,
                # then give up.
                if i < 2:
                    wait = (i + 1) * 5
                    ra = getattr(e, "headers", None)
                    if ra:
                        try:
                            ra_val = ra.get("Retry-After")
                            if ra_val and str(ra_val).isdigit():
                                wait = min(120, int(ra_val))
                        except Exception:
                            pass
                    print(f"    [HTTP {e.code}] rate limited, sleep {wait}s ...",
                          file=sys.stderr)
                    time.sleep(wait)
                    continue
                raise TransientError(f"rate limited: HTTP {e.code}")
            else:
                raise
        except Exception as e:  # noqa: BLE001
            last = e
            time.sleep(backoff)
    raise TransientError(f"persistent failure after {retries} attempts: {last}")
