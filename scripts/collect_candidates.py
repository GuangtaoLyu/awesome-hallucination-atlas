# -*- coding: utf-8 -*-
"""Collect additional hallucination (MLLM/VLM/LLM) papers from major venues,
2020+, deduplicated against existing raw_data.

Sources:
  - DBLP API (per-venue `venue:<KEY>`): conferences
  - arXiv API: preprints
  - Crossref API (container-title): journals (TPAMI/TIP/TMM/TACL/JMLR/AI/TASLP...)
  - CVF Open Access (official proceedings): CVPR/ICCV/ECCV (official-link channel)

Outputs data/candidates_new.json (list of dicts) for review/merge.
"""
import json, re, os, time, urllib.parse
import xml.etree.ElementTree as ET

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
RAW = os.path.join(ROOT, "scripts", "raw_data.py")
OUT = os.path.join(ROOT, "data", "candidates_new.json")

from raw_data import RAW as EXISTING
from lib_common import norm_title as norm
from code_common import http_get

# ---- existing titles (for dedup) ----
EXIST_TITLES = {norm(t) for (t, *_ ) in EXISTING}
SEEN = set(EXIST_TITLES)

# Candidates are gathered by querying "hallucination" directly (DBLP global search
# and arXiv with all:"hallucination"). So every candidate already contains the
# keyword by construction. We only drop clearly off-topic uses of the word that
# have NOTHING to do with AI/ML model (MLLM/LLM/VLM) hallucination:
#   - medical / psychiatric symptoms (auditory-verbal hallucination, psychosis,
#     schizophrenia, drug/buprenorphine-induced, clinical, LSD/hallucinogens)
#   - computer-vision SUPER-RESOLUTION sense ("face hallucination", "texture
#     hallucination", "hallucination for super-resolution") — a different CV
#     subfield, not generative/perceptual errors in models.
OFF_TOPIC = re.compile(
    r"auditory (verbal )?hallucinat|\bavh\b|verbal hallucinat|"
    r"schizophren|psychiatr\w*|psychos\w*|drug[- ]induced|clinical hallucinat|"
    r"hallucinogen|\blsd\b|buprenorphine|opioid|"
    r"face hallucinat|texture hallucinat|super[- ]resolution|"
    r"visual (illusion|migraine)|"
    # CV data-AUGMENTATION sense: "hallucination" used as a METHOD that GENERATES
    # missing data (features / depth / poses / identity / modality / domain), NOT
    # the generative or perceptual-error phenomenon studied in LLM/VLM/MLLM
    # research. NOTE: we deliberately do NOT flag "cross-modal hallucination",
    # "multimodal hallucination", or "hallucination networks of LLMs" — those ARE
    # on-topic (the core subject of this library).
    r"\b(feature|deformation|depth|semantic|identity)\s+hallucinat|"
    r"cross[- ]domain\s+hallucinat|"
    r"hallucinat\w*\s+for\s+few[- ]shot|"
    r"domain\s+generalization\W.{0,40}?hallucinat|hallucinat\w*\W.{0,40}?domain\s+generalization|"
    r"face\s+manipulation\s+via\s+hallucinat|"
    r"gait\s+recognition\s+via\s+hallucinat|"
    # Broader CV-GENERATIVE method sense (data-augmentation "hallucination"):
    # "hallucination" used as a METHOD that GENERATES missing data / features,
    # NOT the perceptual-error phenomenon studied in LLM/VLM/MLLM research.
    # Deliberately scoped to unambiguous CV-method phrases so on-topic
    # "image/object hallucination in VLMs" papers are NEVER removed.
    r"\b(pixel[- ]wise|facial|scene\s+graph|value|anchor)\s+\w*\s*hallucinat|"
    r"\bdata\s+hallucinat|"
    r"hallucinat\w*\s+(diffusion|restoration|reconstruction|synthesis|prior)|"
    r"hallucinat\w*\s+of\s+\w*\s*faces?|tiny\s+faces|face\s+image\s+hallucinat|face\s+enhancement\s+and\s+hallucinat|"
    r"hallucinat\w*\W{0,30}?object\s+detection|"
    r"pedestrian\s+detection\W{0,40}?hallucinat|"
    r"depth\W{0,40}?hallucinat|frontalization\W{0,40}?hallucinat|"
    r"visual\s+hallucinat\w*\s+(for|elevates?|improves?|boosts?|enhances?)\s+(machine\s+translation|speech\s+recognition)|"
    r"thinking\s+hallucinat\w*\s+for\s+video\s+captioning|"
    r"hallucinat\w*\s+for\s+(video\s+captioning|text[- ]based\s+video\s+retrieval|unpaired\s+image\s+captioning|few[- ]shot\s+object\s+detection|thermal\s+pedestrian\s+detection|underwater\s+depth)|"
    r"diffusion[- ]based\s+image\s+restoration|"
    r"illumination[- ]aware\W{0,40}?hallucinat|domain\s+adaptation\W{0,40}?hallucinat|"
    r"disentangled\s+representations|"
    r"speech\s+recognition\s+errors?\W{0,30}?hallucinat|hallucinat\W{0,30}?speech\s+recognition\s+errors|"
    # Early small-model CV "hallucination-as-data-augmentation" (pre-LLM era):
    # hallucination = a MODULE that synthesizes features/modalities to boost a
    # recognition task (few-shot learning, detection, re-ID, pose, face
    # clustering). None of these study LLM/VLM/MLLM hallucination.
    r"hallucinat\w*\s+improves\b|"
    r"privileged\W.{0,50}?hallucinat|hallucinat\w*\W.{0,50}?privileged|"
    r"style\s+hallucinat|person\s+re[- ]identification|"
    r"hallucinat\w*\W.{0,50}?few[- ]shot\s+learning|few[- ]shot\s+learning\W.{0,50}?hallucinat|"
    r"hallucinat\w*[- ]based\s+multispectral|hallucinat\w*\W.{0,60}?pedestrian\s+detection|"
    r"attribute\s+hallucinat|face\s+clustering|"
    r"pose\s+estimation\W.{0,50}?hallucinat|"
    r"hallucinat\w*\s+in\s+object\s+detection\b|"
    r"hallucinat\w*\s+for\s+pedestrian\s+detection|pedestrian\s+detection\W.{0,40}?hallucinat|"
    r"hallucinat\w*\W.{0,60}?image\s+restoration|image\s+restoration\W.{0,60}?hallucinat|"
    r"hallucinat\w*\s+in\s+image\s+restoration|"
    r"domain\s+adaptation\W.{0,50}?hallucinat|hallucinat\w*\W.{0,50}?domain\s+adaptation|"
    r"image\s+hallucinat\w*\s+from\b|hallucinat\w*\s+from\s+attribute|"
    r"federated\s+hallucinat\w*\s+translation|"
    r"correspondence\s+hallucinat|hallucinat\w*\s+correspondence|"
    r"optical\s+flow\W.{0,40}?hallucinat|hallucinat\W.{0,40}?optical\s+flow|"
    r"stereo\s+(matching|fusion)\W.{0,40}?hallucinat|hallucinat\w*\W.{0,30}?stereo\s+(matching|fusion)|"
    r"lidar\W.{0,40}?hallucinat|hallucinat\w*\W.{0,20}?lidar|"
    r"controlled\s+visual\s+hallucinat\w*\W.{0,50}?(domain|adaptation)|"
    r"hallucination\s+feature\s+generator|"
    r"video\s+highlight\s+detection|"
    # ----- Classic CV tasks where "hallucination" is a data-augmentation /
    # SYNTHESIS METHOD (generating missing data / features / modalities / views),
    # NOT the studied perceptual-error phenomenon. Scoped to unambiguous
    # TECHNIQUE phrasings only:
    #   * image captioning is INTENTIONALLY NOT excluded — VLM object / counting
    #     hallucination in captioning IS on-topic;
    #   * "hallucination in <VLM task>" (segmentation / 3D-reconstruction /
    #     object-detection of the phenomenon) is on-topic -> never proximity-ban
    #     the task word after the hallucination;
    #   * T2I "image generation" (evaluation / induction of hallucination) is
    #     on-topic -> not excluded.
    r"texture\s+hallucinat|hallucinat\w*\s+of\s+(opaque\s+)?surfaces?|"
    r"hallucinat\w*\s+of\s+\w*\s*textures?|"
    r"multi[- ]view\s+hallucinat\w*(?!.*\b(vlm|llm|mllm|vision[- ]language|large vision)\b)|"
    r"hallucinat\w*\s+(for|via|based\s+on|to\s+enable|with|using)\s+(multi[- ]view|novel[- ]view)|"
    r"hallucinat\w*\W{0,30}?inpaint|inpaint\W{0,30}?hallucinat|"
    r"hallucinat\w*\W{0,30}?(image|scene|video)\s+classification|"
    r"hallucinat\w*\W{0,30}?action\s+recognition|"
    r"hallucinat\w*\W{0,30}?point\s+cloud|"
    r"hallucinat\w*\W{0,30}?video\s+summar|"
    r"hallucinat\w*\W{0,30}?neural\s+rendering|hallucinat\w*\W{0,30}?gaussian\s+splat|"
    r"hallucinat\w*\W{0,30}?(novel|multi)[- ]view\s+synthesis|"
    r"hallucinat\w*\W{0,30}?scene\s+(recognition|understanding|classification)|"
    r"hallucinat\w*\W{0,30}?object\s+tracking|"
    r"hallucinat\w*\W{0,30}?image\s+compression|"
    r"hyperspectral\s+hallucinat|hallucinat\w*\s+of\s+hyperspectral|"
    # Philosophy / psychology / neuroscience (not AI model behaviour)
    r"colour\s+hallucination|color\s+hallucination|representationalism|"
    r"hallucination[- ]prone|own[- ]voice\s+discriminat|associative\s+learning|"
    # Psychology / perception-science instruments & phenomena (human, not AI)
    r"hallucination[- ]like\s+experiences|launay[- ]slade|hallucination\s+scale|"
    r"stroboscopic\s+hallucinat|strobe\s+stimulation", re.I)

