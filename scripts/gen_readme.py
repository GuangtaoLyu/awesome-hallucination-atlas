"""Regenerate the drift-prone parts of README.md / README.zh-CN.md from data/papers.json.

The README ships in two single-language files:
  * README.md       — English (default)
  * README.zh-CN.md  — 中文

Each file is hand-maintained prose PLUS several data-driven blocks that must
stay in lock-step with papers.json (otherwise numbers / the 2000-line paper
list silently rot). This script rewrites exactly those blocks and nothing else,
for BOTH language files:

  * the shields.io badges at the top (Papers / Abstract / Last Update)
  * `## 📊 Data Overview`      -> stats tables + venue breakdown + CCF   (EN)
    `## 📊 数据概览`            -> 同上（中文）
  * `## 📋 Benchmarks & Evaluation` / `## 📋 评测与 Benchmark`  -> Benchmark list
  * `## 📚 Surveys`            / `## 📚 综述 Survey`            -> Survey list
  * `## 📚 Paper List`        / `## 📚 论文列表`               -> year-grouped list

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
README_EN = os.path.join(ROOT, "README.md")
README_ZH = os.path.join(ROOT, "README.zh-CN.md")

MODEL_LABEL = {"VLM": "VLM", "MLLM": "MLLM(Omni)", "LLM": "LLM"}
ALWAYS_LIST_DEFAULT = ["TNNLS", "TASLP", "TAI", "PRCV"]
BAR_W = 20

# Per-language section anchors used by replace_block.
ANCHOR = {
    "en": {
        "overview": "## 📊 Data Overview",
        "benchmark": "## 📋 Benchmarks & Evaluation",
        "survey": "## 📚 Surveys",
        "paperlist": "## 📚 Paper List",
    },
    "zh": {
        "overview": "## 📊 数据概览",
        "benchmark": "## 📋 评测与 Benchmark",
        "survey": "## 📚 综述 Survey",
        "paperlist": "## 📚 论文列表",
    },
}


def pick(en_s, zh_s, lang):
    return en_s if lang == "en" else zh_s


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
# block generators (language-parameterized)
# ----------------------------------------------------------------------------

def gen_stats(papers, stats, lang):
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
        "VLM": pick("Vision-Language Model (LVLM; also covers works that call themselves MLLM but handle only image/video + text)",
                    "视觉语言模型（LVLM，含自称 MLLM 但仅处理图像/视频+文本的工作）", lang),
        "MLLM": pick("Omni / full-modal model (audio / speech / any-to-any)",
                     "全模态模型（Omni：音频 / 语音 / any-to-any）", lang),
        "LLM": pick("Pure text-based LLM", "纯语言大模型", lang),
    }
    model_rows = ""
    for k in ["VLM", "MLLM", "LLM"]:
        model_rows += f"| **{MODEL_LABEL[k]}** | {model_desc[k]} | {by_model.get(k, 0)} |\n"

    # method distribution
    by_method = {}
    for p in papers:
        by_method[p["method_type"]] = by_method.get(p["method_type"], 0) + 1
    method_rows = (
        f"| **Training-free** | {pick('Training-free (decoding intervention / attention calibration / representation guidance, etc.)', '免训练（解码干预 / 注意力校准 / 表征引导等）', lang)} | {by_method.get('Training-free', 0)} |\n"
        f"| **Training-based** | {pick('Training-based (preference optimization / fine-tuning / RL, etc.)', '基于训练（偏好优化 / 微调 / 强化学习等）', lang)} | {by_method.get('Training-based', 0)} |\n"
    )

    # venue distribution + "其他" detail
    venue_table, other_detail = gen_venue(papers, total, stats, lang)

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
        f"- **{pick('Total papers', '论文总数', lang)}**：`{total}` {pick('(deduplicated)', '（已去重）', lang)}\n"
        f"- **{pick('With paper link', '含论文链接', lang)}**：`{with_link}` · "
        f"**{pick('With abstract', '含全文摘要', lang)}**：`{with_abs}` · "
        f"**{pick('With code', '含代码链接', lang)}**：`{with_code}` · "
        f"**{pick('Published at venue', '顶会正式发表', lang)}**：`{top_pub}`\n"
        "- " + pick("For papers published at a venue: time and link prioritize the official conference/journal info (DBLP), otherwise arXiv info is used.",
                    "顶会正式发表的论文：**时间与链接优先采用会议官方信息**（DBLP 记录），其余采用 arXiv 信息", lang) + "\n"
        f"- **{pick('Year range', '覆盖年份', lang)}**：{ymin} – {ymax}\n"
    )

    venue_block = (
        "<details>\n"
        f"<summary>📊 {pick('Venue Distribution', '按会议 / 期刊分布', lang)}</summary>\n\n"
        f"### {pick('Venue Distribution', '按会议 / 期刊分布', lang)}\n\n"
        "> " + pick("Papers published at a conference / journal are counted by venue (official info prioritized); `arXiv（预印本）` means a preprint not yet officially accepted. Niche journals / small venues, workshops / satellite / co-located events, and venues with only 1 paper are grouped into the “Other” row (details in the collapsible section below). `未标注` marks entries with no resolvable link.",
                    "已正式发表在会议 / 期刊的论文按 venue 统计（顶会官方信息优先）；`arXiv（预印本）` 为尚未正式录用的预印本。小众期刊 / 小会、研讨会 / 卫星会 / 边会等次级 venue 以及各仅 1 篇的 venue 统一归入「其他」行，明细见表下折叠区；`其他` 中仍含少量 DOI 无法解析出处的条目，`未标注` 为无任何链接、暂无法判定的条目。", lang) + "\n\n"
        f"| {pick('Venue / Journal', '会议 / 期刊', lang)} | {pick('Count', '数量', lang)} | {pick('Share', '占比', lang)} |\n"
        "|-------------|------|------|\n"
        f"{venue_table}"
        "\n"
        f"{other_detail}"
        "\n</details>"
    )

    ccf_block = (
        f"### {pick('CCF Rating', '按 CCF 评级分布', lang)}\n\n"
        "> " + pick("CCF ratings follow the **CCF Recommended International Conference / Journal Directory (2022)** for officially published papers; `未收录` covers arXiv preprints, unresolved venues, and venues outside the CCF list.",
                    "依据 **CCF 推荐国际学术会议 / 期刊目录（2022）** 对正式发表的论文标注评级；`未收录` 含 arXiv 预印本、暂未解析出 venue 的条目，以及 CCF 目录之外的会议 / 期刊。", lang) + "\n\n"
        f"| {pick('CCF Rating', 'CCF 评级', lang)} | {pick('Count', '数量', lang)} | {pick('Share', '占比', lang)} |\n"
        "|----------|------|------|\n"
        f"{ccf_rows}"
        "> " + pick(f"📋 `{n_bench}` **Benchmark** papers and 📚 `{n_surv}` **Survey** papers are listed separately (see sections below) and do not affect the method taxonomy.",
                    f"📋 另有 `{n_bench}` 篇 **评测 / Benchmark** 论文、📚 `{n_surv}` 篇 **综述 Survey** 论文，作为独立标记单独列出（见下方对应小节），不占用方法分类。", lang) + "\n\n"
        "---\n"
    )

    blocks = [
        intro.rstrip("\n"),
        f"### {pick('Year Distribution', '按年份分布', lang)}\n\n| {pick('Year', '年份', lang)} | {pick('Count', '数量', lang)} | {pick('Share', '占比', lang)} |\n|------|------|------|\n" + year_rows,
        f"### {pick('Model Type', '按模型类型分布', lang)}\n\n| {pick('Model Type', '模型类型', lang)} | {pick('Description', '说明', lang)} | {pick('Count', '数量', lang)} |\n|----------|------|------|\n" + model_rows,
        f"### {pick('Method Type', '按方法类型分布', lang)}\n\n| {pick('Method Type', '方法类型', lang)} | {pick('Description', '说明', lang)} | {pick('Count', '数量', lang)} |\n|----------|------|------|\n" + method_rows,
        venue_block,
        ccf_block.rstrip("\n"),
    ]
    return "\n\n".join(blocks) + "\n"


def gen_venue(papers, total, stats, lang):
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
            f"<summary>{pick('“Other” details', '「其他」明细', lang)} ({len(others)} venues, {other_total} papers — click to expand)</summary>\n\n"
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


def gen_benchmark(papers, lang):
    items = [p for p in papers if p.get("benchmark") or "Benchmark" in (p.get("tags") or [])]
    items.sort(key=lambda p: (date_key(p), p.get("title") or ""), reverse=True)
    n = len(items)
    body = (
        "> " + pick(f"{n} evaluation / benchmark / dataset papers are listed separately (also kept in the main list below, marked 📋).",
                    f"独立收录 `{n}` 篇评测 / Benchmark / 数据集论文（同时保留在下方主列表中，标有 📋）。", lang) + "\n\n"
        "<details open>\n"
        f"<summary>📋 {pick('Benchmark List', '评测与 Benchmark 列表', lang)} ({n} papers — click to collapse / expand)</summary>\n\n"
        + "\n".join(entry_line(p) for p in items)
        + "\n\n</details>\n"
    )
    return body


def gen_survey(papers, lang):
    items = [p for p in papers if p.get("survey")]
    items.sort(key=lambda p: (date_key(p), p.get("title") or ""), reverse=True)
    n = len(items)
    body = (
        "> " + pick(f"{n} survey / review / taxonomy papers are listed separately (also kept in the main list below, marked 📚).",
                    f"独立收录 `{n}` 篇综述 / 调查 / 分类法论文（同时保留在下方主列表中，标有 📚）。", lang) + "\n\n"
        "<details open>\n"
        f"<summary>📚 {pick('Survey List', '综述 Survey 列表', lang)} ({n} papers — click to collapse / expand)</summary>\n\n"
        + "\n".join(entry_line(p) for p in items)
        + "\n\n</details>\n"
    )
    return body


MODEL_ORDER = [("LLM", "🤖 LLM"), ("VLM", "👁️ VLM"), ("MLLM", "🌐 MLLM(Omni)")]


def gen_list(papers, lang):
    by_model = {}
    for p in papers:
        by_model.setdefault(p.get("model_type") or "LLM", []).append(p)
    known = {k for k, _ in MODEL_ORDER}
    intro = (
        "> " + pick("Grouped by **model type** (LLM / VLM / MLLM), then expanded by year inside each group; click a header to expand / collapse. "
                    "Format per entry: **Title** · venue/year · model · method · 💻code. "
                    "Title links prefer the official venue version. 📋 = Benchmark paper, 📚 = Survey paper. "
                    "Full abstracts and multi-dimensional filtering are available in the interactive website [`docs/index.html`](docs/index.html). PRs welcome.",
                    "按**模型类型**分组（LLM / VLM / MLLM），每组内再按年份展开；点击标题可展开 / 收起。"
                    "每条格式：**标题** · 会议/年份 · 模型 · 方法 · 💻代码。"
                    "标题链接优先顶会官方版本。📋 = 评测/Benchmark 论文，📚 = 综述 Survey 论文。"
                    "完整摘要与多维交叉筛选见交互式网站 [`docs/index.html`](docs/index.html)。欢迎 PR 补充。", lang) + "\n"
    )
    order = list(MODEL_ORDER)
    for k in by_model:
        if k not in known:
            order.append((k, k))

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
            mb.append(f"<summary>📅 {y} · {len(yps)} {pick('papers', '篇', lang)}</summary>")
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
    total = len(papers)
    with_abs = sum(1 for p in papers if p.get("abstract"))

    targets = [("en", README_EN), ("zh", README_ZH)]
    for lang, path in targets:
        if not os.path.exists(path):
            print(f"[gen_readme] WARN: {path} missing, skip", file=sys.stderr)
            continue
        text = open(path, encoding="utf-8").read()
        text = update_badges(text, total, with_abs)
        text = replace_block(text, ANCHOR[lang]["overview"], gen_stats(papers, stats, lang))
        text = replace_block(text, ANCHOR[lang]["benchmark"], gen_benchmark(papers, lang))
        text = replace_block(text, ANCHOR[lang]["survey"], gen_survey(papers, lang))
        text = replace_block(text, ANCHOR[lang]["paperlist"], gen_list(papers, lang))

        tmp = path + ".tmp"
        with open(tmp, "w", encoding="utf-8") as f:
            f.write(text)
        os.replace(tmp, path)

    n_bench = sum(1 for p in papers if p.get("benchmark") or "Benchmark" in (p.get("tags") or []))
    n_surv = sum(1 for p in papers if p.get("survey"))
    print(f"[gen_readme] OK -> README.md + README.zh-CN.md regenerated from {total} papers "
          f"(bench={n_bench}, survey={n_surv}, code={sum(1 for p in papers if p.get('code'))})")


if __name__ == "__main__":
    main()
