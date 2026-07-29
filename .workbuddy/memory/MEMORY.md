# 项目长期记忆：hallucination 资源库（awesome-hallucination-atlas）

## 架构约定（改代码前先读）
- **单一来源函数**：`norm_title`/`arxiv_id` → `scripts/lib_common.py`；`http_get`/`load_json`/`TransientError` → `scripts/code_common.py`；`atomic_dump`（原子写防截断）→ `lib_common`；`parse_venue`/`VENUE_PATTERNS` → `lib_common`；`ALWAYS_LIST_VENUES` → `data/facets.json`（`generate.py` 注入 `stats.facets.always_list_venues`，`app.js` 读该字段）。禁止在别处重定义/各自维护（历史上多次"keep in sync"漂移 bug）。
- **数据层**：`data/seed.json`（[title,authors,url,year]）是唯一真源；`scripts/raw_data.py` 仅兼容 shim；`merge_candidates.py` 写回 seed.json。`data/ccf.json`/`facets.json`/`manual_entries.yaml` 也是真源需提交。
- **字段契约**：代码链接→`paper["code"]`（generate.py:610 读 code_links.json，key=norm_title）；摘要→`paper["abstract"]`（abstracts.json + abstracts_extra.json，key 均为 norm_title）。统计代码覆盖率必须查 `paper["code"]` 而非 `paper["links"]`。
- **前端拆包**：`generate.py` 输出 `docs/papers.lite.json`（首屏，无摘要）+ `docs/abstracts.byid.json`（懒加载）；`app.js` 优先 lite。
- **TLS/门槛**：所有 arXiv 请求用 https + `ssl.create_default_context()`；候选标题门槛用词干 `hallucinat`（非精确 `hallucination`），四通道与 `relevant()` 一致。
- **git 版本控制**：仓库已 `git init`（基线 4e4d3d6）。`.gitignore` 忽略可再生缓存（`__pycache__`/`*.bak`/`abstracts*.json`/`crossref_cache.json`/`incremental.json`/`venue_links.json`/`code_links.json`/`found_links.json`/`stats*.json`/`papers.json.pre_incremental` 等）；真源与产物（`data/papers.json`/`docs/*`/`README.md`/`README.zh-CN.md`/`scripts/*`）需提交。`update_pipeline.py` 在 audit 通过后自动 `git commit`（提交信息含日期/文件数/论文数/步骤；`--no-commit` 跳过）。
- **审计不变量**（每次改动后须验证）：`data/papers.json` 与 `docs/papers.json` md5 一致；CCF 与 ccf.json 一致；`venue_links` 孤儿=0；`audit.py` 恒以 `--strict` 运行（任一硬不变量破裂则非零退出，流水线中止）。已知稳定 md5 基线 `ef88fe2ee7cc44e61e318db45200ef75`。

## 流水线编排
- **`update_pipeline.py` 是唯一编排入口**（automations 只调它）：fetch_new_arxiv → generate#1 → update_arxiv_venues → [富集] → generate#2 → audit。开关：`--enrich`（fetch_abstracts+abstracts+with-abstracts+code+links）、`--full`（collect+collect-2026+enrich）、`--check`（离线 audit）、`--serve`（本地预览）、`--no-commit`。富集顺序：fetch_abstracts 在 generate#1 前；enrich_abstracts/fetch_abstracts_web/fetch_code/enrich_links 在 generate#1 后、generate#2 前。
- **`collect_candidates.py` 的 resume 守卫**：candidates_new.json 已有该类 source 候选即跳过该通道（全跳或全不跳），merge 清空前不重抓。
- **GitHub 限制**：`fetch_code.py` 无 token 时匿名 60/hr、每篇 sleep 1.2s，全量不现实；`api.github.com` 在当前代理可能不通。

## README 生成（双文件单语，防回退）
- **`generate.py:write_readme(papers,stats,lang)` 与 `gen_readme.py` 两处都按 `lang`（en/zh）参数化**，分别写 `README.md`（英文默认）+ `README.zh-CN.md`（中文），顶部互相放语言切换链接。标题 `Awesome Hallucination Atlas`（Title Case）。改文案必须同时改两生成器，否则流水线重跑回退成旧版。
- `gen_readme.py` 按 `##` 锚点重写 4 个数据区块（数据概览/Benchmark/Survey/论文列表）；人工段落（分类体系/引用/贡献/许可）由 generate.py 写、不被覆盖。论文列表按 `model_type`（🤖LLM/👁️VLM/🌐MLLM(Omni)）分组、组内按年份嵌套 `<details>`，按 `(year desc, date desc, title)` 稳定排序。
- **无「网站与部署」小节**：README 顶部仅留一条网站链接（指向 GitHub Pages URL）。

## 仓库品牌/命名（GitHub 对外）
- **正式仓库名 = `awesome-hallucination-atlas`**（2026-07-28 定名）。URL 沿用 owner `GuangtaoLyu`：`https://github.com/GuangtaoLyu/awesome-hallucination-atlas`；网站 `https://guangtaolyu.github.io/awesome-hallucination-atlas/`。若 owner 不同需全局替换。
- **网站 `app.js` 默认英文**（`localStorage hal-lang` fallback `"en"`），EN/中文 toggle。
- **GitHub 元信息已就绪**：`.github/ISSUE_TEMPLATE/*`、`PULL_REQUEST_TEMPLATE.md`、`.github/workflows/{ci,deploy-pages,scheduled-update}.yml`、`CITATION.cff`、`docs/.nojekyll`、`social-preview.png`（1280×640 社交预览图，cover 裁切 + 左侧暗化 + 靛蓝玻璃 pill）。部署需 Settings→Pages→Source 选 GitHub Actions。

## 真实 bug 速查（均已修）
- `update_pipeline.py` 传 `"force"`→`"--force"`；`collect_candidates.py` journal/cvf 通道门槛统一为 `hallucinat` 并加 `.text or ""` 守卫；`audit.py` 字段名 `evaluation`→`benchmark`；`generate.py` 缺 `import sys`、venue_from_doi 截断 `s[:57]+"…"` 已删除；`update_arxiv_venues.crossref_lookup` 未处理 dict 返回已加类型处理。
