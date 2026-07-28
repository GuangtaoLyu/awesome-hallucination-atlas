#!/usr/bin/env python3
"""幻觉资源库正确性审计：对比 README 声明与 papers.json 真实统计，并校验硬不变量。

用法:
    python scripts/audit.py              # 打印全部检查项
    python scripts/audit.py --json       # 输出 JSON（供 CI/脚本消费）
"""
import json
import os
import re
import sys
import hashlib
from collections import Counter

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(ROOT, "data")
DOCS = os.path.join(ROOT, "docs")


def load(path):
    with open(path, encoding="utf-8") as f:
        return json.load(f)


from lib_common import norm_title


def venue_base(v):
    return re.sub(r"\s*\d{4}\s*$", "", (v or "").strip())


def md5(path):
    h = hashlib.md5()
    with open(path, "rb") as f:
        h.update(f.read())
    return h.hexdigest()


def check_links(papers, cap=300, timeout=8):
    """Optional dead-link scan (network). Returns list of (title, url, reason)
    for urls that fail a HEAD/GET. Capped to avoid long CI runs."""
    import urllib.request
    import urllib.error
    dead = []
    checked = 0
    for p in papers:
        url = p.get("url") or p.get("venue_url") or ""
        if not url or not url.startswith("http"):
            continue
        checked += 1
        if cap and checked > cap:
            break
        try:
            req = urllib.request.Request(url, method="HEAD",
                                         headers={"User-Agent": "halu-audit/1.0"})
            with urllib.request.urlopen(req, timeout=timeout) as r:
                if r.status >= 400:
                    dead.append((p.get("title"), url, f"HTTP {r.status}"))
        except urllib.error.HTTPError as e:
            dead.append((p.get("title"), url, f"HTTP {e.code}"))
        except Exception as e:
            dead.append((p.get("title"), url, type(e).__name__))
    return dead


def main(check_links_flag=False, link_cap=300):
    papers_path = os.path.join(DATA, "papers.json")
    docs_papers = os.path.join(DOCS, "papers.json")
    ccf_path = os.path.join(DATA, "ccf.json")

    db = load(papers_path)
    papers = db["papers"]
    n = len(papers)

    inv = {}
    inv["data_docs_md5_match"] = (
        os.path.exists(docs_papers) and md5(papers_path) == md5(docs_papers)
    )

    required = ["title", "venue", "year", "model_type", "method_type"]
    missing_fields = Counter()
    for p in papers:
        for k in required:
            if p.get(k) in (None, "", []):
                missing_fields[k] += 1

    seen, dups = set(), []
    for p in papers:
        k = norm_title(p.get("title", ""))
        if k in seen:
            dups.append(p.get("title"))
        seen.add(k)

    # 与 generate.py 完全一致的定义
    with_link = sum(1 for p in papers if p.get("url"))
    with_abs = sum(1 for p in papers if (p.get("abstract") or "").strip())
    with_code = sum(1 for p in papers if (p.get("code") or "").strip())
    top_venue = sum(1 for p in papers if p.get("venue_url"))  # 顶会正式发表 = 有官方 venue_url
    benchmarks = sum(1 for p in papers if p.get("benchmark"))

    ccf_counts = Counter(p.get("ccf") or "未收录" for p in papers)

    # 复核：papers.json 里存的 ccf 是否真的能在 ccf.json 中找到对应评级
    ccf_ok = True
    ccf_detail = []
    if os.path.exists(ccf_path):
        ccf_db = load(ccf_path)  # 扁平字典 {venue_base: "A"/"B"/"C"/""}
        for p in papers:
            vb = venue_base(p.get("venue", ""))
            if not vb:
                continue
            expected = ccf_db.get(vb, "")
            actual = p.get("ccf") or ""
            if actual != expected:
                ccf_ok = False
                ccf_detail.append((p.get("venue"), actual or "未收录",
                                   expected or "未收录(非CCF)"))
    else:
        ccf_detail.append(("ccf.json 缺失", "", ""))

    year_counts = Counter(p.get("year") for p in papers if p.get("year"))
    years = sorted(year_counts)
    year_min, year_max = (years[0], years[-1]) if years else (None, None)

    tagged = sum(1 for p in papers if p.get("benchmark"))

    # Orphan check: venue_links entries pointing to papers no longer present
    # (e.g. after a dedup/removal). Not a hard failure, but worth surfacing.
    orphan_venue = 0
    orphan_sample = []
    vl_path = os.path.join(DATA, "venue_links.json")
    if os.path.exists(vl_path):
        vl = load(vl_path)
        paper_keys = {norm_title(p.get("title", "")) for p in papers}
        for k in vl:
            if k not in paper_keys:
                orphan_venue += 1
                if len(orphan_sample) < 10:
                    orphan_sample.append(k)

    dead_links = []
    if check_links_flag:
        dead_links = check_links(papers, cap=link_cap)

    return {
        "total": n,
        "with_link": with_link,
        "with_abstract": with_abs,
        "with_code": with_code,
        "top_venue_published": top_venue,
        "ccf": dict(ccf_counts),
        "year_min": year_min,
        "year_max": year_max,
        "year_counts": {str(k): v for k, v in sorted(year_counts.items())},
        "benchmark_tagged": tagged,
        "invariants": inv,
        "missing_fields": dict(missing_fields),
        "duplicates": dups,
        "ccf_consistent_with_ccfjson": ccf_ok,
        "ccf_mismatches_sample": ccf_detail[:20],
        "orphan_venue_links": orphan_venue,
        "orphan_venue_sample": orphan_sample,
        "dead_links_checked": len(dead_links) if check_links_flag else None,
        "dead_links_sample": [(t, u, r) for t, u, r in dead_links[:10]],
    }


