"""Regenerate the drift-prone parts of README.md from data/papers.json.

The README is hand-maintained prose PLUS several data-driven blocks that must
stay in lock-step with papers.json (otherwise numbers / the 2000-line paper
list silently rot). This script rewrites exactly those blocks and nothing else:

  * the shields.io badges at the top (Papers / Abstract / Last Update)
  * `## 📊 数据概览`          -> stats tables + venue breakdown + CCF
  * `## 📋 评测与 Benchmark`  -> the Benchmark list (inside <details>)
  * `## 📚 综述 Survey`        -> the Survey list (inside <details>)
  * `## 📚 论文列表`           -> the year-grouped full list

Everything else (分类体系, 推荐引用, 贡献, 许可, the prose blurbs) is preserved
verbatim. Each block is located by its `## ` heading; the heading line itself is
kept, only the body up to the next `## ` heading is replaced. So the script is
safe to re-run after every pipeline update and idempotent when data is unchanged.

Stdlib only. Run:  python scripts/gen_readme.py
"""

import datetime
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
PAPERS = os.path.join(ROOT, "data", "papers.json")
README = os.path.join(ROOT, "README.md")

MODEL_LABEL = {"VLM": "VLM", "MLLM": "MLLM(Omni)", "LLM": "LLM"}
ALWAYS_LIST_DEFAULT = ["TNNLS", "TASLP", "TAI", "PRCV"]
BAR_W = 20


def bar(pct, width=BAR_W):
    pct = max(0.0, min(100.0, pct))
    filled = int(round(pct / 100.0 * width))
    return "█" * filled + "░" * (width - filled)


def venue_base(v):
    v = (v or "").strip()
    if not v:
        return "未标注"
    v = re.sub(r"\s+\d{4}$", "", v)  # drop trailing year
    return v


def load_papers():
    d = json.load(open(PAPERS, encoding="utf-8"))
    return d["papers"] if isinstance(d, dict) and "papers" in d else d


def load_stats():
    p = os.path.join(ROOT, "data", "stats.json")
    if os.path.exists(p):
        try:
            return json.load(open(p, encoding="utf-8"))
        except Exception:
            return {}
    return {}


def date_key(p):
    if p.get("date"):
        return p["date"]
    if p.get("month"):
        return f"{p['year']}-{p['month']:02d}-00"
    return f"{p['year']}-00-00"


# ----------------------------------------------------------------------------
# block generators
# ----------------------------------------------------------------------------

