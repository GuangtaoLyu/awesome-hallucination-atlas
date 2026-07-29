# -*- coding: utf-8 -*-
"""
Generate structured papers.json + README.md from data/seed.json (via raw_data shim).

Classification pipeline (abstract-based):
  1. fetch_abstracts.py caches real arXiv abstracts in data/abstracts.json
  2. classification uses TITLE + ABSTRACT text (falls back to title-only
     when no abstract is available).

Dimensions:
  - model_type:  LLM | VLM | MLLM (Omni)
  - method_type: Training-free | Training-based
  - benchmark:   separate boolean flag -> adds the "Benchmark" tag
  - survey:      separate boolean flag -> adds the "Survey" tag
  - tags:        Benchmark | Survey | Relation | Attribute | Video | Audio |
                 Multilingual | Medical | 3D | Agent
  - venue / year
"""
import json
import re
import os
import sys
from datetime import datetime, timezone
from collections import Counter
from raw_data import RAW

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
ABS_CACHE = os.path.join(ROOT, "data", "abstracts.json")
FOUND_LINKS = os.path.join(ROOT, "data", "found_links.json")   # title-key -> arxiv url (searched)
CODE_LINKS = os.path.join(ROOT, "data", "code_links.json")     # title-key -> github url
VENUE_LINKS = os.path.join(ROOT, "data", "venue_links.json")   # title-key -> {venue, year, ee}
CCF_FILE = os.path.join(ROOT, "data", "ccf.json")             # venue base -> CCF rating A/B/C/""
CROSSREF_CACHE = os.path.join(ROOT, "data", "crossref_cache.json")  # DOI -> Crossref container-title

CCF = {}   # populated in main(); venue base -> "A"/"B"/"C"/"" ("" = 未收录)

# Secondary / co-located venues (workshops, satellite editions, bridge programs,
# companion tracks) that clutter the venue distribution. They are collapsed into
# "其他" so the main table stays readable. NAACL-HLT is the same conference as
# NAACL and is merged into it instead.
SECONDARY_VENUES = {
    "SemEval@NAACL", "SemEval@ACL", "SIGIR-AP", "AAAI Bridge Program",
    "COLING Workshops", "ECCV Workshops", "CVPRW", "ICCVW", "LREC/COLING",
    "LKM@IJCAI", "KiL@KDD", "DSN-W", "ICTSS", "DBSec",
}
# Well-known venues that must ALWAYS be listed in the main venue table / site
# facet, even below the usual count threshold (user request: TNNLS / TASLP /
# TAI / PRCV are recognizable standard venues, not "小众" clutter).
# Single source of truth for the always-listed venues now lives in
# data/facets.json (consumed by the frontend too), eliminating the py/js
# "keep in sync" drift. Falls back to the hard-coded set if the file is missing.
def _load_trending_tags():
    """Single source of truth for the 'trending' highlight tags (data/facets.json)."""
    fp = os.path.join(ROOT, "data", "facets.json")
    if os.path.exists(fp):
        try:
            with open(fp, encoding="utf-8") as f:
                return list(json.load(f).get("trending_tags", []))
        except Exception:
            pass
    return ["Agent", "RAG", "Reasoning", "Embodied"]


def _load_always_list():
    fp = os.path.join(ROOT, "data", "facets.json")
    if os.path.exists(fp):
        try:
            with open(fp, encoding="utf-8") as f:
                return set(json.load(f).get("always_list_venues", []))
        except Exception:
            pass
    return {"TNNLS", "TASLP", "TAI", "PRCV"}

ALWAYS_LIST_VENUES = _load_always_list()
CROSSREF = {}  # populated in main(); DOI -> container-title (cached reverse lookup)


def load_json(path):
    if os.path.exists(path):
        with open(path, encoding="utf-8") as f:
            return json.load(f)
    return {}


def _yaml_assign(d, kv):
    k, _, v = kv.partition(":")
    k = k.strip()
    v = v.strip().strip('"').strip("'")
    if k:
        d[k] = v


def load_manual_yaml():
    """Load data/manual_entries.yaml — a *minimal* YAML subset (no PyYAML
    dependency): a list of '- key: value' mappings with scalar values.
    Returns (title, authors, url, year) tuples compatible with RAW, so the
    merge loop below treats them identically. This is the human-edited
    curation entry point (recovered papers, pinned venues, etc.)."""
    path = os.path.join(ROOT, "data", "manual_entries.yaml")
    if not os.path.exists(path):
        return []
    out, cur = [], None
    with open(path, encoding="utf-8") as f:
        for line in f:
            s = line.strip()
            if not s or s.startswith("#"):
                continue
            if s.startswith("- "):
                if cur is not None:
                    out.append(cur)
                cur = {}
                _yaml_assign(cur, s[2:].strip())
            elif cur is not None and ":" in s:
                _yaml_assign(cur, s)
        if cur is not None:
            out.append(cur)
    entries = []
    for e in out:
        t = (e.get("title") or "").strip()
        if not t:
            continue
        entries.append((t, (e.get("authors") or "").strip(),
                        (e.get("url") or "").strip(),
                        int(e.get("year") or 2026)))
    return entries


# ---------------------------------------------------------------- helpers
from lib_common import norm_title, arxiv_id, VENUE_PATTERNS, atomic_dump


def year_from_url(url, fallback):
    m = re.search(r"arxiv\.org/abs/(\d{2})(\d{2})\.", url)
    return 2000 + int(m.group(1)) if m else fallback


def month_from_url(url):
    m = re.search(r"arxiv\.org/abs/\d{2}(\d{2})\.", url)
    return int(m.group(1)) if m else 0


def clean_latex(s):
    s = re.sub(r"\\textbf\{([^}]*)\}", r"\1", s)
    s = re.sub(r"\\textit\{([^}]*)\}", r"\1", s)
    s = re.sub(r"\\emph\{([^}]*)\}", r"\1", s)
    s = re.sub(r"\\text\{([^}]*)\}", r"\1", s)
    s = re.sub(r"\\[a-zA-Z]+\s*", "", s)
    s = s.replace("{", "").replace("}", "")
    return re.sub(r"\s+", " ", s).strip()


# ---------------------------------------------------------------- classify
def classify_model(text):
    """LLM | VLM | MLLM (Omni).

    Papers calling their model "MLLM / multimodal LLM" but only handling
    image/video + text are, in practice, VLMs. MLLM (Omni) is reserved for
    true omni-modal models: audio / speech / any-to-any modality.
    """
    t = text.lower()
    # 1. Omni: modalities beyond vision-text
    if re.search(r"omni[- ]?(modal|model|llm|mllm)|any[- ]to[- ]any|audio[- ]visual"
                 r"|speech[- ]vision|\baudio\b|\bspeech\b|omni[- ]language", t):
        return "MLLM"
    # 2. Anything vision-text (incl. papers self-described as MLLM/LMM)
    if re.search(r"vision[- ]language|\blvlms?\b|\bvlms?\b|large vision|video[- ]llm"
                 r"|video large language|3d[- ]llm|visual|image|\bvideo\b|multimodal"
                 r"|multi-modal|\bmllms?\b|\blmms?\b|\bmlrms?\b", t):
        return "VLM"
    return "LLM"


