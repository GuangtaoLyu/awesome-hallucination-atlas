# -*- coding: utf-8 -*-
"""
Single orchestrator for the hallucination research library update pipeline.

It encodes the *correct* ordering that was previously easy to get wrong. The
venue-enrichment step (update_arxiv_venues.py) reads docs/papers.json — an
OUTPUT of generate.py — so the pipeline MUST run generate before it, then
generate again to apply the resolved venues.

Once the library exists, the *enrichment* steps (abstracts / code links /
resolved URLs) read data/papers.json and write caches that generate consumes.
Those are therefore run AFTER the first generate and BEFORE the second one, so
newly-fetched papers get their abstracts and code links in the same run.

Usage:
    python update_pipeline.py                 # fetch arXiv + venues -> generate + audit
    python update_pipeline.py --skip-fetch    # incremental.json already fresh; just rebuild
    python update_pipeline.py --no-audit      # skip the final audit
    python update_pipeline.py --check         # offline integrity check only (audit), no changes
    python update_pipeline.py --with-abstracts  # also crawl publisher sites for missing abstracts
    python update_pipeline.py --enrich        # fetch arXiv abstracts + Crossref/publisher abstracts
                                            #   + GitHub code links + resolve URLs/venues
    python update_pipeline.py --collect       # also harvest DBLP/Crossref/CVF -> merge into seed.json
    python update_pipeline.py --collect-2026  # also harvest 2026 proceedings -> merge into seed.json
    python update_pipeline.py --full          # --collect + --collect-2026 + --enrich
    python update_pipeline.py --backfill --from 20240101   # one-off historical fill
    python update_pipeline.py --serve         # after updating, serve docs/ locally for preview
"""
import os
import sys
import json
import argparse
import subprocess
import datetime

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
DOCS = os.path.join(ROOT, "docs")
PY = sys.executable
if HERE not in sys.path:
    sys.path.insert(0, HERE)
from lib_common import norm_title  # noqa: E402


def run(script, *args):
    cmd = [PY, os.path.join(HERE, script)] + list(args)
    print(f"\n========== [pipeline] {script} {' '.join(args)} ==========")
    rc = subprocess.call(cmd, cwd=ROOT)
    if rc != 0:
        print(f"[pipeline] ERROR: {script} exited with code {rc}", file=sys.stderr)
        sys.exit(rc)
    return rc


def sync_venue_years():
    """Rebuild data/venue_years.json from the freshly generated data/papers.json.

    venue_years.json is the committed cold-checkout fallback for the paper year
    (see generate.py). Keeping it in lock-step with papers.json means a fresh
    clone / CI checkout always reproduces the correct conference years even when
    the gitignored enrichment cache (venue_links.json) is absent. No-op with a
    warning if papers.json is missing; never fails the pipeline.
    """
    ppath = os.path.join(ROOT, "data", "papers.json")
    if not os.path.exists(ppath):
        print("[sync_venue_years] skip: data/papers.json not found", file=sys.stderr)
        return
    try:
        data = json.load(open(ppath, encoding="utf-8"))
        papers = data["papers"] if isinstance(data, dict) and "papers" in data else data
        out = {}
        for p in papers:
            t = (p.get("title") or "").strip()
            y = p.get("year")
            if t and y:
                out[norm_title(t)] = int(y)
        opath = os.path.join(ROOT, "data", "venue_years.json")
        with open(opath, "w", encoding="utf-8") as f:
            json.dump(out, f, ensure_ascii=False, indent=0, sort_keys=True)
        print(f"[sync_venue_years] wrote {len(out)} entries -> data/venue_years.json")
    except Exception as ex:
        print(f"[sync_venue_years] skip: {ex!r}", file=sys.stderr)