def gen_stats(papers, stats):
    total = len(papers)
    with_link = sum(1 for p in papers if p.get("url"))
    with_abs = sum(1 for p in papers if p.get("abstract"))
    with_code = sum(1 for p in papers if p.get("code"))
    top_pub = sum(1 for p in papers if p.get("venue_url"))
    years = [p["year"] for p in papers if p.get("year")]
    ymin, ymax = min(years), max(years)

    # year distribution
    by_year = {}
    for p in papers:
        by_year[p["year"]] = by_year.get(p["year"], 0) + 1
    year_rows = ""
    for y in sorted(by_year, reverse=True):
        n = by_year[y]
        pct = n / total * 100
        year_rows += f"| {y} | {n} | `{bar(pct)}` {pct:.1f}%\n"

    # model distribution
    by_model = {}
    for p in papers:
        by_model[p["model_type"]] = by_model.get(p["model_type"], 0) + 1
    model_desc = {
        "VLM": "视觉语言模型（LVLM，含自称 MLLM 但仅处理图像/视频+文本的工作）",
        "MLLM": "全模态模型（Omni：音频 / 语音 / any-to-any）",
        "LLM": "纯语言大模型",
    }
    model_rows = ""
    for k in ["VLM", "MLLM", "LLM"]:
        model_rows += f"| **{MODEL_LABEL[k]}** | {model_desc[k]} | {by_model.get(k, 0)} |\n"

    # method distribution
    by_method = {}
    for p in papers:
        by_method[p["method_type"]] = by_method.get(p["method_type"], 0) + 1
    method_rows = (
        f"| **Training-free** | 免训练（解码干预 / 注意力校准 / 表征引导等） | {by_method.get('Training-free', 0)} |\n"
        f"| **Training-based** | 基于训练（偏好优化 / 微调 / 强化学习等） | {by_method.get('Training-based', 0)} |\n"
    )

    # venue distribution + "其他" detail
    venue_table, other_detail = gen_venue(papers, total, stats)

    # CCF distribution
    by_ccf = {}
    for p in papers:
        by_ccf[p.get("ccf") or "未收录"] = by_ccf.get(p.get("ccf") or "未收录", 0) + 1
    ccf_rows = ""
    for k in ["A", "B", "C", "未收录"]:
        n = by_ccf.get(k, 0)
        pct = n / total * 100
        label = f"CCF-{k}" if k != "未收录" else "未收录"
        ccf_rows += f"| {label} | {n} | `{bar(pct)}` {pct:.1f}%\n"

    n_bench = sum(1 for p in papers if p.get("benchmark") or "Benchmark" in (p.get("tags") or []))
    n_surv = sum(1 for p in papers if p.get("survey"))

    intro = (
        f"- **论文总数**：`{total}` 篇（已去重）\n"
        f"- **含论文链接**：`{with_link}` 篇 · **含全文摘要**：`{with_abs}` 篇 · **含代码链接**：`{with_code}` 篇 · **顶会正式发表**：`{top_pub}` 篇\n"
        "- 顶会正式发表的论文：**时间与链接优先采用会议官方信息**（DBLP 记录），其余采用 arXiv 信息\n"
        f"- **覆盖年份**：{ymin} – {ymax}\n"
    )

    # Venue distribution is wrapped in <details> (the table + the nested
    # "其他" detail can get long). Blank lines separate every <details>
    # boundary so GitHub/CommonMark does not merge adjacent HTML blocks,
    # which would silently break the collapse and the nested detail.
    venue_block = (
        "<details>\n"
        "<summary>📊 按会议 / 期刊分布（点击折叠 / 展开）</summary>\n\n"
        "### 按会议 / 期刊分布\n\n"
        "> 已正式发表在会议 / 期刊的论文按 venue 统计（顶会官方信息优先）；`arXiv（预印本）` 为尚未正式录用的预印本。小众期刊 / 小会、研讨会 / 卫星会 / 边会等次级 venue 以及各仅 1 篇的 venue 统一归入「其他」行，明细见表下折叠区；`其他` 中仍含少量 DOI 无法解析出处的条目，`未标注` 为无任何链接、暂无法判定的条目。\n\n"
        "| 会议 / 期刊 | 数量 | 占比 |\n"
        "|-------------|------|------|\n"
        f"{venue_table}"
        "\n"
        f"{other_detail}"
        "\n</details>"
    )

    ccf_block = (
        "### 按 CCF 评级分布\n\n"
        "> 依据 **CCF 推荐国际学术会议 / 期刊目录（2022）** 对正式发表的论文标注评级；`未收录` 含 arXiv 预印本、暂未解析出 venue 的条目，以及 CCF 目录之外的会议 / 期刊。\n\n"
        "| CCF 评级 | 数量 | 占比 |\n"
        "|----------|------|------|\n"
        f"{ccf_rows}"
        f"> 📋 另有 `{n_bench}` 篇 **评测 / Benchmark** 论文、📚 `{n_surv}` 篇 **综述 Survey** 论文，作为独立标记单独列出（见下方对应小节），不占用方法分类。\n\n"
        "---\n"
    )

    blocks = [
        intro.rstrip("\n"),
        "### 按年份分布\n\n| 年份 | 数量 | 占比 |\n|------|------|------|\n" + year_rows,
        "### 按模型类型分布\n\n| 模型类型 | 说明 | 数量 |\n|----------|------|------|\n" + model_rows,
        "### 按方法类型分布\n\n| 方法类型 | 说明 | 数量 |\n|----------|------|------|\n" + method_rows,
        venue_block,
        ccf_block.rstrip("\n"),
    ]
    return "\n\n".join(blocks) + "\n"