TRAINING_FREE_SIGNALS = re.compile(
    r"training[- ]free|without (any )?(additional |extra )?(training|fine[- ]tuning|retraining)"
    r"|no (additional |extra )?training|plug[- ]and[- ]play|inference[- ]time|decoding[- ]time"
    r"|post[- ]hoc|at inference", re.I)

TRAINING_BASED_SIGNALS = re.compile(
    r"we (fine[- ]tune|train|post[- ]train)|"
    r"(?:our (?:method|approach|framework|model|system)|the (?:method|approach|framework)) .{0,25}"
    r"(fine[- ]tun|train|optimi[sz]|post[- ]?train|pre[- ]?train)|"
    r"preference optimi[sz]ation|\bdpo\b|\brlhf\b|"
    r"reinforcement (learning|post[- ]?training|from human)|"
    r"instruction tuning|preference learning|"
    r"training (strategy|objective|framework|paradigm|recipe|phase)|"
    r"adversarial .{0,20}training|"
    r"fine[- ]tuning (?:approach|method|framework|the|our|of)|"
    r"fine[- ]tuned (?:detector|checker|classifier|qwen|deberta)|"
    r"(?:we|our|they) .{0,20}fine[- ]tuned|"
    r"supervised fine[- ]?tun(?:e|ing)? (?:of|the|our|on|to|for|via|using|with)|"
    r"reward model|policy optimi[sz]ation|alignment tuning|trained (?:with|on|to|via|using)|"
    r"\blora\b|parameter[- ]efficient|adapter .{0,15}(?:train|tun|fine)|"
    r"model editing|knowledge (?:erasure|editing|removal)|"
    r"post[- ]?train(?:ing)? (?:recipe|phase|data|corpus|objective|method|slm|specialist)|"
    r"pre[- ]?train(?:ing)? (?:recipe|data|corpus|objective|method)|"
    r"group relative policy optimi[sz]ation|direct preference optimi[sz]ation|"
    r"(?:reinforcement )?unlearn", re.I)

# Curated allow-list: papers whose abstract describes a genuine training-based
# method but is not reliably caught by the signals above (verified by hand).
# Keyed by norm_title (see :func:`norm_title`). Forces Training-based even if a
# "training-free" phrase happens to appear. This is the precise fix for papers
# that were mislabeled Training-free (e.g. PretrainRL, DA-DPO, LoRA/model-editing
# methods) — 28 entries audited on 2026-07-24.
METHOD_TRAINING_ALLOW = {
    "fromprooftoprogramcharacterizingtoolinducedreasoninghallucinationsinlargelanguagemodels",
    "pretrainrlalleviatingfactualityhallucinationoflargelanguagemodelsatthebeginning",
    "beyonddocumentgroundingspanlevelhallucinationdetectionovercodetooloutputanddocuments",
    "mitigatingpackagehallucinationsinlargelanguagemodelsviamodelediting",
    "hunyuanocr15makinglightweightocrvlmsfasterandbetter",
    "doyouremembertowardmemorycentricmultimodalai",
    "diffcvediffusionbasedcompressedvideoenhancement",
    "learningmechanisticreasoningforchemicalreactionswithlargelanguagemodels",
    "weedexpertr1incentivizingbotanicalreasoninginmllmswithreinforcementlearningforprecisionweedgrounding",
    "ragalafrugalfullylocalretrievalaugmentedassistantfortechnicalsupportatagovernmentagency",
    "autofilllearningtopredictmissingvaluesaccuratelywithspecialistlanguagemodels",
    "hallucinationinworldmodelsispredictableandpreventable",
    "objecthallucinationfreereinforcementunlearningforvisionlanguagemodels",
    "hallucleardiagnosingevaluatingandmitigatinghallucinationsinguiagents",
    "esgbenchbenchmarkinglongcontextesgreportsforhallucinationmitigation",
    "lookcloseranadversarialparametriceditingframeworkforhallucinationmitigationinvlms",
    "doireallyknowlearningfactualselfverificationforhallucinationreduction",
    "rshalludualmodehallucinationevaluationforremotesensingmultimodallargelanguagemodelswithdomaintailoredmitigation",
    "himemitigatingobjecthallucinationsinlvlmsviahallucinationinsensitivitymodelediting",
    "beyondsuperficialunlearningsharpnessawarerobusterasureofhallucinationsinmultimodalllms",
    "globallocalconfidencefusionforhallucinationdetectioninmathematicalreasoningtask",
    "ghosthallucinationinducingimagegenerationformultimodalllms",
    "focusonwhatmattersenhancingmedicalvisionlanguagemodelswithautomaticattentionalignmenttuning",
    "qwenlookagainguidingvisionlanguagereasoningmodelstoreattentionvisualinformation",
    "dadpocostefficientdifficultyawarepreferenceoptimizationforreducingmllmhallucinations",
    "lunaalightweightevaluationmodeltocatchlanguagemodelhallucinationswithhighaccuracyandlowcost",
    "addressinghallucinationincausalqampatheefficacyoffinetuningoverpromptinginllms",
    "mitigatingfinegrainedhallucinationbyfinetuninglargevisionlanguagemodelswithcaptionrewrites",
}

# Benchmark / evaluation-suite / dataset detection.
# Title-based: a genuine benchmark almost always announces itself in the title
# ("X: A Benchmark for ..."). A secondary abstract signal is allowed only for an
# explicit "we introduce / propose / present / release ... benchmark / dataset"
# construction, and is suppressed when the title is mainly about mitigation (a
# method paper that merely mentions a benchmark in related work).
# Benchmark / dataset / evaluation-suite. Title-led: a genuine benchmark almost
# always announces itself in the title. Abstract-only mentions are overwhelmingly
# related work or method papers that merely evaluate on a benchmark, so they are
# excluded to avoid false positives (this was the root cause of ~40 method/
# analysis papers being mis-tagged as Benchmark).
BENCH_TITLE = re.compile(
    r"\bbenchmark\b|\btest[- ]?bed\b|\bdataset\b|\bleaderboard\b"
    r"|\b\w*Bench\b"                                  # XBench naming (MHBench, HalBench, StepBench…)
    r"|evaluation (suite|benchmark|protocol)"
    r"|\ba (new |novel |comprehensive |large[- ]scale )?(benchmark|dataset)\b", re.I)
# A few genuine benchmarks whose titles omit the standard keywords above (they
# are datasets / eval-suites described in the abstract). Curated allow-list.
BENCH_ALLOW = ("codehalu", "kg-fpq", "negative object presence evaluation")

# Survey / review / taxonomy / overview detection.
# Title-based: a survey is almost always signalled in the title. Abstract
# mentions of "survey" are related work and are intentionally ignored to avoid
# false positives (this was the root cause of surveys being mis-tagged as
# benchmarks before).
SURVEY_STRONG = re.compile(
    r"\ba survey\b|\bsurvey (of|on)\b|\ba comprehensive survey\b|\bsystematic review\b"
    r"|\ba review\b|\breview (of|on)\b|\btaxonomy (of|for)\b|\ba (brief )?overview\b"
    r"|\bsurveys? (and|&) (reviews?|surveys?)\b", re.I)

MITIGATE_SIGNALS = re.compile(
    r"mitigat|alleviat|reduc(e|ing) hallucinat|suppress|correct(ing)? hallucinat"
    r"|we propose|our method|our approach|our framework", re.I)


