# -*- coding: utf-8 -*-
"""Multi-source code-link finder for academic papers.

WHY THIS WAS REWRITTEN
----------------------
The old finder searched GitHub for ``official <title>`` and accepted the top
non-generic repo. That approach has two fatal flaws:

  1. False negatives: official code repos are almost always named after the
     *method* (LLaVA, OPERA, VCD, HALC, WOAD...), not after the paper title.
     A title search simply never surfaces them.
  2. It leans entirely on GitHub title search and ignores the aggregators
     that replaced Papers-with-Code (which is effectively dead).

WHAT ACADEMIC CODE REPOS ACTUALLY LOOK LIKE (the signals we exploit)
--------------------------------------------------------------------
  * The authors paste the repo URL right in the ABSTRACT
        -> extract github/gitlab/bitbucket/hf links from the abstract text
  * They are named after the METHOD acronym           -> GitHub `in:name <acronym>`
  * The repo OWNER is the paper's first author        -> owner-handle == author
                                                         name (citers CANNOT fake this)
  * They are tagged with the method name on GitHub    -> GitHub TOPIC == acronym
  * They cite the paper's arXiv id in their README    -> GitHub `in:readme <id>`
  * They say "official implementation"                -> description signal
  * Aggregators already did the matching for us       -> Semantic Scholar `code`
  * Venue portals link the code officially            -> ACL Anthology "Software",
                                                         OpenReview "Code", Zenodo

  IMPORTANT -- why "arXiv id in SOURCE" is the WEAKEST signal, not the strongest:
  a toolbox/library hardcodes HUNDREDS of arXiv ids in its source (configs/,
  citations.py) and merely *cites* the paper; the real implementation often does
  NOT hardcode its own id in source at all (it lives in README/bibtex). So a
  code-search hit means "this repo mentions the paper somewhere", not "this repo
  implements it". We therefore treat code-search (and in:readme) hits as
  *candidates* that MUST be corroborated: the id must co-occur with the method
  identity (repo name / acronym / author), and citation-list repos (many arXiv
  ids, no method/author match) are rejected. See repo_score()/accept_candidate().

SOURCES (tried in priority order; every source is best-effort & resumable)
--------------------------------------------------------------------------
  1. Abstract links      -- zero network. Authors often write "Code:
     github.com/..." in the abstract. 184 papers in this corpus already do.
  2. Semantic Scholar `code` -- the canonical Papers-with-Code successor.
     Curated, ships `isOfficial` + `repositoryStars`. Needs S2_API_KEY for
     volume, but works unauthenticated at a low rate (skipped on rate-limit).
  3. GitHub `in:readme <arxiv_id>` -- strong, precise signal. We score every
     candidate by overlap of distinctive title tokens / method acronym with
     the repo name+description, and pick the best non-noise repo. This is what
     makes `in:readme <id>` usable: a survey repo that merely *cites* the paper
     scores ~0 and is rejected, while the real implementation scores high.
  4. GitHub `in:name <acronym>` -- when the title carries a method acronym
     (e.g. "LLaVA: ..."), the repo is usually named exactly that. Very precise.
  5. GitHub CODE search `<arxiv_id>` -- repos whose SOURCE contains the arXiv
     id. Token-gated (code search requires auth). This is the WEAKEST signal
     (a toolbox cites the id in source); we only accept a hit if it ALSO
     corroborates as the implementation (method in repo name / author in owner
     / id present in README with method-or-author identity). See gh_code_search.
  6. ACL Anthology "Software" -- only for papers whose DOI is 10.18653/v1/<id>;
     the anthology page links the official code. No auth needed.
  7. OpenReview "Code" -- only for papers whose URL is openreview.net/forum?id=;
     the forum page carries an official Code link. No auth needed.
  8. Zenodo software records -- last-resort; software archives referenced by
     the arXiv id / DOI. No auth needed.
  9. GitHub `official <title>` / `"title"` -- last-resort title fallback, now
     with the same overlap validation (previously it accepted any top repo).

CACHE
-----
data/code_links.json, keyed by arXiv id when available (unambiguous) else by
norm_title. Negative results are cached too ("") so re-runs skip them.
generate.py looks up `code_links.get(arxiv_id(url)) or code_links.get(norm_title(title))`,
so both key styles resolve and the 100+ legacy norm_title entries are preserved.

USAGE
-----
  python scripts/fetch_code.py                  # fill in missing code links
  python scripts/fetch_code.py --limit 40       # smoke test on first 40 missing
  python scripts/fetch_code.py --force          # ignore cache, re-search all
  GITHUB_TOKEN=xxx S2_API_KEY=yyy python scripts/fetch_code.py   # full, fast
Then:  python scripts/generate.py
"""
import argparse
import base64
import json
import os
import re
import ssl
import sys
import time
import urllib.error
import urllib.parse
import urllib.request

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from code_common import (DATA, norm_title, load_papers, load_json, save_json,
                         http_get, _SSL, TransientError)