# Major venues to harvest directly from DBLP (DBLP venue keys). We embed
# "venue:<KEY>" as a field term in the query so each venue is scoped precisely.
DBLP_VENUE_KEYS = [
    "CVPR", "ICCV", "ECCV", "WACV", "NeurIPS", "ICML", "ICLR", "AAAI",
    "ACL", "EMNLP", "NAACL", "COLING", "EACL", "INTERSPEECH", "SIGIR",
    "IJCAI", "ACM MM", "ACM Multimedia", "TMLR", "TPAMI", "IJCV",
    "BMVC", "ICASSP", "SIGGRAPH", "KDD", "WWW", "ICME",
]

# Journals (顶刊). DBLP's `venue:<KEY>` query matches conferences well but
# misses journals, so we harvest these via Crossref (container-title filter).
# Names are the full display titles Crossref indexes. TASLP added per request.
JOURNALS = [
    ("TPAMI", "IEEE Transactions on Pattern Analysis and Machine Intelligence"),
    ("IJCV", "International Journal of Computer Vision"),
    ("TMM", "IEEE Transactions on Multimedia"),
    ("TIP", "IEEE Transactions on Image Processing"),
    ("TNNLS", "IEEE Transactions on Neural Networks and Learning Systems"),
    ("PR", "Pattern Recognition"),
    ("NN", "Neural Networks"),
    ("MLJ", "Machine Learning"),
    ("TACL", "Transactions of the Association for Computational Linguistics"),
    ("CL", "Computational Linguistics"),
    ("JMLR", "Journal of Machine Learning Research"),
    ("AI", "Artificial Intelligence"),
    ("JAIR", "Journal of Artificial Intelligence Research"),
    ("TASLP", "IEEE/ACM Transactions on Audio, Speech, and Language Processing"),
]