def classify_method(title, abstract):
    """Binary: Training-free | Training-based. (Evaluation is a separate flag.)"""
    # Curated allow-list forces Training-based for verified training methods
    # whose abstracts are not reliably caught by the signals below.
    if norm_title(title) in METHOD_TRAINING_ALLOW:
        return "Training-based"
    text = title + " " + abstract
    # explicit training-free wins over incidental training mentions
    if TRAINING_FREE_SIGNALS.search(text):
        return "Training-free"
    if TRAINING_BASED_SIGNALS.search(text):
        return "Training-based"
    return "Training-free"


def is_benchmark(title, abstract):
    """Genuine benchmark / dataset / evaluation-suite paper.

    Title-led only (see :data:`BENCH_TITLE`), plus a small curated allow-list
    for benchmarks whose titles omit the standard keywords. Surveys are never
    benchmarks — the caller enforces that mutual exclusion."""
    t = title.lower()
    if BENCH_TITLE.search(title):
        return True
    return any(k in t for k in BENCH_ALLOW)


def is_survey(title, abstract):
    """Survey / review / taxonomy / overview paper (title-based)."""
    return bool(SURVEY_STRONG.search(title))


def scene_tags(title, abstract):
    """Object hallucination == the default/general case for VLMs, so it is no
    longer a separate dimension. Only the genuinely distinct Relation /
    Attribute hallucinations are surfaced, as optional tags."""
    t = (title + " " + abstract).lower()
    tags = []
    if re.search(r"relation(ship)?[- ](level[- ])?hallucinat|action[- ]relation hallucinat", t):
        tags.append("Relation")
    if re.search(r"attribute[- ](level[- ])?hallucinat|hallucinated attribute", t):
        tags.append("Attribute")
    return tags


def extra_tags(title, abstract, model_type=None):
    t = (title + " " + abstract).lower()
    tags = []
    if re.search(r"\bvideo\b|temporal hallucinat|frame[- ]level", t):
        tags.append("Video")
    if re.search(r"\baudio\b|\bspeech\b", t):
        tags.append("Audio")
    if re.search(r"multilingual|cross[- ]lingual", t):
        tags.append("Multilingual")
    if "medical" in t:
        tags.append("Medical")
    if re.search(r"\b3d\b", t):
        tags.append("3D")
    if re.search(r"\bagents?\b|embodied", t):
        tags.append("Agent")
    if re.search(r"\brag\b|retrieval[- ]augmented|retrieval[- ]based", t):
        tags.append("RAG")
    if re.search(r"reasoning|chain[- ]of[- ]thought|\bcot\b|deliberat|slow[- ]thinking|\bo1\b|deepseek[- ]r1", t):
        tags.append("Reasoning")
    if re.search(r"\bembodied\b|\brobot", t) or ("manipulation" in t and re.search(r"robot|embodied|grasp|physical|act", t)):
        tags.append("Embodied")
    # CV (image / 2D visual) modality — the base visual modality. Kept distinct
    # from Video / 3D so the modality facets form clean, non-overlapping buckets.
    # Gated on non-LLM model_type: pure-text LLM papers (text captioning /
    # grounding / "object") must not be tagged with the visual CV modality.
    # model_type is passed in to avoid re-running classify_model per paper.
    mt = model_type or classify_model(title + " " + abstract)
    if mt != "LLM" and not ({"Video", "3D"} & set(tags)):
        if re.search(r"image|imagery|\bvisual\b|photo|picture|\bscene\b|"
                     r"\bobject\b|grounding|caption|\bocr\b|diagram|chart|"
                     r"figure|pixel|region|spatial|computer vision|\bvision\b", t):
            tags.append("CV")
    return tags


def detect_venue(url):
    if "aclanthology.org" in url:
        return "ACL"
    if "arxiv.org" in url:
        return "arXiv"
    # "ieeexplore.ieee.org" and "link.springer.com" are PUBLISHERS, not venues.
    # Emitting "IEEE"/"Springer" as a venue is misleading (e.g. ICASSP, TMM,
    # CVPR all live under IEEE/Springer). The real venue is resolved by the
    # DBLP enrichment step (data/venue_links.json) and overrides this.
    return ""


# approximate month each conference takes place (for "conference time" display)
VENUE_MONTH = {
    "AAAI": 2, "EACL": 3, "WACV": 3, "ICLR": 4, "ICASSP": 4, "NAACL": 6,
    "CVPR": 6, "ICME": 7, "ICML": 7, "ACL": 7, "SIGIR": 7, "IJCAI": 8,
    "KDD": 8, "INTERSPEECH": 9, "ICCV": 10, "ECCV": 10, "ECAI": 10,
    "ACM MM": 10, "MM": 10, "EMNLP": 11, "NeurIPS": 12, "COLING": 1,
}


def short_venue(v):
    """Normalize DBLP venue strings: 'ACL (1)' -> 'ACL', 'EMNLP (Findings)' -> 'EMNLP-Findings'."""
    v = v.strip()
    m = re.match(r"^(.*?)\s*\(Findings\)$", v)
    if m:
        return m.group(1).strip() + "-Findings"
    v = re.sub(r"\s*\(\d+\)$", "", v)
    return v


def venue_base(v):
    """Map a (possibly canonical) venue string to its month-lookup key.
    Journals get "" so no fake conference month is assigned."""
    if re.search(r"Trans\.|Journal|\bJ\.|Int\. J\.|Mach\. Learn\. Res", v):
        return ""
    if v.startswith("ACM MM") or v.startswith("ACM Multimedia"):
        return "ACM MM"
    if v.startswith("CVPR"):          # incl. "CVPR Workshops" / "CVPRW"
        return "CVPR"
    return v.split("-")[0].split(" ")[0]


# Canonical abbreviations — DBLP returns half-abbreviated venue strings
# (e.g. "IEEE Trans. Multim.", "ACM Trans. Multim. Comput. Commun. Appl.");
# the user wants clean standard codes (TMM / TOMM / IJCV / ACM MM / CVPRW ...).
JOURNAL_ABBR = {
    "acm multimedia": "ACM MM",
    "trans. mach. learn. res": "TMLR",
    "acm trans. multim. comput. commun. appl": "TOMM",
    "acm trans. multim": "TOMM",
    "int. j. comput. vis": "IJCV",
    "ieee trans. multim": "TMM",
    "ieee trans. pattern anal. mach. intell": "TPAMI",
    "ieee trans. image process": "TIP",
    "ieee trans. neural networks learn. syst": "TNNLS",
    "ieee acm trans. audio speech lang. process": "TASLP",
    "ieee trans. audio speech lang. process": "TASLP",
    "ieee trans. artif. intell": "TAI",
    "ieee/caa j. autom. sinica": "JAS",
    "comput. vis. image underst": "CVIU",
    "knowl. based syst": "KBS",
    "iet image process": "IET IP",
    "inf. fusion": "INFFUS",
    "expert syst. appl": "ESWA",
    "neurocomputing": "NEUCOM",
    "pattern recognit. lett": "PRL",
    "image vis. comput": "IVC",
    "neural netw": "NN",
    "mach. learn": "ML",
}
WORKSHOP_ABBR = {
    "cvpr workshops": "CVPRW",
    "iccv workshops": "ICCVW",
}


