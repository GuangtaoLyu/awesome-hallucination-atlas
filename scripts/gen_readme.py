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

from lib_common import vlabel

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
PAPERS = os.path.join(ROOT, "data", "papers.json")
README_EN = os.path.join(ROOT, "README.md")
README_ZH = os.path.join(ROOT, "README.zh-CN.md")
PAPERS_DIR = os.path.join(ROOT, "papers")
PAPERS_INDEX_EN = os.path.join(ROOT, "PAPERS.md")
PAPERS_INDEX_ZH = os.path.join(ROOT, "PAPERS.zh-CN.md")
# GitHub silently truncates README rendering past 500 KiB. Keep every rendered
# Markdown file comfortably below that, with room for a year of new papers.
MAX_RENDER_BYTES = 480 * 1024

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
        label = "CCF-" + k if k != "未收录" else vlabel("未收录", lang)
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
        "> " + pick("Papers published at a conference / journal are counted by venue (official info prioritized); `arXiv (preprint)` means a preprint not yet officially accepted. Niche journals / small venues, workshops / satellite / co-located events, and venues with only 1 paper are grouped into the “Other” row (details in the collapsible section below). `Unlabeled` marks entries with no resolvable link.",
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
        "> " + pick("CCF ratings follow the **CCF Recommended International Conference / Journal Directory (2026)** for officially published papers; `Not in CCF` covers arXiv preprints, unresolved venues, and venues outside the CCF list.",
                    "依据 **CCF 推荐国际学术会议 / 期刊目录（2026）** 对正式发表的论文标注评级；`未收录` 含 arXiv 预印本、暂未解析出 venue 的条目，以及 CCF 目录之外的会议 / 期刊。", lang) + "\n\n"
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
        rows += f"| {vlabel('其他', lang)} | {other_total} | `{bar(pct)}` {pct:.1f}%\n"
    if arx:
        pct = arx / total * 100
        rows += f"| {vlabel('arXiv（预印本）', lang)} | {arx} | `{bar(pct)}` {pct:.1f}%\n"
    if unlabeled:
        pct = unlabeled / total * 100
        rows += f"| {vlabel('未标注', lang)} | {unlabeled} | `{bar(pct)}` {pct:.1f}%\n"

    detail = ""
    if others:
        detail = (
            "<details>\n"
            f"<summary>{pick('“Other” details', '「其他」明细', lang)} ({len(others)} venues, {other_total} papers — click to expand)</summary>\n\n"
            "| venue | " + pick('Count', '数量', lang) + " |\n|-------|------|\n"
        )
        for v in others:
            detail += f"| {v} | {named[v]} |\n"
        detail += "\n</details>\n"
    return rows, detail


def entry_line(p, lang="en"):
    link = p.get("venue_url") or p.get("url") or ""
    title = (p.get("title") or "").replace("]", "\\]").replace("[", "\\[")
    venue = vlabel(p.get("venue") or "未标注", lang)
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
        + "\n".join(entry_line(p, lang) for p in items)
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
        + "\n".join(entry_line(p, lang) for p in items)
        + "\n\n</details>\n"
    )
    return body


MODEL_ORDER = [("LLM", "🤖 LLM"), ("VLM", "👁️ VLM"), ("MLLM", "🌐 MLLM(Omni)")]


SITE_URL = "https://guangtaolyu.github.io/awesome-hallucination-atlas/"
ENTRY_LEGEND = ("Format per entry: **Title** · venue/year · model · method · 💻code. "
                "Title links prefer the official venue version. 📋 = Benchmark paper, "
                "📚 = Survey paper. PRs welcome.")


def year_counts(papers):
    counts = {}
    for p in papers:
        y = p.get("year")
        counts[y] = counts.get(y, 0) + 1
    return dict(sorted(counts.items(), reverse=True))


def gen_nav(papers, lang):
    """Small, always-visible Paper List section kept inside the README."""
    counts = year_counts(papers)
    idx = "PAPERS.md" if lang == "en" else "PAPERS.zh-CN.md"
    L = ["> " + pick(
        "The complete list is split into **per-year files** so GitHub renders all of it "
        "(READMEs are silently truncated past 500 KiB). Browse by year below, or use the "
        "interactive site for full abstracts and faceted search.",
        "完整论文列表已按**年份分册**存放，避免 GitHub 对超过 500 KiB 的 README 静默截断。"
        "可按年份浏览，也可到交互式网站查看完整摘要与多维筛选。", lang), ""]
    L.append("| " + pick("Year", "年份", lang) + " | " + pick("Papers", "篇数", lang)
             + " | " + pick("File", "分册", lang) + " |")
    L.append("|---|---|---|")
    for y, c in counts.items():
        L.append(f"| {y} | {c} | [{y}.md](papers/{y}.md) |")
    L.append("")
    L.append("- [" + pick("Full index by year", "完整索引（按年份）", lang) + f"]({idx})")
    L.append("- [Live Site · " + pick("abstract search & filters", "摘要检索与筛选", lang) + f"]({SITE_URL})")
    return "\n".join(L) + "\n"