from lib_common import arxiv_id as arxiv_id_of

OUT = os.path.join(DATA, "code_links.json")
ABSTRACTS_CACHE = os.path.join(DATA, "abstracts.json")        # arxiv-id -> {abstract}
ABSTRACTS_EXTRA = os.path.join(DATA, "abstracts_extra.json")  # norm_title -> abstract

# Stopwords for distinctive-token extraction (title words that don't identify a
# paper: "hallucination" is deliberately KEPT because it's the corpus theme and
# still discriminates repos, but generic glue words are dropped).
STOP = set("""
a an the of for to in on and with using via from is are be by we our
towards toward against into over under between within without can may
does not no yes it its their this that these those as at was were
have has had do does than then so such if while about across per
new novel towards study approach method based improved effective
""".split())

# Repo-name fragments that mark a NON-code (meta) repository. A repo is noise
# unless the paper itself is a survey/dataset (then these names are expected).
NOISE_REPO = ("awesome", "survey", "surveys", "list", "lists", "tutorial",
              "tutorials", "benchmarks", "benchmark", "dataset", "datasets",
              "paper-list", "awesome-list", "paper-list", "reading",
              "readings", "collection", "collections", "summary", "summaries",
              "zoo", "implementations", "papers", "notes", "slides")

# Lazily-loaded abstract caches (fetch_abstracts / fetch_abstracts_web refresh
# these AFTER generate#1, so we read the files directly rather than papers.json).
_abs_cache = None
_abs_extra = None


def _load_abstracts():
    global _abs_cache, _abs_extra
    if _abs_cache is None:
        _abs_cache = load_json(ABSTRACTS_CACHE, {})
        _abs_extra = load_json(ABSTRACTS_EXTRA, {})
    return _abs_cache, _abs_extra


def distinctive(title):
    """Distinctive lower-cased word tokens (len>=4) of a title, stopwords removed.

    NOTE: we tokenize the ORIGINAL title, not norm_title() -- norm_title() strips
    spaces and would collapse the whole title into a single un-matchable blob,
    defeating the token-overlap scoring below.
    """
    return set(w for w in re.findall(r"[a-z0-9]+", (title or "").lower())
               if len(w) >= 4 and w not in STOP)


def acronym_of(title):
    """Leading method acronym like 'HALC', 'OPERA', 'VCD' if the title has one."""
    m = re.match(r"^([A-Z][A-Za-z0-9\-]{2,15}):", title.strip())
    return m.group(1) if m else None


def is_noise(name):
    n = (name or "").lower()
    return any(w in n for w in NOISE_REPO)


def doi_of(url):
    m = re.search(r"doi\.org/(10\.[^\s)]+)", url or "")
    return m.group(1) if m else None


def acl_id_of(url):
    """ACL Anthology ID from a 10.18653/v1/<id> DOI, else None."""
    m = re.search(r"10\.18653/v1/([A-Za-z0-9.\-]+)", url or "")
    return m.group(1) if m else None