def canon_venue(sv):
    """Convert a DBLP venue string into a clean standard abbreviation."""
    s = sv.strip().lower()
    for k, v in WORKSHOP_ABBR.items():
        if s.startswith(k):
            return v
    for k, v in JOURNAL_ABBR.items():
        if k in s:
            return v
    return sv


def venue_label(v):
    """Strip the trailing year from a resolved venue string for grouping.
    'CVPR 2024' -> 'CVPR'; 'arXiv' stays; '' -> '未标注'."""
    v = (v or "").strip()
    if not v:
        return "未标注"
    if v == "arXiv":
        return "arXiv（预印本）"
    m = re.match(r"^(.*?)\s+\d{4}$", v)
    return m.group(1) if m else v


def ccf_of(venue):
    """Resolve the CCF 2022 rating (A/B/C) for a venue string; '' if unrated."""
    base = re.sub(r"\s+\d{4}$", "", (venue or "").strip())
    if not base:
        return ""
    return CCF.get(base, "")


# Crossref container-title -> clean short venue (only CCF-catalogued venues are
# returned; IEEE/Springer/unknown containers return None so the paper stays
# "未标注"). Now sourced from lib_common.VENUE_PATTERNS (single source of truth,
# shared with update_arxiv_venues.py) so the two parsers can never disagree.

def infer_venue_from_crossref(url):
    """Fallback venue resolution: DOI -> cached Crossref container-title -> short
    venue. Returns e.g. 'EMNLP' or None (unrated / unrecognized)."""
    if not url:
        return None
    m = re.search(r"10\.\d{4,9}/[^\s]+", url)
    if not m:
        return None
    doi = m.group(0).rstrip(").,")
    ct = CROSSREF.get(doi, "")
    if not ct:
        return None
    for venue, pat in VENUE_PATTERNS:
        if re.search(pat, ct, re.I):
            return venue
    return None


def crossref_container_short(url):
    """Real (minor) venue name for DOIs whose container-title is NOT a
    CCF-catalogued venue: shorten the cached Crossref container-title so the
    '其他' bucket can be split into its actual venues. Returns None when the
    DOI has no cached container-title (stays '其他')."""
    if not url:
        return None
    m = re.search(r"10\.\d{4,9}/[^\s]+", url)
    if not m:
        return None
    ct = CROSSREF.get(m.group(0).rstrip(").,"), "")
    if not ct:
        return None
    s = re.sub(r"\s+", " ", ct).strip()
    # Crossref container-titles occasionally carry HTML entities
    s = s.replace("&amp;", "&").replace("&lt;", "<").replace("&gt;", ">").replace("&#38;", "&")
    s = re.sub(r"^Proceedings of (the )?", "", s, flags=re.I)
    s = re.sub(r"^\d{4}\s+", "", s)          # leading conference year
    s = re.sub(r"\s*\((Volume|Vol\.)[^)]*\)$", "", s, flags=re.I)
    # NOTE: do NOT truncate here. A chopped name like "E-Business,…" is
    # ambiguous in the README "其他" detail and can even split one venue into
    # two fake entries. Full container titles are correct and render fine in a
    # markdown table (the column just gets wider).
    return s or None