def git_commit(ran):
    """Commit the pipeline result so every run is revertible.

    Called only AFTER audit passes, so committed states are always verified
    good builds. gitignore excludes regenerable caches/buffers, so only the
    source of truth (seed.json / manual_entries.yaml / configs) and generated
    deliverables (papers.json / docs/ / README.md) are tracked.

    No-op (with a warning) if git is unavailable or there is nothing to stage;
    never fails the pipeline.

    NOTE: this only ever *commits* — it never pushes, so a local run cannot
    touch the remote by surprise. Automation must push explicitly (see
    .github/workflows/scheduled-update.yml). The absence of that push is why
    the weekly job appeared to do nothing: it committed to a throwaway runner.
    """
    try:
        subprocess.check_output(["git", "rev-parse", "--is-inside-work-tree"],
                                cwd=ROOT, stderr=subprocess.DEVNULL)
    except Exception:
        print("[pipeline] git: not a git repo, skipping auto-commit")
        return
    subprocess.call(["git", "add", "-A"], cwd=ROOT)
    st = subprocess.run(["git", "status", "--porcelain"], cwd=ROOT,
                        capture_output=True, text=True)
    if not st.stdout.strip():
        print("[pipeline] git: nothing changed, no commit needed")
        return
    n_changed = len([l for l in st.stdout.splitlines() if l.strip()])
    try:
        with open(os.path.join(ROOT, "data", "papers.json"), encoding="utf-8") as f:
            d = json.load(f)
        n_papers = len(d["papers"]) if isinstance(d, dict) and "papers" in d else len(d)
    except Exception:
        n_papers = None
    stamp = datetime.date.today().strftime("%Y-%m-%d")
    steps = " -> ".join(ran)
    msg = (f"update({stamp}): pipeline run, {n_changed} file(s) changed"
           + (f", {n_papers} papers" if n_papers is not None else "")
           + f"\n\nsteps: {steps}")
    rc = subprocess.call(["git", "commit", "-q", "-m", msg], cwd=ROOT)
    if rc == 0:
        print(f"[pipeline] git: committed {n_changed} file(s) "
              f"({n_papers} papers) — revert with 'git revert HEAD'")
    else:
        print("[pipeline] git: commit returned non-zero; changes left staged",
              file=sys.stderr)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--skip-fetch", action="store_true",
                    help="skip arXiv fetch (assume data/incremental.json already fresh)")
    ap.add_argument("--with-abstracts", action="store_true",
                    help="crawl publisher sites for missing abstracts (fetch_abstracts_web.py)")
    ap.add_argument("--abstracts", action="store_true",
                    help="enrich abstracts from Crossref JATS (enrich_abstracts.py)")
    ap.add_argument("--fetch-abstracts", action="store_true",
                    help="refresh the arXiv abstract cache data/abstracts.json (fetch_abstracts.py)")
    ap.add_argument("--code", action="store_true",
                    help="find GitHub 'official' code links (fetch_code.py)")
    ap.add_argument("--links", action="store_true",
                    help="resolve missing URLs + code-from-abstracts + DBLP venues (enrich_links.py)")
    ap.add_argument("--enrich", action="store_true",
                    help="umbrella: --fetch-abstracts + --abstracts + --with-abstracts + --code + --links")
    ap.add_argument("--collect", action="store_true",
                    help="harvest new candidates from DBLP/Crossref/CVF (collect_candidates.py) then merge into seed.json")
    ap.add_argument("--collect-2026", action="store_true",
                    help="harvest 2026 conference proceedings (collect_2026.py) then merge into seed.json")
    ap.add_argument("--full", action="store_true",
                    help="one-shot full update: --collect + --collect-2026 + --enrich (then fetch + venues + generate + audit)")
    ap.add_argument("--no-audit", action="store_true",
                    help="skip the final audit step")
    ap.add_argument("--no-commit", action="store_true",
                    help="do not auto-commit the result with git (commit is on by default)")
    ap.add_argument("--check", action="store_true",
                    help="offline integrity check only (run audit.py, make no changes) and exit")
    ap.add_argument("--serve", action="store_true",
                    help="after updating, serve docs/ on a local static server for preview (blocks)")
    ap.add_argument("--port", type=int, default=8000,
                    help="port for --serve (default 8000)")
    ap.add_argument("--backfill", action="store_true",
                    help="pass --ti to fetch_new_arxiv.py for a high-precision backfill")
    ap.add_argument("--from", dest="from_date", default=None,
                    help="backfill start date YYYYMMDD (passed to fetch_new_arxiv.py)")
    ap.add_argument("--limit", type=int, default=None,
                    help="limit for update_arxiv_venues.py (debug only)")
    args = ap.parse_args()

    # --full is a convenience shortcut that turns on the discovery + enrichment channels.
    if args.full:
        args.collect = True
        args.collect_2026 = True
        args.enrich = True
    # --enrich turns on every individual enrichment step.
    if args.enrich:
        args.fetch_abstracts = True
        args.abstracts = True
        args.with_abstracts = True
        args.code = True
        args.links = True

    # Offline validation-only mode: report integrity and exit, touching nothing.
    # --strict makes audit exit non-zero on any critical invariant breach.
    if args.check:
        run("audit.py", "--strict")
        print("\n[pipeline] --check done. No files were modified.")
        return

    ran = []

    # 1. fetch new arXiv candidates (title-match, deduped, merged into incremental.json)
    if not args.skip_fetch:
        fetch_args = []
        if args.backfill:
            fetch_args += ["--ti"]
        if args.from_date:
            fetch_args += ["--from", args.from_date]
        run("fetch_new_arxiv.py", *fetch_args)
        ran.append("fetch_new_arxiv")

    # 1a. optionally harvest new candidates from DBLP/Crossref/CVF, then merge
    #     into seed.json (reviewed staging file -> seed). Wires the broad
    #     collect_candidates.py harvester into the automated pipeline so a
    #     single command can also *discover* new papers, not just fetch arXiv.
    if args.collect:
        run("collect_candidates.py")
        run("merge_candidates.py")
        ran.append("collect_candidates+merge")

    # 1b. optionally harvest 2026 conference proceedings, then merge candidates
    #     into seed.json — wires collect_2026.py into the automated pipeline
    #     (previously this was a manual, easy-to-forget step).
    if args.collect_2026:
        run("collect_2026.py")
        run("merge_candidates.py")
        ran.append("collect_2026+merge")

    # 2. materialize: docs/papers.json now contains the new papers (as preprints)
    run("generate.py")
    ran.append("generate#1")

    # 3. enrich venues: reads docs/papers.json, writes data/venue_links.json
    #    --force (set on backfill) re-checks cached-negative preprints so
    #    papers that got published since the last run are caught.
    va_args = []
    if args.backfill:
        va_args.append("--force")
    if args.limit is not None:
        va_args.append(str(args.limit))
    run("update_arxiv_venues.py", *va_args)
    ran.append("update_arxiv_venues")

    # 4. enrichment steps that read data/papers.json and write caches consumed
    #    by the final generate. Run here (after generate#1, before generate#2)
    #    so newly-fetched papers get abstracts + code links in the same run.
    if args.fetch_abstracts:
        run("fetch_abstracts.py")
        ran.append("fetch_abstracts")
    if args.abstracts:
        run("enrich_abstracts.py")
        ran.append("enrich_abstracts")
    if args.with_abstracts:
        run("fetch_abstracts_web.py")
        ran.append("fetch_abstracts_web")
    if args.code:
        run("fetch_code.py")
        ran.append("fetch_code")
    if args.links:
        run("enrich_links.py")
        ran.append("enrich_links")

    # 5. re-materialize: generate now applies the resolved venues + CCF ratings,
    #    abstracts, and code links.
    run("generate.py")
    ran.append("generate#2")

    # 5b. keep data/venue_years.json (the committed cold-checkout year fallback)
    #     in lock-step with papers.json so a fresh clone always reproduces the
    #     correct conference years.
    sync_venue_years()
    ran.append("venue_years")

    # 6. keep README.md in lock-step with the regenerated papers.json so the
    #    hand-written stats / 2000-line paper list can never drift from data.
    run("gen_readme.py")
    ran.append("readme")

    # 6. integrity check (md5 data==docs, CCF consistency, fields, duplicates).
    #    --strict makes audit exit non-zero on any critical invariant breach,
    #    so the pipeline aborts instead of declaring DONE on a broken build.
    if not args.no_audit:
        run("audit.py", "--strict")
        ran.append("audit")

    print("\n[pipeline] DONE. steps run: " + " -> ".join(ran))
    print("[pipeline] papers.json regenerated with venues + CCF + enrichment applied.")

    # 7. version the result: audit has passed, so this commit is a verified
    #    good build and any future run can be reverted with `git revert`.
    if not args.no_commit:
        git_commit(ran)

    # Optional: preview the generated site locally. Blocks until Ctrl-C.
    if args.serve:
        print(f"\n[pipeline] serving docs/ at http://localhost:{args.port}/  (Ctrl-C to stop)")
        subprocess.call([PY, "-m", "http.server", str(args.port),
                         "--directory", DOCS], cwd=ROOT)


if __name__ == "__main__":
    main()
