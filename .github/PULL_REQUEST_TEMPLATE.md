## Description
<!-- What does this PR add or fix? -->

## Type of change
- [ ] Add paper(s)
- [ ] Fix classification / link / metadata
- [ ] Improve the interactive website (`docs/`)
- [ ] Pipeline / script improvement

## How to add a paper (preferred)
Add one line to `data/seed.json`:
```json
["Paper Full Title", "Firstauthor et al.", "https://arxiv.org/abs/XXXX.XXXXX", 2026]
```
Then run `python scripts/generate.py` to regenerate README + `docs/`. See [CONTRIBUTING.md](.github/CONTRIBUTING.md).

## Checklist
- [ ] `python scripts/generate.py` ran without error; README + `docs/` updated
- [ ] `python scripts/audit.py --strict` passes (CI checks this too)
- [ ] Links are reachable (prefer arXiv abstract pages)
- [ ] Commit message is clear and concise