def openreview_id_of(url):
    """OpenReview forum id from an openreview.net/forum?id=<id> URL, else None."""
    m = re.search(r"openreview\.net/forum\?id=([A-Za-z0-9]+)", url or "")
    return m.group(1) if m else None


# ------------------------------------------------ URL extraction helpers
_CODE_HOST_RE = re.compile(
    r"https?://(?:github|gitlab|bitbucket)\.com/[A-Za-z0-9_\-]+/[A-Za-z0-9_\-\.]+")
_HF_RE = re.compile(r"https?://huggingface\.com/[A-Za-z0-9_\-]+/[A-Za-z0-9_\-\.]+")


def _repo_root(u):
    """Strip trailing punctuation and tree/blob/raw/wiki suffixes -> repo root."""
    u = u.rstrip(".,;:)\"']")
    return re.sub(r"/(tree|blob|raw|wiki)/.*$", "", u)


def gh_url_in_text(text):
    """All plausible code-repo URLs found in free text (github/gitlab/bitbucket/
    huggingface), deduplicated, reduced to repo root. Order preserved."""
    out = []
    seen = set()
    for m in _CODE_HOST_RE.finditer(text or ""):
        u = _repo_root(m.group(0))
        if u not in seen:
            seen.add(u)
            out.append(u)
    for m in _HF_RE.finditer(text or ""):
        u = _repo_root(m.group(0))
        if u not in seen:
            seen.add(u)
            out.append(u)
    return out


def gh_urls_from_html(html, exclude_orgs=("acl-org",)):
    """GitHub URLs on an HTML page, with a flag marking links whose anchor text
    is 'Code' (the official code link on ACL Anthology / OpenReview portals).

    Repos owned by ``exclude_orgs`` (e.g. acl-org/acl-anthology footer) are
    dropped. Returns [(url, is_code_labeled), ...], deduplicated, repo-root."""
    out = []
    seen = set()
    for m in re.finditer(r"https?://github\.com/[A-Za-z0-9_\-]+/[A-Za-z0-9_\-\.]+",
                         html or ""):
        u = _repo_root(m.group(0))
        if u in seen:
            continue
        owner = u.split("/")[-2]
        if owner in exclude_orgs:
            continue
        after = html[m.end():m.end() + 60]
        code_label = bool(re.search(r"^[^<]*>\s*Code\s*<", after, re.I))
        seen.add(u)
        out.append((u, code_label))
    return out


def abstract_links(p):
    """Best code URL pasted inside the paper's abstract (zero network).

    Reads the abstract caches directly (arXiv abstracts keyed by arxiv id,
    web/extra abstracts keyed by norm_title) plus the in-paper abstract. If the
    abstract mentions several repos we prefer one whose name contains the
    method acronym; otherwise the first GitHub link (authors list their own
    implementation first).
    """
    _load_abstracts()
    aid = arxiv_id_of(p.get("url", ""))
    title = p.get("title", "")
    key = norm_title(title)
    text = ""
    if aid and aid in _abs_cache:
        text = (_abs_cache[aid].get("abstract") if isinstance(_abs_cache.get(aid), dict)
                else _abs_cache.get(aid, "")) or ""
    if not text:
        extra = _abs_extra.get(key)
        text = (extra.get("abstract") if isinstance(extra, dict) else extra) or ""
    if not text:
        text = p.get("abstract", "") or ""
    urls = gh_url_in_text(text)
    if not urls:
        return None
    acr = acronym_of(title)
    if acr:
        for u in urls:
            if acr.lower() in u.lower():
                return u
    return urls[0]