# CVF Open Access (official proceedings) — used as the DIRECT official-source
# channel for CV/MM conferences (per 顶会.md). DBLP is flaky on CVPR, so this
# is both a supplement and a robust fallback.
CVF_CONFS = {
    "CVPR": [2020, 2021, 2022, 2023, 2024, 2025, 2026],
    "ICCV": [2019, 2021, 2023, 2025],
    "ECCV": [2020, 2022, 2024],
}
CVF_BASE = "https://openaccess.thecvf.com"

def get_json(u, retries=5):
    # Route through the shared retrying http_get so transient 5xx/429/timeout
    # on DBLP don't silently drop an entire venue's harvest.
    try:
        return json.loads(http_get(u, headers={"User-Agent": "Mozilla/5.0"},
                                   timeout=30, retries=retries))
    except Exception:
        return None

def dblp_authors(info):
    a = info.get("authors", {}).get("author", [])
    if isinstance(a, dict):
        a = [a]
    names = [x.get("text", "") for x in a if x.get("text")]
    if not names:
        return "Unknown"
    if len(names) <= 2:
        return " and ".join(names)
    last = names[0].split()[-1] if names[0].split() else names[0]
    return f"{last} et al."

# Relevance rule (final, per user instruction "标题要带hallucination"):
#   HARD GATE — the title MUST contain the stem "hallucinat" so that
#   hallucination/hallucinations/hallucinate/hallucinating/hallucinated all
#   qualify. (Substring "hallucination" was WRONG: it silently rejected verb
#   forms, e.g. "FINER: MLLMs Hallucinate under Fine-grained Negative
#   Queries" @ CVPR2026.) DBLP's `q=hallucinat` and arXiv's
#   all:"hallucination" can match the term in the ABSTRACT too, so we must
#   re-check the title explicitly rather than trust the query.
#   We ONLY drop clearly off-topic medical/psychiatric hallucinations that have
#   nothing to do with AI/ML model behavior. No verb/subject heuristic — a
#   hallucination-in-title paper is assumed to be about the phenomenon.
def relevant(title, venue):
    if "hallucinat" not in title.lower():
        return False
    if OFF_TOPIC.search(title):
        return False
    return True