# ---------------------------------------------------------------- main
def main():
    abstracts = load_json(ABS_CACHE)
    abstracts_title = load_json(os.path.join(ROOT, "data", "abstracts_extra.json"))
    found_links = load_json(FOUND_LINKS)
    code_links = load_json(CODE_LINKS)
    venue_links = load_json(VENUE_LINKS)
    global CCF, CROSSREF
    CCF = load_json(CCF_FILE)
    CROSSREF = load_json(CROSSREF_CACHE)

    # Merge auto-harvested arXiv candidates (if present) into the manual RAW list.
    raw = list(RAW)
    # Manual curation entries (data/manual_entries.yaml) — human-edited source
    # of truth for papers not auto-fetched from arXiv.
    raw += load_manual_yaml()
    inc_path = os.path.join(ROOT, "data", "incremental.json")
    if os.path.exists(inc_path):
        try:
            with open(inc_path, encoding="utf-8") as f:
                inc = json.load(f)
            for it in inc:
                if isinstance(it, (list, tuple)) and len(it) >= 4:
                    raw.append((str(it[0]), str(it[1]), str(it[2]), int(it[3])))
        except Exception as ex:
            print(f"[generate] skip incremental.json: {ex!r}", file=sys.stderr)

    seen = {}
    papers = []
    for title, authors, url, sec_year in raw:
        key = norm_title(title)
        # fill in searched arXiv links for entries missing a URL
        if not url and found_links.get(key):
            url = found_links[key]
        if key in seen:
            if url and not seen[key]["url"]:
                seen[key]["url"] = url
                seen[key]["venue"] = detect_venue(url)
                seen[key]["year"] = year_from_url(url, sec_year)
                seen[key]["month"] = month_from_url(url)
            continue

        aid = arxiv_id(url)
        meta = abstracts.get(aid, {}) if aid else {}
        abstract = clean_latex(meta.get("abstract", "")) or abstracts_title.get(key, "")
        date = (meta.get("published", "") or "")[:10]  # YYYY-MM-DD (arXiv v1)
        text = title + " " + abstract
        model_type = classify_model(text)
        method_type = classify_method(title, abstract)
        survey = is_survey(title, abstract)
        benchmark = is_benchmark(title, abstract) and not survey  # Survey ⊃ Benchmark mutually exclusive
        tags = scene_tags(title, abstract) + extra_tags(title, abstract, model_type)
        if survey:
            tags = ["Survey"] + tags
        elif benchmark:
            tags = ["Benchmark"] + tags

        # ---- official venue (DBLP) takes priority over arXiv ----
        vm = venue_links.get(key) or None
        venue, venue_url = detect_venue(url), ""
        year, month = year_from_url(url, sec_year), month_from_url(url)
        if isinstance(vm, dict) and vm.get("venue"):
            sv = canon_venue(short_venue(vm["venue"]))
            vyear = vm.get("year") or year
            venue = f"{sv} {vyear}"
            venue_url = vm.get("ee", "")
            year = vyear
            vmonth = VENUE_MONTH.get(venue_base(sv), 0)
            if vmonth:
                month = vmonth
                date = f"{vyear}-{vmonth:02d}"       # conference time wins
            else:
                date = str(vyear)
            if not url:                              # official link fills gap
                url = venue_url

        # ---- Crossref fallback: DOI -> real venue (if CCF-catalogued) ----
        if not venue:
            cv = infer_venue_from_crossref(url)
            if cv:
                venue = f"{cv} {year}"

        # ---- Unresolved venue: split "其他" into real minor venues where the
        #      Crossref container-title is cached; papers keep their actual
        #      venue name but carry venue_minor=True so README / the site fold
        #      them by default. DOI without container-title stays "其他";
        #      no link at all stays "未标注". ----
        venue_minor = False
        if not venue:
            if url and re.search(r"10\.\d{4,9}/", url):
                venue = crossref_container_short(url) or "其他"
                venue_minor = True
            else:
                venue = "未标注"

        # ---- Secondary / co-located venues keep their names but are marked
        #      minor (folded in display) instead of being renamed "其他" ----
        vb = venue_label(venue) if venue else ""
        if vb in SECONDARY_VENUES:
            venue_minor = True
        elif vb == "NAACL-HLT":
            venue = venue.replace("NAACL-HLT", "NAACL")

        # ---- venue_url backfill: use the official publisher link when the
        #      resolved venue_url is empty (e.g. DBLP returned no ee, or the
        #      paper was sourced directly from a DOI / ACM / IEEE / CVF page).
        #      arXiv preprints are skipped — their only link is the arXiv page
        #      itself, which the card already shows separately. ----
        if not venue_url and url and "arXiv" not in (venue or ""):
            if re.search(r"(doi\.org|aclanthology\.org|openreview\.net|"
                         r"thecvf\.com|ieeexplore\.ieee\.org|dl\.acm\.org|"
                         r"link\.springer\.com|springer\.com|mdpi\.com|"
                         r"nature\.com|sciencedirect\.com)", url):
                venue_url = url

        rec = {
            "title": title,
            "authors": authors,
            "url": url,
            "venue_url": venue_url,
            # code links are keyed by arXiv id when available (unambiguous),
            # else by norm_title; fall back so legacy entries still resolve.
            "code": code_links.get(aid) or code_links.get(key, ""),
            "year": year,
            "month": month,
            "date": date,
            "venue": venue,
            "venue_minor": venue_minor,
            "ccf": ccf_of(venue),
            "model_type": model_type,
            "method_type": method_type,
            "benchmark": benchmark,
            "survey": survey,
            "tags": tags,
            "abstract": abstract,
        }
        papers.append(rec)
        seen[key] = rec

    papers.sort(key=lambda p: (-p["year"], -p["month"], p["date"] or "0000", p["title"].lower()))
    for i, p in enumerate(papers, 1):
        p["id"] = i

    stats = {
        "total": len(papers),
        "by_year": dict(Counter(p["year"] for p in papers)),
        "by_model": dict(Counter(p["model_type"] for p in papers)),
        "by_method": dict(Counter(p["method_type"] for p in papers)),
        "by_venue": dict(Counter(venue_label(p["venue"]) for p in papers)),
        "minor_venues": sorted({venue_label(p["venue"]) for p in papers if p.get("venue_minor")}),
        "by_ccf": dict(Counter((p["ccf"] or "未收录") for p in papers)),
        "by_tag": dict(Counter(t for p in papers for t in p["tags"])),
        "benchmarks": sum(1 for p in papers if p["benchmark"]),
        "surveys": sum(1 for p in papers if p["survey"]),
        "with_code": sum(1 for p in papers if p["code"]),
        "with_link": sum(1 for p in papers if p["url"]),
        "with_abstract": sum(1 for p in papers if p["abstract"]),
        "with_venue": sum(1 for p in papers if p["venue_url"]),
        "facets": {
            "always_list_venues": sorted(ALWAYS_LIST_VENUES),
            "trending_tags": _load_trending_tags(),
        },
    }

    payload = {"generated": True, "stats": stats, "papers": papers}
    os.makedirs(os.path.join(ROOT, "data"), exist_ok=True)
    os.makedirs(os.path.join(ROOT, "docs"), exist_ok=True)
    # Compact JSON (no indentation) roughly halves on-disk / wire size; the
    # file is generated, not hand-edited. Kept identical between data/ and
    # docs/ so the audit's data==docs md5 invariant still holds.
    # Atomic writes: an interrupted build never leaves a truncated published
    # file that would break the front-end.
    atomic_dump(os.path.join(ROOT, "data", "papers.json"), payload)
    atomic_dump(os.path.join(ROOT, "docs", "papers.json"), payload)

    # Web-optimized artifacts for GitHub Pages:
    #  * papers.lite.json — same list WITHOUT abstracts, for a fast first paint
    #    (the 3MB full file only ships if lite is missing / on direct open).
    #  * abstracts.byid.json — paper-id -> abstract map, lazy-loaded on expand.
    _lite = {"generated": True, "stats": stats,
             "papers": [{k: v for k, v in p.items() if k != "abstract"} for p in papers]}
    atomic_dump(os.path.join(ROOT, "docs", "papers.lite.json"), _lite)
    _abs = {p["id"]: p["abstract"] for p in papers if p.get("abstract")}
    atomic_dump(os.path.join(ROOT, "docs", "abstracts.byid.json"), _abs)

    # Trend snapshot: latest stats + an append-only history (one line per run)
    # so library growth can be tracked over time.
    snap = {"generated_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
            **stats}
    atomic_dump(os.path.join(ROOT, "data", "stats.json"), snap, indent=2)
    with open(os.path.join(ROOT, "data", "stats_history.jsonl"), "a", encoding="utf-8") as f:
        f.write(json.dumps(snap, ensure_ascii=False) + "\n")

    write_readme(papers, stats, "en")
    write_readme(papers, stats, "zh")
    print("Generated", len(papers), "papers")
    print("Stats:", json.dumps(stats, ensure_ascii=False))


# ---------------------------------------------------------------- readme
def bar(count, total, width=22):
    n = round(count / total * width) if total else 0
    return "█" * n + "░" * (width - n)


def bullet(p, mark=False):
    """Compact one-line entry for the README paper / benchmark list.

    `mark` may be a string (e.g. "📋" / "📚") used as a prefix, or False."""
    title = p["title"].replace("|", "\\|")
    link = p["venue_url"] or p["url"]
    tc = f"[{title}]({link})" if link else title
    if mark:
        tc = mark + " " + tc
    meta = p["venue"] or str(p["year"])
    mlbl = "MLLM(Omni)" if p["model_type"] == "MLLM" else p["model_type"]
    parts = [f"**{tc}**", meta, mlbl, p["method_type"]]
    if p["code"]:
        parts.append(f"💻[code]({p['code']})")
    return " · ".join(parts)