def author_tokens(authors):
    """Lower-cased author-name tokens (len>=3) of a paper, 'et al.' stripped.

    e.g. "Haotian Liu et al." -> {"haotian","liu"}; "Liu, Haotian" -> {"liu",
    "haotian"}. These are matched against the GitHub repo OWNER handle and the
    repo README/bibtex to tell an implementation apart from a citer.
    """
    if not authors:
        return set()
    s = re.sub(r"et al\.?", "", authors, flags=re.I)
    s = re.sub(r"[^A-Za-zÀ-ɏ\s\-]", " ", s)
    toks = {t.lower() for t in re.findall(r"[A-Za-zÀ-ɏ][A-Za-zÀ-ɏ'\-]+", s)}
    return {t for t in toks if len(t) >= 3}


def owner_login(repo):
    """Lower-cased GitHub owner login for a repo dict."""
    o = repo.get("owner") or {}
    if isinstance(o, dict):
        return (o.get("login") or "").lower()
    fn = repo.get("full_name") or repo.get("html_url") or ""
    m = re.search(r"github\.com/([A-Za-z0-9_\-]+)/", fn)
    return m.group(1).lower() if m else ""


_README_CACHE = {}


def fetch_readme(repo):
    """Lower-cased README text of a repo (best-effort, cached per run).

    Uses the raw media type first; falls back to base64 JSON. Returns "" on
    any failure (rate-limit / no README / encoding error).
    """
    key = repo.get("full_name") or owner_login(repo)
    if key in _README_CACHE:
        return _README_CACHE[key]
    _README_CACHE[key] = ""  # guard against re-entrancy / repeat failures
    url = f"https://api.github.com/repos/{key}/readme"
    try:
        txt = http_get(url, {"Accept": "application/vnd.github.raw"}, timeout=25)
        _README_CACHE[key] = (txt or "").lower()
        return _README_CACHE[key]
    except Exception:  # noqa: BLE001
        pass
    try:
        d = json.loads(http_get(url, {"Accept": "application/vnd.github+json"},
                                 timeout=25))
        c = d.get("content", "")
        if c:
            _README_CACHE[key] = base64.b64decode(c).decode("utf-8", "ignore").lower()
    except Exception:  # noqa: BLE001
        pass
    return _README_CACHE[key]


def readme_corroborates(repo, p, aid):
    """Does the repo's README prove it implements THIS paper (not just cites it)?

    Acceptance requires the arXiv id to appear in the README (so a bare source
    citation does NOT count) AND at least one identity signal:
      * the method acronym appears in the README, OR
      * a paper-author name appears in the README, OR
      * >=2 distinctive title words appear in the README.
    Rejects citation-list / toolbox repos: a README that mentions MANY arXiv ids
    but none of the method name / authors is almost certainly a survey or a
    "papers we used" list, not the implementation.
    """
    text = fetch_readme(repo)
    if not text:
        return False
    if aid and aid not in text:
        return False  # id must be in README, not only in source files
    acr = acronym_of(p.get("title", ""))
    title_tokens = distinctive(p.get("title", ""))
    author_toks = author_tokens(p.get("authors", ""))
    acr_in = bool(acr and acr.lower() in re.findall(r"[a-z0-9\-]+", text))
    tok_overlap = len(title_tokens & set(re.findall(r"[a-z0-9]+", text)))
    auth_in = any(t in text for t in author_toks)
    n_ids = len(re.findall(r"\d{4}\.\d{4,5}", text))
    if n_ids >= 8 and not (acr_in or auth_in):
        return False  # citation list / toolbox
    return bool(acr_in or auth_in or tok_overlap >= 2)


