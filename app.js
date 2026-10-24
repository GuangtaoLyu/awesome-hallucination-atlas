/* Awesome Hallucination Atlas — interactive app (bilingual: zh / en) */
(function () {
  "use strict";

  let TRENDING = new Set(["Agent", "RAG", "Reasoning", "Embodied"]);
  const state = {
    papers: [],
    stats: null,
    abstracts: {},   // id -> abstract, lazy-loaded from abstracts.byid.json
    filters: { model_type: new Set(), method_type: new Set(), year: new Set(), tags: new Set(), ccf: new Set(), venue: new Set() },
    query: "",
    sort: "new",
    view: "card",
    page: 1,
    pageSize: 100,
    lang: (function () { try { return localStorage.getItem("hal-lang") || "en"; } catch (e) { return "en"; } })(),
  };

  /* ---------- i18n ---------- */
  const I18N = {
    zh: {
      tagline: "多模态大模型幻觉研究图谱 · 结构化可交互资源库",
      github: "⭐ GitHub",
      searchPlaceholder: "搜索标题、作者、摘要全文…（支持中英文）",
      sortLabel: "排序", sortNew: "最新优先", sortOld: "最早优先", sortTitle: "标题 A→Z",
      viewCard: "▦ 卡片", viewTable: "▤ 表格", reset: "✕ 清除筛选",
      kpiTotal: "论文总数（已去重）",
      withLink: (n, yr) => `含链接 ${n} 篇 · ${yr}`,
      modelType: "模型类型", methodType: "方法类型", trend: "历年发表趋势",
      year: "年份", ccfRating: "CCF 评级", venueTitle: "会议 / 期刊", modalityTags: "标签 / 领域",
      moreVenues: (n) => `更多（${n} 个小众 / 次级 venue）`,
      ccfLabel: (k) => (k === "未收录" ? "未收录" : "CCF-" + k),
      arxiv: "arXiv（预印本）", others: "其他", unspecified: "未标注",
      resultCount: (n, t) => `${n} / ${t} 篇`,
      empty: "没有匹配的论文，试试放宽筛选条件。",
      dimModel: "模型", dimMethod: "方法", dimYear: "年份", dimCcf: "CCF", dimTag: "标签", dimVenue: "会议",
      tableHeaders: ["#", "标题", "作者", "时间", "模型", "方法", "会议/期刊", "代码"],
      footerDesc: '数据基于 <a href="https://github.com/GuangtaoLyu/awesome-hallucination-atlas" target="_blank" rel="noopener">awesome-hallucination-atlas</a> 改造增强 · 分类由启发式引擎自动标注，欢迎通过 <a href="../CONTRIBUTING.md" target="_blank">CONTRIBUTING</a> 修正。',
      footerTotal: (n, yr) => `共 ${n} 篇论文 · 覆盖 ${yr}`,
      expandAbs: "📖 展开摘要", paperOfficial: "📄 官方版本", arxivLink: "arXiv",
      paperOnly: "📄 Paper", codeLink: "💻 Code", benchmarkTag: "📋 Benchmark", surveyTag: "📚 综述",
      langBtn: "EN", themeTitle: "切换主题",
      pageSizeLabel: "每页", exportCsv: "⬇ 导出 CSV", prev: "‹ 上一页", next: "下一页 ›",
      pageInfo: (cur, pg, total) => `第 ${cur}/${pg} 页 · 共 ${total} 篇`,
    },
    en: {
      tagline: "Awesome Hallucination Atlas · Structured Interactive Library",
      github: "⭐ GitHub",
      searchPlaceholder: "Search title, authors, abstract… (CN/EN supported)",
      sortLabel: "Sort", sortNew: "Newest first", sortOld: "Oldest first", sortTitle: "Title A→Z",
      viewCard: "▦ Cards", viewTable: "▤ Table", reset: "✕ Clear filters",
      kpiTotal: "Total papers (deduplicated)",
      withLink: (n, yr) => `${n} with links · ${yr}`,
      modelType: "Model type", methodType: "Method type", trend: "Publications by year",
      year: "Year", ccfRating: "CCF rank", venueTitle: "Venue / Journal", modalityTags: "Tags (label / domain)",
      moreVenues: (n) => `More (${n} minor / secondary venues)`,
      ccfLabel: (k) => (k === "未收录" ? "Unranked" : "CCF-" + k),
      arxiv: "arXiv (preprint)", others: "Others", unspecified: "Unspecified",
      resultCount: (n, t) => `${n} / ${t} papers`,
      empty: "No matching papers. Try relaxing the filters.",
      dimModel: "Model", dimMethod: "Method", dimYear: "Year", dimCcf: "CCF", dimTag: "Tag", dimVenue: "Venue",
      tableHeaders: ["#", "Title", "Authors", "Date", "Model", "Method", "Venue", "Code"],
      footerDesc: 'Enhanced from <a href="https://github.com/GuangtaoLyu/awesome-hallucination-atlas" target="_blank" rel="noopener">awesome-hallucination-atlas</a> · Categories auto-labeled by a heuristic engine; corrections welcome via <a href="../CONTRIBUTING.md" target="_blank">CONTRIBUTING</a>.',
      footerTotal: (n, yr) => `${n} papers · ${yr}`,
      expandAbs: "📖 Abstract", paperOfficial: "📄 Official", arxivLink: "arXiv",
      paperOnly: "📄 Paper", codeLink: "💻 Code", benchmarkTag: "📋 Benchmark", surveyTag: "📚 Survey",
      langBtn: "中", themeTitle: "Toggle theme",
      pageSizeLabel: "Per page", exportCsv: "⬇ Export CSV", prev: "‹ Prev", next: "Next ›",
      pageInfo: (cur, pg, total) => `Page ${cur}/${pg} · ${total} papers`,
    },
  };

  const MODEL_ORDER = ["VLM", "MLLM", "LLM"];
  const MODEL_LABEL = {
    zh: { VLM: "VLM/LVLM", MLLM: "MLLM (Omni)", LLM: "LLM" },
    en: { VLM: "VLM/LVLM", MLLM: "MLLM (Omni)", LLM: "LLM" },
  };
  const METHOD_ORDER = ["Training-free", "Training-based"];
  const METHOD_LABEL = {
    zh: { "Training-free": "免训练", "Training-based": "需训练" },
    en: { "Training-free": "Training-free", "Training-based": "Training-based" },
  };
  const TAG_ORDER = ["Benchmark", "Survey", "Relation", "Attribute", "CV", "Video", "Audio", "Multilingual", "Medical", "3D", "Agent"];
  const CCF_ORDER = ["A", "B", "C", "未收录"];
  const CCF_COLOR = { A: "#d97706", B: "#2563eb", C: "#16a34a", "未收录": "#9ca3af" };
  const PAGE_SIZES = [50, 100, 200, 500];

  const badgeClass = {
    MLLM: "b-mllm", VLM: "b-vlm", LLM: "b-llm",
    "Training-free": "b-tf", "Training-based": "b-tb",
  };
  const dotColor = {
    MLLM: "var(--c-mllm)", VLM: "var(--c-vlm)", LLM: "var(--c-llm)",
    "Training-free": "var(--c-tf)", "Training-based": "var(--c-tb)",
    A: "#d97706", B: "#2563eb", C: "#16a34a", "未收录": "#9ca3af",
  };

  const $ = (s) => document.querySelector(s);
  const el = (tag, cls, html) => { const e = document.createElement(tag); if (cls) e.className = cls; if (html != null) e.innerHTML = html; return e; };
  const T = (k, ...a) => { const v = I18N[state.lang][k]; return typeof v === "function" ? v(...a) : v; };
  const MDL = (k) => (MODEL_LABEL[state.lang][k] || k);
  const MTH = (k) => (METHOD_LABEL[state.lang][k] || k);
  const yearRange = () => {
    const ys = Object.keys(state.stats.by_year).map(Number);
    return Math.min(...ys) + "–" + Math.max(...ys);
  };

  /* ---------- load ---------- */
  // Fast first paint: pull the lite list (no abstracts), then lazily fetch the
  // abstract map in the background. Falls back to the full papers.json if the
  // lite artifact is absent (e.g. older deploy).
  function loadAbstracts() {
    fetch("abstracts.byid.json")
      .then((r) => (r.ok ? r.json() : {}))
      .then((m) => {
        state.abstracts = m || {};
        // Once abstracts land, an active query / filter may now match on
        // abstract text — re-render so the visible set reflects it.
        const active = state.query || Object.values(state.filters).some((s) => s.size);
        if (active) render();
      })
      .catch(() => { state.abstracts = {}; });
  }
  fetch("papers.lite.json")
    .then((r) => { if (!r.ok) throw new Error("lite missing"); return r.json(); })
    .catch(() => fetch("papers.json").then((r) => r.json()))
    .then((data) => {
      state.papers = data.papers;
      state.stats = data.stats;
      loadAbstracts();
      init();
    })
    .catch((err) => {
      $("#results").innerHTML = '<div class="empty"><div class="big">⚠️</div>无法加载 papers.json，请通过本地服务器打开（如 <code>python -m http.server</code>）。</div>';
      console.error(err);
    });

  /* ---------- theme (persisted) ---------- */
  function applyTheme(now) {
    document.documentElement.setAttribute("data-theme", now);
    const tt = $("#themeToggle");
    if (tt) tt.textContent = now === "dark" ? "🌙" : "☀️";
    try { localStorage.setItem("hal-theme", now); } catch (e) {}
  }
  function restoreTheme() {
    let saved = "dark";
    try { saved = localStorage.getItem("hal-theme") || "dark"; } catch (e) {}
    applyTheme(saved);
  }

  function scrollToResults() {
    const r = $("#results");
    if (r) r.scrollIntoView({ behavior: "smooth", block: "start" });
  }

  function init() {
    applyHashFromLocation();
    restoreTheme();
    applyStaticI18n();
    syncControlsFromState();
    renderStats();
    renderFacets();
    bindControls();
    render();
  }

  /* ---------- static i18n ---------- */
  function applyStaticI18n() {
    document.querySelectorAll("[data-i18n]").forEach((e) => {
      const key = e.getAttribute("data-i18n");
      const v = I18N[state.lang][key];
      if (v == null) return;
      if (e.hasAttribute("data-i18n-html")) e.innerHTML = v;
      else e.textContent = v;
    });
    document.documentElement.setAttribute("lang", state.lang === "zh" ? "zh-CN" : "en");
    document.title = state.lang === "zh"
      ? "Awesome Hallucination Atlas · 交互式论文库"
      : "Awesome Hallucination Atlas · Interactive Library";
    const search = $("#search");
    if (search) search.placeholder = T("searchPlaceholder");
    const so = $("#sort");
    if (so) {
      so.querySelector('[value="new"]').textContent = T("sortNew");
      so.querySelector('[value="old"]').textContent = T("sortOld");
      so.querySelector('[value="title"]').textContent = T("sortTitle");
    }
    document.querySelectorAll(".seg[data-view]").forEach((b) => {
      b.textContent = b.dataset.view === "card" ? T("viewCard") : T("viewTable");
    });
    const lb = $("#langToggle");
    if (lb) { lb.textContent = T("langBtn"); lb.title = T("langBtn") === "EN" ? "切换语言 / Switch to English" : "切换语言 / Switch to 中文"; }
    const tt = $("#themeToggle");
    if (tt) tt.title = T("themeTitle");
    const fl = $("#footLine");
    if (fl) fl.textContent = T("footerTotal", state.stats ? state.stats.total : "", yearRange());
  }

  function setLang(lang) {
    state.lang = lang;
    try { localStorage.setItem("hal-lang", lang); } catch (e) {}
    applyStaticI18n();
    renderStats();
    renderFacets();
    render();
  }

  /* ---------- stats panel ---------- */
  function renderStats() {
    const s = state.stats;
    const wrap = $("#stats");
    wrap.innerHTML = "";

    const kpi = el("div", "stat-card kpi");
    kpi.innerHTML = `<div class="kpi-num">${s.total}</div>
      <div><div class="kpi-label">${T("kpiTotal")}</div>
      <div class="kpi-label">${T("withLink", s.with_link, yearRange())}</div></div>`;
    wrap.appendChild(kpi);

    wrap.appendChild(miniBarCard(T("modelType"), MODEL_ORDER, s.by_model, MDL));
    wrap.appendChild(miniBarCard(T("methodType"), METHOD_ORDER, s.by_method, MTH));
    wrap.appendChild(trendCard(s.by_year));
  }

  function miniBarCard(title, order, dict, labelFn) {
    const card = el("div", "stat-card");
    card.appendChild(el("h3", null, title));
    const bars = el("div", "mini-bars");
    const max = Math.max(...order.map((k) => dict[k] || 0), 1);
    order.forEach((k) => {
      const v = dict[k] || 0;
      const row = el("div", "mini-row");
      const lbl = labelFn ? labelFn(k) : k;
      row.innerHTML = `<span class="lbl">${lbl}</span>
        <span class="mini-track"><span class="mini-fill" style="width:${(v / max) * 100}%;background:${dotColor[k]}"></span></span>
        <span class="val">${v}</span>`;
      bars.appendChild(row);
    });
    card.appendChild(bars);
    return card;
  }

  function trendCard(byYear) {
    const card = el("div", "stat-card trend");
    card.appendChild(el("h3", null, T("trend")));
    const years = Object.keys(byYear).map(Number).sort((a, b) => a - b);
    const vals = years.map((y) => byYear[y]);
    const max = Math.max(...vals, 1);
    const W = 260, H = 74, pad = 6;
    const step = (W - pad * 2) / (years.length - 1 || 1);
    const pts = vals.map((v, i) => [pad + i * step, H - pad - (v / max) * (H - pad * 2 - 12)]);
    const line = pts.map((p, i) => (i ? "L" : "M") + p[0].toFixed(1) + " " + p[1].toFixed(1)).join(" ");
    const area = `M${pts[0][0]} ${H - pad} ` + pts.map((p) => "L" + p[0].toFixed(1) + " " + p[1].toFixed(1)).join(" ") + ` L${pts[pts.length - 1][0]} ${H - pad} Z`;
    let dots = pts.map((p, i) => `<circle cx="${p[0].toFixed(1)}" cy="${p[1].toFixed(1)}" r="3" fill="var(--accent)"/><text x="${p[0].toFixed(1)}" y="${(p[1] - 7).toFixed(1)}" font-size="9" fill="var(--text-dim)" text-anchor="middle">${vals[i]}</text>`).join("");
    let labels = years.map((y, i) => `<text x="${pts[i][0].toFixed(1)}" y="${H - 1}" font-size="8.5" fill="var(--text-mute)" text-anchor="middle">${y}</text>`).join("");
    card.innerHTML += `<svg viewBox="0 0 ${W} ${H}" preserveAspectRatio="none">
      <defs><linearGradient id="tg" x1="0" y1="0" x2="0" y2="1">
        <stop offset="0" stop-color="var(--accent)" stop-opacity="0.35"/>
        <stop offset="1" stop-color="var(--accent)" stop-opacity="0"/></linearGradient></defs>
      <path d="${area}" fill="url(#tg)"/>
      <path d="${line}" fill="none" stroke="var(--accent)" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
      ${dots}${labels}</svg>`;
    return card;
  }

  /* ---------- facets ---------- */
  /* venue 基名：去掉尾部年份，arXiv 显示为语言相关文案 */
  function venueBase(p) {
    const v = (p.venue || "").replace(/\s+\d{4}$/, "");
    if (!v) return T("unspecified");
    if (v === "arXiv") return T("arxiv");
    return v;
  }

  // Single-pass facet counting: one loop over papers builds all dimension
  // counters at once (vs. 6 separate full passes). Semantics identical to the
  // old counts(dim, dim) — a paper contributes to dim X only if it passes every
  // *other* active filter (matchesExcept semantics).
  function computeFacetCounts() {
    const c = { model_type: {}, method_type: {}, year: {}, ccf: {}, venue: {}, tags: {} };
    const minorSet = new Set();
    state.papers.forEach((p) => {
      if (p.venue_minor) minorSet.add(venueBase(p));
      for (const dim of ["model_type", "method_type", "year", "ccf", "venue", "tags"]) {
        if (!matchesExcept(p, dim)) continue;
        let vals;
        if (dim === "tags") vals = p.tags;
        else if (dim === "year") vals = [p.year];
        else if (dim === "ccf") vals = [p.ccf || "未收录"];
        else if (dim === "venue") vals = [venueBase(p)];
        else vals = [p[dim]];
        vals.forEach((v) => { c[dim][v] = (c[dim][v] || 0) + 1; });
      }
    });
    return { counts: c, minorSet };
  }

  function renderFacets() {
    const wrap = $("#facets");
    wrap.innerHTML = "";
    TRENDING = new Set((state.stats && state.stats.facets && state.stats.facets.trending_tags) || ["Agent", "RAG", "Reasoning", "Embodied"]);
    const { counts: FC, minorSet } = computeFacetCounts();
    const years = Object.keys(FC.year).map(Number).sort((a, b) => b - a).map(String);
    wrap.appendChild(facetGroup(T("modelType"), "model_type", MODEL_ORDER, FC.model_type, MDL));
    wrap.appendChild(facetGroup(T("methodType"), "method_type", METHOD_ORDER, FC.method_type, MTH));
    wrap.appendChild(facetGroup(T("year"), "year", years, FC.year));
    wrap.appendChild(facetGroup(T("ccfRating"), "ccf", CCF_ORDER, FC.ccf, (k) => T("ccfLabel", k)));
    // 会议 / 期刊：按数量降序；主流 venue（非 minor 且 ≥3 篇）直接展示，
    // 小众 / 次级 venue（venue_minor 标记）与 <3 篇的一律折叠到「更多」；
    // ALWAYS_LIST 中的知名 venue（TNNLS/TASLP/TAI/PRCV）即使篇数少也直接展示；
    // 单一配置源来自 generate.py 注入的 stats.facets.always_list_venues（data/facets.json）。
    const ALWAYS_LIST = (state.stats && state.stats.facets && state.stats.facets.always_list_venues) || ["TNNLS", "TASLP", "TAI", "PRCV"];
    const vc = FC.venue;
    const SPECIAL = [T("arxiv"), T("others"), T("unspecified")];
    const named = Object.keys(vc).filter((v) => !SPECIAL.includes(v)).sort((a, b) => vc[b] - vc[a] || a.localeCompare(b));
    const main = named.filter((v) => ALWAYS_LIST.includes(v) || (vc[v] >= 3 && !minorSet.has(v)));
    const more = named.filter((v) => !main.includes(v));
    const vg = facetGroup(T("venueTitle"), "venue", main.concat(SPECIAL.filter((v) => vc[v])), vc);
    if (more.length) {
      const det = el("details", "facet-more");
      det.appendChild(el("summary", null, T("moreVenues", more.length)));
      const chips = el("div", "chips");
      more.forEach((k) => {
        const chip = el("div", "chip");
        chip.dataset.dim = "venue"; chip.dataset.val = k;
        chip.innerHTML = `${k}<span class="cnt">${vc[k]}</span>`;
        chip.addEventListener("click", () => toggleFilter("venue", k, chip));
        chips.appendChild(chip);
      });
      det.appendChild(chips);
      vg.appendChild(det);
    }
    wrap.appendChild(vg);
    const tc = FC.tags;
    const tags = TAG_ORDER.filter((t) => tc[t]);
    if (tags.length) wrap.appendChild(facetGroup(T("modalityTags"), "tags", tags, tc));
  }

  function facetGroup(title, dim, order, cnts, labelFn) {
    const g = el("div", "facet-group");
    g.appendChild(el("h4", null, title));
    const chips = el("div", "chips");
    order.forEach((k) => {
      const key = String(k);
      const chip = el("div", "chip");
      chip.dataset.dim = dim;
      chip.dataset.val = key;
      const color = dotColor[key];
      const label = labelFn ? labelFn(k) : key;
      const isHot = (dim === "tags" && TRENDING.has(key));
      chip.innerHTML = `${color ? `<span class="dot" style="background:${color}"></span>` : ""}${isHot ? "🔥 " : ""}${label}<span class="cnt">${cnts[k] || 0}</span>`;
      if (isHot) { chip.style.borderColor = "#8b7cf6"; chip.style.background = "rgba(139,124,246,0.18)"; chip.style.fontWeight = "600"; }
      chip.addEventListener("click", () => toggleFilter(dim, key, chip));
      chips.appendChild(chip);
    });
    g.appendChild(chips);
    return g;
  }

  function toggleFilter(dim, val, chip) {
    const set = state.filters[dim];
    const v = val;
    if (set.has(v)) { set.delete(v); } else { set.add(v); }
    state.page = 1;
    render(); pushHash();
  }

  /* ---------- controls ---------- */
  function bindControls() {
    let searchTimer = null;
    $("#search").addEventListener("input", (e) => {
      const val = e.target.value.trim().toLowerCase();
      clearTimeout(searchTimer);
      searchTimer = setTimeout(() => { state.query = val; state.page = 1; render(); pushHash(); }, 150);
    });
    $("#sort").addEventListener("change", (e) => { state.sort = e.target.value; state.page = 1; render(); pushHash(); });
    $("#pageSize").addEventListener("change", (e) => { state.pageSize = parseInt(e.target.value, 10) || 100; state.page = 1; render(); pushHash(); });
    $("#exportBtn").addEventListener("click", exportCsv);
    $("#resetBtn").addEventListener("click", () => {
      Object.values(state.filters).forEach((s) => s.clear());
      state.query = ""; $("#search").value = ""; state.page = 1; render(); pushHash();
    });
    document.querySelectorAll(".seg").forEach((b) => b.addEventListener("click", () => {
      document.querySelectorAll(".seg").forEach((x) => x.classList.remove("active"));
      b.classList.add("active"); state.view = b.dataset.view; state.page = 1; render(); pushHash();
    }));
    $("#langToggle").addEventListener("click", () => {
      setLang(state.lang === "zh" ? "en" : "zh"); pushHash();
    });
    $("#themeToggle").addEventListener("click", () => {
      const now = document.documentElement.getAttribute("data-theme") === "dark" ? "light" : "dark";
      applyTheme(now);
    });
    document.addEventListener("keydown", (e) => {
      if (e.key === "/" && document.activeElement.tagName !== "INPUT") { e.preventDefault(); $("#search").focus(); }
    });
  }

  /* ---------- filtering ---------- */
  // matchesExcept(p, dim) ignores the filter in `dim` so facet counts can
  // reflect the currently-active filters (standard faceted-search behavior).
  function matchesExcept(p, exceptDim) {
    const f = state.filters;
    if (exceptDim !== "model_type" && f.model_type.size && !f.model_type.has(p.model_type)) return false;
    if (exceptDim !== "method_type" && f.method_type.size && !f.method_type.has(p.method_type)) return false;
    if (exceptDim !== "year" && f.year.size && !f.year.has(String(p.year))) return false;
    if (exceptDim !== "ccf" && f.ccf.size && !f.ccf.has(p.ccf || "未收录")) return false;
    if (exceptDim !== "venue" && f.venue.size && !f.venue.has(venueBase(p))) return false;
    if (exceptDim !== "tags" && f.tags.size && !p.tags.some((t) => f.tags.has(t))) return false;
    if (state.query) {
      const hay = (p.title + " " + p.authors + " " + (state.abstracts[p.id] || p.abstract || "") + " " + p.venue + " " + p.model_type + " " + p.method_type + " " + p.tags.join(" ")).toLowerCase();
      if (!hay.includes(state.query)) return false;
    }
    return true;
  }
  function matches(p) { return matchesExcept(p, null); }

  function dateKey(p) {
    if (p.date) return p.date;
    if (p.month) return p.year + "-" + String(p.month).padStart(2, "0") + "-00";
    return p.year + "-00-00";
  }

  function sortPapers(list) {
    const arr = list.slice();
    if (state.sort === "new") arr.sort((a, b) => dateKey(b).localeCompare(dateKey(a)) || a.title.localeCompare(b.title));
    else if (state.sort === "old") arr.sort((a, b) => dateKey(a).localeCompare(dateKey(b)) || a.title.localeCompare(b.title));
    else arr.sort((a, b) => a.title.localeCompare(b.title));
    return arr;
  }

  /* ---------- render ---------- */
  function render() {
    syncChipStates();
    const filtered = sortPapers(state.papers.filter(matches));
    const total = filtered.length;
    const ps = state.pageSize;
    const pageCount = Math.max(1, Math.ceil(total / ps));
    if (state.page > pageCount) state.page = pageCount;
    if (state.page < 1) state.page = 1;
    const start = (state.page - 1) * ps;
    const pageItems = filtered.slice(start, start + ps);

    $("#resultCount").textContent = T("resultCount", total, state.papers.length);
    renderActiveChips();
    renderPager(total, pageCount);

    const box = $("#results");
    box.className = "results " + (state.view === "card" ? "card-view" : "table-view");
    if (!total) {
      box.innerHTML = '<div class="empty"><div class="big">🔍</div>' + T("empty") + '</div>';
      return;
    }
    box.innerHTML = state.view === "card" ? pageItems.map(cardHTML).join("") : tableHTML(pageItems, start);
  }

  function syncChipStates() {
    document.querySelectorAll(".chip").forEach((chip) => {
      const dim = chip.dataset.dim, val = chip.dataset.val;
      const active = state.filters[dim].has(val);
      chip.classList.toggle("active", active);
      if (active) { chip.style.background = dotColor[val] || "var(--accent)"; }
      else { chip.style.background = ""; }
    });
  }

  function renderActiveChips() {
    const wrap = $("#activeChips");
    wrap.innerHTML = "";
    const dims = { model_type: T("dimModel"), method_type: T("dimMethod"), year: T("dimYear"), ccf: T("dimCcf"), tags: T("dimTag"), venue: T("dimVenue") };
    Object.keys(state.filters).forEach((dim) => {
      state.filters[dim].forEach((v) => {
        const label = dim === "ccf" ? T("ccfLabel", v) : v;
        const c = el("span", "ac", `${dims[dim]}: ${label} ✕`);
        c.addEventListener("click", () => { state.filters[dim].delete(v); render(); pushHash(); });
        wrap.appendChild(c);
      });
    });
  }

  function badges(p) {
    let b = `<span class="badge ${badgeClass[p.model_type]}">${MDL(p.model_type)}</span>`;
    b += `<span class="badge ${badgeClass[p.method_type]}">${MTH(p.method_type)}</span>`;
    if (p.venue) {
      b += p.venue_url
        ? `<a class="badge b-venue" href="${p.venue_url}" target="_blank" rel="noopener">${p.venue}</a>`
        : `<span class="badge b-venue">${p.venue}</span>`;
    }
    p.tags.forEach((t) => {
      if (t === "Benchmark") {
        b += `<span class="badge b-eval">${T("benchmarkTag")}</span>`;
      } else if (t === "Survey") {
        b += `<span class="badge b-survey">${T("surveyTag")}</span>`;
      } else {
        b += `<span class="badge b-tag">${t}</span>`;
      }
    });
    if (p.ccf) {
      const c = CCF_COLOR[p.ccf];
      b += `<span class="badge b-ccf" style="border-color:${c};color:${c}">${T("ccfLabel", p.ccf)}</span>`;
    }
    return b;
  }

  function esc(s) { return (s || "").replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;"); }

  function dateLabel(p) {
    if (p.date) return p.date.slice(0, 7);
    if (p.month) return p.year + "-" + String(p.month).padStart(2, "0");
    return String(p.year);
  }

  function cardHTML(p) {
    const mainLink = p.venue_url || p.url;               // 顶会官方链接优先
    const title = mainLink ? `<a href="${mainLink}" target="_blank" rel="noopener">${esc(p.title)}</a>` : esc(p.title);
    const code = p.code ? ` · <a class="code-link" href="${p.code}" target="_blank" rel="noopener">${T("codeLink")}</a>` : "";
    let paper = "";
    if (p.venue_url) {
      paper = ` · <a href="${p.venue_url}" target="_blank" rel="noopener">📄 ${esc(p.venue || T("paperOfficial"))}</a>`;
      if (p.url && p.url !== p.venue_url) paper += ` · <a href="${p.url}" target="_blank" rel="noopener">${T("arxivLink")}</a>`;
    } else if (p.url) {
      paper = ` · <a href="${p.url}" target="_blank" rel="noopener">${T("paperOnly")}</a>`;
    }
    const absText = state.abstracts[p.id] || p.abstract;
    const absBlock = absText
      ? `<details class="p-abs"><summary>${T("expandAbs")}</summary><p>${esc(absText)}</p></details>`
      : "";
    return `<article class="paper">
      <span class="yr">${dateLabel(p)}</span>
      <h3 class="p-title">${title}</h3>
      <div class="p-meta">👤 ${esc(p.authors)}${paper}${code}</div>
      ${absBlock}
      <div class="p-badges">${badges(p)}</div>
    </article>`;
  }

  function tableHTML(list, offset) {
    const rows = list.map((p, i) => {
      const mainLink = p.venue_url || p.url;             // 顶会官方链接优先
      const title = mainLink ? `<a href="${mainLink}" target="_blank" rel="noopener">${esc(p.title)}</a>` : esc(p.title);
      const code = p.code ? `<a href="${p.code}" target="_blank" rel="noopener">💻</a>` : "—";
      return `<tr>
        <td>${i + (offset || 0) + 1}</td>
        <td class="t-title">${title}</td>
        <td>${esc(p.authors)}</td>
        <td>${dateLabel(p)}</td>
        <td><span class="badge ${badgeClass[p.model_type]}">${MDL(p.model_type)}</span></td>
        <td><span class="badge ${badgeClass[p.method_type]}">${MTH(p.method_type)}</span></td>
        <td>${p.venue_url ? `<a href="${p.venue_url}" target="_blank" rel="noopener">${p.venue}</a>` : (p.venue || "—")}${p.ccf ? ` <span class="ccf-mini" style="color:${CCF_COLOR[p.ccf]}">${T("ccfLabel", p.ccf)}</span>` : ""}</td>
        <td>${code}</td>
      </tr>`;
    }).join("");
    const H = T("tableHeaders");
    return `<table><thead><tr>${H.map((h) => `<th>${h}</th>`).join("")}</tr></thead><tbody>${rows}</tbody></table>`;
  }

  /* ---------- pager ---------- */
  function renderPager(total, pageCount) {
    const pager = $("#pager");
    if (!pager) return;
    pager.innerHTML = "";
    if (pageCount <= 1) return;
    const mk = (label, page, opts) => {
      opts = opts || {};
      const b = el("button", "pg" + (opts.active ? " active" : "") + (opts.disabled ? " disabled" : ""), label);
      if (!opts.disabled && !opts.active) b.addEventListener("click", () => { state.page = page; render(); pushHash(); scrollToResults(); });
      return b;
    };
    pager.appendChild(mk(T("prev"), state.page - 1, { disabled: state.page <= 1 }));
    const win = [];
    const add = (p) => { if (p >= 1 && p <= pageCount && win.indexOf(p) === -1) win.push(p); };
    add(1); add(pageCount);
    for (let p = Math.max(1, state.page - 2); p <= Math.min(pageCount, state.page + 2); p++) add(p);
    win.sort((a, b) => a - b);
    let last = 0;
    win.forEach((p) => {
      if (p - last > 1) pager.appendChild(el("span", "pg-ellipsis", "…"));
      pager.appendChild(mk(String(p), p, { active: p === state.page }));
      last = p;
    });
    pager.appendChild(mk(T("next"), state.page + 1, { disabled: state.page >= pageCount }));
    pager.appendChild(el("span", "pg-info", T("pageInfo", state.page, pageCount, total)));
  }

  /* ---------- CSV export (current filtered view) ---------- */
  function csvCell(v) {
    v = v == null ? "" : String(v);
    if (/[",\n\r]/.test(v)) return '"' + v.replace(/"/g, '""') + '"';
    return v;
  }
  function exportCsv() {
    const filtered = sortPapers(state.papers.filter(matches));
    const header = ["#", "Title", "Authors", "Year", "Venue", "CCF", "Model", "Method", "Tags", "Code", "URL", "Official"];
    const rows = filtered.map((p, i) => [
      i + 1, p.title, p.authors, p.year, p.venue || "", p.ccf || "", p.model_type, p.method_type,
      (p.tags || []).join("; "), p.code || "", p.url || "", p.venue_url || "",
    ]);
    const csv = [header, ...rows].map((r) => r.map(csvCell).join(",")).join("\r\n");
    const blob = new Blob(["﻿" + csv], { type: "text/csv;charset=utf-8" });
    const a = document.createElement("a");
    a.href = URL.createObjectURL(blob);
    a.download = "hallucination-papers-" + new Date().toISOString().slice(0, 10) + ".csv";
    document.body.appendChild(a); a.click(); document.body.removeChild(a);
    if (a.href) URL.revokeObjectURL(a.href);
  }

  /* ---------- URL hash: shareable / restorable filters ---------- */
  function buildHash() {
    const p = [];
    p.push("v=" + state.view);
    p.push("s=" + state.sort);
    p.push("l=" + state.lang);
    p.push("pg=" + state.page);
    p.push("ps=" + state.pageSize);
    if (state.query) p.push("q=" + encodeURIComponent(state.query));
    const f = state.filters;
    if (f.model_type.size) p.push("m=" + encodeURIComponent([...f.model_type].join(",")));
    if (f.method_type.size) p.push("mt=" + encodeURIComponent([...f.method_type].join(",")));
    if (f.year.size) p.push("y=" + [...f.year].join(","));
    if (f.ccf.size) p.push("c=" + encodeURIComponent([...f.ccf].join(",")));
    if (f.tags.size) p.push("tg=" + encodeURIComponent([...f.tags].join(",")));
    if (f.venue.size) p.push("vn=" + encodeURIComponent([...f.venue].join(",")));
    return "#" + p.join("&");
  }
  function pushHash() {
    const h = buildHash();
    if (location.hash !== h) history.replaceState(null, "", h);
  }
  function applyHashFromLocation() {
    const h = location.hash.replace(/^#/, "");
    if (!h) return;
    const params = new URLSearchParams(h);
    const g = (k) => params.get(k);
    if (g("v")) state.view = g("v");
    if (g("s")) state.sort = g("s");
    if (g("l")) state.lang = g("l") === "en" ? "en" : "zh";
    if (g("pg")) state.page = parseInt(g("pg"), 10) || 1;
    if (g("ps")) state.pageSize = parseInt(g("ps"), 10) || 100;
    if (g("q") != null) state.query = g("q");
    const setFrom = (key, dim) => { const v = g(key); if (v) state.filters[dim] = new Set(v.split(",")); };
    setFrom("m", "model_type"); setFrom("mt", "method_type");
    setFrom("y", "year"); setFrom("c", "ccf"); setFrom("tg", "tags"); setFrom("vn", "venue");
  }
  function syncControlsFromState() {
    const s = $("#search"); if (s) s.value = state.query;
    const so = $("#sort"); if (so) so.value = state.sort;
    const ps = $("#pageSize"); if (ps) ps.value = String(state.pageSize);
    document.querySelectorAll(".seg").forEach((b) => b.classList.toggle("active", b.dataset.view === state.view));
  }
})();
