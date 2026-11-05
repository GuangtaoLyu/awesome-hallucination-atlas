# 贡献指南 · Contributing Guide (中文)

感谢你为 **Awesome Hallucination Atlas** 做出贡献！本库通过一份**单一数据源**（`data/seed.json`）自动生成 README 表格与交互式网站，因此你**只需添加一条数据**，其余（分类、统计、网页）都会自动更新。

---

## 🧩 数据流架构

```
data/seed.json + data/manual_entries.yaml   ← 你唯一需要编辑的文件
        │
        ▼  python scripts/fetch_abstracts.py   （抓取 arXiv 摘要+发表日期，增量缓存）
        ├── data/abstracts.json    摘要缓存（只抓新增条目）
        ▼  python scripts/enrich_links.py      （可选：补全链接/代码/顶会信息，增量缓存）
        ├── data/found_links.json  arXiv 标题搜索找回的论文链接
        ├── data/code_links.json   GitHub 代码链接（摘要提取 + GitHub 搜索）
        ├── data/venue_links.json  DBLP 顶会正式发表记录（venue/年份/官方链接）
        ▼  python scripts/generate.py          （基于摘要全文自动分类）
        ├── data/papers.json     结构化数据（含分类字段与完整摘要）
        ├── docs/papers.json     供网站读取（支持摘要全文搜索）
        └── scripts/gen_readme.py  →  README.md（统计 + 导航）、PAPERS.md（索引）、
                                      papers/<年份>.md（完整列表，按年份拆分）
```

> 📌 **顶会优先原则**：若论文在 DBLP 有正式会议/期刊记录（非 CoRR），则条目的**来源、时间、主链接优先采用会议官方信息**（如 `CVPR 2024` + DOI 链接），arXiv 链接作为补充保留。

> ⚠️ **不要提交生成产物。** `README.md`、`README.zh-CN.md`、`PAPERS.md`、`PAPERS.zh-CN.md`、`papers/<年份>.md`、`data/papers.json`、`docs/papers*.json` 以及各类摘要/链接缓存，都会由每日流水线自动重建。PR 里**只应包含数据源改动**（`data/seed.json` 或 `data/manual_entries.yaml`）。论文列表已按年份拆分，因为 GitHub 会静默截断超过 500 KiB 的 README；用旧版脚本重新生成会把这个拆分覆盖回去。

---

## ➕ 如何添加一篇论文

### 1. 编辑 `data/seed.json`

在 JSON 数组中加入一条记录（若只补录一篇找回的 / 仅有会议版本的论文，也可在 `data/manual_entries.yaml` 里加一个 `- title:` 块）：

```json
["论文完整标题", "第一作者 et al.", "论文链接URL", 2026]
```

**字段说明：**

| 位置 | 字段 | 必填 | 说明 |
|------|------|------|------|
| 1 | `title` | ✅ | 论文完整英文标题，保留原始大小写与冒号 |
| 2 | `authors` | ✅ | 通常写 `Firstauthor et al.`；无法确定时写 `Anonymous et al.` |
| 3 | `url` | 建议 | arXiv abs / ACL / IEEE / Springer 链接；暂无则留空字符串 `""` |
| 4 | `year` | ✅ | 发表年份（若为 arXiv，脚本会依据编号自动校正，可先按你了解的年份填写） |

**示例：**

```json
["HALC: Object Hallucination Reduction via Adaptive Focal-Contrast Decoding", "Chen et al.", "https://arxiv.org/abs/2403.00425", 2024]
```

### 2. 重新生成

```bash
python scripts/generate.py          # 重建 papers.json + docs + README
python scripts/gen_readme.py        # 重建 README + PAPERS 索引 + papers/<年份>.md
python scripts/audit.py --strict    # 校验硬不变量（CI 也会跑）
```

流程：去重 → 基于**摘要全文**自动分类（模型/方法/场景）→ 更新统计 → 重写 README 与网站数据。非 arXiv 论文（IEEE/ACL/Springer）暂无法自动抓摘要，会回退到标题分类，欢迎在 PR 中人工修正。

### 3. 提交 PR

```bash
git add data/seed.json             # 或 data/manual_entries.yaml
git commit -m "docs: add <paper short name> (<year>)"
git push

其余文件由每日 GitHub Action 自动重建。如果本地跑过上面的脚本，提交前请把生成产物还原（`git checkout -- README.md README.zh-CN.md PAPERS.md PAPERS.zh-CN.md papers/ data/papers.json docs/`）。
```

---

## 🏷️ 自动分类规则（供参考）

脚本对**标题 + arXiv 摘要全文**做规则分析标注 4 个维度。若自动结果不准确，欢迎在 PR 中指出，维护者会在 `generate.py` 中补充规则。

| 维度 | 取值 | 判定信号（基于摘要，部分） |
|------|------|---------------------------|
| **模型类型** | `VLM` / `MLLM (Omni)` / `LLM` | omni / audio / speech / any-to-any→MLLM (Omni，真全模态)；vision-language / LVLM / video-LLM / 自称 MLLM 但仅图文→VLM；纯文本→LLM |
| **方法类型** | `Training-free` / `Training-based` / `Evaluation` | 明确 "training-free / inference-time / without training"→Training-free；"we fine-tune / DPO / RL / preference optimization"→Training-based；"introduce a benchmark / survey / 纯分析无缓解方法"→Evaluation |
| **幻觉场景** | `Object` / `Attribute` / `Relation` / `General` | 摘要中 object hallucination / non-existent object→Object；attribute/counting/verb→Attribute；relation(ship)→Relation |
| **附加标签** | `Video` `Audio` `Multilingual` `Medical` `3D` `Agent` | 依摘要中的模态/领域信号 |

---

## 🔗 补充代码链接

原始条目大多缺少代码链接。若你知道某篇论文的官方仓库：

1. 直接编辑 `data/code_links.json`，键为**规范化标题**（小写、去掉所有非字母数字字符），值为 GitHub 仓库链接；
2. 或在 PR 中提供【标题 + 代码链接】清单，由维护者录入；
3. 重新运行 `python scripts/generate.py`。

同理，顶会录取信息可编辑 `data/venue_links.json`（格式 `{"venue": "CVPR", "year": 2025, "ee": "官方链接"}`），也可运行 `python scripts/enrich_links.py venue` 自动从 DBLP 增量抓取。

> 我们鼓励优先补充**官方实现**链接，社区复现请注明。

---

## ✅ 提交前检查清单

- [ ] 标题无重复（脚本会按规范化标题去重，但请人工确认不是换名重投）
- [ ] 链接可访问，优先 arXiv abstract 页
- [ ] 已运行 `python scripts/generate.py` 且无报错
- [ ] `README.md` 与 `docs/papers.json` 已一并更新提交
- [ ] commit message 简洁清晰

---

## 💡 其他贡献方式

- 🐛 修正错误的分类 / 作者 / 链接
- 🌍 完善多语言（中英）摘要
- 🎨 改进 `docs/` 交互网站的样式与功能
- 📊 提出新的分类维度或统计视角

有任何疑问，欢迎提 Issue 讨论。Happy contributing! 🎉