def repo_score(repo, p):
    """Cheap (no README fetch) confidence score for a candidate repo.

    Layered, strongest first; a citer/survey repo scores ~0:
      1000  method acronym is a whole token in the REPO NAME
              (official impls are named after the method; e.g. OPERA, VCD)
       600  first-author lastname is a substring of the repo OWNER handle
              (citers cannot fake this -- MiniGPT-4 is owned by vision-cair,
               not by LLaVA's author haotian)
      3/tok  >=2 distinctive title words overlap name+description
         5  description says "official"
    """
    name = (repo.get("name") or "").lower()
    name_tokens = set(re.findall(r"[a-z0-9]+", name))
    desc = (repo.get("description") or "").lower()
    acr = acronym_of(p.get("title", ""))
    title_tokens = distinctive(p.get("title", ""))
    author_toks = author_tokens(p.get("authors", ""))
    owner = owner_login(repo)
    s = 0
    if acr:
        a = acr.lower()
        parts = a.split("-")
        # acronym may be hyphenated (Med-VCD, CoDA-official): every hyphen part
        # must appear as a repo-name token, or the full slug is a token.
        if all(part in name_tokens for part in parts) or a in name_tokens:
            s += 1000
    if any(t in owner for t in author_toks if len(t) >= 3):
        s += 600
    toks = set(re.findall(r"[a-z0-9]+", name + " " + desc))
    overlap = len(title_tokens & toks)
    if overlap >= 2:
        s += overlap * 3
    if "official" in desc:
        s += 5
    return s


def accept_candidate(repo, p, aid):
    """Gate a GitHub candidate: is it THE implementation, not a citer?

    Strong signals (acronym-in-name, author-in-owner) are trusted immediately.
    Mid-scoring candidates must be corroborated by their README. Weak/no-signal
    candidates are rejected.
    """
    s = repo_score(repo, p)
    if s >= 600:
        return True
    if s >= 6:
        return readme_corroborates(repo, p, aid)
    return False


def gh_headers():
    tok = os.environ.get("GITHUB_TOKEN")
    h = {"Accept": "application/vnd.github+json"}
    if tok:
        h["Authorization"] = f"Bearer {tok}"
    return h


def gh_search(q, per_page=30, sort="stars"):
    """GitHub repository search. Returns list of repo dicts (best-effort).

    ``sort`` is "stars" for acronym/topic searches (popular == real impl), but
    None for arxiv-id searches so the impl (which mentions the id prominently)
    is not pushed below toolboxes that merely cite it.
    """
    url = ("https://api.github.com/search/repositories?q="
           + urllib.parse.quote(q) + f"&per_page={per_page}")
    if sort:
        url += f"&sort={sort}"
    try:
        j = json.loads(http_get(url, gh_headers(), timeout=30))
    except (TransientError, Exception):  # noqa: BLE001
        return []
    return j.get("items", []) or []


def best_repo(items, p, aid, allow_noise=False):
    """Pick the highest-confidenced repo that passes accept_candidate().

    Rejects noise (survey/awesome/zoo) repos unless ``allow_noise``, and only
    keeps repos that corroborate as the implementation (see accept_candidate).
    """
    scored = []
    for it in items:
        if (not allow_noise) and is_noise(it.get("name")):
            continue
        if not accept_candidate(it, p, aid):
            continue
        scored.append((repo_score(it, p), it.get("stargazers_count") or 0, it))
    if not scored:
        return None
    scored.sort(key=lambda x: (x[0], x[1]), reverse=True)
    return scored[0][2]


def gh_code_search(aid, p):
    """GitHub CODE search: repos whose SOURCE contains the arXiv id.

    This is the WEAKEST signal -- a toolbox hardcodes the id in a citations
    file, and the real implementation often does NOT. So every hit is treated as
    a candidate that MUST corroborate: we only return it if accept_candidate()
    passes (method in repo name, author in owner, or the id appears in the
    README together with the method/author identity). A bare source citation is
    rejected. Requires GITHUB_TOKEN (anonymous code search is forbidden).
    """
    if not aid or not os.environ.get("GITHUB_TOKEN"):
        return None
    q = urllib.parse.quote(f"{aid} in:file language:Python")
    url = f"https://api.github.com/search/code?q={q}&per_page=20"
    try:
        j = json.loads(http_get(url, gh_headers(), timeout=30))
    except (TransientError, Exception):  # noqa: BLE001
        return None
    repos = [it.get("repository") for it in (j.get("items") or []) if it.get("repository")]
    repo = best_repo(repos, p, aid)
    return repo.get("html_url") if repo else None