if __name__ == "__main__":
    check_links_flag = "--links" in sys.argv
    link_cap = 300
    for a in sys.argv:
        if a.startswith("--links-cap="):
            try:
                link_cap = int(a.split("=")[1])
            except Exception:
                pass
    strict = "--strict" in sys.argv
    res = main(check_links_flag=check_links_flag, link_cap=link_cap)
    if "--json" in sys.argv:
        print(json.dumps(res, ensure_ascii=False, indent=2))
    else:
        print("=== 硬不变量 ===")
        print("  data/ == docs/ papers.json (md5):", res["invariants"]["data_docs_md5_match"])
        print("  CCF 评级与 ccf.json 一致:", res["ccf_consistent_with_ccfjson"],
              f"({len(res['ccf_mismatches_sample'])} 处不符)")
        print("  venue_links 孤儿(指向已删论文):", res["orphan_venue_links"])
        if res["orphan_venue_links"]:
            print("    示例:", res["orphan_venue_sample"][:5])
        print("\n=== 真实统计 (papers.json) ===")
        print(f"  总数: {res['total']}")
        print(f"  含链接(url): {res['with_link']} | 含摘要: {res['with_abstract']} | 含代码: {res['with_code']} | 顶会正式发表(venue_url): {res['top_venue_published']}")
        print(f"  CCF: {res['ccf']}")
        print(f"  年份范围: {res['year_min']} - {res['year_max']}")
        print(f"  年份分布: {res['year_counts']}")
        print(f"  Benchmark 标记: {res['benchmark_tagged']}")
        print("\n=== 字段完整性 ===")
        print("  缺失字段计数:", res["missing_fields"] or "无")
        print(f"  重复标题: {len(res['duplicates'])} 篇 -> {res['duplicates'][:5]}")
        if check_links_flag:
            print(f"\n=== 死链检查 (抽查 {res['dead_links_checked']}) ===")
            print("  死链:", res["dead_links_sample"] or "无")

    # CI gate: exit non-zero on any critical invariant breach.
    if strict:
        critical = not (
            res["invariants"]["data_docs_md5_match"]
            and res["ccf_consistent_with_ccfjson"]
            and not res["missing_fields"]
            and not res["duplicates"]
        )
        if critical:
            print("\n[audit] STRICT mode: critical invariant FAILED.", file=sys.stderr)
            sys.exit(1)
        print("\n[audit] STRICT mode: all critical invariants OK.")