def collect_dblp():
    out = []
    for vk in DBLP_VENUE_KEYS:
        q = urllib.parse.quote(f"hallucinat venue:{vk}")
        u = f"https://dblp.org/search/publ/api?q={q}&format=json&h=1000"
        d = get_json(u)
        if not d:
            print(f"  DBLP {vk}: query failed; skip")
            continue
        hits = d.get("result", {}).get("hits", {}).get("hit", [])
        n = 0
        for h in hits:
            info = h["info"]
            t = info.get("title", {})
            title = t.get("text", t) if isinstance(t, dict) else t
            title = title.strip().rstrip(".")
            year = int(info.get("year", 0))
            venue = info.get("venue", "")
            if year < 2020:
                continue
            if not relevant(title, venue):
                continue
            key = norm(title)
            if key in SEEN:
                continue
            SEEN.add(key)
            ee = info.get("ee", "") or ""
            vlabel = (venue or "").split()[0] if venue else vk
            out.append({
                "title": title,
                "authors": dblp_authors(info),
                "url": ee,                 # official DOI; arXiv abstract added later if found
                "year": year,
                "source": f"DBLP:{vlabel}",
            })
            n += 1
        print(f"  DBLP {vk}: {len(hits)} hits, {n} new")
        time.sleep(2)
    print(f"  DBLP total -> {len(out)} new")
    return out

def collect_arxiv():
    out = []
    queries = [
        'all:"hallucination" AND (all:"vision-language" OR all:"vision language")',
        'all:"hallucination" AND (all:MLLM OR all:LVLM OR all:VLM OR all:LMM)',
        'all:"hallucination" AND all:"multimodal large language"',
        'all:"hallucination" AND all:"object hallucination"',
        'all:"hallucination" AND all:"large vision"',
        'all:"hallucination" AND (all:"large language model" OR all:"LLM")',
        'all:"hallucination" AND all:"visual"',
        'all:"hallucination" AND all:"image captioning"',
    ]
    ns = {"a": "http://www.w3.org/2005/Atom"}
    for q in queries:
        u = (f"https://export.arxiv.org/api/query?search_query={urllib.parse.quote(q)}"
             f"&start=0&max_results=200&sortBy=submittedDate&sortOrder=descending")
        try:
            txt = http_get(u, headers={"User-Agent": "Mozilla/5.0"}, timeout=30, retries=5)
            root = ET.fromstring(txt)
        except Exception as e:
            print("  arXiv ERR", e); time.sleep(3); continue
        for e in root.findall("a:entry", ns):
            title = (e.find("a:title", ns).text or "").strip().replace("\n", " ")
            pub = e.find("a:published", ns).text or ""
            year = int(pub[:4])
            if year < 2020:
                continue
            if not relevant(title, "arXiv"):
                continue
            aid = e.find("a:id", ns).text
            m = re.search(r"arxiv\.org/abs/(\d{4}\.\d{4,5})", aid)
            if not m:
                continue
            url = f"https://arxiv.org/abs/{m.group(1)}"
            key = norm(title)
            if key in SEEN:
                continue
            SEEN.add(key)
            authors = [a.find("a:name", ns).text for a in e.findall("a:author", ns)]
            if len(authors) <= 2:
                ast = " and ".join(authors)
            else:
                ast = (authors[0].split()[-1] if authors[0].split() else authors[0]) + " et al."
            out.append({
                "title": title, "authors": ast, "url": url,
                "year": year, "source": "arXiv",
            })
        print(f"  arXiv q done -> {len(out)} so far")
        time.sleep(3)
    return out