def gh_topic_search(acr, p):
    """GitHub TOPIC search: community-tagged official repos (precise).

    Official implementation repos are almost always tagged with the method
    acronym as a GitHub topic. We only accept a topic hit if it also corroborates
    (acronym in name, author in owner, or README identity).
    """
    if not acr:
        return None
    items = gh_search(f"topic:{acr}")
    repo = best_repo(items, p, arxiv_id_of(p.get("url", "")))
    return repo.get("html_url") if repo else None


def s2_code(s2id, key):
    """Semantic Scholar `code` field (gold). Returns url or None.

    Unauthenticated S2 is hard rate-limited (429) and would stall a bulk
    crawl, so without S2_API_KEY we make a single short attempt and move on.
    With a key the limit rises sharply and a second attempt is worthwhile.
    """
    if not s2id:
        return None
    url = (f"https://api.semanticscholar.org/graph/v1/paper/{s2id}"
           f"?fields=code")
    h = {"Accept": "application/json"}
    if key:
        h["x-api-key"] = key
    attempts = 2 if key else 1
    for attempt in range(attempts):
        try:
            req = urllib.request.Request(url, headers=h)
            with urllib.request.urlopen(req, timeout=20, context=_SSL) as r:
                data = json.loads(r.read().decode("utf-8", "ignore"))
        except urllib.error.HTTPError as e:
            if e.code == 429:
                time.sleep(2)
                continue
            return None
        except Exception:  # noqa: BLE001
            return None
        code = [c for c in (data.get("code") or []) if c.get("url")]
        if code:
            code.sort(key=lambda c: (not c.get("isOfficial"),
                                      -(c.get("repositoryStars") or 0)))
            return code[0]["url"]
        return None
    return None


def acl_code(url):
    """ACL Anthology official 'Software' link for a paper with a 10.18653/v1 DOI."""
    aid = acl_id_of(url)
    if not aid:
        return None
    try:
        html = http_get(f"https://aclanthology.org/{aid}/",
                        headers={"User-Agent": "Mozilla/5.0"}, timeout=30)
    except (TransientError, Exception):  # noqa: BLE001
        return None
    urls = gh_urls_from_html(html)
    if not urls:
        return None
    labeled = [u for u, c in urls if c]
    return (labeled[0] if labeled else urls[0][0])


def openreview_code(url):
    """OpenReview official 'Code' link for a paper with an openreview forum URL."""
    fid = openreview_id_of(url)
    if not fid:
        return None
    try:
        html = http_get(f"https://openreview.net/forum?id={fid}",
                        headers={"User-Agent": "Mozilla/5.0"}, timeout=30)
    except (TransientError, Exception):  # noqa: BLE001
        return None
    urls = gh_urls_from_html(html)
    if not urls:
        return None
    labeled = [u for u, c in urls if c]
    return (labeled[0] if labeled else urls[0][0])


def zenodo_code(aid, doi):
    """Zenodo software archive referenced by the arXiv id / DOI (last resort)."""
    q = doi or (f"arXiv:{aid}" if aid else None)
    if not q:
        return None
    url = (f"https://zenodo.org/api/records?q={urllib.parse.quote(q)}"
           f"&size=5&type=software")
    try:
        j = json.loads(http_get(url, timeout=30))
    except (TransientError, Exception):  # noqa: BLE001
        return None
    for h in (j.get("hits", {}).get("hits") or []):
        for r in (h.get("metadata", {}).get("related_identifiers") or []):
            ident = r.get("identifier") or ""
            if "github.com" in ident:
                return _repo_root(ident)
    return None


