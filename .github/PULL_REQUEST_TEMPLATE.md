## Description
<!-- What does this PR add or fix? -->

## Type of change
- [ ] Add paper(s)
- [ ] Fix classification / link / metadata
- [ ] Improve the interactive website (`docs/`)
- [ ] Pipeline / script improvement

## How to add a paper (preferred)
Add one record to `data/seed.json`:
```json
["Paper Full Title", "Firstauthor et al.", "https://arxiv.org/abs/XXXX.XXXXX", 2026]
```
For a single recovered / venue-only paper, a `- title:` block in `data/manual_entries.yaml` is also fine.

**Only the data source belongs in this PR.** The README, the per-year paper files and all JSON caches are rebuilt by the daily pipeline. Do **not** commit:
`README.md`, `README.zh-CN.md`, `PAPERS.md`, `PAPERS.zh-CN.md`, `papers/*.md`,
`data/papers.json`, `docs/papers*.json`, `data/abstracts*.json`, or any cache file.
The full list lives in `papers/<year>.md` because GitHub silently truncates READMEs past 500 KiB; regenerating with an older script reverts that split.

Local verification (optional):
```bash
python scripts/generate.py && python scripts/gen_readme.py && python scripts/audit.py --strict
```
Revert the generated files before committing, leaving only the data change. See [CONTRIBUTING.md](.github/CONTRIBUTING.md).

## Checklist
- [ ] PR contains **only** a data-source change (`data/seed.json` or `data/manual_entries.yaml`)
- [ ] No generated artifacts committed (README / PAPERS / papers/*.md / JSON caches / docs)
- [ ] `python scripts/audit.py --strict` passes (CI checks this too)
- [ ] Links are reachable (prefer arXiv abstract pages)
- [ ] Commit message is clear and concise