def gen_index(papers, lang):
    """PAPERS.md / PAPERS.zh-CN.md: the by-year table of contents."""
    counts = year_counts(papers)
    other = "PAPERS.zh-CN.md" if lang == "en" else "PAPERS.md"
    L = ["# " + pick("Paper List · by year", "论文列表 · 按年份", lang), ""]
    L.append(pick(f"{len(papers)} papers in total. Each file stays under GitHub's "
                  "500 KiB rendering limit; older years are frozen once published.",
                  f"共 {len(papers)} 篇。每个分册都控制在 GitHub 的 500 KiB 渲染上限之内；"
                  "历史年份一经生成即不再变动。", lang))
    L.append("")
    L.append("| " + pick("Year", "年份", lang) + " | " + pick("Papers", "篇数", lang)
             + " | " + pick("File", "分册", lang) + " |")
    L.append("|---|---|---|")
    for y, c in counts.items():
        L.append(f"| {y} | {c} | [{y}.md](papers/{y}.md) |")
    L.append("")
    L.append("- [Live Site](" + SITE_URL + ") — " + pick("full-text abstract search, faceted filtering and year sorting", "摘要全文搜索、多维筛选与年份排序", lang))
    L.append(f"- [{other}]({other}) — " + pick("中文索引", "English index", lang))
    L.append("- [" + pick("Back to README", "返回 README", lang) + "](" + ("README.md" if lang == "en" else "README.zh-CN.md") + ")")
    L.append("")
    L.append("> " + ENTRY_LEGEND)
    return "\n".join(L) + "\n"


def gen_year_page(yp, year):
    """One papers/<year>.md file, grouped by model type and sorted by date."""
    by_model = {}
    for p in yp:
        by_model.setdefault(p.get("model_type") or "LLM", []).append(p)
    known = {k for k, _ in MODEL_ORDER}
    order = list(MODEL_ORDER)
    for k in by_model:
        if k not in known:
            order.append((k, k))
    L = [f"# {year} · {len(yp)} papers / 篇", ""]
    L.append(f"[← PAPERS.md](../PAPERS.md) · [中文索引](../PAPERS.zh-CN.md) · [Live Site]({SITE_URL})")
    L.append("")
    L.append("> " + ENTRY_LEGEND)
    L.append("")
    for key, label in order:
        ps = sorted(by_model.get(key, []), key=lambda p: (date_key(p), p.get("title") or ""), reverse=True)
        if not ps:
            continue
        L.append("<details open>")
        L.append(f"<summary>{label} · {len(ps)} 篇</summary>")
        L.append("")
        L.extend(entry_line(p, "en") for p in ps)
        L.append("")
        L.append("</details>")
        L.append("")
    return "\n".join(L).rstrip() + "\n"


def write_papers_files(papers):
    """Materialise the split list. Every Markdown file here is generated."""
    os.makedirs(PAPERS_DIR, exist_ok=True)
    by_year = {}
    for p in papers:
        by_year.setdefault(p.get("year"), []).append(p)
    wanted = {f"{y}.md" for y in by_year}
    for old in os.listdir(PAPERS_DIR):
        if old.endswith(".md") and old not in wanted:
            os.remove(os.path.join(PAPERS_DIR, old))
    for y, yp in by_year.items():
        with open(os.path.join(PAPERS_DIR, f"{y}.md"), "w", encoding="utf-8") as f:
            f.write(gen_year_page(yp, y))
    for path, lang in ((PAPERS_INDEX_EN, "en"), (PAPERS_INDEX_ZH, "zh")):
        with open(path, "w", encoding="utf-8") as f:
            f.write(gen_index(papers, lang))
    paths = [PAPERS_INDEX_EN, PAPERS_INDEX_ZH] + [os.path.join(PAPERS_DIR, f"{y}.md") for y in by_year]
    oversized = [os.path.relpath(p, ROOT) for p in paths
                 if os.path.getsize(p) > MAX_RENDER_BYTES]
    if oversized:
        print(f"[gen_readme] WARN: approaching GitHub's 500 KiB render limit: "
              f"{', '.join(oversized)}", file=sys.stderr)
    return len(by_year)


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
    # An explicit `<a id="sec-...">` anchor sits immediately before the next
    # heading. Keep it, or a data-driven rewrite silently deletes the target of
    # the matching Table-of-Contents link.
    tail = end
    while tail > start + 1 and lines[tail - 1].startswith('<a id="'):
        tail -= 1
    new = lines[: start + 1] + generated.split("\n") + lines[tail:]
    return "\n".join(new)


def update_badges(text, total, with_abs):
    now = datetime.date.today()
    stamp = now.strftime("%Y-%m")
    text = re.sub(r"Papers-\d+", f"Papers-{total}", text)
    text = re.sub(r"Abstract--based-\d+", f"Abstract--based-{with_abs}", text)
    text = re.sub(r"static/v1\?label=Last%20Update&message=\d{4}-\d{2}&color=orange", f"static/v1?label=Last%20Update&message={stamp}&color=orange", text)
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
        text = replace_block(text, ANCHOR[lang]["paperlist"], gen_nav(papers, lang))

        tmp = path + ".tmp"
        with open(tmp, "w", encoding="utf-8") as f:
            f.write(text)
        os.replace(tmp, path)

    n_years = write_papers_files(papers)
    n_bench = sum(1 for p in papers if p.get("benchmark") or "Benchmark" in (p.get("tags") or []))
    n_surv = sum(1 for p in papers if p.get("survey"))
    print(f"[gen_readme] OK -> README.md + README.zh-CN.md + PAPERS(.zh-CN).md "
          f"+ {n_years} year files from {total} papers "
          f"(bench={n_bench}, survey={n_surv}, code={sum(1 for p in papers if p.get('code'))})")


if __name__ == "__main__":
    main()
