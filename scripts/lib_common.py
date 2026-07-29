# -*- coding: utf-8 -*-
"""Shared, single-source-of-truth helpers for the hallucination DB pipeline.

Historically `norm_title` / `arxiv_id` were copy-pasted across ~9 scripts with
slight drift (some with a `(t or "")` guard, some without). That caused subtle
"keep in sync" bugs. They now live here and every script imports them.
"""
import re
import os
import json
import datetime

# Matches an arXiv abs/pdf id, e.g. "2401.01234" or "2401.01234v2".
_ARXIV_ID_RE = re.compile(r"arxiv\.org/abs/(\d{4}\.\d{4,5})")


def norm_title(t):
    """Normalize a title/venue key: lowercase + strip everything non-alphanumeric.

    Safe for None/empty (returns ""). The guard makes it strictly more robust
    than the old unguarded copies while producing identical output for the
    string inputs every caller actually passes.
    """
    return re.sub(r"[^a-z0-9]", "", (t or "").lower())


def arxiv_id(url):
    """Extract the arXiv id (e.g. "2401.01234") from an abs/pdf url, else None."""
    m = _ARXIV_ID_RE.search(url or "")
    return m.group(1) if m else None


# ---------------------------------------------------------------------------
# Single source of truth for venue resolution.
#
# Historically `update_arxiv_venues.py` (VENUE_MATCH) and `generate.py`
# (_XREF_VENUE) kept two separate venue->regex tables that drifted apart:
# VENUE_MATCH missed TASLP/TNNLS/TAI while _XREF_VENUE missed WACV/TMLR, so the
# same DOI resolved to DIFFERENT venues (and thus different CCF ratings)
# depending on which script ran. Both now import this list.
# Patterns kept detailed (canonical-name + short-code) so they match both
# Crossref container-titles and arXiv journal_ref free text.
# ---------------------------------------------------------------------------
VENUE_PATTERNS = [
    ("EMNLP", r"Empirical Methods in Natural Language Processing|EMNLP|findings-emnlp|emnlp-main"),
    ("ACL", r"Annual Meeting of the Association for Computational Linguistics|Proceedings of the ACL|acl-long|acl-main"),
    ("NAACL", r"North American Chapter.*Computational Linguistics|NAACL|naacl-long|naacl-main"),
    ("COLING", r"International Conference on Computational Linguistics|COLING"),
    ("EACL", r"European Chapter.*Computational Linguistics|EACL|eacl-main|findings-eacl"),
    ("AAAI", r"AAAI Conference on Artificial Intelligence|AAAI|aaai\.v"),
    ("IJCAI", r"International Joint Conference on Artificial Intelligence|IJCAI"),
    ("NeurIPS", r"NeurIPS|Neural Information Processing Systems"),
    ("ICML", r"International Conference on Machine Learning|ICML|icicml"),
    ("ICLR", r"International Conference on Learning Representations|ICLR"),
    ("CVPR", r"Computer Vision and Pattern Recognition|CVPR"),
    ("ICCV", r"International Conference on Computer Vision|ICCV"),
    ("ECCV", r"European Conference on Computer Vision|ECCV"),
    ("WACV", r"winter conference on applications of computer vision|wacv"),
    ("ACM MM", r"ACM Multimedia|International Conference on Multimedia"),
    ("SIGIR", r"SIGIR"),
    ("KDD", r"ACM SIGKDD|Knowledge Discovery and Data Mining|KDD"),
    ("WWW", r"The Web Conference|World Wide Web Conference|ACM Web Conference|WWW"),
    ("TPAMI", r"IEEE Transactions on Pattern Analysis and Machine Intelligence"),
    ("TIP", r"IEEE Transactions on Image Processing|TIP"),
    ("TMM", r"IEEE Transactions on Multimedia|TMM"),
    ("IJCV", r"International Journal of Computer Vision|IJCV"),
    ("TASLP", r"IEEE(/ACM)? Transactions on Audio"),
    ("TNNLS", r"IEEE Transactions on Neural Networks and Learning Systems"),
    ("TAI", r"IEEE Transactions on Artificial Intelligence"),
    ("INTERSPEECH", r"INTERSPEECH"),
    ("ICASSP", r"ICASSP"),
    ("TACL", r"Transactions of the Association for Computational Linguistics"),
    ("Comput. Linguistics", r"Computational Linguistics"),
    ("JMLR", r"Journal of Machine Learning Research"),
    ("TMLR", r"transactions on machine learning research|TMLR"),
]


def parse_venue(text):
    """Resolve (venue, year) from a free-text journal_ref / container-title.

    Returns (venue, year) where year is the latest plausible 4-digit year in
    the text (clamped to [1990, this_year+1] so future-dated papers are not
    silently dropped). Returns (None, year) when no known venue matches.
    """
    if not text:
        return None, None
    yr = None
    cur = datetime.date.today().year
    for m in re.finditer(r"(19|20)\d{2}", text):
        y = int(m.group(0))
        if 1990 <= y <= cur + 1:
            if yr is None or y > yr:
                yr = y
    for venue, pat in VENUE_PATTERNS:
        if re.search(pat, text, re.I):
            return venue, yr
    return None, yr


def atomic_dump(path, obj, indent=None):
    """Write JSON atomically: serialize to a temp file, then os.replace onto the
    target. Guarantees readers never see a half-written file (protects the
    published docs/papers.json and cumulative caches like venue_links.json /
    incremental.json from truncation if the process is killed mid-write).

    ``indent=None`` emits compact JSON (separators ``,``/``:``) — the format
    generate.py uses for its web artifacts; any other value pretty-prints
    (save_json uses indent=1).
    """
    import tempfile
    d = os.path.dirname(path)
    if d:
        os.makedirs(d, exist_ok=True)
    fd, tmp = tempfile.mkstemp(dir=d or ".", suffix=".tmp")
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as f:
            if indent is None:
                json.dump(obj, f, ensure_ascii=False, separators=(",", ":"))
            else:
                json.dump(obj, f, ensure_ascii=False, indent=indent)
        os.replace(tmp, path)
    except BaseException:
        try:
            os.unlink(tmp)
        except OSError:
            pass
        raise


# ---------------------------------------------------------------------------
# Single source of truth for localized venue labels.
#
# The data layer (data/papers.json, docs/papers.json, app.js) keeps the canonical
# Chinese keys below so the on-disk data is stable and language-neutral. The two
# README generators (generate.py and gen_readme.py) call vlabel() so the English
# README renders English labels and the Chinese README keeps Chinese — no language
# ever mixes inside one file.
# ---------------------------------------------------------------------------
VENUE_DISPLAY = {
    "未标注": ("Unlabeled", "未标注"),
    "arXiv（预印本）": ("arXiv (preprint)", "arXiv（预印本）"),
    "其他": ("Other", "其他"),
    "未收录": ("Not in CCF", "未收录"),
}


def vlabel(key, lang="en"):
    """Return the display label for a canonical venue key in `lang` (en / zh)."""
    pair = VENUE_DISPLAY.get(key)
    if not pair:
        return key
    return pair[0] if lang == "en" else pair[1]