def write_readme(papers, stats, lang):
    """Render the full README in one language (`en` / `zh`).

    Emits README.md (en) and README.zh-CN.md (zh); each carries a small
    language-switch banner at the top pointing at the other file. Section ids
    (`<a id="sec-...">`) are language-neutral so anchors work in both.
    """
    total = stats["total"]
    years = sorted(stats["by_year"].keys(), reverse=True)
    last_update = datetime.now().strftime("%Y-%m")

    def _(en, zh):
        return en if lang == "en" else zh

    L = []
    L.append("> " + ("🌐 **English** · [中文](README.zh-CN.md)" if lang == "en" else "[English](README.md) · **中文**"))
    L.append("")
    L.append("# Awesome Hallucination Atlas [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)")
    L.append("")
    L.append("> " + _("**Awesome Hallucination Atlas** — A structured, interactive atlas of hallucination research across multimodal LLMs (MLLM / VLM / LLM).",
                       "**Awesome Hallucination Atlas** —— 一个**结构化、可交互**的多模态大模型（MLLM / LVLM / LLM）幻觉研究资源库。"))
    L.append(">")
    L.append("> " + _("Covers **detection, evaluation, and mitigation** of hallucinations, with multi-dimensional faceted filtering by model type, method type, and year, plus tags for modality and scenario.",
                       "涵盖幻觉的**检测、评测与缓解**方法，支持按模型类型、方法类型、年份多维交叉筛选，并以标签补充模态与场景。"))
    L.append(">")
    L.append("> " + _(f"Taxonomy is auto-labeled from the **full arXiv abstract text** ({stats['with_abstract']}/{total} papers), not just title keywords.",
                      f"分类标注基于 **arXiv 论文摘要全文**自动分析（覆盖 {stats['with_abstract']}/{total} 篇），非仅标题关键词。"))
    L.append("")
    L.append("<p align='center'>")
    L.append(f"  <img src='https://img.shields.io/badge/Papers-{total}-blue' />")
    L.append(f"  <img src='https://img.shields.io/badge/Abstract--based-{stats['with_abstract']}-9cf' />")
    L.append("  <img src='https://img.shields.io/badge/PRs-Welcome-brightgreen' />")
    L.append(f"  <img src='https://img.shields.io/static/v1?label=Last%20Update&message={last_update}&color=orange' />")
    L.append("</p>")
    L.append("")
    L.append("**🌐 " + _("Website", "网站") + "**: "
             + _("[awesome-hallucination-atlas on GitHub Pages](https://guangtaolyu.github.io/awesome-hallucination-atlas/) — interactive filtering, full-text abstract search, and year sorting. "
                "Or open [`docs/index.html`](docs/index.html) locally.",
                "[awesome-hallucination-atlas（GitHub Pages）](https://guangtaolyu.github.io/awesome-hallucination-atlas/) —— 交互式筛选、摘要全文搜索与年份排序。也可本地打开 [`docs/index.html`](docs/index.html)。"))
    L.append("")
    L.append("## 📑 " + _("Table of Contents", "目录"))
    L.append("")
    L.append("- [" + _("Data Overview", "数据概览") + "](#sec-overview)")
    L.append("- [" + _("Taxonomy", "分类体系") + "](#sec-taxonomy)")
    L.append("- [" + _("Trending Directions", "热点方向") + "](#sec-trending)")
    L.append("- [" + _("Benchmarks & Evaluation", "评测与 Benchmark") + "](#sec-benchmark)")
    L.append("- [" + _("Surveys", "综述 Survey") + "](#sec-survey)")
    L.append("- [" + _("Paper List", "论文列表") + "](#sec-paperlist)")
    L.append("- [" + _("Citation", "推荐引用") + "](#sec-cite)")
    L.append("- [" + _("Contributing", "贡献") + "](#sec-contrib)")
    L.append("- [" + _("License", "许可") + "](#sec-license)")
    L.append("- [" + _("Star History", "Star 增长趋势") + "](#sec-stars)")
    L.append("")
    L.append("---")
    L.append("")
    L.append('<a id="sec-overview"></a>')
    L.append("## 📊 " + _("Data Overview", "数据概览"))
    L.append("")
    L.append(f"- **{_('Total papers', '论文总数')}**：`{total}` {_('(deduplicated)', '（已去重）')}")
    L.append(f"- **{_('With paper link', '含论文链接')}**：`{stats['with_link']}` · "
             f"**{_('With abstract', '含全文摘要')}**：`{stats['with_abstract']}` · "
             f"**{_('With code', '含代码链接')}**：`{stats['with_code']}` · "
             f"**{_('Published at venue', '顶会正式发表')}**：`{stats.get('with_venue', 0)}`")
    L.append("- " + _("For papers published at a venue: **time and link prioritize the official conference/journal info** (DBLP), otherwise arXiv info is used.",
                      "顶会正式发表的论文：**时间与链接优先采用会议官方信息**（DBLP 记录），其余采用 arXiv 信息。"))
    L.append(f"- **{_('Year range', '覆盖年份')}**：{years[-1]} – {years[0]}")
    L.append("")
    L.append("### " + _("Year Distribution", "按年份分布"))
    L.append("")
    L.append("| " + _("Year", "年份") + " | " + _("Count", "数量") + " | " + _("Share", "占比") + " |")
    L.append("|------|------|------|")
    for y in years:
        c = stats["by_year"][y]
        L.append(f"| {y} | {c} | `{bar(c, total)}` {c / total * 100:.1f}% |")
    L.append("")
    L.append("### " + _("Model Type", "按模型类型分布"))
    L.append("")
    L.append("| " + _("Model Type", "模型类型") + " | " + _("Description", "说明") + " | " + _("Count", "数量") + " |")
    L.append("|----------|------|------|")
    model_desc = {
        "VLM": _("Vision-Language Model (LVLM; also covers works that call themselves MLLM but handle only image/video + text)",
                 "视觉语言模型（LVLM，含自称 MLLM 但仅处理图像/视频+文本的工作）"),
        "MLLM": _("Omni / full-modal model (audio / speech / any-to-any)",
                  "全模态模型（Omni：音频 / 语音 / any-to-any）"),
        "LLM": _("Pure text-based LLM", "纯语言大模型"),
    }
    model_label = {"VLM": "VLM", "MLLM": "MLLM (Omni)", "LLM": "LLM"}
    for m in ["VLM", "MLLM", "LLM"]:
        L.append(f"| **{model_label[m]}** | {model_desc[m]} | {stats['by_model'].get(m, 0)} |")
    L.append("")
    L.append("### " + _("Method Type", "按方法类型分布"))
    L.append("")
    L.append("| " + _("Method Type", "方法类型") + " | " + _("Description", "说明") + " | " + _("Count", "数量") + " |")
    L.append("|----------|------|------|")
    method_desc = {
        "Training-free": _("Training-free (decoding intervention / attention calibration / representation guidance, etc.)",
                           "免训练（解码干预 / 注意力校准 / 表征引导等）"),
        "Training-based": _("Training-based (preference optimization / fine-tuning / RL, etc.)",
                            "基于训练（偏好优化 / 微调 / 强化学习等）"),
    }
    for m in ["Training-free", "Training-based"]:
        L.append(f"| **{m}** | {method_desc[m]} | {stats['by_method'].get(m, 0)} |")
    L.append("")

    # ---- venue distribution ----
    L.append("### " + _("Venue Distribution", "按会议 / 期刊分布"))
    L.append("")
    L.append("> " + _("Papers published at a conference / journal are counted by venue (official info prioritized); "
                       "`arXiv（预印本）` means a preprint not yet officially accepted. Niche journals / small venues, "
                       "workshops / satellite / co-located events, and venues with only 1 paper are grouped into the “Other” row "
                       "(details in the collapsible section below). `未标注` marks entries with no resolvable link.",
                      "已正式发表在会议 / 期刊的论文按 venue 统计（顶会官方信息优先）；`arXiv（预印本）` 为尚未正式录用的预印本。"
                      "小众期刊 / 小会、研讨会 / 卫星会 / 边会等次级 venue 以及各仅 1 篇的 venue 统一归入「其他」行，明细见表下折叠区；"
                      "`其他` 中仍含少量 DOI 无法解析出处的条目，`未标注` 为无任何链接、暂无法判定的条目。"))
    L.append("")
    L.append("| " + _("Venue / Journal", "会议 / 期刊") + " | " + _("Count", "数量") + " | " + _("Share", "占比") + " |")
    L.append("|-------------|------|------|")
    vcounts = sorted(stats["by_venue"].items(), key=lambda kv: (-kv[1], kv[0]))
    SINGLES = ("arXiv（预印本）", "其他", "未标注")
    minor_set = set(stats.get("minor_venues", []))
    # "其他" row = minor venues + count-1 venues + unresolvable-DOI leftovers
    folded = [(v, c) for v, c in vcounts
              if v not in SINGLES and v not in ALWAYS_LIST_VENUES
              and (v in minor_set or c == 1)]
    other_total = stats["by_venue"].get("其他", 0) + sum(c for _, c in folded)
    for v, c in vcounts:
        if v in SINGLES or (v not in ALWAYS_LIST_VENUES
                            and (v in minor_set or c == 1)):
            continue
        L.append(f"| {v} | {c} | `{bar(c, total)}` {c / total * 100:.1f}% |")
    L.append(f"| 其他 | {other_total} | `{bar(other_total, total)}` {other_total / total * 100:.1f}% |")
    if "arXiv（预印本）" in stats["by_venue"]:
        a = stats["by_venue"]["arXiv（预印本）"]
        L.append(f"| arXiv（预印本） | {a} | `{bar(a, total)}` {a / total * 100:.1f}% |")
    if "未标注" in stats["by_venue"]:
        u = stats["by_venue"]["未标注"]
        L.append(f"| 未标注 | {u} | `{bar(u, total)}` {u / total * 100:.1f}% |")
    L.append("")
    # ---- folded breakdown of the "其他" bucket ----
    if folded:
        unres = stats["by_venue"].get("其他", 0)
        L.append("<details>")
        L.append(f"<summary>" + _("“Other” details", "「其他」明细") + f" ({len(folded)} venues, {other_total} papers — click to expand)</summary>")
        L.append("")
        L.append("| venue | 数量 |")
        L.append("|-------|------|")
        for v, c in sorted(folded, key=lambda kv: (-kv[1], kv[0])):
            L.append(f"| {v} | {c} |")
        if unres:
            L.append(f"| （DOI 无法解析出处） | {unres} |")
        L.append("")
        L.append("</details>")
        L.append("")

    # ---- CCF rating distribution ----
    L.append("### " + _("CCF Rating", "按 CCF 评级分布"))
    L.append("")
    L.append("> " + _("CCF ratings follow the **CCF Recommended International Conference / Journal Directory (2022)** for officially published papers; "
                       "`未收录` covers arXiv preprints, unresolved venues, and venues outside the CCF list.",
                      "依据 **CCF 推荐国际学术会议 / 期刊目录（2022）** 对正式发表的论文标注评级；"
                      "`未收录` 含 arXiv 预印本、暂未解析出 venue 的条目，以及 CCF 目录之外的会议 / 期刊。"))
    L.append("")
    L.append("| " + _("CCF Rating", "CCF 评级") + " | " + _("Count", "数量") + " | " + _("Share", "占比") + " |")
    L.append("|----------|------|------|")
    for r in ["A", "B", "C", "未收录"]:
        c = stats["by_ccf"].get(r, 0)
        label = "CCF-" + r if r != "未收录" else "未收录"
        L.append(f"| {label} | {c} | `{bar(c, total)}` {c / total * 100:.1f}% |")
    L.append("")

    L.append("> " + _(f"📋 `{stats.get('benchmarks', 0)}` **Benchmark** papers and 📚 `{stats.get('surveys', 0)}` **Survey** papers "
                       "are listed separately (see sections below) and do not affect the method taxonomy.",
                      f"📋 另有 `{stats.get('benchmarks', 0)}` 篇 **评测 / Benchmark** 论文、📚 `{stats.get('surveys', 0)}` 篇 **综述 Survey** 论文，"
                      "作为独立标记单独列出（见下方对应小节），不占用方法分类。"))
    L.append("")
    L.append("---")
    L.append("")
    L.append('<a id="sec-taxonomy"></a>')
    L.append("## 🧭 " + _("Taxonomy", "分类体系"))
    L.append("")
    L.append(_("Each paper is labeled along **3 dimensions** (model type / method type / year, auto-analyzed from the full abstract), with tags for modality and scenario.",
              "每篇论文标注 **3 个维度**（模型类型 / 方法类型 / 年份，基于摘要全文自动分析），并以标签补充模态与场景："))
    L.append("")
    L.append("| " + _("Dimension", "维度") + " | " + _("Values", "取值") + " |")
    L.append("|------|------|")
    L.append("| **" + _("Model type", "模型类型") + "** | `VLM/LVLM` (vision-language) · `MLLM (Omni)` (omni with audio/speech) · `LLM` (text-only) |")
    L.append("| **" + _("Method type", "方法类型") + "** | `Training-free` · `Training-based` (binary) |")
    L.append(f"| **" + _("Year", "年份") + f"** | {min(years)} – {max(years)} |")
    L.append("")
    L.append("> " + _("Hallucination scenario is no longer a separate dimension: for VLMs, object hallucination *is* the general case. Only genuinely special `Relation` / `Attribute` hallucinations are kept as optional tags.",
                      "幻觉场景不再单独分维度：对 VLM 而言物体幻觉即通用幻觉，二者无实质区别。仅将真正特殊的 `Relation` / `Attribute` 幻觉作为可选标签保留。"))
    L.append("> " + _("Extra tags: `Benchmark` (evaluation; does not affect method taxonomy) · `Survey` · `Relation` · `Attribute` · `CV` (vision) · `Video` · `Audio` · `Multilingual` · `Medical` · `3D` · `Agent` · `RAG` · `Reasoning` · `Embodied`.",
                      "附加标签：`Benchmark`（评测/基准，独立标记不影响方法分类） `Survey`（综述） `Relation` `Attribute` `CV`（图像/视觉模态） `Video` `Audio` `Multilingual` `Medical` `3D` `Agent` `RAG` `Reasoning` `Embodied`（具身/机器人）。"))
    L.append("> " + _("Full abstracts are stored in `data/papers.json` and can be expanded / full-text searched in the interactive website.",
                      "完整摘要收录于 `data/papers.json`，可在交互网站中展开阅读与全文搜索。"))
    L.append("")
    L.append("---")
    L.append("")
    L.append('<a id="sec-trending"></a>')
    L.append("## 🔥 " + _("Trending Directions", "热点方向"))
    L.append("")
    L.append(_("Hallucination research is moving fast. These directions are especially hot in 2025–2026 and well-covered by this atlas (paper counts are auto-computed from real tags):",
               "幻觉研究正在快速演进。以下方向在 2025–2026 尤为火热，本图谱均有真实论文覆盖（数量为按真实标签自动统计）："))
    L.append("")
    L.append("- **" + _("Agentic AI / Multi-Agent", "智能体（Agentic AI / Multi-Agent）") + "** — " + _(f"{stats['by_tag'].get('Agent',0)} papers tagged `Agent`.",
               f"共 {stats['by_tag'].get('Agent',0)} 篇带 `Agent` 标签。"))
    L.append("- **" + _("RAG / Faithfulness", "检索增强生成（RAG / 忠实性）") + "** — " + _(f"{stats['by_tag'].get('RAG',0)} papers tagged `RAG`.",
               f"共 {stats['by_tag'].get('RAG',0)} 篇带 `RAG` 标签。"))
    L.append("- **" + _("Reasoning Models", "推理模型") + "** — " + _(f"{stats['by_tag'].get('Reasoning',0)} papers tagged `Reasoning`.",
               f"共 {stats['by_tag'].get('Reasoning',0)} 篇带 `Reasoning` 标签。"))
    L.append("- **" + _("Embodied / World Model", "具身 / 世界模型") + "** — " + _(f"{stats['by_tag'].get('Embodied',0)} papers tagged `Embodied`.",
               f"共 {stats['by_tag'].get('Embodied',0)} 篇带 `Embodied` 标签。"))
    L.append("")
    L.append("---")
    L.append("")
    L.append('<a id="sec-benchmark"></a>')
    L.append("## 📋 " + _("Benchmarks & Evaluation", "评测与 Benchmark"))
    L.append("")
    benchs = [p for p in papers if p.get("benchmark")]
    L.append("> " + _(f"{len(benchs)} evaluation / benchmark / dataset papers are listed separately (also kept in the main list below, marked 📋).",
                      f"独立收录 `{len(benchs)}` 篇评测 / Benchmark / 数据集论文（同时保留在下方主列表中，标有 📋）。"))
    L.append("")
    L.append(f'<details open>')
    L.append(f"<summary>📋 " + _("Benchmark List", "评测与 Benchmark 列表") + f" ({len(benchs)} papers — click to collapse / expand)</summary>")
    L.append("")
    for p in benchs:
        L.append("- " + bullet(p, mark="📋"))
    L.append("")
    L.append("</details>")
    L.append("")
    L.append("---")
    L.append("")
    L.append('<a id="sec-survey"></a>')
    L.append("## 📚 " + _("Surveys", "综述 Survey"))
    L.append("")
    surveys = [p for p in papers if p.get("survey")]
    L.append("> " + _(f"{len(surveys)} survey / review / taxonomy papers are listed separately (also kept in the main list below, marked 📚).",
                      f"独立收录 `{len(surveys)}` 篇综述 / 调查 / 分类法论文（同时保留在下方主列表中，标有 📚）。"))
    L.append("")
    L.append(f'<details open>')
    L.append(f"<summary>📚 " + _("Survey List", "综述 Survey 列表") + f" ({len(surveys)} papers — click to collapse / expand)</summary>")
    L.append("")
    for p in surveys:
        L.append("- " + bullet(p, mark="📚"))
    L.append("")
    L.append("</details>")
    L.append("")
    L.append("---")
    L.append("")
    L.append('<a id="sec-paperlist"></a>')
    L.append("## 📚 " + _("Paper List", "论文列表"))
    L.append("")
    L.append("> " + _("Grouped by year; click a year header to expand / collapse. Format per entry: **Title** · venue/year · model · method · 💻code. "
                       "Title links prefer the official venue version. 📋 = Benchmark paper, 📚 = Survey paper. "
                       "Full abstracts and multi-dimensional filtering are available in the interactive website [`docs/index.html`](docs/index.html). PRs welcome.",
                      "按年份分组，点击年份标题可展开 / 收起。每条格式：**标题** · 会议/年份 · 模型 · 方法 · 💻代码。"
                      "标题链接优先顶会官方版本。📋 = 评测/Benchmark 论文，📚 = 综述 Survey 论文。"
                      "完整摘要与多维交叉筛选见交互式网站 [`docs/index.html`](docs/index.html)。欢迎 PR 补充。"))
    L.append("")
    for y in years:
        yp = [p for p in papers if p["year"] == y]
        L.append(f'<details{" open" if y == years[0] else ""}>')
        L.append(f"<summary>📅 {y} · {len(yp)} " + _("papers", "篇") + "</summary>")
        L.append("")
        for p in yp:
            mark = "📋" if p.get("benchmark") else ("📚" if p.get("survey") else False)
            L.append("- " + bullet(p, mark=mark))
        L.append("")
        L.append("</details>")
        L.append("")
    L.append("---")
    L.append("")
    L.append('<a id="sec-cite"></a>')
    L.append("## 📖 " + _("Citation", "推荐引用"))
    L.append("")
    L.append(_("If this atlas helps your research, please consider citing our related papers (feedback and suggestions are also welcome):",
              "如果本资源库对你的研究有帮助，欢迎引用我们的相关论文（也欢迎交流与建议）："))
    L.append("")
    L.append("```bibtex")
    L.append("""@article{lyu2026hallu_sae,
  title={Towards Interpretable Hallucination Analysis and Mitigation in LVLMs via Contrastive Neuron Steering},
  author={Lyu, Guangtao and Cheng, Xinyi and Liu, Qi and Xu, Chenghao and Yan, Jiexi and Yang, Muli and Fang, Fen and Deng, Cheng},
  journal={arXiv preprint arXiv:2602.00621},
  year={2026}
}

@article{lyu2025hallu_vdc,
  title={Revealing Perception and Generation Dynamics in LVLMs: Mitigating Hallucinations via Validated Dominance Correction},
  author={Lyu, Guangtao and Cheng, Xinyi and Xu, Chenghao and Liu, Qi and Yang, Muli and Fang, Fen and Chen, Huilin and Yan, Jiexi and Yang, Xu and Deng, Cheng},
  journal={arXiv preprint arXiv:2512.18813},
  year={2025}
}

@article{lyu2026hallu_pade,
  title={Revealing and Enhancing Core Visual Regions: Harnessing Internal Attention Dynamics for Hallucination Mitigation in LVLMs},
  author={Lyu, Guangtao and Liu, Qi and Xu, Chenghao and Yan, Jiexi and Yang, Muli and Li, Xueting and Fang, Fen and Deng, Cheng},
  journal={ACL Findings},
  year={2026}
}""")
    L.append("```")
    L.append("")
    L.append('<a id="sec-contrib"></a>')
    L.append("## 🤝 " + _("Contributing", "贡献"))
    L.append("")
    L.append(_("We welcome new papers, code links, venue info, and taxonomy corrections! Please read [CONTRIBUTING.md](CONTRIBUTING.md).",
              "欢迎补充论文、代码链接、顶会录取信息、修正分类！请阅读 [CONTRIBUTING.md](CONTRIBUTING.md)。"))
    L.append("")
    L.append('<a id="sec-license"></a>')
    L.append("## 📄 " + _("License", "许可"))
    L.append("")
    L.append(_("Released under [CC0-1.0](LICENSE), following the [awesome](https://github.com/sindresorhus/awesome) manifesto.",
              "基于 [CC0-1.0](LICENSE) 协议发布，遵循 [awesome](https://github.com/sindresorhus/awesome) 规范。"))
    L.append("")
    L.append('<a id="sec-stars"></a>')
    L.append("## ⭐ " + _("Star History", "Star 增长趋势"))
    L.append("")
    L.append(_("A record of how this atlas has grown in the community:",
               "本图谱在社区中的增长记录："))
    L.append("")
    L.append('<a href="https://www.star-history.com/#GuangtaoLyu/awesome-hallucination-atlas&Date">')
    L.append('  <picture>')
    L.append('    <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/svg?repos=GuangtaoLyu/awesome-hallucination-atlas&type=Date&theme=dark" />')
    L.append('    <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/svg?repos=GuangtaoLyu/awesome-hallucination-atlas&type=Date" />')
    L.append('    <img alt="Star History Chart" src="https://api.star-history.com/svg?repos=GuangtaoLyu/awesome-hallucination-atlas&type=Date" />')
    L.append('  </picture>')
    L.append('</a>')
    L.append("")

    out_name = "README.md" if lang == "en" else "README.zh-CN.md"
    with open(os.path.join(ROOT, out_name), "w", encoding="utf-8") as f:
        f.write("\n".join(L))


if __name__ == "__main__":
    main()