def find_code(p):
    """Return a code URL for paper ``p`` using all sources, or None.

    Precedence puts the PRECISE, hard-to-fake signals first (method name in
    repo name, author in owner handle, GitHub topic), then the corroborated
    arxiv-id signals (README / code search), then venue portals, then a
    validated title fallback. Every GitHub signal is gated by accept_candidate().
    """
    title = p.get("title", "")
    url = p.get("url", "")
    aid = arxiv_id_of(url)
    acr = acronym_of(title)
    s2key = os.environ.get("S2_API_KEY", "")

    # 1) GitHub/GitLab link pasted in the abstract (zero network)
    u = abstract_links(p)
    if u:
        return u

    # 2) Semantic Scholar -- gold, when reachable
    s2id = (f"arXiv:{aid}" if aid else None) or (f"DOI:{doi_of(url)}" if doi_of(url) else None)
    if s2id:
        u = s2_code(s2id, s2key)
        if u:
            return u

    # 3) GitHub: method acronym in repo NAME (precise, no README needed)
    if acr and acr.upper() not in {"MLLM", "LLM", "LVLM", "VLM"}:
        items = gh_search(f"{acr} in:name,description")
        repo = best_repo(items, p, aid)
        if repo:
            return repo.get("html_url")

    # 4) GitHub TOPIC == acronym (community-tagged official repo, precise)
    if acr and acr.upper() not in {"MLLM", "LLM", "LVLM", "VLM"}:
        u = gh_topic_search(acr, p)
        if u:
            return u

    # 5) GitHub: arXiv id in README, corroborated (rejects toolboxes that
    #    merely cite the paper). sort=None so the impl isn't buried under
    #    high-star citing repos.
    if aid:
        items = gh_search(f"{aid} in:readme", sort=None)
        repo = best_repo(items, p, aid)
        if repo:
            return repo.get("html_url")

    # 6) GitHub CODE search: arXiv id in SOURCE -- only if corroborated
    #    (weakest signal; a toolbox cites the id in source).
    if aid:
        u = gh_code_search(aid, p)
        if u:
            return u

    # 7) Venue portals -- only when the paper is from that venue
    u = acl_code(url)
    if u:
        return u
    u = openreview_code(url)
    if u:
        return u

    # 8) Zenodo software archive (last resort)
    u = zenodo_code(aid, doi_of(url))
    if u:
        return u

    # 9) GitHub: title fallback (validated: must corroborate)
    for q in (f'official {title}', f'"{title}"'):
        items = gh_search(q)
        repo = best_repo(items, p, aid)
        if repo:
            return repo.get("html_url")
    return None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--limit", type=int, default=0)
    ap.add_argument("--force", action="store_true")
    args = ap.parse_args()

    papers = load_papers()
    final = load_json(OUT, {})

    def has_code(k):
        return bool(final.get(k))

    targets = []
    for p in papers:
        key = arxiv_id_of(p.get("url", "")) or norm_title(p["title"])
        if args.force or not has_code(key):
            targets.append(p)
    if args.limit:
        targets = targets[:args.limit]

    token = bool(os.environ.get("GITHUB_TOKEN"))
    delay = 7 if not token else 1.2  # unauthenticated GitHub search: 10/min
    print(f"[code] probing {len(targets)} papers (github_token="
          f"{'yes' if token else 'no'}, s2_key="
          f"{'yes' if os.environ.get('S2_API_KEY') else 'no'})")

    found = 0
    for i, p in enumerate(targets, 1):
        key = arxiv_id_of(p.get("url", "")) or norm_title(p["title"])
        title = p["title"]
        try:
            url = find_code(p)
        except Exception as e:  # noqa: BLE001
            url = None
            print(f"  {i}/{len(targets)} ERR {e}", file=sys.stderr)
        final[key] = url or ""  # cache negatives too
        if url:
            found += 1
            print(f"  {i}/{len(targets)} + {url}  <- {title[:50]}")
        else:
            print(f"  {i}/{len(targets)} . {title[:50]}")
        save_json(OUT, final)  # incremental, resumable
        if i < len(targets):
            time.sleep(delay)

    print(f"[code] done. +{found} new links this run; code_links.json now has "
          f"{sum(1 for v in final.values() if v)} entries. "
          f"Run: python scripts/generate.py")


if __name__ == "__main__":
    main()