def crossref_authors(item):
    aus = item.get("author", []) or []
    names = []
    for a in aus[:3]:
        fam = a.get("family", "")
        given = a.get("given", "")
        names.append((given + " " + fam).strip() or a.get("name", ""))
    if not names:
        return "Unknown"
    if len(names) <= 2:
        return " and ".join(names)
    return (names[0].split()[-1] if names[0].split() else names[0]) + " et al."

def pub_year(item):
    for k in ("published-print", "published-online", "published"):
        d = item.get(k)
        if d and d.get("date-parts") and d["date-parts"][0]:
            return int(d["date-parts"][0][0])
    return 0

def collect_journals():
    """Harvest hallucination papers from major journals via Crossref.
    Uses container-title scoping + a 'hallucination' bibliographic query, 2020+."""
    out = []
    for code, name in JOURNALS:
        q = urllib.parse.urlencode({
            "query.bibliographic": "hallucination",
            "query.container-title": name,
            "filter": "from-pub-date:2020-01-01",
            "rows": 50,
            "select": "title,container-title,published-print,published-online,published,DOI,author",
        })
        u = f"https://api.crossref.org/works?{q}"
        try:
            d = json.loads(http_get(u, headers={"User-Agent": "mailto:halu-bot@example.com"},
                                     timeout=30, retries=5))
        except Exception as e:
            print(f"  Journal {code}: ERR {e}"); time.sleep(2); continue
        n = 0
        for it in d.get("message", {}).get("items", []):
            title = (it.get("title") or [""])[0]
            if "hallucinat" not in title.lower():
                continue
            year = pub_year(it)
            if year and year < 2020:
                continue
            if not relevant(title, code):
                continue
            key = norm(title)
            if key in SEEN:
                continue
            SEEN.add(key)
            doi = it.get("DOI", "")
            out.append({
                "title": title,
                "authors": crossref_authors(it),
                "url": f"https://doi.org/{doi}" if doi else "",
                "year": year,
                "source": f"Crossref:{code}",
            })
            n += 1
        print(f"  Journal {code}: {n} new")
        time.sleep(1)
    print(f"  Journal total -> {len(out)} new")
    return out