def gen_venue(papers, total, stats):
    named = {}
    arx = 0
    unlabeled = 0
    for p in papers:
        vb = venue_base(p.get("venue"))
        if vb == "arXiv":
            arx += 1
        elif vb == "未标注":
            unlabeled += 1
        else:
            named[vb] = named.get(vb, 0) + 1
    minor = set()
    for p in papers:
        if p.get("venue_minor"):
            minor.add(venue_base(p.get("venue")))
    always = (stats.get("facets", {}).get("always_list_venues") or ALWAYS_LIST_DEFAULT)
    main = [v for v in named if v in always or (named[v] >= 2 and v not in minor)]
    main.sort(key=lambda v: (-named[v], v))
    others = [v for v in named if v not in main]
    others.sort(key=lambda v: (-named[v], v))
    other_total = sum(named[v] for v in others)

    rows = ""
    for v in main:
        n = named[v]
        pct = n / total * 100
        rows += f"| {v} | {n} | `{bar(pct)}` {pct:.1f}%\n"
    if other_total:
        pct = other_total / total * 100
        rows += f"| 其他 | {other_total} | `{bar(pct)}` {pct:.1f}%\n"
    if arx:
        pct = arx / total * 100
        rows += f"| arXiv（预印本） | {arx} | `{bar(pct)}` {pct:.1f}%\n"
    if unlabeled:
        pct = unlabeled / total * 100
        rows += f"| 未标注 | {unlabeled} | `{bar(pct)}` {pct:.1f}%\n"

    detail = ""
    if others:
        detail = (
            "<details>\n"
            f"<summary>「其他」明细（{len(others)} 个 venue，共 {other_total} 篇，点击展开）</summary>\n\n"
            "| venue | 数量 |\n|-------|------|\n"
        )
        for v in others:
            detail += f"| {v} | {named[v]} |\n"
        detail += "\n</details>\n"
    return rows, detail


def entry_line(p):
    link = p.get("venue_url") or p.get("url") or ""
    title = (p.get("title") or "").replace("]", "\\]").replace("[", "\\[")
    venue = p.get("venue") or "未标注"
    model = MODEL_LABEL.get(p.get("model_type"), p.get("model_type"))
    method = p.get("method_type") or ""
    prefix = ""
    if p.get("survey"):
        prefix = "📚 "
    elif p.get("benchmark") or "Benchmark" in (p.get("tags") or []):
        prefix = "📋 "
    code = f" · 💻[code]({p['code']})" if p.get("code") else ""
    return f"- **{prefix}[{title}]({link})** · {venue} · {model} · {method}{code}"


def gen_benchmark(papers):
    items = [p for p in papers if p.get("benchmark") or "Benchmark" in (p.get("tags") or [])]
    items.sort(key=lambda p: (date_key(p), p.get("title") or ""), reverse=True)
    n = len(items)
    body = (
        f"> 独立收录 `{n}` 篇评测 / Benchmark / 数据集论文（同时保留在下方主列表中，标有 📋）。\n\n"
        "<details open>\n"
        f"<summary>📋 评测与 Benchmark 列表（{n} 篇，点击折叠 / 展开）</summary>\n\n"
        + "\n".join(entry_line(p) for p in items)
        + "\n\n</details>\n"
    )
    return body


def gen_survey(papers):
    items = [p for p in papers if p.get("survey")]
    items.sort(key=lambda p: (date_key(p), p.get("title") or ""), reverse=True)
    n = len(items)
    body = (
        f"> 独立收录 `{n}` 篇综述 / 调查 / 分类法论文（同时保留在下方主列表中，标有 📚）。\n\n"
        "<details open>\n"
        f"<summary>📚 综述 Survey 列表（{n} 篇，点击折叠 / 展开）</summary>\n\n"
        + "\n".join(entry_line(p) for p in items)
        + "\n\n</details>\n"
    )
    return body


MODEL_ORDER = [("LLM", "🤖 LLM"), ("VLM", "👁️ VLM"), ("MLLM", "🌐 MLLM(Omni)")]


