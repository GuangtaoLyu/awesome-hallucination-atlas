> 🌐 **English** · [中文](README.zh-CN.md)

# Awesome Hallucination Atlas [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> **Awesome Hallucination Atlas** — A structured, interactive atlas of hallucination research across multimodal LLMs (MLLM / VLM / LLM).
>
> Covers **detection, evaluation, and mitigation** of hallucinations, with multi-dimensional faceted filtering by model type, method type, and year, plus tags for modality and scenario.
>
> Taxonomy is auto-labeled from the **full arXiv abstract text** (357/1070 papers), not just title keywords.

<p align='center'>
  <img src='https://img.shields.io/badge/Papers-1070-blue' />
  <img src='https://img.shields.io/badge/Abstract--based-357-9cf' />
  <img src='https://img.shields.io/badge/PRs-Welcome-brightgreen' />
  <img src='https://img.shields.io/static/v1?label=Last%20Update&message=2026-07&color=orange' />
</p>

<p align='center'>
  <a href='https://guangtaolyu.github.io/awesome-hallucination-atlas/'>
    <img alt='Live Website' src='https://img.shields.io/static/v1?label=Live%20Website&message=Visit%20Now&color=8b7cf6&style=for-the-badge' />
  </a>
</p>

> **🌐 Explore the Interactive Website** — [awesome-hallucination-atlas on GitHub Pages](https://guangtaolyu.github.io/awesome-hallucination-atlas/). Faceted filtering, full-text abstract search, and year sorting.
> Prefer offline? Just open [`docs/index.html`](docs/index.html) in any browser — no server needed.

## 📑 Table of Contents

- [Data Overview](#sec-overview)
- [Taxonomy](#sec-taxonomy)
- [Trending Directions](#sec-trending)
- [Benchmarks & Evaluation](#sec-benchmark)
- [Surveys](#sec-survey)
- [Paper List](#sec-paperlist)
- [Citation](#sec-cite)
- [Contributing](#sec-contrib)
- [License](#sec-license)
- [Star History](#sec-stars)

---

<a id="sec-overview"></a>
## 📊 Data Overview

- **Total papers**：`1070` (deduplicated)
- **With paper link**：`1010` · **With abstract**：`357` · **With code**：`0` · **Published at venue**：`597`
- For papers published at a venue: **time and link prioritize the official conference/journal info** (DBLP), otherwise arXiv info is used.
- **Year range**：2018 – 2027

### Year Distribution

| Year | Count | Share |
|------|------|------|
| 2027 | 5 | `░░░░░░░░░░░░░░░░░░░░░░` 0.5% |
| 2026 | 409 | `████████░░░░░░░░░░░░░░` 38.2% |
| 2025 | 397 | `████████░░░░░░░░░░░░░░` 37.1% |
| 2024 | 220 | `█████░░░░░░░░░░░░░░░░░` 20.6% |
| 2023 | 25 | `█░░░░░░░░░░░░░░░░░░░░░` 2.3% |
| 2022 | 5 | `░░░░░░░░░░░░░░░░░░░░░░` 0.5% |
| 2021 | 3 | `░░░░░░░░░░░░░░░░░░░░░░` 0.3% |
| 2020 | 1 | `░░░░░░░░░░░░░░░░░░░░░░` 0.1% |
| 2019 | 4 | `░░░░░░░░░░░░░░░░░░░░░░` 0.4% |
| 2018 | 1 | `░░░░░░░░░░░░░░░░░░░░░░` 0.1% |

### Model Type

| Model Type | Description | Count |
|----------|------|------|
| **VLM** | Vision-Language Model (LVLM; also covers works that call themselves MLLM but handle only image/video + text) | 540 |
| **MLLM (Omni)** | Omni / full-modal model (audio / speech / any-to-any) | 29 |
| **LLM** | Pure text-based LLM | 501 |

### Method Type

| Method Type | Description | Count |
|----------|------|------|
| **Training-free** | Training-free (decoding intervention / attention calibration / representation guidance, etc.) | 990 |
| **Training-based** | Training-based (preference optimization / fine-tuning / RL, etc.) | 80 |

### Venue Distribution

> Papers published at a conference / journal are counted by venue (official info prioritized); `arXiv (preprint)` means a preprint not yet officially accepted. Niche journals / small venues, workshops / satellite / co-located events, and venues with only 1 paper are grouped into the “Other” row (details in the collapsible section below). `Unlabeled` marks entries with no resolvable link.

| Venue / Journal | Count | Share |
|-------------|------|------|
| ACL | 76 | `██░░░░░░░░░░░░░░░░░░░░` 7.1% |
| Other | 482 | `██████████░░░░░░░░░░░░` 45.0% |
| arXiv (preprint) | 366 | `████████░░░░░░░░░░░░░░` 34.2% |
| Unlabeled | 146 | `███░░░░░░░░░░░░░░░░░░░` 13.6% |

### CCF Rating

> CCF ratings follow the **CCF Recommended International Conference / Journal Directory (2022)** for officially published papers; `Not in CCF` covers arXiv preprints, unresolved venues, and venues outside the CCF list.

| CCF Rating | Count | Share |
|----------|------|------|
| CCF-A | 76 | `██░░░░░░░░░░░░░░░░░░░░` 7.1% |
| CCF-B | 0 | `░░░░░░░░░░░░░░░░░░░░░░` 0.0% |
| CCF-C | 0 | `░░░░░░░░░░░░░░░░░░░░░░` 0.0% |
| Not in CCF | 994 | `████████████████████░░` 92.9% |

> 📋 `61` **Benchmark** papers and 📚 `15` **Survey** papers are listed separately (see sections below) and do not affect the method taxonomy.

---

<a id="sec-taxonomy"></a>
## 🧭 Taxonomy

Each paper is labeled along **3 dimensions** (model type / method type / year, auto-analyzed from the full abstract), with tags for modality and scenario.

| Dimension | Values |
|------|------|
| **Model type** | `VLM/LVLM` (vision-language) · `MLLM (Omni)` (omni with audio/speech) · `LLM` (text-only) |
| **Method type** | `Training-free` · `Training-based` (binary) |
| **Year** | 2018 – 2027 |

> Hallucination scenario is no longer a separate dimension: for VLMs, object hallucination *is* the general case. Only genuinely special `Relation` / `Attribute` hallucinations are kept as optional tags.
> Extra tags: `Benchmark` (evaluation; does not affect method taxonomy) · `Survey` · `Relation` · `Attribute` · `CV` (vision) · `Video` · `Audio` · `Multilingual` · `Medical` · `3D` · `Agent` · `RAG` · `Reasoning` · `Embodied`.
> Full abstracts are stored in `data/papers.json` and can be expanded / full-text searched in the interactive website.

---

<a id="sec-trending"></a>
## 🔥 Trending Directions

Hallucination research is moving fast. These directions are especially hot in 2025–2026 and well-covered by this atlas (paper counts are auto-computed from real tags):

- **Agentic AI / Multi-Agent** — 31 papers tagged `Agent`.
- **RAG / Faithfulness** — 38 papers tagged `RAG`.
- **Reasoning Models** — 129 papers tagged `Reasoning`.
- **Embodied / World Model** — 8 papers tagged `Embodied`.

---

<a id="sec-benchmark"></a>
## 📋 Benchmarks & Evaluation

> 61 evaluation / benchmark / dataset papers are listed separately (also kept in the main list below, marked 📋).

<details open>
<summary>📋 Benchmark List (61 papers — click to collapse / expand)</summary>

- **📋 [ArtChart: A Benchmark for Faithful Artistic Chart Generation with Integrated Text Rendering](https://arxiv.org/abs/2607.16060)** · arXiv · LLM · Training-free
- **📋 [HoloCount: A Holistic Visual Counting Benchmark for MLLMs](https://arxiv.org/abs/2607.06420)** · arXiv · VLM · Training-free
- **📋 [MissingBench-Verified: Probing Vision-Language Models' Inability to Detect Missing Object Parts](https://arxiv.org/abs/2607.18673)** · arXiv · VLM · Training-free
- **📋 [MoHallBench: A Benchmark for Motion Hallucination in Video Large Language Models](https://arxiv.org/abs/2607.01117)** · arXiv · VLM · Training-free
- **📋 [HalluTruthQA: A Fine-Grained Benchmark for Hallucination Detection, Localization, and Explanation in Arabic Question Answering](https://arxiv.org/abs/2607.20219)** · arXiv · LLM · Training-free
- **📋 [ClinHallu: A Benchmark for Diagnosing Stage-Wise Hallucinations in Medical MLLM Reasoning](https://arxiv.org/abs/2606.14697)** · arXiv · VLM · Training-free
- **📋 [SAGE: An Expert-Annotated South Asian GI Endoscopy Dataset for Multimodal Learning and Hallucination Analysis](https://arxiv.org/abs/2606.22144)** · arXiv · VLM · Training-free
- **📋 [A Benchmark for Hallucination Detection in VLMs for Gastrointestinal Endoscopy](https://arxiv.org/abs/2606.24115)** · arXiv · VLM · Training-free
- **📋 [MedBench v5: A Dynamic, Process-Oriented, and Hallucination-Aware Benchmark for Clinical Multimodal Models](https://arxiv.org/abs/2606.24155)** · arXiv · VLM · Training-free
- **📋 [Med-StepBench: A Hierarchical Reasoning Framework for Evaluating Hallucinations in Medical Vision-Language Models](https://arxiv.org/abs/2605.10002)** · arXiv · VLM · Training-free
- **📋 [ReactBench: A Cause-Driven Benchmark for Multimodal Hallucination via Systematic Evaluation](https://arxiv.org/abs/2605.29579)** · arXiv · VLM · Training-free
- **📋 [DetailVerifyBench: A Benchmark for Dense Hallucination Localization in Long Image Captions](https://arxiv.org/abs/2604.05623)** · arXiv · VLM · Training-free
- **📋 [DO-Bench: An Attributable Benchmark for Diagnosing Object Hallucination in Vision-Language Models](https://arxiv.org/abs/2604.22822)** · arXiv · VLM · Training-free
- **📋 [INFACT: A Diagnostic Benchmark for Induced Faithfulness and Factuality Hallucinations in Video-LLMs](https://arxiv.org/abs/2603.11481)** · arXiv · VLM · Training-free
- **📋 [HalDec-Bench: Benchmarking Hallucination Detector in Image Captioning](https://arxiv.org/abs/2603.15253)** · arXiv · VLM · Training-free
- **📋 [FREAK: A Fine-grained Hallucination Evaluation Benchmark for Advanced MLLMs](https://arxiv.org/abs/2603.19765)** · arXiv · VLM · Training-free
- **📋 [AutoHall: Automated Factuality Hallucination Dataset Generation for Large Language Models](https://doi.org/10.1109/taslpro.2025.3635038)** · Other · LLM · Training-free
- **📋 [Causal-HalBench: Uncovering LVLMs Object Hallucinations Through Causal Intervention](https://doi.org/10.1609/aaai.v40i40.40712)** · Other · VLM · Training-free
- **📋 [Constructing a Dataset for Hallucination Detection in Japanese Summarization with Fine-grained Faithfulness Labels](https://doi.org/10.18653/v1/2026.eacl-srw.15)** · Other · LLM · Training-free
- **📋 [DHEval: A Dynamic Hallucination Evaluation Protocol Robust to Data Contamination](https://doi.org/10.1109/icassp55912.2026.11462032)** · Other · LLM · Training-free
- **📋 [ESG-Bench: Benchmarking Long-Context ESG Reports for Hallucination Mitigation](https://doi.org/10.1609/aaai.v40i46.41281)** · Other · LLM · Training-based
- **📋 [FFE-Hallu: Hallucinations in Fixed Figurative Expressions: A Benchmark of Idioms and Proverbs in the Persian Language](https://doi.org/10.18653/v1/2026.eacl-long.241)** · Other · LLM · Training-free
- **📋 [GHOST: Getting to the Bottom of Hallucinations with A Multi-round Consistency Benchmark](https://doi.org/10.1109/WACV61042.2026.00596)** · Other · LLM · Training-free
- **📋 [HalluAudio: A Comprehensive Benchmark for Hallucination Detection in Large Audio-Language Models](https://aclanthology.org/2026.acl-long.1797/)** · ACL · MLLM(Omni) · Training-free
- **📋 [Hallucination Detection in Long-Form Text Generated by LLMs: A Benchmark and a Hyper-Relational Knowledge Graph Approach](https://aclanthology.org/2026.findings-acl.1673/)** · ACL · LLM · Training-free
- **📋 [KGHaluBench: A Knowledge Graph-Based Hallucination Benchmark for Evaluating the Breadth and Depth of LLM Knowledge](https://doi.org/10.18653/v1/2026.findings-eacl.206)** · Other · LLM · Training-free
- **📋 [MHB: Medical Hallucination Benchmark for Large Language Models in Complex Clinical Tasks](https://doi.org/10.1609/aaai.v40i45.41243)** · Other · LLM · Training-free
- **📋 [Multi-Hall-SA: A Cross-lingual Benchmark for Multi-Type Hallucination Detection in Low-Resource South African Languages](https://doi.org/10.18653/v1/2026.findings-eacl.330)** · Other · LLM · Training-free
- **📋 [PROBE: PROcess-Based BEnchmark for Hallucination Detection](https://aclanthology.org/2026.findings-acl.2099/)** · ACL · LLM · Training-free
- **📋 [Rethinking Evaluation for LLM Hallucination Detection: A Desiderata, A New RAG-based Benchmark, New Insights](https://aclanthology.org/2026.acl-long.680/)** · ACL · LLM · Training-free
- **📋 [TempHalluc-Bench: Evaluating Temporal Hallucination in VideoLLM-Based Video Search and Information Extraction](https://doi.org/10.5120/ijca-1aef39d4b120)** · Other · VLM · Training-free
- **📋 [MIHBench: Benchmarking and Mitigating Multi-Image Hallucinations in Multimodal Large Language Models](https://arxiv.org/abs/2508.00726)** · arXiv · VLM · Training-free
- **📋 [3D-GRAND: A Million-Scale Dataset for 3D-LLMs with Better Grounding and Less Hallucination](https://openaccess.thecvf.com/content/CVPR2025/html/Yang_3D-GRAND_A_Million-Scale_Dataset_for_3D-LLMs_with_Better_Grounding_and_CVPR_2025_paper.html)** · Unlabeled · VLM · Training-free
- **📋 [AVHBench: A Cross-Modal Hallucination Benchmark for Audio-Visual Large Language Models](https://openreview.net/forum?id=jTEKTdI3K9)** · Unlabeled · MLLM(Omni) · Training-free
- **📋 [CCHall: A Novel Benchmark for Joint Cross-Lingual and Cross-Modal Hallucinations Detection in Large Language Models](https://doi.org/10.18653/v1/2025.acl-long.1485)** · Other · LLM · Training-free
- **📋 [CodeHalu: Investigating Code Hallucinations in LLMs via Execution-based Verification](https://doi.org/10.1609/aaai.v39i24.34717)** · Other · LLM · Training-free
- **📋 [FaithBench: A Diverse Hallucination Benchmark for Summarization by Modern LLMs](https://doi.org/10.18653/v1/2025.naacl-short.38)** · Other · LLM · Training-free
- **📋 [HalluLens: LLM Hallucination Benchmark](https://doi.org/10.18653/v1/2025.acl-long.1176)** · Other · LLM · Training-free
- **📋 [How LLMs React to Industrial Spatio-Temporal Data? Assessing Hallucination with a Novel Traffic Incident Benchmark Dataset](https://doi.org/10.18653/v1/2025.naacl-industry.4)** · Other · LLM · Training-free
- **📋 [K-HALU: Multiple Answer Korean Hallucination Benchmark for Large Language Models](https://openreview.net/forum?id=VnLhUogHYE)** · Unlabeled · LLM · Training-free
- **📋 [KG-FPQ: Evaluating Factuality Hallucination in LLMs with Knowledge Graph-based False Premise Questions](https://aclanthology.org/2025.coling-main.698/)** · ACL · LLM · Training-free
- **📋 [MedHallBench: A New Benchmark for Assessing Hallucination in Medical Large Language Models](https://proceedings.mlr.press/v281/zuo25b.html)** · Unlabeled · LLM · Training-free
- **📋 [MedHallu: A Comprehensive Benchmark for Detecting Medical Hallucinations in Large Language Models](https://doi.org/10.18653/v1/2025.emnlp-main.143)** · Other · LLM · Training-free
- **📋 [MHBench: Demystifying Motion Hallucination in VideoLLMs](https://doi.org/10.1609/aaai.v39i4.32463)** · Other · LLM · Training-free
- **📋 [PHANTOM: A Benchmark for Hallucination Detection in Financial Long-Context QA](http://papers.nips.cc/paper_files/paper/2025/hash/b8badadce3f482ba340ff870f4894441-Abstract-Datasets_and_Benchmarks_Track.html)** · Unlabeled · LLM · Training-free
- **📋 [PhD: A ChatGPT-Prompted Visual Hallucination Evaluation Dataset](https://openaccess.thecvf.com/content/CVPR2025/html/Liu_PhD_A_ChatGPT-Prompted_Visual_Hallucination_Evaluation_Dataset_CVPR_2025_paper.html)** · Unlabeled · VLM · Training-free
- **📋 [ReSelfVerMM: mitigating hallucination in multimodal LLMs through dataset reconstruction and self-verification](https://doi.org/10.1117/12.3072360)** · Other · VLM · Training-free
- **📋 [SHALE: A Scalable Benchmark for Fine-grained Hallucination Evaluation in LVLMs](https://doi.org/10.1145/3746027.3758308)** · Other · VLM · Training-free
- **📋 [Detection, Diagnosis, and Explanation: A Benchmark for Chinese Medial Hallucination Evaluation](https://aclanthology.org/2024.lrec-main.428)** · ACL · LLM · Training-free
- **📋 [DiaHalu: A Dialogue-level Hallucination Evaluation Benchmark for Large Language Models](https://doi.org/10.18653/v1/2024.findings-emnlp.529)** · Other · LLM · Training-free
- **📋 [ERBench: An Entity-Relationship based Automatically Verifiable Hallucination Benchmark for Large Language Models](http://papers.nips.cc/paper_files/paper/2024/hash/5ef9853a6cdea40ae3e301a6d8dc32b5-Abstract-Datasets_and_Benchmarks_Track.html)** · Unlabeled · LLM · Training-free
- **📋 Fine-Grained Multi Image Object Hallucination Benchmark** · Unlabeled · VLM · Training-free
- **📋 [Hallucination Benchmark in Medical Visual Question Answering](https://openreview.net/forum?id=vxlXqOj4zv)** · Unlabeled · VLM · Training-free
- **📋 [HaloQuest: A Visual Hallucination Dataset for Advancing Multimodal Reasoning](https://doi.org/10.1007/978-3-031-72980-5_17)** · Other · VLM · Training-free
- **📋 [HypoTermQA: Hypothetical Terms Dataset for Benchmarking Hallucination Tendency of LLMs](https://doi.org/10.18653/v1/2024.eacl-srw.9)** · Other · LLM · Training-free
- **📋 [MASSIVE Multilingual Abstract Meaning Representation: A Dataset and Baselines for Hallucination Detection](https://doi.org/10.18653/v1/2024.starsem-1.1)** · Other · LLM · Training-free
- **📋 [THRONE: An Object-Based Hallucination Benchmark for the Free-Form Generations of Large Vision-Language Models](https://doi.org/10.1109/CVPR52733.2024.02571)** · Other · VLM · Training-free
- **📋 [ToolBeHonest: A Multi-level Hallucination Diagnostic Benchmark for Tool-Augmented Large Language Models](https://doi.org/10.18653/v1/2024.emnlp-main.637)** · Other · LLM · Training-free
- **📋 [Negative Object Presence Evaluation (NOPE) to Measure Object Hallucination in Vision-Language Models](https://arxiv.org/abs/2310.05338)** · arXiv · VLM · Training-free
- **📋 [A New Benchmark and Reverse Validation Method for Passage-level Hallucination Detection](https://doi.org/10.18653/v1/2023.findings-emnlp.256)** · Other · LLM · Training-free
- **📋 [HalOmi: A Manually Annotated Benchmark for Multilingual Hallucination and Omission Detection in Machine Translation](https://doi.org/10.18653/v1/2023.emnlp-main.42)** · Other · LLM · Training-free

</details>

---

<a id="sec-survey"></a>
## 📚 Surveys

> 15 survey / review / taxonomy papers are listed separately (also kept in the main list below, marked 📚).

<details open>
<summary>📚 Survey List (15 papers — click to collapse / expand)</summary>

- **📚 [Distorted or Fabricated? A Survey on Hallucination in Video LLMs](https://arxiv.org/abs/2604.12944)** · arXiv · VLM · Training-free
- **📚 [A Survey of Hallucination in Large Language Models](https://doi.org/10.12677/airr.2026.151016)** · Other · LLM · Training-free
- **📚 [A Taxonomy of Machine Hallucination in Radiology](https://doi.org/10.1148/ryai.250203)** · Other · LLM · Training-free
- **📚 [Hallucination to truth: a review of fact-checking and factuality evaluation in large language models](https://doi.org/10.1007/s10462-025-11454-w)** · Other · LLM · Training-free
- **📚 [House of Mirrors: A Survey on Hallucination Detection and Mitigation via Decoding Techniques in Language Models](https://doi.org/10.1007/978-3-032-03072-6_9)** · Other · LLM · Training-free
- **📚 [Large language models hallucination: A comprehensive survey](https://doi.org/10.1016/j.cosrev.2026.100970)** · Other · LLM · Training-free
- **📚 [Loki’s Dance of Illusions: A Comprehensive Survey of Hallucination in Large Language Models](https://doi.org/10.1109/tcss.2026.3661295)** · Other · LLM · Training-free
- **📚 [Model stability and hallucination under the data-knowledge dual-drive paradigm: a survey](https://doi.org/10.1117/12.3110427)** · Other · LLM · Training-free
- **📚 [Survey on Hallucination in Reasoning Large Language Model: Evaluation, Taxonomy, Intervention, and Open Issues](https://doi.org/10.3724/2096-7004.di.2025.0131)** · Other · LLM · Training-free
- **📚 [A Survey of Multimodal Hallucination Evaluation and Detection](https://arxiv.org/abs/2507.19024)** · arXiv · VLM · Training-free
- **📚 [A Review of Faithfulness Metrics for Hallucination Assessment in Large Language Models](https://doi.org/10.1109/jstsp.2025.3579203)** · Other · LLM · Training-free
- **📚 [🧜Siren’s Song in the AI Ocean: A Survey on Hallucination in Large Language Models](https://doi.org/10.1162/coli.a.16)** · Other · LLM · Training-free
- **📚 [A Comprehensive Survey of Hallucination in Large Language, Image, Video and Audio Foundation Models](https://doi.org/10.18653/v1/2024.findings-emnlp.685)** · Other · MLLM(Omni) · Training-free
- **📚 [Can Knowledge Graphs Reduce Hallucinations in LLMs? : A Survey](https://doi.org/10.18653/v1/2024.naacl-long.219)** · Other · LLM · Training-free
- **📚 [Cognitive Mirage: A Review of Hallucinations in Large Language Models](https://ceur-ws.org/Vol-3818/paper2.pdf)** · Unlabeled · LLM · Training-free

</details>

---

<a id="sec-paperlist"></a>
## 📚 Paper List

> Grouped by year; click a year header to expand / collapse. Format per entry: **Title** · venue/year · model · method · 💻code. Title links prefer the official venue version. 📋 = Benchmark paper, 📚 = Survey paper. Full abstracts and multi-dimensional filtering are available in the interactive website [`docs/index.html`](docs/index.html). PRs welcome.

<details open>
<summary>📅 2027 · 5 papers</summary>

- **[A Multi-agent Framework for Factuality Hallucination Detection Using Complex Knowledge Graph](https://doi.org/10.1007/978-981-92-2480-7_10)** · Other · LLM · Training-free
- **[Beyond Statistical Divergence: A Hybrid Calibration Framework for Decoupling Hallucination in Large Language Models](https://doi.org/10.1007/978-981-92-2480-7_9)** · Other · LLM · Training-free
- **[Combining NotebookLM and Gemini Gems to Reduce Hallucination and Curriculum Misalignment in Programming Education: System Design and Early Evidence](https://doi.org/10.1007/978-3-032-32115-2_45)** · Other · LLM · Training-free
- **[Quantum Entropy–Driven Temperature Scaling for Hallucination Mitigation in Generative Models](https://doi.org/10.1007/978-3-032-28379-5_48)** · Other · LLM · Training-free
- **[Uncovering Reasoning Failures: Hallucination Detection via Semantic Probing and Attention Tracking](https://doi.org/10.1007/978-981-92-2480-7_23)** · Other · LLM · Training-free

</details>

<details>
<summary>📅 2026 · 409 papers</summary>

- **📋 [ArtChart: A Benchmark for Faithful Artistic Chart Generation with Integrated Text Rendering](https://arxiv.org/abs/2607.16060)** · arXiv · LLM · Training-free
- **[Deceptive Grounding: Entity Attribution Failure in Clinical Retrieval-Augmented Generation](https://arxiv.org/abs/2607.09349)** · arXiv · LLM · Training-free
- **[Do Medical Vision Language Models Actually See? A Counterfactual Grounding Framework and Hard-Negative Contrastive Training for Visually-Reliant Medical VLMs](https://arxiv.org/abs/2607.03647)** · arXiv · VLM · Training-free
- **[Faithful by Design: Evaluating and Improving LLM-Generated Clinical Trial Summaries for Multi-Stakeholder Audiences](https://arxiv.org/abs/2607.09932)** · arXiv · LLM · Training-free
- **[Groc-PO: Grounded Context Preference Optimization for Truthful Multimodal LLMs](https://arxiv.org/abs/2607.13712)** · arXiv · VLM · Training-based
- **[HALLMARK: Diagnosing Three Failure Modes in LLM Citation Verifiers](https://arxiv.org/abs/2607.18360)** · arXiv · LLM · Training-free
- **📋 [HoloCount: A Holistic Visual Counting Benchmark for MLLMs](https://arxiv.org/abs/2607.06420)** · arXiv · VLM · Training-free
- **📋 [MissingBench-Verified: Probing Vision-Language Models' Inability to Detect Missing Object Parts](https://arxiv.org/abs/2607.18673)** · arXiv · VLM · Training-free
- **[ProCap: Prominence-guided Object Rectification for Faithful and Comprehensive Video Captioning](https://arxiv.org/abs/2607.21022)** · arXiv · VLM · Training-free
- **[Readable but Not Controllable: Neuron-Level Evidence for Medical LLM Hallucination](https://arxiv.org/abs/2607.00158)** · arXiv · LLM · Training-free
- **[Beyond Document Grounding: Span-Level Hallucination Detection over Code, Tool Output, and Documents](https://arxiv.org/abs/2607.00895)** · arXiv · LLM · Training-based
- **[Grounded Optimization: A Layered Engineering Framework for Reducing LLM Hallucination in Automated Personal Document Rewriting](https://arxiv.org/abs/2607.01457)** · arXiv · LLM · Training-free
- **📋 [MoHallBench: A Benchmark for Motion Hallucination in Video Large Language Models](https://arxiv.org/abs/2607.01117)** · arXiv · VLM · Training-free
- **[Mitigating Package Hallucinations in Large Language Models via Model Editing](https://arxiv.org/abs/2607.02052)** · arXiv · LLM · Training-based
- **[From Judgments to Issues: Structured Extraction of Legal Reasoning with Citation-Hallucination Control](https://arxiv.org/abs/2607.03325)** · arXiv · LLM · Training-free
- **[CrossHallu: Do Hallucination Signals Generalize Across Languages and Domains in Large Language Model's Internals?](https://arxiv.org/abs/2607.04029)** · arXiv · LLM · Training-free
- **[SeeMe: Mitigating Hallucinations in Large Vision-Language Models through Effective Visual Token Engineering](https://arxiv.org/abs/2607.04163)** · arXiv · VLM · Training-free
- **[Hallucination Detector: A hybrid LLM and Semantic Scholar tool calling for detecting hallucination in scientific literature on AtomGPT.org](https://arxiv.org/abs/2607.09774)** · arXiv · LLM · Training-free
- **[Hallucination Self-Play: Bootstrapping Reinforced Detector via Evolved Generator](https://arxiv.org/abs/2607.07993)** · arXiv · LLM · Training-based
- **[HIVE: Understanding Post-Hallucination Reasoning in Vision Language Models](https://arxiv.org/abs/2607.07507)** · arXiv · VLM · Training-free
- **[Game Theory Driven Multi-Agent Framework Mitigates Language Model Hallucination](https://arxiv.org/abs/2607.08403)** · arXiv · LLM · Training-free
- **[Hallucination Detection in Large Language Models Using Diversion Decoding](https://arxiv.org/abs/2607.10476)** · arXiv · LLM · Training-free
- **[To Answer or to Abstain: Mitigating Search-Agent Hallucinations via Abstention-Aware Reinforcement Learning](https://arxiv.org/abs/2607.10738)** · arXiv · LLM · Training-based
- **[Confidently Wrong: Detecting Hallucinations in Financial Question Answering from LLM Internal States](https://arxiv.org/abs/2607.11414)** · arXiv · LLM · Training-based
- **[Evidence-Grounded Verified Agentic Reasoning: A Path Toward Eliminating LLM Hallucination in Empirical Inference via Tool-Attested Kernel Proofs](https://arxiv.org/abs/2607.12650)** · arXiv · LLM · Training-free
- **[Hallo4D: Multi-Modal Hallucination Mitigation for Consistent Spatio-Temporal Generation](https://arxiv.org/abs/2607.12752)** · arXiv · VLM · Training-free
- **[Protective Capacity Hallucination: When Large Language Models Claim Nonexistent Capabilities](https://arxiv.org/abs/2607.13596)** · arXiv · LLM · Training-free
- **[Look Clearly Before Answering: Mitigating Hallucinations in LVLMs via Saliency-Driven Perceptual Realignment](https://arxiv.org/abs/2607.16841)** · arXiv · VLM · Training-free
- **[Operational Hallucination and Safety Drift in AI Agents](https://arxiv.org/abs/2607.18366)** · arXiv · LLM · Training-free
- **[Zero Hallucination, by Construction: Hallucination-Aware Layered Oversight for Trustworthy Enterprise AI](https://arxiv.org/abs/2607.17883)** · arXiv · LLM · Training-free
- **[Prompt Design at Scale: How Format, Instruction Count, and Context Length Shape Instruction Adherence and Hallucination in Large Language Models](https://arxiv.org/abs/2607.19257)** · arXiv · LLM · Training-free
- **📋 [HalluTruthQA: A Fine-Grained Benchmark for Hallucination Detection, Localization, and Explanation in Arabic Question Answering](https://arxiv.org/abs/2607.20219)** · arXiv · LLM · Training-free
- **[Score-Control for Hallucination Reduction in Diffusion Models](https://arxiv.org/abs/2606.00377)** · arXiv · MLLM(Omni) · Training-free
- **[MM-Snowball: Evaluating and Mitigating Hallucination Snowballing in Multimodal Multi-Turn Dialogue](https://arxiv.org/abs/2606.00622)** · arXiv · VLM · Training-free
- **[Hallucination-Aware Diffusion Sampling for Inverse Problems via Robust Prior Updates](https://arxiv.org/abs/2606.02331)** · arXiv · VLM · Training-free
- **[OmniHalluc-L: Counterfactual Benchmarking and Modality-Perturbation Reliability Calibration for Long-Form Omni Hallucination](https://arxiv.org/abs/2606.03614)** · arXiv · MLLM(Omni) · Training-free
- **[P²-DPO: Grounding Hallucination in Perceptual Processing via Calibration Direct Preference Optimization](https://arxiv.org/abs/2606.03376)** · arXiv · VLM · Training-based
- **[Steer Where It Matters: Token-Level Visual-Sensitivity Steering for LVLMs Hallucination Mitigation](https://arxiv.org/abs/2606.07647)** · arXiv · VLM · Training-free
- **[How Many Counterfactuals Does It Take? Probing VLM Hallucinations Through Circuits and Causal Effects](https://arxiv.org/abs/2606.08777)** · arXiv · VLM · Training-free
- **[Density Ridge Selective Prediction for LLM and VLM Hallucination Detection under Calibration Label Scarcity](https://arxiv.org/abs/2606.10198)** · arXiv · VLM · Training-free
- **[Disentangling Hallucinations: Orthogonal Semantic Projection for Robust Interpretability](https://arxiv.org/abs/2606.14758)** · arXiv · VLM · Training-free
- **[MultiToP: Learning to Patch Visual Tokens to Mitigate Hallucinations in Video Large Multimodal Models](https://arxiv.org/abs/2606.11792)** · arXiv · VLM · Training-free
- **📋 [ClinHallu: A Benchmark for Diagnosing Stage-Wise Hallucinations in Medical MLLM Reasoning](https://arxiv.org/abs/2606.14697)** · arXiv · VLM · Training-free
- **[Mitigating Visual Hallucinations in Multimodal Systems through Retrieval-Augmented Reliability-Aware Inference](https://arxiv.org/abs/2606.15782)** · arXiv · VLM · Training-free
- **[Hallucination Detection and Correction in Medical VLMs via Counter-Evidence Verification](https://arxiv.org/abs/2606.18609)** · arXiv · VLM · Training-free
- **[Thermodynamic Signatures of Reasoning: Free-Energy and Spectral-Form-Factor Diagnostics for Hallucination Detection in Large Language Models](https://arxiv.org/abs/2606.19404)** · arXiv · LLM · Training-free
- **[Spectral Query-Key Product Weight Steering for Training-Free VLM Hallucination Mitigation](https://arxiv.org/abs/2606.20419)** · arXiv · VLM · Training-free
- **[Finetuning with Scientific Data Increases Hallucinations: A Multi-domain Factuality Evaluation of LLMs](https://arxiv.org/abs/2606.21359)** · arXiv · LLM · Training-free
- **[Hallucination as Context Drift: Synchronization Protocols for Multi-Agent LLM Systems](https://arxiv.org/abs/2606.21666)** · arXiv · LLM · Training-free
- **[Pre-Generation Hallucination Detection in Large Language Models via Soft-Target Attention Probing](https://arxiv.org/abs/2606.21917)** · arXiv · LLM · Training-free
- **📋 [SAGE: An Expert-Annotated South Asian GI Endoscopy Dataset for Multimodal Learning and Hallucination Analysis](https://arxiv.org/abs/2606.22144)** · arXiv · VLM · Training-free
- **[From Text Metrics to Model Internals: A Study of Whisper ASR Hallucination Detection](https://arxiv.org/abs/2606.23060)** · arXiv · MLLM(Omni) · Training-free
- **[TTFT-Aware Graph Chain-of-Thought:Distance-Indexed Neural A* for Low-Hallucination Multi-Hop Medical Reasoning](https://arxiv.org/abs/2606.23108)** · arXiv · LLM · Training-free
- **📋 [A Benchmark for Hallucination Detection in VLMs for Gastrointestinal Endoscopy](https://arxiv.org/abs/2606.24115)** · arXiv · VLM · Training-free
- **[Grad Detect: Gradient-Based Hallucination Detection in LLMs](https://arxiv.org/abs/2606.24790)** · arXiv · LLM · Training-free
- **📋 [MedBench v5: A Dynamic, Process-Oriented, and Hallucination-Aware Benchmark for Clinical Multimodal Models](https://arxiv.org/abs/2606.24155)** · arXiv · VLM · Training-free
- **[Staying VIGILant: Mitigating Visual Laziness via Counterfactual Visual Alignment in MLLMs](https://arxiv.org/abs/2606.26387)** · arXiv · VLM · Training-based
- **[Vision-driven Preference Synthesis for Mitigating Hallucinations in VLMs](https://arxiv.org/abs/2606.28401)** · arXiv · VLM · Training-free
- **[From Hallucination to Grounding: Diagnosing Visual Spatial Intelligence via CRISP](https://arxiv.org/abs/2606.26535)** · arXiv · VLM · Training-free
- **[Hallucination in World Models is Predictable and Preventable](https://arxiv.org/abs/2606.27326)** · arXiv · VLM · Training-based
- **[TAVR-VLM: Risk-Conditioned Causal Grounding for Hallucination-Resistant Report Generation](https://arxiv.org/abs/2606.26874)** · arXiv · VLM · Training-free
- **[AURORA: Asymmetry and Update-Induced Rotation for Robust Hallucination Detection in Large Language Models](https://arxiv.org/abs/2606.29545)** · arXiv · VLM · Training-free
- **[Citation Discipline in Spec-Driven Development: A Cross-Model Empirical Study of Output Determinism and Automated Hallucination Detection in LLM-Generated Code](https://arxiv.org/abs/2606.30689)** · arXiv · LLM · Training-free
- **[FADE: Mitigating Hallucinations by Reducing Language-Prior Dominance in Large Vision-Language Models](https://arxiv.org/abs/2606.29431)** · arXiv · VLM · Training-free
- **[Clearer Sight, Fewer Lies: Oriented Pickup Preference Optimization for Multimodal Hallucination Mitigation](https://arxiv.org/abs/2606.29805)** · arXiv · VLM · Training-based
- **[Free-form Association Tasks Reveal Stereotype Hallucination in Large Language Models](https://arxiv.org/abs/2606.30945)** · arXiv · VLM · Training-free
- **[See Only When Needed: Context-Aware Attention Intervention for Mitigating Hallucinations in LVLMs](https://arxiv.org/abs/2606.29847)** · arXiv · VLM · Training-free
- **[CORTEX: Token-Level Hallucination Detection in RAG via Comparative Internal Representations](https://arxiv.org/abs/2606.31033)** · arXiv · LLM · Training-free
- **[No Place to Hide: Benchmarking Video Hallucination with Background-Controlled Pairs](https://arxiv.org/abs/2606.31933)** · arXiv · VLM · Training-free
- **[Online Self-Calibration Against Hallucination in Vision-Language Models](https://arxiv.org/abs/2605.00323)** · arXiv · VLM · Training-based
- **[GEASS: Training-Free Caption Steering for Hallucination Mitigation in Vision-Language Models](https://arxiv.org/abs/2605.01733)** · arXiv · VLM · Training-free
- **[Mitigating Multimodal LLMs Hallucinations via Relevance Propagation at Inference Time](https://arxiv.org/abs/2605.01766)** · arXiv · MLLM(Omni) · Training-free
- **[CAST: Mitigating Object Hallucination in Large Vision-Language Models via Caption-Guided Visual Attention Steering](https://arxiv.org/abs/2605.04641)** · arXiv · VLM · Training-free
- **[When Relations Break: Analyzing Relation Hallucination in Vision-Language Model Under Rotation and Noise](https://arxiv.org/abs/2605.05045)** · arXiv · VLM · Training-free
- **[From Clouds to Hallucinations: Atmospheric Retrieval Hijacking in Remote Sensing Vision-Language RAG](https://arxiv.org/abs/2605.07273)** · arXiv · VLM · Training-free
- **[Object Hallucination-Free Reinforcement Unlearning for Vision-Language Models](https://arxiv.org/abs/2605.08031)** · arXiv · VLM · Training-based
- **📋 [Med-StepBench: A Hierarchical Reasoning Framework for Evaluating Hallucinations in Medical Vision-Language Models](https://arxiv.org/abs/2605.10002)** · arXiv · VLM · Training-free
- **[Vocabulary Hijacking in LVLMs: Unveiling Critical Attention Heads by Excluding Inert Tokens to Mitigate Hallucination](https://arxiv.org/abs/2605.10622)** · arXiv · VLM · Training-free
- **[Instruction Lens Score: Your Instruction Contributes a Powerful Object Hallucination Detector for Multimodal Large Language Models](https://arxiv.org/abs/2605.12258)** · arXiv · VLM · Training-free
- **[Mitigating Action-Relation Hallucinations in LVLMs via Relation-aware Visual Enhancement](https://arxiv.org/abs/2605.11808)** · arXiv · VLM · Training-free
- **[When Looking Is Not Enough: Visual Attention Structure Reveals Hallucination in MLLMs](https://arxiv.org/abs/2605.11559)** · arXiv · VLM · Training-free
- **[Dual-Pathway Circuits of Object Hallucination in Vision-Language Models](https://arxiv.org/abs/2605.13156)** · arXiv · VLM · Training-free
- **[Reducing Hallucination in Vision-Language Models via Stage-wise Preference Optimization under Distribution Shift](https://arxiv.org/abs/2605.16411)** · arXiv · VLM · Training-based
- **[Do We Really Need External Tools to Mitigate Hallucinations? SIRA: Shared-Prefix Internal Reconstruction of Attribution](https://arxiv.org/abs/2605.14621)** · arXiv · VLM · Training-free
- **[MHSA: A Lightweight Framework for Mitigating Hallucinations via Steered Attention in LVLMs](https://arxiv.org/abs/2605.14966)** · arXiv · VLM · Training-free
- **[How do Humans Process AI-generated Hallucination Contents: a Neuroimaging Study](https://arxiv.org/abs/2605.16953)** · arXiv · VLM · Training-free
- **[Causal Evidence for Attention Head Imbalance in Modality Conflict Hallucination](https://arxiv.org/abs/2605.19250)** · arXiv · VLM · Training-free
- **[HalluCXR: Benchmarking and Mitigating Hallucinations in Medical Vision-Language Models for Chest Radiograph Interpretation](https://arxiv.org/abs/2605.20469)** · arXiv · VLM · Training-free
- **[Finding the Correct Visual Evidence Without Forgetting: Mitigating Hallucination in LVLMs via Inter-Layer Visual Attention Discrepancy](https://arxiv.org/abs/2605.20965)** · arXiv · VLM · Training-free
- **[Mitigating Hallucinations in Large Vision-Language Models via Causal Route Gating](https://arxiv.org/abs/2605.24024)** · arXiv · VLM · Training-free
- **[Reducing Object Hallucination in LVLMs via Emphasizing Image-negative Tokens](https://arxiv.org/abs/2605.21300)** · arXiv · VLM · Training-free
- **[VIHD: Visual Intervention-based Hallucination Detection for Medical Visual Question Answering](https://arxiv.org/abs/2605.20772)** · arXiv · VLM · Training-free
- **[Transcoders Trace Visual Grounding and Hallucinations in Vision-Language Models](https://arxiv.org/abs/2605.22902)** · arXiv · VLM · Training-free
- **[CHASD: Language Increment-Calibrated Contrastive Decoding against Hallucination in LVLMs](https://arxiv.org/abs/2605.23344)** · arXiv · VLM · Training-free
- **[Correcting Visual Blur Induced by Attention Distraction to Reduce Hallucinations: Algorithm and Theory](https://arxiv.org/abs/2605.24602)** · arXiv · VLM · Training-free
- **[Mitigating Object Hallucinations in Vision-Language Models through Region-Aware Attention Recalibration](https://arxiv.org/abs/2605.24957)** · arXiv · VLM · Training-free
- **[Adversarial Orthogonal Disentanglement for LVLM Hallucination Mitigation](https://arxiv.org/abs/2605.25377)** · arXiv · VLM · Training-free
- **[Hallucination Behavior in Multimodal LLMs Across Agricultural Image Interpretation and Generation Tasks](https://arxiv.org/abs/2605.27595)** · arXiv · VLM · Training-free
- **[Reasoning Matters: Mitigate Hallucination in Multimodal Large Reasoning Models via Reasoning-Conditioned Preference Optimization](https://arxiv.org/abs/2605.27906)** · arXiv · VLM · Training-based
- **[Rethinking Visual Neglect: Steering via Context-Preference for MLLM Hallucination Mitigation](https://arxiv.org/abs/2605.27993)** · arXiv · VLM · Training-free
- **[Risk-aware Selective Prompting for Hallucination Mitigation in Large Vision-Language Models](https://arxiv.org/abs/2605.28123)** · arXiv · VLM · Training-free
- **[Mitigating Content Shift and Hallucination in GenAI Image Editing via Structural Refinement](https://arxiv.org/abs/2605.30437)** · arXiv · VLM · Training-free
- **[Mitigating Hallucination in Vision-Language Models through Barrier-Regulated Adaptive Closed-form Steering](https://arxiv.org/abs/2605.29881)** · arXiv · VLM · Training-free
- **📋 [ReactBench: A Cause-Driven Benchmark for Multimodal Hallucination via Systematic Evaluation](https://arxiv.org/abs/2605.29579)** · arXiv · VLM · Training-free
- **[Learning from Fine-Grained Visual Discrepancies: Mitigating Multimodal Hallucinations via In-Context Visual Contrastive Optimization](https://arxiv.org/abs/2605.31312)** · arXiv · VLM · Training-based
- **[What Makes LVLMs Hallucinate Less? Unveiling the Architectural Factors Behind Hallucination Robustness](https://arxiv.org/abs/2605.30911)** · arXiv · VLM · Training-free
- **[YARD: Y-Architecture Register Decoding for Efficient Hallucination Mitigation in Large Vision-Language Models](https://arxiv.org/abs/2605.31429)** · arXiv · VLM · Training-free
- **[ACT Now: Preempting LVLM Hallucinations via Adaptive Context Integration](https://arxiv.org/abs/2604.00983)** · arXiv · VLM · Training-free
- **[First Logit Boosting: Visual Grounding Method to Mitigate Object Hallucination in Large Vision-Language Models](https://arxiv.org/abs/2604.00455)** · arXiv · VLM · Training-free
- **[Look Twice: Training-Free Evidence Highlighting in Multimodal Large Language Models](https://arxiv.org/abs/2604.01280)** · arXiv · VLM · Training-free
- **[Attention at Rest Stays at Rest: Breaking Visual Inertia for Cognitive Hallucination Mitigation](https://arxiv.org/abs/2604.01989)** · arXiv · VLM · Training-free
- **[STEAR: Layer-Aware Spatiotemporal Evidence Intervention for Hallucination Mitigation in Video Large Language Models](https://arxiv.org/abs/2604.03045)** · arXiv · VLM · Training-free
- **[Focus Matters: Phase-Aware Suppression for Hallucination in Vision-Language Models](https://arxiv.org/abs/2604.03556)** · arXiv · VLM · Training-free
- **[Beyond the Global Scores: Fine-Grained Token Grounding as a Robust Detector of LVLM Hallucinations](https://arxiv.org/abs/2604.04863)** · arXiv · VLM · Training-free
- **📋 [DetailVerifyBench: A Benchmark for Dense Hallucination Localization in Long Image Captions](https://arxiv.org/abs/2604.05623)** · arXiv · VLM · Training-free
- **[HaloProbe: Bayesian Detection and Mitigation of Object Hallucinations in Vision-Language Models](https://arxiv.org/abs/2604.06165)** · arXiv · VLM · Training-free
- **[Steering the Verifiability of Multimodal AI Hallucinations](https://arxiv.org/abs/2604.06714)** · arXiv · VLM · Training-free
- **[3D-VCD: Hallucination Mitigation in 3D-LLM Embodied Agents through Visual Contrastive Decoding](https://arxiv.org/abs/2604.08645)** · arXiv · VLM · Training-free
- **[Mitigating Entangled Steering in Large Vision-Language Models for Hallucination Reduction](https://arxiv.org/abs/2604.07914)** · arXiv · VLM · Training-free
- **[See Fair, Speak Truth: Equitable Attention Improves Grounding and Reduces Hallucination in Vision-Language Alignment](https://arxiv.org/abs/2604.09749)** · arXiv · VLM · Training-free
- **[SinkTrack: Attention Sink based Context Anchoring for Large Language Models](https://arxiv.org/abs/2604.10027)** · arXiv · VLM · Training-free
- **[Spotlight and Shadow: Attention-Guided Dual-Anchor Introspective Decoding for MLLM Hallucination Mitigation](https://arxiv.org/abs/2604.10071)** · arXiv · VLM · Training-free
- **[A Progressive Training Strategy for Vision-Language Models to Counteract Spatio-Temporal Hallucinations in Embodied Reasoning](https://arxiv.org/abs/2604.10506)** · arXiv · VLM · Training-based
- **[Benchmarking Deflection and Hallucination in Large Vision-Language Models](https://arxiv.org/abs/2604.12033)** · arXiv · VLM · Training-free
- **[HTDC: Hesitation-Triggered Differential Calibration for Mitigating Hallucination in Large Vision-Language Models](https://arxiv.org/abs/2604.12115)** · arXiv · VLM · Training-free
- **[Decoding by Perturbation: Mitigating MLLM Hallucinations via Dynamic Textual Perturbation](https://arxiv.org/abs/2604.12424)** · arXiv · VLM · Training-free
- **📚 [Distorted or Fabricated? A Survey on Hallucination in Video LLMs](https://arxiv.org/abs/2604.12944)** · arXiv · VLM · Training-free
- **[Aligning What Vision-Language Models See and Perceive with Adaptive Information Flow](https://arxiv.org/abs/2604.15809)** · arXiv · VLM · Training-free
- **📋 [DO-Bench: An Attributable Benchmark for Diagnosing Object Hallucination in Vision-Language Models](https://arxiv.org/abs/2604.22822)** · arXiv · VLM · Training-free
- **[HalluClear: Diagnosing, Evaluating and Mitigating Hallucinations in GUI Agents](https://arxiv.org/abs/2604.17284)** · arXiv · VLM · Training-based
- **[When Text Hijacks Vision: Benchmarking and Mitigating Text Overlay-Induced Hallucination in Vision Language Models](https://arxiv.org/abs/2604.17375)** · arXiv · VLM · Training-based
- **[LLM-as-Judge Framework for Evaluating Tone-Induced Hallucination in Vision-Language Models](https://arxiv.org/abs/2604.18803)** · arXiv · VLM · Training-free
- **[Mitigating Multimodal Hallucination via Phase-wise Self-reward](https://arxiv.org/abs/2604.17982)** · arXiv · VLM · Training-free
- **[VCE: A zero-cost hallucination mitigation method of LVLMs via visual contrastive editing](https://arxiv.org/abs/2604.19412)** · arXiv · VLM · Training-free
- **[R-CoV: Region-Aware Chain-of-Verification for Alleviating Object Hallucinations in LVLMs](https://arxiv.org/abs/2604.20696)** · arXiv · VLM · Training-free
- **[When Prompts Override Vision: Prompt-Induced Hallucinations in LVLMs](https://arxiv.org/abs/2604.21911)** · arXiv · VLM · Training-based
- **[SycoPhantasy: Quantifying Sycophancy and Hallucination in Small Open Weight VLMs for Vision-Language Scoring of Fantasy Characters](https://arxiv.org/abs/2604.24346)** · arXiv · VLM · Training-free
- **[Prefill-Time Intervention for Mitigating Hallucination in Large Vision-Language Models](https://arxiv.org/abs/2604.25642)** · arXiv · VLM · Training-free
- **[Self-Correction Inside the Model: Leveraging Layer Attention to Mitigate Hallucinations in Large Vision Language Models](https://arxiv.org/abs/2603.00437)** · arXiv · VLM · Training-free
- **[Semantic Similarity is a Spurious Measure of Comic Understanding: Lessons Learned from Hallucinations in a Benchmarking Experiment](https://arxiv.org/abs/2603.01950)** · arXiv · VLM · Training-free
- **[MoD-DPO: Towards Mitigating Cross-modal Hallucinations in Omni LLMs using Modality Decoupled Preference Optimization](https://arxiv.org/abs/2603.03192)** · arXiv · MLLM(Omni) · Training-based
- **[Seeing Clearly without Training: Mitigating Hallucinations in Multimodal LLMs for Remote Sensing](https://arxiv.org/abs/2603.02754)** · arXiv · VLM · Training-free
- **[AdaIAT: Adaptively Increasing Attention to Generated Text to Alleviate Hallucinations in LVLM](https://arxiv.org/abs/2603.04908)** · arXiv · VLM · Training-free
- **[Lyapunov Probes for Hallucination Detection in Large Foundation Models](https://arxiv.org/abs/2603.06081)** · arXiv · VLM · Training-based
- **[Looking Back and Forth: Cross-Image Attention Calibration and Attentive Preference Learning for Multi-Image Hallucination Mitigation](https://arxiv.org/abs/2603.07048)** · arXiv · VLM · Training-based
- **[Overthinking Causes Hallucination: Tracing Confounder Propagation in Vision Language Models](https://arxiv.org/abs/2603.07619)** · arXiv · VLM · Training-free
- **[GroundCount: Grounding Vision-Language Models with Object Detection for Mitigating Counting Hallucinations](https://arxiv.org/abs/2603.10978)** · arXiv · VLM · Training-free
- **[One Token, Two Fates: A Unified Framework via Vision Token Manipulation Against MLLMs Hallucination](https://arxiv.org/abs/2603.10360)** · arXiv · VLM · Training-free
- **📋 [INFACT: A Diagnostic Benchmark for Induced Faithfulness and Factuality Hallucinations in Video-LLMs](https://arxiv.org/abs/2603.11481)** · arXiv · VLM · Training-free
- **[On the Nature of Attention Sink that Shapes Decoding Strategy in Omni-LLMs](https://arxiv.org/abs/2603.14337)** · arXiv · MLLM(Omni) · Training-free
- **📋 [HalDec-Bench: Benchmarking Hallucination Detector in Image Captioning](https://arxiv.org/abs/2603.15253)** · arXiv · VLM · Training-free
- **[Kestrel: Grounding Self-Refinement for LVLM Hallucination Mitigation](https://arxiv.org/abs/2603.16664)** · arXiv · VLM · Training-free
- **[Locate-then-Sparsify: Attribution Guided Sparse Strategy for Visual Hallucination Mitigation](https://arxiv.org/abs/2603.16284)** · arXiv · VLM · Training-free
- **[Segmentation-Based Attention Entropy: Detecting and Mitigating Object Hallucinations in Large Vision-Language Models](https://arxiv.org/abs/2603.16558)** · arXiv · VLM · Training-free
- **📋 [FREAK: A Fine-grained Hallucination Evaluation Benchmark for Advanced MLLMs](https://arxiv.org/abs/2603.19765)** · arXiv · VLM · Training-free
- **[Deterministic Hallucination Detection in Medical VQA via Confidence-Evidence Bayesian Gain](https://arxiv.org/abs/2603.21693)** · arXiv · VLM · Training-free
- **[Mitigating Object Hallucinations in LVLMs via Attention Imbalance Rectification](https://arxiv.org/abs/2603.24058)** · arXiv · VLM · Training-free
- **[Revealing Multi-View Hallucination in Large Vision-Language Models](https://arxiv.org/abs/2603.23934)** · arXiv · VLM · Training-free
- **[Seeing to Ground: Visual Attention for Hallucination-Resilient MDLLMs](https://arxiv.org/abs/2603.25711)** · arXiv · VLM · Training-free
- **[Visual Attention Drifts,but Anchors Hold:Mitigating Hallucination in Multimodal Large Language Models via Cross-Layer Visual Anchors](https://arxiv.org/abs/2603.25088)** · arXiv · VLM · Training-free
- **[SAGE: Sink-Aware Grounded Decoding for Multimodal Hallucination Mitigation](https://arxiv.org/abs/2603.27898)** · arXiv · VLM · Training-free
- **[Hallucination-aware intermediate representation edit in large vision-language models](https://arxiv.org/abs/2603.29405)** · arXiv · VLM · Training-free
- **[Learning to Decode Against Compositional Hallucination in Video Multimodal Large Language Models](https://arxiv.org/abs/2602.00559)** · arXiv · VLM · Training-based
- **[Towards Interpretable Hallucination Analysis and Mitigation in LVLMs via Contrastive Neuron Steering](https://arxiv.org/abs/2602.00621)** · arXiv · VLM · Training-free
- **[Residual Decoding: Mitigating Hallucinations in Large Vision-Language Models via History-Aware Residual Guidance](https://arxiv.org/abs/2602.01047)** · arXiv · VLM · Training-free
- **[Do I Really Know? Learning Factual Self-Verification for Hallucination Reduction](https://arxiv.org/abs/2602.02018)** · arXiv · LLM · Training-based
- **[IRIS: Implicit Reward-Guided Internal Sifting for Mitigating Multimodal Hallucination](https://arxiv.org/abs/2602.01769)** · arXiv · VLM · Training-based
- **[Beyond Static Cropping: Layer-Adaptive Visual Localization and Decoding Enhancement](https://arxiv.org/abs/2602.04304)** · arXiv · VLM · Training-free
- **[KVSmooth: Mitigating Hallucination in Multi-modal Large Language Models through Key-Value Smoothing](https://arxiv.org/abs/2602.04268)** · arXiv · VLM · Training-free
- **[Attention to details, logits to truth: visual-aware attention and logits enhancement to mitigate hallucinations in LVLMs](https://arxiv.org/abs/2602.09521)** · arXiv · VLM · Training-free
- **[SAKED: Mitigating Hallucination in Large Vision-Language Models via Stability-Aware Knowledge Enhanced Decoding](https://arxiv.org/abs/2602.09825)** · arXiv · VLM · Training-free
- **[Scalpel: Fine-Grained Alignment of Attention Activation Manifolds via Mixture Gaussian Bridges to Mitigate Multimodal Hallucination](https://arxiv.org/abs/2602.09541)** · arXiv · VLM · Training-free
- **[SchroMind: Mitigating Hallucinations in Multimodal Large Language Models via Solving the Schrodinger Bridge Problem](https://arxiv.org/abs/2602.09528)** · arXiv · VLM · Training-free
- **[HII-DPO: Eliminate Hallucination via Accurate Hallucination-Inducing Counterfactual Images](https://arxiv.org/abs/2602.10425)** · arXiv · VLM · Training-based
- **[RSHallu: Dual-Mode Hallucination Evaluation for Remote-Sensing Multimodal Large Language Models with Domain-Tailored Mitigation](https://arxiv.org/abs/2602.10799)** · arXiv · VLM · Training-based
- **[Mask What Matters: Mitigating Object Hallucinations in Multimodal Large Language Models with Object-Aligned Visual Contrastive Decoding](https://arxiv.org/abs/2602.11737)** · arXiv · VLM · Training-free
- **[Revis: Sparse Latent Steering to Mitigate Object Hallucination in Large Vision-Language Models](https://arxiv.org/abs/2602.11824)** · arXiv · VLM · Training-free
- **[AdaVBoost: Mitigating Hallucinations in LVLMs via Token-Level Adaptive Visual Attention Boosting](https://arxiv.org/abs/2602.13600)** · arXiv · VLM · Training-free
- **[VIGIL: Tackling Hallucination Detection in Image Recontextualization](https://arxiv.org/abs/2602.14633)** · arXiv · VLM · Training-free
- **[Detecting Contextual Hallucinations in LLMs with Frequency-Aware Attention](https://arxiv.org/abs/2602.18145)** · arXiv · LLM · Training-free
- **[HIME: Mitigating Object Hallucinations in LVLMs via Hallucination Insensitivity Model Editing](https://arxiv.org/abs/2602.18711)** · arXiv · VLM · Training-based
- **[Causal Decoding for Hallucination-Resistant Multimodal Large Language Models](https://arxiv.org/abs/2602.21441)** · arXiv · VLM · Training-free
- **[Beyond Dominant Patches: Spatial Credit Redistribution For Grounded Vision-Language Models](https://arxiv.org/abs/2602.22469)** · arXiv · VLM · Training-free
- **[Dynamic Multimodal Activation Steering for Hallucination Mitigation in Large Vision-Language Models](https://arxiv.org/abs/2602.21704)** · arXiv · VLM · Training-free
- **[NoLan: Mitigating Object Hallucinations in Large Vision-Language Models via Dynamic Suppression of Language Priors](https://arxiv.org/abs/2602.22144)** · arXiv · VLM · Training-free
- **[See It, Say It, Sorted: An Iterative Training-Free Framework for Visually-Grounded Multimodal Reasoning in LVLMs](https://arxiv.org/abs/2602.21497)** · arXiv · VLM · Training-free
- **[Look Carefully: Adaptive Visual Reinforcements in Multimodal Large Language Models for Hallucination Mitigation](https://arxiv.org/abs/2602.24041)** · arXiv · VLM · Training-free
- **[CRoPS: A Training-Free Hallucination Mitigation Framework for Vision-Language Models](https://arxiv.org/abs/2601.00659)** · arXiv · VLM · Training-free
- **[DA-DPO: Cost-efficient Difficulty-aware Preference Optimization for Reducing MLLM Hallucinations](https://arxiv.org/abs/2601.00623)** · arXiv · VLM · Training-based
- **[Text-Guided Layer Fusion Mitigates Hallucination in Multimodal LLMs](https://arxiv.org/abs/2601.03100)** · arXiv · VLM · Training-free
- **[SDCD: Structure-Disrupted Contrastive Decoding for Mitigating Hallucinations in Large Vision-Language Models](https://arxiv.org/abs/2601.03500)** · arXiv · VLM · Training-free
- **[Vision-Language Introspection: Mitigating Overconfident Hallucinations in MLLMs via Interpretable Bi-Causal Steering](https://arxiv.org/abs/2601.05159)** · arXiv · VLM · Training-free
- **[VIB-Probe: Detecting and Mitigating Hallucinations in Vision-Language Models via Variational Information Bottleneck](https://arxiv.org/abs/2601.05547)** · arXiv · VLM · Training-free
- **[Seeing Right but Saying Wrong: Inter- and Intra-Layer Refinement in MLLMs without Training](https://arxiv.org/abs/2601.07359)** · arXiv · VLM · Training-free
- **[Where Does Vision Meet Language? Understanding and Refining Visual Fusion in MLLMs via Contrastive Attention](https://arxiv.org/abs/2601.08151)** · arXiv · VLM · Training-free
- **[Attention-space Contrastive Guidance for Efficient Hallucination Mitigation in LVLMs](https://arxiv.org/abs/2601.13707)** · arXiv · VLM · Training-free
- **[Hallucination Mitigating for Medical Report Generation](https://arxiv.org/abs/2601.15745)** · arXiv · VLM · Training-free
- **[Beyond Superficial Unlearning: Sharpness-Aware Robust Erasure of Hallucinations in Multimodal LLMs](https://arxiv.org/abs/2601.16527)** · arXiv · VLM · Training-based
- **[V-Loop: Visual Logical Loop Verification for Hallucination Detection in Medical Visual Question Answering](https://arxiv.org/abs/2601.18240)** · arXiv · VLM · Training-free
- **[Countering the Over-Reliance Trap: Mitigating Object Hallucination for LVLMs via a Self-Validation Framework](https://arxiv.org/abs/2601.22451)** · arXiv · VLM · Training-free
- **[A CNN-Based Framework for Addressing Hallucination Phenomena: Mitigating Limitations Across Multimodal and Clinical Contexts](https://doi.org/10.1007/978-3-032-14197-2_22)** · Other · VLM · Training-free
- **[A Context-Aware Hallucination Detection Framework for Large Language Models in High-Stakes Domains](https://doi.org/10.18535/ijecs/v15i06.5531)** · Other · LLM · Training-free
- **[A Hybrid Framework for Hallucination Detection in Large Language Models](https://doi.org/10.1109/tai.2026.3653354)** · Other · LLM · Training-free
- **[A Knowledge Graph Approach Towards Detecting Large Language Model Hallucination](https://doi.org/10.1007/978-3-032-08384-5_19)** · Other · LLM · Training-free
- **[A Multi-Metric Evaluation Perspective on Hallucination Detection in Low-Resource Governance Documents](https://doi.org/10.64388/irev9i11-1717980)** · Other · LLM · Training-free
- **[A Non-intrusive Plug-and-play Method for Hallucination Mitigation via LID-guided Input Preprocessing](https://doi.org/10.1007/s11633-025-1596-7)** · Other · LLM · Training-free
- **[A Real-Time Verification Framework for Hallucination and Bias Detection in AI Generated Text](https://doi.org/10.1109/icicv68925.2026.11554618)** · Other · LLM · Training-free
- **📚 [A Survey of Hallucination in Large Language Models](https://doi.org/10.12677/airr.2026.151016)** · Other · LLM · Training-free
- **📚 [A Taxonomy of Machine Hallucination in Radiology](https://doi.org/10.1148/ryai.250203)** · Other · LLM · Training-free
- **[Adaptive Hallucination Alleviation in Multimodal Large Language Models: From Strategic Data Selection to Severity-Guided Training](https://doi.org/10.1609/aaai.v40i32.39955)** · Other · VLM · Training-free
- **[Advancing LLM-Generated Code Reliability: A Hybrid Approach for Hallucination Detection](https://doi.org/10.1109/tse.2025.3640641)** · Other · LLM · Training-free
- **[Adversarial Abductive Dialogue Framework with Reinforcement for Tackling LLM Hallucination](https://doi.org/10.1007/978-3-032-16524-4_3)** · Other · LLM · Training-free
- **AFTER: Mitigating the Object Hallucination of LVLM via Adaptive Factual-Guided Activation Editing** · Unlabeled · VLM · Training-free
- **[Agentic Data Architecture (Ada): Eliminating The Api Layer For Hallucination-Free, Sub-100ms Enterprise AI Agents](https://doi.org/10.63363/aijfr.2026.v07i02.4079)** · Other · LLM · Training-free
- **[AHA: Aligning Large Audio-Language Models for Reasoning Hallucinations via Counterfactual Hard Negatives](https://aclanthology.org/2026.findings-acl.1464/)** · ACL · MLLM(Omni) · Training-free
- **[AI Hallucination Prediction: A Novel Approach for Preventing False AI Outputs](https://doi.org/10.1007/978-3-032-06688-6_48)** · Other · LLM · Training-free
- **[Aligning with Your Own Voice: Self-Corrected Preference Learning for Hallucination Mitigation in LVLMs](https://aclanthology.org/2026.findings-acl.1784/)** · ACL · VLM · Training-based
- **[Analisis Implementasi Artificial Intelligence dalam Audit Keuangan Atas Kasus Hallucination AI Deloitte Australia 2025](https://doi.org/10.31004/riggs.v5i2.9653)** · Other · LLM · Training-free
- **[Analog Hawking Radiation in Transformer Neural Networks: Discrete Geometric Horizons, Information Thermodynamics, and Hallucination Suppression](https://doi.org/10.33140/amlai.07.01.05)** · Other · LLM · Training-free
- **[Anatomical Region-Guided Contrastive Decoding: A Plug-and-Play Strategy for Mitigating Hallucinations in Medical VLMs](https://doi.org/10.1609/aaai.v40i9.37620)** · Other · VLM · Training-free
- **[Anchoring the Cache: Mitigating Contextual Hallucination in KV-Compressed Long-Context Summarization](https://aclanthology.org/2026.acl-long.1542/)** · ACL · LLM · Training-free
- **[Attention Reallocation: Towards Zero-cost and Controllable Hallucination Mitigation of MLLMs](https://doi.org/10.1007/s11263-025-02607-z)** · Other · VLM · Training-free
- **[Attribution-Guided Multi-Object Hallucination and Bias Detection in Vision-Language Models](https://doi.org/10.18653/v1/2026.eacl-long.210)** · Other · VLM · Training-free
- **📋 [AutoHall: Automated Factuality Hallucination Dataset Generation for Large Language Models](https://doi.org/10.1109/taslpro.2025.3635038)** · Other · LLM · Training-free
- **[Awakening Dormant Experts: Counterfactual Routing to Mitigate MoE Hallucinations](https://aclanthology.org/2026.acl-long.2187/)** · ACL · LLM · Training-free
- **[Being Kind Isn&apos;t Always Being Safe: Diagnosing Affective Hallucination in LLMs](https://doi.org/10.18653/v1/2026.findings-eacl.4)** · Other · LLM · Training-free
- **[Beware of the Woozle Effect: Exploring and Mitigating Hallucination Propagation in Multi-Agent Debate](https://doi.org/10.1109/taslpro.2026.3675803)** · Other · LLM · Training-free
- **[Beyond Next Token Probabilities: Learnable, Fast Detection of Hallucinations and Data Contamination on LLM Output Distributions](https://doi.org/10.1609/aaai.v40i36.40254)** · Other · LLM · Training-free
- **[Beyond Noise: Characterizing Creative Potential in Unverifiable LLM Hallucinations](https://aclanthology.org/2026.acl-long.554/)** · ACL · LLM · Training-free
- **[Beyond Output Confidence: Epistemic-Aware Hallucination Detection with Answer-Level Signals](https://aclanthology.org/2026.findings-acl.674/)** · ACL · LLM · Training-free
- **[Bolster Hallucination Detection via Prompt-Guided Data Augmentation](https://doi.org/10.1609/aaai.v40i44.41096)** · Other · LLM · Training-free
- **[Bridging Day and Night: Target-Class Hallucination Suppression in Unpaired Image Translation](https://doi.org/10.1609/aaai.v40i8.37570)** · Other · VLM · Training-free
- **[Calibrating Uncertainty with Cross-Model Consistency for LLM Hallucination Mitigation](https://doi.org/10.1145/3805712.3809846)** · Other · LLM · Training-free
- **[Cascaded Verification Framework: A Progressive Approach for Mitigating Hallucinations in Large Language Models](https://doi.org/10.1145/3774904.3792852)** · Other · LLM · Training-free
- **📋 [Causal-HalBench: Uncovering LVLMs Object Hallucinations Through Causal Intervention](https://doi.org/10.1609/aaai.v40i40.40712)** · Other · VLM · Training-free
- **[CausalGaze: Unveiling Hallucinations via Counterfactual Graph Intervention in Large Language Models](https://aclanthology.org/2026.findings-acl.1943/)** · ACL · LLM · Training-free
- **[CCD: Mitigating Hallucinations in Radiology MLLMs via Clinical Contrastive Decoding](https://aclanthology.org/2026.findings-acl.1755/)** · ACL · VLM · Training-free
- **[CEBC: Conformal Evidence-Bounded Control for Low-Hallucination Vision-Language Generation](https://aclanthology.org/2026.acl-long.2142/)** · ACL · VLM · Training-free
- **[CoDA: Restoring Contextual Dominance via Copy-Encouraged Attention Intervention for Mitigating RAG Hallucinations](https://aclanthology.org/2026.findings-acl.576/)** · ACL · LLM · Training-free
- **[Collaborated With Hallucination: Enhancing Egocentric Grounded Question Answering via Error Demonstrations](https://doi.org/10.1109/tip.2026.3666732)** · Other · LLM · Training-free
- **[Comprehensive to the Textual Hallucination in Generative AI](https://doi.org/10.2991/978-94-6239-648-7_37)** · Other · LLM · Training-free
- **[Constrained Paraphrase Consistency for LLM Hallucination Detection](https://doi.org/10.1109/icassp55912.2026.11462617)** · Other · LLM · Training-free
- **📋 [Constructing a Dataset for Hallucination Detection in Japanese Summarization with Fine-grained Faithfulness Labels](https://doi.org/10.18653/v1/2026.eacl-srw.15)** · Other · LLM · Training-free
- **Copy-Paste to Mitigate Large Language Model Hallucinations** · Unlabeled · LLM · Training-free
- **[Cross Paraphrastic Invariance Learning for Hallucination Detection](https://doi.org/10.1109/icassp55912.2026.11463868)** · Other · LLM · Training-free
- **[Cross-model diffusion: Mitigating hallucination in large language models for rumor detection](https://doi.org/10.1016/j.neunet.2026.109226)** · Other · LLM · Training-free
- **[CSMAD: Hallucination Detection via Multi-Agent Debate with NLI-Verified Contradictory Statements](https://doi.org/10.1145/3805712.3808508)** · Other · LLM · Training-free
- **[CVSTIM: Mitigating Object Hallucination in Mllms Via Co-Occurrence Guided Visual Stimulation](https://doi.org/10.1109/icassp55912.2026.11464584)** · Other · VLM · Training-free
- **[Data Leakage and Model Hallucination](https://doi.org/10.1002/9781394402069.ch10)** · Other · LLM · Training-free
- **[Dehallu3D: Hallucination-Mitigated 3D Generation from a Single Image via Cyclic View Consistency Refinement](https://openaccess.thecvf.com/content/CVPR2026/html/Wang_Dehallu3D_Hallucination-Mitigated_3D_Generation_from_a_Single_Image_via_Cyclic_CVPR_2026_paper.html)** · Unlabeled · VLM · Training-free
- **[Detecting Citation Hallucinations in Large Language Model Outputs (Student Abstract)](https://doi.org/10.1609/aaai.v40i48.42257)** · Other · LLM · Training-free
- **[Detecting Hallucinations in Retrieval-Augmented Generation via Semantic-level Internal Reasoning Graph](https://aclanthology.org/2026.findings-acl.1385/)** · ACL · LLM · Training-free
- **[Detecting Hallucinations in SpeechLLMs at Inference Time Using Attention Maps](https://aclanthology.org/2026.findings-acl.2147/)** · ACL · LLM · Training-free
- **[Detectra-AI Response Hallucination Detector](https://doi.org/10.62226/ijarst20262726)** · Other · LLM · Training-free
- **📋 [DHEval: A Dynamic Hallucination Evaluation Protocol Robust to Data Contamination](https://doi.org/10.1109/icassp55912.2026.11462032)** · Other · LLM · Training-free
- **[DHI: Leveraging Diverse Hallucination Induction for Enhanced Contrastive Factuality Control in Large Language Models](https://doi.org/10.1007/978-981-95-4088-4_15)** · Other · LLM · Training-free
- **[Dialectic-Med: Mitigating Diagnostic Hallucinations via Counterfactual Adversarial Multi-Agent Debate](https://aclanthology.org/2026.findings-acl.1837/)** · ACL · LLM · Training-free
- **[Diffusion for Combating the Hallucination in Large Language Models (Student Abstract)](https://doi.org/10.1609/aaai.v40i48.42183)** · Other · LLM · Training-free
- **[Do LLM hallucination detectors suffer from low-resource effect?](https://doi.org/10.18653/v1/2026.eacl-long.136)** · Other · LLM · Training-free
- **[Dr.V : A Hierarchical Perception-Temporal-Cognition Framework to Diagnose Video Hallucination by Fine-Grained Spatial-Temporal Grounding](https://doi.org/10.1007/s11263-026-02831-1)** · Other · VLM · Training-free
- **[Dynamic PMI-Guided Contrastive Decoding Reduces Hallucination in Large Language Models: A Unified Framework of Fine-Grained Input Transformations](https://aclanthology.org/2026.findings-acl.1212/)** · ACL · LLM · Training-free
- **[ECD: Efficient Contrastive Decoding with Probabilistic Hallucination Detection](https://doi.org/10.1007/978-3-032-06109-6_2)** · Other · LLM · Training-free
- **[EchoBat: Echo-Vision Enhancement and Echo-Layered Sampling for Video LLMs Hallucination Mitigation](https://doi.org/10.1609/aaai.v40i42.40875)** · Other · VLM · Training-free
- **[Efficient Hallucination Detection in Automatic Code Generation](https://aclanthology.org/2026.findings-acl.2143/)** · ACL · LLM · Training-free
- **[Efficient Hallucination Detection: Adaptive Bayesian Estimation of Semantic Entropy with Guided Semantic Exploration](https://doi.org/10.1609/aaai.v40i39.40595)** · Other · LLM · Training-free
- **[Enhancing Factual Consistency in Large Language Models: An Integrative Paradigm of Grounding and Self-Prompting Methods for Hallucination Minimization](https://doi.org/10.1007/978-981-96-9771-7_13)** · Other · LLM · Training-free
- **[Enhancing Hallucination Detection via Future Context](https://aclanthology.org/2026.findings-acl.35/)** · ACL · LLM · Training-free
- **[Eroding the Truth-Default: A Causal Analysis of Human Susceptibility to Foundation Model Hallucinations and Disinformation in the Wild](https://doi.org/10.1145/3774905.3795832)** · Other · LLM · Training-free
- **📋 [ESG-Bench: Benchmarking Long-Context ESG Reports for Hallucination Mitigation](https://doi.org/10.1609/aaai.v40i46.41281)** · Other · LLM · Training-based
- **[Evidence-Aligned Entity Verification for Hallucination Detection in Retrieval-Augmented Generation](https://aclanthology.org/2026.findings-acl.1477/)** · ACL · LLM · Training-free
- **[Exploring Audio Hallucination in Egocentric Video Understanding](https://doi.org/10.1109/icassp55912.2026.11460380)** · Other · MLLM(Omni) · Training-free
- **[Exposing and Evaluating Hallucinations for GUI Grounding](https://openaccess.thecvf.com/content/CVPR2026/html/Zhang_Exposing_and_Evaluating_Hallucinations_for_GUI_Grounding_CVPR_2026_paper.html)** · Unlabeled · LLM · Training-free
- **[FactSelfCheck: Fact-Level Black-Box Hallucination Detection for LLMs](https://doi.org/10.18653/v1/2026.findings-eacl.296)** · Other · LLM · Training-free
- **[FaithLens: Detecting and Explaining Faithfulness Hallucination](https://aclanthology.org/2026.findings-acl.689/)** · ACL · LLM · Training-free
- **📋 [FFE-Hallu: Hallucinations in Fixed Figurative Expressions: A Benchmark of Idioms and Proverbs in the Persian Language](https://doi.org/10.18653/v1/2026.eacl-long.241)** · Other · LLM · Training-free
- **[Fine-Grained Detection of Context-Grounded Hallucinations Using LLMs](https://aclanthology.org/2026.findings-acl.1907/)** · ACL · LLM · Training-free
- **[FINER: MLLMs Hallucinate under Fine-grained Negative Queries](https://openaccess.thecvf.com/content/CVPR2026/html/Xiao_FINER_MLLMs_Hallucinate_under_Fine-grained_Negative_Queries_CVPR_2026_paper.html)** · Unlabeled · VLM · Training-free
- **[From Detection to Diagnosis: Advancing Hallucination Analysis with Automated Data Synthesis](https://doi.org/10.1609/aaai.v40i38.40495)** · Other · LLM · Training-free
- **[From Hallucination to Articulation: Language Model-Driven Losses for Ultra Low-Bitrate Neural Speech Coding](https://doi.org/10.1109/icassp55912.2026.11462750)** · Other · MLLM(Omni) · Training-free
- **[From Proof to Program: Characterizing Tool-Induced Reasoning Hallucinations in Large Language Models](https://aclanthology.org/2026.acl-long.1951/)** · ACL · LLM · Training-based
- **[Generating Effective CoT Traces for Mitigating Causal Hallucination](https://aclanthology.org/2026.findings-acl.264/)** · ACL · LLM · Training-free
- **📋 [GHOST: Getting to the Bottom of Hallucinations with A Multi-round Consistency Benchmark](https://doi.org/10.1109/WACV61042.2026.00596)** · Other · LLM · Training-free
- **[Global-Local Confidence Fusion for Hallucination Detection in Mathematical Reasoning Task](https://doi.org/10.1609/aaai.v40i41.40762)** · Other · LLM · Training-based
- **[GraphHall: A Graph-Based Framework for Hallucination Detection in Large Language Models](https://doi.org/10.1109/tai.2026.3715425)** · Other · LLM · Training-free
- **[Ground What You See: Hallucination-Resistant MLLMs via Caption Feedback, Diversity-Aware Sampling, and Conflict Regularization](https://doi.org/10.1609/aaai.v40i10.37772)** · Other · VLM · Training-free
- **📋 [HalluAudio: A Comprehensive Benchmark for Hallucination Detection in Large Audio-Language Models](https://aclanthology.org/2026.acl-long.1797/)** · ACL · MLLM(Omni) · Training-free
- **[Hallucination as a Computational Boundary: A Hierarchy of Inevitability and the Oracle Escape](https://doi.org/10.1609/aaai.v40i40.40657)** · Other · LLM · Training-free
- **Hallucination Begins Where Saliency Drops** · Unlabeled · LLM · Training-free
- **[Hallucination Detection and Mitigation in Large Language Models Using Lightweight Inference-Time Models](https://doi.org/10.55248/gengpi.07.0426.c1028)** · Other · LLM · Training-free
- **[Hallucination Detection in Large Language Models using Self Consistency Signals](https://doi.org/10.1109/iccnct68477.2026.11590608)** · Other · LLM · Training-free
- **[Hallucination Detection in Large Language Models via Multi-Granular Uncertainty Quantification](https://doi.org/10.59543/comdem.v3i.17665)** · Other · LLM · Training-free
- **[Hallucination Detection in LLMs with Topological Divergence on Attention Graphs](https://aclanthology.org/2026.acl-long.704/)** · ACL · LLM · Training-free
- **📋 [Hallucination Detection in Long-Form Text Generated by LLMs: A Benchmark and a Hyper-Relational Knowledge Graph Approach](https://aclanthology.org/2026.findings-acl.1673/)** · ACL · LLM · Training-free
- **[Hallucination Detection Via Internal States and Structured Reasoning Consistency in Large Language Models](https://doi.org/10.1109/icassp55912.2026.11462457)** · Other · LLM · Training-free
- **[Hallucination Detection, Categorization, and Mitigation in Large Language Models: A Cross-Domain Evaluation Framework](https://doi.org/10.64388/irev9i10-1716821)** · Other · LLM · Training-free
- **[Hallucination Early Detection in Diffusion Models](https://doi.org/10.1007/s11263-025-02622-0)** · Other · LLM · Training-free
- **[Hallucination Elimination and Text Annotation Framework for Large Vision-Language Models in Traffic Scenarios](https://doi.org/10.1109/tits.2025.3625700)** · Other · VLM · Training-free
- **[Hallucination Mitigation for EEG-to-Text Generation via Multi-Source Semantic Augmentation and Latent Space Regularization](https://doi.org/10.1109/icsipc69751.2026.11584213)** · Other · LLM · Training-free
- **[Hallucination Mitigation with Agentic AI NLP-Based Open-Floor Standard](https://doi.org/10.5220/0013761000004052)** · Other · LLM · Training-free
- **[Hallucination to Consensus: Multi-Agent LLMs for End-to-End JUnit Test Generation](https://doi.org/10.1145/3803418)** · Other · LLM · Training-free
- **📚 [Hallucination to truth: a review of fact-checking and factuality evaluation in large language models](https://doi.org/10.1007/s10462-025-11454-w)** · Other · LLM · Training-free
- **[Hallucinations as Orthogonal Noise: Inference-Time Manifold Alignment via Dynamic Contextual Orthogonalization](https://aclanthology.org/2026.findings-acl.1822/)** · ACL · LLM · Training-free
- **[Hallucinations at the Firewall](https://doi.org/10.1609/aaai.v40i48.42311)** · Other · LLM · Training-free
- **[HalluClean: A Unified Framework to Combat Hallucinations in LLMs](https://doi.org/10.1609/aaai.v40i42.40926)** · Other · LLM · Training-free
- **[HalluGuard: Evidence-Grounded Small Reasoning Models to Mitigate Hallucinations in Retrieval-Augmented Generation](https://aclanthology.org/2026.findings-acl.835/)** · ACL · LLM · Training-free
- **[HalluZig: Hallucination Detection using Zigzag Persistence](https://doi.org/10.18653/v1/2026.eacl-long.159)** · Other · LLM · Training-free
- **[HALP: Detecting Hallucinations in Vision-Language Models without Generating a Single Token](https://doi.org/10.18653/v1/2026.eacl-long.287)** · Other · VLM · Training-free
- **[HAT: Hallucination Annotation for Translation](https://aclanthology.org/2026.acl-long.721/)** · ACL · LLM · Training-free
- **[Heaven-Sent or Hell-Bent? Benchmarking the Intelligence and Defectiveness of LLM Hallucinations](https://doi.org/10.1145/3770854.3785704)** · Other · LLM · Training-free
- **📚 [House of Mirrors: A Survey on Hallucination Detection and Mitigation via Decoding Techniques in Language Models](https://doi.org/10.1007/978-3-032-03072-6_9)** · Other · LLM · Training-free
- **[How Human Experts Educate Specialized LLMs: Filling Knowledge Gaps in KG-Augmented Generation through Hallucination Detection](https://doi.org/10.1145/3774904.3792550)** · Other · LLM · Training-free
- **[HyGen—A Hybrid Automation Testing Approach for Reducing Hallucination in LLM-Based Applications](https://doi.org/10.1007/978-981-96-6537-2_2)** · Other · LLM · Training-free
- **[Joint Evaluation of Answer and Reasoning Consistency for Hallucination Detection in Large Reasoning Models](https://doi.org/10.1609/aaai.v40i39.40624)** · Other · LLM · Training-free
- **[JointCQ: Improving Factual Hallucination Detection with Joint Claim and Query Generation](https://aclanthology.org/2026.findings-acl.58/)** · ACL · LLM · Training-free
- **📋 [KGHaluBench: A Knowledge Graph-Based Hallucination Benchmark for Evaluating the Breadth and Depth of LLM Knowledge](https://doi.org/10.18653/v1/2026.findings-eacl.206)** · Other · LLM · Training-free
- **[Knowledge Injection Exists in MoE? Exploring Expert-Aware Contrast Decoding in MoE for Mitigating LLMs&apos; Hallucinations](https://aclanthology.org/2026.acl-long.1824/)** · ACL · LLM · Training-free
- **[LAFaCT: Attribution-based Localization and Focused Sequential Analysis of Fact-Critical Tokens for Hallucination Detection](https://aclanthology.org/2026.acl-long.312/)** · ACL · LLM · Training-free
- **📚 [Large language models hallucination: A comprehensive survey](https://doi.org/10.1016/j.cosrev.2026.100970)** · Other · LLM · Training-free
- **[Lawsuit AraRAG: A Retrieval-Augmented Generation Framework for Arabic Legal Document Understanding and Hallucination Reduction](https://doi.org/10.1109/lt68265.2026.11592520)** · Other · LLM · Training-free
- **[Lie to Me: Knowledge Graphs for Robust Hallucination Self-Detection in LLMs](https://doi.org/10.5220/0014245100004067)** · Other · LLM · Training-free
- **[Listen like a Teacher: Mitigating Whisper Hallucinations Using Adaptive Layer Attention and Knowledge Distillation](https://doi.org/10.1609/aaai.v40i39.40614)** · Other · LLM · Training-free
- **[LLM-CAS: Dynamic Neuron Perturbation for Real-Time Hallucination Correction](https://doi.org/10.1609/aaai.v40i41.40776)** · Other · LLM · Training-free
- **[Logic Matters in Lightweight Hallucination Classification for RAG System](https://aclanthology.org/2026.acl-long.73/)** · ACL · LLM · Training-free
- **[Logical Consistency as a Bridge: Improving LLM Hallucination Detection via Label Constraint Modeling between Responses and Self-Judgments](https://aclanthology.org/2026.acl-long.286/)** · ACL · LLM · Training-free
- **📚 [Loki’s Dance of Illusions: A Comprehensive Survey of Hallucination in Large Language Models](https://doi.org/10.1109/tcss.2026.3661295)** · Other · LLM · Training-free
- **[Look Closer! An Adversarial Parametric Editing Framework for Hallucination Mitigation in VLMs](https://doi.org/10.1609/aaai.v40i26.39336)** · Other · VLM · Training-based
- **[Lost in Diffusion: Uncovering Hallucination Patterns and Failure Modes in Diffusion Large Language Models](https://aclanthology.org/2026.findings-acl.882/)** · ACL · LLM · Training-free
- **[MARCH: Multi-Agent Reinforced Check for Hallucination](https://aclanthology.org/2026.acl-long.1828/)** · ACL · LLM · Training-free
- **[MeasHalu: Mitigation of Scientific Measurement Hallucinations for Large Language Models with Enhanced Reasoning](https://aclanthology.org/2026.findings-acl.1386/)** · ACL · LLM · Training-free
- **[Mechanisms of Prompt-Induced Hallucination in Vision-Language Models](https://aclanthology.org/2026.acl-long.1941/)** · ACL · VLM · Training-free
- **📋 [MHB: Medical Hallucination Benchmark for Large Language Models in Complex Clinical Tasks](https://doi.org/10.1609/aaai.v40i45.41243)** · Other · LLM · Training-free
- **[Mitigating Entity Hallucinations in 3D Radiology Report Generation via Dual-Stream Alignment](https://doi.org/10.1609/aaai.v40i16.38379)** · Other · LLM · Training-free
- **[Mitigating Hallucination in Financial Retrieval-Augmented Generation Via Fine-Grained Knowledge Verification](https://doi.org/10.1109/icassp55912.2026.11464516)** · Other · LLM · Training-free
- **[Mitigating Hallucination in Multimodal Information Systems: A Comparative Analysis of Modular LLM Architectures](https://doi.org/10.1109/tcss.2026.3691181)** · Other · VLM · Training-free
- **[Mitigating hallucination in Multimodal Large Language Models via cross-layer visual anchors](https://doi.org/10.1016/j.patcog.2026.114380)** · Other · VLM · Training-free
- **[Mitigating Hallucination on Hallucination in RAG via Ensemble Voting](https://doi.org/10.1109/cscwd68734.2026.11582530)** · Other · LLM · Training-free
- **[Mitigating Hallucinations in Large Language Models via Causal Reasoning](https://doi.org/10.1609/aaai.v40i38.40454)** · Other · LLM · Training-free
- **[Mitigating Legal Hallucinations via Symbolic Constraints and Analogical Precedents](https://aclanthology.org/2026.acl-long.633/)** · ACL · LLM · Training-free
- **[Mitigating LLM Hallucination Snowballing in Multiagent Systems via Context-Aware Semantic Consistency Reasoning](https://doi.org/10.1109/tnnls.2026.3655508)** · Other · LLM · Training-free
- **[Mitigating Multimodal Hallucination Through Effective and Perception-Aware Granularity Alignment](https://doi.org/10.1109/taslpro.2026.3703183)** · Other · VLM · Training-free
- **[Mitigating Object and Action Hallucinations in Multimodal LLMs via Self-Augmented Contrastive Alignment](https://doi.org/10.1109/WACV61042.2026.00310)** · Other · VLM · Training-free
- **[Mitigating Object and Relationship Hallucination in Large Vision Language Model with Multi-Agent Guidance](https://ieeexplore.ieee.org/document/11463505/)** · Unlabeled · VLM · Training-free
- **[Mitigating Visual Hallucination in Multimodal Event Extraction via Constrained Prompting](https://doi.org/10.3233/atde260397)** · Other · VLM · Training-free
- **📚 [Model stability and hallucination under the data-knowledge dual-drive paradigm: a survey](https://doi.org/10.1117/12.3110427)** · Other · LLM · Training-free
- **[Multi-Agent Brainstorming for Interpreting and Mitigating Hallucination in Multimodal-LLM](https://doi.org/10.1109/icassp55912.2026.11464937)** · Other · VLM · Training-free
- **[Multi-Agent Undercover Gaming: Hallucination Removal Through Counterfactual Test for Multimodal Reasoning](https://doi.org/10.1609/aaai.v40i8.37613)** · Other · VLM · Training-free
- **📋 [Multi-Hall-SA: A Cross-lingual Benchmark for Multi-Type Hallucination Detection in Low-Resource South African Languages](https://doi.org/10.18653/v1/2026.findings-eacl.330)** · Other · LLM · Training-free
- **[MVRL: A Multi-stage Training Framework for Value Alignment and Hallucination Suppression in Large Language Models](https://doi.org/10.1109/prmvai70103.2026.11605527)** · Other · LLM · Training-based
- **[NewsLensAI: NER-Guided Summarization for Mitigating Hallucination and Bias in LLM-Based News Summaries (Student Abstract)](https://doi.org/10.1609/aaai.v40i48.42250)** · Other · LLM · Training-free
- **[Numerical Hallucinations in Retrieval-Augmented Generation: Detection and Analysis](https://doi.org/10.1145/3805712.3809882)** · Other · LLM · Training-free
- **[OmniDPO: A Preference Optimization Framework to Address Omni-Modal Hallucination](https://doi.org/10.1609/aaai.v40i24.39104)** · Other · MLLM(Omni) · Training-based
- **[Optimizing LVLMs with On-Policy Data for Effective Hallucination Mitigation](https://doi.org/10.1109/WACV61042.2026.00460)** · Other · VLM · Training-free
- **[ORSc: Object-Aware Reinforcement with Semantic Consistency for Hallucination Mitigation in MLLMs](https://ieeexplore.ieee.org/document/11464193/)** · Unlabeled · VLM · Training-free
- **[PASE: Leveraging the Phonological Prior of WavLM for Low-Hallucination Generative Speech Enhancement](https://doi.org/10.1609/aaai.v40i39.40562)** · Other · MLLM(Omni) · Training-free
- **[PHPFND: Detecting Fake News via Post-Hoc Processing of LLMs Hallucination](https://doi.org/10.1609/aaai.v40i1.37050)** · Other · LLM · Training-free
- **[PretrainRL: Alleviating Factuality Hallucination of Large Language Models at the Beginning](https://aclanthology.org/2026.findings-acl.910/)** · ACL · LLM · Training-based
- **[Principled Detection of Hallucinations in Large Language Models via Multiple Testing](https://aclanthology.org/2026.findings-acl.1705/)** · ACL · LLM · Training-free
- **[PRISM: Probing Reasoning, Instruction, and Source Memory in LLM Hallucinations](https://aclanthology.org/2026.acl-long.1551/)** · ACL · LLM · Training-free
- **📋 [PROBE: PROcess-Based BEnchmark for Hallucination Detection](https://aclanthology.org/2026.findings-acl.2099/)** · ACL · LLM · Training-free
- **[ProgRAG: Hallucination-Resistant Progressive Retrieval and Reasoning over Knowledge Graphs](https://doi.org/10.1609/aaai.v40i39.40545)** · Other · LLM · Training-free
- **[PromptFishing: Active Hallucination Inducement to Distinguish LLMs From Humans](https://doi.org/10.1109/tifs.2026.3709099)** · Other · LLM · Training-free
- **[Quantifying Factual Divergence in Generative Models: SHAP-LIME Based Hallucination Score for LLMs](https://doi.org/10.1007/s00530-025-02150-4)** · Other · LLM · Training-free
- **[Rapid End-to-End Test Generation and Hallucination Mitigation Using Generative Artificial Intelligence](https://doi.org/10.1109/access.2026.3657407)** · Other · LLM · Training-free
- **[Reallocating Attention Across Layers to Reduce Multimodal Hallucination](https://openaccess.thecvf.com/content/CVPR2026/html/Lu_Reallocating_Attention_Across_Layers_to_Reduce_Multimodal_Hallucination_CVPR_2026_paper.html)** · Unlabeled · VLM · Training-free
- **[Reasoning&apos;s Razor: Reasoning Improves Accuracy but Hurts Recall at Critical Operating Points in Safety and Hallucination Detection](https://doi.org/10.18653/v1/2026.eacl-long.190)** · Other · LLM · Training-free
- **[Reducing Hallucinations in Language Model-based SPARQL Query Generation Using Post-Generation Memory Retrieval](https://doi.org/10.18653/v1/2026.findings-eacl.243)** · Other · LLM · Training-free
- **[Reducing Hallucinations in LLMs via Factuality-Aware Preference Learning](https://aclanthology.org/2026.findings-acl.1968/)** · ACL · LLM · Training-based
- **[ReFL: Reflective Feedback Learning for Hallucination Detection of Large Language Models](https://aclanthology.org/2026.acl-long.899/)** · ACL · LLM · Training-free
- **[ReGA: Zero-Overhead Graph Alignment for Structural Hallucination Detection Without Generation](https://doi.org/10.1145/3774905.3794657)** · Other · LLM · Training-free
- **📋 [Rethinking Evaluation for LLM Hallucination Detection: A Desiderata, A New RAG-based Benchmark, New Insights](https://aclanthology.org/2026.acl-long.680/)** · ACL · LLM · Training-free
- **[Rethinking Hallucinations: Correctness, Consistency, and Prompt Multiplicity](https://doi.org/10.18653/v1/2026.eacl-long.327)** · Other · LLM · Training-free
- **[Re³: Relevance &amp; Recency Retrieval for Mitigating Temporal Hallucination](https://aclanthology.org/2026.acl-long.1180/)** · ACL · LLM · Training-free
- **[RFI: Rectified Flow Intervention for Mitigating Object Hallucination in Large Vision-Language Models](https://doi.org/10.1609/aaai.v40i5.37320)** · Other · VLM · Training-free
- **[RFS-Guard: Detecting Reasoning Hallucinations via Cross-Phase Routing Focus in Large Reasoning Models](https://aclanthology.org/2026.acl-long.885/)** · ACL · LLM · Training-free
- **[RLSeek: Evidence-Grounded Reasoning for RAG Hallucination Detection](https://aclanthology.org/2026.acl-long.1492/)** · ACL · LLM · Training-free
- **[RusHallu-RAG: benchmarking hallucination detection for Russian RAG](https://doi.org/10.29003/2075-7182-2026-24-516-534)** · Other · LLM · Training-free
- **[SeaRAG: Reducing Hallucination in Retrieval-Augmented Generation via Statement-Entity Adaptive Ranking](https://doi.org/10.1145/3774904.3792598)** · Other · LLM · Training-free
- **[Seeing Is Believing: Rich-Context Hallucination Detection for MLLMs via Backward Visual Grounding](https://doi.org/10.1609/aaai.v40i37.40345)** · Other · VLM · Training-free
- **[Semantic Reformulation Entropy for Robust Hallucination Detection in QA Tasks](https://doi.org/10.1109/icassp55912.2026.11460452)** · Other · LLM · Training-free
- **[SEVADE: Self-Evolving Multi-Agent Analysis with Decoupled Evaluation for Hallucination-Resistant Sarcasm Detection](https://doi.org/10.1609/aaai.v40i35.40200)** · Other · LLM · Training-free
- **[Shadows in the Attention: Contextual Perturbation and Representation Drift in the Dynamics of Hallucination in LLMs](https://doi.org/10.1007/978-981-95-4088-4_32)** · Other · LLM · Training-free
- **[Slopsquatting and package-hallucination in LLMS](https://doi.org/10.64643/ijirtv12i7-191660-459)** · Other · LLM · Training-free
- **[SmartSight: Mitigating Hallucination in Video-LLMs Without Compromising Video Understanding via Temporal Attention Collapse](https://doi.org/10.1609/aaai.v40i11.37883)** · Other · VLM · Training-free
- **[Stable-RAG: Mitigating Retrieval-Permutation-Induced Hallucinations in Retrieval-Augmented Generation](https://aclanthology.org/2026.acl-long.1188/)** · ACL · LLM · Training-free
- **[Streaming Hallucination Detection in Long Chain-of-Thought Reasoning](https://aclanthology.org/2026.findings-acl.1064/)** · ACL · LLM · Training-free
- **📚 [Survey on Hallucination in Reasoning Large Language Model: Evaluation, Taxonomy, Intervention, and Open Issues](https://doi.org/10.3724/2096-7004.di.2025.0131)** · Other · LLM · Training-free
- **[Synonym Knowledge Graph Enhanced Language Model for Inconsistent Hallucination Detection](https://doi.org/10.1145/3819585)** · Other · LLM · Training-free
- **[Taming Object Hallucinations with Verified Atomic Confidence Estimation](https://doi.org/10.18653/v1/2026.eacl-long.252)** · Other · LLM · Training-free
- **[Taming the Phantom: Token-Asymmetric Filtering for Hallucination Mitigation in Large Vision-Language Models](https://doi.org/10.1609/aaai.v40i10.37768)** · Other · VLM · Training-free
- **📋 [TempHalluc-Bench: Evaluating Temporal Hallucination in VideoLLM-Based Video Search and Information Extraction](https://doi.org/10.5120/ijca-1aef39d4b120)** · Other · VLM · Training-free
- **[The Digital Dunning-Kruger Effect: Decoupling Hallucinations via Geometric Hidden-state Observation for Semantic Truthfulness](https://aclanthology.org/2026.acl-long.993/)** · ACL · LLM · Training-free
- **[The Double-Lock Framework: A Multi-Layered System for Grounded Retrieval-Augmented Generation and Hallucination Mitigation](https://doi.org/10.6025/ijclr/2026/17/2/100-126)** · Other · LLM · Training-free
- **[The Immutable Hallucination: A Critical Analysis of AI-Blockchain Integration in Healthcare](https://doi.org/10.5220/0015138500005051)** · Other · LLM · Training-free
- **[The Reasoning Trap: How Enhancing LLM Reasoning Amplifies Tool Hallucination](https://aclanthology.org/2026.acl-long.376/)** · ACL · LLM · Training-free
- **[The Unintended Trade-off of AI Alignment: Balancing Hallucination Mitigation and Safety in LLMs](https://doi.org/10.18653/v1/2026.findings-eacl.53)** · Other · LLM · Training-free
- **[The Virtue of Hallucination: When AI Mistakes Make Software Safer](https://doi.org/10.1109/mc.2026.3659286)** · Other · LLM · Training-free
- **Token-Guard: Towards Token-Level Hallucination Control via Self-Checking Decoding** · Unlabeled · LLM · Training-free
- **[Towards Mitigating Hallucinations in Large Vision-Language Models by Refining Textual Embeddings](https://aclanthology.org/2026.findings-acl.2086/)** · ACL · VLM · Training-free
- **[TPA: Next Token Probability Attribution for Detecting Hallucinations in RAG](https://aclanthology.org/2026.acl-long.1159/)** · ACL · LLM · Training-free
- **[Trustworthiness, Hallucination, and Evaluation in Large Language Models](https://doi.org/10.56975/ijcrt.v14i4.307430)** · Other · LLM · Training-free
- **[Two Pathways to Truthfulness: On the Intrinsic Encoding of LLM Hallucinations](https://aclanthology.org/2026.acl-long.1173/)** · ACL · LLM · Training-free
- **[Understanding New-Knowledge-Induced Factual Hallucinations in LLMs: Analysis and Interpretation](https://aclanthology.org/2026.findings-acl.358/)** · ACL · LLM · Training-free
- **[VCGD: Visual Clue Guided Decoding with Caption Model for Mitigating Hallucination in Multimodal Large Language Models](https://doi.org/10.1609/aaai.v40i24.39089)** · Other · VLM · Training-free
- **[VDIS: Combating Object Hallucination in Multimodal Large Language Models](https://doi.org/10.1007/978-981-95-5696-0_28)** · Other · VLM · Training-free
- **[VES-RFT: Rewarding Visual Evidence Sensitivity to Mitigate Hallucinations in Large Vision-Language Models](https://openaccess.thecvf.com/content/CVPR2026/html/Hou_VES-RFT_Rewarding_Visual_Evidence_Sensitivity_to_Mitigate_Hallucinations_in_Large_CVPR_2026_paper.html)** · Unlabeled · VLM · Training-free
- **[VGL-DPO: Vision-Guided Lexical Direct Preference Optimization for Mitigating Hallucination in Multimodal Large Language Models](https://doi.org/10.1145/3796715)** · Other · VLM · Training-based
- **Visual Multi-Agent System: Mitigating Hallucination Snowballing via Visual Flow** · Unlabeled · VLM · Training-free
- **[When Personalization Misleads: Understanding and Mitigating Hallucinations in Personalized LLMs](https://aclanthology.org/2026.findings-acl.395/)** · ACL · LLM · Training-free
- **[Why Language Model Reasoning Systematically Fails: A Structural Definition of Hallucination Based on Coordinate Closure](https://doi.org/10.1109/access.2026.3707249)** · Other · LLM · Training-free

</details>

<details>
<summary>📅 2025 · 397 papers</summary>

- **[Med-VCD: Mitigating Hallucination for Medical Large Vision Language Models through Visual Contrastive Decoding](https://arxiv.org/abs/2512.01922)** · arXiv · VLM · Training-free
- **[InEx: Hallucination Mitigation via Introspection and Cross-Modal Multi-Agent Collaboration](https://arxiv.org/abs/2512.02981)** · arXiv · VLM · Training-free
- **[V-ITI: Mitigating Hallucinations in Multimodal Large Language Models via Visual Inference-Time Intervention](https://arxiv.org/abs/2512.03542)** · arXiv · VLM · Training-free
- **[Conscious Gaze: Adaptive Attention Mechanisms for Hallucination Mitigation in Vision-Language Models](https://arxiv.org/abs/2512.05546)** · arXiv · VLM · Training-free
- **[HalluShift++: Bridging Language and Vision through Internal Representation Shifts for Hierarchical Hallucinations in MLLMs](https://arxiv.org/abs/2512.07687)** · arXiv · VLM · Training-free
- **[SAVE: Sparse Autoencoder-Driven Visual Information Enhancement for Mitigating Object Hallucination](https://arxiv.org/abs/2512.07730)** · arXiv · VLM · Training-free
- **[VEGAS: Mitigating Hallucinations in Large Vision-Language Models via Vision-Encoder Attention Guided Adaptive Steering](https://arxiv.org/abs/2512.12089)** · arXiv · VLM · Training-free
- **[Revealing Perception and Generation Dynamics in LVLMs: Mitigating Hallucinations via Validated Dominance Correction](https://arxiv.org/abs/2512.18813)** · arXiv · VLM · Training-free
- **[Watch Closely: Mitigating Object Hallucinations in Large Vision-Language Models with Disentangled Decoding](https://arxiv.org/abs/2512.19070)** · arXiv · VLM · Training-free
- **[CoFi-Dec: Hallucination-Resistant Decoding via Coarse-to-Fine Generative Feedback in Large Vision-Language Models](https://arxiv.org/abs/2512.23453)** · arXiv · VLM · Training-free
- **[Taming Hallucinations: Boosting MLLMs' Video Understanding via Counterfactual Video Generation](https://arxiv.org/abs/2512.24271)** · arXiv · VLM · Training-based
- **[Causal Tracing of Object Representations in Large Vision Language Models: Mechanistic Interpretability and Hallucination Mitigation](https://arxiv.org/abs/2511.05923)** · arXiv · VLM · Training-free
- **[Causally-Grounded Dual-Path Attention Intervention for Object Hallucination Mitigation in LVLMs](https://arxiv.org/abs/2511.09018)** · arXiv · VLM · Training-free
- **[Adaptive Residual-Update Steering for Low-Overhead Hallucination Mitigation in Large Vision Language Models](https://arxiv.org/abs/2511.10292)** · arXiv · VLM · Training-free
- **[PAS : Prelim Attention Score for Detecting Object Hallucinations in Large Vision--Language Models](https://arxiv.org/abs/2511.11502)** · arXiv · VLM · Training-free
- **[Suppressing VLM Hallucinations with Spectral Representation Filtering](https://arxiv.org/abs/2511.12220)** · arXiv · VLM · Training-free
- **[VOPE: Revisiting Hallucination of Vision-Language Models in Voluntary Imagination Task](https://arxiv.org/abs/2511.13420)** · arXiv · VLM · Training-free
- **[Tell Model Where to Look: Mitigating Hallucinations in MLLMs by Vision-Guided Attention](https://arxiv.org/abs/2511.20032)** · arXiv · VLM · Training-free
- **[MaskCD: Mitigating LVLM Hallucinations by Image Head Masked Contrastive Decoding](https://arxiv.org/abs/2510.02790)** · arXiv · VLM · Training-free
- **[ChainMPQ: Interleaved Text-Image Reasoning Chains for Mitigating Relation Hallucinations](https://arxiv.org/abs/2510.06292)** · arXiv · VLM · Training-free
- **[To Sink or Not to Sink: Visual Information Pathways in Large Vision-Language Models](https://arxiv.org/abs/2510.08510)** · arXiv · VLM · Training-free
- **[When Images Speak Louder: Mitigating Language Bias-induced Hallucinations in VLMs through Cross-Modal Guidance](https://arxiv.org/abs/2510.10466)** · arXiv · VLM · Training-free
- **[Self-Augmented Visual Contrastive Decoding](https://arxiv.org/abs/2510.13315)** · arXiv · VLM · Training-free
- **[SHIELD: Suppressing Hallucinations In LVLM Encoders via Bias and Vulnerability Defense](https://arxiv.org/abs/2510.16596)** · arXiv · VLM · Training-free
- **[Seeing but Not Believing: Probing the Disconnect Between Visual Attention and Answer Correctness in VLMs](https://arxiv.org/abs/2510.17771)** · arXiv · VLM · Training-free
- **[Beyond Single Models: Mitigating Multimodal Hallucinations via Adaptive Token Ensemble Decoding](https://arxiv.org/abs/2510.18321)** · arXiv · VLM · Training-free
- **[Why LVLMs Are More Prone to Hallucinations in Longer Responses: The Role of Context](https://arxiv.org/abs/2510.20229)** · arXiv · VLM · Training-free
- **[Capturing Gaze Shifts for Guidance: Cross-Modal Fusion Enhancement for VLM Hallucination Mitigation](https://arxiv.org/abs/2510.22067)** · arXiv · VLM · Training-free
- **[Mitigating Attention Sinks and Massive Activations in Audio-Visual Speech Recognition with LLMs](https://arxiv.org/abs/2510.22603)** · arXiv · MLLM(Omni) · Training-free
- **[Two Causes, Not One: Rethinking Omission and Fabrication Hallucinations in MLLMs](https://arxiv.org/abs/2509.00371)** · arXiv · VLM · Training-free
- **[Unveiling the Response of Large Vision-Language Models to Visually Absent Tokens](https://arxiv.org/abs/2509.03025)** · arXiv · VLM · Training-free
- **[D-LEAF: Localizing and Correcting Hallucinations in Multimodal LLMs via Layer-to-head Attention Diagnostics](https://arxiv.org/abs/2509.07864)** · arXiv · VLM · Training-based
- **[ORCA: An Agentic Reasoning Framework for Hallucination and Adversarial Robustness in Vision-Language Models](https://arxiv.org/abs/2509.15435)** · arXiv · VLM · Training-free
- **[ChartHal: A Fine-grained Framework Evaluating Hallucination of Large Vision Language Models in Chart Understanding](https://arxiv.org/abs/2509.17481)** · arXiv · VLM · Training-free
- **[Hallucination as an Upper Bound: A New Perspective on Text-to-Image Evaluation](https://arxiv.org/abs/2509.21257)** · arXiv · VLM · Training-free
- **[Self-Consistency as a Free Lunch: Reducing Hallucinations in Vision-Language Models via Self-Reflection](https://arxiv.org/abs/2509.23236)** · arXiv · VLM · Training-free
- **[GHOST: Hallucination-Inducing Image Generation for Multimodal LLMs](https://arxiv.org/abs/2509.25178)** · arXiv · VLM · Training-based
- **[Mitigating Hallucination in Multimodal LLMs with Layer Contrastive Decoding](https://arxiv.org/abs/2509.25177)** · arXiv · VLM · Training-free
- **[Mitigating Visual Hallucinations via Semantic Curriculum Preference Optimization in MLLMs](https://arxiv.org/abs/2509.24491)** · arXiv · VLM · Training-based
- **📋 [MIHBench: Benchmarking and Mitigating Multi-Image Hallucinations in Multimodal Large Language Models](https://arxiv.org/abs/2508.00726)** · arXiv · VLM · Training-free
- **[Benchmarking and Bridging Emotion Conflicts for Multimodal Emotion Reasoning](https://arxiv.org/abs/2508.01181)** · arXiv · MLLM(Omni) · Training-based
- **[MAP: Mitigating Hallucinations in Large Vision-Language Models with Map-Level Attention Processing](https://arxiv.org/abs/2508.01653)** · arXiv · VLM · Training-free
- **[What Makes "Good" Distractors for Object Hallucination Evaluation in Large Vision-Language Models?](https://arxiv.org/abs/2508.06530)** · arXiv · VLM · Training-free
- **[Modality Bias in LVLMs: Analyzing and Mitigating Object Hallucination via Attention Lens](https://arxiv.org/abs/2508.02419)** · arXiv · VLM · Training-free
- **[SAVER: Mitigating Hallucinations in Large Vision-Language Models via Style-Aware Visual Early Revision](https://arxiv.org/abs/2508.03177)** · arXiv · VLM · Training-free
- **[Analyzing and Mitigating Object Hallucination: A Training Bias Perspective](https://arxiv.org/abs/2508.04567)** · arXiv · VLM · Training-based
- **[GLSim: Detecting Object Hallucinations in LVLMs via Global-Local Similarity](https://arxiv.org/abs/2508.19972)** · arXiv · VLM · Training-free
- **[Mitigating Hallucinations in Multimodal LLMs via Object-aware Preference Optimization](https://arxiv.org/abs/2508.20181)** · arXiv · VLM · Training-based
- **[ONLY: One-Layer Intervention Sufficiently Mitigates Hallucinations in Large Vision-Language Models](https://arxiv.org/abs/2507.00898)** · arXiv · VLM · Training-free
- **[INTER: Mitigating Hallucination in Large Vision-Language Models by Interaction Guidance Sampling](https://arxiv.org/abs/2507.05056)** · arXiv · VLM · Training-free
- **[Energy-Guided Decoding for Object Hallucination Mitigation](https://arxiv.org/abs/2507.07731)** · arXiv · VLM · Training-free
- **[MCA-LLaVA: Manhattan Causal Attention for Reducing Hallucination in Large Vision-Language Models](https://arxiv.org/abs/2507.09184)** · arXiv · VLM · Training-free
- **[Mitigating Object Hallucinations via Sentence-Level Early Intervention](https://arxiv.org/abs/2507.12455)** · arXiv · VLM · Training-based
- **[Extracting Visual Facts from Intermediate Layers for Mitigating Hallucinations in Multimodal Large Language Models](https://arxiv.org/abs/2507.15652)** · arXiv · VLM · Training-free
- **📚 [A Survey of Multimodal Hallucination Evaluation and Detection](https://arxiv.org/abs/2507.19024)** · arXiv · VLM · Training-free
- **[LISA: A Layer-wise Integration and Suppression Approach for Hallucination Mitigation in Multimodal Large Language Models](https://arxiv.org/abs/2507.19110)** · arXiv · VLM · Training-free
- **[TARS: MinMax Token-Adaptive Preference Strategy for MLLM Hallucination Reduction](https://arxiv.org/abs/2507.21584)** · arXiv · VLM · Training-based
- **[CLAIM: Mitigating Multilingual Object Hallucination in Large Vision-Language Models with Cross-Lingual Attention Intervention](https://arxiv.org/abs/2506.11073)** · arXiv · VLM · Training-free
- **[Mitigating Hallucinations in Large Vision-Language Models via Entity-Centric Multimodal Preference Optimization](https://arxiv.org/abs/2506.04039)** · arXiv · VLM · Training-based
- **[When Semantics Mislead Vision: Mitigating Large Multimodal Models Hallucinations in Scene Text Spotting and Understanding](https://arxiv.org/abs/2506.05551)** · arXiv · VLM · Training-free
- **[Mitigating Object Hallucination via Robust Local Perception Search](https://arxiv.org/abs/2506.06729)** · arXiv · VLM · Training-free
- **[Mitigating Behavioral Hallucination in Multimodal Large Language Models for Sequential Images](https://arxiv.org/abs/2506.07184)** · arXiv · VLM · Training-free
- **[Reducing Object Hallucination in Large Audio-Language Models via Audio-Aware Decoding](https://arxiv.org/abs/2506.07233)** · arXiv · MLLM(Omni) · Training-free
- **[SECOND: Mitigating Perceptual Hallucination in Vision-Language Models via Selective and Contrastive Decoding](https://arxiv.org/abs/2506.08391)** · arXiv · VLM · Training-free
- **[Revisit What You See: Disclose Language Prior in Vision Tokens for Efficient Guided Decoding of LVLMs](https://arxiv.org/abs/2506.09522)** · arXiv · VLM · Training-free
- **[Not All Tokens and Heads Are Equally Important: Dual-Level Attention Intervention for Hallucination Mitigation](https://arxiv.org/abs/2506.12609)** · arXiv · VLM · Training-free
- **[ASCD: Attention-Steerable Contrastive Decoding for Reducing Hallucination in MLLM](https://arxiv.org/abs/2506.14766)** · arXiv · VLM · Training-free
- **[HalluRNN: Mitigating Hallucinations via Recurrent Cross-Layer Reasoning in Large Vision-Language Models](https://arxiv.org/abs/2506.17587)** · arXiv · VLM · Training-free
- **[MDSAM:Memory-Driven Sparse Attention Matrix for LVLMs Hallucination Mitigation](https://arxiv.org/abs/2506.17664)** · arXiv · VLM · Training-free
- **[Visual hallucination detection in large vision-language models via evidential conflict](https://arxiv.org/abs/2506.19513)** · arXiv · VLM · Training-free
- **[CAI: Caption-Sensitive Attention Intervention for Mitigating Object Hallucination in Large Vision-Language Models](https://arxiv.org/abs/2506.23590)** · arXiv · VLM · Training-free
- **[A Comprehensive Analysis for Visual Object Hallucination in Large Vision-Language Models](https://arxiv.org/abs/2505.01958)** · arXiv · VLM · Training-free
- **[Mitigating Image Captioning Hallucinations in Vision-Language Models](https://arxiv.org/abs/2505.03420)** · arXiv · VLM · Training-free
- **[Cross-Image Contrastive Decoding: Precise, Lossless Suppression of Language Priors in Large Vision-Language Models](https://arxiv.org/abs/2505.10634)** · arXiv · VLM · Training-free
- **[Mixture of Decoding: An Attention-Inspired Adaptive Decoding Strategy to Mitigate Hallucinations in Large Vision-Language Models](https://arxiv.org/abs/2505.17061)** · arXiv · VLM · Training-free
- **[Steering LVLMs via Sparse Autoencoder for Hallucination Mitigation](https://arxiv.org/abs/2505.16146)** · arXiv · VLM · Training-free
- **[Seeing It or Not? Interpretable Vision-aware Latent Steering to Mitigate Object Hallucinations](https://arxiv.org/abs/2505.17812)** · arXiv · VLM · Training-free
- **[Focus on What Matters: Enhancing Medical Vision-Language Models with Automatic Attention Alignment Tuning](https://arxiv.org/abs/2505.18503)** · arXiv · VLM · Training-based
- **[Causal-LLaVA: Causal Disentanglement for Mitigating Hallucination in Multimodal Large Language Models](https://arxiv.org/abs/2505.19474)** · arXiv · VLM · Training-free
- **[Enhancing Visual Reliance in Text Generation: A Bayesian Perspective on Mitigating Hallucination in Large Vision-Language Models](https://arxiv.org/abs/2505.19498)** · arXiv · VLM · Training-free
- **[Grounding Language with Vision: A Conditional Mutual Information Calibrated Decoding Strategy for Reducing Hallucinations in LVLMs](https://arxiv.org/abs/2505.19678)** · arXiv · VLM · Training-free
- **[Retrieval Visual Contrastive Decoding to Mitigate Object Hallucinations in Large Vision-Language Models](https://arxiv.org/abs/2505.20569)** · arXiv · VLM · Training-free
- **[AVCD: Mitigating Hallucinations in Audio-Visual Large Language Models through Contrastive Decoding](https://arxiv.org/abs/2505.20862)** · arXiv · MLLM(Omni) · Training-free
- **[Mitigating Hallucinations in Large Vision-Language Models via Adaptive Attention Calibration](https://arxiv.org/abs/2505.21472)** · arXiv · VLM · Training-free
- **[Qwen Look Again: Guiding Vision-Language Reasoning Models to Re-attention Visual Information](https://arxiv.org/abs/2505.23558)** · arXiv · VLM · Training-based
- **[TARAC: Mitigating Hallucination in LVLMs via Temporal Attention Real-time Accumulative Connection](https://arxiv.org/abs/2504.04099)** · arXiv · VLM · Training-free
- **[Decoupling Contrastive Decoding: Robust Hallucination Mitigation in Multimodal Large Language Models](https://arxiv.org/abs/2504.08809)** · arXiv · VLM · Training-free
- **[Don't Deceive Me: Mitigating Gaslighting through Attention Reallocation in LMMs](https://arxiv.org/abs/2504.09456)** · arXiv · VLM · Training-free
- **[The Mirage of Performance Gains: Why Contrastive Decoding Fails to Mitigate Object Hallucinations in MLLMs?](https://arxiv.org/abs/2504.10020)** · arXiv · VLM · Training-free
- **[HalCECE: A Framework for Explainable Hallucination Detection through Conceptual Counterfactuals in Image Captioning](https://arxiv.org/abs/2503.00436)** · arXiv · VLM · Training-free
- **[Octopus: Alleviating Hallucination via Dynamic Contrastive Decoding](https://arxiv.org/abs/2503.00361)** · arXiv · VLM · Training-free
- **[See What You Are Told: Visual Attention Sink in Large Multimodal Models](https://arxiv.org/abs/2503.03321)** · arXiv · VLM · Training-free
- **[TPC: Cross-Temporal Prediction Connection for Vision-Language Model Hallucination Reduction](https://arxiv.org/abs/2503.04457)** · arXiv · VLM · Training-free
- **[PerturboLLaVA: Reducing Multimodal Hallucinations with Perturbative Visual Training](https://arxiv.org/abs/2503.06486)** · arXiv · VLM · Training-free
- **[Hallucinatory Image Tokens: A Training-free EAZY Approach on Detecting and Mitigating Object Hallucinations in LVLMs](https://arxiv.org/abs/2503.07772)** · arXiv · VLM · Training-free
- **[Attention Hijackers: Detect and Disentangle Attention Hijacking in LVLMs for Hallucination Mitigation](https://arxiv.org/abs/2503.08216)** · arXiv · VLM · Training-free
- **[Through the Magnifying Glass: Adaptive Perception Magnification for Hallucination-Free VLM Decoding](https://arxiv.org/abs/2503.10183)** · arXiv · VLM · Training-free
- **[TruthPrInt: Mitigating LVLM Object Hallucination Via Latent Truthful-Guided Pre-Intervention](https://arxiv.org/abs/2503.10602)** · arXiv · VLM · Training-free
- **[Mitigating Object Hallucinations in MLLMs via Multi-Frequency Perturbations](https://arxiv.org/abs/2503.14895)** · arXiv · VLM · Training-free
- **[Mitigating Low-Level Visual Hallucinations Requires Self-Awareness: Database, Model and Training Strategy](https://arxiv.org/abs/2503.20673)** · arXiv · VLM · Training-based
- **[MINT: Mitigating Hallucinations in Large Vision-Language Models via Token Reduction](https://arxiv.org/abs/2502.00717)** · arXiv · VLM · Training-free
- **[Mitigating Hallucinations in Large Vision-Language Models with Internal Fact-based Contrastive Decoding](https://arxiv.org/abs/2502.01056)** · arXiv · VLM · Training-free
- **[Visual Attention Never Fades: Selective Progressive Attention ReCalibration for Detailed Image Captioning in Multimodal Large Language Models](https://arxiv.org/abs/2502.01419)** · arXiv · VLM · Training-free
- **[Mitigating Object Hallucinations in Large Vision-Language Models via Attention Calibration](https://arxiv.org/abs/2502.01969)** · arXiv · VLM · Training-free
- **[Self-Correcting Decoding with Generative Feedback for Mitigating Hallucinations in Large Vision-Language Models](https://arxiv.org/abs/2502.06130)** · arXiv · VLM · Training-free
- **[CutPaste&Find: Efficient Multimodal Hallucination Detector with Visual-aid Knowledge Base](https://arxiv.org/abs/2502.12591)** · arXiv · VLM · Training-free
- **[Re-Align: Aligning Vision Language Models via Retrieval-Augmented Direct Preference Optimization](https://arxiv.org/abs/2502.13146)** · arXiv · VLM · Training-based
- **[Reducing Hallucinations of Medical Multimodal Large Language Models with Visual Retrieval-Augmented Generation](https://arxiv.org/abs/2502.15040)** · arXiv · VLM · Training-free
- **[The Role of Background Information in Reducing Object Hallucination in Vision-Language Models: Insights from Cutoff API Prompting](https://arxiv.org/abs/2502.15389)** · arXiv · VLM · Training-free
- **[Exploring Causes and Mitigation of Hallucinations in Large Vision Language Models](https://arxiv.org/abs/2502.16842)** · arXiv · VLM · Training-free
- **[MLLMs Know Where to Look: Training-free Perception of Small Visual Details with Multimodal LLMs](https://arxiv.org/abs/2502.17422)** · arXiv · VLM · Training-free
- **[Do Vision Encoders Truly Explain Object Hallucination?: Mitigating Object Hallucination via Simple Fine-Grained CLIPScore](https://arxiv.org/abs/2502.20034)** · arXiv · VLM · Training-free
- **[Cross-Modal Attention Calibration for LVLM Hallucination Mitigation](https://arxiv.org/abs/2501.01926)** · arXiv · VLM · Training-free
- **[PAINT: Paying Attention to INformed Tokens to Mitigate Hallucination in Large Vision-Language Model](https://arxiv.org/abs/2501.12206)** · arXiv · VLM · Training-free
- **[Evaluating Hallucination in Large Vision-Language Models based on Context-Aware Object Similarities](https://arxiv.org/abs/2501.15046)** · arXiv · VLM · Training-free
- **[Poison as Cure: Visual Noise for Mitigating Object Hallucinations in LVMs](https://arxiv.org/abs/2501.19164)** · arXiv · VLM · Training-free
- **[&quot;Not Aligned&quot; is Not &quot;Malicious&quot;: Being Careful about Hallucinations of Large Language Models&apos; Jailbreak](https://aclanthology.org/2025.coling-main.146/)** · ACL · LLM · Training-free
- **📋 [3D-GRAND: A Million-Scale Dataset for 3D-LLMs with Better Grounding and Less Hallucination](https://openaccess.thecvf.com/content/CVPR2025/html/Yang_3D-GRAND_A_Million-Scale_Dataset_for_3D-LLMs_with_Better_Grounding_and_CVPR_2025_paper.html)** · Unlabeled · VLM · Training-free
- **[A Head to Predict and a Head to Question: Pre-trained Uncertainty Quantification Heads for Hallucination Detection in LLM Outputs](https://doi.org/10.18653/v1/2025.emnlp-main.1809)** · Other · LLM · Training-free
- **[A Probabilistic Framework for LLM Hallucination Detection via Belief Tree Propagation](https://doi.org/10.18653/v1/2025.naacl-long.158)** · Other · LLM · Training-free
- **📚 [A Review of Faithfulness Metrics for Hallucination Assessment in Large Language Models](https://doi.org/10.1109/jstsp.2025.3579203)** · Other · LLM · Training-free
- **[A Weighted Cross-entropy Loss for Mitigating LLM Hallucinations in Cross-lingual Continual Pretraining](https://doi.org/10.1109/ICASSP49660.2025.10888877)** · Other · LLM · Training-free
- **Activation Steering Decoding: Mitigating Hallucination in Large Vision-Language Models through Bidirectional Hidden State Intervention** · Unlabeled · VLM · Training-free
- **[Active Layer-Contrastive Decoding Reduces Hallucination in Large Language Model Generation](https://doi.org/10.18653/v1/2025.emnlp-main.150)** · Other · LLM · Training-free
- **[Adaptive Activation Steering: A Tuning-Free LLM Truthfulness Improvement Method for Diverse Hallucinations Categories](https://doi.org/10.1145/3696410.3714640)** · Other · LLM · Training-free
- **[Addressing Hallucination in Causal Q&amp;A: The Efficacy of Fine-tuning over Prompting in LLMs](https://aclanthology.org/2025.finnlp-1.27/)** · ACL · LLM · Training-based
- **[Aerial Mirage: Unmasking Hallucinations in Large Vision Language Models](https://doi.org/10.1109/WACV61041.2025.00537)** · Other · VLM · Training-free
- **[Aftina: enhancing stability and preventing hallucination in AI-based Islamic fatwa generation using LLMs and RAG](https://doi.org/10.1007/s00521-025-11229-y)** · Other · LLM · Training-free
- **[Agentic Legal Intake: A Multi-Agent Framework For Hallucination-Free, Audit-Ready AI Screening In Mass-Tort Litigation](https://doi.org/10.37547/feaiml/volume02issue09-02)** · Other · LLM · Training-free
- **[AI Hallucination and Strategies to Overcome: Enhancing Human-AI Interaction](https://doi.org/10.1109/aimv66517.2025.11203756)** · Other · LLM · Training-free
- **[AI Hallucination in the Context of Education: Exploring College Students’ Use of Generative AI for Academic Tasks](https://doi.org/10.1109/ic4e65071.2025.11075444)** · Other · LLM · Training-free
- **[AI Hallucinations? What About Human Hallucination?! Addressing Human Imperfection Is Needed for an Ethical AI](https://doi.org/10.9781/ijimai.2025.02.010)** · Other · LLM · Training-free
- **[AI in conjunctivitis research: assessing ChatGPT and DeepSeek for etiology, intervention, and citation integrity via hallucination rate analysis](https://doi.org/10.3389/frai.2025.1579375)** · Other · LLM · Training-free
- **Alleviating Hallucination in Large Vision-Language Models with Active Retrieval Augmentation** · Unlabeled · VLM · Training-free
- **[Alleviating Hallucinations from Knowledge Misalignment in Large Language Models via Selective Abstention Learning](https://doi.org/10.18653/v1/2025.acl-long.1199)** · Other · LLM · Training-free
- **[Alleviating Hallucinations in Large Language Models through Multi-Model Contrastive Decoding and Dynamic Hallucination Detection](http://papers.nips.cc/paper_files/paper/2025/hash/f1a92c4df8cd7dc1cab2613fb999d5e7-Abstract-Conference.html)** · Unlabeled · LLM · Training-free
- **[Alleviating Hallucinations of Large Language Models through Induced Hallucinations](https://doi.org/10.18653/v1/2025.findings-naacl.459)** · Other · LLM · Training-free
- **[Alleviating LLM-based Generative Retrieval Hallucination in Alipay Search](https://doi.org/10.1145/3726302.3731951)** · Other · LLM · Training-free
- **[An Analysis on AI Hallucination from the Perspective of Media Archaeology](https://doi.org/10.54254/2753-7064/2025.bj29177)** · Other · LLM · Training-free
- **[Antidote: A Unified Framework for Mitigating LVLM Hallucinations in Counterfactual Presupposition and Object Perception](https://openaccess.thecvf.com/content/CVPR2025/html/Wu_Antidote_A_Unified_Framework_for_Mitigating_LVLM_Hallucinations_in_Counterfactual_CVPR_2025_paper.html)** · Unlabeled · VLM · Training-free
- **[AraHalluEval: A Fine-grained Hallucination Evaluation Framework for Arabic LLMs](https://doi.org/10.18653/v1/2025.arabicnlp-main.12)** · Other · LLM · Training-free
- **[ARGUS: Hallucination and Omission Evaluation in Video-LLMs](https://doi.org/10.1109/ICCV51701.2025.01886)** · Other · VLM · Training-free
- **[Attention-guided Self-reflection for Zero-shot Hallucination Detection in Large Language Models](https://doi.org/10.18653/v1/2025.emnlp-main.1063)** · Other · LLM · Training-free
- **[Attributive Reasoning for Hallucination Diagnosis of Large Language Models](https://doi.org/10.1609/aaai.v39i22.34536)** · Other · LLM · Training-free
- **[Auditing Meta-Cognitive Hallucinations in Reasoning Large Language Models](http://papers.nips.cc/paper_files/paper/2025/hash/ee0e336e2423430ef86071300299e074-Abstract-Conference.html)** · Unlabeled · LLM · Training-free
- **📋 [AVHBench: A Cross-Modal Hallucination Benchmark for Audio-Visual Large Language Models](https://openreview.net/forum?id=jTEKTdI3K9)** · Unlabeled · MLLM(Omni) · Training-free
- **[Benford&apos;s Curse: Tracing Digit Bias to Numerical Hallucination in LLMs](http://papers.nips.cc/paper_files/paper/2025/hash/aa5f5e6eb6f613ec412f1d948dfa21a5-Abstract-Conference.html)** · Unlabeled · LLM · Training-free
- **[Beyond Facts: Evaluating Intent Hallucination in Large Language Models](https://doi.org/10.18653/v1/2025.acl-long.349)** · Other · LLM · Training-free
- **[Beyond Hallucination: Generative AI as a Catalyst for Human Creativity and Cognitive Evolution](https://doi.org/10.62762/tetai.2025.657559)** · Other · LLM · Training-free
- **[Beyond Logit Lens: Contextual Embeddings for Robust Hallucination Detection &amp; Grounding in VLMs](https://doi.org/10.18653/v1/2025.naacl-long.488)** · Other · VLM · Training-free
- **[Beyond Multimodal Hallucinations: Enhancing LVLMs through Hallucination-Aware Direct Preference Optimization](https://doi.org/10.1109/ICME59968.2025.11209377)** · Other · VLM · Training-based
- **[Beyond Token Probes: Hallucination Detection via Activation Tensors with ACT-ViT](http://papers.nips.cc/paper_files/paper/2025/hash/7b8694d58c34b9bec9c2f29735c3a250-Abstract-Conference.html)** · Unlabeled · LLM · Training-free
- **BIMA: Bijective Maximum Likelihood Learning Approach to Hallucination Prediction and Mitigation in Large Vision-Language Models** · Unlabeled · VLM · Training-free
- **[Black-Box Visual Prompt Engineering for Mitigating Object Hallucination in Large Vision Language Models](https://doi.org/10.18653/v1/2025.naacl-short.45)** · Other · VLM · Training-free
- **[Bold Claims or Self-Doubt? Factuality Hallucination Type Detection via Belief State](https://doi.org/10.18653/v1/2025.findings-emnlp.527)** · Other · LLM · Training-free
- **[Bridging External and Parametric Knowledge: Mitigating Hallucination of LLMs with Shared-Private Semantic Synergy in Dual-Stream Knowledge](https://doi.org/10.18653/v1/2025.emnlp-main.549)** · Other · LLM · Training-free
- **CAAC: Confidence-Aware Attention Calibration to Reduce Hallucinations in Large Vision-Language Models** · Unlabeled · VLM · Training-free
- **[Calibrating Verbal Uncertainty as a Linear Feature to Reduce Hallucinations](https://doi.org/10.18653/v1/2025.emnlp-main.187)** · Other · LLM · Training-free
- **[Calm-Whisper: Reduce Whisper Hallucination On Non-Speech By Calming Crazy Heads Down](https://doi.org/10.21437/Interspeech.2025-201)** · Other · MLLM(Omni) · Training-free
- **[Can Hallucination Correction Improve Video-Language Alignment?](https://doi.org/10.18653/v1/2025.findings-acl.1314)** · Other · VLM · Training-free
- **[Can Knowledge Editing Really Correct Hallucinations?](https://openreview.net/forum?id=hmDt068MoZ)** · Unlabeled · LLM · Training-based
- **[Can Large Audio-Language Models Truly Hear? Tackling Hallucinations with Multi-Task Assessment and Stepwise Audio Reasoning](https://doi.org/10.1109/ICASSP49660.2025.10888384)** · Other · MLLM(Omni) · Training-free
- **[Can We Trust Large Language Models for Video Analysis: An Exploration of Hallucination in Multimodal LLMs](https://doi.org/10.22318/icls2025.704957)** · Other · VLM · Training-free
- **📋 [CCHall: A Novel Benchmark for Joint Cross-Lingual and Cross-Modal Hallucinations Detection in Large Language Models](https://doi.org/10.18653/v1/2025.acl-long.1485)** · Other · LLM · Training-free
- **[CCL-XCoT: An Efficient Cross-Lingual Knowledge Transfer Method for Mitigating Hallucination Generation](https://doi.org/10.18653/v1/2025.findings-emnlp.93)** · Other · LLM · Training-free
- **[Chain-of-Thought Prompting Obscures Hallucination Cues in Large Language Models: An Empirical Evaluation](https://doi.org/10.18653/v1/2025.findings-emnlp.67)** · Other · LLM · Training-free
- **[CHAIR-Classifier of Hallucination As Improver](https://doi.org/10.1109/ijcnn64981.2025.11227344)** · Other · LLM · Training-free
- **[ChartCap: Mitigating Hallucination of Dense Chart Captioning](https://doi.org/10.1109/ICCV51701.2025.01224)** · Other · LLM · Training-free
- **ClearSight: Visual Signal Enhancement for Object Hallucination Mitigation in Multimodal Large Language Models** · Unlabeled · VLM · Training-free
- **📋 [CodeHalu: Investigating Code Hallucinations in LLMs via Execution-based Verification](https://doi.org/10.1609/aaai.v39i24.34717)** · Other · LLM · Training-free
- **[Collaboration Wins More: Dual-Modal Collaborative Attention Reinforcement for Mitigating Large Vision Language Models Hallucination](https://doi.org/10.1145/3746027.3755320)** · Other · VLM · Training-free
- **[Combating Multimodal LLM Hallucination via Bottom-Up Holistic Reasoning](https://doi.org/10.1609/aaai.v39i8.32913)** · Other · VLM · Training-free
- **[Comparison of explainability methods for hallucination analysis in LLMs](https://doi.org/10.12688/openreseurope.20839.1)** · Other · LLM · Training-free
- **[CoMT: Chain-of-Medical-Thought Reduces Hallucination in Medical Report Generation](https://doi.org/10.1109/ICASSP49660.2025.10887699)** · Other · LLM · Training-free
- **[Confident but Incorrect: Mitigating Hallucination and Overconfidence in Agentic AI Coders](https://doi.org/10.1109/iciip68302.2025.11346318)** · Other · LLM · Training-free
- **[Context-Aware Image Caption Editing via Hallucination-Resistant Visual Instruction Tuning](https://doi.org/10.1109/ICCVW69036.2025.00615)** · Other · VLM · Training-based
- **[Counterfactual Debating with Preset Stances for Hallucination Elimination of LLMs](https://aclanthology.org/2025.coling-main.703/)** · ACL · LLM · Training-free
- **[Countering AI Hallucination by Utilizing a Concept-Aware Model](https://doi.org/10.1109/mecon67253.2025.11277080)** · Other · LLM · Training-free
- **Damo: Decoding by Accumulating Activations Momentum for Mitigating Hallucinations in Vision-Language Models** · Unlabeled · VLM · Training-free
- **[DAPE-BR: Distance-Aware Positional Encoding for Mitigating Object Hallucination in LVLMs](https://doi.org/10.18653/v1/2025.findings-emnlp.459)** · Other · VLM · Training-free
- **[DASH: Detection and Assessment of Systematic Hallucinations of VLMs](https://doi.org/10.1109/ICCV51701.2025.02112)** · Other · VLM · Training-free
- **[DeCoRe: Decoding by Contrasting Retrieval Heads to Mitigate Hallucinations](https://doi.org/10.18653/v1/2025.findings-emnlp.531)** · Other · LLM · Training-free
- **[DeepSIX at ACM MM 2025 Grand Challenge: Enhancing Context Text Processing for Multimodal Hallucination Detection and Fact Verification](https://doi.org/10.1145/3746027.3762061)** · Other · VLM · Training-free
- **[Detecting and Mitigating Hallucination in Large Vision Language Models via Fine-Grained AI Feedback](https://doi.org/10.1609/aaai.v39i24.34744)** · Other · VLM · Training-free
- **[Detecting Hallucination in Large Language Models Through Deep Internal Representation Analysis](https://doi.org/10.24963/ijcai.2025/929)** · Other · LLM · Training-free
- **[Detecting LLM Hallucination Through Layer-wise Information Deficiency: Analysis of Ambiguous Prompts and Unanswerable Questions](https://doi.org/10.18653/v1/2025.emnlp-main.1644)** · Other · LLM · Training-free
- **[Detection of LLM Hallucinations Using Late Internal Representations](https://doi.org/10.1109/ICMLA66185.2025.00214)** · Other · LLM · Training-free
- **[Developing a Reliable, Fast, General-Purpose Hallucination Detection and Mitigation Service](https://doi.org/10.18653/v1/2025.naacl-industry.72)** · Other · LLM · Training-free
- **[DHCP: Detecting Hallucinations by Cross-modal Attention Pattern in Large Vision-Language Models](https://doi.org/10.1145/3746027.3755118)** · Other · VLM · Training-free
- **[Diving into Mitigating Hallucinations from a Vision Perspective for Large Vision-Language Models](https://doi.org/10.18653/v1/2025.findings-emnlp.936)** · Other · VLM · Training-free
- **[Do I Know This Entity? Knowledge Awareness and Hallucinations in Language Models](https://openreview.net/forum?id=WCRQFlji2q)** · Unlabeled · LLM · Training-free
- **[Do LVLMs Truly Understand Video Anomalies? Revealing Hallucination via Co-Occurrence Patterns](http://papers.nips.cc/paper_files/paper/2025/hash/99b419554537c66bf27e5eb7a74c7de4-Abstract-Conference.html)** · Unlabeled · VLM · Training-free
- **[Do Robot Snakes Dream like Electric Sheep? Investigating the Effects of Architectural Inductive Biases on Hallucination](https://doi.org/10.18653/v1/2025.findings-acl.60)** · Other · LLM · Training-free
- **[Do You Keep an Eye on What I Ask? Mitigating Multimodal Hallucination via Attention-Guided Ensemble Decoding](https://openreview.net/forum?id=ziw5bzg2NO)** · Unlabeled · VLM · Training-free
- **[DRAG: Distilling RAG for SLMs from LLMs to Transfer Knowledge and Mitigate Hallucination via Evidence and Graph-based Distillation](https://doi.org/10.18653/v1/2025.acl-long.358)** · Other · LLM · Training-free
- **[Dynamic Cognitive Bias: Hallucination and Forgetting in the Cognitive Dynamics of LLMs](https://doi.org/10.1109/ijcnn64981.2025.11229003)** · Other · LLM · Training-free
- **[EGOILLUSION: Benchmarking Hallucinations in Egocentric Video Understanding](https://doi.org/10.18653/v1/2025.emnlp-main.1446)** · Other · VLM · Training-free
- **[Enhancing Uncertainty Modeling with Semantic Graph for Hallucination Detection](https://doi.org/10.1609/aaai.v39i22.34528)** · Other · LLM · Training-free
- **[Ethical Prompt Design for Health Equity: Preventing Hallucination and Addressing Bias in AI Diagnoses](https://doi.org/10.63282/3050-9262.ijaidsml-v6i3p102)** · Other · LLM · Training-free
- **[Evaluating and Mitigating Object Hallucination in Large Vision-Language Models: Can They Still See Removed Objects?](https://doi.org/10.18653/v1/2025.naacl-long.349)** · Other · VLM · Training-free
- **[Evaluating Evaluation Metrics - The Mirage of Hallucination Detection](https://doi.org/10.18653/v1/2025.findings-emnlp.1035)** · Other · LLM · Training-free
- **[Evaluating Image Hallucination in Text-to-Image Generation with Question-Answering](https://doi.org/10.1609/aaai.v39i25.34827)** · Other · VLM · Training-free
- **[Evaluating LLMs’ Assessment of Mixed-Context Hallucination Through the Lens of Summarization](https://doi.org/10.18653/v1/2025.findings-acl.847)** · Other · LLM · Training-free
- **[Evaluating the Effects of Prompt Perturbation on Bias and Hallucination in Large Language Models](https://doi.org/10.1007/978-981-96-6588-4_25)** · Other · LLM · Training-free
- **[Expertise or Hallucination? A Comprehensive Evaluation of ChatGPT's Aptitude in Clinical Genetics](https://doi.org/10.1109/tbdata.2025.3536939)** · Other · LLM · Training-free
- **[Explainable Hallucination through Natural Language Inference Mapping](https://doi.org/10.18653/v1/2025.findings-acl.96)** · Other · LLM · Training-free
- **[Explore the Hallucination on Low-level Perception for MLLMs](https://doi.org/10.1109/ICASSP49660.2025.10888437)** · Other · VLM · Training-free
- **[Exploring the Generalizability of Factual Hallucination Mitigation via Enhancing Precise Knowledge Utilization](https://doi.org/10.18653/v1/2025.findings-emnlp.211)** · Other · LLM · Training-free
- **[Fact-Controlled Diagnosis of Hallucinations in Medical Text Summarization](https://doi.org/10.21437/Interspeech.2025-537)** · Other · LLM · Training-free
- **[FACT: Mitigating Inconsistent Hallucinations in LLMs via Fact-Driven Alternating Code-Text Training](http://papers.nips.cc/paper_files/paper/2025/hash/bc75254bc4b8b42f401d0ab5d6e9aa4b-Abstract-Conference.html)** · Unlabeled · LLM · Training-free
- **[FACTCHECKMATE: Preemptively Detecting and Mitigating Hallucinations in LMs](https://doi.org/10.18653/v1/2025.findings-emnlp.663)** · Other · LLM · Training-free
- **[FactCheXcker: Mitigating Measurement Hallucinations in Chest X-ray Report Generation Models](https://openaccess.thecvf.com/content/CVPR2025/html/Heiman_FactCheXcker_Mitigating_Measurement_Hallucinations_in_Chest_X-ray_Report_Generation_Models_CVPR_2025_paper.html)** · Unlabeled · LLM · Training-free
- **📋 [FaithBench: A Diverse Hallucination Benchmark for Summarization by Modern LLMs](https://doi.org/10.18653/v1/2025.naacl-short.38)** · Other · LLM · Training-free
- **[Few-Shot Optimized Framework for Hallucination Detection in Resource-Limited NLP Systems](https://doi.org/10.1007/978-981-96-6441-2_16)** · Other · LLM · Training-free
- **[FG-PRM: Fine-grained Hallucination Detection and Mitigation in Language Model Mathematical Reasoning](https://doi.org/10.18653/v1/2025.findings-emnlp.228)** · Other · LLM · Training-free
- **[From Pixels to Tokens: Revisiting Object Hallucinations in Large Vision-Language Models](https://doi.org/10.1145/3746027.3755728)** · Other · VLM · Training-free
- **[Fuzzy Contrastive Decoding to Alleviate Object Hallucination in Large Vision-Language Models](https://doi.org/10.1109/ICCV51701.2025.01913)** · Other · VLM · Training-free
- **[G2LDetect: A Global-to-Local Approach for Hallucination Detection](https://doi.org/10.1609/aaai.v39i1.31985)** · Other · LLM · Training-free
- **[Generalization or Hallucination? Understanding Out-of-Context Reasoning in Transformers](http://papers.nips.cc/paper_files/paper/2025/hash/cc7c9c8e4a84b0ca00d874e1a8938644-Abstract-Conference.html)** · Unlabeled · LLM · Training-free
- **[Generative AI in Medical Pharmacology: Balancing Educational Benefits and Hallucination Risks](https://doi.org/10.21275/sr25415140148)** · Other · LLM · Training-free
- **[GOLFer: Smaller LMs-Generated Documents Hallucination Filter &amp; Combiner for Query Expansion in Information Retrieval](https://doi.org/10.18653/v1/2025.findings-acl.8)** · Other · LLM · Training-free
- **[GPTs and Hallucination](https://doi.org/10.1145/3703757)** · Other · LLM · Training-free
- **[Gradient-guided Attention Map Editing: Towards Efficient Contextual Hallucination Mitigation](https://doi.org/10.18653/v1/2025.findings-naacl.458)** · Other · LLM · Training-free
- **[GRAIT: Gradient-Driven Refusal-Aware Instruction Tuning for Effective Hallucination Mitigation](https://doi.org/10.18653/v1/2025.findings-naacl.223)** · Other · LLM · Training-based
- **[GraphRAG: Leveraging Graph-Based Efficiency to Minimize Hallucinations in LLM-Driven RAG for Finance Data](https://aclanthology.org/2025.genaik-1.6/)** · ACL · LLM · Training-free
- **[GRAVITI: Grounded Retrieval Generation Framework for VideoLLM Hallucination Mitigation](https://doi.org/10.5120/ijca2025926005)** · Other · LLM · Training-free
- **[HaDeMiF: Hallucination Detection and Mitigation in Large Language Models](https://openreview.net/forum?id=VwOYxPScxB)** · Unlabeled · LLM · Training-free
- **[HalLoc: Token-level Localization of Hallucinations for Vision Language Models](https://openaccess.thecvf.com/content/CVPR2025/html/Park_HalLoc_Token-level_Localization_of_Hallucinations_for_Vision_Language_Models_CVPR_2025_paper.html)** · Unlabeled · VLM · Training-free
- **[HALLUCANA: Fixing LLM Hallucination with A Canary Lookahead](https://doi.org/10.18653/v1/2025.findings-naacl.12)** · Other · LLM · Training-free
- **[Hallucination and Panic in Autonomous Systems](https://doi.org/10.1007/978-3-031-95207-4)** · Other · LLM · Training-free
- **[Hallucination at a Glance: Controlled Visual Edits and Fine-Grained Multimodal Learning](http://papers.nips.cc/paper_files/paper/2025/hash/c518f504ad5894ccb264a9890f0f5544-Abstract-Conference.html)** · Unlabeled · VLM · Training-free
- **[Hallucination Detection and Confidence Calibration for Large Language Model Outputs: Reproducible Experiments on HaluEval](https://doi.org/10.69987/aimlr.2025.60401)** · Other · LLM · Training-free
- **[Hallucination Detection in LLMs Using Spectral Features of Attention Maps](https://doi.org/10.18653/v1/2025.emnlp-main.1239)** · Other · LLM · Training-free
- **[Hallucination Detection in LLMs via Beam Search Sampling and Semantic Consistency Analysis](https://doi.org/10.1109/dsn-w65791.2025.00076)** · Other · LLM · Training-free
- **[Hallucination Detection in Structured Query Generation via LLM Self-Debating](https://doi.org/10.18653/v1/2025.findings-emnlp.873)** · Other · LLM · Training-free
- **[Hallucination Detectives at SemEval-2025 Task 3: Span-Level Hallucination Detection for LLM-Generated Answers](https://aclanthology.org/2025.semeval-1.84/)** · ACL · LLM · Training-free
- **[Hallucination Reduction in Video-Language Models via Hierarchical Multimodal Consistency](https://doi.org/10.24963/ijcai.2025/1019)** · Other · VLM · Training-free
- **[Hallucination-Aware Prompt Optimization for Text-to-Video Synthesis](https://doi.org/10.24963/ijcai.2025/1133)** · Other · VLM · Training-free
- **[Hallucination-Free Automatic Question &amp; Answer Generation for Intuitive Learning](https://doi.org/10.1109/icipw68931.2025.11386040)** · Other · LLM · Training-free
- **[Hallucinatory Image Tokens: A Training-Free EAZY Approach to Detecting and Mitigating Object Hallucinations in LVLMs](https://doi.org/10.1109/ICCV51701.2025.02009)** · Other · VLM · Training-free
- **[HalluDetect: Detecting, Mitigating, and Benchmarking Hallucinations in Conversational Systems in the Legal Domain](https://doi.org/10.18653/v1/2025.emnlp-industry.128)** · Other · LLM · Training-free
- **📋 [HalluLens: LLM Hallucination Benchmark](https://doi.org/10.18653/v1/2025.acl-long.1176)** · Other · LLM · Training-free
- **[HalluShift: Measuring Distribution Shifts towards Hallucination Detection in LLMs](https://doi.org/10.1109/ijcnn64981.2025.11228484)** · Other · LLM · Training-free
- **[HD-NDEs: Neural Differential Equations for Hallucination Detection in LLMs](https://doi.org/10.18653/v1/2025.acl-long.309)** · Other · LLM · Training-free
- **[HEAL: An Empirical Study on Hallucinations in Embodied Agents Driven by Large Language Models](https://doi.org/10.18653/v1/2025.findings-emnlp.1158)** · Other · LLM · Training-free
- **[Hermit Kingdom Through the Lens of Multiple Perspectives: A Case Study of LLM Hallucination on North Korea](https://aclanthology.org/2025.coling-main.226/)** · ACL · LLM · Training-free
- **[HICD: Hallucination-Inducing via Attention Dispersion for Contrastive Decoding to Mitigate Hallucinations in Large Language Models](https://doi.org/10.18653/v1/2025.findings-acl.405)** · Other · LLM · Training-free
- **[HKD4VLM: A Progressive Hybrid Knowledge Distillation Framework for Robust Multimodal Hallucination and Factuality Detection in VLMs](https://doi.org/10.1145/3746027.3762014)** · Other · VLM · Training-free
- **📋 [How LLMs React to Industrial Spatio-Temporal Data? Assessing Hallucination with a Novel Traffic Incident Benchmark Dataset](https://doi.org/10.18653/v1/2025.naacl-industry.4)** · Other · LLM · Training-free
- **[How Much Do LLMs Hallucinate across Languages? On Realistic Multilingual Estimation of LLM Hallucination](https://doi.org/10.18653/v1/2025.emnlp-main.1481)** · Other · LLM · Training-free
- **[ICT: Image-Object Cross-Level Trusted Intervention for Mitigating Object Hallucination in Large Vision-Language Models](https://openaccess.thecvf.com/content/CVPR2025/html/Chen_ICT_Image-Object_Cross-Level_Trusted_Intervention_for_Mitigating_Object_Hallucination_in_CVPR_2025_paper.html)** · Unlabeled · VLM · Training-free
- **[Identify, Isolate, and Purge: Mitigating Hallucinations in LVLMs via Self-Evolving Distillation](https://doi.org/10.1145/3746027.3754784)** · Other · VLM · Training-free
- **[Image Token Matters: Mitigating Hallucination in Discrete Tokenizer-based Large Vision-Language Models via Latent Editing](http://papers.nips.cc/paper_files/paper/2025/hash/a17c939f1bdee90ec74a9c3cb938d8c3-Abstract-Conference.html)** · Unlabeled · VLM · Training-free
- **Improve Decoding Factuality by Token-wise Cross Layer Entropy of Large Language Models** · Unlabeled · LLM · Training-free
- **[Instruction-Aligned Visual Attention for Mitigating Hallucinations in Large Vision-Language Models](https://doi.org/10.1109/ICME59968.2025.11209139)** · Other · VLM · Training-free
- **Interpreting and Editing Vision-Language Representations to Mitigate Hallucinations** · Unlabeled · VLM · Training-free
- **[Intervene-All-Paths: Unified Mitigation of LVLM Hallucinations across Alignment Formats](http://papers.nips.cc/paper_files/paper/2025/hash/d0cf89927acd9136d27ebf08f9e8a888-Abstract-Conference.html)** · Unlabeled · VLM · Training-free
- **Intervening Anchor Token: Decoding Strategy in Alleviating Hallucinations for MLLMs** · Unlabeled · VLM · Training-free
- **[Investigating Hallucinations in Simultaneous Machine Translation: Knowledge Distillation Solution and Components Analysis](https://doi.org/10.18653/v1/2025.naacl-long.364)** · Other · LLM · Training-free
- **[Investigating Hallucinations of Time Series Foundation Models through Signal Subspace Analysis](http://papers.nips.cc/paper_files/paper/2025/hash/a5059a9a389ccc76da85760ea79490d8-Abstract-Conference.html)** · Unlabeled · LLM · Training-free
- **[Investigation of Whisper ASR Hallucinations Induced by Non-Speech Audio](https://doi.org/10.1109/ICASSP49660.2025.10890105)** · Other · MLLM(Omni) · Training-free
- **[Is LLMs Hallucination Usable? LLM-based Negative Reasoning for Fake News Detection](https://doi.org/10.1609/aaai.v39i1.32089)** · Other · LLM · Training-free
- **📋 [K-HALU: Multiple Answer Korean Hallucination Benchmark for Large Language Models](https://openreview.net/forum?id=VnLhUogHYE)** · Unlabeled · LLM · Training-free
- **📋 [KG-FPQ: Evaluating Factuality Hallucination in LLMs with Knowledge Graph-based False Premise Questions](https://aclanthology.org/2025.coling-main.698/)** · ACL · LLM · Training-free
- **[Large Language Models With Contrastive Decoding Algorithm for Hallucination Mitigation in Low‐Resource Languages](https://doi.org/10.1049/cit2.70004)** · Other · LLM · Training-free
- **[LargePiG for Hallucination-Free Query Generation: Your Large Language Model is Secretly a Pointer Generator](https://doi.org/10.1145/3696410.3714800)** · Other · LLM · Training-free
- **[LLMs Know More Than They Show: On the Intrinsic Representation of LLM Hallucinations](https://openreview.net/forum?id=KRnsX5Em3W)** · Unlabeled · LLM · Training-free
- **[Logit Space Constrained Fine-Tuning for Mitigating Hallucinations in LLM-Based Recommender Systems](https://doi.org/10.18653/v1/2025.emnlp-main.1491)** · Other · LLM · Training-free
- **[Long-form Hallucination Detection with Self-elicitation](https://doi.org/10.18653/v1/2025.findings-acl.211)** · Other · LLM · Training-free
- **[Look, Compare, Decide: Alleviating Hallucination in Large Vision-Language Models via Multi-View Multi-Path Reasoning](https://aclanthology.org/2025.coling-main.299/)** · ACL · VLM · Training-free
- **[Lost in Transcription, Found in Distribution Shift: Demystifying Hallucination in Speech Foundation Models](https://doi.org/10.18653/v1/2025.findings-acl.1190)** · Other · MLLM(Omni) · Training-free
- **[Low-Hallucination and Efficient Coreference Resolution with LLMs](https://doi.org/10.18653/v1/2025.findings-emnlp.934)** · Other · LLM · Training-free
- **[Luna: A Lightweight Evaluation Model to Catch Language Model Hallucinations with High Accuracy and Low Cost](https://aclanthology.org/2025.coling-industry.34/)** · ACL · LLM · Training-based
- **[Make VLM Recognize Visual Hallucination on Cartoon Character Image with Pose Information](https://doi.org/10.1109/WACV61041.2025.00527)** · Other · VLM · Training-free
- **[MASH-VLM: Mitigating Action-Scene Hallucination in Video-LLMs through Disentangled Spatial-Temporal Representations](https://openaccess.thecvf.com/content/CVPR2025/html/Bae_MASH-VLM_Mitigating_Action-Scene_Hallucination_in_Video-LLMs_through_Disentangled_Spatial-Temporal_Representations_CVPR_2025_paper.html)** · Unlabeled · VLM · Training-free
- **📋 [MedHallBench: A New Benchmark for Assessing Hallucination in Medical Large Language Models](https://proceedings.mlr.press/v281/zuo25b.html)** · Unlabeled · LLM · Training-free
- **📋 [MedHallu: A Comprehensive Benchmark for Detecting Medical Hallucinations in Large Language Models](https://doi.org/10.18653/v1/2025.emnlp-main.143)** · Other · LLM · Training-free
- **[MESH - Understanding Videos Like Human: Measuring Hallucinations in Large Video Models](https://doi.org/10.1145/3746027.3755626)** · Other · VLM · Training-free
- **[MHALO: Evaluating MLLMs as Fine-grained Hallucination Detectors](https://doi.org/10.18653/v1/2025.findings-acl.478)** · Other · VLM · Training-free
- **📋 [MHBench: Demystifying Motion Hallucination in VideoLLMs](https://doi.org/10.1609/aaai.v39i4.32463)** · Other · LLM · Training-free
- **[MIRAGE: Assessing Hallucination in Multimodal Reasoning Chains of MLLM](http://papers.nips.cc/paper_files/paper/2025/hash/b238324b309da12c7446d92c14db9f7e-Abstract-Conference.html)** · Unlabeled · VLM · Training-free
- **[Mitigating Geospatial Knowledge Hallucination in Large Language Models: Benchmarking and Dynamic Factuality Aligning](https://doi.org/10.18653/v1/2025.findings-emnlp.45)** · Other · LLM · Training-free
- **[Mitigating Hallucinated Translations in Large Language Models with Hallucination-focused Preference Optimization](https://doi.org/10.18653/v1/2025.naacl-long.175)** · Other · LLM · Training-based
- **Mitigating Hallucination for Large Vision Language Model by Inter-Modality Correlation Calibration Decoding** · Unlabeled · VLM · Training-free
- **[Mitigating Hallucination in Large Video-Language Models with Injected Semantics](https://doi.org/10.1109/ICME59968.2025.11209977)** · Other · VLM · Training-free
- **[Mitigating Hallucination in Large Vision-Language Models through Aligning Attention Distribution to Information Flow](https://doi.org/10.18653/v1/2025.findings-emnlp.1352)** · Other · VLM · Training-free
- **[Mitigating Hallucination in Multimodal Large Language Model via Hallucination-targeted Direct Preference Optimization](https://doi.org/10.18653/v1/2025.findings-acl.850)** · Other · VLM · Training-based
- **[Mitigating Hallucination in Large Language Model by Leveraging Decoder Layer Contrasting](https://doi.org/10.1007/978-3-031-78498-9_4)** · Other · LLM · Training-free
- **[Mitigating Hallucination Through Theory-Consistent Symmetric Multimodal Preference Optimization](http://papers.nips.cc/paper_files/paper/2025/hash/a1718f361df32ff3a1fc224f8673c556-Abstract-Conference.html)** · Unlabeled · VLM · Training-based
- **Mitigating Hallucinations in Large Vision-Language Models by Adaptively Constraining Information Flow** · Unlabeled · VLM · Training-free
- **[Mitigating Hallucinations in Large Vision-Language Models by Self-Injecting Hallucinations](https://doi.org/10.18653/v1/2025.findings-emnlp.746)** · Other · VLM · Training-free
- **[Mitigating Hallucinations in Large Vision-Language Models via DPO: On-Policy Data Hold the Key](https://openaccess.thecvf.com/content/CVPR2025/html/Yang_Mitigating_Hallucinations_in_Large_Vision-Language_Models_via_DPO_On-Policy_Data_CVPR_2025_paper.html)** · Unlabeled · VLM · Training-based
- **[Mitigating Hallucinations in Large Vision-Language Models via Reasoning Uncertainty-Guided Refinement](https://ieeexplore.ieee.org/document/11125489/)** · Unlabeled · VLM · Training-free
- **[Mitigating Hallucinations in Large Vision-Language Models via Summary-Guided Decoding](https://doi.org/10.18653/v1/2025.findings-naacl.235)** · Other · VLM · Training-free
- **[Mitigating Hallucinations in LM-Based TTS Models via Distribution Alignment Using GFlowNets](https://doi.org/10.18653/v1/2025.emnlp-main.976)** · Other · LLM · Training-free
- **[Mitigating Hallucinations in Multi-modal Large Language Models via Image Token Attention-Guided Decoding](https://doi.org/10.18653/v1/2025.naacl-long.75)** · Other · VLM · Training-free
- **[Mitigating Hallucinations in Multimodal Spatial Relations through Constraint-Aware Prompting](https://doi.org/10.18653/v1/2025.findings-naacl.192)** · Other · VLM · Training-free
- **[Mitigating Hallucinations in Vision-Language Models through Image-Guided Head Suppression](https://doi.org/10.18653/v1/2025.emnlp-main.631)** · Other · VLM · Training-free
- **[Mitigating Hallucinations on Object Attributes using Multiview Images and Negative Instructions](https://doi.org/10.1109/ICASSP49660.2025.10888481)** · Other · VLM · Training-free
- **[Mitigating Object Hallucination in Large Vision-Language Models via Visual Attention Direct Preference Optimization](https://doi.org/10.1109/ICME59968.2025.11209127)** · Other · VLM · Training-based
- **[Mitigating Object Hallucination in MLLMs via Data-augmented Phrase-level Alignment](https://openreview.net/forum?id=yG1fW8igzP)** · Unlabeled · VLM · Training-free
- **Mitigating Object Hallucinations in Large Vision-Language Models with Assembly of Global and Local Attention** · Unlabeled · VLM · Training-free
- **[MixHD: A Method for Detecting Hallucinations Based on the Internal State and Output Probability of Large Language Models](https://doi.org/10.1109/ICASSP49660.2025.10889328)** · Other · LLM · Training-free
- **MoLE: Decoding by Mixture of Layer Experts Alleviates Hallucination in Large Vision-Language Models** · Unlabeled · VLM · Training-free
- **[Monitoring Decoding: Mitigating Hallucination via Evaluating the Factuality of Partial Response during Generation](https://doi.org/10.18653/v1/2025.findings-acl.752)** · Other · LLM · Training-free
- **[More Thinking, Less Seeing? Assessing Amplified Hallucination in Multimodal Reasoning Models](http://papers.nips.cc/paper_files/paper/2025/hash/777db387a5ccb131ba8c7cd155166b85-Abstract-Conference.html)** · Unlabeled · VLM · Training-free
- **[MPI-CD: Multi-Path Information Contrastive Decoding for Mitigating Hallucinations in Large Vision-Language Models](https://doi.org/10.1145/3746027.3755372)** · Other · VLM · Training-free
- **[MRFD: Multi-Region Fusion Decoding with Self-Consistency for Mitigating Hallucinations in LVLMs](https://doi.org/10.18653/v1/2025.findings-emnlp.858)** · Other · VLM · Training-free
- **[Multi-Frequency Contrastive Decoding: Alleviating Hallucinations for Large Vision-Language Models](https://doi.org/10.18653/v1/2025.emnlp-main.1452)** · Other · VLM · Training-free
- **[Not all Hallucinations are Good to Throw Away When it Comes to Legal Abstractive Summarization](https://doi.org/10.18653/v1/2025.naacl-long.275)** · Other · LLM · Training-free
- **[NoVo: Norm Voting off Hallucinations with Attention Heads in Large Language Models](https://openreview.net/forum?id=yaOe2xBcLC)** · Unlabeled · LLM · Training-free
- **Nullu: Mitigating Object Hallucinations in Large Vision-Language Models via HalluSpace Projection** · Unlabeled · VLM · Training-free
- **[ODE: Open-Set Evaluation of Hallucinations in Multimodal Large Language Models](https://openaccess.thecvf.com/content/CVPR2025/html/Tu_ODE_Open-Set_Evaluation_of_Hallucinations_in_Multimodal_Large_Language_Models_CVPR_2025_paper.html)** · Unlabeled · VLM · Training-free
- **[On A Scale From 1 to 5: Quantifying Hallucination in Faithfulness Evaluation](https://doi.org/10.18653/v1/2025.findings-naacl.433)** · Other · LLM · Training-free
- **[On Epistemic Uncertainty of Visual Tokens for Object Hallucinations in Large Vision-Language Models](http://papers.nips.cc/paper_files/paper/2025/hash/bd6673d95a2a994a5647dca1df91a000-Abstract-Conference.html)** · Unlabeled · VLM · Training-free
- **[On Reducing Factual Hallucinations in Graph-to-Text Generation Using Large Language Models](https://aclanthology.org/2025.genaik-1.5/)** · ACL · LLM · Training-free
- **[One SPACE to Rule Them All: Jointly Mitigating Factuality and Faithfulness Hallucinations in LLMs](http://papers.nips.cc/paper_files/paper/2025/hash/e77d684aae157abd84df1eeb76d8b9cd-Abstract-Conference.html)** · Unlabeled · LLM · Training-free
- **[Paying More Attention to Image: A Training-Free Method for Alleviating Hallucination in LVLMs](https://link.springer.com/10.1007/978-3-031-73010-8_8)** · Other · VLM · Training-free
- **[Persona Vectors in Controlling Hallucination of Small Large Language Models: A Safety-Oriented Analysis](https://doi.org/10.1109/cars67163.2025.11337402)** · Other · LLM · Training-free
- **📋 [PHANTOM: A Benchmark for Hallucination Detection in Financial Long-Context QA](http://papers.nips.cc/paper_files/paper/2025/hash/b8badadce3f482ba340ff870f4894441-Abstract-Datasets_and_Benchmarks_Track.html)** · Unlabeled · LLM · Training-free
- **📋 [PhD: A ChatGPT-Prompted Visual Hallucination Evaluation Dataset](https://openaccess.thecvf.com/content/CVPR2025/html/Liu_PhD_A_ChatGPT-Prompted_Visual_Hallucination_Evaluation_Dataset_CVPR_2025_paper.html)** · Unlabeled · VLM · Training-free
- **[RaDIO: Real-Time Hallucination Detection with Contextual Index Optimized Query Formulation for Dynamic Retrieval Augmented Generation](https://doi.org/10.1609/aaai.v39i24.34809)** · Other · LLM · Training-free
- **[RAG Technology for Reliable Medical Retrieval and Hallucination Mitigation](https://doi.org/10.1109/ccnis69465.2025.00009)** · Other · LLM · Training-free
- **RAR: Reversing Visual Attention Re-sinking for Unlocking Potential in Multimodal Large Language Models** · Unlabeled · VLM · Training-free
- **[RARR Unraveled: Component-Level Insights into Hallucination Detection and Mitigation](https://doi.org/10.1145/3726302.3730337)** · Other · LLM · Training-free
- **[ReDeEP: Detecting Hallucination in Retrieval-Augmented Generation via Mechanistic Interpretability](https://openreview.net/forum?id=ztzZDzgfrh)** · Unlabeled · LLM · Training-free
- **[Reducing extrinsic hallucination in multimodal abstractive summaries with post-processing technique](https://doi.org/10.1007/s00521-024-10895-8)** · Other · VLM · Training-free
- **[Reducing Hallucinations in Large Vision-Language Models via Latent Space Steering](https://openreview.net/forum?id=LBl7Hez0fF)** · Unlabeled · VLM · Training-free
- **Reducing Hallucinations in Vision-Language Models via Latent Space Steering** · Unlabeled · VLM · Training-free
- **[Reducing Tool Hallucination via Reliability Alignment](https://proceedings.mlr.press/v267/xu25ap.html)** · Unlabeled · LLM · Training-free
- **[Regularized Contrastive Decoding with Hard Negative Samples for LLM Hallucination Mitigation](https://doi.org/10.18653/v1/2025.findings-emnlp.322)** · Other · LLM · Training-free
- **[ReLoop: &quot;Seeing Twice and Thinking Backwards&quot; via Closed-loop Training to Mitigate Hallucinations in Multimodal understanding](https://doi.org/10.18653/v1/2025.findings-emnlp.222)** · Other · VLM · Training-free
- **[Removal of Hallucination on Hallucination: Debate-Augmented RAG](https://doi.org/10.18653/v1/2025.acl-long.770)** · Other · LLM · Training-free
- **[Representation-based Broad Hallucination Detectors Fail to Generalize Out of Distribution](https://doi.org/10.18653/v1/2025.findings-emnlp.952)** · Other · LLM · Training-free
- **📋 [ReSelfVerMM: mitigating hallucination in multimodal LLMs through dataset reconstruction and self-verification](https://doi.org/10.1117/12.3072360)** · Other · VLM · Training-free
- **[ReXTrust: A Model for Fine-Grained Hallucination Detection in AI-Generated Radiology Reports](https://proceedings.mlr.press/v281/hardy25a.html)** · Unlabeled · LLM · Training-free
- **[Robust Hallucination Detection in LLMs via Adaptive Token Selection](http://papers.nips.cc/paper_files/paper/2025/hash/b7c43d4a79dede363a2d061c6158e5a5-Abstract-Conference.html)** · Unlabeled · LLM · Training-free
- **[RoleBreak: Character Hallucination as a Jailbreak Attack in Role-Playing Systems](https://aclanthology.org/2025.coling-main.494/)** · ACL · LLM · Training-free
- **[Rowen: Adaptive Retrieval-Augmented Generation for Hallucination Mitigation in LLMs](https://doi.org/10.1145/3767695.3769500)** · Other · LLM · Training-free
- **[RRHF-V: Ranking Responses to Mitigate Hallucinations in Multimodal Large Language Models with Human Feedback](https://aclanthology.org/2025.coling-main.454/)** · ACL · VLM · Training-free
- **[S-AI-ANTI HALLUCINATION: A BIO-INSPIRED AND CONFIDENCE-AWARE SPARSE AI FRAMEWORK FOR RELIABLE GENERATIVE SYSTEMS](https://doi.org/10.5121/ijaia.2025.16601)** · Other · LLM · Training-free
- **[SAFE: A Sparse Autoencoder-Based Framework for Robust Query Enrichment and Hallucination Mitigation in LLMs](https://doi.org/10.18653/v1/2025.findings-emnlp.496)** · Other · LLM · Training-free
- **[SECA: Semantically Equivalent and Coherent Attacks for Eliciting LLM Hallucinations](http://papers.nips.cc/paper_files/paper/2025/hash/d077bc9ea82a2998ca6b2d0158b5ac6e-Abstract-Conference.html)** · Unlabeled · LLM · Training-free
- **[See Different, Think Better: Visual Variations Mitigating Hallucinations in LVLMs](https://doi.org/10.1145/3746027.3755044)** · Other · VLM · Training-free
- **[Seeing Beyond Hallucinations: LLM-based Compositional Information Extraction for Multimodal Reasoning](https://doi.org/10.1145/3726302.3730081)** · Other · VLM · Training-free
- **Seeing Far and Clearly: Mitigating Hallucinations in MLLMs with Attention Causal Decoding** · Unlabeled · VLM · Training-free
- **📋 [SHALE: A Scalable Benchmark for Fine-grained Hallucination Evaluation in LVLMs](https://doi.org/10.1145/3746027.3758308)** · Other · VLM · Training-free
- **Shallow Focus, Deep Fixes: Enhancing Shallow Layers Vision Attention Sinks to Alleviate Hallucination in LVLMs** · Unlabeled · VLM · Training-free
- **[SHARP: Steering Hallucination in LVLMs via Representation Engineering](https://doi.org/10.18653/v1/2025.emnlp-main.725)** · Other · VLM · Training-free
- **[SHIFT: Smoothing Hallucinations by Information Flow Tuning for Multimodal Large Language Models](https://doi.org/10.1109/ICCV51701.2025.00347)** · Other · VLM · Training-free
- **[Simple Factuality Probes Detect Hallucinations in Long-Form Natural Language Generation](https://doi.org/10.18653/v1/2025.findings-emnlp.880)** · Other · LLM · Training-free
- **[SSCM: Self-Supervised Critical Model for Reducing Hallucinations in Chinese Financial Text Generation](https://doi.org/10.1109/ICASSP49660.2025.10887684)** · Other · LLM · Training-free
- **[Steer LLM Latents for Hallucination Detection](https://proceedings.mlr.press/v267/park25a.html)** · Unlabeled · LLM · Training-free
- **[Stochastic Chameleons: Irrelevant Context Hallucinations Reveal Class-Based (Mis)Generalization in LLMs](https://doi.org/10.18653/v1/2025.acl-long.1458)** · Other · LLM · Training-free
- **[Stop Learning it all to Mitigate Visual Hallucination, Focus on the Hallucination Target](https://openaccess.thecvf.com/content/CVPR2025/html/Yoon_Stop_Learning_it_all_to_Mitigate_Visual_Hallucination_Focus_on_CVPR_2025_paper.html)** · Unlabeled · VLM · Training-free
- **[Synthetic Data in AI: Performance Gains versus Hallucination Risk](https://doi.org/10.47852/bonviewaia52026620)** · Other · LLM · Training-free
- **[Synthetic Paths to Integral Truth: Mitigating Hallucinations Caused by Confirmation Bias with Synthetic Data](https://aclanthology.org/2025.coling-main.347/)** · ACL · LLM · Training-free
- **[Systematic Reward Gap Optimization for Mitigating VLM Hallucinations](http://papers.nips.cc/paper_files/paper/2025/hash/a63ce8e6867a1bf4b4ca62e5077814d9-Abstract-Conference.html)** · Unlabeled · VLM · Training-free
- **[Teaching Audio-Aware Large Language Models What Does Not Hear: Mitigating Hallucinations through Synthesized Negative Samples](https://doi.org/10.21437/Interspeech.2025-324)** · Other · MLLM(Omni) · Training-free
- **[Temporal Insight Enhancement: Mitigating Temporal Hallucination in Video Understanding by Multimodal Large Language Models](https://doi.org/10.1007/978-3-031-78183-4_29)** · Other · VLM · Training-free
- **[The Curse of Multi-Modalities: Evaluating Hallucinations of Large Multimodal Models across Language, Visual, and Audio](http://papers.nips.cc/paper_files/paper/2025/hash/9b0b18a77421d45d26c3df5612caefe7-Abstract-Datasets_and_Benchmarks_Track.html)** · Unlabeled · MLLM(Omni) · Training-free
- **[The hallucination problem in Generative Artificial Intelligence: accuracy and trust in digital learning](https://doi.org/10.58503/icvl-v20y202503)** · Other · LLM · Training-free
- **[The Hallucination Tax of Reinforcement Finetuning](https://doi.org/10.18653/v1/2025.findings-emnlp.112)** · Other · LLM · Training-free
- **[The Hidden Life of Tokens: Reducing Hallucination of Large Vision-Language Models Via Visual Information Steering](https://proceedings.mlr.press/v267/li25ca.html)** · Unlabeled · VLM · Training-free
- **[The Illusion of Progress: Re-evaluating Hallucination Detection in LLMs](https://doi.org/10.18653/v1/2025.emnlp-main.1761)** · Other · LLM · Training-free
- **[The Impact of Negated Text on Hallucination with Large Language Models](https://doi.org/10.18653/v1/2025.emnlp-main.684)** · Other · LLM · Training-free
- **[The Law of Knowledge Overshadowing: Towards Understanding, Predicting and Preventing LLM Hallucination](https://doi.org/10.18653/v1/2025.findings-acl.1199)** · Other · LLM · Training-free
- **[Think More, Hallucinate Less: Mitigating Hallucinations via Dual Process of Fast and Slow Thinking](https://doi.org/10.18653/v1/2025.findings-acl.417)** · Other · LLM · Training-free
- **[Token Preference Optimization with Self-Calibrated Visual-Anchored Rewards for Hallucination Mitigation](https://doi.org/10.18653/v1/2025.findings-emnlp.1076)** · Other · VLM · Training-based
- **[Toward Reliable Scientific Hypothesis Generation: Evaluating Truthfulness and Hallucination in Large Language Models](https://doi.org/10.24963/ijcai.2025/873)** · Other · LLM · Training-free
- **[Towards Detecting LLMs Hallucination via Markov Chain-based Multi-agent Debate Framework](https://doi.org/10.1109/ICASSP49660.2025.10889448)** · Other · LLM · Training-free
- **[Towards Long Context Hallucination Detection](https://doi.org/10.18653/v1/2025.findings-naacl.436)** · Other · LLM · Training-free
- **[Towards Understanding Text Hallucination of Diffusion Models via Local Generation Bias](https://openreview.net/forum?id=SKW10XJlAI)** · Unlabeled · LLM · Training-free
- **[Treble Counterfactual VLMs: A Causal Approach to Hallucination](https://doi.org/10.18653/v1/2025.findings-emnlp.1000)** · Other · VLM · Training-free
- **[Trucidator: Document-level Event Factuality Identification via Hallucination Enhancement and Cross-Document Inference](https://aclanthology.org/2025.coling-main.139/)** · ACL · LLM · Training-free
- **[Trustworthy Information Retrieval in the LLM Era: Bias, Unfairness, and Hallucination](https://doi.org/10.1145/3767695.3769670)** · Other · LLM · Training-free
- **[Trustworthy Medical Imaging with Large Language Models: A Study of Hallucinations Across Modalities](https://doi.org/10.1109/ICCVW69036.2025.00136)** · Other · LLM · Training-free
- **[TruthPrInt: Mitigating Large Vision-Language Models Object Hallucination via Latent Truthful-Guided Pre-Intervention](https://doi.org/10.1109/ICCV51701.2025.00692)** · Other · VLM · Training-free
- **[Uncertainty-Aware Fusion: An Ensemble Framework for Mitigating Hallucinations in Large Language Models](https://doi.org/10.1145/3701716.3715523)** · Other · LLM · Training-free
- **Understanding and Mitigating Hallucination in Large Vision-Language Models via Modular Attribution and Intervention** · Unlabeled · VLM · Training-free
- **[Understanding Visual Detail Hallucinations of Large Vision-Language Models](https://doi.org/10.24963/ijcai.2025/212)** · Other · VLM · Training-free
- **[Unsupervised Hallucination Detection by Inspecting Reasoning Processes](https://doi.org/10.18653/v1/2025.emnlp-main.1124)** · Other · LLM · Training-free
- **[VADE: Visual Attention Guided Hallucination Detection and Elimination](https://doi.org/10.18653/v1/2025.findings-acl.773)** · Other · VLM · Training-free
- **VASparse: Towards Efficient Visual Hallucination Mitigation via Visual-Aware Token Sparsification** · Unlabeled · VLM · Training-free
- **[VideoHallu: Evaluating and Mitigating Multi-modal Hallucinations on Synthetic Video Understanding](http://papers.nips.cc/paper_files/paper/2025/hash/6e1734c47c0cc899021060d88f69dc65-Abstract-Conference.html)** · Unlabeled · VLM · Training-free
- **[VidHalluc: Evaluating Temporal Hallucinations in Multimodal Large Language Models for Video Understanding](https://openaccess.thecvf.com/content/CVPR2025/html/Li_VidHalluc_Evaluating_Temporal_Hallucinations_in_Multimodal_Large_Language_Models_for_CVPR_2025_paper.html)** · Unlabeled · VLM · Training-free
- **Visual Evidence Prompting Mitigates Hallucinations in Large Vision-Language Models** · Unlabeled · VLM · Training-free
- **[Visual Perception Uncertainty Learning for Hallucination Detection in Large Vision-Language Models](https://doi.org/10.1145/3746027.3755126)** · Other · VLM · Training-free
- **[VLM3KG:A Hallucination Mitigation Method for Vision-Language Models based on Multimodal Knowledge Graph](https://doi.org/10.1109/mlprae67267.2025.11290735)** · Other · VLM · Training-free
- **[VoiceNoNG: Robust High-Quality Speech Editing Model without Hallucinations](https://doi.org/10.21437/Interspeech.2025-431)** · Other · MLLM(Omni) · Training-free
- **[When Models Lie, We Learn: Multilingual Span-Level Hallucination Detection with PsiloQA](https://doi.org/10.18653/v1/2025.findings-emnlp.626)** · Other · LLM · Training-free
- **[Who Brings the Frisbee: Probing Hidden Hallucination Factors in Large Vision-Language Model via Causality Analysis](https://doi.org/10.1109/WACV61041.2025.00597)** · Other · VLM · Training-free
- **[Wisdom is Knowing What not to Say: Hallucination-Free LLMs Unlearning via Attention Shifting](http://papers.nips.cc/paper_files/paper/2025/hash/8eb3e953455f01ebbd83d7df351bdf95-Abstract-Conference.html)** · Unlabeled · LLM · Training-based
- **[WITHDRAWN: Ambiguity processing in Large Language Models: Detection, resolution, and the path to hallucination](https://doi.org/10.1016/j.nlp.2025.100173)** · Other · LLM · Training-free
- **[Zero-knowledge LLM hallucination detection and mitigation through fine-grained cross-model consistency](https://doi.org/10.18653/v1/2025.emnlp-industry.139)** · Other · LLM · Training-free
- **[Zero-resource Hallucination Detection for Text Generation via Graph-based Contextual Knowledge Triples Modeling](https://doi.org/10.1609/aaai.v39i22.34559)** · Other · LLM · Training-free
- **📚 [🧜Siren’s Song in the AI Ocean: A Survey on Hallucination in Large Language Models](https://doi.org/10.1162/coli.a.16)** · Other · LLM · Training-free

</details>

<details>
<summary>📅 2024 · 220 papers</summary>

- **[Verb Mirage: Unveiling and Assessing Verb Concept Hallucinations in Multimodal Large Language Models](https://arxiv.org/abs/2412.04939)** · arXiv · VLM · Training-free
- **[Hallucination Elimination and Semantic Enhancement Framework for Vision-Language Models in Traffic Scenarios](https://arxiv.org/abs/2412.07518)** · arXiv · VLM · Training-free
- **[Cracking the Code of Hallucination in LVLMs with Vision-aware Head Divergence](https://arxiv.org/abs/2412.13949)** · arXiv · VLM · Training-free
- **[Toward Robust Hyper-Detailed Image Captioning: A Multiagent Approach and Dual Evaluation Metrics for Factuality and Coverage](https://arxiv.org/abs/2412.15484)** · arXiv · VLM · Training-free
- **[VORD: Visual Ordinal Calibration for Mitigating Object Hallucinations in Large Vision-Language Models](https://arxiv.org/abs/2412.15739)** · arXiv · VLM · Training-free
- **[Layer Importance and Hallucination Analysis in Large Language Models via Enhanced Activation Variance-Sparsity](https://arxiv.org/abs/2411.10069)** · arXiv · LLM · Training-free
- **[Seeing Clearly by Layer Two: Enhancing Attention Heads to Alleviate Hallucination in LVLMs](https://arxiv.org/abs/2411.09968)** · arXiv · VLM · Training-free
- **[Devils in Middle Layers of Large Vision-Language Models: Interpreting, Detecting and Mitigating Object Hallucinations via Attention Lens](https://arxiv.org/abs/2411.16724)** · arXiv · VLM · Training-free
- **[VaLiD: Mitigating the Hallucination of Large Vision Language Models by Visual Layer Fusion Contrastive Decoding](https://arxiv.org/abs/2411.15839)** · arXiv · VLM · Training-free
- **[Look Twice Before You Answer: Memory-Space Visual Retracing for Hallucination Mitigation in Multimodal Large Language Models](https://arxiv.org/abs/2410.03577)** · arXiv · VLM · Training-free
- **[Unraveling Cross-Modality Knowledge Conflict in Large Vision-Language Models](https://arxiv.org/abs/2410.03659)** · arXiv · VLM · Training-free
- **[Mitigating Modality Prior-Induced Hallucinations in Multimodal Large Language Models via Deciphering Attention Causality](https://arxiv.org/abs/2410.04780)** · arXiv · VLM · Training-free
- **[Insight Over Sight: Exploring the Vision-Knowledge Conflicts in Multimodal LLMs](https://arxiv.org/abs/2410.08145)** · arXiv · VLM · Training-free
- **[MLLM can see? Dynamic Correction Decoding for Hallucination Mitigation](https://arxiv.org/abs/2410.11779)** · arXiv · VLM · Training-free
- **[Unified Triplet-Level Hallucination Evaluation for Large Vision-Language Models](https://arxiv.org/abs/2410.23114)** · arXiv · VLM · Training-free
- **[Understanding Multimodal Hallucination with Parameter-Free Representation Alignment](https://arxiv.org/abs/2409.01151)** · arXiv · VLM · Training-free
- **[Mitigating Hallucination in Visual-Language Models via Re-Balancing Contrastive Decoding](https://arxiv.org/abs/2409.06485)** · arXiv · VLM · Training-free
- **[LLMs Can Check Their Own Results to Mitigate Hallucinations in Traffic Understanding Tasks](https://arxiv.org/abs/2409.12580)** · arXiv · VLM · Training-free
- **[DENEB: A Hallucination-Robust Automatic Evaluation Metric for Image Captioning](https://arxiv.org/abs/2409.19255)** · arXiv · VLM · Training-free
- **[VACoDe: Visual Augmented Contrastive Decoding](https://arxiv.org/abs/2408.05337)** · arXiv · VLM · Training-free
- **[Mitigating Multilingual Hallucination in Large Vision-Language Models](https://arxiv.org/abs/2408.00550)** · arXiv · VLM · Training-based
- **[Self-Introspective Decoding: Alleviating Hallucinations for Large Vision-Language Models](https://arxiv.org/abs/2408.02032)** · arXiv · VLM · Training-based
- **[Mitigating Hallucinations in Large Vision-Language Models (LVLMs) via Language-Contrastive Decoding (LCD)](https://arxiv.org/abs/2408.04664)** · arXiv · VLM · Training-free
- **[ConVis: Contrastive Decoding with Hallucination Visualization for Mitigating Hallucinations in Multimodal Large Language Models](https://arxiv.org/abs/2408.13906)** · arXiv · VLM · Training-free
- **[CODE: Contrasting Self-generated Description to Combat Hallucination in Large Multi-modal Models](https://arxiv.org/abs/2406.01920)** · arXiv · VLM · Training-free
- **[Do More Details Always Introduce More Hallucinations in LVLM-based Image Captioning?](https://arxiv.org/abs/2406.12663)** · arXiv · VLM · Training-free
- **[CrossCheckGPT: Universal Hallucination Ranking for Multimodal Foundation Models](https://arxiv.org/abs/2405.13684)** · arXiv · MLLM(Omni) · Training-based
- **[Visual Description Grounding Reduces Hallucinations and Boosts Reasoning in LVLMs](https://arxiv.org/abs/2405.15683)** · arXiv · VLM · Training-free
- **[Don't Miss the Forest for the Trees: Attentional Vision Calibration for Large Vision Language Models](https://arxiv.org/abs/2405.17820)** · arXiv · VLM · Training-free
- **[RITUAL: Random Image Transformations as a Universal Anti-hallucination Lever in Large Vision Language Models](https://arxiv.org/abs/2405.17821)** · arXiv · VLM · Training-free
- **[Seeing the Image: Prioritizing Visual Correlation by Contrastive Alignment](https://arxiv.org/abs/2405.17871)** · arXiv · VLM · Training-free
- **[MetaToken: Detecting Hallucination in Image Descriptions by Meta Classification](https://arxiv.org/abs/2405.19186)** · arXiv · VLM · Training-free
- **[HALC: Object Hallucination Reduction via Adaptive Focal-Contrast Decoding](https://arxiv.org/abs/2403.00425)** · arXiv · VLM · Training-free
- **[In-Context Sharpness as Alerts: An Inner Representation Perspective for Hallucination Mitigation](https://arxiv.org/abs/2403.01548)** · arXiv · LLM · Training-free
- **[Contrastive Region Guidance: Improving Grounding in Vision-Language Models without Training](https://arxiv.org/abs/2403.02325)** · arXiv · VLM · Training-free
- **[Visual Hallucination: Definition, Quantification, and Prescriptive Remediations](https://arxiv.org/abs/2403.17306)** · arXiv · VLM · Training-free
- **[Mitigating Hallucinations in Large Vision-Language Models with Instruction Contrastive Decoding](https://arxiv.org/abs/2403.18715)** · arXiv · VLM · Training-free
- **[Mitigating Object Hallucination in Large Vision-Language Models via Image-Grounded Guidance](https://arxiv.org/abs/2402.08680)** · arXiv · VLM · Training-free
- **[Logical Closed Loop: Uncovering Object Hallucinations in Large Vision-Language Models](https://arxiv.org/abs/2402.11622)** · arXiv · VLM · Training-free
- **[Seeing is Believing: Mitigating Hallucination in Large Vision-Language Models via CLIP-Guided Decoding](https://arxiv.org/abs/2402.15300)** · arXiv · VLM · Training-free
- **[IBD: Alleviating Hallucinations in Large Vision-Language Models via Image-Biased Decoding](https://arxiv.org/abs/2402.18476)** · arXiv · VLM · Training-free
- **[A Cause-Effect Look at Alleviating Hallucination of Knowledge-grounded Dialogue Generation](https://aclanthology.org/2024.lrec-main.9)** · ACL · LLM · Training-free
- **📚 [A Comprehensive Survey of Hallucination in Large Language, Image, Video and Audio Foundation Models](https://doi.org/10.18653/v1/2024.findings-emnlp.685)** · Other · MLLM(Omni) · Training-free
- **[A Culturally Sensitive Test to Evaluate Nuanced GPT Hallucination](https://doi.org/10.1109/tai.2023.3332837)** · Other · LLM · Training-free
- **[ACUEval: Fine-grained Hallucination Evaluation and Correction for Abstractive Summarization](https://doi.org/10.18653/v1/2024.findings-acl.597)** · Other · LLM · Training-free
- **AHEAD: Attention Head Energy-Aware Dynamics for Hallucination Mitigation in MLLMs** · Unlabeled · VLM · Training-free
- **[AIGCs Confuse AI Too: Investigating and Explaining Synthetic Image-induced Hallucinations in Large Vision-Language Models](https://doi.org/10.1145/3664647.3681467)** · Other · VLM · Training-free
- **[AILS-NTUA at SemEval-2024 Task 6: Efficient model tuning for hallucination detection and analysis](https://doi.org/10.18653/v1/2024.semeval-1.222)** · Other · LLM · Training-free
- **[Alleviating Action Hallucination for LLM-based Embodied Agents via Inner and Outer Alignment](https://doi.org/10.1109/prai62207.2024.10826957)** · Other · LLM · Training-free
- **[Alleviating Hallucinations in Large Vision-Language Models through Hallucination-Induced Optimization](http://papers.nips.cc/paper_files/paper/2024/hash/dde040998d82553cf7f689e8ae173d5a-Abstract-Conference.html)** · Unlabeled · VLM · Training-free
- **[Alleviating Hallucinations Via Supportive Window Indexing in Abstractive Summarization](https://doi.org/10.1109/ICASSP48485.2024.10446022)** · Other · LLM · Training-free
- **[ALOHa: A New Measure for Hallucination in Captioning Models](https://doi.org/10.18653/v1/2024.naacl-short.30)** · Other · LLM · Training-free
- **[AlphaIntellect at SemEval-2024 Task 6: Detection of Hallucinations in Generated Text](https://doi.org/10.18653/v1/2024.semeval-1.137)** · Other · LLM · Training-free
- **[An Audit on the Perspectives and Challenges of Hallucinations in NLP](https://doi.org/10.18653/v1/2024.emnlp-main.375)** · Other · LLM · Training-free
- **[ANAH-v2: Scaling Analytical Hallucination Annotation of Large Language Models](http://papers.nips.cc/paper_files/paper/2024/hash/6e4cdfdd909ea4e34bfc85a12774cba0-Abstract-Conference.html)** · Unlabeled · LLM · Training-free
- **[Analyzing and Mitigating Object Hallucination in Large Vision-Language Models](https://openreview.net/forum?id=oZDJKTlOUe)** · Unlabeled · VLM · Training-free
- **[Ask, Assess, and Refine: Rectifying Factual Consistency and Hallucination in LLMs with Metric-Guided Feedback Learning](https://doi.org/10.18653/v1/2024.eacl-long.149)** · Other · LLM · Training-free
- **[AutoHallusion: Automatic Generation of Hallucination Benchmarks for Vision-Language Models](https://doi.org/10.18653/v1/2024.findings-emnlp.493)** · Other · VLM · Training-free
- **[BEAF: Observing BEfore-AFter Changes to Evaluate Hallucination in Vision-Language Models](https://doi.org/10.1007/978-3-031-73247-8_14)** · Other · VLM · Training-free
- **[Benchmarking Hallucination in Large Language Models Based on Unanswerable Math Word Problem](https://aclanthology.org/2024.lrec-main.196)** · ACL · LLM · Training-free
- **[BrainLlama at SemEval-2024 Task 6: Prompting Llama to detect hallucinations and related observable overgeneration mistakes](https://doi.org/10.18653/v1/2024.semeval-1.14)** · Other · LLM · Training-free
- **[Can Hallucination Reduction in LLMs Improve Online Sexism Detection?](https://doi.org/10.1007/978-3-031-66329-1_40)** · Other · LLM · Training-free
- **📚 [Can Knowledge Graphs Reduce Hallucinations in LLMs? : A Survey](https://doi.org/10.18653/v1/2024.naacl-long.219)** · Other · LLM · Training-free
- **CausalLens: Sensitivity-Guided Multi-Head Causal Intervention for Hallucination Mitigation in Large Vision-Language Models** · Unlabeled · VLM · Training-free
- **[CLIP-DPO: Vision-Language Models as a Source of Preference for Fixing Hallucinations in LVLMs](https://doi.org/10.1007/978-3-031-73116-7_23)** · Other · VLM · Training-based
- **[Coarse-to-Fine Highlighting: Reducing Knowledge Hallucination in Large Language Models](https://proceedings.mlr.press/v235/lv24c.html)** · Unlabeled · LLM · Training-free
- **📚 [Cognitive Mirage: A Review of Hallucinations in Large Language Models](https://ceur-ws.org/Vol-3818/paper2.pdf)** · Unlabeled · LLM · Training-free
- **[Combating Visual Question Answering Hallucinations via Robust Multi-Space Co-Debias Learning](https://doi.org/10.1145/3664647.3681663)** · Other · VLM · Training-free
- **[Compos Mentis at SemEval2024 Task6: A Multi-Faceted Role-based Large Language Model Ensemble to Detect Hallucination](https://doi.org/10.18653/v1/2024.semeval-1.208)** · Other · LLM · Training-free
- **Contrastive Decoding Reduces Hallucinations in Large Multilingual Machine Translation Models** · Unlabeled · LLM · Training-free
- **COPO: Causal-Oriented Policy Optimization for Hallucinations of MLLMs** · Unlabeled · VLM · Training-based
- **[Correcting Factuality Hallucination in Complaint Large Language Model via Entity-Augmented](https://doi.org/10.1109/ijcnn60899.2024.10650208)** · Other · LLM · Training-free
- **Counterfactual Segmentation Reasoning: Diagnosing and Mitigating Pixel-Grounding Hallucination** · Unlabeled · LLM · Training-free
- **[DAMRO: Dive into the Attention Mechanism of LVLM to Reduce Object Hallucination](https://aclanthology.org/2024.emnlp-main.439)** · ACL · VLM · Training-free
- **[Deceptive Semantic Shortcuts on Reasoning Chains: How Far Can Models Go without Hallucination?](https://doi.org/10.18653/v1/2024.naacl-long.424)** · Other · LLM · Training-free
- **[DeepPavlov at SemEval-2024 Task 6: Detection of Hallucinations and Overgeneration Mistakes with an Ensemble of Transformer-based Models](https://doi.org/10.18653/v1/2024.semeval-1.42)** · Other · LLM · Training-free
- **[Detecting and Preventing Hallucinations in Large Vision Language Models](https://doi.org/10.1609/aaai.v38i16.29771)** · Other · VLM · Training-free
- **[Detecting Hallucination and Coverage Errors in Retrieval Augmented Generation for Controversial Topics](https://aclanthology.org/2024.lrec-main.423)** · ACL · LLM · Training-free
- **📋 [Detection, Diagnosis, and Explanation: A Benchmark for Chinese Medial Hallucination Evaluation](https://aclanthology.org/2024.lrec-main.428)** · ACL · LLM · Training-free
- **📋 [DiaHalu: A Dialogue-level Hallucination Evaluation Benchmark for Large Language Models](https://doi.org/10.18653/v1/2024.findings-emnlp.529)** · Other · LLM · Training-free
- **DiVE: Decoupling Intra-layer Visual Evidence for Mitigating Hallucinations in Large Vision-Language Models** · Unlabeled · VLM · Training-free
- **[Does Fine-Tuning LLMs on New Knowledge Encourage Hallucinations?](https://doi.org/10.18653/v1/2024.emnlp-main.444)** · Other · LLM · Training-free
- **[Does Object Grounding Really Reduce Hallucination of Large Vision-Language Models?](https://doi.org/10.18653/v1/2024.emnlp-main.159)** · Other · VLM · Training-free
- **[DUTh at SemEval-2024 Task 6: Comparing Pre-trained Models on Sentence Similarity Evaluation for Detecting of Hallucinations and Related Observable Overgeneration Mistakes](https://doi.org/10.18653/v1/2024.semeval-1.154)** · Other · LLM · Training-free
- **[EFUF: Efficient Fine-Grained Unlearning Framework for Mitigating Hallucinations in Multimodal Large Language Models](https://doi.org/10.18653/v1/2024.emnlp-main.67)** · Other · VLM · Training-based
- **ELV-Halluc: Benchmarking Semantic Aggregation Hallucinations in Video Understanding** · Unlabeled · VLM · Training-free
- **[Embedding and Gradient Say Wrong: A White-Box Method for Hallucination Detection](https://doi.org/10.18653/v1/2024.emnlp-main.116)** · Other · LLM · Training-free
- **[Enhanced Hallucination Detection in Neural Machine Translation through Simple Detector Aggregation](https://doi.org/10.18653/v1/2024.emnlp-main.1033)** · Other · LLM · Training-free
- **[Enhancing Hallucination Detection through Perturbation-Based Synthetic Data Generation in System Responses](https://doi.org/10.18653/v1/2024.findings-acl.789)** · Other · LLM · Training-free
- **Envision, Attend, Then Respond: Counterfactual Hallucination Mitigation in Large Vision-Language Models** · Unlabeled · VLM · Training-free
- **📋 [ERBench: An Entity-Relationship based Automatically Verifiable Hallucination Benchmark for Large Language Models](http://papers.nips.cc/paper_files/paper/2024/hash/5ef9853a6cdea40ae3e301a6d8dc32b5-Abstract-Datasets_and_Benchmarks_Track.html)** · Unlabeled · LLM · Training-free
- **[Estimating the Hallucination Rate of Generative AI](http://papers.nips.cc/paper_files/paper/2024/hash/3791f5fc0e8e43730466afd2bcdb7493-Abstract-Conference.html)** · Unlabeled · LLM · Training-free
- **[Evaluating and Analyzing Relationship Hallucinations in Large Vision-Language Models](https://proceedings.mlr.press/v235/wu24l.html)** · Unlabeled · VLM · Training-free
- **[Evaluating Hallucination in Medical Prompt Responses: A Comparative Study of ChatGPT-4 and ChatGPT-4o](https://doi.org/10.1109/comnetsat63286.2024.10862480)** · Other · LLM · Training-free
- **[Explicitly Stating Assumptions Reduces Hallucinations in Natural Language Inference](https://openreview.net/forum?id=eJI9pfNwBS)** · Unlabeled · LLM · Training-free
- **[Exploiting Semantic Reconstruction to Mitigate Hallucinations in Vision-Language Models](https://doi.org/10.1007/978-3-031-73016-0_14)** · Other · VLM · Training-free
- **[FactCHD: Benchmarking Fact-Conflicting Hallucination Detection](https://www.ijcai.org/proceedings/2024/687)** · Unlabeled · LLM · Training-free
- **[FaithScore: Fine-grained Evaluations of Hallucinations in Large Vision-Language Models](https://doi.org/10.18653/v1/2024.findings-emnlp.290)** · Other · VLM · Training-free
- **Fighting Hallucinations with Counterfactuals: Diffusion-Guided Perturbations for LVLM Hallucination Suppression** · Unlabeled · VLM · Training-free
- **📋 Fine-Grained Multi Image Object Hallucination Benchmark** · Unlabeled · VLM · Training-free
- **[Game on Tree: Visual Hallucination Mitigation via Coarse-to-Fine View Tree and Game Theory](https://doi.org/10.18653/v1/2024.emnlp-main.998)** · Other · VLM · Training-free
- **[Gemini Goes to Med School: Exploring the Capabilities of Multimodal Large Language Models on Medical Challenge Problems &amp; Hallucinations](https://doi.org/10.18653/v1/2024.clinicalnlp-1.3)** · Other · VLM · Training-free
- **Global Context or Local Detail? Adaptive Visual Grounding for Hallucination Mitigation** · Unlabeled · VLM · Training-free
- **[GraphEval: A Knowledge-Graph Based LLM Hallucination Evaluation Framework](https://ceur-ws.org/Vol-3894/paper5.pdf)** · Unlabeled · LLM · Training-free
- **HAD: Hallucination-Aware Diffusion Priors for 3D Reconstruction** · Unlabeled · LLM · Training-free
- **HAIT: Hybrid Adversarial Iterative Training for Mitigating Object Hallucination in Large Vision-Language Models** · Unlabeled · VLM · Training-based
- **[Hal-Eval: A Universal and Fine-grained Hallucination Evaluation Framework for Large Vision Language Models](https://doi.org/10.1145/3664647.3680576)** · Other · VLM · Training-free
- **[Hallo3D: Multi-Modal Hallucination Detection and Mitigation for Consistent 3D Content Generation](http://papers.nips.cc/paper_files/paper/2024/hash/d75660d6eb0ce31360c768fef85301dd-Abstract-Conference.html)** · Unlabeled · VLM · Training-free
- **[Hallu-PI: Evaluating Hallucination in Multi-modal Large Language Models within Perturbed Inputs](https://doi.org/10.1145/3664647.3681251)** · Other · VLM · Training-free
- **[Hallucination Augmented Contrastive Learning for Multimodal Large Language Model](https://doi.org/10.1109/CVPR52733.2024.02553)** · Other · VLM · Training-free
- **📋 [Hallucination Benchmark in Medical Visual Question Answering](https://openreview.net/forum?id=vxlXqOj4zv)** · Unlabeled · VLM · Training-free
- **[Hallucination Diversity-Aware Active Learning for Text Summarization](https://doi.org/10.18653/v1/2024.naacl-long.479)** · Other · LLM · Training-free
- **[HalluMeasure: Fine-grained Hallucination Measurement Using Chain-of-Thought Reasoning](https://doi.org/10.18653/v1/2024.emnlp-main.837)** · Other · LLM · Training-free
- **[HalluSafe at SemEval-2024 Task 6: An NLI-based Approach to Make LLMs Safer by Better Detecting Hallucinations and Overgeneration Mistakes](https://doi.org/10.18653/v1/2024.semeval-1.22)** · Other · LLM · Training-free
- **📋 [HaloQuest: A Visual Hallucination Dataset for Advancing Multimodal Reasoning](https://doi.org/10.1007/978-3-031-72980-5_17)** · Other · VLM · Training-free
- **[HaloScope: Harnessing Unlabeled LLM Generations for Hallucination Detection](http://papers.nips.cc/paper_files/paper/2024/hash/ba92705991cfbbcedc26e27e833ebbae-Abstract-Conference.html)** · Unlabeled · LLM · Training-free
- **[Halu-NLP at SemEval-2024 Task 6: MetaCheckGPT - A Multi-task Hallucination Detection using LLM uncertainty and meta-models](https://doi.org/10.18653/v1/2024.semeval-1.52)** · Other · LLM · Training-free
- **[Halwasa: Quantify and Analyze Hallucinations in Large Language Models: Arabic as a Case Study](https://aclanthology.org/2024.lrec-main.705)** · ACL · LLM · Training-free
- **[HaRMoNEE at SemEval-2024 Task 6: Tuning-based Approaches to Hallucination Recognition](https://doi.org/10.18653/v1/2024.semeval-1.191)** · Other · LLM · Training-free
- **[HELPD: Mitigating Hallucination of LVLMs by Hierarchical Feedback Learning with Vision-enhanced Penalty Decoding](https://doi.org/10.18653/v1/2024.emnlp-main.105)** · Other · VLM · Training-free
- **[HIT-MI&amp;T Lab at SemEval-2024 Task 6: DeBERTa-based Entailment Model is a Reliable Hallucination Detector](https://doi.org/10.18653/v1/2024.semeval-1.253)** · Other · LLM · Training-free
- **[How Language Model Hallucinations Can Snowball](https://proceedings.mlr.press/v235/zhang24ay.html)** · Unlabeled · LLM · Training-free
- **HulluEdit: Single-Pass Evidence-Consistent Subspace Editing for Mitigating Hallucinations in Large Vision-Language Models** · Unlabeled · VLM · Training-free
- **📋 [HypoTermQA: Hypothetical Terms Dataset for Benchmarking Hallucination Tendency of LLMs](https://doi.org/10.18653/v1/2024.eacl-srw.9)** · Other · LLM · Training-free
- **Inject to Heal: Alleviating hallucination in LVLMs via Context Embedding Injection** · Unlabeled · VLM · Training-free
- **[INSIDE: LLMs&apos; Internal States Retain the Power of Hallucination Detection](https://openreview.net/forum?id=Zj12nzlQbz)** · Unlabeled · LLM · Training-free
- **[Investigating and Mitigating Object Hallucinations in Pretrained Vision-Language (CLIP) Models](https://doi.org/10.18653/v1/2024.emnlp-main.1016)** · Other · VLM · Training-free
- **[IRIT-Berger-Levrault at SemEval-2024: How Sensitive Sentence Embeddings are to Hallucinations?](https://doi.org/10.18653/v1/2024.semeval-1.86)** · Other · LLM · Training-free
- **[Knowledge Verification to Nip Hallucination in the Bud](https://doi.org/10.18653/v1/2024.emnlp-main.152)** · Other · LLM · Training-free
- **[Knowledge-Centric Hallucination Detection](https://doi.org/10.18653/v1/2024.emnlp-main.395)** · Other · LLM · Training-free
- **Latent Attention Denoising: A Training-Free Energy-Based Framework for Mitigating Hallucinations in Vision-Language Models** · Unlabeled · VLM · Training-free
- **[Leveraging Hallucinations to Reduce Manual Prompt Dependency in Promptable Segmentation](http://papers.nips.cc/paper_files/paper/2024/hash/c1e1ad233411e25b54bb5df3a0576c2c-Abstract-Conference.html)** · Unlabeled · LLM · Training-free
- **[LLM Internal States Reveal Hallucination Risk Faced With a Query](https://doi.org/10.18653/v1/2024.blackboxnlp-1.6)** · Other · LLM · Training-free
- **[LLM-Check: Investigating Detection of Hallucinations in Large Language Models](http://papers.nips.cc/paper_files/paper/2024/hash/3c1e1fdf305195cd620c118aaa9717ad-Abstract-Conference.html)** · Unlabeled · LLM · Training-free
- **[Lookback Lens: Detecting and Mitigating Contextual Hallucinations in Large Language Models Using Only Attention Maps](https://doi.org/10.18653/v1/2024.emnlp-main.84)** · Other · LLM · Training-free
- **[Looks Too Good To Be True: An Information-Theoretic Analysis of Hallucinations in Generative Restoration Models](http://papers.nips.cc/paper_files/paper/2024/hash/2847d43f17410c5beb25b2736c3ae778-Abstract-Conference.html)** · Unlabeled · LLM · Training-free
- **[Machine Translation Hallucination Detection for Low and High Resource Languages using Large Language Models](https://doi.org/10.18653/v1/2024.findings-emnlp.564)** · Other · LLM · Training-free
- **MAD: Modality-Adaptive Decoding for Mitigating Cross-Modal Hallucinations in Multimodal Large Language Models** · Unlabeled · VLM · Training-free
- **[Maha Bhaashya at SemEval-2024 Task 6: Zero-Shot Multi-task Hallucination Detection](https://doi.org/10.18653/v1/2024.semeval-1.241)** · Other · LLM · Training-free
- **[MALTO at SemEval-2024 Task 6: Leveraging Synthetic Data for LLM Hallucination Detection](https://doi.org/10.18653/v1/2024.semeval-1.240)** · Other · LLM · Training-free
- **[MARiA at SemEval 2024 Task-6: Hallucination Detection Through LLMs, MNLI, and Cosine similarity](https://doi.org/10.18653/v1/2024.semeval-1.225)** · Other · LLM · Training-free
- **📋 [MASSIVE Multilingual Abstract Meaning Representation: A Dataset and Baselines for Hallucination Detection](https://doi.org/10.18653/v1/2024.starsem-1.1)** · Other · LLM · Training-free
- **[Mechanistic Understanding and Mitigation of Language Model Non-Factual Hallucinations](https://doi.org/10.18653/v1/2024.findings-emnlp.466)** · Other · LLM · Training-free
- **[Medico: Towards Hallucination Detection and Correction with Multi-source Evidence Fusion](https://doi.org/10.18653/v1/2024.emnlp-demo.4)** · Other · LLM · Training-free
- **[Mitigating Entity-Level Hallucination in Large Language Models](https://doi.org/10.1145/3673791.3698403)** · Other · LLM · Training-free
- **[Mitigating Hallucination in Abstractive Summarization with Domain-Conditional Mutual Information](https://doi.org/10.18653/v1/2024.findings-naacl.117)** · Other · LLM · Training-free
- **[Mitigating Hallucination in Fictional Character Role-Play](https://doi.org/10.18653/v1/2024.findings-emnlp.846)** · Other · LLM · Training-free
- **[Mitigating Hallucination in Large Multi-Modal Models via Robust Instruction Tuning](https://openreview.net/forum?id=J44HfH4JCg)** · Unlabeled · VLM · Training-based
- **[Mitigating Hallucination in Visual Language Model Segmentation with Negative Sampling](https://doi.org/10.1109/iscslp63861.2024.10800691)** · Other · VLM · Training-free
- **[Mitigating Hallucination Issues in Small-Parameter LLMs through Inter-Layer Contrastive Decoding](https://doi.org/10.1109/ijcnn60899.2024.10650644)** · Other · LLM · Training-free
- **[Mitigating Hallucinations and Off-target Machine Translation with Source-Contrastive and Language-Contrastive Decoding](https://doi.org/10.18653/v1/2024.eacl-short.4)** · Other · LLM · Training-free
- **Mitigating Hallucinations in Large Vision-Language Models without Performance Degradation** · Unlabeled · VLM · Training-free
- **Mitigating Hallucinations in VLMs: Enhancing Visual Attention via Head-Wise Perturbation** · Unlabeled · VLM · Training-free
- **[Mitigating Hallucinations of Large Language Models in Medical Information Extraction via Contrastive Decoding](https://doi.org/10.18653/v1/2024.findings-emnlp.456)** · Other · LLM · Training-free
- **[Mitigating Large Language Model Hallucinations via Autonomous Knowledge Graph-Based Retrofitting](https://doi.org/10.1609/aaai.v38i16.29770)** · Other · LLM · Training-free
- **Mitigating Multimodal Hallucinations via Gradient-based Self-Reflection** · Unlabeled · VLM · Training-free
- **Mitigating Object Hallucination via Concentric Causal Attention** · Unlabeled · LLM · Training-free
- **[Mitigating Open-Vocabulary Caption Hallucinations](https://doi.org/10.18653/v1/2024.emnlp-main.1263)** · Other · LLM · Training-free
- **[Multi-Modal Hallucination Control by Visual Information Grounding](https://ieeexplore.ieee.org/document/10655750/)** · Unlabeled · VLM · Training-free
- **[Multi-Object Hallucination in Vision Language Models](http://papers.nips.cc/paper_files/paper/2024/hash/4ea4a1ea4d9ff273688c8e92bd087112-Abstract-Conference.html)** · Unlabeled · VLM · Training-free
- **[Multilingual Fine-Grained News Headline Hallucination Detection](https://doi.org/10.18653/v1/2024.findings-emnlp.461)** · Other · LLM · Training-free
- **[Navigating Hallucinations for Reasoning of Unintentional Activities](https://doi.org/10.18653/v1/2024.findings-emnlp.565)** · Other · LLM · Training-free
- **[NootNoot At SemEval-2024 Task 6: Hallucinations and Related Observable Overgeneration Mistakes Detection](https://doi.org/10.18653/v1/2024.semeval-1.139)** · Other · LLM · Training-free
- **[NU-RU at SemEval-2024 Task 6: Hallucination and Related Observable Overgeneration Mistake Detection Using Hypothesis-Target Similarity and SelfCheckGPT](https://doi.org/10.18653/v1/2024.semeval-1.39)** · Other · LLM · Training-free
- **[Null-Shot Prompting: Rethinking Prompting Large Language Models With Hallucination](https://doi.org/10.18653/v1/2024.emnlp-main.740)** · Other · LLM · Training-free
- **[On Early Detection of Hallucinations in Factual Question Answering](https://doi.org/10.1145/3637528.3671796)** · Other · LLM · Training-free
- **[On Large Language Models&apos; Hallucination with Regard to Known Facts](https://doi.org/10.18653/v1/2024.naacl-long.60)** · Other · LLM · Training-free
- **Once Correct, Still Wrong: Counterfactual Hallucination in Multilingual Vision-Language Models** · Unlabeled · VLM · Training-free
- **[OPDAI at SemEval-2024 Task 6: Small LLMs can Accelerate Hallucination Detection with Weakly Supervised Data](https://doi.org/10.18653/v1/2024.semeval-1.104)** · Other · LLM · Training-free
- **[OPERA: Alleviating Hallucination in Multi-Modal Large Language Models via Over-Trust Penalty and Retrospection-Allocation](https://ieeexplore.ieee.org/document/10655465/)** · Unlabeled · VLM · Training-free
- **[Optimizing Resource Consumption in Diffusion Models Through Hallucination Early Detection](https://doi.org/10.1007/978-3-031-91979-4_23)** · Other · LLM · Training-free
- **[Pelican: Correcting Hallucination in Vision-LLMs via Claim Decomposition and Program of Thought Verification](https://doi.org/10.18653/v1/2024.emnlp-main.470)** · Other · LLM · Training-free
- **Perceptual Hallucination in Vision-Language Models: Definition, Analysis and Verification** · Unlabeled · VLM · Training-free
- **[PoLLMgraph: Unraveling Hallucinations in Large Language Models via State Transition Dynamics](https://doi.org/10.18653/v1/2024.findings-naacl.294)** · Other · LLM · Training-free
- **[RadFlag: A Black-Box Hallucination Detection Method for Medical Vision Language Models](https://proceedings.mlr.press/v259/zhang25c.html)** · Unlabeled · VLM · Training-free
- **[RAG-Guided Large Language Models for Visual Spatial Description with Adaptive Hallucination Corrector](https://doi.org/10.1145/3664647.3688990)** · Other · VLM · Training-free
- **[RAG-HAT: A Hallucination-Aware Tuning Pipeline for LLM in Retrieval-Augmented Generation](https://doi.org/10.18653/v1/2024.emnlp-industry.113)** · Other · LLM · Training-free
- **[Reducing hallucination in structured outputs via Retrieval-Augmented Generation](https://doi.org/10.18653/v1/2024.naacl-industry.19)** · Other · LLM · Training-free
- **[ReEval: Automatic Hallucination Evaluation for Retrieval-Augmented Large Language Models via Transferable Adversarial Attacks](https://doi.org/10.18653/v1/2024.findings-naacl.85)** · Other · LLM · Training-free
- **[Reference-free Hallucination Detection for Large Vision-Language Models](https://doi.org/10.18653/v1/2024.findings-emnlp.262)** · Other · VLM · Training-free
- **[Reflective Instruction Tuning: Mitigating Hallucinations in Large Vision-Language Models](https://doi.org/10.1007/978-3-031-73113-6_12)** · Other · VLM · Training-based
- **Revealing and Enhancing Core Visual Regions: Harnessing Internal Attention Dynamics for Hallucination Mitigation in LVLMs** · Unlabeled · VLM · Training-free
- **[Roberta with Low-Rank Adaptation and Hierarchical Attention for Hallucination Detection in LLMs](https://doi.org/10.1109/icicml63543.2024.10957858)** · Other · LLM · Training-free
- **Same Attention, Different Truths: Put Logit-Lens over Visual Attention to Detect and Mitigate LVLM Object Hallucination** · Unlabeled · VLM · Training-free
- **SEASON: Mitigating Temporal Hallucination in Video Large Language Models via Self-Diagnostic Contrastive Decoding** · Unlabeled · VLM · Training-free
- **[Self-contradictory Hallucinations of Large Language Models: Evaluation, Detection and Mitigation](https://openreview.net/forum?id=EmQSOi1X2f)** · Unlabeled · LLM · Training-free
- **[SemEval-2024 Task 6: SHROOM, a Shared-task on Hallucinations and Related Observable Overgeneration Mistakes](https://doi.org/10.18653/v1/2024.semeval-1.273)** · Other · LLM · Training-free
- **[SHROOM-INDElab at SemEval-2024 Task 6: Zero- and Few-Shot LLM-Based Classification for Hallucination Detection](https://doi.org/10.18653/v1/2024.semeval-1.120)** · Other · LLM · Training-free
- **[SLPL SHROOM at SemEval2024 Task 06 : A comprehensive study on models ability to detect hallucination](https://doi.org/10.18653/v1/2024.semeval-1.167)** · Other · LLM · Training-free
- **[Small Agent Can Also Rock! Empowering Small Language Models as Hallucination Detector](https://doi.org/10.18653/v1/2024.emnlp-main.809)** · Other · LLM · Training-free
- **[SmurfCat at SemEval-2024 Task 6: Leveraging Synthetic Data for Hallucination Detection](https://doi.org/10.18653/v1/2024.semeval-1.125)** · Other · LLM · Training-free
- **SVHalluc: Benchmarking Speech-Vision Hallucination in Audio-Visual Large Language Models** · Unlabeled · MLLM(Omni) · Training-free
- **[Tackling Structural Hallucination in Image Translation with Local Diffusion](https://doi.org/10.1007/978-3-031-73004-7_6)** · Other · VLM · Training-free
- **Tell Your Model Where to Attend: Post-hoc Attention Steering for LLMs** · Unlabeled · LLM · Training-free
- **[The Pitfalls of Defining Hallucination](https://doi.org/10.1162/coli_a_00509)** · Other · LLM · Training-free
- **[The Problem of AI Hallucination and How to Solve It](https://doi.org/10.34190/ecel.23.1.2584)** · Other · LLM · Training-free
- **Thinking in Uncertainty: Mitigating Hallucinations in MLRMs with Latent Entropy-Aware Decoding** · Unlabeled · VLM · Training-free
- **📋 [THRONE: An Object-Based Hallucination Benchmark for the Free-Form Generations of Large Vision-Language Models](https://doi.org/10.1109/CVPR52733.2024.02571)** · Other · VLM · Training-free
- **[TofuEval: Evaluating Hallucinations of LLMs on Topic-Focused Dialogue Summarization](https://doi.org/10.18653/v1/2024.naacl-long.251)** · Other · LLM · Training-free
- **📋 [ToolBeHonest: A Multi-level Hallucination Diagnostic Benchmark for Tool-Augmented Large Language Models](https://doi.org/10.18653/v1/2024.emnlp-main.637)** · Other · LLM · Training-free
- **[Toward a Stable, Fair, and Comprehensive Evaluation of Object Hallucination in Large Vision-Language Models](http://papers.nips.cc/paper_files/paper/2024/hash/c9b551a2e195a209fc0b280de2f7f781-Abstract-Conference.html)** · Unlabeled · VLM · Training-free
- **TriDF: Evaluating Perception, Detection, and Hallucination for Interpretable DeepFake Detection** · Unlabeled · LLM · Training-free
- **[Truth-O-Meter: Handling Multiple Inconsistent Sources Repairing LLM Hallucinations](https://doi.org/10.1145/3626772.3657679)** · Other · LLM · Training-free
- **[TU Wien at SemEval-2024 Task 6: Unifying Model-Agnostic and Model-Aware Techniques for Hallucination Detection](https://doi.org/10.18653/v1/2024.semeval-1.173)** · Other · LLM · Training-free
- **[Two-tiered Encoder-based Hallucination Detection for Retrieval-Augmented Generation in the Wild](https://doi.org/10.18653/v1/2024.emnlp-industry.2)** · Other · LLM · Training-free
- **[UMUTeam at SemEval-2024 Task 6: Leveraging Zero-Shot Learning for Detecting Hallucinations and Related Observable Overgeneration Mistakes](https://doi.org/10.18653/v1/2024.semeval-1.98)** · Other · LLM · Training-free
- **Understanding and Mitigating Hallucinations in Multimodal Chain-of-Thought Models** · Unlabeled · VLM · Training-free
- **[Understanding Hallucinations in Diffusion Models through Mode Interpolation](http://papers.nips.cc/paper_files/paper/2024/hash/f29369d192b13184b65c6d2515474d78-Abstract-Conference.html)** · Unlabeled · LLM · Training-free
- **[Understanding Sounds, Missing the Questions: The Challenge of Object Hallucination in Large Audio-Language Models](https://doi.org/10.21437/Interspeech.2024-1076)** · Other · MLLM(Omni) · Training-free
- **Understanding the Role of Hallucination in Reinforcement Post-Training of Multimodal Reasoning Models** · Unlabeled · VLM · Training-based
- **Unstitching the Chimera: Frame-Level Risk and Train-Free Mitigation for Video Hallucination** · Unlabeled · VLM · Training-free
- **[Untangling Emotional Threads: Hallucination Networks of Large Language Models](https://doi.org/10.1007/978-3-031-53468-3_17)** · Other · LLM · Training-free
- **[V-DPO: Mitigating Hallucination in Large Vision Language Models via Vision-Guided Direct Preference Optimization](https://doi.org/10.18653/v1/2024.findings-emnlp.775)** · Other · VLM · Training-based
- **[VGA: Vision GUI Assistant - Minimizing Hallucinations through Image-Centric Fine-Tuning](https://doi.org/10.18653/v1/2024.findings-emnlp.68)** · Other · VLM · Training-free
- **[Vista-llama: Reducing Hallucination in Video Language Models via Equal Distance to Visual Tokens](https://doi.org/10.1109/CVPR52733.2024.01249)** · Other · VLM · Training-free
- **[Volcano: Mitigating Multimodal Hallucination through Self-Feedback Guided Revision](https://doi.org/10.18653/v1/2024.naacl-long.23)** · Other · VLM · Training-free
- **[What if...?: Thinking Counterfactual Keywords Helps to Mitigate Hallucination in Large Multi-modal Models](https://doi.org/10.18653/v1/2024.findings-emnlp.626)** · Other · VLM · Training-free
- **[Whispers that Shake Foundations: Analyzing and Mitigating False Premise Hallucinations in Large Language Models](https://doi.org/10.18653/v1/2024.emnlp-main.155)** · Other · LLM · Training-free
- **[Zero-Resource Hallucination Prevention for Large Language Models](https://doi.org/10.18653/v1/2024.findings-emnlp.204)** · Other · LLM · Training-free
- **ZINA: Multimodal Fine-grained Hallucination Detection and Editing** · Unlabeled · VLM · Training-free

</details>

<details>
<summary>📅 2023 · 25 papers</summary>

- **[Mitigating Fine-Grained Hallucination by Fine-Tuning Large Vision-Language Models with Caption Rewrites](https://arxiv.org/abs/2312.01701)** · arXiv · VLM · Training-based
- **[Instructive Decoding: Instruction-Tuned Large Language Models are Self-Refiner from Noisy Instructions](https://arxiv.org/abs/2311.00233)** · arXiv · LLM · Training-free
- **[Mitigating Object Hallucinations in Large Vision-Language Models through Visual Contrastive Decoding](https://arxiv.org/abs/2311.16922)** · arXiv · VLM · Training-free
- **[HallE-Control: Controlling Object Hallucination in Large Multimodal Models](https://arxiv.org/abs/2310.01779)** · arXiv · VLM · Training-free
- **📋 [Negative Object Presence Evaluation (NOPE) to Measure Object Hallucination in Vision-Language Models](https://arxiv.org/abs/2310.05338)** · arXiv · VLM · Training-free
- **[DoLa: Decoding by Contrasting Layers Improves Factuality in Large Language Models](https://arxiv.org/abs/2309.03883)** · arXiv · LLM · Training-free
- **[Evaluating Object Hallucination in Large Vision-Language Models](https://arxiv.org/abs/2305.10355)** · arXiv · VLM · Training-free
- **[&quot;Why is this misleading?&quot;: Detecting News Headline Hallucinations with Explanations](https://doi.org/10.1145/3543507.3583375)** · Other · LLM · Training-free
- **📋 [A New Benchmark and Reverse Validation Method for Passage-level Hallucination Detection](https://doi.org/10.18653/v1/2023.findings-emnlp.256)** · Other · LLM · Training-free
- **[CaPE: Contrastive Parameter Ensembling for Reducing Hallucination in Abstractive Summarization](https://doi.org/10.18653/v1/2023.findings-acl.685)** · Other · LLM · Training-free
- **[Contrastive Learning Reduces Hallucination in Conversations](https://doi.org/10.1609/aaai.v37i11.26596)** · Other · LLM · Training-free
- **[Critic-Driven Decoding for Mitigating Hallucinations in Data-to-text Generation](https://doi.org/10.18653/v1/2023.emnlp-main.172)** · Other · LLM · Training-free
- **[CRUSH4SQL: Collective Retrieval Using Schema Hallucination For Text2SQL](https://doi.org/10.18653/v1/2023.emnlp-main.868)** · Other · LLM · Training-free
- **[Detecting Dialogue Hallucination Using Graph Neural Networks](https://doi.org/10.1109/ICMLA58977.2023.00128)** · Other · LLM · Training-free
- **[Eyes Show the Way: Modelling Gaze Behaviour for Hallucination Detection](https://doi.org/10.18653/v1/2023.findings-emnlp.764)** · Other · LLM · Training-free
- **[Hallucination Detection for Grounded Instruction Generation](https://doi.org/10.18653/v1/2023.findings-emnlp.266)** · Other · LLM · Training-free
- **📋 [HalOmi: A Manually Annotated Benchmark for Multilingual Hallucination and Omission Detection in Machine Translation](https://doi.org/10.18653/v1/2023.emnlp-main.42)** · Other · LLM · Training-free
- **[KCTS: Knowledge-Constrained Tree Search Decoding with Token-Level Hallucination Detection](https://doi.org/10.18653/v1/2023.emnlp-main.867)** · Other · LLM · Training-free
- **[Looking for a Needle in a Haystack: A Comprehensive Study of Hallucinations in Neural Machine Translation](https://doi.org/10.18653/v1/2023.eacl-main.75)** · Other · LLM · Training-free
- **[Med-HALT: Medical Domain Hallucination Test for Large Language Models](https://doi.org/10.18653/v1/2023.conll-1.21)** · Other · LLM · Training-free
- **[Plausible May Not Be Faithful: Probing Object Hallucination in Vision-Language Pre-training](https://doi.org/10.18653/v1/2023.eacl-main.156)** · Other · VLM · Training-free
- **[SAC3: Reliable Hallucination Detection in Black-Box Language Models via Semantic-aware Cross-check Consistency: Reliable Hallucination Detection in Black-Box Language Models via Semantic-aware Cross-check Consistency](https://doi.org/10.18653/v1/2023.findings-emnlp.1032)** · Other · LLM · Training-free
- **[Sources of Hallucination by Large Language Models on Inference Tasks](https://doi.org/10.18653/v1/2023.findings-emnlp.182)** · Other · LLM · Training-free
- **[Towards Mitigating LLM Hallucination via Self Reflection](https://doi.org/10.18653/v1/2023.findings-emnlp.123)** · Other · LLM · Training-free
- **[Towards reducing hallucination in extracting information from financial reports using Large Language Models](https://doi.org/10.1145/3639856.3639895)** · Other · LLM · Training-free

</details>

<details>
<summary>📅 2022 · 5 papers</summary>

- **[Contrastive Decoding: Open-ended Text Generation as Optimization](https://arxiv.org/abs/2210.15097)** · arXiv · LLM · Training-free
- **[Hallucinated but Factual! Inspecting the Factuality of Hallucinations in Abstractive Summarization](https://doi.org/10.18653/v1/2022.acl-long.236)** · Other · LLM · Training-free
- **[Hallucination of Speech Recognition Errors With Sequence to Sequence Learning](https://doi.org/10.1109/taslp.2022.3145313)** · Other · MLLM(Omni) · Training-free
- **[Let there be a clock on the beach: Reducing Object Hallucination in Image Captioning](https://doi.org/10.1109/WACV51458.2022.00253)** · Other · VLM · Training-free
- **[On the Origin of Hallucinations in Conversational Models: Is it the Datasets or the Models?](https://doi.org/10.18653/v1/2022.naacl-main.387)** · Other · LLM · Training-free

</details>

<details>
<summary>📅 2021 · 3 papers</summary>

- **[On Hallucination and Predictive Uncertainty in Conditional Language Generation](https://doi.org/10.18653/v1/2021.eacl-main.236)** · Other · LLM · Training-free
- **[Retrieval Augmentation Reduces Hallucination in Conversation](https://doi.org/10.18653/v1/2021.findings-emnlp.320)** · Other · LLM · Training-free
- **[The Curious Case of Hallucinations in Neural Machine Translation](https://doi.org/10.18653/v1/2021.naacl-main.92)** · Other · LLM · Training-free

</details>

<details>
<summary>📅 2020 · 1 papers</summary>

- **[Structural Hallucination in LLMs: A Formal Characterization and Mitigation Method](https://doi.org/10.36948/ijfmr.2020.v02i05.61072)** · Other · LLM · Training-free

</details>

<details>
<summary>📅 2019 · 4 papers</summary>

- **[Sticking to the Facts: Confident Decoding for Faithful Data-to-Text Generation](https://arxiv.org/abs/1910.08684)** · arXiv · LLM · Training-based
- **[A Simple Recipe towards Reducing Hallucination in Neural Surface Realisation](https://doi.org/10.18653/v1/P19-1256)** · Other · LLM · Training-free
- **[Assessing The Factual Accuracy of Generated Text](https://doi.org/10.1145/3292500.3330955)** · Other · LLM · Training-free
- **[Ranking Generated Summaries by Correctness: An Interesting but Challenging Application for Natural Language Inference](https://doi.org/10.18653/v1/P19-1213)** · Other · LLM · Training-free

</details>

<details>
<summary>📅 2018 · 1 papers</summary>

- **[Object Hallucination in Image Captioning](https://doi.org/10.18653/v1/D18-1437)** · Other · VLM · Training-free

</details>

---

<a id="sec-cite"></a>
## 📖 Citation

If this atlas helps your research, please consider citing our related papers (feedback and suggestions are also welcome):

```bibtex
@article{lyu2026hallu_sae,
  title={Towards Interpretable Hallucination Analysis and Mitigation in LVLMs via Contrastive Neuron Steering},
  author={Lyu, Guangtao and Cheng, Xinyi and Liu, Qi and Xu, Chenghao and Yan, Jiexi and Yang, Muli and Fang, Fen and Deng, Cheng},
  journal={arXiv preprint arXiv:2602.00621},
  year={2026}
}

@article{lyu2025hallu_vdc,
  title={Revealing Perception and Generation Dynamics in LVLMs: Mitigating Hallucinations via Validated Dominance Correction},
  author={Lyu, Guangtao and Cheng, Xinyi and Xu, Chenghao and Liu, Qi and Yang, Muli and Fang, Fen and Chen, Huilin and Yan, Jiexi and Yang, Xu and Deng, Cheng},
  journal={arXiv preprint arXiv:2512.18813},
  year={2025}
}

@article{lyu2026hallu_pade,
  title={Revealing and Enhancing Core Visual Regions: Harnessing Internal Attention Dynamics for Hallucination Mitigation in LVLMs},
  author={Lyu, Guangtao and Liu, Qi and Xu, Chenghao and Yan, Jiexi and Yang, Muli and Li, Xueting and Fang, Fen and Deng, Cheng},
  journal={ACL Findings},
  year={2026}
}
```

<a id="sec-contrib"></a>
## 🤝 Contributing

We welcome new papers, code links, venue info, and taxonomy corrections! Please read [CONTRIBUTING.md](.github/CONTRIBUTING.md).

<a id="sec-license"></a>
## 📄 License

Released under [CC0-1.0](LICENSE), following the [awesome](https://github.com/sindresorhus/awesome) manifesto.

<a id="sec-stars"></a>
## ⭐ Star History

A record of how this atlas has grown in the community:

<a href="https://www.star-history.com/?repos=GuangtaoLyu%2Fawesome-hallucination-atlas&type=date&legend=top-left">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=GuangtaoLyu/awesome-hallucination-atlas&type=date&theme=dark&legend=top-left&sealed_token=es4O-8rwqglOmnZDjxaqaRD-Ucj7DRdPVwK8M-Q3DFyjCaJd_lqSECa1wcEFD6xTtJsuU_wc8vS4IOM8cc10PMTV8r_I5CX3j1zoaifBJhbYcwconoGqMT8wSFdOhwLGQIejqcG7fAUtXusYAEmAxTBQgdMFqU1CchsMrhaPgcwbPq4vSpaaDMALHIKg" />
    <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=GuangtaoLyu/awesome-hallucination-atlas&type=date&legend=top-left&sealed_token=es4O-8rwqglOmnZDjxaqaRD-Ucj7DRdPVwK8M-Q3DFyjCaJd_lqSECa1wcEFD6xTtJsuU_wc8vS4IOM8cc10PMTV8r_I5CX3j1zoaifBJhbYcwconoGqMT8wSFdOhwLGQIejqcG7fAUtXusYAEmAxTBQgdMFqU1CchsMrhaPgcwbPq4vSpaaDMALHIKg" />
    <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=GuangtaoLyu/awesome-hallucination-atlas&type=date&legend=top-left&sealed_token=es4O-8rwqglOmnZDjxaqaRD-Ucj7DRdPVwK8M-Q3DFyjCaJd_lqSECa1wcEFD6xTtJsuU_wc8vS4IOM8cc10PMTV8r_I5CX3j1zoaifBJhbYcwconoGqMT8wSFdOhwLGQIejqcG7fAUtXusYAEmAxTBQgdMFqU1CchsMrhaPgcwbPq4vSpaaDMALHIKg" />
  </picture>
</a>
