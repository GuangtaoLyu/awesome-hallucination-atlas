# Contributing Guide

Thank you for contributing to **Awesome Hallucination Atlas**! This repository auto-generates the README tables and the interactive website from a **single source of data** (`data/seed.json`), so you only need to add **one data entry** — everything else (classification, statistics, and the website) updates automatically.

---

## 🧩 Data Flow

```
data/seed.json + data/manual_entries.yaml   ← the only files you need to edit
        │
        ▼  python scripts/fetch_abstracts.py   (fetch arXiv abstracts + publication dates, incremental cache)
        ├── data/abstracts.json    abstract cache (only new entries are fetched)
        ▼  python scripts/enrich_links.py      (optional: fill in links / code / venue info, incremental cache)
        ├── data/found_links.json  paper links recovered via arXiv title search
        ├── data/code_links.json   GitHub code links (abstract extraction + GitHub search)
        ├── data/venue_links.json  DBLP official publication records (venue / year / official link)
        ▼  python scripts/generate.py          (auto-classify from the full abstract text)
        ├── data/papers.json     structured data (with taxonomy fields and full abstracts)
        ├── docs/papers.json     read by the website (supports full-text abstract search)
        └── scripts/gen_readme.py  →  README.md (stats + navigation), PAPERS.md (index),
                                     papers/<year>.md (full list, split by year)
```

> 📌 **Venue-priority principle**: if a paper has an official conference/journal record in DBLP (not CoRR), the entry's **source, date, and primary link use the official venue info** (e.g. `CVPR 2024` + a DOI link), and the arXiv link is kept as a supplement.

> ⚠️ **Do not commit generated artifacts.** `README.md`, `README.zh-CN.md`, `PAPERS.md`, `PAPERS.zh-CN.md`, `papers/<year>.md`, `data/papers.json`, `docs/papers*.json` and the abstract/link caches are all rebuilt by the daily pipeline. A PR should contain **only** the data-source change (`data/seed.json` or `data/manual_entries.yaml`). The paper list is split per year because GitHub silently truncates READMEs past 500 KiB; regenerating it with an older script reverts that split.

---

## ➕ How to Add a Paper

### 1. Edit `data/seed.json`

Add one record to the JSON array (or, for a single recovered / venue-only paper, one `- title:` block to `data/manual_entries.yaml`):

```json
["Full paper title", "First Author et al.", "paper URL", 2026]
```

**Field reference:**

| # | Field | Required | Notes |
|---|-------|----------|-------|
| 1 | `title` | ✅ | Full English title, preserving original capitalization and colons |
| 2 | `authors` | ✅ | Usually `Firstauthor et al.`; use `Anonymous et al.` if unknown |
| 3 | `url` | recommended | arXiv abs / ACL / IEEE / Springer link; leave as empty string `""` if none yet |
| 4 | `year` | ✅ | Publication year (for arXiv, the script auto-corrects from the ID; fill in your best guess) |

**Example:**

```json
["HALC: Object Hallucination Reduction via Adaptive Focal-Contrast Decoding", "Chen et al.", "https://arxiv.org/abs/2403.00425", 2024]
```

### 2. Regenerate

```bash
python scripts/generate.py          # rebuild papers.json + docs + README
python scripts/gen_readme.py        # rebuild README + PAPERS index + papers/<year>.md
python scripts/audit.py --strict    # verify invariants (CI runs this too)
```

Pipeline: deduplicate → auto-classify from the **full abstract text** (model / method / scene) → update statistics → rewrite README and website data. Non-arXiv papers (IEEE / ACL / Springer) cannot fetch abstracts automatically yet and fall back to title-based classification; feel free to correct them manually in your PR.

### 3. Open a PR

```bash
git add data/seed.json             # or data/manual_entries.yaml
git commit -m "docs: add <paper short name> (<year>)"
git push

The daily GitHub Action regenerates everything else. If you ran the scripts locally, revert the generated files before committing (`git checkout -- README.md README.zh-CN.md PAPERS.md PAPERS.zh-CN.md papers/ data/papers.json docs/`).
```

---

## 🏷️ Automatic Taxonomy (for reference)

The script applies rule-based analysis to the **title + full arXiv abstract** and labels 4 dimensions. If a result looks wrong, point it out in your PR and a maintainer will add rules in `generate.py`.

| Dimension | Values | Signals (based on the abstract, partial) |
|-----------|--------|------------------------------------------|
| **Model type** | `VLM` / `MLLM (Omni)` / `LLM` | omni / audio / speech / any-to-any → MLLM (Omni, true full-modal); vision-language / LVLM / video-LLM / self-claimed MLLM but image-text only → VLM; pure text → LLM |
| **Method type** | `Training-free` / `Training-based` / `Evaluation` | explicit "training-free / inference-time / without training" → Training-free; "we fine-tune / DPO / RL / preference optimization" → Training-based; "introduce a benchmark / survey / pure analysis with no mitigation" → Evaluation |
| **Hallucination scene** | `Object` / `Attribute` / `Relation` / `General` | object hallucination / non-existent object in abstract → Object; attribute / counting / verb → Attribute; relation(ship) → Relation |
| **Extra tags** | `Video` `Audio` `Multilingual` `Medical` `3D` `Agent` | modality / domain signals in the abstract |

---

## 🔗 Adding Code Links

Most raw entries lack code links. If you know a paper's official repository:

1. Edit `data/code_links.json` directly — the key is the **normalized title** (lowercase, all non-alphanumeric characters removed) and the value is the GitHub repo link;
2. Or provide a list of **[title + code link]** in your PR and a maintainer will enter them;
3. Re-run `python scripts/generate.py`.

Likewise, venue acceptance info can be edited in `data/venue_links.json` (format `{"venue": "CVPR", "year": 2025, "ee": "official link"}`), or fetched incrementally from DBLP via `python scripts/enrich_links.py venue`.

> We encourage prioritizing **official implementation** links; please note when a link is a community reimplementation.

---

## ✅ Pre-submission Checklist

- [ ] Title is not duplicated (the script dedupes by normalized title, but please confirm it is not a re-submission under a different name)
- [ ] Link is accessible; prefer the arXiv abstract page
- [ ] `python scripts/generate.py` ran without errors
- [ ] `README.md` and `docs/papers.json` are updated and committed together
- [ ] Commit message is concise and clear

---

## 💡 Other Ways to Contribute

- 🐛 Fix incorrect classification / authors / links
- 🌍 Improve multilingual (Chinese/English) abstracts
- 🎨 Improve the styling and features of the `docs/` interactive website
- 📊 Propose new taxonomy dimensions or statistical views

If you have any questions, feel free to open an Issue. Happy contributing! 🎉