def gen_list(papers):
    by_model = {}
    for p in papers:
        by_model.setdefault(p.get("model_type") or "LLM", []).append(p)
    known = {k for k, _ in MODEL_ORDER}
    intro = (
        "> 按**模型类型**分组（LLM / VLM / MLLM），每组内再按年份展开；点击标题可展开 / 收起。"
        "每条格式：**标题** · 会议/年份 · 模型 · 方法 · 💻代码。"
        "标题链接优先顶会官方版本。📋 = 评测/Benchmark 论文，📚 = 综述 Survey 论文。"
        "完整摘要与多维交叉筛选见交互式网站 [`docs/index.html`](docs/index.html)。欢迎 PR 补充。\n"
    )
    order = list(MODEL_ORDER)
    for k in by_model:
        if k not in known:
            order.append((k, k))

    # Each model group is a "block"; blocks are joined by a BLANK LINE so the
    # closing </details> of one group is never adjacent to the next <details>.
    # GitHub/CommonMark merges adjacent HTML-block lines into one block, which
    # silently breaks nested <details> and renders them permanently expanded.
    blocks = [intro.rstrip("\n")]
    for key, label in order:
        ps = by_model.get(key, [])
        if not ps:
            continue
        mb = ["<details>", f"<summary>{label} · {len(ps)} 篇</summary>", ""]
        groups = {}
        for p in ps:
            groups.setdefault(p["year"], []).append(p)
        for y in sorted(groups, reverse=True):
            yps = sorted(groups[y], key=lambda p: (date_key(p), p.get("title") or ""), reverse=True)
            mb.append("<details>")
            mb.append(f"<summary>📅 {y} · {len(yps)} 篇</summary>")
            mb.append("")
            mb.extend(entry_line(p) for p in yps)
            mb.append("")          # blank line before the group's own </details>
            mb.append("</details>")
            mb.append("")          # blank line between consecutive year groups
        mb.append("</details>")
        blocks.append("\n".join(mb))
    return "\n\n".join(blocks) + "\n"


# ----------------------------------------------------------------------------
# assembly
# ----------------------------------------------------------------------------

def replace_block(text, anchor, generated):
    lines = text.split("\n")
    start = next((i for i, l in enumerate(lines) if l.startswith(anchor)), None)
    if start is None:
        print(f"[gen_readme] WARN: anchor not found: {anchor!r}", file=sys.stderr)
        return text
    end = next((i for i in range(start + 1, len(lines)) if lines[i].startswith("## ")), len(lines))
    new = lines[: start + 1] + generated.split("\n") + lines[end:]
    return "\n".join(new)


def update_badges(text, total, with_abs):
    now = datetime.date.today()
    stamp = now.strftime("%Y-%m")
    text = re.sub(r"Papers-\d+", f"Papers-{total}", text)
    text = re.sub(r"Abstract--based-\d+", f"Abstract--based-{with_abs}", text)
    text = re.sub(r"Last%20Update-\d{4}-\d{2}", f"Last%20Update-{stamp}", text)
    return text


def main():
    papers = load_papers()
    stats = load_stats()
    text = open(README, encoding="utf-8").read()

    total = len(papers)
    with_abs = sum(1 for p in papers if p.get("abstract"))

    text = update_badges(text, total, with_abs)
    text = replace_block(text, "## 📊 数据概览", gen_stats(papers, stats))
    text = replace_block(text, "## 📋 评测与 Benchmark", gen_benchmark(papers))
    text = replace_block(text, "## 📚 综述 Survey", gen_survey(papers))
    text = replace_block(text, "## 📚 论文列表", gen_list(papers))

    tmp = README + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        f.write(text)
    os.replace(tmp, README)

    n_bench = sum(1 for p in papers if p.get("benchmark") or "Benchmark" in (p.get("tags") or []))
    n_surv = sum(1 for p in papers if p.get("survey"))
    print(f"[gen_readme] OK -> README.md regenerated from {total} papers "
          f"(bench={n_bench}, survey={n_surv}, code={sum(1 for p in papers if p.get('code'))})")


if __name__ == "__main__":
    main()