def collect_cvf():
    """Direct official-source harvest from CVF Open Access (CVPR/ICCV/ECCV).
    Honors the 顶会.md official-proceedings links; robust fallback for CVPR."""
    out = []
    for conf, years in CVF_CONFS.items():
        for y in years:
            url = f"{CVF_BASE}/{conf}{y}?day=all"
            try:
                # NOTE: ?day=all pages can exceed 12 MB (CVPR2026 has 4000+
                # papers), so use a generous timeout — 30s used to silently
                # miss entire conferences. http_get adds retry/backoff so a
                # transient failure doesn't drop a whole conference.
                html = http_get(url, headers={"User-Agent": "Mozilla/5.0"}, timeout=300, retries=5)
            except Exception as e:
                print(f"  CVF {conf}{y}: ERR {e}"); time.sleep(1); continue
            # Two page layouts exist:
            #   old: <dt class="ptitle"><a href="..">T</a></dt>...<dd class="auth">Authors</dd>
            #   new (2026+): <dt class="ptitle"><br><a href="..">T</a></dt> then a <dd>
            #        holding per-author <form class="authsearch"> with
            #        <input name="query_author" value="Name">.
            # Parse by splitting on ptitle blocks and reading authors from either shape.
            chunks = re.split(r'<dt class="ptitle">', html)[1:]
            blocks = []
            for ch in chunks:
                am = re.search(r'<a[^>]*href="([^"]+)"[^>]*>(.*?)</a>', ch, re.S)
                if not am:
                    continue
                old_auth = re.search(r'<dd class="auth">(.*?)</dd>', ch, re.S)
                if old_auth:
                    auth_raw = old_auth.group(1)
                else:
                    names = re.findall(r'name="query_author"\s+value="([^"]+)"', ch)
                    auth_raw = ", ".join(names)
                blocks.append((am.group(1), am.group(2), auth_raw))
            n = 0
            for href, t_raw, auth_raw in blocks:
                title = re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", t_raw)).strip()
                if "hallucinat" not in title.lower():
                    continue
                if not relevant(title, conf):
                    continue
                key = norm(title)
                if key in SEEN:
                    continue
                SEEN.add(key)
                href = re.sub(r"^(\.\./)+", "", href)
                if href.startswith("/"):
                    href = CVF_BASE + href
                else:
                    href = CVF_BASE + "/" + href
                authors = re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", auth_raw)).strip() or "CVF"
                out.append({
                    "title": title,
                    "authors": authors,
                    "url": href,
                    "year": y,
                    "source": f"CVF:{conf}",
                })
                n += 1
            print(f"  CVF {conf}{y}: {n} new")
            time.sleep(1)
    print(f"  CVF total -> {len(out)} new")
    return out

def main():
    # resume: seed SEEN from any previously collected candidates
    out = []
    if os.path.exists(OUT):
        with open(OUT, encoding="utf-8") as f:
            out = json.load(f)
        for p in out:
            SEEN.add(norm(p["title"]))
    need_arxiv = not any(p.get("source") == "arXiv" for p in out)
    need_dblp = not any(p.get("source", "").startswith("DBLP:") for p in out)
    # journals (Crossref) and CVF pages can be large/slow (CVF single page
    # exceeds 12 MB), so apply the same resume guard as dblp/arxiv: skip the
    # channel entirely while un-reviewed candidates already exist, to avoid
    # re-querying the network on every re-run.
    need_journals = not any(p.get("source", "").startswith("Crossref:") for p in out)
    need_cvf = not any(p.get("source", "").startswith("CVF:") for p in out)

    dblp, arx, jour, cvf = [], [], [], []
    if need_dblp:
        print("Collecting from DBLP ...")
        dblp = collect_dblp()
    else:
        print("DBLP already collected, skipping (pending review in candidates_new.json).")
    if need_arxiv:
        print("Collecting from arXiv ...")
        arx = collect_arxiv()
    else:
        print("arXiv already collected, skipping (pending review in candidates_new.json).")
    if need_journals:
        print("Collecting journals (Crossref) ...")
        jour = collect_journals()
    else:
        print("Journals already collected, skipping (pending review in candidates_new.json).")
    if need_cvf:
        print("Collecting CVF Open Access (CVPR/ICCV/ECCV) ...")
        cvf = collect_cvf()
    else:
        print("CVF already collected, skipping (pending review in candidates_new.json).")
    merged = out + dblp + arx + jour + cvf
    # final dedup by normalized title (arXiv ID / DOI handled upstream)
    uniq = {}
    for p in merged:
        k = norm(p["title"])
        if k not in uniq:
            uniq[k] = p
    merged = list(uniq.values())
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as f:
        json.dump(merged, f, ensure_ascii=False, indent=2)
    by_src = {}
    by_year = {}
    for p in merged:
        by_src[p["source"].split(":")[0]] = by_src.get(p["source"].split(":")[0], 0) + 1
        by_year[p["year"]] = by_year.get(p["year"], 0) + 1
    print(f"\nTOTAL new candidates: {len(merged)}")
    print("by source:", by_src)
    print("by year:", dict(sorted(by_year.items())))

if __name__ == "__main__":
    main()
