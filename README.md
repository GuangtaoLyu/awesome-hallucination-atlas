> 🌐 **English** · [中文](README.zh-CN.md)

# Awesome Hallucination Atlas [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> **Awesome Hallucination Atlas** — A structured, interactive atlas of hallucination research across multimodal LLMs (MLLM / VLM / LLM).
>
> Covers **detection, evaluation, and mitigation** of hallucinations, with multi-dimensional faceted filtering by model type, method type, and year, plus tags for modality and scenario.
>
> Taxonomy is auto-labeled from the **full arXiv abstract text** (21/1918 papers), not just title keywords.

<p align='center'>
  <img src='https://img.shields.io/badge/Papers-1918-blue' />
  <img src='https://img.shields.io/badge/Abstract--based-21-9cf' />
  <img src='https://img.shields.io/badge/PRs-Welcome-brightgreen' />
  <img src='https://img.shields.io/static/v1?label=Last%20Update&message=2026-08&color=orange' />
</p>

<p align='center'>
  <a href='https://guangtaolyu.github.io/awesome-hallucination-atlas/'>
    <img alt='Live Website' src='https://img.shields.io/static/v1?label=Live%20Website&message=Visit%20Now&color=8b7cf6&style=for-the-badge' />
  </a>
</p>

> **🌐 Explore the Interactive Website** — [awesome-hallucination-atlas — Live Site](https://guangtaolyu.github.io/awesome-hallucination-atlas/). Faceted filtering, full-text abstract search, and year sorting.
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
- **Total papers**：`1918` (deduplicated)
- **With paper link**：`1909` · **With abstract**：`21` · **With code**：`0` · **Published at venue**：`935`
- For papers published at a venue: time and link prioritize the official conference/journal info (DBLP), otherwise arXiv info is used.
- **Year range**：2018 – 2027

### Year Distribution

| Year | Count | Share |
|------|------|------|
| 2027 | 5 | `░░░░░░░░░░░░░░░░░░░░` 0.3%
| 2026 | 749 | `████████░░░░░░░░░░░░` 39.1%
| 2025 | 763 | `████████░░░░░░░░░░░░` 39.8%
| 2024 | 364 | `████░░░░░░░░░░░░░░░░` 19.0%
| 2023 | 24 | `░░░░░░░░░░░░░░░░░░░░` 1.3%
| 2022 | 4 | `░░░░░░░░░░░░░░░░░░░░` 0.2%
| 2021 | 3 | `░░░░░░░░░░░░░░░░░░░░` 0.2%
| 2020 | 1 | `░░░░░░░░░░░░░░░░░░░░` 0.1%
| 2019 | 4 | `░░░░░░░░░░░░░░░░░░░░` 0.2%
| 2018 | 1 | `░░░░░░░░░░░░░░░░░░░░` 0.1%


### Model Type

| Model Type | Description | Count |
|----------|------|------|
| **VLM** | Vision-Language Model (LVLM; also covers works that call themselves MLLM but handle only image/video + text) | 655 |
| **MLLM(Omni)** | Omni / full-modal model (audio / speech / any-to-any) | 28 |
| **LLM** | Pure text-based LLM | 1235 |


### Method Type

| Method Type | Description | Count |
|----------|------|------|
| **Training-free** | Training-free (decoding intervention / attention calibration / representation guidance, etc.) | 1832 |
| **Training-based** | Training-based (preference optimization / fine-tuning / RL, etc.) | 86 |


<details>
<summary>📊 Venue Distribution</summary>

### Venue Distribution

> Papers published at a conference / journal are counted by venue (official info prioritized); `arXiv (preprint)` means a preprint not yet officially accepted. Niche journals / small venues, workshops / satellite / co-located events, and venues with only 1 paper are grouped into the “Other” row (details in the collapsible section below). `Unlabeled` marks entries with no resolvable link.

| Venue / Journal | Count | Share |
|-------------|------|------|
| ACL | 152 | `██░░░░░░░░░░░░░░░░░░` 7.9%
| EMNLP | 108 | `█░░░░░░░░░░░░░░░░░░░` 5.6%
| AAAI | 62 | `█░░░░░░░░░░░░░░░░░░░` 3.2%
| CVPR | 62 | `█░░░░░░░░░░░░░░░░░░░` 3.2%
| ICLR | 36 | `░░░░░░░░░░░░░░░░░░░░` 1.9%
| NAACL | 36 | `░░░░░░░░░░░░░░░░░░░░` 1.9%
| NeurIPS | 34 | `░░░░░░░░░░░░░░░░░░░░` 1.8%
| EACL | 24 | `░░░░░░░░░░░░░░░░░░░░` 1.3%
| ACM MM | 22 | `░░░░░░░░░░░░░░░░░░░░` 1.1%
| ICASSP | 22 | `░░░░░░░░░░░░░░░░░░░░` 1.1%
| ICML | 17 | `░░░░░░░░░░░░░░░░░░░░` 0.9%
| ICCV | 12 | `░░░░░░░░░░░░░░░░░░░░` 0.6%
| TMLR | 12 | `░░░░░░░░░░░░░░░░░░░░` 0.6%
| WACV | 11 | `░░░░░░░░░░░░░░░░░░░░` 0.6%
| COLING | 9 | `░░░░░░░░░░░░░░░░░░░░` 0.5%
| ECCV | 9 | `░░░░░░░░░░░░░░░░░░░░` 0.5%
| Lecture Notes in Networks and Systems | 9 | `░░░░░░░░░░░░░░░░░░░░` 0.5%
| SIGIR | 8 | `░░░░░░░░░░░░░░░░░░░░` 0.4%
| WWW | 8 | `░░░░░░░░░░░░░░░░░░░░` 0.4%
| Comput. Linguistics | 6 | `░░░░░░░░░░░░░░░░░░░░` 0.3%
| IJCAI | 6 | `░░░░░░░░░░░░░░░░░░░░` 0.3%
| IJCNN | 5 | `░░░░░░░░░░░░░░░░░░░░` 0.3%
| INTERSPEECH | 5 | `░░░░░░░░░░░░░░░░░░░░` 0.3%
| KDD | 5 | `░░░░░░░░░░░░░░░░░░░░` 0.3%
| ICME | 4 | `░░░░░░░░░░░░░░░░░░░░` 0.2%
| IJCV | 4 | `░░░░░░░░░░░░░░░░░░░░` 0.2%
| Lecture Notes in Computer Science | 4 | `░░░░░░░░░░░░░░░░░░░░` 0.2%
| TASLP | 4 | `░░░░░░░░░░░░░░░░░░░░` 0.2%
| 18th International Workshop on Semantic Evaluation (SemEval-2024) | 3 | `░░░░░░░░░░░░░░░░░░░░` 0.2%
| CIKM | 3 | `░░░░░░░░░░░░░░░░░░░░` 0.2%
| ECIR | 3 | `░░░░░░░░░░░░░░░░░░░░` 0.2%
| IJCNLP-AACL | 3 | `░░░░░░░░░░░░░░░░░░░░` 0.2%
| TAI | 3 | `░░░░░░░░░░░░░░░░░░░░` 0.2%
| TOMM | 3 | `░░░░░░░░░░░░░░░░░░░░` 0.2%
| ASRU | 2 | `░░░░░░░░░░░░░░░░░░░░` 0.1%
| CLEF | 2 | `░░░░░░░░░░░░░░░░░░░░` 0.1%
| Communications in Computer and Information Science | 2 | `░░░░░░░░░░░░░░░░░░░░` 0.1%
| FLLM | 2 | `░░░░░░░░░░░░░░░░░░░░` 0.1%
| ICIC | 2 | `░░░░░░░░░░░░░░░░░░░░` 0.1%
| ICMLA | 2 | `░░░░░░░░░░░░░░░░░░░░` 0.1%
| ICPR | 2 | `░░░░░░░░░░░░░░░░░░░░` 0.1%
| IEEE Access | 2 | `░░░░░░░░░░░░░░░░░░░░` 0.1%
| IEEE Trans. Software Eng. | 2 | `░░░░░░░░░░░░░░░░░░░░` 0.1%
| IEEE Trans. Vis. Comput. Graph. | 2 | `░░░░░░░░░░░░░░░░░░░░` 0.1%
| IEEE Transactions on Computational Social Systems | 2 | `░░░░░░░░░░░░░░░░░░░░` 0.1%
| Iconic Research and Engineering Journals | 2 | `░░░░░░░░░░░░░░░░░░░░` 0.1%
| International Journal of Computer Applications | 2 | `░░░░░░░░░░░░░░░░░░░░` 0.1%
| MICCAI | 2 | `░░░░░░░░░░░░░░░░░░░░` 0.1%
| NN | 2 | `░░░░░░░░░░░░░░░░░░░░` 0.1%
| Neural Comput. Appl. | 2 | `░░░░░░░░░░░░░░░░░░░░` 0.1%
| PRCV | 2 | `░░░░░░░░░░░░░░░░░░░░` 0.1%
| Proc. ACM Softw. Eng. | 2 | `░░░░░░░░░░░░░░░░░░░░` 0.1%
| USENIX Security Symposium | 2 | `░░░░░░░░░░░░░░░░░░░░` 0.1%
| TNNLS | 1 | `░░░░░░░░░░░░░░░░░░░░` 0.1%
| Other | 195 | `██░░░░░░░░░░░░░░░░░░` 10.2%
| arXiv (preprint) | 944 | `██████████░░░░░░░░░░` 49.2%
| Unlabeled | 26 | `░░░░░░░░░░░░░░░░░░░░` 1.4%

<details>
<summary>“Other” details (152 venues, 195 papers — click to expand)</summary>

| venue | Count |
|-------|------|
| SemEval@NAACL | 21 |
| SemEval@ACL | 13 |
| LREC/COLING | 6 |
| SIGIR-AP | 3 |
| AAAI Bridge Program | 2 |
| COLING Workshops | 2 |
| CVPRW | 2 |
| ICCVW | 2 |
| 13th Joint Conference on Lexical and Computational Semantics (*SEM 2024) | 1 |
| 16th International Conference on E-Education, E-Business, E-Management and E-Learning (IC4e) | 1 |
| 23rd International Learning and Technology Conference (L&amp;T) | 1 |
| 29th International Conference on Computer Supported Cooperative Work in Design (CSCWD) | 1 |
| 2nd International Conference on Computer Communication, Networks and Information Science (CCNIS) | 1 |
| 6th Clinical Natural Language Processing Workshop | 1 |
| 7th International Conference on Intelligent Communication Technologies and Virtual Mobile Networks (ICICV) | 1 |
| 7th International Conference on Pattern Recognition and Artificial Intelligence (PRAI) | 1 |
| ACCV | 1 |
| ACLING | 1 |
| ACM Comput. Surv. | 1 |
| ACM Transactions on Asian and Low-Resource Language Information Processing | 1 |
| ACM Transactions on Software Engineering and Methodology | 1 |
| AIMLSystems | 1 |
| ASE | 1 |
| Advanced International Journal for Research | 1 |
| Advances in Computer Science Research | 1 |
| Advances in Machine Learning & Artificial Intelligence | 1 |
| Advances in Transdisciplinary Engineering | 1 |
| Adversarial Machine Learning | 1 |
| Appl. Netw. Sci. | 1 |
| Applications of Neuro-Symbolic Artificial Intelligence | 1 |
| Artif. Intell. Rev. | 1 |
| Artificial Intelligence and Applications | 1 |
| Artificial Intelligence and Machine Learning Review | 1 |
| Artificial Intelligence and Robotics Research | 1 |
| BDCAT | 1 |
| BIOSTEC | 1 |
| Bioinform. | 1 |
| CAAI Trans. Intell. Technol. | 1 |
| CAI | 1 |
| CHASE | 1 |
| CODS | 1 |
| COMPLEX NETWORKS | 1 |
| ClinicalNLP@NAACL | 1 |
| CoNLL | 1 |
| CogSci | 1 |
| Commun. ACM | 1 |
| Communications in Humanities Research | 1 |
| Companion Proceedings of the ACM on Web Conference | 1 |
| Comput. Biol. Medicine | 1 |
| Comput. Hum. Behav. | 1 |
| Comput. Sci. Rev. | 1 |
| Computer | 1 |
| Computer and Decision Making: An International Journal | 1 |
| Cyber Awareness and Research Symposium (CARS) | 1 |
| DBSec | 1 |
| DCC | 1 |
| DSN-W | 1 |
| Data Intell. | 1 |
| Data Knowl. Eng. | 1 |
| ECAI | 1 |
| ECCV Workshops | 1 |
| ECML/PKDD | 1 |
| ESWA | 1 |
| Eighth International Conference on Image Information Processing (ICIIP) | 1 |
| European Conference on e-Learning | 1 |
| FAccT | 1 |
| FORGE@ICSE | 1 |
| Frontiers Artif. Intell. | 1 |
| Frontiers in Emerging Artificial Intelligence and Machine Learning | 1 |
| GLOBECOM | 1 |
| HGAIS@ISWC | 1 |
| IAAI/ALA@ECAI | 1 |
| ICAART | 1 |
| ICAIF | 1 |
| ICAIIC | 1 |
| ICARCV | 1 |
| ICCK Transactions on Emerging Topics in Artificial Intelligence | 1 |
| ICCS | 1 |
| ICDE | 1 |
| ICDEW | 1 |
| ICICT | 1 |
| ICIPW | 1 |
| ICLP | 1 |
| ICONIP | 1 |
| ICPRAM | 1 |
| ICTSS | 1 |
| IDSTA | 1 |
| IEEE International Conference on Communication, Networks and Satellite (COMNETSAT) | 1 |
| IEEE International Conference on Image Processing Workshops (ICIPW) | 1 |
| IEEE International Conference on Pattern Recognition, Machine Vision and Artificial Intelligence (PRMVAI) | 1 |
| IEEE J. Sel. Top. Signal Process. | 1 |
| IEEE Open J. Comput. Soc. | 1 |
| IEEE Trans. Big Data | 1 |
| IEEE Trans. Circuits Syst. Video Technol. | 1 |
| IEEE Trans. Intell. Transp. Syst. | 1 |
| IEEE Transactions on Information Forensics and Security | 1 |
| INFFUS | 1 |
| INTERNATIONAL JOURNAL OF CREATIVE RESEARCH THOUGHTS | 1 |
| ISCSLP | 1 |
| ISNCC | 1 |
| Inf. Sci. | 1 |
| Int. J. Approx. Reason. | 1 |
| Int. J. Interact. Multim. Artif. Intell. | 1 |
| International Conference of the Learning Sciences | 1 |
| International Conference on Artificial Intelligence and Blockchain in Healthcare | 1 |
| International Conference on Artificial Intelligence and Machine Vision (AIMV) | 1 |
| International Conference on Computer Networks and Inventive Communication Technologies (ICCNCT) | 1 |
| International Conference on Signal Image Processing and Communication (ICSIPC) | 1 |
| International Conference on Virtual Learning - VIRTUAL LEARNING - VIRTUAL REALITY (20th edition) | 1 |
| International Journal For Multidisciplinary Research | 1 |
| International Journal of Advanced Research in Science and Technology | 1 |
| International Journal of Artificial Intelligence & Applications | 1 |
| International Journal of Artificial Intelligence, Data Science, and Machine Learning | 1 |
| International Journal of Engineering and Computer Science | 1 |
| International Journal of Innovative Research in Technology | 1 |
| International Journal of Research Publication and Reviews | 1 |
| International Journal of Science and Research (IJSR) | 1 |
| J. Biomed. Informatics | 1 |
| J. Web Semant. | 1 |
| KBC-LM/LM-KBC@ISWC | 1 |
| KBS | 1 |
| KGSWC | 1 |
| KiL@KDD | 1 |
| LKM@IJCAI | 1 |
| MMM | 1 |
| Mach. Intell. Res. | 1 |
| Multim. Syst. | 1 |
| Multimedia University Engineering Conference (MECON) | 1 |
| NDSS | 1 |
| NEUCOM | 1 |
| NLDB | 1 |
| Natural Language Processing Journal | 1 |
| NeSy | 1 |
| Open Research Europe | 1 |
| Pattern Recognit. | 1 |
| Patterns | 1 |
| RIGGS: Journal of Artificial Intelligence and Digital Business | 1 |
| Radiology: Artificial Intelligence | 1 |
| SEIP@ICSE | 1 |
| SEMANTiCS | 1 |
| SIGSOFT FSE Companion | 1 |
| SMC | 1 |
| STOC | 1 |
| Second International Conference on Image Processing and Artificial Intelligence (ICIPAI 2025) | 1 |
| Studies in Computational Intelligence | 1 |
| TIP | 1 |
| TMM | 1 |
| TRUST-AI@ECAI | 1 |
| Text2Story@ECIR | 1 |
| Third Arabic Natural Language Processing Conference | 1 |
| VISIGRAPP (2) - VISAPP | 1 |
| xAI | 1 |

</details>

</details>

### CCF Rating

> CCF ratings follow the **CCF Recommended International Conference / Journal Directory (2026)** for officially published papers; `Not in CCF` covers arXiv preprints, unresolved venues, and venues outside the CCF list.

| CCF Rating | Count | Share |
|----------|------|------|
| CCF-A | 435 | `█████░░░░░░░░░░░░░░░` 22.7%
| CCF-B | 233 | `██░░░░░░░░░░░░░░░░░░` 12.1%
| CCF-C | 34 | `░░░░░░░░░░░░░░░░░░░░` 1.8%
| Not in CCF | 1216 | `█████████████░░░░░░░` 63.4%
> 📋 `115` **Benchmark** papers and 📚 `32` **Survey** papers are listed separately (see sections below) and do not affect the method taxonomy.

---

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

- **Agentic AI / Multi-Agent** — 64 papers tagged `Agent`.
- **RAG / Faithfulness** — 84 papers tagged `RAG`.
- **Reasoning Models** — 109 papers tagged `Reasoning`.
- **Embodied / World Model** — 6 papers tagged `Embodied`.

---

<a id="sec-benchmark"></a>
## 📋 Benchmarks & Evaluation
> 115 evaluation / benchmark / dataset papers are listed separately (also kept in the main list below, marked 📋).

<details open>
<summary>📋 Benchmark List (115 papers — click to collapse / expand)</summary>

- **📋 [KnowHal: A Knowledge-Driven Benchmark for Comprehensive Multimodal Hallucination Evaluation](https://arxiv.org/abs/2608.03782)** · arXiv · VLM · Training-free
- **📋 [MoHallBench: A Benchmark for Motion Hallucination in Video Large Language Models](https://arxiv.org/abs/2607.01117)** · arXiv · VLM · Training-free
- **📋 [MissingBench-Verified: Probing Vision-Language Models' Inability to Detect Missing Object Parts](https://arxiv.org/abs/2607.18673)** · arXiv · VLM · Training-free
- **📋 [HoloCount: A Holistic Visual Counting Benchmark for MLLMs](https://arxiv.org/abs/2607.06420)** · arXiv · VLM · Training-free
- **📋 [HalluTruthQA: A Fine-Grained Benchmark for Hallucination Detection, Localization, and Explanation in Arabic Question Answering](https://arxiv.org/abs/2607.20219)** · arXiv · LLM · Training-free
- **📋 [ArtChart: A Benchmark for Faithful Artistic Chart Generation with Integrated Text Rendering](https://arxiv.org/abs/2607.16060)** · arXiv · LLM · Training-free
- **📋 [Rethinking Evaluation for LLM Hallucination Detection: A Desiderata, A New RAG-based Benchmark, New Insights](https://aclanthology.org/2026.acl-long.680/)** · ACL 2026 · LLM · Training-free
- **📋 [PROBE: PROcess-Based BEnchmark for Hallucination Detection](https://aclanthology.org/2026.findings-acl.2099/)** · ACL 2026 · LLM · Training-free
- **📋 [INFACT: A Diagnostic Benchmark for Induced Faithfulness and Factuality Hallucinations in Video-LLMs](https://aclanthology.org/2026.acl-long.2062/)** · ACL 2026 · VLM · Training-free
- **📋 [Hallucination Detection in Long-Form Text Generated by LLMs: A Benchmark and a Hyper-Relational Knowledge Graph Approach](https://aclanthology.org/2026.findings-acl.1673/)** · ACL 2026 · LLM · Training-free
- **📋 [HalluAudio: A Comprehensive Benchmark for Hallucination Detection in Large Audio-Language Models](https://aclanthology.org/2026.acl-long.1797/)** · ACL 2026 · MLLM(Omni) · Training-free
- **📋 [SAGE: An Expert-Annotated South Asian GI Endoscopy Dataset for Multimodal Learning and Hallucination Analysis](https://arxiv.org/abs/2606.22144)** · arXiv · VLM · Training-free
- **📋 [OpenHalDet: A Unified Benchmark for Hallucination Detection across Diverse Generation Scenarios](https://arxiv.org/abs/2606.06959)** · arXiv · LLM · Training-free
- **📋 [MedHal-Loc: Are "Explainable-by-Architecture" Medical Hallucination Detectors Faithful Localizers? A Localization Benchmark](https://arxiv.org/abs/2606.21517)** · arXiv · LLM · Training-free
- **📋 [MedBench v5: A Dynamic, Process-Oriented, and Hallucination-Aware Benchmark for Clinical Multimodal Models](https://arxiv.org/abs/2606.24155)** · arXiv · VLM · Training-free
- **📋 [How Far Can You Get Without a GPU? A Systematic Benchmark of Lightweight Hallucination Detection Across Question Answering, Dialogue, and Summarisation](https://arxiv.org/abs/2606.29809)** · arXiv · LLM · Training-free
- **📋 [HALAS: A Human-Annotated Dataset of Hallucinations of Modern ASR Systems](https://arxiv.org/abs/2606.23048)** · arXiv · LLM · Training-free
- **📋 [ClinHallu: A Benchmark for Diagnosing Stage-Wise Hallucinations in Medical MLLM Reasoning](https://arxiv.org/abs/2606.14697)** · arXiv · VLM · Training-free
- **📋 [A Benchmark for Hallucination Detection in VLMs for Gastrointestinal Endoscopy](https://arxiv.org/abs/2606.24115)** · arXiv · VLM · Training-free
- **📋 [Fine-Grained Multi Image Object Hallucination Benchmark](https://openaccess.thecvf.com/content/CVPR2026/html/Min_Fine-Grained_Multi_Image_Object_Hallucination_Benchmark_CVPR_2026_paper.html)** · CVPR 2026 · VLM · Training-free
- **📋 [ReactBench: A Cause-Driven Benchmark for Multimodal Hallucination via Systematic Evaluation](https://arxiv.org/abs/2605.29579)** · arXiv · VLM · Training-free
- **📋 [PARALLAX: Separating Genuine Hallucination Detection from Benchmark Construction Artifacts](https://arxiv.org/abs/2605.17028)** · arXiv · LLM · Training-free
- **📋 [Med-StepBench: A Hierarchical Reasoning Framework for Evaluating Hallucinations in Medical Vision-Language Models](https://arxiv.org/abs/2605.10002)** · arXiv · VLM · Training-free
- **📋 [HalluWorld: A Controlled Benchmark for Hallucination via Reference World Models](https://arxiv.org/abs/2605.19341)** · arXiv · LLM · Training-free
- **📋 [HalluScore: Large Language Model Hallucination Question Answering Benchmark](https://arxiv.org/abs/2605.17007)** · arXiv · LLM · Training-free
- **📋 [HalluScan: A Systematic Benchmark for Detecting and Mitigating Hallucinations in Instruction-Following LLMs](https://arxiv.org/abs/2605.02443)** · arXiv · LLM · Training-free
- **📋 [Delulu: A Verified Multi-Lingual Benchmark for Code Hallucination Detection in Fill-in-the-Middle Tasks](https://arxiv.org/abs/2605.07024)** · arXiv · LLM · Training-free
- **📋 [A multilingual hallucination benchmark: MultiWikiQHalluA](https://arxiv.org/abs/2605.02504)** · arXiv · LLM · Training-free
- **📋 [Semantic Layers for Reliable LLM-Powered Data Analytics: A Paired Benchmark of Accuracy and Hallucination Across Three Frontier Models](https://arxiv.org/abs/2604.25149)** · arXiv · LLM · Training-free
- **📋 [DetailVerifyBench: A Benchmark for Dense Hallucination Localization in Long Image Captions](https://arxiv.org/abs/2604.05623)** · arXiv · VLM · Training-free
- **📋 [DO-Bench: An Attributable Benchmark for Diagnosing Object Hallucination in Vision-Language Models](https://arxiv.org/abs/2604.22822)** · arXiv · VLM · Training-free
- **📋 [DHEval: A Dynamic Hallucination Evaluation Protocol Robust to Data Contamination](https://doi.org/10.1109/icassp55912.2026.11462032)** · ICASSP 2026 · LLM · Training-free
- **📋 [ManiBench: A Benchmark for Testing Visual-Logic Drift and Syntactic Hallucinations in Manim Code Generation](https://arxiv.org/abs/2603.13251)** · arXiv · VLM · Training-free
- **📋 [HalDec-Bench: Benchmarking Hallucination Detector in Image Captioning](https://arxiv.org/abs/2603.15253)** · arXiv · VLM · Training-free
- **📋 [FinReflectKG -- HalluBench: GraphRAG Hallucination Benchmark for Financial Question Answering Systems](https://arxiv.org/abs/2603.20252)** · arXiv · LLM · Training-free
- **📋 [FREAK: A Fine-grained Hallucination Evaluation Benchmark for Advanced MLLMs](https://arxiv.org/abs/2603.19765)** · arXiv · VLM · Training-free
- **📋 [Multi-Hall-SA: A Cross-lingual Benchmark for Multi-Type Hallucination Detection in Low-Resource South African Languages](https://doi.org/10.18653/v1/2026.findings-eacl.330)** · EACL 2026 · LLM · Training-free
- **📋 [KGHaluBench: A Knowledge Graph-Based Hallucination Benchmark for Evaluating the Breadth and Depth of LLM Knowledge](https://doi.org/10.18653/v1/2026.findings-eacl.206)** · EACL 2026 · LLM · Training-free
- **📋 [GHOST: Getting to the Bottom of Hallucinations with A Multi-round Consistency Benchmark](https://doi.org/10.1109/WACV61042.2026.00596)** · WACV 2026 · LLM · Training-free
- **📋 [FFE-Hallu: Hallucinations in Fixed Figurative Expressions: A Benchmark of Idioms and Proverbs in the Persian Language](https://doi.org/10.18653/v1/2026.eacl-long.241)** · EACL 2026 · LLM · Training-free
- **📋 [Constructing a Dataset for Hallucination Detection in Japanese Summarization with Fine-grained Faithfulness Labels](https://doi.org/10.18653/v1/2026.eacl-srw.15)** · EACL 2026 · LLM · Training-free
- **📋 [Halluverse-M^3: A multitask multilingual benchmark for hallucination in LLMs](https://arxiv.org/abs/2602.06920)** · arXiv · LLM · Training-free
- **📋 [HalluHard: A Hard Multi-Turn Hallucination Benchmark](https://arxiv.org/abs/2602.01031)** · arXiv · LLM · Training-free
- **📋 [MHB: Medical Hallucination Benchmark for Large Language Models in Complex Clinical Tasks](https://doi.org/10.1609/aaai.v40i45.41243)** · AAAI 2026 · LLM · Training-free
- **📋 [ESG-Bench: Benchmarking Long-Context ESG Reports for Hallucination Mitigation](https://doi.org/10.1609/aaai.v40i46.41281)** · AAAI 2026 · LLM · Training-based
- **📋 [Causal-HalBench: Uncovering LVLMs Object Hallucinations Through Causal Intervention](https://doi.org/10.1609/aaai.v40i40.40712)** · AAAI 2026 · VLM · Training-free
- **📋 [TempHalluc-Bench: Evaluating Temporal Hallucination in VideoLLM-Based Video Search and Information Extraction](https://doi.org/10.5120/ijca-1aef39d4b120)** · International Journal of Computer Applications 2026 · VLM · Training-free
- **📋 [EH-Benchmark Ophthalmic Hallucination Benchmark and Agent-Driven Top-Down Traceable Reasoning Workflow](https://doi.org/10.1016/j.inffus.2025.103631)** · INFFUS 2026 · LLM · Training-free
- **📋 [CDH-Bench: A Commonsense-Driven Hallucination Benchmark for Evaluating Visual Fidelity in Vision-Language Models](https://doi.org/10.1007/978-981-92-3504-9_17)** · ICIC 2026 · VLM · Training-free
- **📋 [AutoHall: Automated Factuality Hallucination Dataset Generation for Large Language Models](https://doi.org/10.1109/taslpro.2025.3635038)** · TASLP 2026 · LLM · Training-free
- **📋 [BHRAM-IL: A Benchmark for Hallucination Recognition and Assessment in Multiple Indian Languages](https://arxiv.org/abs/2512.01852)** · arXiv · LLM · Training-free
- **📋 [PHANTOM: A Benchmark for Hallucination Detection in Financial Long-Context QA](http://papers.nips.cc/paper_files/paper/2025/hash/b8badadce3f482ba340ff870f4894441-Abstract-Datasets_and_Benchmarks_Track.html)** · NeurIPS 2025 · LLM · Training-free
- **📋 [What Color Is It? A Text-Interference Multimodal Hallucination Benchmark](https://arxiv.org/abs/2511.13400)** · arXiv · VLM · Training-free
- **📋 [MUCH: A Multilingual Claim Hallucination Benchmark](https://arxiv.org/abs/2511.17081)** · arXiv · LLM · Training-free
- **📋 [MedHallu: A Comprehensive Benchmark for Detecting Medical Hallucinations in Large Language Models](https://doi.org/10.18653/v1/2025.emnlp-main.143)** · EMNLP 2025 · LLM · Training-free
- **📋 [Hallucination Benchmark for Speech Foundation Models](https://arxiv.org/abs/2510.16567)** · arXiv · MLLM(Omni) · Training-free
- **📋 [Confabulations from ACL Publications (CAP): A Dataset for Scientific Hallucination Detection](https://arxiv.org/abs/2510.22395)** · arXiv · LLM · Training-free
- **📋 [Challenging Multilingual LLMs: A New Taxonomy and Benchmark for Unraveling Hallucination in Translation](https://arxiv.org/abs/2510.24073)** · arXiv · LLM · Training-free
- **📋 [SHALE: A Scalable Benchmark for Fine-grained Hallucination Evaluation in LVLMs](https://doi.org/10.1145/3746027.3758308)** · ACM MM 2025 · VLM · Training-free
- **📋 [MIHBench: Benchmarking and Mitigating Multi-Image Hallucinations in Multimodal Large Language Models](https://doi.org/10.1145/3746027.3754993)** · ACM MM 2025 · VLM · Training-free
- **📋 [PerHalluEval: Persian Hallucination Evaluation Benchmark for Large Language Models](https://arxiv.org/abs/2509.21104)** · arXiv · LLM · Training-free
- **📋 [MIRAGE-Bench: LLM Agent is Hallucinating and Where to Find Them](https://arxiv.org/abs/2507.21017)** · arXiv · LLM · Training-free
- **📋 [TreeCut: A Synthetic Unanswerable Math Word Problem Dataset for LLM Hallucination Evaluation](https://doi.org/10.18653/v1/2025.acl-short.84)** · ACL 2025 · LLM · Training-free
- **📋 [Reefknot: A Comprehensive Benchmark for Relation Hallucination Evaluation, Analysis and Mitigation in Multimodal Large Language Models](https://doi.org/10.18653/v1/2025.findings-acl.322)** · ACL 2025 · VLM · Training-free
- **📋 [HalluLens: LLM Hallucination Benchmark](https://doi.org/10.18653/v1/2025.acl-long.1176)** · ACL 2025 · LLM · Training-free
- **📋 [CCHall: A Novel Benchmark for Joint Cross-Lingual and Cross-Modal Hallucinations Detection in Large Language Models](https://doi.org/10.18653/v1/2025.acl-long.1485)** · ACL 2025 · LLM · Training-free
- **📋 [PhD: A ChatGPT-Prompted Visual Hallucination Evaluation Dataset](https://openaccess.thecvf.com/content/CVPR2025/html/Liu_PhD_A_ChatGPT-Prompted_Visual_Hallucination_Evaluation_Dataset_CVPR_2025_paper.html)** · CVPR 2025 · VLM · Training-free
- **📋 [How LLMs React to Industrial Spatio-Temporal Data? Assessing Hallucination with a Novel Traffic Incident Benchmark Dataset](https://doi.org/10.18653/v1/2025.naacl-industry.4)** · NAACL 2025 · LLM · Training-free
- **📋 [FaithBench: A Diverse Hallucination Benchmark for Summarization by Modern LLMs](https://doi.org/10.18653/v1/2025.naacl-short.38)** · NAACL 2025 · LLM · Training-free
- **📋 [3D-GRAND: A Million-Scale Dataset for 3D-LLMs with Better Grounding and Less Hallucination](https://openaccess.thecvf.com/content/CVPR2025/html/Yang_3D-GRAND_A_Million-Scale_Dataset_for_3D-LLMs_with_Better_Grounding_and_CVPR_2025_paper.html)** · CVPR 2025 · VLM · Training-free
- **📋 [MultiHal: Multilingual Dataset for Knowledge-Graph Grounded Evaluation of LLM Hallucinations](https://arxiv.org/abs/2505.14101)** · arXiv · LLM · Training-free
- **📋 [Localizing Before Answering: A Hallucination Evaluation Benchmark for Grounded Medical Multimodal LLMs](https://arxiv.org/abs/2505.00744)** · arXiv · VLM · Training-free
- **📋 [HalluMix: A Task-Agnostic, Multi-Domain Benchmark for Real-World Hallucination Detection](https://arxiv.org/abs/2505.00506)** · arXiv · LLM · Training-free
- **📋 [MedHal: An Evaluation Dataset for Medical Hallucination Detection](https://arxiv.org/abs/2504.08596)** · arXiv · LLM · Training-free
- **📋 [How to Detect and Defeat Molecular Mirage: A Metric-Driven Benchmark for Hallucination in LLM-based Molecular Comprehension](https://arxiv.org/abs/2504.12314)** · arXiv · LLM · Training-free
- **📋 [K-HALU: Multiple Answer Korean Hallucination Benchmark for Large Language Models](https://openreview.net/forum?id=VnLhUogHYE)** · ICLR 2025 · LLM · Training-free
- **📋 [AVHBench: A Cross-Modal Hallucination Benchmark for Audio-Visual Large Language Models](https://openreview.net/forum?id=jTEKTdI3K9)** · ICLR 2025 · MLLM(Omni) · Training-free
- **📋 [Poly-FEVER: A Multilingual Fact Verification Benchmark for Hallucination Detection in Large Language Models](https://arxiv.org/abs/2503.16541)** · arXiv · LLM · Training-free
- **📋 [OAEI-LLM-T: A TBox Benchmark Dataset for Understanding Large Language Model Hallucinations in Ontology Matching](https://arxiv.org/abs/2503.21813)** · arXiv · LLM · Training-free
- **📋 [HalluVerse25: Fine-grained Multilingual Benchmark Dataset for LLM Hallucinations](https://arxiv.org/abs/2503.07833)** · arXiv · LLM · Training-free
- **📋 [Exploring Hallucination of Large Multimodal Models in Video Understanding: Benchmark, Analysis and Mitigation](https://arxiv.org/abs/2503.19622)** · arXiv · VLM · Training-free
- **📋 [MedHallTune: An Instruction-Tuning Benchmark for Mitigating Medical Hallucination in Vision-Language Models](https://arxiv.org/abs/2502.20780)** · arXiv · VLM · Training-free
- **📋 [Bi'an: A Bilingual Benchmark and Model for Hallucination Detection in Retrieval-Augmented Generation](https://arxiv.org/abs/2502.19209)** · arXiv · LLM · Training-free
- **📋 [MedHallBench: A New Benchmark for Assessing Hallucination in Medical Large Language Models](https://proceedings.mlr.press/v281/zuo25b.html)** · AAAI Bridge Program 2025 · LLM · Training-free
- **📋 [MHBench: Demystifying Motion Hallucination in VideoLLMs](https://doi.org/10.1609/aaai.v39i4.32463)** · AAAI 2025 · LLM · Training-free
- **📋 [CodeHalu: Investigating Code Hallucinations in LLMs via Execution-based Verification](https://doi.org/10.1609/aaai.v39i24.34717)** · AAAI 2025 · LLM · Training-free
- **📋 [Measuring and Mitigating Hallucinations in Vision-Language Dataset Generation for Remote Sensing](https://arxiv.org/abs/2501.14905)** · arXiv · VLM · Training-free
- **📋 [KG-FPQ: Evaluating Factuality Hallucination in LLMs with Knowledge Graph-based False Premise Questions](https://aclanthology.org/2025.coling-main.698/)** · COLING 2025 · LLM · Training-free
- **📋 [ReSelfVerMM: mitigating hallucination in multimodal LLMs through dataset reconstruction and self-verification](https://doi.org/10.1117/12.3072360)** · Second International Conference on Image Processing and Artificial Intelligence (ICIPAI 2025) 2025 · VLM · Training-free
- **📋 [Hallucination-Aware Multimodal Benchmark for Gastrointestinal Image Analysis with Large Vision-Language Models](https://doi.org/10.1007/978-3-032-05127-1_23)** · MICCAI 2025 · VLM · Training-free
- **📋 [ChartInsighter: An Approach for Mitigating Hallucination in Time-series Chart Summary Generation with A Benchmark Dataset](https://doi.org/10.1109/TVCG.2025.3567122)** · IEEE Trans. Vis. Comput. Graph. 2025 · LLM · Training-free
- **📋 [C-FAITH: A Chinese Fine-Grained Benchmark for Automated Hallucination Evaluation](https://doi.org/10.1145/3746252.3761604)** · CIKM 2025 · LLM · Training-free
- **📋 [The HalluRAG Dataset: Detecting Closed-Domain Hallucinations in RAG Applications Using an LLM's Internal States](https://arxiv.org/abs/2412.17056)** · arXiv · LLM · Training-free
- **📋 [ViBe: A Text-to-Video Benchmark for Evaluating Hallucination in Large Multimodal Models](https://arxiv.org/abs/2411.10867)** · arXiv · VLM · Training-free
- **📋 [DAHL: Domain-specific Automated Hallucination Evaluation of Long-Form Text through a Benchmark Dataset in Biomedicine](https://arxiv.org/abs/2411.09255)** · arXiv · LLM · Training-free
- **📋 [ToolBeHonest: A Multi-level Hallucination Diagnostic Benchmark for Tool-Augmented Large Language Models](https://doi.org/10.18653/v1/2024.emnlp-main.637)** · EMNLP 2024 · LLM · Training-free
- **📋 [DiaHalu: A Dialogue-level Hallucination Evaluation Benchmark for Large Language Models](https://doi.org/10.18653/v1/2024.findings-emnlp.529)** · EMNLP 2024 · LLM · Training-free
- **📋 [Collu-Bench: A Benchmark for Predicting Language Model Hallucinations in Code](https://arxiv.org/abs/2410.09997)** · arXiv · LLM · Training-free
- **📋 [HaloQuest: A Visual Hallucination Dataset for Advancing Multimodal Reasoning](https://doi.org/10.1007/978-3-031-72980-5_17)** · ECCV 2024 · VLM · Training-free
- **📋 [Order Matters in Hallucination: Reasoning Order as Benchmark and Reflexive Prompting for Large-Language-Models](https://arxiv.org/abs/2408.05093)** · arXiv · LLM · Training-free
- **📋 [HalluDial: A Large-Scale Benchmark for Automatic Dialogue-Level Hallucination Evaluation](https://arxiv.org/abs/2406.07070)** · arXiv · LLM · Training-free
- **📋 [DefAn: Definitive Answer Dataset for LLMs Hallucination Evaluation](https://arxiv.org/abs/2406.09155)** · arXiv · LLM · Training-free
- **📋 [THRONE: An Object-Based Hallucination Benchmark for the Free-Form Generations of Large Vision-Language Models](https://doi.org/10.1109/CVPR52733.2024.02571)** · CVPR 2024 · VLM · Training-free
- **📋 [RefChecker: Reference-based Fine-grained Hallucination Checker and Benchmark for Large Language Models](https://arxiv.org/abs/2405.14486)** · arXiv · LLM · Training-free
- **📋 [The Hallucinations Leaderboard -- An Open Effort to Measure Hallucinations in Large Language Models](https://arxiv.org/abs/2404.05904)** · arXiv · LLM · Training-free
- **📋 [HypoTermQA: Hypothetical Terms Dataset for Benchmarking Hallucination Tendency of LLMs](https://doi.org/10.18653/v1/2024.eacl-srw.9)** · EACL 2024 · LLM · Training-free
- **📋 [Hallucination Benchmark in Medical Visual Question Answering](https://openreview.net/forum?id=vxlXqOj4zv)** · Unlabeled · VLM · Training-free
- **📋 [ERBench: An Entity-Relationship based Automatically Verifiable Hallucination Benchmark for Large Language Models](http://papers.nips.cc/paper_files/paper/2024/hash/5ef9853a6cdea40ae3e301a6d8dc32b5-Abstract-Datasets_and_Benchmarks_Track.html)** · Unlabeled · LLM · Training-free
- **📋 [OAEI-LLM: A Benchmark Dataset for Understanding Large Language Model Hallucinations in Ontology Matching](https://ceur-ws.org/Vol-3953/361.pdf)** · HGAIS@ISWC 2024 · LLM · Training-free
- **📋 [MASSIVE Multilingual Abstract Meaning Representation: A Dataset and Baselines for Hallucination Detection](https://doi.org/10.18653/v1/2024.starsem-1.1)** · 13th Joint Conference on Lexical and Computational Semantics (*SEM 2024) 2024 · LLM · Training-free
- **📋 [German also Hallucinates! Inconsistency Detection in News Summaries with the Absinth Dataset](https://aclanthology.org/2024.lrec-main.680)** · LREC/COLING 2024 · LLM · Training-free
- **📋 [Detection, Diagnosis, and Explanation: A Benchmark for Chinese Medial Hallucination Evaluation](https://aclanthology.org/2024.lrec-main.428)** · LREC/COLING 2024 · LLM · Training-free
- **📋 [HalOmi: A Manually Annotated Benchmark for Multilingual Hallucination and Omission Detection in Machine Translation](https://doi.org/10.18653/v1/2023.emnlp-main.42)** · EMNLP 2023 · LLM · Training-free
- **📋 [A New Benchmark and Reverse Validation Method for Passage-level Hallucination Detection](https://doi.org/10.18653/v1/2023.findings-emnlp.256)** · EMNLP 2023 · LLM · Training-free
- **📋 [Negative Object Presence Evaluation (NOPE) to Measure Object Hallucination in Vision-Language Models](https://arxiv.org/abs/2310.05338)** · arXiv · VLM · Training-free

</details>

## 📚 Surveys
> 32 survey / review / taxonomy papers are listed separately (also kept in the main list below, marked 📚).

<details open>
<summary>📚 Survey List (32 papers — click to collapse / expand)</summary>

- **📚 [Model stability and hallucination under the data-knowledge dual-drive paradigm: a survey](https://doi.org/10.1117/12.3110427)** · ICML 2026 · LLM · Training-free
- **📚 [Distorted or Fabricated? A Survey on Hallucination in Video LLMs](https://aclanthology.org/2026.findings-acl.1325/)** · ACL 2026 · VLM · Training-free
- **📚 [DECK: A Consistency x Confidence Taxonomy of LLM Hallucinations](https://arxiv.org/abs/2606.02289)** · arXiv · LLM · Training-free
- **📚 [A Geometric Taxonomy of Hallucinations in LLMs](https://arxiv.org/abs/2602.13224)** · arXiv · LLM · Training-free
- **📚 [Survey on Hallucination in Reasoning Large Language Model: Evaluation, Taxonomy, Intervention, and Open Issues](https://doi.org/10.3724/2096-7004.di.2025.0131)** · Data Intell. 2026 · LLM · Training-free
- **📚 [Loki’s Dance of Illusions: A Comprehensive Survey of Hallucination in Large Language Models](https://doi.org/10.1109/tcss.2026.3661295)** · IEEE Transactions on Computational Social Systems 2026 · LLM · Training-free
- **📚 [Large language models hallucination: A comprehensive survey](https://doi.org/10.1016/j.cosrev.2026.100970)** · Comput. Sci. Rev. 2026 · LLM · Training-free
- **📚 [House of Mirrors: A Survey on Hallucination Detection and Mitigation via Decoding Techniques in Language Models](https://doi.org/10.1007/978-3-032-03072-6_9)** · Lecture Notes in Networks and Systems 2026 · LLM · Training-free
- **📚 [Hallucination to truth: a review of fact-checking and factuality evaluation in large language models](https://doi.org/10.1007/s10462-025-11454-w)** · Artif. Intell. Rev. 2026 · LLM · Training-free
- **📚 [Attribution Techniques for Mitigating Hallucinated Information in RAG Systems: A Survey](https://doi.org/10.1109/ICAIIC68212.2026.11454197)** · ICAIIC 2026 · LLM · Training-free
- **📚 [A Taxonomy of Machine Hallucination in Radiology](https://doi.org/10.1148/ryai.250203)** · Radiology: Artificial Intelligence 2026 · LLM · Training-free
- **📚 [A Survey of Multimodal Hallucination Evaluation and Detection](https://doi.org/10.1007/s11263-026-02756-9)** · IJCV 2026 · VLM · Training-free
- **📚 [A Survey of Hallucination in Large Language Models](https://doi.org/10.12677/airr.2026.151016)** · Artificial Intelligence and Robotics Research 2026 · LLM · Training-free
- **📚 [A Concise Review of Hallucinations in LLMs and their Mitigation](https://arxiv.org/abs/2512.02527)** · arXiv · LLM · Training-free
- **📚 [Review of Hallucination Understanding in Large Language and Vision Models](https://arxiv.org/abs/2510.00034)** · arXiv · LLM · Training-free
- **📚 [Mitigating Hallucination in Large Language Models (LLMs): An Application-Oriented Survey on RAG, Reasoning, and Agentic Systems](https://arxiv.org/abs/2510.24476)** · arXiv · LLM · Training-free
- **📚 [LLM-based Agents Suffer from Hallucinations: A Survey of Taxonomy, Methods, and Directions](https://arxiv.org/abs/2509.18970)** · arXiv · LLM · Training-free
- **📚 [A comprehensive taxonomy of hallucinations in Large Language Models](https://arxiv.org/abs/2508.01781)** · arXiv · LLM · Training-free
- **📚 [🧜Siren’s Song in the AI Ocean: A Survey on Hallucination in Large Language Models](https://doi.org/10.1162/coli.a.16)** · Comput. Linguistics 2025 · LLM · Training-free
- **📚 [Hallucination Detection in Foundation Models for Decision-Making: A Flexible Definition and Review of the State of the Art](https://doi.org/10.1145/3716846)** · ACM Comput. Surv. 2025 · LLM · Training-free
- **📚 [A Scoping Review of Natural Language Processing in Addressing Medically Inaccurate Information: Errors, Misinformation, and Hallucination](https://doi.org/10.1016/j.jbi.2025.104866)** · J. Biomed. Informatics 2025 · LLM · Training-free
- **📚 [A Review of Faithfulness Metrics for Hallucination Assessment in Large Language Models](https://doi.org/10.1109/JSTSP.2025.3579203)** · IEEE J. Sel. Top. Signal Process. 2025 · LLM · Training-free
- **📚 [A Comprehensive Survey of Hallucination in Large Language, Image, Video and Audio Foundation Models](https://doi.org/10.18653/v1/2024.findings-emnlp.685)** · EMNLP 2024 · MLLM(Omni) · Training-free
- **📚 [A Survey of Hallucination in Large Visual Language Models](https://arxiv.org/abs/2410.15359)** · arXiv · VLM · Training-free
- **📚 [Can Knowledge Graphs Reduce Hallucinations in LLMs? : A Survey](https://doi.org/10.18653/v1/2024.naacl-long.219)** · NAACL 2024 · LLM · Training-free
- **📚 [Hallucination of Multimodal Large Language Models: A Survey](https://arxiv.org/abs/2404.18930)** · arXiv · VLM · Training-free
- **📚 [A Survey of Automatic Hallucination Evaluation on Natural Language Generation](https://arxiv.org/abs/2404.12041)** · arXiv · LLM · Training-free
- **📚 [A Survey on Large Language Model Hallucination via a Creativity Perspective](https://arxiv.org/abs/2402.06647)** · arXiv · LLM · Training-free
- **📚 [A Survey on Hallucination in Large Vision-Language Models](https://arxiv.org/abs/2402.00253)** · arXiv · VLM · Training-free
- **📚 [LightHouse: A Survey of AGI Hallucination](https://arxiv.org/abs/2401.06792)** · arXiv · LLM · Training-free
- **📚 [A Comprehensive Survey of Hallucination Mitigation Techniques in Large Language Models](https://arxiv.org/abs/2401.01313)** · arXiv · LLM · Training-free
- **📚 [Cognitive Mirage: A Review of Hallucinations in Large Language Models](https://ceur-ws.org/Vol-3818/paper2.pdf)** · LKM@IJCAI 2024 · LLM · Training-free

</details>

## 📚 Paper List
> Grouped by **model type** (LLM / VLM / MLLM), then expanded by year inside each group; click a header to expand / collapse. Format per entry: **Title** · venue/year · model · method · 💻code. Title links prefer the official venue version. 📋 = Benchmark paper, 📚 = Survey paper. Full abstracts and multi-dimensional filtering are available in the interactive website [`docs/index.html`](docs/index.html). PRs welcome.

<details>
<summary>🤖 LLM · 1235 篇</summary>

<details>
<summary>📅 2027 · 5 papers</summary>

- **[Uncovering Reasoning Failures: Hallucination Detection via Semantic Probing and Attention Tracking](https://doi.org/10.1007/978-981-92-2480-7_23)** · Lecture Notes in Computer Science 2027 · LLM · Training-free
- **[Quantum Entropy–Driven Temperature Scaling for Hallucination Mitigation in Generative Models](https://doi.org/10.1007/978-3-032-28379-5_48)** · Lecture Notes in Networks and Systems 2027 · LLM · Training-free
- **[Combining NotebookLM and Gemini Gems to Reduce Hallucination and Curriculum Misalignment in Programming Education: System Design and Early Evidence](https://doi.org/10.1007/978-3-032-32115-2_45)** · Lecture Notes in Computer Science 2027 · LLM · Training-free
- **[Beyond Statistical Divergence: A Hybrid Calibration Framework for Decoupling Hallucination in Large Language Models](https://doi.org/10.1007/978-981-92-2480-7_9)** · Lecture Notes in Computer Science 2027 · LLM · Training-free
- **[A Multi-agent Framework for Factuality Hallucination Detection Using Complex Knowledge Graph](https://doi.org/10.1007/978-981-92-2480-7_10)** · Lecture Notes in Computer Science 2027 · LLM · Training-free

</details>

<details>
<summary>📅 2026 · 475 papers</summary>

- **[Decomposed Entailment for Factuality Checking and Hallucination Detection](https://arxiv.org/abs/2608.05823)** · arXiv · LLM · Training-free
- **[Hallucinations on the Board: Tool-Augmented Evaluation of LLM Chess Commentary](https://arxiv.org/abs/2608.04240)** · arXiv · LLM · Training-free
- **[HalluTruthQA-4K: A Fine-Grained Corpus and Annotation Process for Arabic Hallucination Detection and Truth Verification](https://arxiv.org/abs/2608.03966)** · arXiv · LLM · Training-free
- **[Eliciting Intrinsic Hallucinations in LLMs via Semantically Equivalent Adversarial Attacks](https://arxiv.org/abs/2608.04286)** · arXiv · LLM · Training-based
- **[Detecting Hallucinations and Recovering Verified Answers in Arabic Islamic Question Answering](https://arxiv.org/abs/2608.03720)** · arXiv · LLM · Training-based
- **[Can Humans Dream of Electric Sheep? Human-Written Samples for Fine-Grained Vision-and-Language Hallucination Benchmarking](https://arxiv.org/abs/2608.01021)** · arXiv · LLM · Training-free
- **[Tracing the Cascade: A Topology-Aware Evaluation Framework for Scientific Agent Hallucinations](https://arxiv.org/abs/2608.00711)** · arXiv · LLM · Training-free
- **[Heaven-Sent or Hell-Bent? Benchmarking the Intelligence and Defectiveness of LLM Hallucinations](https://doi.org/10.1145/3770854.3785704)** · KDD 2026 · LLM · Training-free
- **[AI and Authenticity in Islamic Research: A Critical Evaluation of Generative AI Reliability, Hallucination, and Source Fidelity in Quranic, Hadith, and Fiqh Knowledge](https://arxiv.org/abs/2607.28237)** · arXiv · LLM · Training-free
- **[The Cost of Knowing: A Resource-Aware Protocol for Benchmarking Hallucination Beyond Static Leaderboards](https://arxiv.org/abs/2607.24063)** · arXiv · LLM · Training-free
- **[D-Score: A Spectral Hidden-State Signal for Hallucination Detection in Large Language Models](https://arxiv.org/abs/2607.24586)** · arXiv · LLM · Training-free
- **[Hallucination Rates in Language Generation](https://arxiv.org/abs/2607.23361)** · arXiv · LLM · Training-free
- **[Reasoning Denoiser: Denoising Reasoning Traces for Hallucination Detection in Large Reasoning Models](https://arxiv.org/abs/2607.22098)** · arXiv · LLM · Training-free
- **[SIRIN: A Unified Toolkit for Detecting Contextual Hallucinations in Retrieval-Augmented and Memory-Grounded LLM Systems](https://arxiv.org/abs/2608.00033)** · arXiv · LLM · Training-free
- **[Zero Hallucination, by Construction: Hallucination-Aware Layered Oversight for Trustworthy Enterprise AI](https://arxiv.org/abs/2607.17883)** · arXiv · LLM · Training-free
- **[Understanding Why Language Models Hallucinate: Testing Reasoning Against Priors](https://arxiv.org/abs/2607.00447)** · arXiv · LLM · Training-free
- **[To Answer or to Abstain: Mitigating Search-Agent Hallucinations via Abstention-Aware Reinforcement Learning](https://arxiv.org/abs/2607.10738)** · arXiv · LLM · Training-based
- **[SciForma: Structure-Faithful Generation of Scientific Diagrams](https://arxiv.org/abs/2607.18091)** · arXiv · LLM · Training-free
- **[Readable but Not Controllable: Neuron-Level Evidence for Medical LLM Hallucination](https://arxiv.org/abs/2607.00158)** · arXiv · LLM · Training-free
- **[Protective Capacity Hallucination: When Large Language Models Claim Nonexistent Capabilities](https://arxiv.org/abs/2607.13596)** · arXiv · LLM · Training-free
- **[Prompt Design at Scale: How Format, Instruction Count, and Context Length Shape Instruction Adherence and Hallucination in Large Language Models](https://arxiv.org/abs/2607.19257)** · arXiv · LLM · Training-free
- **[Phantom References: Hallucinated Citations That Survive Peer Review at Top-Tier Conferences](https://arxiv.org/abs/2607.00738)** · arXiv · LLM · Training-free
- **[Operational Hallucination and Safety Drift in AI Agents](https://arxiv.org/abs/2607.18366)** · arXiv · LLM · Training-free
- **[Naming the Concepts Classifiers Rely On: Language-Anchored Decomposition for Faithful Explanation](https://arxiv.org/abs/2607.07264)** · arXiv · LLM · Training-free
- **[Mitigating Package Hallucinations in Large Language Models via Model Editing](https://arxiv.org/abs/2607.02052)** · arXiv · LLM · Training-based
- **[Mitigating Factual Hallucination in Large Reasoning Models via Mixed-Mode Advantage Regularization](https://arxiv.org/abs/2607.05861)** · arXiv · LLM · Training-free
- **[Hallucination Self-Play: Bootstrapping Reinforced Detector via Evolved Generator](https://arxiv.org/abs/2607.07993)** · arXiv · LLM · Training-free
- **[Hallucination Detector: A hybrid LLM and Semantic Scholar tool calling for detecting hallucination in scientific literature on AtomGPT.org](https://arxiv.org/abs/2607.09774)** · arXiv · LLM · Training-free
- **📋 [HalluTruthQA: A Fine-Grained Benchmark for Hallucination Detection, Localization, and Explanation in Arabic Question Answering](https://arxiv.org/abs/2607.20219)** · arXiv · LLM · Training-free
- **[HALLMARK: Diagnosing Three Failure Modes in LLM Citation Verifiers](https://arxiv.org/abs/2607.18360)** · arXiv · LLM · Training-free
- **[Grounded Optimization: A Layered Engineering Framework for Reducing LLM Hallucination in Automated Personal Document Rewriting](https://arxiv.org/abs/2607.01457)** · arXiv · LLM · Training-free
- **[Game Theory Driven Multi-Agent Framework Mitigates Language Model Hallucination](https://arxiv.org/abs/2607.08403)** · arXiv · LLM · Training-free
- **[From Judgments to Issues: Structured Extraction of Legal Reasoning with Citation-Hallucination Control](https://arxiv.org/abs/2607.03325)** · arXiv · LLM · Training-free
- **[Faithful by Design: Evaluating and Improving LLM-Generated Clinical Trial Summaries for Multi-Stakeholder Audiences](https://arxiv.org/abs/2607.09932)** · arXiv · LLM · Training-free
- **[Evidence-Grounded Verified Agentic Reasoning: A Path Toward Eliminating LLM Hallucination in Empirical Inference via Tool-Attested Kernel Proofs](https://arxiv.org/abs/2607.12650)** · arXiv · LLM · Training-free
- **[Diversity-Oriented Fine-Tuning for Uncertainty-Based Hallucination Detection](https://arxiv.org/abs/2607.16643)** · arXiv · LLM · Training-free
- **[Directional Hallucinations: Ideological Drift in News-Grounded LLM Question Answering](https://arxiv.org/abs/2607.20487)** · arXiv · LLM · Training-free
- **[Detecting Hallucinations in Retrieval-Augmented Generation through Grounding-Aware Sensitivity by Perturbation (GASP)](https://arxiv.org/abs/2607.04223)** · arXiv · LLM · Training-free
- **[Deceptive Grounding: Entity Attribution Failure in Clinical Retrieval-Augmented Generation](https://arxiv.org/abs/2607.09349)** · arXiv · LLM · Training-free
- **[CrossHallu: Do Hallucination Signals Generalize Across Languages and Domains in Large Language Model's Internals?](https://arxiv.org/abs/2607.04029)** · arXiv · LLM · Training-free
- **[Confidently Wrong: Detecting Hallucinations in Financial Question Answering from LLM Internal States](https://arxiv.org/abs/2607.11414)** · arXiv · LLM · Training-free
- **[Chemical Chain-of-Thought Functions as a Hallucination-Prone Molecular Scratchpad](https://arxiv.org/abs/2607.20935)** · arXiv · LLM · Training-free
- **[Beyond Document Grounding: Span-Level Hallucination Detection over Code, Tool Output, and Documents](https://arxiv.org/abs/2607.00895)** · arXiv · LLM · Training-based
- **[Axolotl3D: a Unified Framework for Faithful 3D Shape Completion](https://arxiv.org/abs/2607.20660)** · arXiv · LLM · Training-free
- **📋 [ArtChart: A Benchmark for Faithful Artistic Chart Generation with Integrated Text Rendering](https://arxiv.org/abs/2607.16060)** · arXiv · LLM · Training-free
- **[Anatomically Faithful but Temporally Diffuse: Auditing Attribution for Left-Ventricular Ejection-Fraction Estimation from Echocardiography](https://arxiv.org/abs/2607.13738)** · arXiv · LLM · Training-free
- **[Why LLMs Hallucinate on Structured Knowledge: A Mechanistic Analysis of Reasoning over Linearized Representations](https://aclanthology.org/2026.acl-long.914/)** · ACL 2026 · LLM · Training-free
- **[When Personalization Misleads: Understanding and Mitigating Hallucinations in Personalized LLMs](https://aclanthology.org/2026.findings-acl.395/)** · ACL 2026 · LLM · Training-free
- **[Understanding New-Knowledge-Induced Factual Hallucinations in LLMs: Analysis and Interpretation](https://aclanthology.org/2026.findings-acl.358/)** · ACL 2026 · LLM · Training-free
- **[Two Pathways to Truthfulness: On the Intrinsic Encoding of LLM Hallucinations](https://aclanthology.org/2026.acl-long.1173/)** · ACL 2026 · LLM · Training-free
- **[The Reasoning Trap: How Enhancing LLM Reasoning Amplifies Tool Hallucination](https://aclanthology.org/2026.acl-long.376/)** · ACL 2026 · LLM · Training-free
- **[The Digital Dunning-Kruger Effect: Decoupling Hallucinations via Geometric Hidden-state Observation for Semantic Truthfulness](https://aclanthology.org/2026.acl-long.993/)** · ACL 2026 · LLM · Training-free
- **[TPA: Next Token Probability Attribution for Detecting Hallucinations in RAG](https://aclanthology.org/2026.acl-long.1159/)** · ACL 2026 · LLM · Training-free
- **[Streaming Hallucination Detection in Long Chain-of-Thought Reasoning](https://aclanthology.org/2026.findings-acl.1064/)** · ACL 2026 · LLM · Training-free
- **[Stable-RAG: Mitigating Retrieval-Permutation-Induced Hallucinations in Retrieval-Augmented Generation](https://aclanthology.org/2026.acl-long.1188/)** · ACL 2026 · LLM · Training-free
- **[Re³: Relevance &amp; Recency Retrieval for Mitigating Temporal Hallucination](https://aclanthology.org/2026.acl-long.1180/)** · ACL 2026 · LLM · Training-free
- **📋 [Rethinking Evaluation for LLM Hallucination Detection: A Desiderata, A New RAG-based Benchmark, New Insights](https://aclanthology.org/2026.acl-long.680/)** · ACL 2026 · LLM · Training-free
- **[Reducing Hallucinations in LLMs via Factuality-Aware Preference Learning](https://aclanthology.org/2026.findings-acl.1968/)** · ACL 2026 · LLM · Training-based
- **[ReFL: Reflective Feedback Learning for Hallucination Detection of Large Language Models](https://aclanthology.org/2026.acl-long.899/)** · ACL 2026 · LLM · Training-free
- **[RLSeek: Evidence-Grounded Reasoning for RAG Hallucination Detection](https://aclanthology.org/2026.acl-long.1492/)** · ACL 2026 · LLM · Training-free
- **[RFS-Guard: Detecting Reasoning Hallucinations via Cross-Phase Routing Focus in Large Reasoning Models](https://aclanthology.org/2026.acl-long.885/)** · ACL 2026 · LLM · Training-free
- **[Principled Detection of Hallucinations in Large Language Models via Multiple Testing](https://aclanthology.org/2026.findings-acl.1705/)** · ACL 2026 · LLM · Training-free
- **[PretrainRL: Alleviating Factuality Hallucination of Large Language Models at the Beginning](https://aclanthology.org/2026.findings-acl.910/)** · ACL 2026 · LLM · Training-based
- **📋 [PROBE: PROcess-Based BEnchmark for Hallucination Detection](https://aclanthology.org/2026.findings-acl.2099/)** · ACL 2026 · LLM · Training-free
- **[PRISM: Probing Reasoning, Instruction, and Source Memory in LLM Hallucinations](https://aclanthology.org/2026.acl-long.1551/)** · ACL 2026 · LLM · Training-free
- **[Numerical Hallucinations in Retrieval-Augmented Generation: Detection and Analysis](https://doi.org/10.1145/3805712.3809882)** · SIGIR 2026 · LLM · Training-free
- **📚 [Model stability and hallucination under the data-knowledge dual-drive paradigm: a survey](https://doi.org/10.1117/12.3110427)** · ICML 2026 · LLM · Training-free
- **[Mitigating Legal Hallucinations via Symbolic Constraints and Analogical Precedents](https://aclanthology.org/2026.acl-long.633/)** · ACL 2026 · LLM · Training-free
- **[MeasHalu: Mitigation of Scientific Measurement Hallucinations for Large Language Models with Enhanced Reasoning](https://aclanthology.org/2026.findings-acl.1386/)** · ACL 2026 · LLM · Training-free
- **[MARCH: Multi-Agent Reinforced Check for Hallucination](https://aclanthology.org/2026.acl-long.1828/)** · ACL 2026 · LLM · Training-free
- **[Lost in Diffusion: Uncovering Hallucination Patterns and Failure Modes in Diffusion Large Language Models](https://aclanthology.org/2026.findings-acl.882/)** · ACL 2026 · LLM · Training-free
- **[Logical Consistency as a Bridge: Improving LLM Hallucination Detection via Label Constraint Modeling between Responses and Self-Judgments](https://aclanthology.org/2026.acl-long.286/)** · ACL 2026 · LLM · Training-free
- **[Logic Matters in Lightweight Hallucination Classification for RAG System](https://aclanthology.org/2026.acl-long.73/)** · ACL 2026 · LLM · Training-free
- **[LAFaCT: Attribution-based Localization and Focused Sequential Analysis of Fact-Critical Tokens for Hallucination Detection](https://aclanthology.org/2026.acl-long.312/)** · ACL 2026 · LLM · Training-free
- **[Knowledge Injection Exists in MoE? Exploring Expert-Aware Contrast Decoding in MoE for Mitigating LLMs&apos; Hallucinations](https://aclanthology.org/2026.acl-long.1824/)** · ACL 2026 · LLM · Training-free
- **[JointCQ: Improving Factual Hallucination Detection with Joint Claim and Query Generation](https://aclanthology.org/2026.findings-acl.58/)** · ACL 2026 · LLM · Training-free
- **[Hallucinations as Orthogonal Noise: Inference-Time Manifold Alignment via Dynamic Contextual Orthogonalization](https://aclanthology.org/2026.findings-acl.1822/)** · ACL 2026 · LLM · Training-free
- **📋 [Hallucination Detection in Long-Form Text Generated by LLMs: A Benchmark and a Hyper-Relational Knowledge Graph Approach](https://aclanthology.org/2026.findings-acl.1673/)** · ACL 2026 · LLM · Training-free
- **[Hallucination Detection in LLMs with Topological Divergence on Attention Graphs](https://aclanthology.org/2026.acl-long.704/)** · ACL 2026 · LLM · Training-free
- **[HalluGuard: Evidence-Grounded Small Reasoning Models to Mitigate Hallucinations in Retrieval-Augmented Generation](https://aclanthology.org/2026.findings-acl.835/)** · ACL 2026 · LLM · Training-free
- **[HalluCitation Matters: Revealing the Impact of Hallucinated References with 300 Hallucinated Papers in ACL Conferences](https://aclanthology.org/2026.acl-long.2189/)** · ACL 2026 · LLM · Training-free
- **[HAT: Hallucination Annotation for Translation](https://aclanthology.org/2026.acl-long.721/)** · ACL 2026 · LLM · Training-free
- **[Grad Detect: Gradient-Based Hallucination Detection in LLMs](https://arxiv.org/abs/2606.24790)** · ICML 2026 · LLM · Training-free
- **[Generating Effective CoT Traces for Mitigating Causal Hallucination](https://aclanthology.org/2026.findings-acl.264/)** · ACL 2026 · LLM · Training-free
- **[From Proof to Program: Characterizing Tool-Induced Reasoning Hallucinations in Large Language Models](https://aclanthology.org/2026.acl-long.1951/)** · ACL 2026 · LLM · Training-based
- **[Fine-Grained Detection of Context-Grounded Hallucinations Using LLMs](https://aclanthology.org/2026.findings-acl.1907/)** · ACL 2026 · LLM · Training-free
- **[FaithLens: Detecting and Explaining Faithfulness Hallucination](https://aclanthology.org/2026.findings-acl.689/)** · ACL 2026 · LLM · Training-free
- **[Evidence-Aligned Entity Verification for Hallucination Detection in Retrieval-Augmented Generation](https://aclanthology.org/2026.findings-acl.1477/)** · ACL 2026 · LLM · Training-free
- **[Enhancing Hallucination Detection via Future Context](https://aclanthology.org/2026.findings-acl.35/)** · ACL 2026 · LLM · Training-free
- **[Efficient Hallucination Detection in Automatic Code Generation](https://aclanthology.org/2026.findings-acl.2143/)** · ACL 2026 · LLM · Training-free
- **[Efficient Hallucination Detection for LLMs Using Uncertainty-Aware Attention Heads](https://arxiv.org/abs/2505.20045)** · ICML 2026 · LLM · Training-free
- **[Dynamic PMI-Guided Contrastive Decoding Reduces Hallucination in Large Language Models: A Unified Framework of Fine-Grained Input Transformations](https://aclanthology.org/2026.findings-acl.1212/)** · ACL 2026 · LLM · Training-free
- **[Dialectic-Med: Mitigating Diagnostic Hallucinations via Counterfactual Adversarial Multi-Agent Debate](https://aclanthology.org/2026.findings-acl.1837/)** · ACL 2026 · LLM · Training-free
- **[Detecting Hallucinations in SpeechLLMs at Inference Time Using Attention Maps](https://aclanthology.org/2026.findings-acl.2147/)** · ACL 2026 · LLM · Training-free
- **[Detecting Hallucinations in Retrieval-Augmented Generation via Semantic-level Internal Reasoning Graph](https://aclanthology.org/2026.findings-acl.1385/)** · ACL 2026 · LLM · Training-free
- **[CoDA: Restoring Contextual Dominance via Copy-Encouraged Attention Intervention for Mitigating RAG Hallucinations](https://aclanthology.org/2026.findings-acl.576/)** · ACL 2026 · LLM · Training-free
- **[CausalGaze: Unveiling Hallucinations via Counterfactual Graph Intervention in Large Language Models](https://aclanthology.org/2026.findings-acl.1943/)** · ACL 2026 · LLM · Training-free
- **[Calibrating Uncertainty with Cross-Model Consistency for LLM Hallucination Mitigation](https://doi.org/10.1145/3805712.3809846)** · SIGIR 2026 · LLM · Training-free
- **[CSMAD: Hallucination Detection via Multi-Agent Debate with NLI-Verified Contradictory Statements](https://doi.org/10.1145/3805712.3808508)** · SIGIR 2026 · LLM · Training-free
- **[Beyond Output Confidence: Epistemic-Aware Hallucination Detection with Answer-Level Signals](https://aclanthology.org/2026.findings-acl.674/)** · ACL 2026 · LLM · Training-free
- **[Beyond Noise: Characterizing Creative Potential in Unverifiable LLM Hallucinations](https://aclanthology.org/2026.acl-long.554/)** · ACL 2026 · LLM · Training-free
- **[Awakening Dormant Experts: Counterfactual Routing to Mitigate MoE Hallucinations](https://aclanthology.org/2026.acl-long.2187/)** · ACL 2026 · LLM · Training-free
- **[Anchoring the Cache: Mitigating Contextual Hallucination in KV-Compressed Long-Context Summarization](https://aclanthology.org/2026.acl-long.1542/)** · ACL 2026 · LLM · Training-free
- **[Zero-source LLM Hallucination Detection with Human-like Criteria Probing](https://arxiv.org/abs/2606.12900)** · arXiv · LLM · Training-free
- **[Who Checks the Citations? Benchmarking Legal Hallucination Detection](https://arxiv.org/abs/2606.21155)** · arXiv · LLM · Training-free
- **[Whisper Hallucination Detection and Mitigation via Hidden Representation Steering and Sparse AutoEncoders](https://arxiv.org/abs/2606.07473)** · arXiv · LLM · Training-free
- **[TriLens: Per-Layer Logit-Lens Entropy for White-Box Hallucination Detection](https://arxiv.org/abs/2606.01033)** · arXiv · LLM · Training-free
- **[Towards Lightweight Reliability: Using Soft Prompts for Hallucination Mitigation in Large Language Models](https://arxiv.org/abs/2606.00919)** · arXiv · LLM · Training-free
- **[Thermodynamic Signatures of Reasoning: Free-Energy and Spectral-Form-Factor Diagnostics for Hallucination Detection in Large Language Models](https://arxiv.org/abs/2606.19404)** · arXiv · LLM · Training-free
- **[TTFT-Aware Graph Chain-of-Thought:Distance-Indexed Neural A* for Low-Hallucination Multi-Hop Medical Reasoning](https://arxiv.org/abs/2606.23108)** · arXiv · LLM · Training-free
- **[Score-Control for Hallucination Reduction in Diffusion Models](https://arxiv.org/abs/2606.00377)** · arXiv · LLM · Training-free
- **[SafeLLM: Extraction as a Hallucination-Resistant Alternative to Rewriting in Safety-Critical Settings](https://arxiv.org/abs/2606.12897)** · arXiv · LLM · Training-free
- **[Reducing Hallucinations in Complex Question Answering using Simple Graph-based Retrieval-Augmented Generation (long version)](https://arxiv.org/abs/2606.05901)** · arXiv · LLM · Training-free
- **[Quickest Detection of Hallucination Onset: Delay Bounds and Learned CUSUM Statistics](https://arxiv.org/abs/2606.12476)** · arXiv · LLM · Training-free
- **[P²-DPO: Grounding Hallucination in Perceptual Processing via Calibration Direct Preference Optimization](https://arxiv.org/abs/2606.03376)** · arXiv · LLM · Training-based
- **[Pre-Generation Hallucination Detection in Large Language Models via Soft-Target Attention Probing](https://arxiv.org/abs/2606.21917)** · arXiv · LLM · Training-free
- **📋 [OpenHalDet: A Unified Benchmark for Hallucination Detection across Diverse Generation Scenarios](https://arxiv.org/abs/2606.06959)** · arXiv · LLM · Training-free
- **[OmniHalluc-L: Counterfactual Benchmarking and Modality-Perturbation Reliability Calibration for Long-Form Omni Hallucination](https://arxiv.org/abs/2606.03614)** · arXiv · LLM · Training-free
- **[NTS-CoT: Mitigating Hallucinations in LLM-based News Timeline Summarization with Chain-of-Thought Reasoning](https://arxiv.org/abs/2606.13171)** · arXiv · LLM · Training-free
- **[MotionHalluc: Diagnosing Kinematic Hallucinations in Fine-Grained Motion Reasoning](https://arxiv.org/abs/2606.23061)** · arXiv · LLM · Training-free
- **[Mitigating Hallucinations in Large Language Models Via Decoder Layer Skipping](https://arxiv.org/abs/2606.00819)** · arXiv · LLM · Training-free
- **📋 [MedHal-Loc: Are "Explainable-by-Architecture" Medical Hallucination Detectors Faithful Localizers? A Localization Benchmark](https://arxiv.org/abs/2606.21517)** · arXiv · LLM · Training-free
- **[Med-HEAL: Analyzing and Mitigating Hallucinations in Medical LLMs with Hallucination-Aware In-Context Learning](https://arxiv.org/abs/2606.01301)** · arXiv · LLM · Training-free
- **[LegalHalluLens: Typed Hallucination Auditing and Calibrated Multi-Agent Debate for Trustworthy Legal AI](https://arxiv.org/abs/2606.18021)** · arXiv · LLM · Training-free
- **[Layer-Resolved Optimal Transport for Hallucination Detection in NMT and Abstractive Summarization](https://arxiv.org/abs/2606.13216)** · arXiv · LLM · Training-free
- **[Islamic Large Language Models: From Knowledge Acquisition to Trustworthy and Hallucination-Resistant AI](https://arxiv.org/abs/2606.16629)** · arXiv · LLM · Training-free
- **📋 [How Far Can You Get Without a GPU? A Systematic Benchmark of Lightweight Hallucination Detection Across Question Answering, Dialogue, and Summarisation](https://arxiv.org/abs/2606.29809)** · arXiv · LLM · Training-free
- **[Hallucination-Aware Diffusion Sampling for Inverse Problems via Robust Prior Updates](https://arxiv.org/abs/2606.02331)** · arXiv · LLM · Training-free
- **[Hallucination in World Models is Predictable and Preventable](https://arxiv.org/abs/2606.27326)** · arXiv · LLM · Training-based
- **[Hallucination in Medical Imaging AI: A Cross-Modality Analytical Framework for Taxonomy, Detection, and Mitigation under Regulatory Constraints](https://arxiv.org/abs/2606.13211)** · arXiv · LLM · Training-free
- **[Hallucination as Context Drift: Synchronization Protocols for Multi-Agent LLM Systems](https://arxiv.org/abs/2606.21666)** · arXiv · LLM · Training-free
- **[Hallucination Is Linearly Decodable from Mid-Layer Hidden States in Quantized LLMs](https://arxiv.org/abs/2606.02628)** · arXiv · LLM · Training-free
- **📋 [HALAS: A Human-Annotated Dataset of Hallucinations of Modern ASR Systems](https://arxiv.org/abs/2606.23048)** · arXiv · LLM · Training-free
- **[Generating in the Limit with Infinitely Many Hallucinations](https://arxiv.org/abs/2606.28354)** · arXiv · LLM · Training-free
- **[From Text Metrics to Model Internals: A Study of Whisper ASR Hallucination Detection](https://arxiv.org/abs/2606.23060)** · arXiv · LLM · Training-free
- **[From Architecture to Output: Structural Origins of Hallucination in Large Language Models and the Amplifying Role of Data](https://arxiv.org/abs/2606.07537)** · arXiv · LLM · Training-free
- **[Free-form Association Tasks Reveal Stereotype Hallucination in Large Language Models](https://arxiv.org/abs/2606.30945)** · arXiv · LLM · Training-free
- **[Finetuning with Scientific Data Increases Hallucinations: A Multi-domain Factuality Evaluation of LLMs](https://arxiv.org/abs/2606.21359)** · arXiv · LLM · Training-free
- **[Evidence Graph Consistency in Retrieval-Augmented Generation: A Model-Dependent Analysis of Hallucination Detection](https://arxiv.org/abs/2606.06748)** · arXiv · LLM · Training-free
- **[Evaluating Hallucinations in Domain-Adapted Large Language Models](https://arxiv.org/abs/2606.07521)** · arXiv · LLM · Training-free
- **[Disentangling Hallucinations: Orthogonal Semantic Projection for Robust Interpretability](https://arxiv.org/abs/2606.14758)** · arXiv · LLM · Training-free
- **[Detecting Hallucinations for Large Language Model-based Knowledge Graph Reasoning](https://arxiv.org/abs/2606.19351)** · arXiv · LLM · Training-free
- **📚 [DECK: A Consistency x Confidence Taxonomy of LLM Hallucinations](https://arxiv.org/abs/2606.02289)** · arXiv · LLM · Training-free
- **[Citation Grounding: Detecting and Reducing LLM Citation Hallucinations via Legal Citation Graphs](https://arxiv.org/abs/2606.00898)** · arXiv · LLM · Training-free
- **[Citation Discipline in Spec-Driven Development: A Cross-Model Empirical Study of Output Determinism and Automated Hallucination Detection in LLM-Generated Code](https://arxiv.org/abs/2606.30689)** · arXiv · LLM · Training-free
- **[Cascading Hallucination in Agentic RAG: The CHARM Framework for Detection and Mitigation](https://arxiv.org/abs/2606.04435)** · arXiv · LLM · Training-free
- **[CORTEX: Token-Level Hallucination Detection in RAG via Comparative Internal Representations](https://arxiv.org/abs/2606.31033)** · arXiv · LLM · Training-free
- **[Building Reliable Long-Form Generation via Hallucination Rejection Sampling](https://arxiv.org/abs/2606.03628)** · arXiv · LLM · Training-free
- **[BEACON: Behavioral Entropy Aggregation for Cross-Model Hallucination Detection in Large Language Models](https://arxiv.org/abs/2606.07528)** · arXiv · LLM · Training-free
- **[BALTO: Balanced Token-Level Policy Optimization for Hallucination Mitigation](https://arxiv.org/abs/2606.15893)** · arXiv · LLM · Training-based
- **[Analyzing the Correlation Between Hallucinations and Knowledge Conflicts in Large Language Models](https://arxiv.org/abs/2606.08705)** · arXiv · LLM · Training-free
- **[Agentic AI-based Framework for Mitigating Premature Diagnostic Handoff and Silent Hallucination in Healthcare Applications](https://arxiv.org/abs/2606.18068)** · arXiv · LLM · Training-free
- **[AURORA: Asymmetry and Update-Induced Rotation for Robust Hallucination Detection in Large Language Models](https://arxiv.org/abs/2606.29545)** · arXiv · LLM · Training-free
- **[TriDF: Evaluating Perception, Detection, and Hallucination for Interpretable DeepFake Detection](https://openaccess.thecvf.com/content/CVPR2026/html/Jiang-Lin_TriDF_Evaluating_Perception_Detection_and_Hallucination_for_Interpretable_DeepFake_Detection_CVPR_2026_paper.html)** · CVPR 2026 · LLM · Training-free
- **[Lyapunov Probes for Hallucination Detection in Large Foundation Models](https://openaccess.thecvf.com/content/CVPR2026/html/Luan_Lyapunov_Probes_for_Hallucination_Detection_in_Large_Foundation_Models_CVPR_2026_paper.html)** · CVPR 2026 · LLM · Training-free
- **[HAD: Hallucination-Aware Diffusion Priors for 3D Reconstruction](https://openaccess.thecvf.com/content/CVPR2026/html/Liu_HAD_Hallucination-Aware_Diffusion_Priors_for_3D_Reconstruction_CVPR_2026_paper.html)** · CVPR 2026 · LLM · Training-free
- **[Exposing and Evaluating Hallucinations for GUI Grounding](https://openaccess.thecvf.com/content/CVPR2026/html/Zhang_Exposing_and_Evaluating_Hallucinations_for_GUI_Grounding_CVPR_2026_paper.html)** · CVPR 2026 · LLM · Training-free
- **[Why DDIM Hallucinates More Than DDPM: A Theoretical Analysis of Reverse Dynamics](https://arxiv.org/abs/2605.06831)** · arXiv · LLM · Training-free
- **[Where Does Reasoning Break? Step-Level Hallucination Detection via Hidden-State Transport Geometry](https://arxiv.org/abs/2605.13772)** · arXiv · LLM · Training-free
- **[When Answers Stray from Questions: Hallucination Detection via Question-Answer Orthogonal Decomposition](https://arxiv.org/abs/2605.14449)** · arXiv · LLM · Training-free
- **[The First Token Knows: Single-Decode Confidence for Hallucination Detection](https://arxiv.org/abs/2605.05166)** · arXiv · LLM · Training-free
- **[Text Corpora as Concept Fields: Black-Box Hallucination and Novelty Measurement](https://arxiv.org/abs/2605.05103)** · arXiv · LLM · Training-free
- **[TRACE: Trajectory Correction from Cross-layer Evidence for Hallucination Reduction](https://arxiv.org/abs/2605.18163)** · arXiv · LLM · Training-free
- **[Source or It Didn't Happen: A Multi-Agent Framework for Citation Hallucination Detection](https://arxiv.org/abs/2605.08583)** · arXiv · LLM · Training-free
- **[Scalable Token-Level Hallucination Detection in Large Language Models](https://arxiv.org/abs/2605.12384)** · arXiv · LLM · Training-free
- **[Sanity Checks for Long-Form Hallucination Detection](https://arxiv.org/abs/2605.08346)** · arXiv · LLM · Training-free
- **[Retrieval-Based Multi-Label Legal Annotation: Extensible, Data-Efficient and Hallucination-Free](https://arxiv.org/abs/2605.16767)** · arXiv · LLM · Training-free
- **[REALISTA: Realistic Latent Adversarial Attacks that Elicit LLM Hallucinations](https://arxiv.org/abs/2605.12813)** · arXiv · LLM · Training-free
- **📋 [PARALLAX: Separating Genuine Hallucination Detection from Benchmark Construction Artifacts](https://arxiv.org/abs/2605.17028)** · arXiv · LLM · Training-free
- **[OptArgus: A Multi-Agent System to Detect Hallucinations in LLM-based Optimization Modeling](https://arxiv.org/abs/2605.11738)** · arXiv · LLM · Training-free
- **[On Hallucinations in Inverse Problems: Fundamental Limits and Provable Assessment Methods](https://arxiv.org/abs/2605.13146)** · arXiv · LLM · Training-free
- **[Not All That Is Fluent Is Factual: Investigating Hallucinations of Large Language Models in Academic Writing](https://arxiv.org/abs/2605.04171)** · arXiv · LLM · Training-free
- **[Neuro-Symbolic Agents for Hallucination-Free Requirements Reuse](https://arxiv.org/abs/2605.01562)** · arXiv · LLM · Training-free
- **[MultiHaluDet: Multilingual Hallucination Detection via LLM Hidden State Probing](https://arxiv.org/abs/2605.24919)** · arXiv · LLM · Training-free
- **[Micro-Macro Retrieval: Reducing Long-Form Hallucination in Large Language Models](https://arxiv.org/abs/2605.28828)** · arXiv · LLM · Training-free
- **[Max-pooling Network Revisited: Analyzing the Role of Semantic Probability in Multiple Instance Learning for Hallucination Detection](https://arxiv.org/abs/2605.08863)** · arXiv · LLM · Training-free
- **[Local Intrinsic Dimension Unveils Hallucinations in Diffusion Models](https://arxiv.org/abs/2605.05026)** · arXiv · LLM · Training-free
- **[LLM hallucinations in the wild: Large-scale evidence from non-existent citations](https://arxiv.org/abs/2605.07723)** · arXiv · LLM · Training-free
- **[LLM Ghostbusters: Surgical Hallucination Suppression via Adaptive Unlearning](https://arxiv.org/abs/2605.01047)** · arXiv · LLM · Training-based
- **[Innovation: An Almost Characterization of Hallucination](https://arxiv.org/abs/2605.26808)** · arXiv · LLM · Training-free
- **[How do Humans Process AI-generated Hallucination Contents: a Neuroimaging Study](https://arxiv.org/abs/2605.16953)** · arXiv · LLM · Training-free
- **[Hallucinations Undermine Trust; Metacognition is a Way Forward](https://arxiv.org/abs/2605.01428)** · arXiv · LLM · Training-free
- **[Hallucination as an Anomaly: Dynamic Intervention via Probabilistic Circuits](https://arxiv.org/abs/2605.05953)** · arXiv · LLM · Training-free
- **[Hallucination as Commitment Failure: Larger LLMs Misfire Despite Knowing the Answer](https://arxiv.org/abs/2605.22007)** · arXiv · LLM · Training-free
- **[Hallucination Mitigation with Agentic AI, Nested Learning, and AI Sustainability via Semantic Caching](https://arxiv.org/abs/2605.29055)** · arXiv · LLM · Training-free
- **[Hallucination Detection-Guided Preference Optimization for Clinical Summarization](https://arxiv.org/abs/2605.28910)** · arXiv · LLM · Training-based
- **[Hallucination Detection via Activations of Open-Weight Proxy Analyzers](https://arxiv.org/abs/2605.07209)** · arXiv · LLM · Training-free
- **📋 [HalluWorld: A Controlled Benchmark for Hallucination via Reference World Models](https://arxiv.org/abs/2605.19341)** · arXiv · LLM · Training-free
- **📋 [HalluScore: Large Language Model Hallucination Question Answering Benchmark](https://arxiv.org/abs/2605.17007)** · arXiv · LLM · Training-free
- **📋 [HalluScan: A Systematic Benchmark for Detecting and Mitigating Hallucinations in Instruction-Following LLMs](https://arxiv.org/abs/2605.02443)** · arXiv · LLM · Training-free
- **[From Flat Facts to Sharp Hallucinations: Detecting Stubborn Errors via Gradient Sensitivity](https://arxiv.org/abs/2605.00939)** · arXiv · LLM · Training-free
- **[Fighting Numerical Hallucinations via Data-centric Compilation for Online Financial QA](https://arxiv.org/abs/2605.31064)** · arXiv · LLM · Training-free
- **[Evaluating the Relevance of Uncertainty Estimators for LLM Hallucination](https://arxiv.org/abs/2605.27016)** · arXiv · LLM · Training-free
- **[Entropy Distribution as a Fingerprint for Hallucinations in Generative Models](https://arxiv.org/abs/2605.28264)** · arXiv · LLM · Training-free
- **[Empirical Analysis and Detection of Hallucinations in LLM-Generated Bug Report Summaries](https://arxiv.org/abs/2605.24137)** · arXiv · LLM · Training-free
- **[Do We Really Need External Tools to Mitigate Hallucinations? SIRA: Shared-Prefix Internal Reconstruction of Attribution](https://arxiv.org/abs/2605.14621)** · arXiv · LLM · Training-free
- **[Do No Harm? Hallucination and Actor-Level Abuse in Web-Deployed Medical Large Language Models](https://arxiv.org/abs/2605.20591)** · arXiv · LLM · Training-free
- **[Do Benchmarks Underestimate LLM Performance? Evaluating Hallucination Detection With LLM-First Human-Adjudicated Assessment](https://arxiv.org/abs/2605.08462)** · arXiv · LLM · Training-free
- **[Detecting Hallucinations in Large Language Models via Internal Attention Divergence Signals](https://arxiv.org/abs/2605.05025)** · arXiv · LLM · Training-free
- **📋 [Delulu: A Verified Multi-Lingual Benchmark for Code Hallucination Detection in Fill-in-the-Middle Tasks](https://arxiv.org/abs/2605.07024)** · arXiv · LLM · Training-free
- **[CuraView: A Multi-Agent Framework for Medical Hallucination Detection with GraphRAG-Enhanced Knowledge Verification](https://arxiv.org/abs/2605.03476)** · arXiv · LLM · Training-free
- **[CiteCheck: Retrieval-Grounded Detection of LLM Citation Hallucinations in Scientific Text](https://arxiv.org/abs/2605.27700)** · arXiv · LLM · Training-free
- **[Chain-based Adaptive Reconfiguration Over Lattices for Hallucination Reduction](https://arxiv.org/abs/2605.27706)** · arXiv · LLM · Training-free
- **[Causal Evidence for Attention Head Imbalance in Modality Conflict Hallucination](https://arxiv.org/abs/2605.19250)** · arXiv · LLM · Training-free
- **[Can These Views Be One Scene? Evaluating Multiview 3D Consistency when 3D Foundation Models Hallucinate](https://arxiv.org/abs/2605.18754)** · arXiv · LLM · Training-free
- **[Can Hallucinations Be Useful? Solving Multi-Hop Questions With SLMs By Chaining System-I/II Reasoning](https://arxiv.org/abs/2605.27596)** · arXiv · LLM · Training-free
- **[CAAFC: Chronological Actionable Automated Fact-Checker for misinformation / non-factual hallucination detection and correction](https://arxiv.org/abs/2605.12436)** · arXiv · LLM · Training-free
- **[Beyond Final Answers: Auditing Trajectory-Level Hallucinations in Multi-Agent Industrial Workflows](https://arxiv.org/abs/2605.24219)** · arXiv · LLM · Training-free
- **[BenHalluEval: A Multi-Task Hallucination Evaluation Framework for Large Language Models on Bengali](https://arxiv.org/abs/2605.31483)** · arXiv · LLM · Training-free
- **[Automatic Layer Selection for Hallucination Detection](https://arxiv.org/abs/2605.26366)** · arXiv · LLM · Training-free
- **[Attractor Geometry of Transformer Memory: From Conflict Arbitration to Confident Hallucination](https://arxiv.org/abs/2605.05686)** · arXiv · LLM · Training-free
- **[ACL-Verbatim: hallucination-free question answering for research](https://arxiv.org/abs/2605.21102)** · arXiv · LLM · Training-free
- **📋 [A multilingual hallucination benchmark: MultiWikiQHalluA](https://arxiv.org/abs/2605.02504)** · arXiv · LLM · Training-free
- **[A Theory of Time-Sensitive Language Generation: Sparse Hallucination Beats Mode Collapse](https://arxiv.org/abs/2605.11302)** · arXiv · LLM · Training-free
- **[Why Fine-Tuning Encourages Hallucinations and How to Fix It](https://arxiv.org/abs/2604.15574)** · arXiv · LLM · Training-free
- **[Where Fake Citations Are Made: Tracing Field-Level Hallucination to Specific Neurons in LLMs](https://arxiv.org/abs/2604.18880)** · arXiv · LLM · Training-free
- **[When Do Hallucinations Arise? A Graph Perspective on the Evolution of Path Reuse and Path Compression](https://arxiv.org/abs/2604.03557)** · arXiv · LLM · Training-free
- **[Weakly Supervised Distillation of Hallucination Signals into Transformer Representations](https://arxiv.org/abs/2604.06277)** · arXiv · LLM · Training-free
- **[Unmasking Hallucinations: A Causal Graph-Attention Perspective on Factual Reliability in Large Language Models](https://arxiv.org/abs/2604.04020)** · arXiv · LLM · Training-free
- **[Synthius-Mem: Brain-Inspired Hallucination-Resistant Persona Memory Achieving 94.4% Memory Accuracy and 99.6% Adversarial Robustness on LoCoMo](https://arxiv.org/abs/2604.11563)** · arXiv · LLM · Training-free
- **[SinkTrack: Attention Sink based Context Anchoring for Large Language Models](https://arxiv.org/abs/2604.10027)** · arXiv · LLM · Training-free
- **📋 [Semantic Layers for Reliable LLM-Powered Data Analytics: A Paired Benchmark of Accuracy and Hallucination Across Three Frontier Models](https://arxiv.org/abs/2604.25149)** · arXiv · LLM · Training-free
- **[Reducing Hallucinations in LLM-based Scientific Literature Analysis Using Peer Context Outlier Detection](https://arxiv.org/abs/2604.01461)** · arXiv · LLM · Training-free
- **[RAGognizer: Hallucination-Aware Fine-Tuning via Detection Head Integration](https://arxiv.org/abs/2604.15945)** · arXiv · LLM · Training-free
- **[Paper Reconstruction Evaluation: Evaluating Presentation and Hallucination in AI-written Papers](https://arxiv.org/abs/2604.01128)** · arXiv · LLM · Training-free
- **[Overconfidence and Calibration in Medical VQA: Empirical Findings and Hallucination-Aware Mitigation](https://arxiv.org/abs/2604.02543)** · arXiv · LLM · Training-free
- **[Noise-Aware In-Context Learning for Hallucination Mitigation in ALLMs](https://arxiv.org/abs/2604.09021)** · arXiv · LLM · Training-free
- **[Mind the Unseen Mass: Unmasking LLM Hallucinations via Soft-Hybrid Alphabet Estimation](https://arxiv.org/abs/2604.19162)** · arXiv · LLM · Training-free
- **[KARL: Mitigating Hallucinations in LLMs via Knowledge-Boundary-Aware Reinforcement Learning](https://arxiv.org/abs/2604.22779)** · arXiv · LLM · Training-based
- **[I-CALM: Incentivizing Confidence-Aware Abstention for LLM Hallucination Mitigation](https://arxiv.org/abs/2604.03904)** · arXiv · LLM · Training-free
- **[How unique are hallucinated citations offered by generative Artificial Intelligence models?](https://arxiv.org/abs/2604.16407)** · arXiv · LLM · Training-free
- **[Hallucination as output-boundary misclassification: a composite abstention architecture for language models](https://arxiv.org/abs/2604.06195)** · arXiv · LLM · Training-free
- **[Hallucination as Trajectory Commitment: Causal Evidence for Asymmetric Attractor Dynamics in Transformer Generation](https://arxiv.org/abs/2604.15400)** · arXiv · LLM · Training-free
- **[Hallucination Basins: A Dynamic Framework for Understanding and Controlling LLM Hallucinations](https://arxiv.org/abs/2604.04743)** · arXiv · LLM · Training-free
- **[HalluSAE: Detecting Hallucinations in Large Language Models via Sparse Auto-Encoders](https://arxiv.org/abs/2604.16430)** · arXiv · LLM · Training-free
- **[HalluClear: Diagnosing, Evaluating and Mitigating Hallucinations in GUI Agents](https://arxiv.org/abs/2604.17284)** · arXiv · LLM · Training-based
- **[HalluCiteChecker: A Lightweight Toolkit for Hallucinated Citation Detection and Verification in the Era of AI Scientists](https://arxiv.org/abs/2604.26835)** · arXiv · LLM · Training-free
- **[Hackers or Hallucinators? A Comprehensive Analysis of LLM-Based Automated Penetration Testing](https://arxiv.org/abs/2604.05719)** · arXiv · LLM · Training-free
- **[HIVE: Hidden-Evidence Verification for Hallucination Detection in Diffusion Large Language Models](https://arxiv.org/abs/2604.26139)** · arXiv · LLM · Training-free
- **[GSAR: Typed Grounding for Hallucination Detection and Recovery in Multi-Agent LLMs](https://arxiv.org/abs/2604.23366)** · arXiv · LLM · Training-free
- **[GIRL: Generative Imagination Reinforcement Learning via Information-Theoretic Hallucination Control](https://arxiv.org/abs/2604.07426)** · arXiv · LLM · Training-based
- **[From Retinal Evidence to Safe Decisions: RETINA-SAFE and ECRT for Hallucination Risk Triage in Medical LLMs](https://arxiv.org/abs/2604.05348)** · arXiv · LLM · Training-free
- **[From Hallucination to Structure Snowballing: The Alignment Tax of Constrained Decoding in LLM Reflection](https://arxiv.org/abs/2604.06066)** · arXiv · LLM · Training-free
- **[From Dispersion to Attraction: Spectral Dynamics of Hallucination Across Whisper Model Scales](https://arxiv.org/abs/2604.08591)** · arXiv · LLM · Training-free
- **[FinGround: Detecting and Grounding Financial Hallucinations via Atomic Claim Verification](https://arxiv.org/abs/2604.23588)** · arXiv · LLM · Training-free
- **[Facet-Level Tracing of Evidence Uncertainty and Hallucination in RAG](https://arxiv.org/abs/2604.09174)** · arXiv · LLM · Training-free
- **[Do Hallucination Neurons Generalize? Evidence from Cross-Domain Transfer in LLMs](https://arxiv.org/abs/2604.19765)** · arXiv · LLM · Training-free
- **[Disentangling Prompt Element Level Risk Factors for Hallucinations and Omissions in Mental Health LLM Responses](https://arxiv.org/abs/2604.00014)** · arXiv · LLM · Training-free
- **[Detection Without Correction: A Robust Asymmetry in Activation-Based Hallucination Probing](https://arxiv.org/abs/2604.13068)** · arXiv · LLM · Training-free
- **[Detecting and Correcting Reference Hallucinations in Commercial LLMs and Deep Research Agents](https://arxiv.org/abs/2604.03173)** · arXiv · LLM · Training-free
- **[Council Mode: A Heterogeneous Multi-Agent Consensus Framework for Reducing LLM Hallucination and Bias](https://arxiv.org/abs/2604.02923)** · arXiv · LLM · Training-free
- **[CareGuardAI: Context-Aware Multi-Agent Guardrails for Clinical Safety & Hallucination Mitigation in Patient-Facing LLMs](https://arxiv.org/abs/2604.26959)** · arXiv · LLM · Training-free
- **[Blending Human and LLM Expertise to Detect Hallucinations and Omissions in Mental Health Chatbot Responses](https://arxiv.org/abs/2604.06216)** · arXiv · LLM · Training-free
- **[BibTeX Citation Hallucinations in Scientific Publishing Agents: Evaluation and Mitigation](https://arxiv.org/abs/2604.03159)** · arXiv · LLM · Training-free
- **[Beyond Literal Summarization: Redefining Hallucination for Medical SOAP Note Evaluation](https://arxiv.org/abs/2604.14829)** · arXiv · LLM · Training-free
- **[Attention Sinks as Internal Signals for Hallucination Detection in Large Language Models](https://arxiv.org/abs/2604.10697)** · arXiv · LLM · Training-free
- **[Anchored Confabulation: Partial Evidence Non-Monotonically Amplifies Confident Hallucination in LLMs](https://arxiv.org/abs/2604.25931)** · arXiv · LLM · Training-free
- **[An Empirical Analysis of Static Analysis Methods for Detection and Mitigation of Code Library Hallucinations](https://arxiv.org/abs/2604.07755)** · arXiv · LLM · Training-free
- **[AI models of unstable flow exhibit hallucination](https://arxiv.org/abs/2604.20372)** · arXiv · LLM · Training-free
- **[Token-Guard: Towards Token-Level Hallucination Control via Self-Checking Decoding]()** · ICLR 2026 · LLM · Training-free
- **[Semantic Uncertainty Quantification of Hallucinations in LLMs: A Quantum Tensor Network Based Method](https://arxiv.org/abs/2601.20026)** · ICLR 2026 · LLM · Training-free
- **[Semantic Reformulation Entropy for Robust Hallucination Detection in QA Tasks](https://doi.org/10.1109/icassp55912.2026.11460452)** · ICASSP 2026 · LLM · Training-free
- **[Mitigating Hallucination in Financial Retrieval-Augmented Generation Via Fine-Grained Knowledge Verification](https://doi.org/10.1109/icassp55912.2026.11464516)** · ICASSP 2026 · LLM · Training-free
- **[Hallucination Detection Via Internal States and Structured Reasoning Consistency in Large Language Models](https://doi.org/10.1109/icassp55912.2026.11462457)** · ICASSP 2026 · LLM · Training-free
- **[HARP: Hallucination Detection via Reasoning Subspace Projection](https://arxiv.org/abs/2509.11536)** · ICLR 2026 · LLM · Training-free
- **📋 [DHEval: A Dynamic Hallucination Evaluation Protocol Robust to Data Contamination](https://doi.org/10.1109/icassp55912.2026.11462032)** · ICASSP 2026 · LLM · Training-free
- **[Cross Paraphrastic Invariance Learning for Hallucination Detection](https://doi.org/10.1109/icassp55912.2026.11463868)** · ICASSP 2026 · LLM · Training-free
- **[Constrained Paraphrase Consistency for LLM Hallucination Detection](https://doi.org/10.1109/icassp55912.2026.11462617)** · ICASSP 2026 · LLM · Training-free
- **[An Industrial-Scale Insurance LLM Achieving Verifiable Domain Mastery and Hallucination Control without Competence Trade-offs](https://arxiv.org/abs/2603.14463)** · ICLR 2026 · LLM · Training-free
- **[Whitening Reveals Cluster Commitment as the Geometric Separator of Hallucination Types](https://arxiv.org/abs/2603.07755)** · arXiv · LLM · Training-free
- **[Toward Epistemic Stability: Engineering Consistent Procedures for Industrial LLM Hallucination Reduction](https://arxiv.org/abs/2603.10047)** · arXiv · LLM · Training-free
- **[Tool Receipts, Not Zero-Knowledge Proofs: Practical Hallucination Detection for AI Agents](https://arxiv.org/abs/2603.10060)** · arXiv · LLM · Training-free
- **[The System Hallucination Scale (SHS): A Minimal yet Effective Human-Centered Instrument for Evaluating Hallucination-Related Behavior in Large Language Models](https://arxiv.org/abs/2603.09989)** · arXiv · LLM · Training-free
- **[The Phenomenology of Hallucinations](https://arxiv.org/abs/2603.13911)** · arXiv · LLM · Training-free
- **[Squish and Release: Exposing Hidden Hallucinations by Making Them Surface as Safety Signals](https://arxiv.org/abs/2603.26829)** · arXiv · LLM · Training-free
- **[Semantic Similarity is a Spurious Measure of Comic Understanding: Lessons Learned from Hallucinations in a Benchmarking Experiment](https://arxiv.org/abs/2603.01950)** · arXiv · LLM · Training-free
- **[Sample Transform Cost-Based Training-Free Hallucination Detector for Large Language Models](https://arxiv.org/abs/2603.22303)** · arXiv · LLM · Training-free
- **[Retromorphic Testing with Hierarchical Verification for Hallucination Detection in RAG](https://arxiv.org/abs/2603.27752)** · arXiv · LLM · Training-free
- **[Quantifying Hallucinations in Language Language Models on Medical Textbooks](https://arxiv.org/abs/2603.09986)** · arXiv · LLM · Training-free
- **[Progressive Training for Explainable Citation-Grounded Dialogue: Reducing Hallucination to Zero in English-Hindi LLMs](https://arxiv.org/abs/2603.18911)** · arXiv · LLM · Training-free
- **[POaaS: Minimal-Edit Prompt Optimization as a Service to Lift Accuracy and Cut Hallucinations on On-Device sLLMs](https://arxiv.org/abs/2603.16045)** · arXiv · LLM · Training-free
- **[Neuro-Symbolic Financial Reasoning via Deterministic Fact Ledgers and Adversarial Low-Latency Hallucination Detector](https://arxiv.org/abs/2603.04663)** · arXiv · LLM · Training-free
- **[Mitigating LLM Hallucinations through Domain-Grounded Tiered Retrieval](https://arxiv.org/abs/2603.17872)** · arXiv · LLM · Training-free
- **[MARCH: Multi-Agent Reinforced Self-Check for LLM Hallucination](https://arxiv.org/abs/2603.24579)** · arXiv · LLM · Training-free
- **[Large Language Models for Missing Data Imputation: Understanding Behavior, Hallucination Effects, and Control Mechanisms](https://arxiv.org/abs/2603.22332)** · arXiv · LLM · Training-free
- **[Inducing Epistemological Humility in Large Language Models: A Targeted SFT Approach to Reducing Hallucination](https://arxiv.org/abs/2603.17504)** · arXiv · LLM · Training-free
- **[How Much Do LLMs Hallucinate in Document Q&A Scenarios? A 172-Billion-Token Study Across Temperatures, Context Lengths, and Hardware Platforms](https://arxiv.org/abs/2603.08274)** · arXiv · LLM · Training-free
- **[HART: Data-Driven Hallucination Attribution and Evidence-Based Tracing for Large Language Models](https://arxiv.org/abs/2603.05828)** · arXiv · LLM · Training-free
- **[From Prerequisites to Predictions: Validating a Geometric Hallucination Taxonomy Through Controlled Induction](https://arxiv.org/abs/2603.00307)** · arXiv · LLM · Training-free
- **📋 [FinReflectKG -- HalluBench: GraphRAG Hallucination Benchmark for Financial Question Answering Systems](https://arxiv.org/abs/2603.20252)** · arXiv · LLM · Training-free
- **[DynHD: Hallucination Detection for Diffusion Large Language Models via Denoising Dynamics Deviation Learning](https://arxiv.org/abs/2603.16459)** · arXiv · LLM · Training-free
- **[Do Deployment Constraints Make LLMs Hallucinate Citations? An Empirical Study across Four Models and Five Prompting Regimes](https://arxiv.org/abs/2603.07287)** · arXiv · LLM · Training-free
- **[Deterministic Hallucination Detection in Medical VQA via Confidence-Evidence Bayesian Gain](https://arxiv.org/abs/2603.21693)** · arXiv · LLM · Training-free
- **[Adaptive Activation Cancellation for Hallucination Mitigation in Large Language Models](https://arxiv.org/abs/2603.10195)** · arXiv · LLM · Training-free
- **[A Novel Multi-Agent Architecture to Reduce Hallucinations of Large Language Models in Multi-Step Structural Modeling](https://arxiv.org/abs/2603.07728)** · arXiv · LLM · Training-free
- **[The Unintended Trade-off of AI Alignment: Balancing Hallucination Mitigation and Safety in LLMs](https://doi.org/10.18653/v1/2026.findings-eacl.53)** · EACL 2026 · LLM · Training-free
- **[Taming Object Hallucinations with Verified Atomic Confidence Estimation](https://doi.org/10.18653/v1/2026.eacl-long.252)** · EACL 2026 · LLM · Training-free
- **[Rethinking Hallucinations: Correctness, Consistency, and Prompt Multiplicity](https://doi.org/10.18653/v1/2026.eacl-long.327)** · EACL 2026 · LLM · Training-free
- **[Reducing Hallucinations in Language Model-based SPARQL Query Generation Using Post-Generation Memory Retrieval](https://doi.org/10.18653/v1/2026.findings-eacl.243)** · EACL 2026 · LLM · Training-free
- **[Reasoning&apos;s Razor: Reasoning Improves Accuracy but Hurts Recall at Critical Operating Points in Safety and Hallucination Detection](https://doi.org/10.18653/v1/2026.eacl-long.190)** · EACL 2026 · LLM · Training-free
- **📋 [Multi-Hall-SA: A Cross-lingual Benchmark for Multi-Type Hallucination Detection in Low-Resource South African Languages](https://doi.org/10.18653/v1/2026.findings-eacl.330)** · EACL 2026 · LLM · Training-free
- **📋 [KGHaluBench: A Knowledge Graph-Based Hallucination Benchmark for Evaluating the Breadth and Depth of LLM Knowledge](https://doi.org/10.18653/v1/2026.findings-eacl.206)** · EACL 2026 · LLM · Training-free
- **[HalluZig: Hallucination Detection using Zigzag Persistence](https://doi.org/10.18653/v1/2026.eacl-long.159)** · EACL 2026 · LLM · Training-free
- **📋 [GHOST: Getting to the Bottom of Hallucinations with A Multi-round Consistency Benchmark](https://doi.org/10.1109/WACV61042.2026.00596)** · WACV 2026 · LLM · Training-free
- **[FactSelfCheck: Fact-Level Black-Box Hallucination Detection for LLMs](https://doi.org/10.18653/v1/2026.findings-eacl.296)** · EACL 2026 · LLM · Training-free
- **📋 [FFE-Hallu: Hallucinations in Fixed Figurative Expressions: A Benchmark of Idioms and Proverbs in the Persian Language](https://doi.org/10.18653/v1/2026.eacl-long.241)** · EACL 2026 · LLM · Training-free
- **[Do LLM hallucination detectors suffer from low-resource effect?](https://doi.org/10.18653/v1/2026.eacl-long.136)** · EACL 2026 · LLM · Training-free
- **📋 [Constructing a Dataset for Hallucination Detection in Japanese Summarization with Fine-grained Faithfulness Labels](https://doi.org/10.18653/v1/2026.eacl-srw.15)** · EACL 2026 · LLM · Training-free
- **[Being Kind Isn't Always Being Safe: Diagnosing Affective Hallucination in LLMs](https://doi.org/10.18653/v1/2026.findings-eacl.4)** · EACL 2026 · LLM · Training-free
- **[Being Kind Isn&apos;t Always Being Safe: Diagnosing Affective Hallucination in LLMs](https://doi.org/10.18653/v1/2026.findings-eacl.4)** · EACL 2026 · LLM · Training-free
- **[What do Geometric Hallucination Detection Metrics Actually Measure?](https://arxiv.org/abs/2602.09158)** · arXiv · LLM · Training-free
- **[Triggering hallucinations in model-based MRI reconstruction via adversarial perturbations](https://arxiv.org/abs/2602.18536)** · arXiv · LLM · Training-free
- **[The Energy of Falsehood: Detecting Hallucinations via Diffusion Model Likelihoods](https://arxiv.org/abs/2602.11364)** · arXiv · LLM · Training-free
- **[Tethered Reasoning: Decoupling Entropy from Hallucination in Quantized LLMs via Manifold Steering](https://arxiv.org/abs/2602.17691)** · arXiv · LLM · Training-free
- **[TDGNet: Hallucination Detection in Diffusion Language Models via Temporal Dynamic Graphs](https://arxiv.org/abs/2602.08048)** · arXiv · LLM · Training-free
- **[Suppressing Prior-Comparison Hallucinations in Radiology Report Generation via Semantically Decoupled Latent Steering](https://arxiv.org/abs/2602.23676)** · arXiv · LLM · Training-free
- **[Stop Rewarding Hallucinated Steps: Faithfulness-Aware Step-Level Reinforcement Learning for Small Reasoning Models](https://arxiv.org/abs/2602.05897)** · arXiv · LLM · Training-based
- **[Spectral Guardrails for Agents in the Wild: Detecting Tool Use Hallucinations via Attention Topology](https://arxiv.org/abs/2602.08082)** · arXiv · LLM · Training-free
- **[Small Updates, Big Doubts: Does Parameter-Efficient Fine-tuning Enhance Hallucination Detection ?](https://arxiv.org/abs/2602.11166)** · arXiv · LLM · Training-based
- **[No One Size Fits All: QueryBandits for Hallucination Mitigation](https://arxiv.org/abs/2602.20332)** · arXiv · LLM · Training-free
- **[Listen to the Layers: Mitigating Hallucinations with Inter-Layer Disagreement](https://arxiv.org/abs/2602.09486)** · arXiv · LLM · Training-free
- **[Halt the Hallucination: Decoupling Signal and Semantic OOD Detection Based on Cascaded Early Rejection](https://arxiv.org/abs/2602.06330)** · arXiv · LLM · Training-free
- **📋 [Halluverse-M^3: A multitask multilingual benchmark for hallucination in LLMs](https://arxiv.org/abs/2602.06920)** · arXiv · LLM · Training-free
- **[Hallucination-Resistant Security Planning with a Large Language Model](https://arxiv.org/abs/2602.05279)** · arXiv · LLM · Training-free
- **[Hallucination is a Consequence of Space-Optimality: A Rate-Distortion Theorem for Membership Testing](https://arxiv.org/abs/2602.00906)** · arXiv · LLM · Training-free
- **📋 [HalluHard: A Hard Multi-Turn Hallucination Benchmark](https://arxiv.org/abs/2602.01031)** · arXiv · LLM · Training-free
- **[HALT: Hallucination Assessment via Log-probs as Time series](https://arxiv.org/abs/2602.02888)** · arXiv · LLM · Training-free
- **[From Out-of-Distribution Detection to Hallucination Detection: A Geometric View](https://arxiv.org/abs/2602.07253)** · arXiv · LLM · Training-free
- **[Fine-Refine: Iterative Fine-grained Refinement for Mitigating Dialogue Hallucination](https://arxiv.org/abs/2602.15509)** · arXiv · LLM · Training-free
- **[Epistemic Filtering and Collective Hallucination: A Jury Theorem for Confidence-Calibrated Agents](https://arxiv.org/abs/2602.22413)** · arXiv · LLM · Training-free
- **[Do I Really Know? Learning Factual Self-Verification for Hallucination Reduction](https://arxiv.org/abs/2602.02018)** · arXiv · LLM · Training-based
- **[Disentangling Deception and Hallucination Failures in LLMs](https://arxiv.org/abs/2602.14529)** · arXiv · LLM · Training-free
- **[Detecting LLM Hallucinations via Embedding Cluster Geometry: A Three-Type Taxonomy with Measurable Signatures](https://arxiv.org/abs/2602.14259)** · arXiv · LLM · Training-free
- **[Detecting Contextual Hallucinations in LLMs with Frequency-Aware Attention](https://arxiv.org/abs/2602.18145)** · arXiv · LLM · Training-free
- **[CheckIfExist: Detecting Citation Hallucinations in the Era of AI-Generated Content](https://arxiv.org/abs/2602.15871)** · arXiv · LLM · Training-free
- **[Beyond Accuracy: Risk-Sensitive Evaluation of Hallucinated Medical Advice](https://arxiv.org/abs/2602.07319)** · arXiv · LLM · Training-free
- **[AI Hallucination from Students' Perspective: A Thematic Analysis](https://arxiv.org/abs/2602.17671)** · arXiv · LLM · Training-free
- **📚 [A Geometric Taxonomy of Hallucinations in LLMs](https://arxiv.org/abs/2602.13224)** · arXiv · LLM · Training-free
- **[A Geometric Analysis of Small-sized Language Model Hallucinations](https://arxiv.org/abs/2602.14778)** · arXiv · LLM · Training-free
- **[SEVADE: Self-Evolving Multi-Agent Analysis with Decoupled Evaluation for Hallucination-Resistant Sarcasm Detection](https://doi.org/10.1609/aaai.v40i35.40200)** · AAAI 2026 · LLM · Training-free
- **[ProgRAG: Hallucination-Resistant Progressive Retrieval and Reasoning over Knowledge Graphs](https://doi.org/10.1609/aaai.v40i39.40545)** · AAAI 2026 · LLM · Training-free
- **[PHPFND: Detecting Fake News via Post-Hoc Processing of LLMs Hallucination](https://doi.org/10.1609/aaai.v40i1.37050)** · AAAI 2026 · LLM · Training-free
- **[Not All Tokens and Heads Are Equally Important: Dual-Level Attention Intervention for Hallucination Mitigation](https://doi.org/10.1609/aaai.v40i11.37904)** · AAAI 2026 · LLM · Training-free
- **[NewsLensAI: NER-Guided Summarization for Mitigating Hallucination and Bias in LLM-Based News Summaries (Student Abstract)](https://doi.org/10.1609/aaai.v40i48.42250)** · AAAI 2026 · LLM · Training-free
- **[Mitigating Hallucinations in Large Language Models via Causal Reasoning](https://doi.org/10.1609/aaai.v40i38.40454)** · AAAI 2026 · LLM · Training-free
- **[Mitigating Entity Hallucinations in 3D Radiology Report Generation via Dual-Stream Alignment](https://doi.org/10.1609/aaai.v40i16.38379)** · AAAI 2026 · LLM · Training-free
- **📋 [MHB: Medical Hallucination Benchmark for Large Language Models in Complex Clinical Tasks](https://doi.org/10.1609/aaai.v40i45.41243)** · AAAI 2026 · LLM · Training-free
- **[Listen like a Teacher: Mitigating Whisper Hallucinations Using Adaptive Layer Attention and Knowledge Distillation](https://doi.org/10.1609/aaai.v40i39.40614)** · AAAI 2026 · LLM · Training-free
- **[LLM-CAS: Dynamic Neuron Perturbation for Real-Time Hallucination Correction](https://doi.org/10.1609/aaai.v40i41.40776)** · AAAI 2026 · LLM · Training-free
- **[Joint Evaluation of Answer and Reasoning Consistency for Hallucination Detection in Large Reasoning Models](https://doi.org/10.1609/aaai.v40i39.40624)** · AAAI 2026 · LLM · Training-free
- **[InEx: Hallucination Mitigation via Introspection and Cross-Modal Multi-Agent Collaboration](https://doi.org/10.1609/aaai.v40i35.40229)** · AAAI 2026 · LLM · Training-free
- **[Hallucinations at the Firewall](https://doi.org/10.1609/aaai.v40i48.42311)** · AAAI 2026 · LLM · Training-free
- **[Hallucination as a Computational Boundary: A Hierarchy of Inevitability and the Oracle Escape](https://doi.org/10.1609/aaai.v40i40.40657)** · AAAI 2026 · LLM · Training-free
- **[Hallucinate Less by Thinking More: Aspect-Based Causal Abstention for Large Language Models](https://doi.org/10.1609/aaai.v40i38.40532)** · AAAI 2026 · LLM · Training-free
- **[HalluClean: A Unified Framework to Combat Hallucinations in LLMs](https://doi.org/10.1609/aaai.v40i42.40926)** · AAAI 2026 · LLM · Training-free
- **[Global-Local Confidence Fusion for Hallucination Detection in Mathematical Reasoning Task](https://doi.org/10.1609/aaai.v40i41.40762)** · AAAI 2026 · LLM · Training-based
- **[From Detection to Diagnosis: Advancing Hallucination Analysis with Automated Data Synthesis](https://doi.org/10.1609/aaai.v40i38.40495)** · AAAI 2026 · LLM · Training-free
- **[Efficient Hallucination Detection: Adaptive Bayesian Estimation of Semantic Entropy with Guided Semantic Exploration](https://doi.org/10.1609/aaai.v40i39.40595)** · AAAI 2026 · LLM · Training-free
- **📋 [ESG-Bench: Benchmarking Long-Context ESG Reports for Hallucination Mitigation](https://doi.org/10.1609/aaai.v40i46.41281)** · AAAI 2026 · LLM · Training-based
- **[Diffusion for Combating the Hallucination in Large Language Models (Student Abstract)](https://doi.org/10.1609/aaai.v40i48.42183)** · AAAI 2026 · LLM · Training-free
- **[Detecting Citation Hallucinations in Large Language Model Outputs (Student Abstract)](https://doi.org/10.1609/aaai.v40i48.42257)** · AAAI 2026 · LLM · Training-free
- **[Bolster Hallucination Detection via Prompt-Guided Data Augmentation](https://doi.org/10.1609/aaai.v40i44.41096)** · AAAI 2026 · LLM · Training-free
- **[Beyond Next Token Probabilities: Learnable, Fast Detection of Hallucinations and Data Contamination on LLM Output Distributions](https://doi.org/10.1609/aaai.v40i36.40254)** · AAAI 2026 · LLM · Training-free
- **[Analyzing and Mitigating Object Hallucination: A Training Bias Perspective](https://doi.org/10.1609/aaai.v40i8.37594)** · AAAI 2026 · LLM · Training-free
- **[Why Your Deep Research Agent Fails? On Hallucination Evaluation in Full Research Trajectory](https://arxiv.org/abs/2601.22984)** · arXiv · LLM · Training-free
- **[Temporal Graph Network: Hallucination Detection in Multi-Turn Conversation](https://arxiv.org/abs/2601.03051)** · arXiv · LLM · Training-free
- **[Supervision-by-Hallucination-and-Transfer: A Weakly-Supervised Approach for Robust and Precise Facial Landmark Detection](https://arxiv.org/abs/2601.12919)** · arXiv · LLM · Training-free
- **[Spectral Geometry for Deep Learning: Compression and Hallucination Detection via Random Matrix Theory](https://arxiv.org/abs/2601.17357)** · arXiv · LLM · Training-free
- **[Relational Linearity is a Predictor of Hallucinations](https://arxiv.org/abs/2601.11429)** · arXiv · LLM · Training-free
- **[RAL2M: Retrieval Augmented Learning-To-Match Against Hallucination in Compliance-Guaranteed Service Systems](https://arxiv.org/abs/2601.02917)** · arXiv · LLM · Training-free
- **[Probabilistic Guarantees for Reducing Contextual Hallucinations in LLMs](https://arxiv.org/abs/2601.00641)** · arXiv · LLM · Training-free
- **[Predictive Coding and Information Bottleneck for Hallucination Detection in Large Language Models](https://arxiv.org/abs/2601.15652)** · arXiv · LLM · Training-free
- **[Physio-DPO: Aligning Large Language Models with the Protein Energy Landscape to Eliminate Structural Hallucinations](https://arxiv.org/abs/2601.00647)** · arXiv · LLM · Training-based
- **[Not All Needles Are Found: How Fact Distribution and Don't Make It Up Prompts Shape Retrieval, Reasoning, and Hallucination in Long-Context LLMs](https://arxiv.org/abs/2601.02023)** · arXiv · LLM · Training-free
- **[Mitigating Prompt-Induced Hallucinations in Large Language Models via Structured Reasoning](https://arxiv.org/abs/2601.02739)** · arXiv · LLM · Training-free
- **[Lowest Span Confidence: A Zero-Shot Metric for Efficient and Black-Box Hallucination Detection in LLMs](https://arxiv.org/abs/2601.19918)** · arXiv · LLM · Training-free
- **[LANCET: Neural Intervention via Structural Entropy for Mitigating Faithfulness Hallucinations in LLMs](https://arxiv.org/abs/2601.01401)** · arXiv · LLM · Training-free
- **[KDCM: Reducing Hallucination in LLMs through Explicit Reasoning Structures](https://arxiv.org/abs/2601.04086)** · arXiv · LLM · Training-free
- **[Internal Representations as Indicators of Hallucinations in Agent Tool Selection](https://arxiv.org/abs/2601.05214)** · arXiv · LLM · Training-free
- **[Hallucinations Live in Variance](https://arxiv.org/abs/2601.07058)** · arXiv · LLM · Training-free
- **[Hallucination Mitigating for Medical Report Generation](https://arxiv.org/abs/2601.15745)** · arXiv · LLM · Training-free
- **[HalluGuard: Demystifying Data-Driven and Reasoning-Driven Hallucinations in LLMs](https://arxiv.org/abs/2601.18753)** · arXiv · LLM · Training-free
- **[Geometry-Aware Hallucination Detection in Large Language Models](https://arxiv.org/abs/2601.06196)** · arXiv · LLM · Training-free
- **[From Particles to Agents: Hallucination as a Metric for Cognitive Friction in Spatial Simulation](https://arxiv.org/abs/2601.21977)** · arXiv · LLM · Training-free
- **[Engineering of Hallucination in Generative AI: It's not a Bug, it's a Feature](https://arxiv.org/abs/2601.07046)** · arXiv · LLM · Training-free
- **[Empowering Small Language Models with Factual Hallucination-Aware Reasoning for Financial Classification](https://arxiv.org/abs/2601.01378)** · arXiv · LLM · Training-free
- **[Distortion Instead of Hallucination: The Effect of Reasoning Under Strict Constraints](https://arxiv.org/abs/2601.01490)** · arXiv · LLM · Training-free
- **[DSC2025 -- ViHallu Challenge: Detecting Hallucination in Vietnamese LLMs](https://arxiv.org/abs/2601.04711)** · arXiv · LLM · Training-free
- **[Can We Improve Educational Diagram Generation with In-Context Examples? Not if a Hallucination Spoils the Bunch](https://arxiv.org/abs/2601.20476)** · arXiv · LLM · Training-free
- **[CORVUS: Red-Teaming Hallucination Detectors via Internal Signal Camouflage in Large Language Models](https://arxiv.org/abs/2601.14310)** · arXiv · LLM · Training-free
- **[AgentHallu: Benchmarking Automated Hallucination Attribution of LLM-based Agents](https://arxiv.org/abs/2601.06818)** · arXiv · LLM · Training-free
- **[Hallucination Begins Where Saliency Drops]()** · Unlabeled · LLM · Training-free
- **[Why Language Model Reasoning Systematically Fails: A Structural Definition of Hallucination Based on Coordinate Closure](https://doi.org/10.1109/ACCESS.2026.3707249)** · IEEE Access 2026 · LLM · Training-free
- **[Verify when Uncertain: Beyond Self-Consistency in Black Box Hallucination Detection](https://openreview.net/forum?id=6tlLISSgiu)** · TMLR 2026 · LLM · Training-free
- **[Trustworthiness, Hallucination, and Evaluation in Large Language Models](https://doi.org/10.56975/ijcrt.v14i4.307430)** · INTERNATIONAL JOURNAL OF CREATIVE RESEARCH THOUGHTS 2026 · LLM · Training-free
- **[The Virtue of Hallucination: When AI Mistakes Make Software Safer](https://doi.org/10.1109/MC.2026.3659286)** · Computer 2026 · LLM · Training-free
- **[The Immutable Hallucination: A Critical Analysis of AI-Blockchain Integration in Healthcare](https://doi.org/10.5220/0015138500005051)** · International Conference on Artificial Intelligence and Blockchain in Healthcare 2026 · LLM · Training-free
- **[The Double-Lock Framework: A Multi-Layered System for Grounded Retrieval-Augmented Generation and Hallucination Mitigation](https://doi.org/10.6025/ijclr/2026/17/2/100-126)** · Comput. Linguistics 2026 · LLM · Training-free
- **[The Case for Repeatable, Open, and Expert-Grounded Hallucination Benchmarks in Large Language Models](https://doi.org/10.1145/3803291.3803328)** · ICICT 2026 · LLM · Training-free
- **[Synonym Knowledge Graph Enhanced Language Model for Inconsistent Hallucination Detection](https://doi.org/10.1145/3819585)** · ACM Transactions on Asian and Low-Resource Language Information Processing 2026 · LLM · Training-free
- **📚 [Survey on Hallucination in Reasoning Large Language Model: Evaluation, Taxonomy, Intervention, and Open Issues](https://doi.org/10.3724/2096-7004.di.2025.0131)** · Data Intell. 2026 · LLM · Training-free
- **[Slopsquatting and package-hallucination in LLMS](https://doi.org/10.64643/ijirtv12i7-191660-459)** · International Journal of Innovative Research in Technology 2026 · LLM · Training-free
- **[Shadows in the Attention: Contextual Perturbation and Representation Drift in the Dynamics of Hallucination in LLMs](https://doi.org/10.1007/978-981-95-4088-4_32)** · Communications in Computer and Information Science 2026 · LLM · Training-free
- **[SelfCheck-Eval: A Multi-Module Framework for Zero-Resource Hallucination Detection in Large Language Models](https://doi.org/10.1016/j.patter.2026.101569)** · Patterns 2026 · LLM · Training-free
- **[SeaRAG: Reducing Hallucination in Retrieval-Augmented Generation via Statement-Entity Adaptive Ranking](https://doi.org/10.1145/3774904.3792598)** · WWW 2026 · LLM · Training-free
- **[SUMMIR: A Hallucination-Aware Framework for Ranking Sports Insights from LLMs](https://doi.org/10.1007/978-3-032-21289-4_23)** · ECIR 2026 · LLM · Training-free
- **[SINdex: Semantic INconsistency Index for Hallucination Detection in LLMs](https://doi.org/10.1109/OJCS.2026.3697236)** · IEEE Open J. Comput. Soc. 2026 · LLM · Training-free
- **[RusHallu-RAG: benchmarking hallucination detection for Russian RAG](https://doi.org/10.29003/2075-7182-2026-24-516-534)** · Comput. Linguistics 2026 · LLM · Training-free
- **[ReGA: Zero-Overhead Graph Alignment for Structural Hallucination Detection Without Generation](https://doi.org/10.1145/3774905.3794657)** · WWW 2026 · LLM · Training-free
- **[Rapid End-to-End Test Generation and Hallucination Mitigation Using Generative Artificial Intelligence](https://doi.org/10.1109/ACCESS.2026.3657407)** · IEEE Access 2026 · LLM · Training-free
- **[Quantifying Factual Divergence in Generative Models: SHAP-LIME Based Hallucination Score for LLMs](https://doi.org/10.1007/s00530-025-02150-4)** · Multim. Syst. 2026 · LLM · Training-free
- **[PromptFishing: Active Hallucination Inducement to Distinguish LLMs From Humans](https://doi.org/10.1109/tifs.2026.3709099)** · IEEE Transactions on Information Forensics and Security 2026 · LLM · Training-free
- **[Predicting LLM Correctness in Prosthodontics Using Metadata and Hallucination Signals](https://doi.org/10.5220/0014357700004070)** · BIOSTEC 2026 · LLM · Training-free
- **[Mitigating hallucinations in healthcare LLMs with granular fact-checking and domain-specific adaptation](https://doi.org/10.1016/j.eswa.2026.132966)** · ESWA 2026 · LLM · Training-free
- **[Mitigating LLM Hallucination Snowballing in Multiagent Systems via Context-Aware Semantic Consistency Reasoning](https://doi.org/10.1109/tnnls.2026.3655508)** · TNNLS 2026 · LLM · Training-free
- **[Mitigating Hallucination on Hallucination in RAG via Ensemble Voting](https://doi.org/10.1109/cscwd68734.2026.11582530)** · 29th International Conference on Computer Supported Cooperative Work in Design (CSCWD) 2026 · LLM · Training-free
- **[MVRL: A Multi-stage Training Framework for Value Alignment and Hallucination Suppression in Large Language Models](https://doi.org/10.1109/prmvai70103.2026.11605527)** · IEEE International Conference on Pattern Recognition, Machine Vision and Artificial Intelligence (PRMVAI) 2026 · LLM · Training-based
- **📚 [Loki’s Dance of Illusions: A Comprehensive Survey of Hallucination in Large Language Models](https://doi.org/10.1109/tcss.2026.3661295)** · IEEE Transactions on Computational Social Systems 2026 · LLM · Training-free
- **[Lie to Me: Knowledge Graphs for Robust Hallucination Self-Detection in LLMs](https://doi.org/10.5220/0014245100004067)** · ICPRAM 2026 · LLM · Training-free
- **[Learned Hallucination Detection in Black-Box LLMs using Token-level Entropy Production Rate](https://doi.org/10.1007/978-3-032-21289-4_8)** · ECIR 2026 · LLM · Training-free
- **[Lawsuit AraRAG: A Retrieval-Augmented Generation Framework for Arabic Legal Document Understanding and Hallucination Reduction](https://doi.org/10.1109/lt68265.2026.11592520)** · 23rd International Learning and Technology Conference (L&amp;T) 2026 · LLM · Training-free
- **📚 [Large language models hallucination: A comprehensive survey](https://doi.org/10.1016/j.cosrev.2026.100970)** · Comput. Sci. Rev. 2026 · LLM · Training-free
- **[LLMs Prompted for Graphs: Hallucinations and Generative Capabilities](https://doi.org/10.1007/s41109-025-00754-3)** · Appl. Netw. Sci. 2026 · LLM · Training-free
- **[Incident Response Planning Using a Lightweight Large Language Model with Reduced Hallucination](https://www.ndss-symposium.org/ndss-paper/incident-response-planning-using-a-lightweight-large-language-model-with-reduced-hallucination/)** · NDSS 2026 · LLM · Training-free
- **[HyGen—A Hybrid Automation Testing Approach for Reducing Hallucination in LLM-Based Applications](https://doi.org/10.1007/978-981-96-6537-2_2)** · Lecture Notes in Networks and Systems 2026 · LLM · Training-free
- **[How Human Experts Educate Specialized LLMs: Filling Knowledge Gaps in KG-Augmented Generation through Hallucination Detection](https://doi.org/10.1145/3774904.3792550)** · WWW 2026 · LLM · Training-free
- **📚 [House of Mirrors: A Survey on Hallucination Detection and Mitigation via Decoding Techniques in Language Models](https://doi.org/10.1007/978-3-032-03072-6_9)** · Lecture Notes in Networks and Systems 2026 · LLM · Training-free
- **📚 [Hallucination to truth: a review of fact-checking and factuality evaluation in large language models](https://doi.org/10.1007/s10462-025-11454-w)** · Artif. Intell. Rev. 2026 · LLM · Training-free
- **[Hallucination to Consensus: Multi-Agent LLMs for End-to-End JUnit Test Generation](https://doi.org/10.1145/3803418)** · ACM Transactions on Software Engineering and Methodology 2026 · LLM · Training-free
- **[Hallucination or Creativity: How to Evaluate AI-Generated Scientific Stories?](https://ceur-ws.org/Vol-4202/paper7.pdf)** · Text2Story@ECIR 2026 · LLM · Training-free
- **[Hallucination Mitigation with Agentic AI NLP-Based Open-Floor Standard](https://doi.org/10.5220/0013761000004052)** · ICAART 2026 · LLM · Training-free
- **[Hallucination Mitigation for EEG-to-Text Generation via Multi-Source Semantic Augmentation and Latent Space Regularization](https://doi.org/10.1109/icsipc69751.2026.11584213)** · International Conference on Signal Image Processing and Communication (ICSIPC) 2026 · LLM · Training-free
- **[Hallucination Early Detection in Diffusion Models](https://doi.org/10.1007/s11263-025-02622-0)** · IJCV 2026 · LLM · Training-free
- **[Hallucination Detection, Categorization, and Mitigation in Large Language Models: A Cross-Domain Evaluation Framework](https://doi.org/10.64388/irev9i10-1716821)** · Iconic Research and Engineering Journals 2026 · LLM · Training-free
- **[Hallucination Detection in Large Language Models via Multi-Granular Uncertainty Quantification](https://doi.org/10.59543/comdem.v3i.17665)** · Computer and Decision Making: An International Journal 2026 · LLM · Training-free
- **[Hallucination Detection in Large Language Models using Self Consistency Signals](https://doi.org/10.1109/iccnct68477.2026.11590608)** · International Conference on Computer Networks and Inventive Communication Technologies (ICCNCT) 2026 · LLM · Training-free
- **[Hallucination Detection and Mitigation with Diffusion in Multi-Variate Time-Series Foundation Models](https://openreview.net/forum?id=fHGQ7hZlb5)** · TMLR 2026 · LLM · Training-free
- **[Hallucination Detection and Mitigation in Large Language Models Using Lightweight Inference-Time Models](https://doi.org/10.55248/gengpi.07.0426.c1028)** · International Journal of Research Publication and Reviews 2026 · LLM · Training-free
- **[HalluJudge: A Reference-Free Hallucination Detection for Context Misalignment in Code Review Automation](https://doi.org/10.1145/3803437.3805236)** · SIGSOFT FSE Companion 2026 · LLM · Training-free
- **[GraphHall: A Graph-Based Framework for Hallucination Detection in Large Language Models](https://doi.org/10.1109/tai.2026.3715425)** · TAI 2026 · LLM · Training-free
- **[FACTUM: Mechanistic Detection of Citation Hallucination in Long-Form RAG](https://doi.org/10.1007/978-3-032-21289-4_18)** · ECIR 2026 · LLM · Training-free
- **[Exploring and Mitigating Fawning Hallucinations in Large Language Models](https://doi.org/10.1016/j.neucom.2025.132166)** · NEUCOM 2026 · LLM · Training-free
- **[Eroding the Truth-Default: A Causal Analysis of Human Susceptibility to Foundation Model Hallucinations and Disinformation in the Wild](https://doi.org/10.1145/3774905.3795832)** · WWW 2026 · LLM · Training-free
- **[Enhancing Factual Consistency in Large Language Models: An Integrative Paradigm of Grounding and Self-Prompting Methods for Hallucination Minimization](https://doi.org/10.1007/978-981-96-9771-7_13)** · Lecture Notes in Networks and Systems 2026 · LLM · Training-free
- **📋 [EH-Benchmark Ophthalmic Hallucination Benchmark and Agent-Driven Top-Down Traceable Reasoning Workflow](https://doi.org/10.1016/j.inffus.2025.103631)** · INFFUS 2026 · LLM · Training-free
- **[Don't Let It Hallucinate: Premise Verification via Retrieval-Augmented Logical Reasoning](https://openreview.net/forum?id=BDxStRGWba)** · TMLR 2026 · LLM · Training-free
- **[Do Vision Encoders Truly Explain Object Hallucination?: Mitigating Object Hallucination via Simple Fine-Grained CLIPScore](https://openreview.net/forum?id=JTua6tDPgZ)** · TMLR 2026 · LLM · Training-free
- **[Detectra-AI Response Hallucination Detector](https://doi.org/10.62226/ijarst20262726)** · International Journal of Advanced Research in Science and Technology 2026 · LLM · Training-free
- **[Detecting and Correcting Hallucinations in LLM-Generated Code via Deterministic AST Analysis](https://doi.org/10.1145/3793655.3793725)** · FORGE@ICSE 2026 · LLM · Training-free
- **[Data Leakage and Model Hallucination](https://doi.org/10.1002/9781394402069.ch10)** · Adversarial Machine Learning 2026 · LLM · Training-free
- **[DHI: Leveraging Diverse Hallucination Induction for Enhanced Contrastive Factuality Control in Large Language Models](https://doi.org/10.1007/978-981-95-4088-4_15)** · Communications in Computer and Information Science 2026 · LLM · Training-free
- **[Cross-model diffusion: Mitigating hallucination in large language models for rumor detection](https://doi.org/10.1016/j.neunet.2026.109226)** · NN 2026 · LLM · Training-free
- **[Comprehensive to the Textual Hallucination in Generative AI](https://doi.org/10.2991/978-94-6239-648-7_37)** · Advances in Computer Science Research 2026 · LLM · Training-free
- **[Collaborated With Hallucination: Enhancing Egocentric Grounded Question Answering via Error Demonstrations](https://doi.org/10.1109/TIP.2026.3666732)** · TIP 2026 · LLM · Training-free
- **[Cascaded Verification Framework: A Progressive Approach for Mitigating Hallucinations in Large Language Models](https://doi.org/10.1145/3774904.3792852)** · WWW 2026 · LLM · Training-free
- **[CHIME: Conditional Hallucination and Integrated Multi-scale Enhancement for Time Series Diffusion Model](https://doi.org/10.1016/j.knosys.2026.116089)** · KBS 2026 · LLM · Training-free
- **[Beyond Functional Correctness: Exploring Hallucinations in LLM-Generated Code](https://doi.org/10.1109/TSE.2026.3657432)** · IEEE Trans. Software Eng. 2026 · LLM · Training-free
- **[Beware of the Woozle Effect: Exploring and Mitigating Hallucination Propagation in Multi-Agent Debate](https://doi.org/10.1109/taslpro.2026.3675803)** · TASLP 2026 · LLM · Training-free
- **📋 [AutoHall: Automated Factuality Hallucination Dataset Generation for Large Language Models](https://doi.org/10.1109/taslpro.2025.3635038)** · TASLP 2026 · LLM · Training-free
- **📚 [Attribution Techniques for Mitigating Hallucinated Information in RAG Systems: A Survey](https://doi.org/10.1109/ICAIIC68212.2026.11454197)** · ICAIIC 2026 · LLM · Training-free
- **[Analog Hawking Radiation in Transformer Neural Networks: Discrete Geometric Horizons, Information Thermodynamics, and Hallucination Suppression](https://doi.org/10.33140/amlai.07.01.05)** · Advances in Machine Learning & Artificial Intelligence 2026 · LLM · Training-free
- **[Analisis Implementasi Artificial Intelligence dalam Audit Keuangan Atas Kasus Hallucination AI Deloitte Australia 2025](https://doi.org/10.31004/riggs.v5i2.9653)** · RIGGS: Journal of Artificial Intelligence and Digital Business 2026 · LLM · Training-free
- **[Agentic Data Architecture (Ada): Eliminating The Api Layer For Hallucination-Free, Sub-100ms Enterprise AI Agents](https://doi.org/10.63363/aijfr.2026.v07i02.4079)** · Advanced International Journal for Research 2026 · LLM · Training-free
- **[Adversarial Abductive Dialogue Framework with Reinforcement for Tackling LLM Hallucination](https://doi.org/10.1007/978-3-032-16524-4_3)** · Applications of Neuro-Symbolic Artificial Intelligence 2026 · LLM · Training-free
- **[Advancing LLM-Generated Code Reliability: A Hybrid Approach for Hallucination Detection](https://doi.org/10.1109/TSE.2025.3640641)** · IEEE Trans. Software Eng. 2026 · LLM · Training-free
- **[Addressing Hallucinations with RAG and NMISS in Italian Healthcare LLM Chatbots](https://doi.org/10.1016/j.datak.2026.102627)** · Data Knowl. Eng. 2026 · LLM · Training-free
- **[AI Hallucination Prediction: A Novel Approach for Preventing False AI Outputs](https://doi.org/10.1007/978-3-032-06688-6_48)** · Lecture Notes in Networks and Systems 2026 · LLM · Training-free
- **📚 [A Taxonomy of Machine Hallucination in Radiology](https://doi.org/10.1148/ryai.250203)** · Radiology: Artificial Intelligence 2026 · LLM · Training-free
- **📚 [A Survey of Hallucination in Large Language Models](https://doi.org/10.12677/airr.2026.151016)** · Artificial Intelligence and Robotics Research 2026 · LLM · Training-free
- **[A Real-Time Verification Framework for Hallucination and Bias Detection in AI Generated Text](https://doi.org/10.1109/icicv68925.2026.11554618)** · 7th International Conference on Intelligent Communication Technologies and Virtual Mobile Networks (ICICV) 2026 · LLM · Training-free
- **[A Non-intrusive Plug-and-play Method for Hallucination Mitigation via LID-guided Input Preprocessing](https://doi.org/10.1007/s11633-025-1596-7)** · Mach. Intell. Res. 2026 · LLM · Training-free
- **[A Multi-Metric Evaluation Perspective on Hallucination Detection in Low-Resource Governance Documents](https://doi.org/10.64388/irev9i11-1717980)** · Iconic Research and Engineering Journals 2026 · LLM · Training-free
- **[A Knowledge Graph Approach Towards Detecting Large Language Model Hallucination](https://doi.org/10.1007/978-3-032-08384-5_19)** · Lecture Notes in Networks and Systems 2026 · LLM · Training-free
- **[A Hybrid Framework for Hallucination Detection in Large Language Models](https://doi.org/10.1109/tai.2026.3653354)** · TAI 2026 · LLM · Training-free
- **[A Context-Aware Hallucination Detection Framework for Large Language Models in High-Stakes Domains](https://doi.org/10.18535/ijecs/v15i06.5531)** · International Journal of Engineering and Computer Science 2026 · LLM · Training-free

</details>

<details>
<summary>📅 2025 · 472 papers</summary>

- **[Towards Unification of Hallucination Detection and Fact Verification for Large Language Models](https://arxiv.org/abs/2512.02772)** · arXiv · LLM · Training-free
- **[The Semantic Illusion: Certified Limits of Embedding-Based Hallucination Detection in RAG Systems](https://arxiv.org/abs/2512.15068)** · arXiv · LLM · Training-free
- **[Semantic Faithfulness and Entropy Production Measures to Tame Your LLM Demons and Manage Hallucinations](https://arxiv.org/abs/2512.05156)** · arXiv · LLM · Training-free
- **[Photorealistic Phantom Roads in Real Scenes: Disentangling 3D Hallucinations from Physical Geometry](https://arxiv.org/abs/2512.15423)** · arXiv · LLM · Training-free
- **[Neural Probe-Based Hallucination Detection for Large Language Models](https://arxiv.org/abs/2512.20949)** · arXiv · LLM · Training-free
- **[Model-First Reasoning LLM Agents: Reducing Hallucinations through Explicit Problem Modeling](https://arxiv.org/abs/2512.14474)** · arXiv · LLM · Training-free
- **[Mitigating hallucinations and omissions in LLMs for invertible problems: An application to hardware logic design automation](https://arxiv.org/abs/2512.03053)** · arXiv · LLM · Training-free
- **[Mitigating LLM Hallucination via Behaviorally Calibrated Reinforcement Learning](https://arxiv.org/abs/2512.19920)** · arXiv · LLM · Training-based
- **[Mitigating Hallucinations in Zero-Shot Scientific Summarisation: A Pilot Study](https://arxiv.org/abs/2512.00931)** · arXiv · LLM · Training-free
- **[InpaintDPO: Mitigating Spatial Relationship Hallucinations in Foreground-conditioned Inpainting via Diverse Preference Optimization](https://arxiv.org/abs/2512.15644)** · arXiv · LLM · Training-based
- **[Incentives or Ontology? A Structural Rebuttal to OpenAI's Hallucination Thesis](https://arxiv.org/abs/2512.14801)** · arXiv · LLM · Training-free
- **[Hybrid-Code v2: Zero-Hallucination Clinical ICD-10 Coding via Neuro-Symbolic Verification and Automated Knowledge Base Expansion](https://arxiv.org/abs/2512.23743)** · arXiv · LLM · Training-free
- **[HaluNet: Learning Hallucination Risk from Internal Signals in LLM Question Answering](https://arxiv.org/abs/2512.24562)** · arXiv · LLM · Training-free
- **[Hallucination Detection and Evaluation of Large Language Model](https://arxiv.org/abs/2512.22416)** · arXiv · LLM · Training-free
- **[HalluMat: Detecting Hallucinations in LLM-Generated Materials Science Content Through Multi-Stage Verification](https://arxiv.org/abs/2512.22396)** · arXiv · LLM · Training-free
- **[HalluGraph: Auditable Hallucination Detection for Legal RAG Systems via Knowledge Graph Alignment](https://arxiv.org/abs/2512.01659)** · arXiv · LLM · Training-free
- **[H-Neurons: On the Existence, Impact, and Origin of Hallucination-Associated Neurons in LLMs](https://arxiv.org/abs/2512.01797)** · arXiv · LLM · Training-free
- **[FVA-RAG: Falsification-Verification Alignment for Mitigating Sycophantic Hallucinations](https://arxiv.org/abs/2512.07015)** · arXiv · LLM · Training-free
- **[Does Less Hallucination Mean Less Creativity? An Empirical Investigation in LLMs](https://arxiv.org/abs/2512.11509)** · arXiv · LLM · Training-free
- **[Detecting Hallucinations in Graph Retrieval-Augmented Generation via Attention Patterns and Semantic Alignment](https://arxiv.org/abs/2512.09148)** · arXiv · LLM · Training-free
- **[Detecting AI Hallucinations in Finance: An Information-Theoretic Method Cuts Hallucination Rate by 92%](https://arxiv.org/abs/2512.03107)** · arXiv · LLM · Training-free
- **[CONFIDE: Hallucination Assessment for Reliable Biomolecular Structure Prediction and Design](https://arxiv.org/abs/2512.02033)** · arXiv · LLM · Training-free
- **[CIP: A Plug-and-Play Causal Prompting Framework for Mitigating Hallucinations under Long-Context Noise](https://arxiv.org/abs/2512.11282)** · arXiv · LLM · Training-free
- **[Bounding Hallucinations: Information-Theoretic Guarantees for RAG Systems via Merlin-Arthur Protocols](https://arxiv.org/abs/2512.11614)** · arXiv · LLM · Training-free
- **[Beyond Hallucinations: A Composite Score for Measuring Reliability in Open-Source Large Language Models](https://arxiv.org/abs/2512.24058)** · arXiv · LLM · Training-free
- **📋 [BHRAM-IL: A Benchmark for Hallucination Recognition and Assessment in Multiple Indian Languages](https://arxiv.org/abs/2512.01852)** · arXiv · LLM · Training-free
- **[A Unified Definition of Hallucination: It's The World Model, Stupid!](https://arxiv.org/abs/2512.21577)** · arXiv · LLM · Training-free
- **📚 [A Concise Review of Hallucinations in LLMs and their Mitigation](https://arxiv.org/abs/2512.02527)** · arXiv · LLM · Training-free
- **[Wisdom is Knowing What not to Say: Hallucination-Free LLMs Unlearning via Attention Shifting](http://papers.nips.cc/paper_files/paper/2025/hash/8eb3e953455f01ebbd83d7df351bdf95-Abstract-Conference.html)** · NeurIPS 2025 · LLM · Training-based
- **[SECA: Semantically Equivalent and Coherent Attacks for Eliciting LLM Hallucinations](http://papers.nips.cc/paper_files/paper/2025/hash/d077bc9ea82a2998ca6b2d0158b5ac6e-Abstract-Conference.html)** · NeurIPS 2025 · LLM · Training-free
- **[Robust Hallucination Detection in LLMs via Adaptive Token Selection](http://papers.nips.cc/paper_files/paper/2025/hash/b7c43d4a79dede363a2d061c6158e5a5-Abstract-Conference.html)** · NeurIPS 2025 · LLM · Training-free
- **[Reasoning Models Hallucinate More: Factuality-Aware Reinforcement Learning for Large Reasoning Models](http://papers.nips.cc/paper_files/paper/2025/hash/ddd50f29fa472095515fa0df31749e6c-Abstract-Conference.html)** · NeurIPS 2025 · LLM · Training-based
- **📋 [PHANTOM: A Benchmark for Hallucination Detection in Financial Long-Context QA](http://papers.nips.cc/paper_files/paper/2025/hash/b8badadce3f482ba340ff870f4894441-Abstract-Datasets_and_Benchmarks_Track.html)** · NeurIPS 2025 · LLM · Training-free
- **[One SPACE to Rule Them All: Jointly Mitigating Factuality and Faithfulness Hallucinations in LLMs](http://papers.nips.cc/paper_files/paper/2025/hash/e77d684aae157abd84df1eeb76d8b9cd-Abstract-Conference.html)** · NeurIPS 2025 · LLM · Training-free
- **[Investigating Hallucinations of Time Series Foundation Models through Signal Subspace Analysis](http://papers.nips.cc/paper_files/paper/2025/hash/a5059a9a389ccc76da85760ea79490d8-Abstract-Conference.html)** · NeurIPS 2025 · LLM · Training-free
- **[Generalization or Hallucination? Understanding Out-of-Context Reasoning in Transformers](http://papers.nips.cc/paper_files/paper/2025/hash/cc7c9c8e4a84b0ca00d874e1a8938644-Abstract-Conference.html)** · NeurIPS 2025 · LLM · Training-free
- **[FACT: Mitigating Inconsistent Hallucinations in LLMs via Fact-Driven Alternating Code-Text Training](http://papers.nips.cc/paper_files/paper/2025/hash/bc75254bc4b8b42f401d0ab5d6e9aa4b-Abstract-Conference.html)** · NeurIPS 2025 · LLM · Training-free
- **[Beyond Token Probes: Hallucination Detection via Activation Tensors with ACT-ViT](http://papers.nips.cc/paper_files/paper/2025/hash/7b8694d58c34b9bec9c2f29735c3a250-Abstract-Conference.html)** · NeurIPS 2025 · LLM · Training-free
- **[Benford's Curse: Tracing Digit Bias to Numerical Hallucination in LLMs](http://papers.nips.cc/paper_files/paper/2025/hash/aa5f5e6eb6f613ec412f1d948dfa21a5-Abstract-Conference.html)** · NeurIPS 2025 · LLM · Training-free
- **[Auditing Meta-Cognitive Hallucinations in Reasoning Large Language Models](http://papers.nips.cc/paper_files/paper/2025/hash/ee0e336e2423430ef86071300299e074-Abstract-Conference.html)** · NeurIPS 2025 · LLM · Training-free
- **[Alleviating Hallucinations in Large Language Models through Multi-Model Contrastive Decoding and Dynamic Hallucination Detection](http://papers.nips.cc/paper_files/paper/2025/hash/f1a92c4df8cd7dc1cab2613fb999d5e7-Abstract-Conference.html)** · NeurIPS 2025 · LLM · Training-free
- **[When Bias Pretends to Be Truth: How Spurious Correlations Undermine Hallucination Detection in LLMs](https://arxiv.org/abs/2511.07318)** · arXiv · LLM · Training-free
- **[Thinking, Faithful and Stable: Mitigating Hallucinations in LLMs](https://arxiv.org/abs/2511.15921)** · arXiv · LLM · Training-free
- **[The Map of Misbelief: Tracing Intrinsic and Extrinsic Hallucinations Through Attention Patterns](https://arxiv.org/abs/2511.10837)** · arXiv · LLM · Training-free
- **[Stemming Hallucination in Language Models Using a Licensing Oracle](https://arxiv.org/abs/2511.06073)** · arXiv · LLM · Training-free
- **[Place Matters: Comparing LLM Hallucination Rates for Place-Based Legal Queries](https://arxiv.org/abs/2511.06700)** · arXiv · LLM · Training-free
- **[Measuring the Impact of Lexical Training Data Coverage on Hallucination Detection in Large Language Models](https://arxiv.org/abs/2511.17946)** · arXiv · LLM · Training-free
- **[Mathematical Analysis of Hallucination Dynamics in Large Language Models: Uncertainty Quantification, Advanced Decoding, and Principled Mitigation](https://arxiv.org/abs/2511.15005)** · arXiv · LLM · Training-free
- **📋 [MUCH: A Multilingual Claim Hallucination Benchmark](https://arxiv.org/abs/2511.17081)** · arXiv · LLM · Training-free
- **[Learning Under Laws: A Constraint-Projected Neural PDE Solver that Eliminates Hallucinations](https://arxiv.org/abs/2511.03578)** · arXiv · LLM · Training-free
- **[Laplacian Score Sharpening for Mitigating Hallucination in Diffusion Models](https://arxiv.org/abs/2511.07496)** · arXiv · LLM · Training-free
- **[HaluMem: Evaluating Hallucinations in Memory Systems of Agents](https://arxiv.org/abs/2511.03506)** · arXiv · LLM · Training-free
- **[GRAD: Graph-Retrieved Adaptive Decoding for Hallucination Mitigation](https://arxiv.org/abs/2511.03900)** · arXiv · LLM · Training-free
- **[Diagnosing Hallucination Risk in AI Surgical Decision-Support: A Sequential Framework for Sequential Validation](https://arxiv.org/abs/2511.00588)** · arXiv · LLM · Training-free
- **[Critical Confabulation: Can LLMs Hallucinate for Social Good?](https://arxiv.org/abs/2511.07722)** · arXiv · LLM · Training-free
- **[Can a Small Model Learn to Look Before It Leaps? Dynamic Learning and Proactive Correction for Hallucination Detection](https://arxiv.org/abs/2511.05854)** · arXiv · LLM · Training-free
- **[Can LLMs Detect Their Own Hallucinations?](https://arxiv.org/abs/2511.11087)** · arXiv · LLM · Training-free
- **[COMPASS: Context-Modulated PID Attention Steering System for Hallucination Mitigation](https://arxiv.org/abs/2511.14776)** · arXiv · LLM · Training-free
- **["AGI" team at SHROOM-CAP: Data-Centric Approach to Multilingual Hallucination Detection using XLM-RoBERTa](https://arxiv.org/abs/2511.18301)** · arXiv · LLM · Training-free
- **[Zero-knowledge LLM hallucination detection and mitigation through fine-grained cross-model consistency](https://doi.org/10.18653/v1/2025.emnlp-industry.139)** · EMNLP 2025 · LLM · Training-free
- **[When Models Lie, We Learn: Multilingual Span-Level Hallucination Detection with PsiloQA](https://doi.org/10.18653/v1/2025.findings-emnlp.626)** · EMNLP 2025 · LLM · Training-free
- **[Unsupervised Hallucination Detection by Inspecting Reasoning Processes](https://doi.org/10.18653/v1/2025.emnlp-main.1124)** · EMNLP 2025 · LLM · Training-free
- **[Trust Me, I'm Wrong: LLMs Hallucinate with Certainty Despite Knowing the Answer](https://doi.org/10.18653/v1/2025.findings-emnlp.792)** · EMNLP 2025 · LLM · Training-free
- **[The Impact of Negated Text on Hallucination with Large Language Models](https://doi.org/10.18653/v1/2025.emnlp-main.684)** · EMNLP 2025 · LLM · Training-free
- **[The Illusion of Progress: Re-evaluating Hallucination Detection in LLMs](https://doi.org/10.18653/v1/2025.emnlp-main.1761)** · EMNLP 2025 · LLM · Training-free
- **[The Hallucination Tax of Reinforcement Finetuning](https://doi.org/10.18653/v1/2025.findings-emnlp.112)** · EMNLP 2025 · LLM · Training-free
- **[Simple Factuality Probes Detect Hallucinations in Long-Form Natural Language Generation](https://doi.org/10.18653/v1/2025.findings-emnlp.880)** · EMNLP 2025 · LLM · Training-free
- **[SAFE: A Sparse Autoencoder-Based Framework for Robust Query Enrichment and Hallucination Mitigation in LLMs](https://doi.org/10.18653/v1/2025.findings-emnlp.496)** · EMNLP 2025 · LLM · Training-free
- **[Representation-based Broad Hallucination Detectors Fail to Generalize Out of Distribution](https://doi.org/10.18653/v1/2025.findings-emnlp.952)** · EMNLP 2025 · LLM · Training-free
- **[Regularized Contrastive Decoding with Hard Negative Samples for LLM Hallucination Mitigation](https://doi.org/10.18653/v1/2025.findings-emnlp.322)** · EMNLP 2025 · LLM · Training-free
- **[Mitigating Hallucinations in LM-Based TTS Models via Distribution Alignment Using GFlowNets](https://doi.org/10.18653/v1/2025.emnlp-main.976)** · EMNLP 2025 · LLM · Training-free
- **[Mitigating Geospatial Knowledge Hallucination in Large Language Models: Benchmarking and Dynamic Factuality Aligning](https://doi.org/10.18653/v1/2025.findings-emnlp.45)** · EMNLP 2025 · LLM · Training-free
- **📋 [MedHallu: A Comprehensive Benchmark for Detecting Medical Hallucinations in Large Language Models](https://doi.org/10.18653/v1/2025.emnlp-main.143)** · EMNLP 2025 · LLM · Training-free
- **[Low-Hallucination and Efficient Coreference Resolution with LLMs](https://doi.org/10.18653/v1/2025.findings-emnlp.934)** · EMNLP 2025 · LLM · Training-free
- **[Logit Space Constrained Fine-Tuning for Mitigating Hallucinations in LLM-Based Recommender Systems](https://doi.org/10.18653/v1/2025.emnlp-main.1491)** · EMNLP 2025 · LLM · Training-free
- **[Humans Hallucinate Too: Language Models Identify and Correct Subjective Annotation Errors With Label-in-a-Haystack Prompts](https://doi.org/10.18653/v1/2025.emnlp-main.993)** · EMNLP 2025 · LLM · Training-free
- **[How Much Do LLMs Hallucinate across Languages? On Realistic Multilingual Estimation of LLM Hallucination](https://doi.org/10.18653/v1/2025.emnlp-main.1481)** · EMNLP 2025 · LLM · Training-free
- **[Hallucination Detection in Structured Query Generation via LLM Self-Debating](https://doi.org/10.18653/v1/2025.findings-emnlp.873)** · EMNLP 2025 · LLM · Training-free
- **[Hallucination Detection in LLMs Using Spectral Features of Attention Maps](https://doi.org/10.18653/v1/2025.emnlp-main.1239)** · EMNLP 2025 · LLM · Training-free
- **[HalluDetect: Detecting, Mitigating, and Benchmarking Hallucinations in Conversational Systems in the Legal Domain](https://doi.org/10.18653/v1/2025.emnlp-industry.128)** · EMNLP 2025 · LLM · Training-free
- **[HEAL: An Empirical Study on Hallucinations in Embodied Agents Driven by Large Language Models](https://doi.org/10.18653/v1/2025.findings-emnlp.1158)** · EMNLP 2025 · LLM · Training-free
- **[FG-PRM: Fine-grained Hallucination Detection and Mitigation in Language Model Mathematical Reasoning](https://doi.org/10.18653/v1/2025.findings-emnlp.228)** · EMNLP 2025 · LLM · Training-free
- **[FACTCHECKMATE: Preemptively Detecting and Mitigating Hallucinations in LMs](https://doi.org/10.18653/v1/2025.findings-emnlp.663)** · EMNLP 2025 · LLM · Training-free
- **[Exploring the Generalizability of Factual Hallucination Mitigation via Enhancing Precise Knowledge Utilization](https://doi.org/10.18653/v1/2025.findings-emnlp.211)** · EMNLP 2025 · LLM · Training-free
- **[Evaluating Evaluation Metrics - The Mirage of Hallucination Detection](https://doi.org/10.18653/v1/2025.findings-emnlp.1035)** · EMNLP 2025 · LLM · Training-free
- **[Detecting LLM Hallucination Through Layer-wise Information Deficiency: Analysis of Ambiguous Prompts and Unanswerable Questions](https://doi.org/10.18653/v1/2025.emnlp-main.1644)** · EMNLP 2025 · LLM · Training-free
- **[DeCoRe: Decoding by Contrasting Retrieval Heads to Mitigate Hallucinations](https://doi.org/10.18653/v1/2025.findings-emnlp.531)** · EMNLP 2025 · LLM · Training-free
- **[Chain-of-Thought Prompting Obscures Hallucination Cues in Large Language Models: An Empirical Evaluation](https://doi.org/10.18653/v1/2025.findings-emnlp.67)** · EMNLP 2025 · LLM · Training-free
- **[Calibrating Verbal Uncertainty as a Linear Feature to Reduce Hallucinations](https://doi.org/10.18653/v1/2025.emnlp-main.187)** · EMNLP 2025 · LLM · Training-free
- **[CCL-XCoT: An Efficient Cross-Lingual Knowledge Transfer Method for Mitigating Hallucination Generation](https://doi.org/10.18653/v1/2025.findings-emnlp.93)** · EMNLP 2025 · LLM · Training-free
- **[Bridging External and Parametric Knowledge: Mitigating Hallucination of LLMs with Shared-Private Semantic Synergy in Dual-Stream Knowledge](https://doi.org/10.18653/v1/2025.emnlp-main.549)** · EMNLP 2025 · LLM · Training-free
- **[Bold Claims or Self-Doubt? Factuality Hallucination Type Detection via Belief State](https://doi.org/10.18653/v1/2025.findings-emnlp.527)** · EMNLP 2025 · LLM · Training-free
- **[Attention-guided Self-reflection for Zero-shot Hallucination Detection in Large Language Models](https://doi.org/10.18653/v1/2025.emnlp-main.1063)** · EMNLP 2025 · LLM · Training-free
- **[Active Layer-Contrastive Decoding Reduces Hallucination in Large Language Model Generation](https://doi.org/10.18653/v1/2025.emnlp-main.150)** · EMNLP 2025 · LLM · Training-free
- **[A Head to Predict and a Head to Question: Pre-trained Uncertainty Quantification Heads for Hallucination Detection in LLM Outputs](https://doi.org/10.18653/v1/2025.emnlp-main.1809)** · EMNLP 2025 · LLM · Training-free
- **[When Hallucination Costs Millions: Benchmarking AI Agents in High-Stakes Adversarial Financial Markets](https://arxiv.org/abs/2510.00332)** · arXiv · LLM · Training-free
- **[Uncertainty Quantification for Hallucination Detection in Large Language Models: Foundations, Methodology, and Future Directions](https://arxiv.org/abs/2510.12040)** · arXiv · LLM · Training-free
- **[Trustworthy Retrosynthesis: Eliminating Hallucinations with a Diverse Ensemble of Reaction Scorers](https://arxiv.org/abs/2510.10645)** · arXiv · LLM · Training-free
- **[Train for Truth, Keep the Skills: Binary Retrieval-Augmented Reward Mitigates Hallucinations](https://arxiv.org/abs/2510.17733)** · arXiv · LLM · Training-free
- **[TraceDet: Hallucination Detection from the Decoding Trace of Diffusion Large Language Models](https://arxiv.org/abs/2510.01274)** · arXiv · LLM · Training-free
- **[The Geometry of Truth: Layer-wise Semantic Dynamics for Hallucination Detection in Large Language Models](https://arxiv.org/abs/2510.04933)** · arXiv · LLM · Training-free
- **[TAG: Tangential Amplifying Guidance for Hallucination-Resistant Sampling](https://arxiv.org/abs/2510.04533)** · arXiv · LLM · Training-free
- **[Revisiting Hallucination Detection with Effective Rank-based Uncertainty](https://arxiv.org/abs/2510.08389)** · arXiv · LLM · Training-free
- **📚 [Review of Hallucination Understanding in Large Language and Vision Models](https://arxiv.org/abs/2510.00034)** · arXiv · LLM · Training-free
- **[Reasoning's Razor: Reasoning Improves Accuracy but Can Hurt Recall at Critical Operating Points in Safety and Hallucination Detection](https://arxiv.org/abs/2510.21049)** · arXiv · LLM · Training-free
- **[Neural Diversity Regularizes Hallucinations in Language Models](https://arxiv.org/abs/2510.20690)** · arXiv · LLM · Training-free
- **[Multi-stage Prompt Refinement for Mitigating Hallucinations in Large Language Models](https://arxiv.org/abs/2510.12032)** · arXiv · LLM · Training-free
- **📚 [Mitigating Hallucination in Large Language Models (LLMs): An Application-Oriented Survey on RAG, Reasoning, and Agentic Systems](https://arxiv.org/abs/2510.24476)** · arXiv · LLM · Training-free
- **[Mitigating Diffusion Model Hallucinations with Dynamic Guidance](https://arxiv.org/abs/2510.05356)** · arXiv · LLM · Training-free
- **[Measuring Language Model Hallucinations Through Distributional Correctness](https://arxiv.org/abs/2510.04302)** · arXiv · LLM · Training-free
- **[Learning to Reason for Hallucination Span Detection](https://arxiv.org/abs/2510.02173)** · arXiv · LLM · Training-free
- **[InterpDetect: Interpretable Signals for Detecting Hallucinations in Retrieval-Augmented Generation](https://arxiv.org/abs/2510.21538)** · arXiv · LLM · Training-free
- **[Hallucinations in Bibliographic Recommendation: Citation Frequency as a Proxy for Training Data Redundancy](https://arxiv.org/abs/2510.25378)** · arXiv · LLM · Training-free
- **[Hallucination-Resistant, Domain-Specific Research Assistant with Self-Evaluation and Vector-Grounded Retrieval](https://arxiv.org/abs/2510.02326)** · arXiv · LLM · Training-free
- **[Hallucination reduction with CASAL: Contrastive Activation Steering For Amortized Learning](https://arxiv.org/abs/2510.02324)** · arXiv · LLM · Training-free
- **[Hallucination is Inevitable for LLMs with the Open World Assumption](https://arxiv.org/abs/2510.05116)** · arXiv · LLM · Training-free
- **[HAD: HAllucination Detection Language Models Based on a Comprehensive Hallucination Taxonomy](https://arxiv.org/abs/2510.19318)** · arXiv · LLM · Training-free
- **[HACK: Hallucinations Along Certainty and Knowledge Axes](https://arxiv.org/abs/2510.24222)** · arXiv · LLM · Training-free
- **[Distributional Semantics Tracing: A Framework for Explaining Hallucinations in Large Language Models](https://arxiv.org/abs/2510.06107)** · arXiv · LLM · Training-free
- **[Detecting Hallucinations in Authentic LLM-Human Interactions](https://arxiv.org/abs/2510.10539)** · arXiv · LLM · Training-free
- **[Credal Transformer: A Principled Approach for Quantifying and Mitigating Hallucinations in Large Language Models](https://arxiv.org/abs/2510.12137)** · arXiv · LLM · Training-free
- **[Counting Hallucinations in Diffusion Models](https://arxiv.org/abs/2510.13080)** · arXiv · LLM · Training-free
- **[Confidence-Aware Routing for Large Language Model Reliability Enhancement: A Multi-Signal Approach to Pre-Generation Hallucination Mitigation](https://arxiv.org/abs/2510.01237)** · arXiv · LLM · Training-free
- **📋 [Confabulations from ACL Publications (CAP): A Dataset for Scientific Hallucination Detection](https://arxiv.org/abs/2510.22395)** · arXiv · LLM · Training-free
- **📋 [Challenging Multilingual LLMs: A New Taxonomy and Benchmark for Unraveling Hallucination in Translation](https://arxiv.org/abs/2510.24073)** · arXiv · LLM · Training-free
- **[Beyond "Hallucinations": A Framework for Stable Human-AI Reasoning](https://arxiv.org/abs/2510.14665)** · arXiv · LLM · Training-free
- **[A novel hallucination classification framework](https://arxiv.org/abs/2510.05189)** · arXiv · LLM · Training-free
- **[A Graph Signal Processing Framework for Hallucination Detection in Large Language Models](https://arxiv.org/abs/2510.19117)** · arXiv · LLM · Training-free
- **[VisHall3D: Monocular Semantic Scene Completion from Reconstructing the Visible Regions to Hallucinating the Invisible Regions](https://doi.org/10.1109/ICCV51701.2025.02663)** · ICCV 2025 · LLM · Training-free
- **[Towards Mitigation of Hallucination for LLM-empowered Agents: Progressive Generalization Bound Exploration and Watchdog Monitor](https://doi.org/10.3233/FAIA250910)** · ECAI 2025 · LLM · Training-free
- **[Mitigating Object Hallucinations via Sentence-Level Early Intervention](https://doi.org/10.1109/ICCV51701.2025.00067)** · ICCV 2025 · LLM · Training-free
- **[ChartCap: Mitigating Hallucination of Dense Chart Captioning](https://doi.org/10.1109/ICCV51701.2025.01224)** · ICCV 2025 · LLM · Training-free
- **[Why Language Models Hallucinate](https://arxiv.org/abs/2509.04664)** · arXiv · LLM · Training-free
- **[Turk-LettuceDetect: A Hallucination Detection Models for Turkish RAG Applications](https://arxiv.org/abs/2509.17671)** · arXiv · LLM · Training-free
- **[Real-Time Detection of Hallucinated Entities in Long-Form Generation](https://arxiv.org/abs/2509.03531)** · arXiv · LLM · Training-free
- **[Quantifying Genuine Awareness in Hallucination Prediction Beyond Question-Side Shortcuts](https://arxiv.org/abs/2509.15339)** · arXiv · LLM · Training-free
- **📋 [PerHalluEval: Persian Hallucination Evaluation Benchmark for Large Language Models](https://arxiv.org/abs/2509.21104)** · arXiv · LLM · Training-free
- **[Library Hallucinations in LLM-Generated Code: A Risk Analysis Grounded in Developer Queries](https://arxiv.org/abs/2509.22202)** · arXiv · LLM · Training-free
- **[LUMINA: Detecting Hallucinations in RAG System with Context-Knowledge Signals](https://arxiv.org/abs/2509.21875)** · arXiv · LLM · Training-free
- **📚 [LLM-based Agents Suffer from Hallucinations: A Survey of Taxonomy, Methods, and Directions](https://arxiv.org/abs/2509.18970)** · arXiv · LLM · Training-free
- **[LLM Hallucination Detection: HSAD](https://arxiv.org/abs/2509.23580)** · arXiv · LLM · Training-free
- **[LLM Hallucination Detection: A Fast Fourier Transform Method Based on Hidden Layer Temporal Signals](https://arxiv.org/abs/2509.13154)** · arXiv · LLM · Training-free
- **[LLM Enhancement with Domain Expert Mental Model to Reduce LLM Hallucination with Causal Prompt Engineering](https://arxiv.org/abs/2509.10818)** · arXiv · LLM · Training-free
- **[Knowledge-Driven Hallucination in Large Language Models: An Empirical Study on Process Modeling](https://arxiv.org/abs/2509.15336)** · arXiv · LLM · Training-free
- **[How Large Language Models are Designed to Hallucinate](https://arxiv.org/abs/2509.16297)** · arXiv · LLM · Training-free
- **[Hallucination Detection with the Internal Layers of LLMs](https://arxiv.org/abs/2509.14254)** · arXiv · LLM · Training-free
- **[HalluField: Detecting LLM Hallucinations via Field-Theoretic Modeling](https://arxiv.org/abs/2509.10753)** · arXiv · LLM · Training-free
- **[HAVE: Head-Adaptive Gating and ValuE Calibration for Hallucination Mitigation in Large Language Models](https://arxiv.org/abs/2509.06596)** · arXiv · LLM · Training-free
- **[HALT-RAG: A Task-Adaptable Framework for Hallucination Detection with Calibrated NLI Ensembles and Abstention](https://arxiv.org/abs/2509.07475)** · arXiv · LLM · Training-free
- **[Geometric Uncertainty for Detecting and Correcting Hallucinations in LLMs](https://arxiv.org/abs/2509.13813)** · arXiv · LLM · Training-free
- **[From Noise to Narrative: Tracing the Origins of Hallucinations in Transformers](https://arxiv.org/abs/2509.06938)** · arXiv · LLM · Training-free
- **[Fact Grounded Attention: Eliminating Hallucination in Large Language Models Through Attention Level Knowledge Integration](https://arxiv.org/abs/2509.25252)** · arXiv · LLM · Training-free
- **[Enhancing Financial RAG with Agentic AI and Multi-HyDE: A Novel Approach to Knowledge Retrieval and Hallucination Reduction](https://arxiv.org/abs/2509.16369)** · arXiv · LLM · Training-free
- **[Eliminating stability hallucinations in llm-based tts models via attention guidance](https://arxiv.org/abs/2509.19852)** · arXiv · LLM · Training-free
- **[DSCC-HS: A Dynamic Self-Reinforcing Framework for Hallucination Suppression in Large Language Models](https://arxiv.org/abs/2509.13702)** · arXiv · LLM · Training-free
- **[D$^2$HScore: Reasoning-Aware Hallucination Detection via Semantic Breadth and Depth Analysis in LLMs](https://arxiv.org/abs/2509.11569)** · arXiv · LLM · Training-free
- **[Black-Box Hallucination Detection via Consistency Under the Uncertain Expression](https://arxiv.org/abs/2509.21999)** · arXiv · LLM · Training-free
- **[Beyond Textual Context: Structural Graph Encoding with Adaptive Space Alignment to alleviate the hallucination of LLMs](https://arxiv.org/abs/2509.22251)** · arXiv · LLM · Training-free
- **[Beyond ROUGE: N-Gram Subspace Features for LLM Hallucination Detection](https://arxiv.org/abs/2509.05360)** · arXiv · LLM · Training-free
- **[Beyond Accuracy: Rethinking Hallucination and Regulatory Response in Generative AI](https://arxiv.org/abs/2509.13345)** · arXiv · LLM · Training-free
- **[Are Hallucinations Bad Estimations?](https://arxiv.org/abs/2509.21473)** · arXiv · LLM · Training-free
- **[A Novel Differential Feature Learning for Effective Hallucination Detection and Classification](https://arxiv.org/abs/2509.21357)** · arXiv · LLM · Training-free
- **[Fact-Controlled Diagnosis of Hallucinations in Medical Text Summarization](https://doi.org/10.21437/Interspeech.2025-537)** · INTERSPEECH 2025 · LLM · Training-free
- **[Towards Hallucination-Free Music: A Reinforcement Learning Preference Optimization Framework for Reliable Song Generation](https://arxiv.org/abs/2508.05011)** · arXiv · LLM · Training-based
- **[SEVADE: Self-Evolving Multi-Agent Analysis with Decoupled Evaluation for Hallucination-Resistant Irony Detection](https://arxiv.org/abs/2508.06803)** · arXiv · LLM · Training-free
- **[QueryBandits for Hallucination Mitigation: Exploiting Semantic Features for No-Regret Rewriting](https://arxiv.org/abs/2508.16697)** · arXiv · LLM · Training-free
- **[Prompt-Response Semantic Divergence Metrics for Faithfulness Hallucination and Misalignment Detection in Large Language Models](https://arxiv.org/abs/2508.10192)** · arXiv · LLM · Training-free
- **[Multispin Physics of AI Tipping Points and Hallucinations](https://arxiv.org/abs/2508.01097)** · arXiv · LLM · Training-free
- **[Hallucinations in medical devices](https://arxiv.org/abs/2508.14118)** · arXiv · LLM · Training-free
- **[Hallucination-Resistant Relation Extraction via Dependency-Aware Sentence Simplification and Two-tiered Hierarchical Refinement](https://arxiv.org/abs/2508.14391)** · arXiv · LLM · Training-free
- **[Hallucination vs interpretation: rethinking accuracy and precision in AI-assisted data extraction for knowledge synthesis](https://arxiv.org/abs/2508.09458)** · arXiv · LLM · Training-free
- **[Decoding Memories: An Efficient Pipeline for Self-Consistency Hallucination Detection](https://arxiv.org/abs/2508.21228)** · arXiv · LLM · Training-free
- **[Counterfactual Probing for Hallucination Detection and Mitigation in Large Language Models](https://arxiv.org/abs/2508.01862)** · arXiv · LLM · Training-free
- **[An Investigation on Group Query Hallucination Attacks](https://arxiv.org/abs/2508.19321)** · arXiv · LLM · Training-free
- **[Addressing accuracy and hallucination of LLMs in Alzheimer's disease research through knowledge graphs](https://arxiv.org/abs/2508.21238)** · arXiv · LLM · Training-free
- **📚 [A comprehensive taxonomy of hallucinations in Large Language Models](https://arxiv.org/abs/2508.01781)** · arXiv · LLM · Training-free
- **[Toward Reliable Scientific Hypothesis Generation: Evaluating Truthfulness and Hallucination in Large Language Models](https://doi.org/10.24963/ijcai.2025/873)** · IJCAI 2025 · LLM · Training-free
- **[Detecting Hallucination in Large Language Models Through Deep Internal Representation Analysis](https://doi.org/10.24963/ijcai.2025/929)** · IJCAI 2025 · LLM · Training-free
- **[Using multi-agent architecture to mitigate the risk of LLM hallucinations](https://arxiv.org/abs/2507.01446)** · arXiv · LLM · Training-free
- **[Theoretical Foundations and Mitigation of Hallucination in Large Language Models](https://arxiv.org/abs/2507.22915)** · arXiv · LLM · Training-free
- **[Reducing Hallucinations in Summarization via Reinforcement Learning with Entity Hallucination Index](https://arxiv.org/abs/2507.22744)** · arXiv · LLM · Training-based
- **[RODS: Robust Optimization Inspired Diffusion Sampling for Detecting and Reducing Hallucination in Generative Models](https://arxiv.org/abs/2507.12201)** · arXiv · LLM · Training-free
- **📋 [MIRAGE-Bench: LLM Agent is Hallucinating and Where to Find Them](https://arxiv.org/abs/2507.21017)** · arXiv · LLM · Training-free
- **[Investigating Hallucination in Conversations for Low Resource Languages](https://arxiv.org/abs/2507.22720)** · arXiv · LLM · Training-free
- **[Hallucination Stations: On Some Basic Limitations of Transformer-Based Language Models](https://arxiv.org/abs/2507.07505)** · arXiv · LLM · Training-free
- **[Hallucinating 360°: Panoramic Street-View Generation via Local Scenes Diffusion and Probabilistic Prompting](https://arxiv.org/abs/2507.06971)** · arXiv · LLM · Training-free
- **[First Hallucination Tokens Are Different from Conditional Ones](https://arxiv.org/abs/2507.20836)** · arXiv · LLM · Training-free
- **[FRED: Financial Retrieval-Enhanced Detection and Editing of Hallucinations in Language Models](https://arxiv.org/abs/2507.20930)** · arXiv · LLM · Training-free
- **[Energy-Guided Decoding for Object Hallucination Mitigation](https://arxiv.org/abs/2507.07731)** · arXiv · LLM · Training-free
- **[Detecting Token-Level Hallucinations Using Variance Signals: A Reference-Free Approach](https://arxiv.org/abs/2507.04137)** · arXiv · LLM · Training-free
- **[AutoRAG-LoRA: Hallucination-Triggered Knowledge Retuning via Lightweight Adapters](https://arxiv.org/abs/2507.10586)** · arXiv · LLM · Training-based
- **[Trustworthy Information Retrieval in the LLM Era: Bias, Unfairness, and Hallucination](https://doi.org/10.1145/3767695.3769670)** · SIGIR-AP 2025 · LLM · Training-free
- **📋 [TreeCut: A Synthetic Unanswerable Math Word Problem Dataset for LLM Hallucination Evaluation](https://doi.org/10.18653/v1/2025.acl-short.84)** · ACL 2025 · LLM · Training-free
- **[Think More, Hallucinate Less: Mitigating Hallucinations via Dual Process of Fast and Slow Thinking](https://doi.org/10.18653/v1/2025.findings-acl.417)** · ACL 2025 · LLM · Training-free
- **[The Law of Knowledge Overshadowing: Towards Understanding, Predicting and Preventing LLM Hallucination](https://doi.org/10.18653/v1/2025.findings-acl.1199)** · ACL 2025 · LLM · Training-free
- **[Stochastic Chameleons: Irrelevant Context Hallucinations Reveal Class-Based (Mis)Generalization in LLMs](https://doi.org/10.18653/v1/2025.acl-long.1458)** · ACL 2025 · LLM · Training-free
- **[Steer LLM Latents for Hallucination Detection](https://proceedings.mlr.press/v267/park25a.html)** · ICML 2025 · LLM · Training-free
- **[SHARP: Unlocking Interactive Hallucination via Stance Transfer in Role-Playing LLMs](https://arxiv.org/abs/2411.07965)** · ACL 2025 · LLM · Training-free
- **[Rowen: Adaptive Retrieval-Augmented Generation for Hallucination Mitigation in LLMs](https://doi.org/10.1145/3767695.3769500)** · SIGIR-AP 2025 · LLM · Training-free
- **[Removal of Hallucination on Hallucination: Debate-Augmented RAG](https://doi.org/10.18653/v1/2025.acl-long.770)** · ACL 2025 · LLM · Training-free
- **[Rejecting Hallucinated State Targets during Planning](https://proceedings.mlr.press/v267/zhao25t.html)** · ICML 2025 · LLM · Training-free
- **[Reducing Tool Hallucination via Reliability Alignment](https://proceedings.mlr.press/v267/xu25ap.html)** · ICML 2025 · LLM · Training-free
- **[RARR Unraveled: Component-Level Insights into Hallucination Detection and Mitigation](https://doi.org/10.1145/3726302.3730337)** · SIGIR 2025 · LLM · Training-free
- **[Prompt-Guided Internal States for Hallucination Detection of Large Language Models](https://doi.org/10.18653/v1/2025.acl-long.1058)** · ACL 2025 · LLM · Training-free
- **[On-Policy Self-Alignment with Fine-grained Knowledge Feedback for Hallucination Mitigation](https://doi.org/10.18653/v1/2025.findings-acl.271)** · ACL 2025 · LLM · Training-free
- **[Monitoring Decoding: Mitigating Hallucination via Evaluating the Factuality of Partial Response during Generation](https://doi.org/10.18653/v1/2025.findings-acl.752)** · ACL 2025 · LLM · Training-free
- **[Long-form Hallucination Detection with Self-elicitation](https://doi.org/10.18653/v1/2025.findings-acl.211)** · ACL 2025 · LLM · Training-free
- **[Learning Auxiliary Tasks Improves Reference-Free Hallucination Detection in Open-Domain Long-Form Generation](https://doi.org/10.18653/v1/2025.acl-short.93)** · ACL 2025 · LLM · Training-free
- **[ICR Probe: Tracking Hidden State Dynamics for Reliable Hallucination Detection in LLMs](https://doi.org/10.18653/v1/2025.acl-long.880)** · ACL 2025 · LLM · Training-free
- **[Hallucination Detox: Sensitivity Dropout (SenD) for Large Language Model Training](https://doi.org/10.18653/v1/2025.acl-long.276)** · ACL 2025 · LLM · Training-free
- **📋 [HalluLens: LLM Hallucination Benchmark](https://doi.org/10.18653/v1/2025.acl-long.1176)** · ACL 2025 · LLM · Training-free
- **[HICD: Hallucination-Inducing via Attention Dispersion for Contrastive Decoding to Mitigate Hallucinations in Large Language Models](https://doi.org/10.18653/v1/2025.findings-acl.405)** · ACL 2025 · LLM · Training-free
- **[HD-NDEs: Neural Differential Equations for Hallucination Detection in LLMs](https://doi.org/10.18653/v1/2025.acl-long.309)** · ACL 2025 · LLM · Training-free
- **[HALoGEN: Fantastic LLM Hallucinations and Where to Find Them](https://doi.org/10.18653/v1/2025.acl-long.71)** · ACL 2025 · LLM · Training-free
- **[Explainable Hallucination through Natural Language Inference Mapping](https://doi.org/10.18653/v1/2025.findings-acl.96)** · ACL 2025 · LLM · Training-free
- **[Evaluating LLMs’ Assessment of Mixed-Context Hallucination Through the Lens of Summarization](https://doi.org/10.18653/v1/2025.findings-acl.847)** · ACL 2025 · LLM · Training-free
- **[ETF: An Entity Tracing Framework for Hallucination Detection in Code Summaries](https://doi.org/10.18653/v1/2025.acl-long.1480)** · ACL 2025 · LLM · Training-free
- **[Dynamic Attention-Guided Context Decoding for Mitigating Context Faithfulness Hallucinations in Large Language Models](https://doi.org/10.18653/v1/2025.findings-acl.269)** · ACL 2025 · LLM · Training-free
- **[Do Robot Snakes Dream like Electric Sheep? Investigating the Effects of Architectural Inductive Biases on Hallucination](https://doi.org/10.18653/v1/2025.findings-acl.60)** · ACL 2025 · LLM · Training-free
- **[DRAG: Distilling RAG for SLMs from LLMs to Transfer Knowledge and Mitigate Hallucination via Evidence and Graph-based Distillation](https://doi.org/10.18653/v1/2025.acl-long.358)** · ACL 2025 · LLM · Training-free
- **📋 [CCHall: A Novel Benchmark for Joint Cross-Lingual and Cross-Modal Hallucinations Detection in Large Language Models](https://doi.org/10.18653/v1/2025.acl-long.1485)** · ACL 2025 · LLM · Training-free
- **[Beyond Facts: Evaluating Intent Hallucination in Large Language Models](https://doi.org/10.18653/v1/2025.acl-long.349)** · ACL 2025 · LLM · Training-free
- **[Alleviating LLM-based Generative Retrieval Hallucination in Alipay Search](https://doi.org/10.1145/3726302.3731951)** · SIGIR 2025 · LLM · Training-free
- **[Alleviating Hallucinations from Knowledge Misalignment in Large Language Models via Selective Abstention Learning](https://doi.org/10.18653/v1/2025.acl-long.1199)** · ACL 2025 · LLM · Training-free
- **[Aligning Large Language Models to Follow Instructions and Hallucinate Less via Effective Data Filtering](https://doi.org/10.18653/v1/2025.acl-long.804)** · ACL 2025 · LLM · Training-free
- **[Addressing Hallucination in Causal Q&amp;A: The Efficacy of Fine-tuning over Prompting in LLMs](https://aclanthology.org/2025.finnlp-1.27/)** · ACL 2025 · LLM · Training-based
- **[&quot;Not Aligned&quot; is Not &quot;Malicious&quot;: Being Careful about Hallucinations of Large Language Models&apos; Jailbreak](https://aclanthology.org/2025.coling-main.146/)** · ACL 2025 · LLM · Training-free
- **[Trustworthy AI for Medicine: Continuous Hallucination Detection and Elimination with CHECK](https://arxiv.org/abs/2506.11129)** · arXiv · LLM · Training-free
- **[The impact of fine tuning in LLaMA on hallucinations for named entity extraction in legal documentation](https://arxiv.org/abs/2506.08827)** · arXiv · LLM · Training-free
- **[Shaking to Reveal: Perturbation-Based Detection of LLM Hallucinations](https://arxiv.org/abs/2506.02696)** · arXiv · LLM · Training-free
- **[Probabilistic distances-based hallucination detection in LLMs with RAG](https://arxiv.org/abs/2506.09886)** · arXiv · LLM · Training-free
- **[On the Fundamental Impossibility of Hallucination Control in Large Language Models](https://arxiv.org/abs/2506.06382)** · arXiv · LLM · Training-free
- **[Mitigating Object Hallucination via Robust Local Perception Search](https://arxiv.org/abs/2506.06729)** · arXiv · LLM · Training-free
- **[MMD-Flagger: Leveraging Maximum Mean Discrepancy to Detect Hallucinations](https://arxiv.org/abs/2506.01367)** · arXiv · LLM · Training-free
- **[MALM: A Multi-Information Adapter for Large Language Models to Mitigate Hallucination](https://arxiv.org/abs/2506.12483)** · arXiv · LLM · Training-free
- **[HIDE and Seek: Detecting Hallucinations in Language Models via Decoupled Representations](https://arxiv.org/abs/2506.17748)** · arXiv · LLM · Training-free
- **[GOLFer: Smaller LM-Generated Documents Hallucination Filter & Combiner for Query Expansion in Information Retrieval](https://arxiv.org/abs/2506.04762)** · arXiv · LLM · Training-free
- **[Eliminating Hallucination-Induced Errors in LLM Code Generation with Functional Clustering](https://arxiv.org/abs/2506.11021)** · arXiv · LLM · Training-free
- **[Correcting Hallucinations in News Summaries: Exploration of Self-Correcting LLM Methods with External Knowledge](https://arxiv.org/abs/2506.19607)** · arXiv · LLM · Training-free
- **[CLATTER: Comprehensive Entailment Reasoning for Hallucination Detection](https://arxiv.org/abs/2506.05243)** · arXiv · LLM · Training-free
- **[Ask a Local: Detecting Hallucinations With Specialized Model Divergence](https://arxiv.org/abs/2506.03357)** · arXiv · LLM · Training-free
- **[Unfamiliar Finetuning Examples Control How Language Models Hallucinate](https://doi.org/10.18653/v1/2025.naacl-long.183)** · NAACL 2025 · LLM · Training-free
- **[Towards Long Context Hallucination Detection](https://doi.org/10.18653/v1/2025.findings-naacl.436)** · NAACL 2025 · LLM · Training-free
- **[On A Scale From 1 to 5: Quantifying Hallucination in Faithfulness Evaluation](https://doi.org/10.18653/v1/2025.findings-naacl.433)** · NAACL 2025 · LLM · Training-free
- **[Octopus: Alleviating Hallucination via Dynamic Contrastive Decoding](https://openaccess.thecvf.com/content/CVPR2025/html/Suo_Octopus_Alleviating_Hallucination_via_Dynamic_Contrastive_Decoding_CVPR_2025_paper.html)** · CVPR 2025 · LLM · Training-free
- **[Not all Hallucinations are Good to Throw Away When it Comes to Legal Abstractive Summarization](https://doi.org/10.18653/v1/2025.naacl-long.275)** · NAACL 2025 · LLM · Training-free
- **[Mitigating Hallucinated Translations in Large Language Models with Hallucination-focused Preference Optimization](https://doi.org/10.18653/v1/2025.naacl-long.175)** · NAACL 2025 · LLM · Training-based
- **[Investigating Hallucinations in Simultaneous Machine Translation: Knowledge Distillation Solution and Components Analysis](https://doi.org/10.18653/v1/2025.naacl-long.364)** · NAACL 2025 · LLM · Training-free
- **[Improve Decoding Factuality by Token-wise Cross Layer Entropy of Large Language Models](https://doi.org/10.18653/v1/2025.findings-naacl.217)** · NAACL 2025 · LLM · Training-free
- **📋 [How LLMs React to Industrial Spatio-Temporal Data? Assessing Hallucination with a Novel Traffic Incident Benchmark Dataset](https://doi.org/10.18653/v1/2025.naacl-industry.4)** · NAACL 2025 · LLM · Training-free
- **[HALLUCANA: Fixing LLM Hallucination with A Canary Lookahead](https://doi.org/10.18653/v1/2025.findings-naacl.12)** · NAACL 2025 · LLM · Training-free
- **[Gradient-guided Attention Map Editing: Towards Efficient Contextual Hallucination Mitigation](https://doi.org/10.18653/v1/2025.findings-naacl.458)** · NAACL 2025 · LLM · Training-free
- **[GRAIT: Gradient-Driven Refusal-Aware Instruction Tuning for Effective Hallucination Mitigation](https://doi.org/10.18653/v1/2025.findings-naacl.223)** · NAACL 2025 · LLM · Training-based
- **[From Single to Multi: How LLMs Hallucinate in Multi-Document Summarization](https://doi.org/10.18653/v1/2025.findings-naacl.293)** · NAACL 2025 · LLM · Training-free
- **📋 [FaithBench: A Diverse Hallucination Benchmark for Summarization by Modern LLMs](https://doi.org/10.18653/v1/2025.naacl-short.38)** · NAACL 2025 · LLM · Training-free
- **[FactCheXcker: Mitigating Measurement Hallucinations in Chest X-ray Report Generation Models](https://openaccess.thecvf.com/content/CVPR2025/html/Heiman_FactCheXcker_Mitigating_Measurement_Hallucinations_in_Chest_X-ray_Report_Generation_Models_CVPR_2025_paper.html)** · CVPR 2025 · LLM · Training-free
- **[Developing a Reliable, Fast, General-Purpose Hallucination Detection and Mitigation Service](https://doi.org/10.18653/v1/2025.naacl-industry.72)** · NAACL 2025 · LLM · Training-free
- **[Alleviating Hallucinations of Large Language Models through Induced Hallucinations](https://doi.org/10.18653/v1/2025.findings-naacl.459)** · NAACL 2025 · LLM · Training-free
- **[A Probabilistic Framework for LLM Hallucination Detection via Belief Tree Propagation](https://doi.org/10.18653/v1/2025.naacl-long.158)** · NAACL 2025 · LLM · Training-free
- **[VeriTrail: Closed-Domain Hallucination Detection with Traceability](https://arxiv.org/abs/2505.21786)** · arXiv · LLM · Training-free
- **[Triggering Hallucinations in LLMs: A Quantitative Study of Prompt-Induced Hallucination in Large Language Models](https://arxiv.org/abs/2505.00557)** · arXiv · LLM · Training-free
- **[Teaching with Lies: Curriculum DPO on Synthetic Negatives for Hallucination Detection](https://arxiv.org/abs/2505.17558)** · arXiv · LLM · Training-based
- **[Seeing It or Not? Interpretable Vision-aware Latent Steering to Mitigate Object Hallucinations](https://arxiv.org/abs/2505.17812)** · arXiv · LLM · Training-free
- **[SEReDeEP: Hallucination Detection in Retrieval-Augmented Models via Semantic Entropy and Context-Parameter Fusion](https://arxiv.org/abs/2505.07528)** · arXiv · LLM · Training-free
- **[Reasoning Large Language Model Errors Arise from Hallucinating Critical Problem Features](https://arxiv.org/abs/2505.12151)** · arXiv · LLM · Training-free
- **[RePPL: Recalibrating Perplexity by Uncertainty in Semantic Propagation and Language Generation for Explainable QA Hallucination Detection](https://arxiv.org/abs/2505.15386)** · arXiv · LLM · Training-free
- **[Osiris: A Lightweight Open-Source Hallucination Detection System](https://arxiv.org/abs/2505.04844)** · arXiv · LLM · Training-free
- **📋 [MultiHal: Multilingual Dataset for Knowledge-Graph Grounded Evaluation of LLM Hallucinations](https://arxiv.org/abs/2505.14101)** · arXiv · LLM · Training-free
- **[Mitigating Hallucination in VideoLLMs via Temporal-Aware Activation Engineering](https://arxiv.org/abs/2505.12826)** · arXiv · LLM · Training-free
- **[Hallucinate at the Last in Long Response Generation: A Case Study on Long Document Summarization](https://arxiv.org/abs/2505.15291)** · arXiv · LLM · Training-free
- **📋 [HalluMix: A Task-Agnostic, Multi-Domain Benchmark for Real-World Hallucination Detection](https://arxiv.org/abs/2505.00506)** · arXiv · LLM · Training-free
- **[From Hallucinations to Jailbreaks: Rethinking the Vulnerability of Large Foundation Models](https://arxiv.org/abs/2505.24232)** · arXiv · LLM · Training-free
- **[Finetune-RAG: Fine-Tuning Language Models to Resist Hallucination in Retrieval-Augmented Generation](https://arxiv.org/abs/2505.10792)** · arXiv · LLM · Training-free
- **[Evaluation Hallucination in Multi-Round Incomplete Information Lateral-Driven Reasoning Tasks](https://arxiv.org/abs/2505.23843)** · arXiv · LLM · Training-free
- **[Detection and Mitigation of Hallucination in Large Reasoning Models: A Mechanistic Perspective](https://arxiv.org/abs/2505.12886)** · arXiv · LLM · Training-free
- **[Critique Before Thinking: Mitigating Hallucination through Rationale-Augmented Instruction Tuning](https://arxiv.org/abs/2505.07172)** · arXiv · LLM · Training-based
- **[Are Reasoning Models More Prone to Hallucination?](https://arxiv.org/abs/2505.23646)** · arXiv · LLM · Training-free
- **[Why and How LLMs Hallucinate: Connecting the Dots with Subsequence Associations](https://arxiv.org/abs/2504.12691)** · arXiv · LLM · Training-free
- **[Synthetic Fluency: Hallucinations, Confabulations, and the Creation of Irish Words in LLM-Generated Translations](https://arxiv.org/abs/2504.07680)** · arXiv · LLM · Training-free
- **[Span-Level Hallucination Detection for LLM-Generated Answers](https://arxiv.org/abs/2504.18639)** · arXiv · LLM · Training-free
- **[Purposefully Induced Psychosis (PIP): Embracing Hallucination as Imagination in Large Language Models](https://arxiv.org/abs/2504.12012)** · arXiv · LLM · Training-free
- **[Noise Augmented Fine Tuning for Mitigating Hallucinations in Large Language Models](https://arxiv.org/abs/2504.03302)** · arXiv · LLM · Training-free
- **[Mitigating LLM Hallucinations with Knowledge Graphs: A Case Study](https://arxiv.org/abs/2504.12422)** · arXiv · LLM · Training-free
- **📋 [MedHal: An Evaluation Dataset for Medical Hallucination Detection](https://arxiv.org/abs/2504.08596)** · arXiv · LLM · Training-free
- **[LLM Enhancer: Merged Approach using Vector Embedding for Reducing Large Language Model Hallucinations with External Knowledge](https://arxiv.org/abs/2504.21132)** · arXiv · LLM · Training-free
- **[Hyper-RAG: Combating LLM Hallucinations using Hypergraph-Driven Retrieval-Augmented Generation](https://arxiv.org/abs/2504.08758)** · arXiv · LLM · Training-free
- **[Hybrid Retrieval for Hallucination Mitigation in Large Language Models: A Comparative Analysis](https://arxiv.org/abs/2504.05324)** · arXiv · LLM · Training-free
- **📋 [How to Detect and Defeat Molecular Mirage: A Metric-Driven Benchmark for Hallucination in LLM-based Molecular Comprehension](https://arxiv.org/abs/2504.12314)** · arXiv · LLM · Training-free
- **[Hallucinations and Key Information Extraction in Medical Texts: A Comprehensive Assessment of Open-Source Large Language Models](https://arxiv.org/abs/2504.19061)** · arXiv · LLM · Training-free
- **[Hallucination, reliability, and the role of generative AI in science](https://arxiv.org/abs/2504.08526)** · arXiv · LLM · Training-free
- **[Hallucination by Code Generation LLMs: Taxonomy, Benchmarks, Mitigation, and Challenges](https://arxiv.org/abs/2504.20799)** · arXiv · LLM · Training-free
- **[Hallucinated Span Detection with Multi-View Attention Features](https://arxiv.org/abs/2504.04335)** · arXiv · LLM · Training-free
- **[HalluciNot: Hallucination Detection Through Context and Common Knowledge Verification](https://arxiv.org/abs/2504.07069)** · arXiv · LLM · Training-free
- **[Enhancing Mathematical Reasoning in Large Language Models with Self-Consistency-Based Hallucination Detection](https://arxiv.org/abs/2504.09440)** · arXiv · LLM · Training-free
- **[DataPuzzle: Breaking Free from the Hallucinated Promise of LLMs in Data Analysis](https://arxiv.org/abs/2504.10036)** · arXiv · LLM · Training-free
- **[Capturing AI's Attention: Physics of Repetition, Hallucination, Bias and Beyond](https://arxiv.org/abs/2504.04600)** · arXiv · LLM · Training-free
- **[Can LLMs Detect Intrinsic Hallucinations in Paraphrasing and Machine Translation?](https://arxiv.org/abs/2504.20699)** · arXiv · LLM · Training-free
- **[Beyond Misinformation: A Conceptual Framework for Studying AI Hallucinations in (Science) Communication](https://arxiv.org/abs/2504.13777)** · arXiv · LLM · Training-free
- **[A Unified Virtual Mixture-of-Experts Framework:Enhanced Inference and Hallucination Mitigation in Single-Model System](https://arxiv.org/abs/2504.03739)** · arXiv · LLM · Training-free
- **[(Im)possibility of Automated Hallucination Detection in Large Language Models](https://arxiv.org/abs/2504.17004)** · arXiv · LLM · Training-free
- **[Towards Understanding Text Hallucination of Diffusion Models via Local Generation Bias](https://openreview.net/forum?id=SKW10XJlAI)** · ICLR 2025 · LLM · Training-free
- **[Towards Detecting LLMs Hallucination via Markov Chain-based Multi-agent Debate Framework](https://doi.org/10.1109/ICASSP49660.2025.10889448)** · ICASSP 2025 · LLM · Training-free
- **[SSCM: Self-Supervised Critical Model for Reducing Hallucinations in Chinese Financial Text Generation](https://doi.org/10.1109/ICASSP49660.2025.10887684)** · ICASSP 2025 · LLM · Training-free
- **[ReDeEP: Detecting Hallucination in Retrieval-Augmented Generation via Mechanistic Interpretability](https://openreview.net/forum?id=ztzZDzgfrh)** · ICLR 2025 · LLM · Training-free
- **[NoVo: Norm Voting off Hallucinations with Attention Heads in Large Language Models](https://openreview.net/forum?id=yaOe2xBcLC)** · ICLR 2025 · LLM · Training-free
- **[No Free Lunch: Fundamental Limits of Learning Non-Hallucinating Generative Models](https://arxiv.org/abs/2410.19217)** · ICLR 2025 · LLM · Training-free
- **[MixHD: A Method for Detecting Hallucinations Based on the Internal State and Output Probability of Large Language Models](https://doi.org/10.1109/ICASSP49660.2025.10889328)** · ICASSP 2025 · LLM · Training-free
- **[LLMs Know More Than They Show: On the Intrinsic Representation of LLM Hallucinations](https://openreview.net/forum?id=KRnsX5Em3W)** · ICLR 2025 · LLM · Training-free
- **📋 [K-HALU: Multiple Answer Korean Hallucination Benchmark for Large Language Models](https://openreview.net/forum?id=VnLhUogHYE)** · ICLR 2025 · LLM · Training-free
- **[Hallucination Detection and Mitigation in Large Language Models](https://openreview.net/forum?id=VwOYxPScxB)** · ICLR 2025 · LLM · Training-free
- **[HaDeMiF: Hallucination Detection and Mitigation in Large Language Models](https://openreview.net/forum?id=VwOYxPScxB)** · ICLR 2025 · LLM · Training-free
- **[Do I Know This Entity? Knowledge Awareness and Hallucinations in Language Models](https://openreview.net/forum?id=WCRQFlji2q)** · ICLR 2025 · LLM · Training-free
- **[CoMT: Chain-of-Medical-Thought Reduces Hallucination in Medical Report Generation](https://doi.org/10.1109/ICASSP49660.2025.10887699)** · ICASSP 2025 · LLM · Training-free
- **[Can Knowledge Editing Really Correct Hallucinations?](https://openreview.net/forum?id=hmDt068MoZ)** · ICLR 2025 · LLM · Training-based
- **[A Weighted Cross-entropy Loss for Mitigating LLM Hallucinations in Cross-lingual Continual Pretraining](https://doi.org/10.1109/ICASSP49660.2025.10888877)** · ICASSP 2025 · LLM · Training-free
- **[Shakespearean Sparks: The Dance of Hallucination and Creativity in LLMs' Decoding Layers](https://arxiv.org/abs/2503.02851)** · arXiv · LLM · Training-free
- **[ShED-HD: A Shannon Entropy Distribution Framework for Lightweight Hallucination Detection on Edge Devices](https://arxiv.org/abs/2503.18242)** · arXiv · LLM · Training-free
- **[RAG-KG-IL: A Multi-Agent Hybrid Framework for Reducing Hallucinations and Enhancing LLM Reasoning through RAG and Incremental Knowledge Graph Learning Integration](https://arxiv.org/abs/2503.13514)** · arXiv · LLM · Training-free
- **📋 [Poly-FEVER: A Multilingual Fact Verification Benchmark for Hallucination Detection in Large Language Models](https://arxiv.org/abs/2503.16541)** · arXiv · LLM · Training-free
- **📋 [OAEI-LLM-T: A TBox Benchmark Dataset for Understanding Large Language Model Hallucinations in Ontology Matching](https://arxiv.org/abs/2503.21813)** · arXiv · LLM · Training-free
- **[Medical Hallucinations in Foundation Models and Their Impact on Healthcare](https://arxiv.org/abs/2503.05777)** · arXiv · LLM · Training-free
- **[KSHSeek: Data-Driven Approaches to Mitigating and Detecting Knowledge-Shortcut Hallucinations in Generative Models](https://arxiv.org/abs/2503.19482)** · arXiv · LLM · Training-free
- **[How do language models learn facts? Dynamics, curricula and hallucinations](https://arxiv.org/abs/2503.21676)** · arXiv · LLM · Training-free
- **📋 [HalluVerse25: Fine-grained Multilingual Benchmark Dataset for LLM Hallucinations](https://arxiv.org/abs/2503.07833)** · arXiv · LLM · Training-free
- **[HDLCoRe: A Training-Free Framework for Mitigating Hallucinations in LLM-Generated HDL](https://arxiv.org/abs/2503.16528)** · arXiv · LLM · Training-free
- **[Guarding against artificial intelligence--hallucinated citations: the case for full-text reference deposit](https://arxiv.org/abs/2503.19848)** · arXiv · LLM · Training-free
- **[Graph-Grounded LLMs: Leveraging Graphical Function Calling to Minimize LLM Hallucinations](https://arxiv.org/abs/2503.10941)** · arXiv · LLM · Training-free
- **[From "Hallucination" to "Suture": Insights from Language Philosophy to Enhance Large Language Models](https://arxiv.org/abs/2503.14392)** · arXiv · LLM · Training-free
- **[Do Chains-of-Thoughts of Large Language Models Suffer from Hallucinations, Cognitive Biases, or Phobias in Bayesian Reasoning?](https://arxiv.org/abs/2503.15268)** · arXiv · LLM · Training-free
- **[`Generalization is hallucination' through the lens of tensor completions](https://arxiv.org/abs/2502.17305)** · arXiv · LLM · Training-free
- **[Winning Big with Small Models: Knowledge Distillation vs. Self-Training for Reducing Hallucination in Product QA Agents](https://arxiv.org/abs/2502.19545)** · arXiv · LLM · Training-free
- **[What are Models Thinking about? Understanding Large Language Model Hallucinations "Psychology" through Model Inner State Analysis](https://arxiv.org/abs/2502.13490)** · arXiv · LLM · Training-free
- **[Valuable Hallucinations: Realizable Non-realistic Propositions](https://arxiv.org/abs/2502.11113)** · arXiv · LLM · Training-free
- **[Smoothing Out Hallucinations: Mitigating LLM Hallucination with Smoothed Knowledge Distillation](https://arxiv.org/abs/2502.11306)** · arXiv · LLM · Training-free
- **[Mitigating Hallucinations in Diffusion Models through Adaptive Attention Modulation](https://arxiv.org/abs/2502.16872)** · arXiv · LLM · Training-free
- **[MIH-TCCT: Mitigating Inconsistent Hallucinations in LLMs via Event-Driven Text-Code Cyclic Training](https://arxiv.org/abs/2502.08904)** · arXiv · LLM · Training-free
- **[Linear Correlation in LM's Compositional Generalization and Hallucination](https://arxiv.org/abs/2502.04520)** · arXiv · LLM · Training-free
- **[LettuceDetect: A Hallucination Detection Framework for RAG Applications](https://arxiv.org/abs/2502.17125)** · arXiv · LLM · Training-free
- **[HuDEx: Integrating Hallucination Detection and Explainability for Enhancing the Reliability of LLM responses](https://arxiv.org/abs/2502.08109)** · arXiv · LLM · Training-free
- **[Hallucinations are inevitable but can be made statistically negligible](https://arxiv.org/abs/2502.12187)** · arXiv · LLM · Training-free
- **[Hallucinations and Truth: A Comprehensive Accuracy Evaluation of RAG, LoRA and DoRA](https://arxiv.org/abs/2502.10497)** · arXiv · LLM · Training-based
- **[Hallucination, Monofacts, and Miscalibration: An Empirical Investigation](https://arxiv.org/abs/2502.08666)** · arXiv · LLM · Training-free
- **[Hallucination Detection: A Probabilistic Framework Using Embeddings Distance Analysis](https://arxiv.org/abs/2502.08663)** · arXiv · LLM · Training-free
- **[FilterRAG: Zero-Shot Informed Retrieval-Augmented Generation to Mitigate Hallucinations in VQA](https://arxiv.org/abs/2502.18536)** · arXiv · LLM · Training-free
- **[Enhancing Hallucination Detection through Noise Injection](https://arxiv.org/abs/2502.03799)** · arXiv · LLM · Training-free
- **[Detecting LLM Fact-conflicting Hallucinations Enhanced by Temporal-logic-based Reasoning](https://arxiv.org/abs/2502.13416)** · arXiv · LLM · Training-free
- **[Delta -- Contrastive Decoding Mitigates Text Hallucinations in Large Language Models](https://arxiv.org/abs/2502.05825)** · arXiv · LLM · Training-free
- **📋 [Bi'an: A Bilingual Benchmark and Model for Hallucination Detection in Retrieval-Augmented Generation](https://arxiv.org/abs/2502.19209)** · arXiv · LLM · Training-free
- **[Zero-resource Hallucination Detection for Text Generation via Graph-based Contextual Knowledge Triples Modeling](https://doi.org/10.1609/aaai.v39i22.34559)** · AAAI 2025 · LLM · Training-free
- **[ReXTrust: A Model for Fine-Grained Hallucination Detection in AI-Generated Radiology Reports](https://proceedings.mlr.press/v281/hardy25a.html)** · AAAI Bridge Program 2025 · LLM · Training-free
- **[RaDIO: Real-Time Hallucination Detection with Contextual Index Optimized Query Formulation for Dynamic Retrieval Augmented Generation](https://doi.org/10.1609/aaai.v39i24.34809)** · AAAI 2025 · LLM · Training-free
- **📋 [MedHallBench: A New Benchmark for Assessing Hallucination in Medical Large Language Models](https://proceedings.mlr.press/v281/zuo25b.html)** · AAAI Bridge Program 2025 · LLM · Training-free
- **📋 [MHBench: Demystifying Motion Hallucination in VideoLLMs](https://doi.org/10.1609/aaai.v39i4.32463)** · AAAI 2025 · LLM · Training-free
- **[Is LLMs Hallucination Usable? LLM-based Negative Reasoning for Fake News Detection](https://doi.org/10.1609/aaai.v39i1.32089)** · AAAI 2025 · LLM · Training-free
- **[G2LDetect: A Global-to-Local Approach for Hallucination Detection](https://doi.org/10.1609/aaai.v39i1.31985)** · AAAI 2025 · LLM · Training-free
- **[Enhancing Uncertainty Modeling with Semantic Graph for Hallucination Detection](https://doi.org/10.1609/aaai.v39i22.34528)** · AAAI 2025 · LLM · Training-free
- **📋 [CodeHalu: Investigating Code Hallucinations in LLMs via Execution-based Verification](https://doi.org/10.1609/aaai.v39i24.34717)** · AAAI 2025 · LLM · Training-free
- **[Attributive Reasoning for Hallucination Diagnosis of Large Language Models](https://doi.org/10.1609/aaai.v39i22.34536)** · AAAI 2025 · LLM · Training-free
- **[Question-to-Question Retrieval for Hallucination-Free Knowledge Access: An Approach for Wikipedia and Wikidata Question Answering](https://arxiv.org/abs/2501.11301)** · arXiv · LLM · Training-free
- **[Prompt-Based Monte Carlo Tree Search for Mitigating Hallucinations in Large Models](https://arxiv.org/abs/2501.13942)** · arXiv · LLM · Training-free
- **[OnionEval: An Unified Evaluation of Fact-conflicting Hallucination for Small-Large Language Models](https://arxiv.org/abs/2501.12975)** · arXiv · LLM · Training-free
- **[Importing Phantoms: Measuring LLM Package Hallucination Vulnerabilities](https://arxiv.org/abs/2501.19012)** · arXiv · LLM · Training-free
- **[Hallucination Mitigation using Agentic AI Natural Language-Based Frameworks](https://arxiv.org/abs/2501.13946)** · arXiv · LLM · Training-free
- **[Can Hallucinations Help? Boosting LLMs for Drug Discovery](https://arxiv.org/abs/2501.13824)** · arXiv · LLM · Training-free
- **[Trucidator: Document-level Event Factuality Identification via Hallucination Enhancement and Cross-Document Inference](https://aclanthology.org/2025.coling-main.139/)** · COLING 2025 · LLM · Training-free
- **[Synthetic Paths to Integral Truth: Mitigating Hallucinations Caused by Confirmation Bias with Synthetic Data](https://aclanthology.org/2025.coling-main.347/)** · COLING 2025 · LLM · Training-free
- **[RoleBreak: Character Hallucination as a Jailbreak Attack in Role-Playing Systems](https://aclanthology.org/2025.coling-main.494/)** · COLING 2025 · LLM · Training-free
- **[On Reducing Factual Hallucinations in Graph-to-Text Generation Using Large Language Models](https://aclanthology.org/2025.genaik-1.5/)** · COLING Workshops 2025 · LLM · Training-free
- **[Luna: A Lightweight Evaluation Model to Catch Language Model Hallucinations with High Accuracy and Low Cost](https://aclanthology.org/2025.coling-industry.34/)** · COLING 2025 · LLM · Training-based
- **📋 [KG-FPQ: Evaluating Factuality Hallucination in LLMs with Knowledge Graph-based False Premise Questions](https://aclanthology.org/2025.coling-main.698/)** · COLING 2025 · LLM · Training-free
- **[Hermit Kingdom Through the Lens of Multiple Perspectives: A Case Study of LLM Hallucination on North Korea](https://aclanthology.org/2025.coling-main.226/)** · COLING 2025 · LLM · Training-free
- **[GraphRAG: Leveraging Graph-Based Efficiency to Minimize Hallucinations in LLM-Driven RAG for Finance Data](https://aclanthology.org/2025.genaik-1.6/)** · COLING Workshops 2025 · LLM · Training-free
- **[Counterfactual Debating with Preset Stances for Hallucination Elimination of LLMs](https://aclanthology.org/2025.coling-main.703/)** · COLING 2025 · LLM · Training-free
- **[Counterfactual Segmentation Reasoning: Diagnosing and Mitigating Pixel-Grounding Hallucination]()** · Unlabeled · LLM · Training-free
- **[Copy-Paste to Mitigate Large Language Model Hallucinations]()** · Unlabeled · LLM · Training-free
- **[Benford&apos;s Curse: Tracing Digit Bias to Numerical Hallucination in LLMs](http://papers.nips.cc/paper_files/paper/2025/hash/aa5f5e6eb6f613ec412f1d948dfa21a5-Abstract-Conference.html)** · Unlabeled · LLM · Training-free
- **📚 [🧜Siren’s Song in the AI Ocean: A Survey on Hallucination in Large Language Models](https://doi.org/10.1162/coli.a.16)** · Comput. Linguistics 2025 · LLM · Training-free
- **[keepitsimple at SemEval-2025 Task 3: LLM-Uncertainty based Approach for Multilingual Hallucination Span Detection](https://aclanthology.org/2025.semeval-1.11/)** · SemEval@ACL 2025 · LLM · Training-free
- **[WonderHuman: Hallucinating Unseen Parts in Dynamic 3D Human Reconstruction](https://doi.org/10.1109/TVCG.2025.3618268)** · IEEE Trans. Vis. Comput. Graph. 2025 · LLM · Training-free
- **[We Have a Package for You! A Comprehensive Analysis of Package Hallucinations by Code Generating LLMs](https://www.usenix.org/conference/usenixsecurity25/presentation/spracklen)** · USENIX Security Symposium 2025 · LLM · Training-free
- **[WITHDRAWN: Ambiguity processing in Large Language Models: Detection, resolution, and the path to hallucination](https://doi.org/10.1016/j.nlp.2025.100173)** · Natural Language Processing Journal 2025 · LLM · Training-free
- **[Uncertainty-Aware Fusion: An Ensemble Framework for Mitigating Hallucinations in Large Language Models](https://doi.org/10.1145/3701716.3715523)** · Companion Proceedings of the ACM on Web Conference 2025 · LLM · Training-free
- **[UCSC at SemEval-2025 Task 3: Context, Models and Prompt Optimization for Automated Hallucination Detection in LLM Output](https://aclanthology.org/2025.semeval-1.257/)** · SemEval@ACL 2025 · LLM · Training-free
- **[Trustworthy Medical Imaging with Large Language Models: A Study of Hallucinations Across Modalities](https://doi.org/10.1109/ICCVW69036.2025.00136)** · ICCVW 2025 · LLM · Training-free
- **[The hallucination problem in Generative Artificial Intelligence: accuracy and trust in digital learning](https://doi.org/10.58503/icvl-v20y202503)** · International Conference on Virtual Learning - VIRTUAL LEARNING - VIRTUAL REALITY (20th edition) 2025 · LLM · Training-free
- **[TUM-MiKaNi at SemEval-2025 Task 3: Towards Multilingual and Knowledge-Aware Non-factual Hallucination Identification](https://aclanthology.org/2025.semeval-1.141/)** · SemEval@ACL 2025 · LLM · Training-free
- **[Synthetic Data in AI: Performance Gains versus Hallucination Risk](https://doi.org/10.47852/bonviewaia52026620)** · Artificial Intelligence and Applications 2025 · LLM · Training-free
- **[SymLoc: Symbolic Localization of Hallucination across HaluEval and TruthfulQA](https://doi.org/10.1145/3799830.3799850)** · CODS 2025 · LLM · Training-free
- **[Shared Imagination: LLMs Hallucinate Alike](https://openreview.net/forum?id=NUXpBMtDYs)** · TMLR 2025 · LLM · Training-free
- **[SemEval-2025 Task 3: Mu-SHROOM, the Multilingual Shared Task on Hallucinations and Related Observable Overgeneration Mistakes](https://aclanthology.org/2025.semeval-1.322/)** · SemEval@ACL 2025 · LLM · Training-free
- **[SOK: Exploring Hallucinations and Security Risks in AI-Assisted Software Development with Insights for LLM Deployment](https://doi.org/10.1109/IDSTA66210.2025.11202778)** · IDSTA 2025 · LLM · Training-free
- **[S-AI-ANTI HALLUCINATION: A BIO-INSPIRED AND CONFIDENCE-AWARE SPARSE AI FRAMEWORK FOR RELIABLE GENERATIVE SYSTEMS](https://doi.org/10.5121/ijaia.2025.16601)** · International Journal of Artificial Intelligence & Applications 2025 · LLM · Training-free
- **[REFIND at SemEval-2025 Task 3: Retrieval-Augmented Factuality Hallucination Detection in Large Language Models](https://aclanthology.org/2025.semeval-1.2/)** · SemEval@ACL 2025 · LLM · Training-free
- **[RAG Technology for Reliable Medical Retrieval and Hallucination Mitigation](https://doi.org/10.1109/ccnis69465.2025.00009)** · 2nd International Conference on Computer Communication, Networks and Information Science (CCNIS) 2025 · LLM · Training-free
- **[Privacy-hardened and hallucination-resistant synthetic data generation with logic-solvers](https://doi.org/10.1093/bioinformatics/btaf600)** · Bioinform. 2025 · LLM · Training-free
- **[Persona Vectors in Controlling Hallucination of Small Large Language Models: A Safety-Oriented Analysis](https://doi.org/10.1109/cars67163.2025.11337402)** · Cyber Awareness and Research Symposium (CARS) 2025 · LLM · Training-free
- **[On the Limits of Language Generation: Trade-Offs Between Hallucination and Mode Collapse](https://doi.org/10.1145/3717823.3718108)** · STOC 2025 · LLM · Training-free
- **[On Mitigating Code LLM Hallucinations with API Documentation](https://doi.org/10.1109/ICSE-SEIP66354.2025.00027)** · SEIP@ICSE 2025 · LLM · Training-free
- **[NCL-UoR at SemEval-2025 Task 3: Detecting Multilingual Hallucination and Related Observable Overgeneration Text Spans with Modified RefChecker and Modified SeflCheckGPT](https://aclanthology.org/2025.semeval-1.39/)** · SemEval@ACL 2025 · LLM · Training-free
- **[MultiRAG: A Knowledge-guided Framework for Mitigating Hallucination in Multi-source Retrieval Augmented Generation](https://doi.org/10.1109/ICDE65448.2025.00230)** · ICDE 2025 · LLM · Training-free
- **[MetaRAG: Metamorphic Testing for Hallucination Detection in RAG Systems](https://ceur-ws.org/Vol-4136/iaai6.pdf)** · IAAI/ALA@ECAI 2025 · LLM · Training-free
- **[MSA at SemEval-2025 Task 3: High Quality Weak Labeling and LLM Ensemble Verification for Multilingual Hallucination Detection](https://aclanthology.org/2025.semeval-1.131/)** · SemEval@ACL 2025 · LLM · Training-free
- **[LargePiG for Hallucination-Free Query Generation: Your Large Language Model is Secretly a Pointer Generator](https://doi.org/10.1145/3696410.3714800)** · WWW 2025 · LLM · Training-free
- **[Large Language Models With Contrastive Decoding Algorithm for Hallucination Mitigation in Low‐Resource Languages](https://doi.org/10.1049/cit2.70004)** · CAAI Trans. Intell. Technol. 2025 · LLM · Training-free
- **[LLM Hallucinations in Practical Code Generation: Phenomena, Mechanism, and Mitigation](https://doi.org/10.1145/3728894)** · Proc. ACM Softw. Eng. 2025 · LLM · Training-free
- **[Knowledge Graphs, Large Language Models, and Hallucinations: An NLP Perspective](https://doi.org/10.1016/j.websem.2024.100844)** · J. Web Semant. 2025 · LLM · Training-free
- **[KEA Explain: Explanations of Hallucinations using Graph Kernel Analysis](https://proceedings.mlr.press/v284/haskins25a.html)** · NeSy 2025 · LLM · Training-free
- **[Investigating Symbolic Triggers of Hallucination in Gemma Models Across HaluEval and TruthfulQA](https://ceur-ws.org/Vol-4064/SymGenAI4Sci-paper2.pdf)** · SEMANTiCS 2025 · LLM · Training-free
- **[HausaNLP at SemEval-2025 Task 3: Towards a Fine-Grained Model-Aware Hallucination Detection](https://aclanthology.org/2025.semeval-1.227/)** · SemEval@ACL 2025 · LLM · Training-free
- **[Hallucinations in Code Change to Natural Language Generation: Prevalence and Evaluation of Detection Metrics](https://doi.org/10.18653/v1/2025.ijcnlp-long.137)** · IJCNLP-AACL 2025 · LLM · Training-free
- **[Hallucination-Free Automatic Question &amp; Answer Generation for Intuitive Learning](https://doi.org/10.1109/icipw68931.2025.11386040)** · IEEE International Conference on Image Processing Workshops (ICIPW) 2025 · LLM · Training-free
- **[Hallucination-Free Automatic Question & Answer Generation for Intuitive Learning](https://doi.org/10.1109/ICIPW68931.2025.11386040)** · ICIPW 2025 · LLM · Training-free
- **[Hallucination-Aware Generative Pretrained Transformer for Cooperative Aerial Mobility Control](https://doi.org/10.1109/GLOBECOM59602.2025.11432325)** · GLOBECOM 2025 · LLM · Training-free
- **[Hallucination in LLM-Based Code Generation: An Automotive Case Study](https://doi.org/10.1109/FLLM67465.2025.11391125)** · FLLM 2025 · LLM · Training-free
- **[Hallucination and Panic in Autonomous Systems](https://doi.org/10.1007/978-3-031-95207-4)** · Studies in Computational Intelligence 2025 · LLM · Training-free
- **[Hallucination Detectives at SemEval-2025 Task 3: Span-Level Hallucination Detection for LLM-Generated Answers](https://aclanthology.org/2025.semeval-1.84/)** · SemEval@ACL 2025 · LLM · Training-free
- **[Hallucination Detection with Small Language Models](https://doi.org/10.1109/ICDEW67478.2025.00033)** · ICDEW 2025 · LLM · Training-free
- **[Hallucination Detection in Large Language Models with Metamorphic Relations](https://doi.org/10.1145/3715735)** · Proc. ACM Softw. Eng. 2025 · LLM · Training-free
- **[Hallucination Detection in Large Language Models Using Diversion Decoding](https://doi.org/10.1007/978-3-031-96590-6_7)** · DBSec 2025 · LLM · Training-free
- **[Hallucination Detection in LLMs via Beam Search Sampling and Semantic Consistency Analysis](https://doi.org/10.1109/DSN-W65791.2025.00076)** · DSN-W 2025 · LLM · Training-free
- **📚 [Hallucination Detection in Foundation Models for Decision-Making: A Flexible Definition and Review of the State of the Art](https://doi.org/10.1145/3716846)** · ACM Comput. Surv. 2025 · LLM · Training-free
- **[Hallucination Detection and Mitigation in Scientific Text Simplification using Ensemble Approaches: DS@GT at CLEF 2025 SimpleText](https://ceur-ws.org/Vol-4038/paper_356.pdf)** · CLEF 2025 · LLM · Training-free
- **[Hallucination Detection and Confidence Calibration for Large Language Model Outputs: Reproducible Experiments on HaluEval](https://doi.org/10.69987/aimlr.2025.60401)** · Artificial Intelligence and Machine Learning Review 2025 · LLM · Training-free
- **[HalluShift: Measuring Distribution Shifts towards Hallucination Detection in LLMs](https://doi.org/10.1109/IJCNN64981.2025.11228484)** · IJCNN 2025 · LLM · Training-free
- **[HalluSearch at SemEval-2025 Task 3: A Search-Enhanced RAG Pipeline for Hallucination Detection](https://aclanthology.org/2025.semeval-1.189/)** · SemEval@ACL 2025 · LLM · Training-free
- **[HalluEntity: Benchmarking and Understanding Entity-Level Hallucination Detection](https://openreview.net/forum?id=494k7e9R5D)** · TMLR 2025 · LLM · Training-free
- **[HalluCounter: Reference-free LLM Hallucination Detection in the Wild!](https://doi.org/10.18653/v1/2025.findings-ijcnlp.20)** · IJCNLP-AACL 2025 · LLM · Training-free
- **[HFuzzer: Testing Large Language Models for Package Hallucinations via Phrase-based Fuzzing](https://doi.org/10.1109/ASE63991.2025.00225)** · ASE 2025 · LLM · Training-free
- **[HALO: Hallucination Analysis and Learning Optimization to Empower LLMs with Retrieval-Augmented Context for Guided Clinical Decision Making](https://doi.org/10.1145/3721201.3721385)** · CHASE 2025 · LLM · Training-free
- **[Generative AI in Medical Pharmacology: Balancing Educational Benefits and Hallucination Risks](https://doi.org/10.21275/sr25415140148)** · International Journal of Science and Research (IJSR) 2025 · LLM · Training-free
- **[GRAVITI: Grounded Retrieval Generation Framework for VideoLLM Hallucination Mitigation](https://doi.org/10.5120/ijca2025926005)** · International Journal of Computer Applications 2025 · LLM · Training-free
- **[GPTs and Hallucination](https://doi.org/10.1145/3703757)** · Commun. ACM 2025 · LLM · Training-free
- **[GOLFer: Smaller LMs-Generated Documents Hallucination Filter &amp; Combiner for Query Expansion in Information Retrieval](https://doi.org/10.18653/v1/2025.findings-acl.8)** · Comput. Linguistics 2025 · LLM · Training-free
- **[Fine-Tuned Large Language Models for Logical Translation: Reducing Hallucinations with Lang2Logic](https://doi.org/10.1109/ISNCC66965.2025.11250432)** · ISNCC 2025 · LLM · Training-free
- **[Fewer Hallucinations, More Verification: A Three-Stage LLM-Based Framework for ASR Error Correction](https://doi.org/10.1109/ASRU65441.2025.11434775)** · ASRU 2025 · LLM · Training-free
- **[Few-Shot Optimized Framework for Hallucination Detection in Resource-Limited NLP Systems](https://doi.org/10.1007/978-981-96-6441-2_16)** · Lecture Notes in Networks and Systems 2025 · LLM · Training-free
- **[FAITH: A Framework for Assessing Intrinsic Tabular Hallucinations in Finance](https://doi.org/10.1145/3768292.3770433)** · ICAIF 2025 · LLM · Training-free
- **[Exploring Causal Effect of Social Bias on Faithfulness Hallucinations in Large Language Models](https://doi.org/10.1145/3746252.3761298)** · CIKM 2025 · LLM · Training-free
- **[Expertise or Hallucination? A Comprehensive Evaluation of ChatGPT's Aptitude in Clinical Genetics](https://doi.org/10.1109/TBDATA.2025.3536939)** · IEEE Trans. Big Data 2025 · LLM · Training-free
- **[Evidence-Enhanced Triplet Generation Framework for Hallucination Alleviation in Generative Question Answering](https://escholarship.org/uc/item/21j040mk)** · CogSci 2025 · LLM · Training-free
- **[Ethical Prompt Design for Health Equity: Preventing Hallucination and Addressing Bias in AI Diagnoses](https://doi.org/10.63282/3050-9262.ijaidsml-v6i3p102)** · International Journal of Artificial Intelligence, Data Science, and Machine Learning 2025 · LLM · Training-free
- **[ECD: Efficient Contrastive Decoding with Probabilistic Hallucination Detection](https://doi.org/10.1007/978-3-032-06109-6_2)** · ECML/PKDD 2025 · LLM · Training-free
- **[Dynamics-inspired Structure Hallucination for Protein-protein Interaction Modeling](https://arxiv.org/abs/2601.06214)** · TMLR 2025 · LLM · Training-free
- **[Dynamic Cognitive Bias: Hallucination and Forgetting in the Cognitive Dynamics of LLMs](https://doi.org/10.1109/IJCNN64981.2025.11229003)** · IJCNN 2025 · LLM · Training-free
- **[Detection of LLM Hallucinations Using Late Internal Representations](https://doi.org/10.1109/ICMLA66185.2025.00214)** · ICMLA 2025 · LLM · Training-free
- **[Cross-Layer Attention Probing for Fine-Grained Hallucination Detection](https://ceur-ws.org/Vol-4132/short39.pdf)** · TRUST-AI@ECAI 2025 · LLM · Training-free
- **[Countering AI Hallucination by Utilizing a Concept-Aware Model](https://doi.org/10.1109/mecon67253.2025.11277080)** · Multimedia University Engineering Conference (MECON) 2025 · LLM · Training-free
- **[Consistency Is the Key: Detecting Hallucinations in LLM Generated Text By Checking Inconsistencies About Key Facts](https://doi.org/10.18653/v1/2025.findings-ijcnlp.129)** · IJCNLP-AACL 2025 · LLM · Training-free
- **[Confident but Incorrect: Mitigating Hallucination and Overconfidence in Agentic AI Coders](https://doi.org/10.1109/iciip68302.2025.11346318)** · Eighth International Conference on Image Information Processing (ICIIP) 2025 · LLM · Training-free
- **[Comparison of explainability methods for hallucination analysis in LLMs](https://doi.org/10.12688/openreseurope.20839.1)** · Open Research Europe 2025 · LLM · Training-free
- **📋 [ChartInsighter: An Approach for Mitigating Hallucination in Time-series Chart Summary Generation with A Benchmark Dataset](https://doi.org/10.1109/TVCG.2025.3567122)** · IEEE Trans. Vis. Comput. Graph. 2025 · LLM · Training-free
- **[Catch Me if You Search: When Contextual Web Search Results Affect the Detection of Hallucinations](https://doi.org/10.1016/j.chb.2025.108763)** · Comput. Hum. Behav. 2025 · LLM · Training-free
- **[Can LLM be a Good Path Planner based on Prompt Engineering? Mitigating the Hallucination for Path Planning](https://doi.org/10.1007/978-981-95-0014-7_1)** · ICIC 2025 · LLM · Training-free
- **[Calibrated Trust in Dealing with LLM Hallucinations: A Qualitative Study](https://doi.org/10.1109/FLLM67465.2025.11391250)** · FLLM 2025 · LLM · Training-free
- **[CHAIR-Classifier of Hallucination As Improver](https://doi.org/10.1109/IJCNN64981.2025.11227344)** · IJCNN 2025 · LLM · Training-free
- **[CCNU at SemEval-2025 Task 3: Leveraging Internal and External Knowledge of Large Language Models for Multilingual Hallucination Annotation](https://aclanthology.org/2025.semeval-1.62/)** · SemEval@ACL 2025 · LLM · Training-free
- **📋 [C-FAITH: A Chinese Fine-Grained Benchmark for Automated Hallucination Evaluation](https://doi.org/10.1145/3746252.3761604)** · CIKM 2025 · LLM · Training-free
- **[Beyond Hallucination: Generative AI as a Catalyst for Human Creativity and Cognitive Evolution](https://doi.org/10.62762/tetai.2025.657559)** · ICCK Transactions on Emerging Topics in Artificial Intelligence 2025 · LLM · Training-free
- **[AraHalluEval: A Fine-grained Hallucination Evaluation Framework for Arabic LLMs](https://doi.org/10.18653/v1/2025.arabicnlp-main.12)** · Third Arabic Natural Language Processing Conference 2025 · LLM · Training-free
- **[An Analysis on AI Hallucination from the Perspective of Media Archaeology](https://doi.org/10.54254/2753-7064/2025.bj29177)** · Communications in Humanities Research 2025 · LLM · Training-free
- **[AggTruth: Contextual Hallucination Detection using Aggregated Attention Scores in LLMs](https://doi.org/10.1007/978-3-031-97570-7_18)** · ICCS 2025 · LLM · Training-free
- **[Agentic Legal Intake: A Multi-Agent Framework For Hallucination-Free, Audit-Ready AI Screening In Mass-Tort Litigation](https://doi.org/10.37547/feaiml/volume02issue09-02)** · Frontiers in Emerging Artificial Intelligence and Machine Learning 2025 · LLM · Training-free
- **[Aftina: enhancing stability and preventing hallucination in AI-based Islamic fatwa generation using LLMs and RAG](https://doi.org/10.1007/s00521-025-11229-y)** · Neural Comput. Appl. 2025 · LLM · Training-free
- **[Adaptive Activation Steering: A Tuning-Free LLM Truthfulness Improvement Method for Diverse Hallucinations Categories](https://doi.org/10.1145/3696410.3714640)** · WWW 2025 · LLM · Training-free
- **[ATLANTIS at SemEval-2025 Task 3: Detecting Hallucinated Text Spans in Question Answering](https://aclanthology.org/2025.semeval-1.145/)** · SemEval@ACL 2025 · LLM · Training-free
- **[AILS-NTUA at SemEval-2025 Task 3: Leveraging Large Language Models and Translation Strategies for Multilingual Hallucination Detection](https://aclanthology.org/2025.semeval-1.172/)** · SemEval@ACL 2025 · LLM · Training-free
- **[AI in conjunctivitis research: assessing ChatGPT and DeepSeek for etiology, intervention, and citation integrity via hallucination rate analysis](https://doi.org/10.3389/frai.2025.1579375)** · Frontiers Artif. Intell. 2025 · LLM · Training-free
- **[AI Hallucinations? What About Human Hallucination?! Addressing Human Imperfection Is Needed for an Ethical AI](https://doi.org/10.9781/ijimai.2025.02.010)** · Int. J. Interact. Multim. Artif. Intell. 2025 · LLM · Training-free
- **[AI Hallucination in the Context of Education: Exploring College Students’ Use of Generative AI for Academic Tasks](https://doi.org/10.1109/ic4e65071.2025.11075444)** · 16th International Conference on E-Education, E-Business, E-Management and E-Learning (IC4e) 2025 · LLM · Training-free
- **[AI Hallucination and Strategies to Overcome: Enhancing Human-AI Interaction](https://doi.org/10.1109/aimv66517.2025.11203756)** · International Conference on Artificial Intelligence and Machine Vision (AIMV) 2025 · LLM · Training-free
- **📚 [A Scoping Review of Natural Language Processing in Addressing Medically Inaccurate Information: Errors, Misinformation, and Hallucination](https://doi.org/10.1016/j.jbi.2025.104866)** · J. Biomed. Informatics 2025 · LLM · Training-free
- **📚 [A Review of Faithfulness Metrics for Hallucination Assessment in Large Language Models](https://doi.org/10.1109/JSTSP.2025.3579203)** · IEEE J. Sel. Top. Signal Process. 2025 · LLM · Training-free

</details>

<details>
<summary>📅 2024 · 253 papers</summary>

- **📋 [The HalluRAG Dataset: Detecting Closed-Domain Hallucinations in RAG Applications Using an LLM's Internal States](https://arxiv.org/abs/2412.17056)** · arXiv · LLM · Training-free
- **[On Characterizations for Language Generation: Interplay of Hallucinations, Breadth, and Stability](https://arxiv.org/abs/2412.18530)** · arXiv · LLM · Training-free
- **[From Hallucinations to Facts: Enhancing Language Models with Curated Knowledge Graphs](https://arxiv.org/abs/2412.18672)** · arXiv · LLM · Training-free
- **[An Evolutionary Large Language Model for Hallucination Mitigation](https://arxiv.org/abs/2412.02790)** · arXiv · LLM · Training-free
- **[100% Elimination of Hallucinations on RAGTruth for GPT-4 and GPT-3.5 Turbo](https://arxiv.org/abs/2412.05223)** · arXiv · LLM · Training-free
- **[Understanding Hallucinations in Diffusion Models through Mode Interpolation](http://papers.nips.cc/paper_files/paper/2024/hash/f29369d192b13184b65c6d2515474d78-Abstract-Conference.html)** · NeurIPS 2024 · LLM · Training-free
- **[THaMES: An End-to-End Tool for Hallucination Mitigation and Evaluation in Large Language Models](https://arxiv.org/abs/2409.11353)** · NeurIPS 2024 · LLM · Training-free
- **[Mitigating Object Hallucination via Concentric Causal Attention](http://papers.nips.cc/paper_files/paper/2024/hash/a76ed4a8ef522c823d73925e7fff16d4-Abstract-Conference.html)** · NeurIPS 2024 · LLM · Training-free
- **[LLM-Check: Investigating Detection of Hallucinations in Large Language Models](http://papers.nips.cc/paper_files/paper/2024/hash/3c1e1fdf305195cd620c118aaa9717ad-Abstract-Conference.html)** · NeurIPS 2024 · LLM · Training-free
- **[ANAH-v2: Scaling Analytical Hallucination Annotation of Large Language Models](http://papers.nips.cc/paper_files/paper/2024/hash/6e4cdfdd909ea4e34bfc85a12774cba0-Abstract-Conference.html)** · NeurIPS 2024 · LLM · Training-free
- **[VidHal: Benchmarking Temporal Hallucinations in Vision LLMs](https://arxiv.org/abs/2411.16771)** · arXiv · LLM · Training-free
- **[Seeing Through the Fog: A Cost-Effectiveness Analysis of Hallucination Detection Systems](https://arxiv.org/abs/2411.05270)** · arXiv · LLM · Training-free
- **[Prompt-Efficient Fine-Tuning for GPT-like Deep Models to Reduce Hallucination and to Improve Reproducibility in Scientific Text Generation Using Stochastic Optimisation Techniques](https://arxiv.org/abs/2411.06445)** · arXiv · LLM · Training-free
- **[Probing LLM Hallucination from Within: Perturbation-Driven Approach via Internal Knowledge](https://arxiv.org/abs/2411.09689)** · arXiv · LLM · Training-free
- **[Mitigating Hallucination with ZeroG: An Advanced Knowledge Management Engine](https://arxiv.org/abs/2411.05936)** · arXiv · LLM · Training-free
- **[Layer Importance and Hallucination Analysis in Large Language Models via Enhanced Activation Variance-Sparsity](https://arxiv.org/abs/2411.10069)** · arXiv · LLM · Training-free
- **[Hallucination Detection in Virtually-Stained Histology: A Latent Space Baseline](https://arxiv.org/abs/2411.15060)** · arXiv · LLM · Training-free
- **[Enhancing Multi-Agent Consensus through Third-Party LLM Integration: Analyzing Uncertainty and Mitigating Hallucinations in Large Language Models](https://arxiv.org/abs/2411.16189)** · arXiv · LLM · Training-free
- **[EF-LLM: Energy Forecasting LLM with AI-assisted Automation, Enhanced Sparse Prediction, Hallucination Detection](https://arxiv.org/abs/2411.00852)** · arXiv · LLM · Training-free
- **[DecoPrompt : Decoding Prompts Reduces Hallucinations when Large Language Models Meet False Premises](https://arxiv.org/abs/2411.07457)** · arXiv · LLM · Training-free
- **📋 [DAHL: Domain-specific Automated Hallucination Evaluation of Long-Form Text through a Benchmark Dataset in Biomedicine](https://arxiv.org/abs/2411.09255)** · arXiv · LLM · Training-free
- **[Addressing Hallucinations in Language Models with Knowledge Graph Embeddings as an Additional Modality](https://arxiv.org/abs/2411.11531)** · arXiv · LLM · Training-free
- **[A Novel Approach to Eliminating Hallucinations in Large Language Model-Assisted Causal Discovery](https://arxiv.org/abs/2411.12759)** · arXiv · LLM · Training-free
- **[Zero-Resource Hallucination Prevention for Large Language Models](https://doi.org/10.18653/v1/2024.findings-emnlp.204)** · EMNLP 2024 · LLM · Training-free
- **[Whispers that Shake Foundations: Analyzing and Mitigating False Premise Hallucinations in Large Language Models](https://doi.org/10.18653/v1/2024.emnlp-main.155)** · EMNLP 2024 · LLM · Training-free
- **[Two-tiered Encoder-based Hallucination Detection for Retrieval-Augmented Generation in the Wild](https://doi.org/10.18653/v1/2024.emnlp-industry.2)** · EMNLP 2024 · LLM · Training-free
- **📋 [ToolBeHonest: A Multi-level Hallucination Diagnostic Benchmark for Tool-Augmented Large Language Models](https://doi.org/10.18653/v1/2024.emnlp-main.637)** · EMNLP 2024 · LLM · Training-free
- **[Small Agent Can Also Rock! Empowering Small Language Models as Hallucination Detector](https://doi.org/10.18653/v1/2024.emnlp-main.809)** · EMNLP 2024 · LLM · Training-free
- **[RAG-HAT: A Hallucination-Aware Tuning Pipeline for LLM in Retrieval-Augmented Generation](https://doi.org/10.18653/v1/2024.emnlp-industry.113)** · EMNLP 2024 · LLM · Training-free
- **[Pre-trained Language Models Return Distinguishable Probability Distributions to Unfaithfully Hallucinated Texts](https://doi.org/10.18653/v1/2024.findings-emnlp.738)** · EMNLP 2024 · LLM · Training-free
- **[Pelican: Correcting Hallucination in Vision-LLMs via Claim Decomposition and Program of Thought Verification](https://doi.org/10.18653/v1/2024.emnlp-main.470)** · EMNLP 2024 · LLM · Training-free
- **[Null-Shot Prompting: Rethinking Prompting Large Language Models With Hallucination](https://doi.org/10.18653/v1/2024.emnlp-main.740)** · EMNLP 2024 · LLM · Training-free
- **[Navigating Hallucinations for Reasoning of Unintentional Activities](https://doi.org/10.18653/v1/2024.findings-emnlp.565)** · EMNLP 2024 · LLM · Training-free
- **[Multilingual Fine-Grained News Headline Hallucination Detection](https://doi.org/10.18653/v1/2024.findings-emnlp.461)** · EMNLP 2024 · LLM · Training-free
- **[Mitigating Open-Vocabulary Caption Hallucinations](https://doi.org/10.18653/v1/2024.emnlp-main.1263)** · EMNLP 2024 · LLM · Training-free
- **[Mitigating Hallucinations of Large Language Models in Medical Information Extraction via Contrastive Decoding](https://doi.org/10.18653/v1/2024.findings-emnlp.456)** · EMNLP 2024 · LLM · Training-free
- **[Mitigating Hallucination in Fictional Character Role-Play](https://doi.org/10.18653/v1/2024.findings-emnlp.846)** · EMNLP 2024 · LLM · Training-free
- **[Medico: Towards Hallucination Detection and Correction with Multi-source Evidence Fusion](https://doi.org/10.18653/v1/2024.emnlp-demo.4)** · EMNLP 2024 · LLM · Training-free
- **[Mechanistic Understanding and Mitigation of Language Model Non-Factual Hallucinations](https://doi.org/10.18653/v1/2024.findings-emnlp.466)** · EMNLP 2024 · LLM · Training-free
- **[Machine Translation Hallucination Detection for Low and High Resource Languages using Large Language Models](https://doi.org/10.18653/v1/2024.findings-emnlp.564)** · EMNLP 2024 · LLM · Training-free
- **[Lookback Lens: Detecting and Mitigating Contextual Hallucinations in Large Language Models Using Only Attention Maps](https://doi.org/10.18653/v1/2024.emnlp-main.84)** · EMNLP 2024 · LLM · Training-free
- **[Knowledge-Centric Hallucination Detection](https://doi.org/10.18653/v1/2024.emnlp-main.395)** · EMNLP 2024 · LLM · Training-free
- **[Knowledge Verification to Nip Hallucination in the Bud](https://doi.org/10.18653/v1/2024.emnlp-main.152)** · EMNLP 2024 · LLM · Training-free
- **[HalluMeasure: Fine-grained Hallucination Measurement Using Chain-of-Thought Reasoning](https://doi.org/10.18653/v1/2024.emnlp-main.837)** · EMNLP 2024 · LLM · Training-free
- **[Enhanced Hallucination Detection in Neural Machine Translation through Simple Detector Aggregation](https://doi.org/10.18653/v1/2024.emnlp-main.1033)** · EMNLP 2024 · LLM · Training-free
- **[Embedding and Gradient Say Wrong: A White-Box Method for Hallucination Detection](https://doi.org/10.18653/v1/2024.emnlp-main.116)** · EMNLP 2024 · LLM · Training-free
- **[Does Fine-Tuning LLMs on New Knowledge Encourage Hallucinations?](https://doi.org/10.18653/v1/2024.emnlp-main.444)** · EMNLP 2024 · LLM · Training-free
- **📋 [DiaHalu: A Dialogue-level Hallucination Evaluation Benchmark for Large Language Models](https://doi.org/10.18653/v1/2024.findings-emnlp.529)** · EMNLP 2024 · LLM · Training-free
- **[An Audit on the Perspectives and Challenges of Hallucinations in NLP](https://doi.org/10.18653/v1/2024.emnlp-main.375)** · EMNLP 2024 · LLM · Training-free
- **[Multilingual Hallucination Gaps in Large Language Models](https://arxiv.org/abs/2410.18270)** · arXiv · LLM · Training-free
- **[Mitigating Hallucinations Using Ensemble of Knowledge Graph and Vector Store in Large Language Models to Enhance Mental Health Support](https://arxiv.org/abs/2410.10853)** · arXiv · LLM · Training-free
- **[Maintaining Informative Coherence: Migrating Hallucinations in Large Language Models via Absorbing Markov Chains](https://arxiv.org/abs/2410.20340)** · arXiv · LLM · Training-free
- **[Leveraging the Domain Adaptation of Retrieval Augmented Generation Models for Question Answering and Reducing Hallucination](https://arxiv.org/abs/2410.17783)** · arXiv · LLM · Training-free
- **[Large Language Models Powered Multiagent Ensemble for Mitigating Hallucination and Efficient Atrial Fibrillation Annotation of ECG Reports](https://arxiv.org/abs/2410.16543)** · arXiv · LLM · Training-free
- **[Iter-AHMCL: Alleviate Hallucination for Large Language Model via Iterative Model-level Contrastive Learning](https://arxiv.org/abs/2410.12130)** · arXiv · LLM · Training-free
- **[Investigating the Role of Prompting and External Tools in Hallucination Rates of Large Language Models](https://arxiv.org/abs/2410.19385)** · arXiv · LLM · Training-free
- **[Ingest-And-Ground: Dispelling Hallucinations from Continually-Pretrained LLMs with RAG](https://arxiv.org/abs/2410.02825)** · arXiv · LLM · Training-free
- **[Hallucinating AI Hijacking Attack: Large Language Models and Malicious Code Recommenders](https://arxiv.org/abs/2410.06462)** · arXiv · LLM · Training-free
- **[Good Parenting is all you need -- Multi-agentic LLM Hallucination Mitigation](https://arxiv.org/abs/2410.14262)** · arXiv · LLM · Training-free
- **[Distinguishing Ignorance from Error in LLM Hallucinations](https://arxiv.org/abs/2410.22071)** · arXiv · LLM · Training-free
- **📋 [Collu-Bench: A Benchmark for Predicting Language Model Hallucinations in Code](https://arxiv.org/abs/2410.09997)** · arXiv · LLM · Training-free
- **[Beyond Fine-Tuning: Effective Strategies for Mitigating Hallucinations in Large Language Models for Data Analytics](https://arxiv.org/abs/2410.20024)** · arXiv · LLM · Training-free
- **[A Debate-Driven Experiment on LLM Hallucinations and Accuracy](https://arxiv.org/abs/2410.19485)** · arXiv · LLM · Training-free
- **[Optimizing Resource Consumption in Diffusion Models Through Hallucination Early Detection](https://doi.org/10.1007/978-3-031-91979-4_23)** · ECCV Workshops 2024 · LLM · Training-free
- **[MedHalu: Hallucinations in Responses to Healthcare Queries by Large Language Models](https://arxiv.org/abs/2409.19492)** · arXiv · LLM · Training-free
- **[Long-horizon Embodied Planning with Implicit Logical Inference and Hallucination Mitigation](https://arxiv.org/abs/2409.15658)** · arXiv · LLM · Training-free
- **[Hallucination Detection in LLMs: Fast and Memory-Efficient Fine-Tuned Models](https://arxiv.org/abs/2409.02976)** · arXiv · LLM · Training-free
- **[Gaps or Hallucinations? Gazing into Machine-Generated Legal Analysis for Fine-grained Text Evaluations](https://arxiv.org/abs/2409.09947)** · arXiv · LLM · Training-free
- **[Combining LLMs and Knowledge Graphs to Reduce Hallucinations in Question Answering](https://arxiv.org/abs/2409.04181)** · arXiv · LLM · Training-free
- **[A Multiple-Fill-in-the-Blank Exam Approach for Enhancing Zero-Resource Hallucination Detection in Large Language Models](https://arxiv.org/abs/2409.17173)** · arXiv · LLM · Training-free
- **[Training Language Models on the Knowledge Graph: Insights on Hallucinations and Their Detectability](https://arxiv.org/abs/2408.07852)** · arXiv · LLM · Training-free
- **[Towards Reliable Medical Question Answering: Techniques and Challenges in Mitigating Hallucinations in Language Models](https://arxiv.org/abs/2408.13808)** · arXiv · LLM · Training-free
- **[SLM Meets LLM: Balancing Latency, Interpretability and Consistency in Hallucination Detection](https://arxiv.org/abs/2408.12748)** · arXiv · LLM · Training-free
- **📋 [Order Matters in Hallucination: Reasoning Order as Benchmark and Reflexive Prompting for Large-Language-Models](https://arxiv.org/abs/2408.05093)** · arXiv · LLM · Training-free
- **[Lower Layers Matter: Alleviating Hallucination via Multi-Layer Fusion Contrastive Decoding with Truthfulness Refocused](https://arxiv.org/abs/2408.08769)** · arXiv · LLM · Training-free
- **[LRP4RAG: Detecting Hallucinations in Retrieval-Augmented Generation via Layer-wise Relevance Propagation](https://arxiv.org/abs/2408.15533)** · arXiv · LLM · Training-free
- **[Interactive DualChecker for Mitigating Hallucinations in Distilling Large Language Models](https://arxiv.org/abs/2408.12326)** · arXiv · LLM · Training-free
- **[FiSTECH: Financial Style Transfer to Enhance Creativity without Hallucinations in LLMs](https://arxiv.org/abs/2408.05365)** · arXiv · LLM · Training-free
- **[CodeMirage: Hallucinations in Code Generated by Large Language Models](https://arxiv.org/abs/2408.08333)** · arXiv · LLM · Training-free
- **[On Early Detection of Hallucinations in Factual Question Answering](https://doi.org/10.1145/3637528.3671796)** · KDD 2024 · LLM · Training-free
- **[Honest AI: Fine-Tuning "Small" Language Models to Say "I Don't Know", and Reducing Hallucination in RAG](https://arxiv.org/abs/2410.09699)** · KDD 2024 · LLM · Training-free
- **[FactCHD: Benchmarking Fact-Conflicting Hallucination Detection](https://www.ijcai.org/proceedings/2024/687)** · IJCAI 2024 · LLM · Training-free
- **[Controlled Automatic Task-Specific Synthetic Data Generation for Hallucination Detection](https://arxiv.org/abs/2410.12278)** · KDD 2024 · LLM · Training-free
- **[PFME: A Modular Approach for Fine-grained Hallucination Detection and Editing of Large Language Models](https://arxiv.org/abs/2407.00488)** · arXiv · LLM · Training-free
- **[Lynx: An Open Source Hallucination Evaluation Model](https://arxiv.org/abs/2407.08488)** · arXiv · LLM · Training-free
- **[Look Within, Why LLMs Hallucinate: A Causal Perspective](https://arxiv.org/abs/2407.10153)** · arXiv · LLM · Training-free
- **[Knowledge Overshadowing Causes Amalgamated Hallucination in Large Language Models](https://arxiv.org/abs/2407.08039)** · arXiv · LLM · Training-free
- **[Halu-J: Critique-Based Hallucination Judge](https://arxiv.org/abs/2407.12943)** · arXiv · LLM · Training-free
- **[Generation Constraint Scaling Can Mitigate Hallucination](https://arxiv.org/abs/2407.16908)** · arXiv · LLM · Training-free
- **[Cost-Effective Hallucination Detection for LLMs](https://arxiv.org/abs/2407.21424)** · arXiv · LLM · Training-free
- **[Code Hallucination](https://arxiv.org/abs/2407.04831)** · arXiv · LLM · Training-free
- **[Unsupervised Real-Time Hallucination Detection based on the Internal States of Large Language Models](https://doi.org/10.18653/v1/2024.findings-acl.854)** · ACL 2024 · LLM · Training-free
- **[TruthX: Alleviating Hallucinations by Editing Large Language Models in Truthful Space](https://doi.org/10.18653/v1/2024.acl-long.483)** · ACL 2024 · LLM · Training-free
- **[Truth-O-Meter: Handling Multiple Inconsistent Sources Repairing LLM Hallucinations](https://doi.org/10.1145/3626772.3657679)** · SIGIR 2024 · LLM · Training-free
- **[Truth-Aware Context Selection: Mitigating Hallucinations of Large Language Models Being Misled by Untruthful Contexts](https://doi.org/10.18653/v1/2024.findings-acl.645)** · ACL 2024 · LLM · Training-free
- **[TimeChara: Evaluating Point-in-Time Character Hallucination of Role-Playing Large Language Models](https://doi.org/10.18653/v1/2024.findings-acl.197)** · ACL 2024 · LLM · Training-free
- **[The Dawn After the Dark: An Empirical Study on Factuality Hallucination in Large Language Models](https://doi.org/10.18653/v1/2024.acl-long.586)** · ACL 2024 · LLM · Training-free
- **[Strong hallucinations from negation and how to fix them](https://doi.org/10.18653/v1/2024.findings-acl.752)** · ACL 2024 · LLM · Training-free
- **[Self-Alignment for Factuality: Mitigating Hallucinations in LLMs via Self-Evaluation](https://doi.org/10.18653/v1/2024.acl-long.107)** · ACL 2024 · LLM · Training-free
- **[Roberta with Low-Rank Adaptation and Hierarchical Attention for Hallucination Detection in LLMs](https://doi.org/10.1109/icicml63543.2024.10957858)** · ICML 2024 · LLM · Training-free
- **[On the Hallucination in Simultaneous Machine Translation](https://doi.org/10.18653/v1/2024.acl-short.66)** · ACL 2024 · LLM · Training-free
- **[OTTAWA: Optimal TransporT Adaptive Word Aligner for Hallucination and Omission Translation Errors Detection](https://doi.org/10.18653/v1/2024.findings-acl.377)** · ACL 2024 · LLM · Training-free
- **[Mitigating Entity-Level Hallucination in Large Language Models](https://doi.org/10.1145/3673791.3698403)** · SIGIR-AP 2024 · LLM · Training-free
- **[Leveraging Graph Structures to Detect Hallucinations in Large Language Models](https://arxiv.org/abs/2407.04485)** · ACL 2024 · LLM · Training-free
- **[InterrogateLLM: Zero-Resource Hallucination Detection in LLM-Generated Answers](https://arxiv.org/abs/2403.02889)** · ACL 2024 · LLM · Training-free
- **[In-Context Sharpness as Alerts: An Inner Representation Perspective for Hallucination Mitigation](https://proceedings.mlr.press/v235/chen24av.html)** · ICML 2024 · LLM · Training-free
- **[HALC: Object Hallucination Reduction via Adaptive Focal-Contrast Decoding](https://proceedings.mlr.press/v235/chen24bi.html)** · ICML 2024 · LLM · Training-free
- **[Genetic Approach to Mitigate Hallucination in Generative IR](https://arxiv.org/abs/2409.00085)** · SIGIR 2024 · LLM · Training-free
- **[Enhancing Hallucination Detection through Perturbation-Based Synthetic Data Generation in System Responses](https://doi.org/10.18653/v1/2024.findings-acl.789)** · ACL 2024 · LLM · Training-free
- **[Don't Hallucinate, Abstain: Identifying LLM Knowledge Gaps via Multi-LLM Collaboration](https://doi.org/10.18653/v1/2024.acl-long.786)** · ACL 2024 · LLM · Training-free
- **[Confabulation: The Surprising Value of Large Language Model Hallucinations](https://doi.org/10.18653/v1/2024.acl-long.770)** · ACL 2024 · LLM · Training-free
- **[Before Generation, Align it! A Novel and Effective Strategy for Mitigating Hallucinations in Text-to-SQL Generation](https://doi.org/10.18653/v1/2024.findings-acl.324)** · ACL 2024 · LLM · Training-free
- **[Analyzing LLM Behavior in Dialogue Summarization: Unveiling Circumstantial Hallucination Trends](https://doi.org/10.18653/v1/2024.acl-long.677)** · ACL 2024 · LLM · Training-free
- **[ANHALTEN: Cross-Lingual Transfer for German Token-Level Reference-Free Hallucination Detection](https://doi.org/10.18653/v1/2024.acl-srw.18)** · ACL 2024 · LLM · Training-free
- **[ANAH: Analytical Annotation of Hallucinations in Large Language Models](https://doi.org/10.18653/v1/2024.acl-long.442)** · ACL 2024 · LLM · Training-free
- **[ACUEval: Fine-grained Hallucination Evaluation and Correction for Abstractive Summarization](https://doi.org/10.18653/v1/2024.findings-acl.597)** · ACL 2024 · LLM · Training-free
- **[Semantic Entropy Probes: Robust and Cheap Hallucination Detection in LLMs](https://arxiv.org/abs/2406.15927)** · arXiv · LLM · Training-free
- **[Mitigating Large Language Model Hallucination with Faithful Finetuning](https://arxiv.org/abs/2406.11267)** · arXiv · LLM · Training-free
- **[Luna: An Evaluation Foundation Model to Catch Language Model Hallucinations with High Accuracy and Low Cost](https://arxiv.org/abs/2406.00975)** · arXiv · LLM · Training-free
- **[Large Language Models are Skeptics: False Negative Problem of Input-conflicting Hallucination](https://arxiv.org/abs/2406.13929)** · arXiv · LLM · Training-free
- **[Investigating and Addressing Hallucinations of LLMs in Tasks Involving Negation](https://arxiv.org/abs/2406.05494)** · arXiv · LLM · Training-free
- **📋 [HalluDial: A Large-Scale Benchmark for Automatic Dialogue-Level Hallucination Evaluation](https://arxiv.org/abs/2406.07070)** · arXiv · LLM · Training-free
- **📋 [DefAn: Definitive Answer Dataset for LLMs Hallucination Evaluation](https://arxiv.org/abs/2406.09155)** · arXiv · LLM · Training-free
- **[Confidence-Aware Sub-Structure Beam Search (CABS): Mitigating Hallucination in Structured Data Generation with Large Language Models](https://arxiv.org/abs/2406.00069)** · arXiv · LLM · Training-free
- **[Chaos with Keywords: Exposing Large Language Models Sycophantic Hallucination to Misleading Keywords and Evaluating Defense Strategies](https://arxiv.org/abs/2406.03827)** · arXiv · LLM · Training-free
- **[Banishing LLM Hallucinations Requires Rethinking Generalization](https://arxiv.org/abs/2406.17642)** · arXiv · LLM · Training-free
- **[Ask-EDA: A Design Assistant Empowered by LLM, Hybrid RAG and Abbreviation De-hallucination](https://arxiv.org/abs/2406.06575)** · arXiv · LLM · Training-free
- **["Not Aligned" is Not "Malicious": Being Careful about Hallucinations of Large Language Models' Jailbreak](https://arxiv.org/abs/2406.11668)** · arXiv · LLM · Training-free
- **[TofuEval: Evaluating Hallucinations of LLMs on Topic-Focused Dialogue Summarization](https://doi.org/10.18653/v1/2024.naacl-long.251)** · NAACL 2024 · LLM · Training-free
- **[Reducing hallucination in structured outputs via Retrieval-Augmented Generation](https://doi.org/10.18653/v1/2024.naacl-industry.19)** · NAACL 2024 · LLM · Training-free
- **[ReEval: Automatic Hallucination Evaluation for Retrieval-Augmented Large Language Models via Transferable Adversarial Attacks](https://doi.org/10.18653/v1/2024.findings-naacl.85)** · NAACL 2024 · LLM · Training-free
- **[PoLLMgraph: Unraveling Hallucinations in Large Language Models via State Transition Dynamics](https://doi.org/10.18653/v1/2024.findings-naacl.294)** · NAACL 2024 · LLM · Training-free
- **[On Large Language Models' Hallucination with Regard to Known Facts](https://doi.org/10.18653/v1/2024.naacl-long.60)** · NAACL 2024 · LLM · Training-free
- **[On Large Language Models&apos; Hallucination with Regard to Known Facts](https://doi.org/10.18653/v1/2024.naacl-long.60)** · NAACL 2024 · LLM · Training-free
- **[Mitigating Hallucination in Abstractive Summarization with Domain-Conditional Mutual Information](https://doi.org/10.18653/v1/2024.findings-naacl.117)** · NAACL 2024 · LLM · Training-free
- **[Hallucination Diversity-Aware Active Learning for Text Summarization](https://doi.org/10.18653/v1/2024.naacl-long.479)** · NAACL 2024 · LLM · Training-free
- **[Deceptive Semantic Shortcuts on Reasoning Chains: How Far Can Models Go without Hallucination?](https://doi.org/10.18653/v1/2024.naacl-long.424)** · NAACL 2024 · LLM · Training-free
- **📚 [Can Knowledge Graphs Reduce Hallucinations in LLMs? : A Survey](https://doi.org/10.18653/v1/2024.naacl-long.219)** · NAACL 2024 · LLM · Training-free
- **[ALOHa: A New Measure for Hallucination in Captioning Models](https://doi.org/10.18653/v1/2024.naacl-short.30)** · NAACL 2024 · LLM · Training-free
- **📋 [RefChecker: Reference-based Fine-grained Hallucination Checker and Benchmark for Large Language Models](https://arxiv.org/abs/2405.14486)** · arXiv · LLM · Training-free
- **[Mitigating LLM Hallucinations via Conformal Abstention](https://arxiv.org/abs/2405.01563)** · arXiv · LLM · Training-free
- **[Mitigating Hallucinations in Large Language Models via Self-Refinement-Enhanced Knowledge Retrieval](https://arxiv.org/abs/2405.06545)** · arXiv · LLM · Training-free
- **[Hallucination-Free? Assessing the Reliability of Leading AI Legal Research Tools](https://arxiv.org/abs/2405.20362)** · arXiv · LLM · Training-free
- **[Detecting Hallucinations in Large Language Model Generation: A Token Probability Approach](https://arxiv.org/abs/2405.19648)** · arXiv · LLM · Training-free
- **[Can a Hallucinating Model help in Reducing Human "Hallucination"?](https://arxiv.org/abs/2405.00843)** · arXiv · LLM · Training-free
- **[Addressing Topic Granularity and Hallucination in Large Language Models for Topic Modelling](https://arxiv.org/abs/2405.00611)** · arXiv · LLM · Training-free
- **[Uncertainty-Based Abstention in LLMs Improves Safety and Reduces Hallucinations](https://arxiv.org/abs/2404.10960)** · arXiv · LLM · Training-free
- **📋 [The Hallucinations Leaderboard -- An Open Effort to Measure Hallucinations in Large Language Models](https://arxiv.org/abs/2404.05904)** · arXiv · LLM · Training-free
- **[MetaCheckGPT -- A Multi-task Hallucination Detector Using LLM Uncertainty and Meta-models](https://arxiv.org/abs/2404.06948)** · arXiv · LLM · Training-free
- **[KnowHalu: Hallucination Detection via Multi-Form Knowledge Based Factual Checking](https://arxiv.org/abs/2404.02935)** · arXiv · LLM · Training-free
- **[Fakes of Varying Shades: How Warning Affects Human Perception and Engagement Regarding LLM Hallucinations](https://arxiv.org/abs/2404.03745)** · arXiv · LLM · Training-free
- **[Constructing Benchmarks and Interventions for Combating Hallucinations in LLMs](https://arxiv.org/abs/2404.09971)** · arXiv · LLM · Training-free
- **[Benchmarking Llama2, Mistral, Gemma and GPT for Factuality, Toxicity, Bias and Propensity for Hallucinations](https://arxiv.org/abs/2404.09785)** · arXiv · LLM · Training-free
- **[A robust and scalable framework for hallucination detection in virtual tissue staining and digital pathology](https://arxiv.org/abs/2404.18458)** · arXiv · LLM · Training-free
- **📚 [A Survey of Automatic Hallucination Evaluation on Natural Language Generation](https://arxiv.org/abs/2404.12041)** · arXiv · LLM · Training-free
- **[Tell Your Model Where to Attend: Post-hoc Attention Steering for LLMs](https://openreview.net/forum?id=xZDWO0oejD)** · ICLR 2024 · LLM · Training-free
- **[Instructive Decoding: Instruction-Tuned Large Language Models are Self-Refiner from Noisy Instructions](https://openreview.net/forum?id=LebzzClHYw)** · ICLR 2024 · LLM · Training-free
- **[INSIDE: LLMs' Internal States Retain the Power of Hallucination Detection](https://openreview.net/forum?id=Zj12nzlQbz)** · ICLR 2024 · LLM · Training-free
- **[DoLa: Decoding by Contrasting Layers Improves Factuality in Large Language Models](https://openreview.net/forum?id=Th6NyL07na)** · ICLR 2024 · LLM · Training-free
- **[Alleviating Hallucinations Via Supportive Window Indexing in Abstractive Summarization](https://doi.org/10.1109/ICASSP48485.2024.10446022)** · ICASSP 2024 · LLM · Training-free
- **[Zero-Shot Multi-task Hallucination Detection](https://arxiv.org/abs/2403.12244)** · arXiv · LLM · Training-free
- **[Using Hallucinations to Bypass GPT4's Filter](https://arxiv.org/abs/2403.04769)** · arXiv · LLM · Training-free
- **[HaluEval-Wild: Evaluating Hallucinations of Language Models in the Wild](https://arxiv.org/abs/2403.04307)** · arXiv · LLM · Training-free
- **[FACTOID: FACtual enTailment fOr hallucInation Detection](https://arxiv.org/abs/2403.19113)** · arXiv · LLM · Training-free
- **[Enhancing LLM Factual Accuracy with RAG to Counter Hallucinations: A Case Study on Domain-Specific Queries in Private Knowledge-Bases](https://arxiv.org/abs/2403.10446)** · arXiv · LLM · Training-free
- **[DiffMAC: Diffusion Manifold Hallucination Correction for High Generalization Blind Face Restoration](https://arxiv.org/abs/2403.10098)** · arXiv · LLM · Training-free
- **["Sorry, Come Again?" Prompting -- Enhancing Comprehension and Diminishing Hallucination with \[PAUSE\]-injected Optimal Paraphrasing](https://arxiv.org/abs/2403.18976)** · arXiv · LLM · Training-free
- **[Mitigating Hallucinations and Off-target Machine Translation with Source-Contrastive and Language-Contrastive Decoding](https://doi.org/10.18653/v1/2024.eacl-short.4)** · EACL 2024 · LLM · Training-free
- **📋 [HypoTermQA: Hypothetical Terms Dataset for Benchmarking Hallucination Tendency of LLMs](https://doi.org/10.18653/v1/2024.eacl-srw.9)** · EACL 2024 · LLM · Training-free
- **[Contrastive Decoding Reduces Hallucinations in Large Multilingual Machine Translation Models](https://doi.org/10.18653/v1/2024.eacl-long.155)** · EACL 2024 · LLM · Training-free
- **[Ask, Assess, and Refine: Rectifying Factual Consistency and Hallucination in LLMs with Metric-Guided Feedback Learning](https://doi.org/10.18653/v1/2024.eacl-long.149)** · EACL 2024 · LLM · Training-free
- **[Reducing Hallucinations in Entity Abstract Summarization with Facts-Template Decomposition](https://arxiv.org/abs/2402.18873)** · arXiv · LLM · Training-free
- **[Redefining "Hallucination" in LLMs: Towards a psychology-informed framework for mitigating misinformation](https://arxiv.org/abs/2402.01769)** · arXiv · LLM · Training-free
- **[Measuring and Reducing LLM Hallucination without Gold-Standard Answers](https://arxiv.org/abs/2402.10412)** · arXiv · LLM · Training-free
- **[Hallucinations or Attention Misdirection? The Path to Strategic Value Extraction in Business Using Large Language Models](https://arxiv.org/abs/2402.14002)** · arXiv · LLM · Training-free
- **[Do LLMs Know about Hallucination? An Empirical Investigation of LLM's Hidden States](https://arxiv.org/abs/2402.09733)** · arXiv · LLM · Training-free
- **[Comparing Hallucination Detection Metrics for Multilingual Generation](https://arxiv.org/abs/2402.10496)** · arXiv · LLM · Training-free
- **📚 [A Survey on Large Language Model Hallucination via a Creativity Perspective](https://arxiv.org/abs/2402.06647)** · arXiv · LLM · Training-free
- **[Mitigating Large Language Model Hallucinations via Autonomous Knowledge Graph-Based Retrofitting](https://doi.org/10.1609/aaai.v38i16.29770)** · AAAI 2024 · LLM · Training-free
- **[Navigating Uncertainty: Optimizing API Dependency for Hallucination Reduction in Closed-Book Question Answering](https://arxiv.org/abs/2401.01780)** · arXiv · LLM · Training-free
- **📚 [LightHouse: A Survey of AGI Hallucination](https://arxiv.org/abs/2401.06792)** · arXiv · LLM · Training-free
- **[Learning to Trust Your Feelings: Leveraging Self-awareness in LLMs for Hallucination Mitigation](https://arxiv.org/abs/2401.15449)** · arXiv · LLM · Training-free
- **[Large Legal Fictions: Profiling Legal Hallucinations in Large Language Models](https://arxiv.org/abs/2401.01301)** · arXiv · LLM · Training-free
- **[Hallucination is Inevitable: An Innate Limitation of Large Language Models](https://arxiv.org/abs/2401.11817)** · arXiv · LLM · Training-free
- **[Hallucination Detection and Hallucination Mitigation: An Investigation](https://arxiv.org/abs/2401.08358)** · arXiv · LLM · Training-free
- **[Fine-grained Hallucination Detection and Editing for Language Models](https://arxiv.org/abs/2401.06855)** · arXiv · LLM · Training-free
- **📚 [A Comprehensive Survey of Hallucination Mitigation Techniques in Large Language Models](https://arxiv.org/abs/2401.01313)** · arXiv · LLM · Training-free
- **[Self-contradictory Hallucinations of Large Language Models: Evaluation, Detection and Mitigation](https://openreview.net/forum?id=EmQSOi1X2f)** · Unlabeled · LLM · Training-free
- **[Looks Too Good To Be True: An Information-Theoretic Analysis of Hallucinations in Generative Restoration Models](http://papers.nips.cc/paper_files/paper/2024/hash/2847d43f17410c5beb25b2736c3ae778-Abstract-Conference.html)** · Unlabeled · LLM · Training-free
- **[Leveraging Hallucinations to Reduce Manual Prompt Dependency in Promptable Segmentation](http://papers.nips.cc/paper_files/paper/2024/hash/c1e1ad233411e25b54bb5df3a0576c2c-Abstract-Conference.html)** · Unlabeled · LLM · Training-free
- **[INSIDE: LLMs&apos; Internal States Retain the Power of Hallucination Detection](https://openreview.net/forum?id=Zj12nzlQbz)** · Unlabeled · LLM · Training-free
- **[How Language Model Hallucinations Can Snowball](https://proceedings.mlr.press/v235/zhang24ay.html)** · Unlabeled · LLM · Training-free
- **[HaloScope: Harnessing Unlabeled LLM Generations for Hallucination Detection](http://papers.nips.cc/paper_files/paper/2024/hash/ba92705991cfbbcedc26e27e833ebbae-Abstract-Conference.html)** · Unlabeled · LLM · Training-free
- **[Explicitly Stating Assumptions Reduces Hallucinations in Natural Language Inference](https://openreview.net/forum?id=eJI9pfNwBS)** · Unlabeled · LLM · Training-free
- **[Estimating the Hallucination Rate of Generative AI](http://papers.nips.cc/paper_files/paper/2024/hash/3791f5fc0e8e43730466afd2bcdb7493-Abstract-Conference.html)** · Unlabeled · LLM · Training-free
- **📋 [ERBench: An Entity-Relationship based Automatically Verifiable Hallucination Benchmark for Large Language Models](http://papers.nips.cc/paper_files/paper/2024/hash/5ef9853a6cdea40ae3e301a6d8dc32b5-Abstract-Datasets_and_Benchmarks_Track.html)** · Unlabeled · LLM · Training-free
- **[Coarse-to-Fine Highlighting: Reducing Knowledge Hallucination in Large Language Models](https://proceedings.mlr.press/v235/lv24c.html)** · Unlabeled · LLM · Training-free
- **[Utilizing GPT to Enhance Text Summarization: A Strategy to Minimize Hallucinations](https://doi.org/10.1016/j.procs.2024.10.197)** · ACLING 2024 · LLM · Training-free
- **[Using Laplace Transform To Optimize the Hallucination of Generation Models](https://doi.org/10.1109/ICARCV63323.2024.10821684)** · ICARCV 2024 · LLM · Training-free
- **[UMUTeam at SemEval-2024 Task 6: Leveraging Zero-Shot Learning for Detecting Hallucinations and Related Observable Overgeneration Mistakes](https://doi.org/10.18653/v1/2024.semeval-1.98)** · SemEval@NAACL 2024 · LLM · Training-free
- **[The Two Sides of the Coin: Hallucination Generation and Detection with LLMs as Evaluators for LLMs](https://ceur-ws.org/Vol-3740/paper-71.pdf)** · CLEF 2024 · LLM · Training-free
- **[The Problem of AI Hallucination and How to Solve It](https://doi.org/10.34190/ecel.23.1.2584)** · European Conference on e-Learning 2024 · LLM · Training-free
- **[The Pitfalls of Defining Hallucination](https://doi.org/10.1162/coli_a_00509)** · Comput. Linguistics 2024 · LLM · Training-free
- **[The Effects of Hallucinations in Synthetic Training Data for Relation Extraction](https://ceur-ws.org/Vol-3853/paper4.pdf)** · KBC-LM/LM-KBC@ISWC 2024 · LLM · Training-free
- **[TU Wien at SemEval-2024 Task 6: Unifying Model-Agnostic and Model-Aware Techniques for Hallucination Detection](https://doi.org/10.18653/v1/2024.semeval-1.173)** · SemEval@NAACL 2024 · LLM · Training-free
- **[SmurfCat at SemEval-2024 Task 6: Leveraging Synthetic Data for Hallucination Detection](https://doi.org/10.18653/v1/2024.semeval-1.125)** · SemEval@NAACL 2024 · LLM · Training-free
- **[SemEval-2024 Task 6: SHROOM, a Shared-task on Hallucinations and Related Observable Overgeneration Mistakes](https://doi.org/10.18653/v1/2024.semeval-1.273)** · SemEval@NAACL 2024 · LLM · Training-free
- **[SemEval-2024 Shared Task 6: SHROOM, a Shared-task on Hallucinations and Related Observable Overgeneration Mistakes](https://doi.org/10.18653/v1/2024.semeval-1.273)** · SemEval@NAACL 2024 · LLM · Training-free
- **[SLPL SHROOM at SemEval2024 Task 06 : A comprehensive study on models ability to detect hallucination](https://doi.org/10.18653/v1/2024.semeval-1.167)** · SemEval@NAACL 2024 · LLM · Training-free
- **[SHROOM-INDElab at SemEval-2024 Task 6: Zero- and Few-Shot LLM-Based Classification for Hallucination Detection](https://doi.org/10.18653/v1/2024.semeval-1.120)** · SemEval@NAACL 2024 · LLM · Training-free
- **[OPDAI at SemEval-2024 Task 6: Small LLMs can Accelerate Hallucination Detection with Weakly Supervised Data](https://doi.org/10.18653/v1/2024.semeval-1.104)** · SemEval@NAACL 2024 · LLM · Training-free
- **📋 [OAEI-LLM: A Benchmark Dataset for Understanding Large Language Model Hallucinations in Ontology Matching](https://ceur-ws.org/Vol-3953/361.pdf)** · HGAIS@ISWC 2024 · LLM · Training-free
- **[NootNoot At SemEval-2024 Task 6: Hallucinations and Related Observable Overgeneration Mistakes Detection](https://doi.org/10.18653/v1/2024.semeval-1.139)** · SemEval@NAACL 2024 · LLM · Training-free
- **[NU-RU at SemEval-2024 Task 6: Hallucination and Related Observable Overgeneration Mistake Detection Using Hypothesis-Target Similarity and SelfCheckGPT](https://doi.org/10.18653/v1/2024.semeval-1.39)** · SemEval@NAACL 2024 · LLM · Training-free
- **[Mitigating Hallucination in Large Language Model by Leveraging Decoder Layer Contrasting](https://doi.org/10.1007/978-3-031-78498-9_4)** · ICPR 2024 · LLM · Training-free
- **[Mitigating Hallucination Issues in Small-Parameter LLMs through Inter-Layer Contrastive Decoding](https://doi.org/10.1109/IJCNN60899.2024.10650644)** · IJCNN 2024 · LLM · Training-free
- **[Maha Bhaashya at SemEval-2024 Task 6: Zero-Shot Multi-task Hallucination Detection](https://doi.org/10.18653/v1/2024.semeval-1.241)** · SemEval@NAACL 2024 · LLM · Training-free
- **📋 [MASSIVE Multilingual Abstract Meaning Representation: A Dataset and Baselines for Hallucination Detection](https://doi.org/10.18653/v1/2024.starsem-1.1)** · 13th Joint Conference on Lexical and Computational Semantics (*SEM 2024) 2024 · LLM · Training-free
- **[MARiA at SemEval 2024 Task-6: Hallucination Detection Through LLMs, MNLI, and Cosine similarity](https://doi.org/10.18653/v1/2024.semeval-1.225)** · SemEval@NAACL 2024 · LLM · Training-free
- **[MALTO at SemEval-2024 Task 6: Leveraging Synthetic Data for LLM Hallucination Detection](https://doi.org/10.18653/v1/2024.semeval-1.240)** · SemEval@NAACL 2024 · LLM · Training-free
- **[LP-LM: No Hallucinations in Question Answering with Logic Programming](https://doi.org/10.4204/EPTCS.416.5)** · ICLP 2024 · LLM · Training-free
- **[LLMs Can Check Their Own Results to Mitigate Hallucinations in Traffic Understanding Tasks](https://doi.org/10.1007/978-3-031-80889-0_8)** · ICTSS 2024 · LLM · Training-free
- **[LLM Internal States Reveal Hallucination Risk Faced With a Query](https://doi.org/10.18653/v1/2024.blackboxnlp-1.6)** · NN 2024 · LLM · Training-free
- **[IRIT-Berger-Levrault at SemEval-2024: How Sensitive Sentence Embeddings are to Hallucinations?](https://doi.org/10.18653/v1/2024.semeval-1.86)** · SemEval@NAACL 2024 · LLM · Training-free
- **[Halwasa: Quantify and Analyze Hallucinations in Large Language Models: Arabic as a Case Study](https://aclanthology.org/2024.lrec-main.705)** · LREC/COLING 2024 · LLM · Training-free
- **[Halu-NLP at SemEval-2024 Task 6: MetaCheckGPT - A Multi-task Hallucination Detection using LLM uncertainty and meta-models](https://doi.org/10.18653/v1/2024.semeval-1.52)** · SemEval@NAACL 2024 · LLM · Training-free
- **[HalluSafe at SemEval-2024 Task 6: An NLI-based Approach to Make LLMs Safer by Better Detecting Hallucinations and Overgeneration Mistakes](https://doi.org/10.18653/v1/2024.semeval-1.22)** · SemEval@NAACL 2024 · LLM · Training-free
- **[HaRMoNEE at SemEval-2024 Task 6: Tuning-based Approaches to Hallucination Recognition](https://doi.org/10.18653/v1/2024.semeval-1.191)** · SemEval@NAACL 2024 · LLM · Training-free
- **[HIT-MI&amp;T Lab at SemEval-2024 Task 6: DeBERTa-based Entailment Model is a Reliable Hallucination Detector](https://doi.org/10.18653/v1/2024.semeval-1.253)** · 18th International Workshop on Semantic Evaluation (SemEval-2024) 2024 · LLM · Training-free
- **[GraphEval: A Knowledge-Graph Based LLM Hallucination Evaluation Framework](https://ceur-ws.org/Vol-3894/paper5.pdf)** · KiL@KDD 2024 · LLM · Training-free
- **📋 [German also Hallucinates! Inconsistency Detection in News Summaries with the Absinth Dataset](https://aclanthology.org/2024.lrec-main.680)** · LREC/COLING 2024 · LLM · Training-free
- **[Exploring the Knowledge Mismatch Hypothesis: Hallucination Propensity in Small Models Fine-tuned on Data from Larger Models](https://doi.org/10.1109/BDCAT63179.2024.00048)** · BDCAT 2024 · LLM · Training-free
- **[Evaluating the Effects of Prompt Perturbation on Bias and Hallucination in Large Language Models](https://doi.org/10.1007/978-981-96-6588-4_25)** · ICONIP 2024 · LLM · Training-free
- **[Evaluating Hallucination in Medical Prompt Responses: A Comparative Study of ChatGPT-4 and ChatGPT-4o](https://doi.org/10.1109/comnetsat63286.2024.10862480)** · IEEE International Conference on Communication, Networks and Satellite (COMNETSAT) 2024 · LLM · Training-free
- **[Enhancing Knowledge Graph Construction: Evaluating with Emphasis on Hallucination, Omission, and Graph Similarity Metrics](https://doi.org/10.1007/978-3-031-81221-7_3)** · KGSWC 2024 · LLM · Training-free
- **📋 [Detection, Diagnosis, and Explanation: A Benchmark for Chinese Medial Hallucination Evaluation](https://aclanthology.org/2024.lrec-main.428)** · LREC/COLING 2024 · LLM · Training-free
- **[Detecting Hallucination and Coverage Errors in Retrieval Augmented Generation for Controversial Topics](https://aclanthology.org/2024.lrec-main.423)** · LREC/COLING 2024 · LLM · Training-free
- **[DeepPavlov at SemEval-2024 Task 6: Detection of Hallucinations and Overgeneration Mistakes with an Ensemble of Transformer-based Models](https://doi.org/10.18653/v1/2024.semeval-1.42)** · SemEval@NAACL 2024 · LLM · Training-free
- **[DUTh at SemEval-2024 Task 6: Comparing Pre-trained Models on Sentence Similarity Evaluation for Detecting of Hallucinations and Related Observable Overgeneration Mistakes](https://doi.org/10.18653/v1/2024.semeval-1.154)** · 18th International Workshop on Semantic Evaluation (SemEval-2024) 2024 · LLM · Training-free
- **[DAHRS: Divergence-Aware Hallucination-Remediated SRL Projection](https://doi.org/10.1007/978-3-031-70239-6_29)** · NLDB 2024 · LLM · Training-free
- **[Correcting Factuality Hallucination in Complaint Large Language Model via Entity-Augmented](https://doi.org/10.1109/IJCNN60899.2024.10650208)** · IJCNN 2024 · LLM · Training-free
- **[Compos Mentis at SemEval2024 Task6: A Multi-Faceted Role-based Large Language Model Ensemble to Detect Hallucination](https://doi.org/10.18653/v1/2024.semeval-1.208)** · SemEval@NAACL 2024 · LLM · Training-free
- **📚 [Cognitive Mirage: A Review of Hallucinations in Large Language Models](https://ceur-ws.org/Vol-3818/paper2.pdf)** · LKM@IJCAI 2024 · LLM · Training-free
- **[Can Hallucination Reduction in LLMs Improve Online Sexism Detection?](https://doi.org/10.1007/978-3-031-66329-1_40)** · Lecture Notes in Networks and Systems 2024 · LLM · Training-free
- **[CPR: Mitigating Large Language Model Hallucinations with Curative Prompt Refinement](https://doi.org/10.1109/SMC54092.2024.10830938)** · SMC 2024 · LLM · Training-free
- **[BrainLlama at SemEval-2024 Task 6: Prompting Llama to detect hallucinations and related observable overgeneration mistakes](https://doi.org/10.18653/v1/2024.semeval-1.14)** · SemEval@NAACL 2024 · LLM · Training-free
- **[Benchmarking Hallucination in Large Language Models Based on Unanswerable Math Word Problem](https://aclanthology.org/2024.lrec-main.196)** · LREC/COLING 2024 · LLM · Training-free
- **[AlphaIntellect at SemEval-2024 Task 6: Detection of Hallucinations in Generated Text](https://doi.org/10.18653/v1/2024.semeval-1.137)** · SemEval@NAACL 2024 · LLM · Training-free
- **[Alleviating Action Hallucination for LLM-based Embodied Agents via Inner and Outer Alignment](https://doi.org/10.1109/prai62207.2024.10826957)** · 7th International Conference on Pattern Recognition and Artificial Intelligence (PRAI) 2024 · LLM · Training-free
- **[AILS-NTUA at SemEval-2024 Task 6: Efficient model tuning for hallucination detection and analysis](https://doi.org/10.18653/v1/2024.semeval-1.222)** · 18th International Workshop on Semantic Evaluation (SemEval-2024) 2024 · LLM · Training-free
- **[AI Hallucinations: A Misnomer Worth Clarifying](https://doi.org/10.1109/CAI59869.2024.00033)** · CAI 2024 · LLM · Training-free
- **[A Culturally Sensitive Test to Evaluate Nuanced GPT Hallucination](https://doi.org/10.1109/TAI.2023.3332837)** · TAI 2024 · LLM · Training-free
- **[A Cause-Effect Look at Alleviating Hallucination of Knowledge-grounded Dialogue Generation](https://aclanthology.org/2024.lrec-main.9)** · LREC/COLING 2024 · LLM · Training-free

</details>

<details>
<summary>📅 2023 · 20 papers</summary>

- **[Towards Mitigating LLM Hallucination via Self Reflection](https://doi.org/10.18653/v1/2023.findings-emnlp.123)** · EMNLP 2023 · LLM · Training-free
- **[Sources of Hallucination by Large Language Models on Inference Tasks](https://doi.org/10.18653/v1/2023.findings-emnlp.182)** · EMNLP 2023 · LLM · Training-free
- **[SAC3: Reliable Hallucination Detection in Black-Box Language Models via Semantic-aware Cross-check Consistency: Reliable Hallucination Detection in Black-Box Language Models via Semantic-aware Cross-check Consistency](https://doi.org/10.18653/v1/2023.findings-emnlp.1032)** · EMNLP 2023 · LLM · Training-free
- **[KCTS: Knowledge-Constrained Tree Search Decoding with Token-Level Hallucination Detection](https://doi.org/10.18653/v1/2023.emnlp-main.867)** · EMNLP 2023 · LLM · Training-free
- **[Hallucination Detection for Grounded Instruction Generation](https://doi.org/10.18653/v1/2023.findings-emnlp.266)** · EMNLP 2023 · LLM · Training-free
- **📋 [HalOmi: A Manually Annotated Benchmark for Multilingual Hallucination and Omission Detection in Machine Translation](https://doi.org/10.18653/v1/2023.emnlp-main.42)** · EMNLP 2023 · LLM · Training-free
- **[Eyes Show the Way: Modelling Gaze Behaviour for Hallucination Detection](https://doi.org/10.18653/v1/2023.findings-emnlp.764)** · EMNLP 2023 · LLM · Training-free
- **[Critic-Driven Decoding for Mitigating Hallucinations in Data-to-text Generation](https://doi.org/10.18653/v1/2023.emnlp-main.172)** · EMNLP 2023 · LLM · Training-free
- **[CRUSH4SQL: Collective Retrieval Using Schema Hallucination For Text2SQL](https://doi.org/10.18653/v1/2023.emnlp-main.868)** · EMNLP 2023 · LLM · Training-free
- **📋 [A New Benchmark and Reverse Validation Method for Passage-level Hallucination Detection](https://doi.org/10.18653/v1/2023.findings-emnlp.256)** · EMNLP 2023 · LLM · Training-free
- **[Contrastive Decoding: Open-ended Text Generation as Optimization](https://doi.org/10.18653/v1/2023.acl-long.687)** · ACL 2023 · LLM · Training-free
- **[CaPE: Contrastive Parameter Ensembling for Reducing Hallucination in Abstractive Summarization](https://doi.org/10.18653/v1/2023.findings-acl.685)** · ACL 2023 · LLM · Training-free
- **[Looking for a Needle in a Haystack: A Comprehensive Study of Hallucinations in Neural Machine Translation](https://doi.org/10.18653/v1/2023.eacl-main.75)** · EACL 2023 · LLM · Training-free
- **[Contrastive Learning Reduces Hallucination in Conversations](https://doi.org/10.1609/aaai.v37i11.26596)** · AAAI 2023 · LLM · Training-free
- **[Untangling Emotional Threads: Hallucination Networks of Large Language Models](https://doi.org/10.1007/978-3-031-53468-3_17)** · COMPLEX NETWORKS 2023 · LLM · Training-free
- **[Towards reducing hallucination in extracting information from financial reports using Large Language Models](https://doi.org/10.1145/3639856.3639895)** · AIMLSystems 2023 · LLM · Training-free
- **[Med-HALT: Medical Domain Hallucination Test for Large Language Models](https://doi.org/10.18653/v1/2023.conll-1.21)** · CoNLL 2023 · LLM · Training-free
- **[Hallucination Detection: Robustly Discerning Reliable Answers in Large Language Models](https://doi.org/10.1145/3583780.3614905)** · CIKM 2023 · LLM · Training-free
- **[Detecting Dialogue Hallucination Using Graph Neural Networks](https://doi.org/10.1109/ICMLA58977.2023.00128)** · ICMLA 2023 · LLM · Training-free
- **[&quot;Why is this misleading?&quot;: Detecting News Headline Hallucinations with Explanations](https://doi.org/10.1145/3543507.3583375)** · WWW 2023 · LLM · Training-free

</details>

<details>
<summary>📅 2022 · 2 papers</summary>

- **[Hallucinated but Factual! Inspecting the Factuality of Hallucinations in Abstractive Summarization](https://doi.org/10.18653/v1/2022.acl-long.236)** · ACL 2022 · LLM · Training-free
- **[On the Origin of Hallucinations in Conversational Models: Is it the Datasets or the Models?](https://doi.org/10.18653/v1/2022.naacl-main.387)** · NAACL 2022 · LLM · Training-free

</details>

<details>
<summary>📅 2021 · 3 papers</summary>

- **[Retrieval Augmentation Reduces Hallucination in Conversation](https://doi.org/10.18653/v1/2021.findings-emnlp.320)** · EMNLP 2021 · LLM · Training-free
- **[The Curious Case of Hallucinations in Neural Machine Translation](https://doi.org/10.18653/v1/2021.naacl-main.92)** · NAACL 2021 · LLM · Training-free
- **[On Hallucination and Predictive Uncertainty in Conditional Language Generation](https://doi.org/10.18653/v1/2021.eacl-main.236)** · EACL 2021 · LLM · Training-free

</details>

<details>
<summary>📅 2020 · 1 papers</summary>

- **[Structural Hallucination in LLMs: A Formal Characterization and Mitigation Method](https://doi.org/10.36948/ijfmr.2020.v02i05.61072)** · International Journal For Multidisciplinary Research 2020 · LLM · Training-free

</details>

<details>
<summary>📅 2019 · 4 papers</summary>

- **[Sticking to the Facts: Confident Decoding for Faithful Data-to-Text Generation](https://arxiv.org/abs/1910.08684)** · arXiv · LLM · Training-free
- **[Assessing The Factual Accuracy of Generated Text](https://doi.org/10.1145/3292500.3330955)** · KDD 2019 · LLM · Training-free
- **[Ranking Generated Summaries by Correctness: An Interesting but Challenging Application for Natural Language Inference](https://doi.org/10.18653/v1/P19-1213)** · ACL 2019 · LLM · Training-free
- **[A Simple Recipe towards Reducing Hallucination in Neural Surface Realisation](https://doi.org/10.18653/v1/p19-1256)** · ACL 2019 · LLM · Training-free

</details>

</details>

<details>
<summary>👁️ VLM · 655 篇</summary>

<details>
<summary>📅 2026 · 265 papers</summary>

- **[See Only When Needed: Context-Aware Attention Intervention for Mitigating Hallucinations in LVLMs](https://arxiv.org/abs/2606.29847)** · ECCV 2026 · VLM · Training-free
- **[TruthLens: Object Hallucination Detection via Self-Evaluating Truthfulness Scores in LVLMs](https://arxiv.org/abs/2608.05616)** · arXiv · VLM · Training-based
- **[UHP Detection: LVLMs have their Unique Hallucination Pattern in the Consistency Space](https://arxiv.org/abs/2608.03817)** · arXiv · VLM · Training-free
- **📋 [KnowHal: A Knowledge-Driven Benchmark for Comprehensive Multimodal Hallucination Evaluation](https://arxiv.org/abs/2608.03782)** · arXiv · VLM · Training-free
- **[When Model Priors Conflict with Visual Evidence: Mitigating Commonsense-Driven Hallucinations by Selective Prior Calibration](https://arxiv.org/abs/2607.29240)** · arXiv · VLM · Training-free
- **[Role-Break in Attention Heads: Understanding and Detecting Hallucinations in VLMs](https://arxiv.org/abs/2607.29412)** · arXiv · VLM · Training-based
- **[Hallucinations Leave a Grounding Signature:Verifier-Guided Decoding for Selective Object Correction](https://arxiv.org/abs/2607.27823)** · arXiv · VLM · Training-free
- **[When Low CER is Not Enough: An Analysis of Hallucinations in Vision-Language OCR Systems on Historical Uruguayan Documents](https://arxiv.org/abs/2607.24077)** · arXiv · VLM · Training-free
- **[HALLELUAI: A Hallucination-Aware AI System for Ultra-Realistic Image-to-Video Generation at Scale](https://arxiv.org/abs/2607.22959)** · arXiv · VLM · Training-free
- **[Vera: Identity-Faithful Human Subject-to-Video Generation](https://arxiv.org/abs/2607.20247)** · arXiv · VLM · Training-free
- **[SeeMe: Mitigating Hallucinations in Large Vision-Language Models through Effective Visual Token Engineering](https://arxiv.org/abs/2607.04163)** · arXiv · VLM · Training-free
- **[ProCap: Prominence-guided Object Rectification for Faithful and Comprehensive Video Captioning](https://arxiv.org/abs/2607.21022)** · arXiv · VLM · Training-free
- **📋 [MoHallBench: A Benchmark for Motion Hallucination in Video Large Language Models](https://arxiv.org/abs/2607.01117)** · arXiv · VLM · Training-free
- **📋 [MissingBench-Verified: Probing Vision-Language Models' Inability to Detect Missing Object Parts](https://arxiv.org/abs/2607.18673)** · arXiv · VLM · Training-free
- **[Look Clearly Before Answering: Mitigating Hallucinations in LVLMs via Saliency-Driven Perceptual Realignment](https://arxiv.org/abs/2607.16841)** · arXiv · VLM · Training-free
- **📋 [HoloCount: A Holistic Visual Counting Benchmark for MLLMs](https://arxiv.org/abs/2607.06420)** · arXiv · VLM · Training-free
- **[HalluScope: Fine-grained Hallucination Diagnosis for Multimodal Large Language Models](https://arxiv.org/abs/2607.21105)** · arXiv · VLM · Training-free
- **[Hallo4D: Multi-Modal Hallucination Mitigation for Consistent Spatio-Temporal Generation](https://arxiv.org/abs/2607.12752)** · arXiv · VLM · Training-free
- **[HIVE: Understanding Post-Hallucination Reasoning in Vision Language Models](https://arxiv.org/abs/2607.07507)** · arXiv · VLM · Training-free
- **[Groc-PO: Grounded Context Preference Optimization for Truthful Multimodal LLMs](https://arxiv.org/abs/2607.13712)** · arXiv · VLM · Training-based
- **[Geo3R: Mitigating Spatial Reasoning Hallucination in Multimodal Large Language Models](https://arxiv.org/abs/2607.21085)** · arXiv · VLM · Training-free
- **[Do Medical Vision Language Models Actually See? A Counterfactual Grounding Framework and Hard-Negative Contrastive Training for Visually-Reliant Medical VLMs](https://arxiv.org/abs/2607.03647)** · arXiv · VLM · Training-free
- **[A Good Initialization is All You Need for Faithful Visual Attribution](https://arxiv.org/abs/2607.06726)** · arXiv · VLM · Training-free
- **[Vocabulary Hijacking in LVLMs: Unveiling Critical Attention Heads by Excluding Inert Tokens to Mitigate Hallucination](https://aclanthology.org/2026.acl-long.1782/)** · ACL 2026 · VLM · Training-free
- **[Vision-Language Introspection: Mitigating Overconfident Hallucinations in MLLMs via Interpretable Bi-Causal Steering](https://aclanthology.org/2026.acl-long.1784/)** · ACL 2026 · VLM · Training-free
- **[VIB-Probe: Detecting and Mitigating Hallucinations in Vision-Language Models via Variational Information Bottleneck](https://aclanthology.org/2026.acl-long.1078/)** · ACL 2026 · VLM · Training-free
- **[Towards Mitigating Hallucinations in Large Vision-Language Models by Refining Textual Embeddings](https://aclanthology.org/2026.findings-acl.2086/)** · ACL 2026 · VLM · Training-free
- **[Through the Magnifying Glass: Adaptive Perception Magnification for Hallucination-Free VLM Decoding](https://aclanthology.org/2026.acl-long.2059/)** · ACL 2026 · VLM · Training-free
- **[Spotlight and Shadow: Attention-Guided Dual-Anchor Introspective Decoding for MLLM Hallucination Mitigation](https://aclanthology.org/2026.findings-acl.646/)** · ACL 2026 · VLM · Training-free
- **[Revealing and Enhancing Core Visual Regions: Harnessing Internal Attention Dynamics for Hallucination Mitigation in LVLMs](https://aclanthology.org/2026.findings-acl.748/)** · ACL 2026 · VLM · Training-free
- **[Perceptual Hallucination in Vision-Language Models: Definition, Analysis and Verification](https://aclanthology.org/2026.findings-acl.1237/)** · ACL 2026 · VLM · Training-free
- **[Once Correct, Still Wrong: Counterfactual Hallucination in Multilingual Vision-Language Models](https://aclanthology.org/2026.findings-acl.234/)** · ACL 2026 · VLM · Training-free
- **[Mitigating Hallucinations in VLMs: Enhancing Visual Attention via Head-Wise Perturbation](https://aclanthology.org/2026.findings-acl.1016/)** · ACL 2026 · VLM · Training-free
- **[Mitigating Hallucinations in Large Vision-Language Models without Performance Degradation](https://aclanthology.org/2026.acl-long.89/)** · ACL 2026 · VLM · Training-free
- **[Mitigating Action-Relation Hallucinations in LVLMs via Relation-aware Visual Enhancement](https://aclanthology.org/2026.acl-long.1142/)** · ACL 2026 · VLM · Training-free
- **[Mechanisms of Prompt-Induced Hallucination in Vision-Language Models](https://aclanthology.org/2026.acl-long.1941/)** · ACL 2026 · VLM · Training-free
- **[Latent Attention Denoising: A Training-Free Energy-Based Framework for Mitigating Hallucinations in Vision-Language Models](https://aclanthology.org/2026.acl-long.1327/)** · ACL 2026 · VLM · Training-free
- **[Inject to Heal: Alleviating hallucination in LVLMs via Context Embedding Injection](https://aclanthology.org/2026.findings-acl.2048/)** · ACL 2026 · VLM · Training-free
- **📋 [INFACT: A Diagnostic Benchmark for Induced Faithfulness and Factuality Hallucinations in Video-LLMs](https://aclanthology.org/2026.acl-long.2062/)** · ACL 2026 · VLM · Training-free
- **[Global Context or Local Detail? Adaptive Visual Grounding for Hallucination Mitigation](https://aclanthology.org/2026.findings-acl.745/)** · ACL 2026 · VLM · Training-free
- **📚 [Distorted or Fabricated? A Survey on Hallucination in Video LLMs](https://aclanthology.org/2026.findings-acl.1325/)** · ACL 2026 · VLM · Training-free
- **[DiVE: Decoupling Intra-layer Visual Evidence for Mitigating Hallucinations in Large Vision-Language Models](https://aclanthology.org/2026.acl-long.1742/)** · ACL 2026 · VLM · Training-free
- **[Correcting Visual Blur Induced by Attention Distraction to Reduce Hallucinations: Algorithm and Theory](https://arxiv.org/abs/2605.24602)** · ICML 2026 · VLM · Training-free
- **[CEBC: Conformal Evidence-Bounded Control for Low-Hallucination Vision-Language Generation](https://aclanthology.org/2026.acl-long.2142/)** · ACL 2026 · VLM · Training-free
- **[CCD: Mitigating Hallucinations in Radiology MLLMs via Clinical Contrastive Decoding](https://aclanthology.org/2026.findings-acl.1755/)** · ACL 2026 · VLM · Training-free
- **[Benchmarking Deflection and Hallucination in Large Vision-Language Models](https://aclanthology.org/2026.acl-long.1307/)** · ACL 2026 · VLM · Training-free
- **[Aligning with Your Own Voice: Self-Corrected Preference Learning for Hallucination Mitigation in LVLMs](https://aclanthology.org/2026.findings-acl.1784/)** · ACL 2026 · VLM · Training-based
- **[AHEAD: Attention Head Energy-Aware Dynamics for Hallucination Mitigation in MLLMs](https://aclanthology.org/2026.findings-acl.425/)** · ACL 2026 · VLM · Training-free
- **[Vision-driven Preference Synthesis for Mitigating Hallucinations in VLMs](https://arxiv.org/abs/2606.28401)** · arXiv · VLM · Training-free
- **[TIGER: Traceable Inference with Graph-Based Evidence Routing for Mitigating Hallucinations in Multimodal Generation](https://arxiv.org/abs/2606.00232)** · arXiv · VLM · Training-free
- **[TAVR-VLM: Risk-Conditioned Causal Grounding for Hallucination-Resistant Report Generation](https://arxiv.org/abs/2606.26874)** · arXiv · VLM · Training-free
- **[Steer Where It Matters: Token-Level Visual-Sensitivity Steering for LVLMs Hallucination Mitigation](https://arxiv.org/abs/2606.07647)** · arXiv · VLM · Training-free
- **[Staying VIGILant: Mitigating Visual Laziness via Counterfactual Visual Alignment in MLLMs](https://arxiv.org/abs/2606.26387)** · arXiv · VLM · Training-free
- **[Spectral Query-Key Product Weight Steering for Training-Free VLM Hallucination Mitigation](https://arxiv.org/abs/2606.20419)** · arXiv · VLM · Training-free
- **📋 [SAGE: An Expert-Annotated South Asian GI Endoscopy Dataset for Multimodal Learning and Hallucination Analysis](https://arxiv.org/abs/2606.22144)** · arXiv · VLM · Training-free
- **[No Place to Hide: Benchmarking Video Hallucination with Background-Controlled Pairs](https://arxiv.org/abs/2606.31933)** · arXiv · VLM · Training-free
- **[MultiToP: Learning to Patch Visual Tokens to Mitigate Hallucinations in Video Large Multimodal Models](https://arxiv.org/abs/2606.11792)** · arXiv · VLM · Training-free
- **[Mitigating Visual Hallucinations in Multimodal Systems through Retrieval-Augmented Reliability-Aware Inference](https://arxiv.org/abs/2606.15782)** · arXiv · VLM · Training-free
- **📋 [MedBench v5: A Dynamic, Process-Oriented, and Hallucination-Aware Benchmark for Clinical Multimodal Models](https://arxiv.org/abs/2606.24155)** · arXiv · VLM · Training-free
- **[MM-Snowball: Evaluating and Mitigating Hallucination Snowballing in Multimodal Multi-Turn Dialogue](https://arxiv.org/abs/2606.00622)** · arXiv · VLM · Training-free
- **[How Many Counterfactuals Does It Take? Probing VLM Hallucinations Through Circuits and Causal Effects](https://arxiv.org/abs/2606.08777)** · arXiv · VLM · Training-free
- **[Hallucination Detection and Correction in Medical VLMs via Counter-Evidence Verification](https://arxiv.org/abs/2606.18609)** · arXiv · VLM · Training-free
- **[From Hallucination to Grounding: Diagnosing Visual Spatial Intelligence via CRISP](https://arxiv.org/abs/2606.26535)** · arXiv · VLM · Training-free
- **[FADE: Mitigating Hallucinations by Reducing Language-Prior Dominance in Large Vision-Language Models](https://arxiv.org/abs/2606.29431)** · arXiv · VLM · Training-free
- **[Detecting Clinical Hallucinations in LVLMs via Counterfactual Visual Grounding Uncertainty](https://arxiv.org/abs/2606.28520)** · arXiv · VLM · Training-free
- **[Density Ridge Selective Prediction for LLM and VLM Hallucination Detection under Calibration Label Scarcity](https://arxiv.org/abs/2606.10198)** · arXiv · VLM · Training-free
- **📋 [ClinHallu: A Benchmark for Diagnosing Stage-Wise Hallucinations in Medical MLLM Reasoning](https://arxiv.org/abs/2606.14697)** · arXiv · VLM · Training-free
- **[Clearer Sight, Fewer Lies: Oriented Pickup Preference Optimization for Multimodal Hallucination Mitigation](https://arxiv.org/abs/2606.29805)** · arXiv · VLM · Training-based
- **📋 [A Benchmark for Hallucination Detection in VLMs for Gastrointestinal Endoscopy](https://arxiv.org/abs/2606.24115)** · arXiv · VLM · Training-free
- **[ZINA: Multimodal Fine-grained Hallucination Detection and Editing](https://openaccess.thecvf.com/content/CVPR2026/html/Wada_ZINA_Multimodal_Fine-grained_Hallucination_Detection_and_Editing_CVPR_2026_paper.html)** · CVPR 2026 · VLM · Training-free
- **[VES-RFT: Rewarding Visual Evidence Sensitivity to Mitigate Hallucinations in Large Vision-Language Models](https://openaccess.thecvf.com/content/CVPR2026/html/Hou_VES-RFT_Rewarding_Visual_Evidence_Sensitivity_to_Mitigate_Hallucinations_in_Large_CVPR_2026_paper.html)** · CVPR 2026 · VLM · Training-free
- **[Unstitching the Chimera: Frame-Level Risk and Train-Free Mitigation for Video Hallucination](https://openaccess.thecvf.com/content/CVPR2026/html/Yang_Unstitching_the_Chimera_Frame-Level_Risk_and_Train-Free_Mitigation_for_Video_CVPR_2026_paper.html)** · CVPR 2026 · VLM · Training-free
- **[Understanding the Role of Hallucination in Reinforcement Post-Training of Multimodal Reasoning Models](https://openaccess.thecvf.com/content/CVPR2026/html/Zhang_Understanding_the_Role_of_Hallucination_in_Reinforcement_Post-Training_of_Multimodal_CVPR_2026_paper.html)** · CVPR 2026 · VLM · Training-based
- **[Understanding and Mitigating Hallucinations in Multimodal Chain-of-Thought Models](https://openaccess.thecvf.com/content/CVPR2026/html/Ma_Understanding_and_Mitigating_Hallucinations_in_Multimodal_Chain-of-Thought_Models_CVPR_2026_paper.html)** · CVPR 2026 · VLM · Training-free
- **[Thinking in Uncertainty: Mitigating Hallucinations in MLRMs with Latent Entropy-Aware Decoding](https://openaccess.thecvf.com/content/CVPR2026/html/Xu_Thinking_in_Uncertainty_Mitigating_Hallucinations_in_MLRMs_with_Latent_Entropy-Aware_CVPR_2026_paper.html)** · CVPR 2026 · VLM · Training-free
- **[Tell Model Where to Look: Mitigating Hallucinations in MLLMs by Vision-Guided Attention](https://openaccess.thecvf.com/content/CVPR2026/html/Zhao_Tell_Model_Where_to_Look_Mitigating_Hallucinations_in_MLLMs_by_CVPR_2026_paper.html)** · CVPR 2026 · VLM · Training-free
- **[Same Attention, Different Truths: Put Logit-Lens over Visual Attention to Detect and Mitigate LVLM Object Hallucination](https://openaccess.thecvf.com/content/CVPR2026/html/Wang_Same_Attention_Different_Truths_Put_Logit-Lens_over_Visual_Attention_to_CVPR_2026_paper.html)** · CVPR 2026 · VLM · Training-free
- **[SEASON: Mitigating Temporal Hallucination in Video Large Language Models via Self-Diagnostic Contrastive Decoding](https://openaccess.thecvf.com/content/CVPR2026/html/Wu_SEASON_Mitigating_Temporal_Hallucination_in_Video_Large_Language_Models_via_CVPR_2026_paper.html)** · CVPR 2026 · VLM · Training-free
- **[Residual Decoding: Mitigating Hallucinations in Large Vision-Language Models via History-Aware Residual Guidance](https://openaccess.thecvf.com/content/CVPR2026/html/Chen_Residual_Decoding_Mitigating_Hallucinations_in_Large_Vision-Language_Models_via_History-Aware_CVPR_2026_paper.html)** · CVPR 2026 · VLM · Training-free
- **[Reallocating Attention Across Layers to Reduce Multimodal Hallucination](https://openaccess.thecvf.com/content/CVPR2026/html/Lu_Reallocating_Attention_Across_Layers_to_Reduce_Multimodal_Hallucination_CVPR_2026_paper.html)** · CVPR 2026 · VLM · Training-free
- **[Prefill-Time Intervention for Mitigating Hallucination in Large Vision-Language Models](https://openaccess.thecvf.com/content/CVPR2026/html/Zhang_Prefill-Time_Intervention_for_Mitigating_Hallucination_in_Large_Vision-Language_Models_CVPR_2026_paper.html)** · CVPR 2026 · VLM · Training-free
- **[PAS : Prelim Attention Score for Detecting Object Hallucinations in Large Vision--Language Models](https://openaccess.thecvf.com/content/CVPR2026/html/Hoang_PAS_Prelim_Attention_Score_for_Detecting_Object_Hallucinations_in_Large_CVPR_2026_paper.html)** · CVPR 2026 · VLM · Training-free
- **[One Token, Two Fates: A Unified Framework via Vision Token Manipulation Against MLLMs Hallucination](https://openaccess.thecvf.com/content/CVPR2026/html/Fa_One_Token_Two_Fates_A_Unified_Framework_via_Vision_Token_CVPR_2026_paper.html)** · CVPR 2026 · VLM · Training-free
- **[Mitigating Multimodal Hallucinations via Gradient-based Self-Reflection](https://openaccess.thecvf.com/content/CVPR2026/html/Wang_Mitigating_Multimodal_Hallucinations_via_Gradient-based_Self-Reflection_CVPR_2026_paper.html)** · CVPR 2026 · VLM · Training-free
- **[MAD: Modality-Adaptive Decoding for Mitigating Cross-Modal Hallucinations in Multimodal Large Language Models](https://openaccess.thecvf.com/content/CVPR2026/html/Chung_MAD_Modality-Adaptive_Decoding_for_Mitigating_Cross-Modal_Hallucinations_in_Multimodal_Large_CVPR_2026_paper.html)** · CVPR 2026 · VLM · Training-free
- **[Locate-then-Sparsify: Attribution Guided Sparse Strategy for Visual Hallucination Mitigation](https://openaccess.thecvf.com/content/CVPR2026/html/Dang_Locate-then-Sparsify_Attribution_Guided_Sparse_Strategy_for_Visual_Hallucination_Mitigation_CVPR_2026_paper.html)** · CVPR 2026 · VLM · Training-free
- **[KVSmooth: Mitigating Hallucination in Multi-modal Large Language Models through Key-Value Smoothing](https://openaccess.thecvf.com/content/CVPR2026/html/Jiang_KVSmooth_Mitigating_Hallucination_in_Multi-modal_Large_Language_Models_through_Key-Value_CVPR_2026_paper.html)** · CVPR 2026 · VLM · Training-free
- **[HulluEdit: Single-Pass Evidence-Consistent Subspace Editing for Mitigating Hallucinations in Large Vision-Language Models](https://openaccess.thecvf.com/content/CVPR2026/html/Lin_HulluEdit_Single-Pass_Evidence-Consistent_Subspace_Editing_for_Mitigating_Hallucinations_in_Large_CVPR_2026_paper.html)** · CVPR 2026 · VLM · Training-free
- **[First Logit Boosting: Visual Grounding Method to Mitigate Object Hallucination in Large Vision-Language Models](https://openaccess.thecvf.com/content/CVPR2026/html/Ha_First_Logit_Boosting_Visual_Grounding_Method_to_Mitigate_Object_Hallucination_CVPR_2026_paper.html)** · CVPR 2026 · VLM · Training-free
- **📋 [Fine-Grained Multi Image Object Hallucination Benchmark](https://openaccess.thecvf.com/content/CVPR2026/html/Min_Fine-Grained_Multi_Image_Object_Hallucination_Benchmark_CVPR_2026_paper.html)** · CVPR 2026 · VLM · Training-free
- **[Fighting Hallucinations with Counterfactuals: Diffusion-Guided Perturbations for LVLM Hallucination Suppression](https://openaccess.thecvf.com/content/CVPR2026/html/Dastmalchi_Fighting_Hallucinations_with_Counterfactuals_Diffusion-Guided_Perturbations_for_LVLM_Hallucination_Suppression_CVPR_2026_paper.html)** · CVPR 2026 · VLM · Training-free
- **[FINER: MLLMs Hallucinate under Fine-grained Negative Queries](https://openaccess.thecvf.com/content/CVPR2026/html/Xiao_FINER_MLLMs_Hallucinate_under_Fine-grained_Negative_Queries_CVPR_2026_paper.html)** · CVPR 2026 · VLM · Training-free
- **[Envision, Attend, Then Respond: Counterfactual Hallucination Mitigation in Large Vision-Language Models](https://openaccess.thecvf.com/content/CVPR2026/html/Liang_Envision_Attend_Then_Respond_Counterfactual_Hallucination_Mitigation_in_Large_Vision-Language_CVPR_2026_paper.html)** · CVPR 2026 · VLM · Training-free
- **[ELV-Halluc: Benchmarking Semantic Aggregation Hallucinations in Video Understanding](https://openaccess.thecvf.com/content/CVPR2026/html/Lu_ELV-Halluc_Benchmarking_Semantic_Aggregation_Hallucinations_in_Video_Understanding_CVPR_2026_paper.html)** · CVPR 2026 · VLM · Training-free
- **[Dehallu3D: Hallucination-Mitigated 3D Generation from a Single Image via Cyclic View Consistency Refinement](https://openaccess.thecvf.com/content/CVPR2026/html/Wang_Dehallu3D_Hallucination-Mitigated_3D_Generation_from_a_Single_Image_via_Cyclic_CVPR_2026_paper.html)** · CVPR 2026 · VLM · Training-free
- **[Cross-Modal Attention Calibration for LVLM Hallucination Mitigation](https://openaccess.thecvf.com/content/CVPR2026/html/Li_Cross-Modal_Attention_Calibration_for_LVLM_Hallucination_Mitigation_CVPR_2026_paper.html)** · CVPR 2026 · VLM · Training-free
- **[CausalLens: Sensitivity-Guided Multi-Head Causal Intervention for Hallucination Mitigation in Large Vision-Language Models](https://openaccess.thecvf.com/content/CVPR2026/html/Ji_CausalLens_Sensitivity-Guided_Multi-Head_Causal_Intervention_for_Hallucination_Mitigation_in_Large_CVPR_2026_paper.html)** · CVPR 2026 · VLM · Training-free
- **[COPO: Causal-Oriented Policy Optimization for Hallucinations of MLLMs](https://openaccess.thecvf.com/content/CVPR2026/html/Guo_COPO_Causal-Oriented_Policy_Optimization_for_Hallucinations_of_MLLMs_CVPR_2026_paper.html)** · CVPR 2026 · VLM · Training-based
- **[Beyond the Global Scores: Fine-Grained Token Grounding as a Robust Detector of LVLM Hallucinations](https://openaccess.thecvf.com/content/CVPR2026/html/Nguyen_Beyond_the_Global_Scores_Fine-Grained_Token_Grounding_as_a_Robust_CVPR_2026_paper.html)** · CVPR 2026 · VLM · Training-free
- **[AdaIAT: Adaptively Increasing Attention to Generated Text to Alleviate Hallucinations in LVLM](https://openaccess.thecvf.com/content/CVPR2026/html/Zhong_AdaIAT_Adaptively_Increasing_Attention_to_Generated_Text_to_Alleviate_Hallucinations_CVPR_2026_paper.html)** · CVPR 2026 · VLM · Training-free
- **[3D-VCD: Hallucination Mitigation in 3D-LLM Embodied Agents through Visual Contrastive Decoding](https://openaccess.thecvf.com/content/CVPR2026/html/Ogunleye_3D-VCD_Hallucination_Mitigation_in_3D-LLM_Embodied_Agents_through_Visual_Contrastive_CVPR_2026_paper.html)** · CVPR 2026 · VLM · Training-free
- **[YARD: Y-Architecture Register Decoding for Efficient Hallucination Mitigation in Large Vision-Language Models](https://arxiv.org/abs/2605.31429)** · arXiv · VLM · Training-free
- **[When Relations Break: Analyzing Relation Hallucination in Vision-Language Model Under Rotation and Noise](https://arxiv.org/abs/2605.05045)** · arXiv · VLM · Training-free
- **[When Looking Is Not Enough: Visual Attention Structure Reveals Hallucination in MLLMs](https://arxiv.org/abs/2605.11559)** · arXiv · VLM · Training-free
- **[What Makes LVLMs Hallucinate Less? Unveiling the Architectural Factors Behind Hallucination Robustness](https://arxiv.org/abs/2605.30911)** · arXiv · VLM · Training-free
- **[VIHD: Visual Intervention-based Hallucination Detection for Medical Visual Question Answering](https://arxiv.org/abs/2605.20772)** · arXiv · VLM · Training-free
- **[Transcoders Trace Visual Grounding and Hallucinations in Vision-Language Models](https://arxiv.org/abs/2605.22902)** · arXiv · VLM · Training-free
- **[Risk-aware Selective Prompting for Hallucination Mitigation in Large Vision-Language Models](https://arxiv.org/abs/2605.28123)** · arXiv · VLM · Training-free
- **[Rethinking Visual Neglect: Steering via Context-Preference for MLLM Hallucination Mitigation](https://arxiv.org/abs/2605.27993)** · arXiv · VLM · Training-free
- **[Reducing Object Hallucination in LVLMs via Emphasizing Image-negative Tokens](https://arxiv.org/abs/2605.21300)** · arXiv · VLM · Training-free
- **[Reducing Hallucination in Vision-Language Models via Stage-wise Preference Optimization under Distribution Shift](https://arxiv.org/abs/2605.16411)** · arXiv · VLM · Training-based
- **[Reasoning Matters: Mitigate Hallucination in Multimodal Large Reasoning Models via Reasoning-Conditioned Preference Optimization](https://arxiv.org/abs/2605.27906)** · arXiv · VLM · Training-based
- **📋 [ReactBench: A Cause-Driven Benchmark for Multimodal Hallucination via Systematic Evaluation](https://arxiv.org/abs/2605.29579)** · arXiv · VLM · Training-free
- **[Online Self-Calibration Against Hallucination in Vision-Language Models](https://arxiv.org/abs/2605.00323)** · arXiv · VLM · Training-free
- **[Object Hallucination-Free Reinforcement Unlearning for Vision-Language Models](https://arxiv.org/abs/2605.08031)** · arXiv · VLM · Training-based
- **[Mitigating Object Hallucinations in Vision-Language Models through Region-Aware Attention Recalibration](https://arxiv.org/abs/2605.24957)** · arXiv · VLM · Training-free
- **[Mitigating Multimodal LLMs Hallucinations via Relevance Propagation at Inference Time](https://arxiv.org/abs/2605.01766)** · arXiv · VLM · Training-free
- **[Mitigating Hallucinations in Large Vision-Language Models via Causal Route Gating](https://arxiv.org/abs/2605.24024)** · arXiv · VLM · Training-free
- **[Mitigating Hallucination in Vision-Language Models through Barrier-Regulated Adaptive Closed-form Steering](https://arxiv.org/abs/2605.29881)** · arXiv · VLM · Training-free
- **[Mitigating Content Shift and Hallucination in GenAI Image Editing via Structural Refinement](https://arxiv.org/abs/2605.30437)** · arXiv · VLM · Training-free
- **📋 [Med-StepBench: A Hierarchical Reasoning Framework for Evaluating Hallucinations in Medical Vision-Language Models](https://arxiv.org/abs/2605.10002)** · arXiv · VLM · Training-free
- **[MHSA: A Lightweight Framework for Mitigating Hallucinations via Steered Attention in LVLMs](https://arxiv.org/abs/2605.14966)** · arXiv · VLM · Training-free
- **[Learning from Fine-Grained Visual Discrepancies: Mitigating Multimodal Hallucinations via In-Context Visual Contrastive Optimization](https://arxiv.org/abs/2605.31312)** · arXiv · VLM · Training-free
- **[Instruction Lens Score: Your Instruction Contributes a Powerful Object Hallucination Detector for Multimodal Large Language Models](https://arxiv.org/abs/2605.12258)** · arXiv · VLM · Training-free
- **[Hallucination as Exploit: Evidence-Carrying Multimodal Agents](https://arxiv.org/abs/2605.19192)** · arXiv · VLM · Training-free
- **[Hallucination Behavior in Multimodal LLMs Across Agricultural Image Interpretation and Generation Tasks](https://arxiv.org/abs/2605.27595)** · arXiv · VLM · Training-free
- **[HalluCXR: Benchmarking and Mitigating Hallucinations in Medical Vision-Language Models for Chest Radiograph Interpretation](https://arxiv.org/abs/2605.20469)** · arXiv · VLM · Training-free
- **[GEASS: Training-Free Caption Steering for Hallucination Mitigation in Vision-Language Models](https://arxiv.org/abs/2605.01733)** · arXiv · VLM · Training-free
- **[From Clouds to Hallucinations: Atmospheric Retrieval Hijacking in Remote Sensing Vision-Language RAG](https://arxiv.org/abs/2605.07273)** · arXiv · VLM · Training-free
- **[Finding the Correct Visual Evidence Without Forgetting: Mitigating Hallucination in LVLMs via Inter-Layer Visual Attention Discrepancy](https://arxiv.org/abs/2605.20965)** · arXiv · VLM · Training-free
- **[Dual-Pathway Circuits of Object Hallucination in Vision-Language Models](https://arxiv.org/abs/2605.13156)** · arXiv · VLM · Training-free
- **[CHASD: Language Increment-Calibrated Contrastive Decoding against Hallucination in LVLMs](https://arxiv.org/abs/2605.23344)** · arXiv · VLM · Training-free
- **[CAST: Mitigating Object Hallucination in Large Vision-Language Models via Caption-Guided Visual Attention Steering](https://arxiv.org/abs/2605.04641)** · arXiv · VLM · Training-free
- **[Adversarial Orthogonal Disentanglement for LVLM Hallucination Mitigation](https://arxiv.org/abs/2605.25377)** · arXiv · VLM · Training-free
- **[When Text Hijacks Vision: Benchmarking and Mitigating Text Overlay-Induced Hallucination in Vision Language Models](https://arxiv.org/abs/2604.17375)** · arXiv · VLM · Training-free
- **[When Prompts Override Vision: Prompt-Induced Hallucinations in LVLMs](https://arxiv.org/abs/2604.21911)** · arXiv · VLM · Training-free
- **[VCE: A zero-cost hallucination mitigation method of LVLMs via visual contrastive editing](https://arxiv.org/abs/2604.19412)** · arXiv · VLM · Training-free
- **[SycoPhantasy: Quantifying Sycophancy and Hallucination in Small Open Weight VLMs for Vision-Language Scoring of Fantasy Characters](https://arxiv.org/abs/2604.24346)** · arXiv · VLM · Training-free
- **[Steering the Verifiability of Multimodal AI Hallucinations](https://arxiv.org/abs/2604.06714)** · arXiv · VLM · Training-free
- **[See Fair, Speak Truth: Equitable Attention Improves Grounding and Reduces Hallucination in Vision-Language Alignment](https://arxiv.org/abs/2604.09749)** · arXiv · VLM · Training-free
- **[STEAR: Layer-Aware Spatiotemporal Evidence Intervention for Hallucination Mitigation in Video Large Language Models](https://arxiv.org/abs/2604.03045)** · arXiv · VLM · Training-free
- **[Relaxing Anchor-Frame Dominance for Mitigating Hallucinations in Video Large Language Models](https://arxiv.org/abs/2604.12582)** · arXiv · VLM · Training-free
- **[R-CoV: Region-Aware Chain-of-Verification for Alleviating Object Hallucinations in LVLMs](https://arxiv.org/abs/2604.20696)** · arXiv · VLM · Training-free
- **[Mitigating Multimodal Hallucination via Phase-wise Self-reward](https://arxiv.org/abs/2604.17982)** · arXiv · VLM · Training-free
- **[Mitigating Entangled Steering in Large Vision-Language Models for Hallucination Reduction](https://arxiv.org/abs/2604.07914)** · arXiv · VLM · Training-free
- **[Look Twice: Training-Free Evidence Highlighting in Multimodal Large Language Models](https://arxiv.org/abs/2604.01280)** · arXiv · VLM · Training-free
- **[LLM-as-Judge Framework for Evaluating Tone-Induced Hallucination in Vision-Language Models](https://arxiv.org/abs/2604.18803)** · arXiv · VLM · Training-free
- **[HaloProbe: Bayesian Detection and Mitigation of Object Hallucinations in Vision-Language Models](https://arxiv.org/abs/2604.06165)** · arXiv · VLM · Training-free
- **[HTDC: Hesitation-Triggered Differential Calibration for Mitigating Hallucination in Large Vision-Language Models](https://arxiv.org/abs/2604.12115)** · arXiv · VLM · Training-free
- **[Focus Matters: Phase-Aware Suppression for Hallucination in Vision-Language Models](https://arxiv.org/abs/2604.03556)** · arXiv · VLM · Training-free
- **[EnsemHalDet: Robust VLM Hallucination Detection via Ensemble of Internal State Detectors](https://arxiv.org/abs/2604.02784)** · arXiv · VLM · Training-free
- **📋 [DetailVerifyBench: A Benchmark for Dense Hallucination Localization in Long Image Captions](https://arxiv.org/abs/2604.05623)** · arXiv · VLM · Training-free
- **[Decoding by Perturbation: Mitigating MLLM Hallucinations via Dynamic Textual Perturbation](https://arxiv.org/abs/2604.12424)** · arXiv · VLM · Training-free
- **📋 [DO-Bench: An Attributable Benchmark for Diagnosing Object Hallucination in Vision-Language Models](https://arxiv.org/abs/2604.22822)** · arXiv · VLM · Training-free
- **[Cognitive Pivot Points and Visual Anchoring: Unveiling and Rectifying Hallucinations in Multimodal Reasoning Models](https://arxiv.org/abs/2604.10219)** · arXiv · VLM · Training-free
- **[Attention at Rest Stays at Rest: Breaking Visual Inertia for Cognitive Hallucination Mitigation](https://arxiv.org/abs/2604.01989)** · arXiv · VLM · Training-free
- **[Aligning What Vision-Language Models See and Perceive with Adaptive Information Flow](https://arxiv.org/abs/2604.15809)** · arXiv · VLM · Training-free
- **[ACT Now: Preempting LVLM Hallucinations via Adaptive Context Integration](https://arxiv.org/abs/2604.00983)** · arXiv · VLM · Training-free
- **[A Progressive Training Strategy for Vision-Language Models to Counteract Spatio-Temporal Hallucinations in Embodied Reasoning](https://arxiv.org/abs/2604.10506)** · arXiv · VLM · Training-based
- **[ORSc: Object-Aware Reinforcement with Semantic Consistency for Hallucination Mitigation in MLLMs](https://doi.org/10.1109/icassp55912.2026.11464193)** · ICASSP 2026 · VLM · Training-free
- **[Multi-Agent Brainstorming for Interpreting and Mitigating Hallucination in Multimodal-LLM](https://doi.org/10.1109/icassp55912.2026.11464937)** · ICASSP 2026 · VLM · Training-free
- **[Mitigating Object and Relationship Hallucination in Large Vision Language Model with Multi-Agent Guidance](https://doi.org/10.1109/icassp55912.2026.11463505)** · ICASSP 2026 · VLM · Training-free
- **[CVSTIM: Mitigating Object Hallucination in Mllms Via Co-Occurrence Guided Visual Stimulation](https://doi.org/10.1109/icassp55912.2026.11464584)** · ICASSP 2026 · VLM · Training-free
- **[AFTER: Mitigating the Object Hallucination of LVLM via Adaptive Factual-Guided Activation Editing]()** · ICLR 2026 · VLM · Training-free
- **[Visual Attention Drifts,but Anchors Hold:Mitigating Hallucination in Multimodal Large Language Models via Cross-Layer Visual Anchors](https://arxiv.org/abs/2603.25088)** · arXiv · VLM · Training-free
- **[VGS-Decoding: Visual Grounding Score Guided Decoding for Hallucination Mitigation in Medical VLMs](https://arxiv.org/abs/2603.20314)** · arXiv · VLM · Training-free
- **[Self-Correction Inside the Model: Leveraging Layer Attention to Mitigate Hallucinations in Large Vision Language Models](https://arxiv.org/abs/2603.00437)** · arXiv · VLM · Training-free
- **[Segmentation-Based Attention Entropy: Detecting and Mitigating Object Hallucinations in Large Vision-Language Models](https://arxiv.org/abs/2603.16558)** · arXiv · VLM · Training-free
- **[Seeing to Ground: Visual Attention for Hallucination-Resilient MDLLMs](https://arxiv.org/abs/2603.25711)** · arXiv · VLM · Training-free
- **[Seeing Clearly without Training: Mitigating Hallucinations in Multimodal LLMs for Remote Sensing](https://arxiv.org/abs/2603.02754)** · arXiv · VLM · Training-free
- **[SAGE: Sink-Aware Grounded Decoding for Multimodal Hallucination Mitigation](https://arxiv.org/abs/2603.27898)** · arXiv · VLM · Training-free
- **[Revealing Multi-View Hallucination in Large Vision-Language Models](https://arxiv.org/abs/2603.23934)** · arXiv · VLM · Training-free
- **[Overthinking Causes Hallucination: Tracing Confounder Propagation in Vision Language Models](https://arxiv.org/abs/2603.07619)** · arXiv · VLM · Training-free
- **[Mitigating Object Hallucinations in LVLMs via Attention Imbalance Rectification](https://arxiv.org/abs/2603.24058)** · arXiv · VLM · Training-free
- **📋 [ManiBench: A Benchmark for Testing Visual-Logic Drift and Syntactic Hallucinations in Manim Code Generation](https://arxiv.org/abs/2603.13251)** · arXiv · VLM · Training-free
- **[Looking Back and Forth: Cross-Image Attention Calibration and Attentive Preference Learning for Multi-Image Hallucination Mitigation](https://arxiv.org/abs/2603.07048)** · arXiv · VLM · Training-based
- **[Kestrel: Grounding Self-Refinement for LVLM Hallucination Mitigation](https://arxiv.org/abs/2603.16664)** · arXiv · VLM · Training-free
- **[Hallucination-aware intermediate representation edit in large vision-language models](https://arxiv.org/abs/2603.29405)** · arXiv · VLM · Training-free
- **📋 [HalDec-Bench: Benchmarking Hallucination Detector in Image Captioning](https://arxiv.org/abs/2603.15253)** · arXiv · VLM · Training-free
- **[GroundCount: Grounding Vision-Language Models with Object Detection for Mitigating Counting Hallucinations](https://arxiv.org/abs/2603.10978)** · arXiv · VLM · Training-free
- **📋 [FREAK: A Fine-grained Hallucination Evaluation Benchmark for Advanced MLLMs](https://arxiv.org/abs/2603.19765)** · arXiv · VLM · Training-free
- **[Do Not Leave a Gap: Hallucination-Free Object Concealment in Vision-Language Models](https://arxiv.org/abs/2603.15940)** · arXiv · VLM · Training-free
- **[Dehallu3D: Hallucination-Mitigated 3D Generation from Single Image via Cyclic View Consistency Refinement](https://arxiv.org/abs/2603.01601)** · arXiv · VLM · Training-free
- **[Anatomy of a Lie: A Multi-Stage Diagnostic Framework for Tracing Hallucinations in Vision-Language Models](https://arxiv.org/abs/2603.15557)** · arXiv · VLM · Training-free
- **[Scalpel: Fine-Grained Alignment of Attention Activation Manifolds via Mixture Gaussian Bridges to Mitigate Multimodal Hallucination](https://doi.org/10.1109/WACV61042.2026.00290)** · WACV 2026 · VLM · Training-free
- **[SAVE: Sparse Autoencoder-Driven Visual Information Enhancement for Mitigating Object Hallucination](https://doi.org/10.1109/WACV61042.2026.00766)** · WACV 2026 · VLM · Training-free
- **[Optimizing LVLMs with On-Policy Data for Effective Hallucination Mitigation](https://doi.org/10.1109/WACV61042.2026.00460)** · WACV 2026 · VLM · Training-free
- **[Mitigating Object and Action Hallucinations in Multimodal LLMs via Self-Augmented Contrastive Alignment](https://doi.org/10.1109/WACV61042.2026.00310)** · WACV 2026 · VLM · Training-free
- **[Mask What Matters: Mitigating Object Hallucinations in Multimodal Large Language Models with Object-Aligned Visual Contrastive Decoding](https://doi.org/10.18653/v1/2026.eacl-srw.2)** · EACL 2026 · VLM · Training-free
- **[HALP: Detecting Hallucinations in Vision-Language Models without Generating a Single Token](https://doi.org/10.18653/v1/2026.eacl-long.287)** · EACL 2026 · VLM · Training-free
- **[CAAC: Confidence-Aware Attention Calibration to Reduce Hallucinations in Large Vision-Language Models](https://doi.org/10.1109/WACV61042.2026.00127)** · WACV 2026 · VLM · Training-free
- **[Attribution-Guided Multi-Object Hallucination and Bias Detection in Vision-Language Models](https://doi.org/10.18653/v1/2026.eacl-long.210)** · EACL 2026 · VLM · Training-free
- **[Visualizing and Benchmarking LLM Factual Hallucination Tendencies via Internal State Analysis and Clustering](https://arxiv.org/abs/2602.11167)** · arXiv · VLM · Training-free
- **[VIGIL: Tackling Hallucination Detection in Image Recontextualization](https://arxiv.org/abs/2602.14633)** · arXiv · VLM · Training-free
- **[Towards Interpretable Hallucination Analysis and Mitigation in LVLMs via Contrastive Neuron Steering](https://arxiv.org/abs/2602.00621)** · arXiv · VLM · Training-free
- **[Seeing Through the Chain: Mitigate Hallucination in Multimodal Reasoning Models via CoT Compression and Contrastive Preference Optimization](https://arxiv.org/abs/2602.03380)** · arXiv · VLM · Training-based
- **[See It, Say It, Sorted: An Iterative Training-Free Framework for Visually-Grounded Multimodal Reasoning in LVLMs](https://arxiv.org/abs/2602.21497)** · arXiv · VLM · Training-free
- **[SchroMind: Mitigating Hallucinations in Multimodal Large Language Models via Solving the Schrodinger Bridge Problem](https://arxiv.org/abs/2602.09528)** · arXiv · VLM · Training-free
- **[SAKED: Mitigating Hallucination in Large Vision-Language Models via Stability-Aware Knowledge Enhanced Decoding](https://arxiv.org/abs/2602.09825)** · arXiv · VLM · Training-free
- **[Revis: Sparse Latent Steering to Mitigate Object Hallucination in Large Vision-Language Models](https://arxiv.org/abs/2602.11824)** · arXiv · VLM · Training-free
- **[RSHallu: Dual-Mode Hallucination Evaluation for Remote-Sensing Multimodal Large Language Models with Domain-Tailored Mitigation](https://arxiv.org/abs/2602.10799)** · arXiv · VLM · Training-based
- **[NoLan: Mitigating Object Hallucinations in Large Vision-Language Models via Dynamic Suppression of Language Priors](https://arxiv.org/abs/2602.22144)** · arXiv · VLM · Training-free
- **[Look Carefully: Adaptive Visual Reinforcements in Multimodal Large Language Models for Hallucination Mitigation](https://arxiv.org/abs/2602.24041)** · arXiv · VLM · Training-free
- **[Learning to Decode Against Compositional Hallucination in Video Multimodal Large Language Models](https://arxiv.org/abs/2602.00559)** · arXiv · VLM · Training-free
- **[IRIS: Implicit Reward-Guided Internal Sifting for Mitigating Multimodal Hallucination](https://arxiv.org/abs/2602.01769)** · arXiv · VLM · Training-free
- **[HIME: Mitigating Object Hallucinations in LVLMs via Hallucination Insensitivity Model Editing](https://arxiv.org/abs/2602.18711)** · arXiv · VLM · Training-based
- **[HII-DPO: Eliminate Hallucination via Accurate Hallucination-Inducing Counterfactual Images](https://arxiv.org/abs/2602.10425)** · arXiv · VLM · Training-based
- **[Dynamic Multimodal Activation Steering for Hallucination Mitigation in Large Vision-Language Models](https://arxiv.org/abs/2602.21704)** · arXiv · VLM · Training-free
- **[ConsistentRFT: Reducing Visual Hallucinations in Flow-based Reinforcement Fine-Tuning](https://arxiv.org/abs/2602.03425)** · arXiv · VLM · Training-free
- **[ClueTracer: Question-to-Vision Clue Tracing for Training-Free Hallucination Suppression in Multimodal Reasoning](https://arxiv.org/abs/2602.02004)** · arXiv · VLM · Training-free
- **[Beyond Static Cropping: Layer-Adaptive Visual Localization and Decoding Enhancement](https://arxiv.org/abs/2602.04304)** · arXiv · VLM · Training-free
- **[Beyond Dominant Patches: Spatial Credit Redistribution For Grounded Vision-Language Models](https://arxiv.org/abs/2602.22469)** · arXiv · VLM · Training-free
- **[Attention to details, logits to truth: visual-aware attention and logits enhancement to mitigate hallucinations in LVLMs](https://arxiv.org/abs/2602.09521)** · arXiv · VLM · Training-free
- **[AdaVBoost: Mitigating Hallucinations in LVLMs via Token-Level Adaptive Visual Attention Boosting](https://arxiv.org/abs/2602.13600)** · arXiv · VLM · Training-free
- **[Action Hallucination in Generative Vision-Language-Action Models](https://arxiv.org/abs/2602.06339)** · arXiv · VLM · Training-free
- **[Verb Mirage: Unveiling and Assessing Verb Concept Hallucinations in Multimodal Large Language Models](https://doi.org/10.1609/aaai.v40i12.38005)** · AAAI 2026 · VLM · Training-free
- **[VCGD: Visual Clue Guided Decoding with Caption Model for Mitigating Hallucination in Multimodal Large Language Models](https://doi.org/10.1609/aaai.v40i24.39089)** · AAAI 2026 · VLM · Training-free
- **[Taming the Phantom: Token-Asymmetric Filtering for Hallucination Mitigation in Large Vision-Language Models](https://doi.org/10.1609/aaai.v40i10.37768)** · AAAI 2026 · VLM · Training-free
- **[SmartSight: Mitigating Hallucination in Video-LLMs Without Compromising Video Understanding via Temporal Attention Collapse](https://doi.org/10.1609/aaai.v40i11.37883)** · AAAI 2026 · VLM · Training-free
- **[Seeing Is Believing: Rich-Context Hallucination Detection for MLLMs via Backward Visual Grounding](https://doi.org/10.1609/aaai.v40i37.40345)** · AAAI 2026 · VLM · Training-free
- **[SAVER: Mitigating Hallucinations in Large Vision-Language Models via Style-Aware Visual Early Revision](https://doi.org/10.1609/aaai.v40i42.40873)** · AAAI 2026 · VLM · Training-free
- **[RFI: Rectified Flow Intervention for Mitigating Object Hallucination in Large Vision-Language Models](https://doi.org/10.1609/aaai.v40i5.37320)** · AAAI 2026 · VLM · Training-free
- **[Multi-Agent Undercover Gaming: Hallucination Removal Through Counterfactual Test for Multimodal Reasoning](https://doi.org/10.1609/aaai.v40i8.37613)** · AAAI 2026 · VLM · Training-free
- **[Look Closer! An Adversarial Parametric Editing Framework for Hallucination Mitigation in VLMs](https://doi.org/10.1609/aaai.v40i26.39336)** · AAAI 2026 · VLM · Training-based
- **[Ground What You See: Hallucination-Resistant MLLMs via Caption Feedback, Diversity-Aware Sampling, and Conflict Regularization](https://doi.org/10.1609/aaai.v40i10.37772)** · AAAI 2026 · VLM · Training-free
- **[EchoBat: Echo-Vision Enhancement and Echo-Layered Sampling for Video LLMs Hallucination Mitigation](https://doi.org/10.1609/aaai.v40i42.40875)** · AAAI 2026 · VLM · Training-free
- **[Causally-Grounded Dual-Path Attention Intervention for Object Hallucination Mitigation in LVLMs](https://doi.org/10.1609/aaai.v40i42.40918)** · AAAI 2026 · VLM · Training-free
- **📋 [Causal-HalBench: Uncovering LVLMs Object Hallucinations Through Causal Intervention](https://doi.org/10.1609/aaai.v40i40.40712)** · AAAI 2026 · VLM · Training-free
- **[Causal Tracing of Object Representations in Large Vision Language Models: Mechanistic Interpretability and Hallucination Mitigation](https://doi.org/10.1609/aaai.v40i37.40431)** · AAAI 2026 · VLM · Training-free
- **[Bridging Day and Night: Target-Class Hallucination Suppression in Unpaired Image Translation](https://doi.org/10.1609/aaai.v40i8.37570)** · AAAI 2026 · VLM · Training-free
- **[Anatomical Region-Guided Contrastive Decoding: A Plug-and-Play Strategy for Mitigating Hallucinations in Medical VLMs](https://doi.org/10.1609/aaai.v40i9.37620)** · AAAI 2026 · VLM · Training-free
- **[Adaptive Hallucination Alleviation in Multimodal Large Language Models: From Strategic Data Selection to Severity-Guided Training](https://doi.org/10.1609/aaai.v40i32.39955)** · AAAI 2026 · VLM · Training-free
- **[ASCD: Attention-Steerable Contrastive Decoding for Reducing Hallucination in MLLM](https://doi.org/10.1609/aaai.v40i12.38000)** · AAAI 2026 · VLM · Training-free
- **[Where Does Vision Meet Language? Understanding and Refining Visual Fusion in MLLMs via Contrastive Attention](https://arxiv.org/abs/2601.08151)** · arXiv · VLM · Training-free
- **[VideoHEDGE: Entropy-Based Hallucination Detection for Video-VLMs via Semantic Clustering and Spatiotemporal Perturbations](https://arxiv.org/abs/2601.08557)** · arXiv · VLM · Training-free
- **[VERHallu: Evaluating and Mitigating Event Relation Hallucination in Video Large Language Models](https://arxiv.org/abs/2601.10010)** · arXiv · VLM · Training-free
- **[V-Loop: Visual Logical Loop Verification for Hallucination Detection in Medical Visual Question Answering](https://arxiv.org/abs/2601.18240)** · arXiv · VLM · Training-free
- **[Tone Matters: The Impact of Linguistic Tone on Hallucination in VLMs](https://arxiv.org/abs/2601.06460)** · arXiv · VLM · Training-free
- **[Text-Guided Layer Fusion Mitigates Hallucination in Multimodal LLMs](https://arxiv.org/abs/2601.03100)** · arXiv · VLM · Training-free
- **[Seeing Right but Saying Wrong: Inter- and Intra-Layer Refinement in MLLMs without Training](https://arxiv.org/abs/2601.07359)** · arXiv · VLM · Training-free
- **[SDCD: Structure-Disrupted Contrastive Decoding for Mitigating Hallucinations in Large Vision-Language Models](https://arxiv.org/abs/2601.03500)** · arXiv · VLM · Training-free
- **[One-shot Optimized Steering Vector for Hallucination Mitigation for VLMs](https://arxiv.org/abs/2601.23041)** · arXiv · VLM · Training-free
- **[FaithSCAN: Model-Driven Single-Pass Hallucination Detection for Faithful Visual Question Answering](https://arxiv.org/abs/2601.00269)** · arXiv · VLM · Training-free
- **[Enhancing Video Representations with Spatiotemporal-Semantic Residual to Mitigate Hallucinations in Video Large Multimodal Models](https://arxiv.org/abs/2601.22574)** · arXiv · VLM · Training-free
- **[Countering the Over-Reliance Trap: Mitigating Object Hallucination for LVLMs via a Self-Validation Framework](https://arxiv.org/abs/2601.22451)** · arXiv · VLM · Training-free
- **[CounterVid: Counterfactual Video Generation for Mitigating Action and Temporal Hallucinations in Video-Language Models](https://arxiv.org/abs/2601.04778)** · arXiv · VLM · Training-free
- **[Beyond Superficial Unlearning: Sharpness-Aware Robust Erasure of Hallucinations in Multimodal LLMs](https://arxiv.org/abs/2601.16527)** · arXiv · VLM · Training-based
- **[Attention-space Contrastive Guidance for Efficient Hallucination Mitigation in LVLMs](https://arxiv.org/abs/2601.13707)** · arXiv · VLM · Training-free
- **[VGL-DPO: Vision-Guided Lexical Direct Preference Optimization for Mitigating Hallucination in Multimodal Large Language Models](https://doi.org/10.1145/3796715)** · TOMM 2026 · VLM · Training-based
- **📋 [TempHalluc-Bench: Evaluating Temporal Hallucination in VideoLLM-Based Video Search and Information Extraction](https://doi.org/10.5120/ijca-1aef39d4b120)** · International Journal of Computer Applications 2026 · VLM · Training-free
- **[Mitigating hallucination in Multimodal Large Language Models via cross-layer visual anchors](https://doi.org/10.1016/j.patcog.2026.114380)** · Pattern Recognit. 2026 · VLM · Training-free
- **[Mitigating Visual Hallucination in Multimodal Event Extraction via Constrained Prompting](https://doi.org/10.3233/atde260397)** · Advances in Transdisciplinary Engineering 2026 · VLM · Training-free
- **[Mitigating Multimodal Hallucination Through Effective and Perception-Aware Granularity Alignment](https://doi.org/10.1109/taslpro.2026.3703183)** · TASLP 2026 · VLM · Training-free
- **[Mitigating Multilingual Hallucination in Large Vision-Language Models](https://doi.org/10.1145/3797025)** · TOMM 2026 · VLM · Training-free
- **[Mitigating Low-Level Visual Hallucinations Requires Self-Awareness: Database, Model and Training Strategy](https://doi.org/10.1109/TCSVT.2025.3619558)** · IEEE Trans. Circuits Syst. Video Technol. 2026 · VLM · Training-based
- **[Mitigating Hallucination in Multimodal Information Systems: A Comparative Analysis of Modular LLM Architectures](https://doi.org/10.1109/tcss.2026.3691181)** · IEEE Transactions on Computational Social Systems 2026 · VLM · Training-free
- **[Med-VCD: Mitigating Hallucination for Medical Large Vision Language Models through Visual Contrastive Decoding](https://doi.org/10.1016/j.compbiomed.2025.111347)** · Comput. Biol. Medicine 2026 · VLM · Training-free
- **[Hallucination Elimination and Text Annotation Framework for Large Vision-Language Models in Traffic Scenarios](https://doi.org/10.1109/TITS.2025.3625700)** · IEEE Trans. Intell. Transp. Syst. 2026 · VLM · Training-free
- **[Dr.V : A Hierarchical Perception-Temporal-Cognition Framework to Diagnose Video Hallucination by Fine-Grained Spatial-Temporal Grounding](https://doi.org/10.1007/s11263-026-02831-1)** · IJCV 2026 · VLM · Training-free
- **[Causal Decoding for Hallucination-Resistant Multimodal Large Language Models](https://openreview.net/forum?id=5Wb5c0FaCG)** · TMLR 2026 · VLM · Training-free
- **[CRoPS: A Training-Free Hallucination Mitigation Framework for Vision-Language Models](https://openreview.net/forum?id=KQSoZDPVGX)** · TMLR 2026 · VLM · Training-free
- **📋 [CDH-Bench: A Commonsense-Driven Hallucination Benchmark for Evaluating Visual Fidelity in Vision-Language Models](https://doi.org/10.1007/978-981-92-3504-9_17)** · ICIC 2026 · VLM · Training-free
- **[Attention Reallocation: Towards Zero-cost and Controllable Hallucination Mitigation of MLLMs](https://doi.org/10.1007/s11263-025-02607-z)** · IJCV 2026 · VLM · Training-free
- **📚 [A Survey of Multimodal Hallucination Evaluation and Detection](https://doi.org/10.1007/s11263-026-02756-9)** · IJCV 2026 · VLM · Training-free
- **[A CNN-Based Framework for Addressing Hallucination Phenomena: Mitigating Limitations Across Multimodal and Clinical Contexts](https://doi.org/10.1007/978-3-032-14197-2_22)** · Lecture Notes in Networks and Systems 2026 · VLM · Training-free

</details>

<details>
<summary>📅 2025 · 278 papers</summary>

- **[When normalization hallucinates: unseen risks in AI-powered whole slide image processing](https://arxiv.org/abs/2512.07426)** · arXiv · VLM · Training-free
- **[Watch Closely: Mitigating Object Hallucinations in Large Vision-Language Models with Disentangled Decoding](https://arxiv.org/abs/2512.19070)** · arXiv · VLM · Training-free
- **[VEGAS: Mitigating Hallucinations in Large Vision-Language Models via Vision-Encoder Attention Guided Adaptive Steering](https://arxiv.org/abs/2512.12089)** · arXiv · VLM · Training-free
- **[V-ITI: Mitigating Hallucinations in Multimodal Large Language Models via Visual Inference-Time Intervention](https://arxiv.org/abs/2512.03542)** · arXiv · VLM · Training-free
- **[Toward More Reliable Artificial Intelligence: Reducing Hallucinations in Vision-Language Models](https://arxiv.org/abs/2512.07564)** · arXiv · VLM · Training-free
- **[Taming Hallucinations: Boosting MLLMs' Video Understanding via Counterfactual Video Generation](https://arxiv.org/abs/2512.24271)** · arXiv · VLM · Training-free
- **[Revealing Perception and Generation Dynamics in LVLMs: Mitigating Hallucinations via Validated Dominance Correction](https://arxiv.org/abs/2512.18813)** · arXiv · VLM · Training-free
- **[HalluShift++: Bridging Language and Vision through Internal Representation Shifts for Hierarchical Hallucinations in MLLMs](https://arxiv.org/abs/2512.07687)** · arXiv · VLM · Training-free
- **[Graphing the Truth: Structured Visualizations for Automated Hallucination Detection in LLMs](https://arxiv.org/abs/2512.00663)** · arXiv · VLM · Training-free
- **[Conscious Gaze: Adaptive Attention Mechanisms for Hallucination Mitigation in Vision-Language Models](https://arxiv.org/abs/2512.05546)** · arXiv · VLM · Training-free
- **[CHEM: Estimating and Understanding Hallucinations in Deep Learning for Image Processing](https://arxiv.org/abs/2512.09806)** · arXiv · VLM · Training-free
- **[VideoHallu: Evaluating and Mitigating Multi-modal Hallucinations on Synthetic Video Understanding](http://papers.nips.cc/paper_files/paper/2025/hash/6e1734c47c0cc899021060d88f69dc65-Abstract-Conference.html)** · NeurIPS 2025 · VLM · Training-free
- **[Systematic Reward Gap Optimization for Mitigating VLM Hallucinations](http://papers.nips.cc/paper_files/paper/2025/hash/a63ce8e6867a1bf4b4ca62e5077814d9-Abstract-Conference.html)** · NeurIPS 2025 · VLM · Training-free
- **[On Epistemic Uncertainty of Visual Tokens for Object Hallucinations in Large Vision-Language Models](http://papers.nips.cc/paper_files/paper/2025/hash/bd6673d95a2a994a5647dca1df91a000-Abstract-Conference.html)** · NeurIPS 2025 · VLM · Training-free
- **[More Thinking, Less Seeing? Assessing Amplified Hallucination in Multimodal Reasoning Models](http://papers.nips.cc/paper_files/paper/2025/hash/777db387a5ccb131ba8c7cd155166b85-Abstract-Conference.html)** · NeurIPS 2025 · VLM · Training-free
- **[MIRAGE: Assessing Hallucination in Multimodal Reasoning Chains of MLLM](http://papers.nips.cc/paper_files/paper/2025/hash/b238324b309da12c7446d92c14db9f7e-Abstract-Conference.html)** · NeurIPS 2025 · VLM · Training-free
- **[Intervene-All-Paths: Unified Mitigation of LVLM Hallucinations across Alignment Formats](http://papers.nips.cc/paper_files/paper/2025/hash/d0cf89927acd9136d27ebf08f9e8a888-Abstract-Conference.html)** · NeurIPS 2025 · VLM · Training-free
- **[Image Token Matters: Mitigating Hallucination in Discrete Tokenizer-based Large Vision-Language Models via Latent Editing](http://papers.nips.cc/paper_files/paper/2025/hash/a17c939f1bdee90ec74a9c3cb938d8c3-Abstract-Conference.html)** · NeurIPS 2025 · VLM · Training-free
- **[Hallucination at a Glance: Controlled Visual Edits and Fine-Grained Multimodal Learning](http://papers.nips.cc/paper_files/paper/2025/hash/c518f504ad5894ccb264a9890f0f5544-Abstract-Conference.html)** · NeurIPS 2025 · VLM · Training-free
- **[Grounding Language with Vision: A Conditional Mutual Information Calibrated Decoding Strategy for Reducing Hallucinations in LVLMs](http://papers.nips.cc/paper_files/paper/2025/hash/9796170d31d42b943534df40bdee68d3-Abstract-Conference.html)** · NeurIPS 2025 · VLM · Training-free
- **[Do LVLMs Truly Understand Video Anomalies? Revealing Hallucination via Co-Occurrence Patterns](http://papers.nips.cc/paper_files/paper/2025/hash/99b419554537c66bf27e5eb7a74c7de4-Abstract-Conference.html)** · NeurIPS 2025 · VLM · Training-free
- **[Decoupling Contrastive Decoding: Robust Hallucination Mitigation in Multimodal Large Language Models](http://papers.nips.cc/paper_files/paper/2025/hash/f39cc9110544a067f024c1fb8b396128-Abstract-Conference.html)** · NeurIPS 2025 · VLM · Training-free
- **[What's in Common? Multimodal Models Hallucinate When Reasoning Across Scenes](https://arxiv.org/abs/2511.03768)** · arXiv · VLM · Training-free
- **📋 [What Color Is It? A Text-Interference Multimodal Hallucination Benchmark](https://arxiv.org/abs/2511.13400)** · arXiv · VLM · Training-free
- **[VOPE: Revisiting Hallucination of Vision-Language Models in Voluntary Imagination Task](https://arxiv.org/abs/2511.13420)** · arXiv · VLM · Training-free
- **[Suppressing VLM Hallucinations with Spectral Representation Filtering](https://arxiv.org/abs/2511.12220)** · arXiv · VLM · Training-free
- **[NOAH: Benchmarking Narrative Prior driven Hallucination and Omission in Video Large Language Models](https://arxiv.org/abs/2511.06475)** · arXiv · VLM · Training-free
- **[Multi-agent Undercover Gaming: Hallucination Removal via Counterfactual Test for Multimodal Reasoning](https://arxiv.org/abs/2511.11182)** · arXiv · VLM · Training-free
- **[HEDGE: Hallucination Estimation via Dense Geometric Entropy for VQA with Vision-Language Models](https://arxiv.org/abs/2511.12693)** · arXiv · VLM · Training-free
- **[Decoupling Perception from Reasoning for Hallucination-Resistant Video Understanding](https://arxiv.org/abs/2511.18463)** · arXiv · VLM · Training-free
- **[Adaptive Residual-Update Steering for Low-Overhead Hallucination Mitigation in Large Vision Language Models](https://arxiv.org/abs/2511.10292)** · arXiv · VLM · Training-free
- **[A Low-Rank Method for Vision Language Model Hallucination Mitigation in Autonomous Driving](https://arxiv.org/abs/2511.06496)** · arXiv · VLM · Training-free
- **[Unveiling the Response of Large Vision-Language Models to Visually Absent Tokens](https://doi.org/10.18653/v1/2025.emnlp-main.1092)** · EMNLP 2025 · VLM · Training-free
- **[Treble Counterfactual VLMs: A Causal Approach to Hallucination](https://doi.org/10.18653/v1/2025.findings-emnlp.1000)** · EMNLP 2025 · VLM · Training-free
- **[Token Preference Optimization with Self-Calibrated Visual-Anchored Rewards for Hallucination Mitigation](https://doi.org/10.18653/v1/2025.findings-emnlp.1076)** · EMNLP 2025 · VLM · Training-based
- **[Steering LVLMs via Sparse Autoencoder for Hallucination Mitigation](https://doi.org/10.18653/v1/2025.findings-emnlp.572)** · EMNLP 2025 · VLM · Training-free
- **[Shallow Focus, Deep Fixes: Enhancing Shallow Layers Vision Attention Sinks to Alleviate Hallucination in LVLMs](https://doi.org/10.18653/v1/2025.emnlp-main.174)** · EMNLP 2025 · VLM · Training-free
- **[SHARP: Steering Hallucination in LVLMs via Representation Engineering](https://doi.org/10.18653/v1/2025.emnlp-main.725)** · EMNLP 2025 · VLM · Training-free
- **[ReLoop: &quot;Seeing Twice and Thinking Backwards&quot; via Closed-loop Training to Mitigate Hallucinations in Multimodal understanding](https://doi.org/10.18653/v1/2025.findings-emnlp.222)** · EMNLP 2025 · VLM · Training-free
- **[ReLoop: "Seeing Twice and Thinking Backwards" via Closed-loop Training to Mitigate Hallucinations in Multimodal understanding](https://doi.org/10.18653/v1/2025.findings-emnlp.222)** · EMNLP 2025 · VLM · Training-free
- **[Re-Align: Aligning Vision Language Models via Retrieval-Augmented Direct Preference Optimization](https://doi.org/10.18653/v1/2025.emnlp-main.121)** · EMNLP 2025 · VLM · Training-based
- **[Multi-Frequency Contrastive Decoding: Alleviating Hallucinations for Large Vision-Language Models](https://doi.org/10.18653/v1/2025.emnlp-main.1452)** · EMNLP 2025 · VLM · Training-free
- **[Mitigating Object Hallucinations in MLLMs via Multi-Frequency Perturbations](https://doi.org/10.18653/v1/2025.findings-emnlp.64)** · EMNLP 2025 · VLM · Training-free
- **[Mitigating Hallucinations in Vision-Language Models through Image-Guided Head Suppression](https://doi.org/10.18653/v1/2025.emnlp-main.631)** · EMNLP 2025 · VLM · Training-free
- **[Mitigating Hallucinations in Large Vision-Language Models via Entity-Centric Multimodal Preference Optimization](https://doi.org/10.18653/v1/2025.emnlp-main.982)** · EMNLP 2025 · VLM · Training-based
- **[Mitigating Hallucinations in Large Vision-Language Models by Self-Injecting Hallucinations](https://doi.org/10.18653/v1/2025.findings-emnlp.746)** · EMNLP 2025 · VLM · Training-free
- **[Mitigating Hallucination in Large Vision-Language Models through Aligning Attention Distribution to Information Flow](https://doi.org/10.18653/v1/2025.findings-emnlp.1352)** · EMNLP 2025 · VLM · Training-free
- **[MaskCD: Mitigating LVLM Hallucinations by Image Head Masked Contrastive Decoding](https://doi.org/10.18653/v1/2025.findings-emnlp.1025)** · EMNLP 2025 · VLM · Training-free
- **[MRFD: Multi-Region Fusion Decoding with Self-Consistency for Mitigating Hallucinations in LVLMs](https://doi.org/10.18653/v1/2025.findings-emnlp.858)** · EMNLP 2025 · VLM · Training-free
- **[EGOILLUSION: Benchmarking Hallucinations in Egocentric Video Understanding](https://doi.org/10.18653/v1/2025.emnlp-main.1446)** · EMNLP 2025 · VLM · Training-free
- **[Diving into Mitigating Hallucinations from a Vision Perspective for Large Vision-Language Models](https://doi.org/10.18653/v1/2025.findings-emnlp.936)** · EMNLP 2025 · VLM · Training-free
- **[DAPE-BR: Distance-Aware Positional Encoding for Mitigating Object Hallucination in LVLMs](https://doi.org/10.18653/v1/2025.findings-emnlp.459)** · EMNLP 2025 · VLM · Training-free
- **[When Images Speak Louder: Mitigating Language Bias-induced Hallucinations in VLMs through Cross-Modal Guidance](https://arxiv.org/abs/2510.10466)** · arXiv · VLM · Training-free
- **[To Sink or Not to Sink: Visual Information Pathways in Large Vision-Language Models](https://arxiv.org/abs/2510.08510)** · arXiv · VLM · Training-free
- **[Self-Augmented Visual Contrastive Decoding](https://arxiv.org/abs/2510.13315)** · arXiv · VLM · Training-free
- **[Seeing but Not Believing: Probing the Disconnect Between Visual Attention and Answer Correctness in VLMs](https://arxiv.org/abs/2510.17771)** · arXiv · VLM · Training-free
- **[SHIELD: Suppressing Hallucinations In LVLM Encoders via Bias and Vulnerability Defense](https://arxiv.org/abs/2510.16596)** · arXiv · VLM · Training-free
- **[PruneHal: Reducing Hallucinations in Multi-modal Large Language Models through Adaptive KV Cache Pruning](https://arxiv.org/abs/2510.19183)** · arXiv · VLM · Training-free
- **[Multi-Modal Fact-Verification Framework for Reducing Hallucinations in Large Language Models](https://arxiv.org/abs/2510.22751)** · arXiv · VLM · Training-free
- **[Hallucination Localization in Video Captioning](https://arxiv.org/abs/2510.25225)** · arXiv · VLM · Training-free
- **[Hallucination Filtering in Radiology Vision-Language Models Using Discrete Semantic Entropy](https://arxiv.org/abs/2510.09256)** · arXiv · VLM · Training-free
- **[Grounding or Guessing? Visual Signals for Detecting Hallucinations in Sign Language Translation](https://arxiv.org/abs/2510.18439)** · arXiv · VLM · Training-free
- **[Efficient High-Resolution Image Editing with Hallucination-Aware Loss and Adaptive Tiling](https://arxiv.org/abs/2510.06295)** · arXiv · VLM · Training-free
- **[ChainMPQ: Interleaved Text-Image Reasoning Chains for Mitigating Relation Hallucinations](https://arxiv.org/abs/2510.06292)** · arXiv · VLM · Training-free
- **[Capturing Gaze Shifts for Guidance: Cross-Modal Fusion Enhancement for VLM Hallucination Mitigation](https://arxiv.org/abs/2510.22067)** · arXiv · VLM · Training-free
- **[Beyond Single Models: Mitigating Multimodal Hallucinations via Adaptive Token Ensemble Decoding](https://arxiv.org/abs/2510.18321)** · arXiv · VLM · Training-free
- **[Why LVLMs Are More Prone to Hallucinations in Longer Responses: The Role of Context](https://doi.org/10.1109/ICCV51701.2025.00391)** · ICCV 2025 · VLM · Training-free
- **[Visual Perception Uncertainty Learning for Hallucination Detection in Large Vision-Language Models](https://doi.org/10.1145/3746027.3755126)** · ACM MM 2025 · VLM · Training-free
- **[TruthPrInt: Mitigating Large Vision-Language Models Object Hallucination via Latent Truthful-Guided Pre-Intervention](https://doi.org/10.1109/ICCV51701.2025.00692)** · ICCV 2025 · VLM · Training-free
- **[See Different, Think Better: Visual Variations Mitigating Hallucinations in LVLMs](https://doi.org/10.1145/3746027.3755044)** · ACM MM 2025 · VLM · Training-free
- **[SHIFT: Smoothing Hallucinations by Information Flow Tuning for Multimodal Large Language Models](https://doi.org/10.1109/ICCV51701.2025.00347)** · ICCV 2025 · VLM · Training-free
- **📋 [SHALE: A Scalable Benchmark for Fine-grained Hallucination Evaluation in LVLMs](https://doi.org/10.1145/3746027.3758308)** · ACM MM 2025 · VLM · Training-free
- **[ONLY: One-Layer Intervention Sufficiently Mitigates Hallucinations in Large Vision-Language Models](https://doi.org/10.1109/ICCV51701.2025.00309)** · ICCV 2025 · VLM · Training-free
- **[Mitigating Image Captioning Hallucinations in Vision-Language Models](https://arxiv.org/abs/2505.03420)** · ACM MM 2025 · VLM · Training-free
- **[MPI-CD: Multi-Path Information Contrastive Decoding for Mitigating Hallucinations in Large Vision-Language Models](https://doi.org/10.1145/3746027.3755372)** · ACM MM 2025 · VLM · Training-free
- **📋 [MIHBench: Benchmarking and Mitigating Multi-Image Hallucinations in Multimodal Large Language Models](https://doi.org/10.1145/3746027.3754993)** · ACM MM 2025 · VLM · Training-free
- **[MESH - Understanding Videos Like Human: Measuring Hallucinations in Large Video Models](https://doi.org/10.1145/3746027.3755626)** · ACM MM 2025 · VLM · Training-free
- **[MCA-LLaVA: Manhattan Causal Attention for Reducing Hallucination in Large Vision-Language Models](https://doi.org/10.1145/3746027.3755271)** · ACM MM 2025 · VLM · Training-free
- **[Identify, Isolate, and Purge: Mitigating Hallucinations in LVLMs via Self-Evolving Distillation](https://doi.org/10.1145/3746027.3754784)** · ACM MM 2025 · VLM · Training-free
- **[INTER: Mitigating Hallucination in Large Vision-Language Models by Interaction Guidance Sampling](https://doi.org/10.1109/ICCV51701.2025.00244)** · ICCV 2025 · VLM · Training-free
- **[Hallucinatory Image Tokens: A Training-Free EAZY Approach to Detecting and Mitigating Object Hallucinations in LVLMs](https://doi.org/10.1109/ICCV51701.2025.02009)** · ICCV 2025 · VLM · Training-free
- **[HKD4VLM: A Progressive Hybrid Knowledge Distillation Framework for Robust Multimodal Hallucination and Factuality Detection in VLMs](https://doi.org/10.1145/3746027.3762014)** · ACM MM 2025 · VLM · Training-free
- **[Fuzzy Contrastive Decoding to Alleviate Object Hallucination in Large Vision-Language Models](https://doi.org/10.1109/ICCV51701.2025.01913)** · ICCV 2025 · VLM · Training-free
- **[From Pixels to Tokens: Revisiting Object Hallucinations in Large Vision-Language Models](https://doi.org/10.1145/3746027.3755728)** · ACM MM 2025 · VLM · Training-free
- **[Enhancing Visual Reliance in Text Generation: A Bayesian Perspective on Mitigating Hallucination in Large Vision-Language Models](https://doi.org/10.1145/3746027.3755606)** · ACM MM 2025 · VLM · Training-free
- **[DeepSIX at ACM MM 2025 Grand Challenge: Enhancing Context Text Processing for Multimodal Hallucination Detection and Fact Verification](https://doi.org/10.1145/3746027.3762061)** · ACM MM 2025 · VLM · Training-free
- **[DHCP: Detecting Hallucinations by Cross-modal Attention Pattern in Large Vision-Language Models](https://doi.org/10.1145/3746027.3755118)** · ACM MM 2025 · VLM · Training-free
- **[DASH: Detection and Assessment of Systematic Hallucinations of VLMs](https://doi.org/10.1109/ICCV51701.2025.02112)** · ICCV 2025 · VLM · Training-free
- **[Collaboration Wins More: Dual-Modal Collaborative Attention Reinforcement for Mitigating Large Vision Language Models Hallucination](https://doi.org/10.1145/3746027.3755320)** · ACM MM 2025 · VLM · Training-free
- **[CoFi-Dec: Hallucination-Resistant Decoding via Coarse-to-Fine Generative Feedback in Large Vision-Language Models](https://doi.org/10.1145/3746027.3754791)** · ACM MM 2025 · VLM · Training-free
- **[Benchmarking and Bridging Emotion Conflicts for Multimodal Emotion Reasoning](https://doi.org/10.1145/3746027.3754856)** · ACM MM 2025 · VLM · Training-free
- **[ARGUS: Hallucination and Omission Evaluation in Video-LLMs](https://doi.org/10.1109/ICCV51701.2025.01886)** · ICCV 2025 · VLM · Training-free
- **[Two Causes, Not One: Rethinking Omission and Fabrication Hallucinations in MLLMs](https://arxiv.org/abs/2509.00371)** · arXiv · VLM · Training-free
- **[Self-Consistency as a Free Lunch: Reducing Hallucinations in Vision-Language Models via Self-Reflection](https://arxiv.org/abs/2509.23236)** · arXiv · VLM · Training-free
- **[ORCA: An Agentic Reasoning Framework for Hallucination and Adversarial Robustness in Vision-Language Models](https://arxiv.org/abs/2509.15435)** · arXiv · VLM · Training-free
- **[Mitigating Visual Hallucinations via Semantic Curriculum Preference Optimization in MLLMs](https://arxiv.org/abs/2509.24491)** · arXiv · VLM · Training-based
- **[Mitigating Hallucination in Multimodal LLMs with Layer Contrastive Decoding](https://arxiv.org/abs/2509.25177)** · arXiv · VLM · Training-free
- **[Leveraging NTPs for Efficient Hallucination Detection in VLMs](https://arxiv.org/abs/2509.20379)** · arXiv · VLM · Training-free
- **[Hallucination as an Upper Bound: A New Perspective on Text-to-Image Evaluation](https://arxiv.org/abs/2509.21257)** · arXiv · VLM · Training-free
- **[GroundSight: Augmenting Vision-Language Models with Grounding Information and De-hallucination](https://arxiv.org/abs/2509.25669)** · arXiv · VLM · Training-free
- **[GHOST: Hallucination-Inducing Image Generation for Multimodal LLMs](https://arxiv.org/abs/2509.25178)** · arXiv · VLM · Training-based
- **[Exposing Hallucinations To Suppress Them: VLMs Representation Editing With Generative Anchors](https://arxiv.org/abs/2509.21997)** · arXiv · VLM · Training-free
- **[D-LEAF: Localizing and Correcting Hallucinations in Multimodal LLMs via Layer-to-head Attention Diagnostics](https://arxiv.org/abs/2509.07864)** · arXiv · VLM · Training-free
- **[ChartHal: A Fine-grained Framework Evaluating Hallucination of Large Vision Language Models in Chart Understanding](https://arxiv.org/abs/2509.17481)** · arXiv · VLM · Training-free
- **[What Makes "Good" Distractors for Object Hallucination Evaluation in Large Vision-Language Models?](https://arxiv.org/abs/2508.06530)** · arXiv · VLM · Training-free
- **[Modality Bias in LVLMs: Analyzing and Mitigating Object Hallucination via Attention Lens](https://arxiv.org/abs/2508.02419)** · arXiv · VLM · Training-free
- **[Mitigating Hallucinations in Multimodal LLMs via Object-aware Preference Optimization](https://arxiv.org/abs/2508.20181)** · arXiv · VLM · Training-based
- **[MAP: Mitigating Hallucinations in Large Vision-Language Models with Map-Level Attention Processing](https://arxiv.org/abs/2508.01653)** · arXiv · VLM · Training-free
- **[Grounding the Ungrounded: A Spectral-Graph Framework for Quantifying Hallucinations in Multimodal LLMs](https://arxiv.org/abs/2508.19366)** · arXiv · VLM · Training-free
- **[GLSim: Detecting Object Hallucinations in LVLMs via Global-Local Similarity](https://arxiv.org/abs/2508.19972)** · arXiv · VLM · Training-free
- **[ELV-Halluc: Benchmarking Semantic Aggregation Hallucinations in Long Video Understanding](https://arxiv.org/abs/2508.21496)** · arXiv · VLM · Training-free
- **[Cure or Poison? Embedding Instructions Visually Alters Hallucination in Vision-Language Models](https://arxiv.org/abs/2508.01678)** · arXiv · VLM · Training-free
- **[Understanding Visual Detail Hallucinations of Large Vision-Language Models](https://doi.org/10.24963/ijcai.2025/212)** · IJCAI 2025 · VLM · Training-free
- **[Hallucination-Aware Prompt Optimization for Text-to-Video Synthesis](https://doi.org/10.24963/ijcai.2025/1133)** · IJCAI 2025 · VLM · Training-free
- **[Hallucination Reduction in Video-Language Models via Hierarchical Multimodal Consistency](https://doi.org/10.24963/ijcai.2025/1019)** · IJCAI 2025 · VLM · Training-free
- **[Taming the Tri-Space Tension: ARC-Guided Hallucination Modeling and Control for Text-to-Image Generation](https://arxiv.org/abs/2507.04946)** · arXiv · VLM · Training-free
- **[TARS: MinMax Token-Adaptive Preference Strategy for MLLM Hallucination Reduction](https://arxiv.org/abs/2507.21584)** · arXiv · VLM · Training-free
- **[Multi-Stage Verification-Centric Framework for Mitigating Hallucination in Multi-Modal RAG](https://arxiv.org/abs/2507.20136)** · arXiv · VLM · Training-free
- **[LISA: A Layer-wise Integration and Suppression Approach for Hallucination Mitigation in Multimodal Large Language Models](https://arxiv.org/abs/2507.19110)** · arXiv · VLM · Training-free
- **[Investigating VLM Hallucination from a Cognitive Psychology Perspective: A First Step Toward Interpretation with Intriguing Observations](https://arxiv.org/abs/2507.03123)** · arXiv · VLM · Training-free
- **[From dots to faces: Individual differences in visual imagery capacity predict the content of Ganzflicker-induced hallucinations](https://arxiv.org/abs/2507.09011)** · arXiv · VLM · Training-free
- **[Extracting Visual Facts from Intermediate Layers for Mitigating Hallucinations in Multimodal Large Language Models](https://arxiv.org/abs/2507.15652)** · arXiv · VLM · Training-free
- **[Visual Evidence Prompting Mitigates Hallucinations in Large Vision-Language Models](https://doi.org/10.18653/v1/2025.acl-long.205)** · ACL 2025 · VLM · Training-free
- **[Visual Attention Never Fades: Selective Progressive Attention ReCalibration for Detailed Image Captioning in Multimodal Large Language Models](https://proceedings.mlr.press/v267/jung25c.html)** · ICML 2025 · VLM · Training-free
- **[VLM3KG:A Hallucination Mitigation Method for Vision-Language Models based on Multimodal Knowledge Graph](https://doi.org/10.1109/mlprae67267.2025.11290735)** · ICML 2025 · VLM · Training-free
- **[VADE: Visual Attention Guided Hallucination Detection and Elimination](https://doi.org/10.18653/v1/2025.findings-acl.773)** · ACL 2025 · VLM · Training-free
- **[Toward Robust Hyper-Detailed Image Captioning: A Multiagent Approach and Dual Evaluation Metrics for Factuality and Coverage](https://proceedings.mlr.press/v267/lee25aj.html)** · ICML 2025 · VLM · Training-free
- **[The Hidden Life of Tokens: Reducing Hallucination of Large Vision-Language Models Via Visual Information Steering](https://proceedings.mlr.press/v267/li25ca.html)** · ICML 2025 · VLM · Training-free
- **[Seeing Beyond Hallucinations: LLM-based Compositional Information Extraction for Multimodal Reasoning](https://doi.org/10.1145/3726302.3730081)** · SIGIR 2025 · VLM · Training-free
- **[SECOND: Mitigating Perceptual Hallucination in Vision-Language Models via Selective and Contrastive Decoding](https://proceedings.mlr.press/v267/park25c.html)** · ICML 2025 · VLM · Training-free
- **[Retrieval Visual Contrastive Decoding to Mitigate Object Hallucinations in Large Vision-Language Models](https://doi.org/10.18653/v1/2025.findings-acl.430)** · ACL 2025 · VLM · Training-free
- **📋 [Reefknot: A Comprehensive Benchmark for Relation Hallucination Evaluation, Analysis and Mitigation in Multimodal Large Language Models](https://doi.org/10.18653/v1/2025.findings-acl.322)** · ACL 2025 · VLM · Training-free
- **[Mixture of Decoding: An Attention-Inspired Adaptive Decoding Strategy to Mitigate Hallucinations in Large Vision-Language Models](https://doi.org/10.18653/v1/2025.findings-acl.448)** · ACL 2025 · VLM · Training-free
- **[Mitigating Object Hallucination in Large Vision-Language Models via Visual Attention Direct Preference Optimization](https://doi.org/10.1109/ICME59968.2025.11209127)** · ICME 2025 · VLM · Training-based
- **[Mitigating Object Hallucination in Large Vision-Language Models via Image-Grounded Guidance](https://proceedings.mlr.press/v267/zhao25j.html)** · ICML 2025 · VLM · Training-free
- **[Mitigating Hallucination in Multimodal Large Language Model via Hallucination-targeted Direct Preference Optimization](https://doi.org/10.18653/v1/2025.findings-acl.850)** · ACL 2025 · VLM · Training-based
- **[Mitigating Hallucination in Large Video-Language Models with Injected Semantics](https://doi.org/10.1109/ICME59968.2025.11209977)** · ICME 2025 · VLM · Training-free
- **[MHALO: Evaluating MLLMs as Fine-grained Hallucination Detectors](https://doi.org/10.18653/v1/2025.findings-acl.478)** · ACL 2025 · VLM · Training-free
- **[Look Twice Before You Answer: Memory-Space Visual Retracing for Hallucination Mitigation in Multimodal Large Language Models](https://proceedings.mlr.press/v267/zou25e.html)** · ICML 2025 · VLM · Training-free
- **[Instruction-Aligned Visual Attention for Mitigating Hallucinations in Large Vision-Language Models](https://doi.org/10.1109/ICME59968.2025.11209139)** · ICME 2025 · VLM · Training-free
- **[Insight Over Sight: Exploring the Vision-Knowledge Conflicts in Multimodal LLMs](https://doi.org/10.18653/v1/2025.acl-long.872)** · ACL 2025 · VLM · Training-free
- **[Focus on What Matters: Enhancing Medical Vision-Language Models with Automatic Attention Alignment Tuning](https://doi.org/10.18653/v1/2025.acl-long.460)** · ACL 2025 · VLM · Training-based
- **[Don't Miss the Forest for the Trees: Attentional Vision Calibration for Large Vision Language Models](https://doi.org/10.18653/v1/2025.findings-acl.99)** · ACL 2025 · VLM · Training-free
- **[Cracking the Code of Hallucination in LVLMs with Vision-aware Head Divergence](https://doi.org/10.18653/v1/2025.acl-long.175)** · ACL 2025 · VLM · Training-free
- **[Can Hallucination Correction Improve Video-Language Alignment?](https://doi.org/10.18653/v1/2025.findings-acl.1314)** · ACL 2025 · VLM · Training-free
- **[CLAIM: Mitigating Multilingual Object Hallucination in Large Vision-Language Models with Cross-Lingual Attention Intervention](https://doi.org/10.18653/v1/2025.acl-long.640)** · ACL 2025 · VLM · Training-free
- **[Beyond Multimodal Hallucinations: Enhancing LVLMs through Hallucination-Aware Direct Preference Optimization](https://doi.org/10.1109/ICME59968.2025.11209377)** · ICME 2025 · VLM · Training-based
- **[Activation Steering Decoding: Mitigating Hallucination in Large Vision-Language Models through Bidirectional Hidden State Intervention](https://doi.org/10.18653/v1/2025.acl-long.634)** · ACL 2025 · VLM · Training-free
- **[When Semantics Mislead Vision: Mitigating Large Multimodal Models Hallucinations in Scene Text Spotting and Understanding](https://arxiv.org/abs/2506.05551)** · arXiv · VLM · Training-free
- **[Seeing is Believing? Mitigating OCR Hallucinations in Multimodal Large Language Models](https://arxiv.org/abs/2506.20168)** · arXiv · VLM · Training-free
- **[Revisit What You See: Disclose Language Prior in Vision Tokens for Efficient Guided Decoding of LVLMs](https://arxiv.org/abs/2506.09522)** · arXiv · VLM · Training-free
- **[ReCo: Reminder Composition Mitigates Hallucinations in Vision-Language Models](https://arxiv.org/abs/2506.22636)** · arXiv · VLM · Training-free
- **[Mitigating Behavioral Hallucination in Multimodal Large Language Models for Sequential Images](https://arxiv.org/abs/2506.07184)** · arXiv · VLM · Training-free
- **[MDSAM:Memory-Driven Sparse Attention Matrix for LVLMs Hallucination Mitigation](https://arxiv.org/abs/2506.17664)** · arXiv · VLM · Training-free
- **[Hallucinate, Ground, Repeat: A Framework for Generalized Visual Relationship Detection](https://arxiv.org/abs/2506.05651)** · arXiv · VLM · Training-free
- **[HalluRNN: Mitigating Hallucinations via Recurrent Cross-Layer Reasoning in Large Vision-Language Models](https://arxiv.org/abs/2506.17587)** · arXiv · VLM · Training-free
- **[CAI: Caption-Sensitive Attention Intervention for Mitigating Object Hallucination in Large Vision-Language Models](https://arxiv.org/abs/2506.23590)** · arXiv · VLM · Training-free
- **[VidHalluc: Evaluating Temporal Hallucinations in Multimodal Large Language Models for Video Understanding](https://openaccess.thecvf.com/content/CVPR2025/html/Li_VidHalluc_Evaluating_Temporal_Hallucinations_in_Multimodal_Large_Language_Models_for_CVPR_2025_paper.html)** · CVPR 2025 · VLM · Training-free
- **[VASparse: Towards Efficient Visual Hallucination Mitigation via Visual-Aware Token Sparsification](https://openaccess.thecvf.com/content/CVPR2025/html/Zhuang_VASparse_Towards_Efficient_Visual_Hallucination_Mitigation_via_Visual-Aware_Token_Sparsification_CVPR_2025_paper.html)** · CVPR 2025 · VLM · Training-free
- **[Stop Learning it all to Mitigate Visual Hallucination, Focus on the Hallucination Target](https://openaccess.thecvf.com/content/CVPR2025/html/Yoon_Stop_Learning_it_all_to_Mitigate_Visual_Hallucination_Focus_on_CVPR_2025_paper.html)** · CVPR 2025 · VLM · Training-free
- **[Seeing Far and Clearly: Mitigating Hallucinations in MLLMs with Attention Causal Decoding](https://openaccess.thecvf.com/content/CVPR2025/html/Tang_Seeing_Far_and_Clearly_Mitigating_Hallucinations_in_MLLMs_with_Attention_CVPR_2025_paper.html)** · CVPR 2025 · VLM · Training-free
- **📋 [PhD: A ChatGPT-Prompted Visual Hallucination Evaluation Dataset](https://openaccess.thecvf.com/content/CVPR2025/html/Liu_PhD_A_ChatGPT-Prompted_Visual_Hallucination_Evaluation_Dataset_CVPR_2025_paper.html)** · CVPR 2025 · VLM · Training-free
- **[ODE: Open-Set Evaluation of Hallucinations in Multimodal Large Language Models](https://openaccess.thecvf.com/content/CVPR2025/html/Tu_ODE_Open-Set_Evaluation_of_Hallucinations_in_Multimodal_Large_Language_Models_CVPR_2025_paper.html)** · CVPR 2025 · VLM · Training-free
- **[Nullu: Mitigating Object Hallucinations in Large Vision-Language Models via HalluSpace Projection](https://openaccess.thecvf.com/content/CVPR2025/html/Yang_Nullu_Mitigating_Object_Hallucinations_in_Large_Vision-Language_Models_via_HalluSpace_CVPR_2025_paper.html)** · CVPR 2025 · VLM · Training-free
- **[Mitigating Object Hallucinations in Large Vision-Language Models with Assembly of Global and Local Attention](https://openaccess.thecvf.com/content/CVPR2025/html/An_Mitigating_Object_Hallucinations_in_Large_Vision-Language_Models_with_Assembly_of_CVPR_2025_paper.html)** · CVPR 2025 · VLM · Training-free
- **[Mitigating Hallucinations in Multimodal Spatial Relations through Constraint-Aware Prompting](https://doi.org/10.18653/v1/2025.findings-naacl.192)** · NAACL 2025 · VLM · Training-free
- **[Mitigating Hallucinations in Multi-modal Large Language Models via Image Token Attention-Guided Decoding](https://doi.org/10.18653/v1/2025.naacl-long.75)** · NAACL 2025 · VLM · Training-free
- **[Mitigating Hallucinations in Large Vision-Language Models via Summary-Guided Decoding](https://doi.org/10.18653/v1/2025.findings-naacl.235)** · NAACL 2025 · VLM · Training-free
- **[Mitigating Hallucinations in Large Vision-Language Models via DPO: On-Policy Data Hold the Key](https://openaccess.thecvf.com/content/CVPR2025/html/Yang_Mitigating_Hallucinations_in_Large_Vision-Language_Models_via_DPO_On-Policy_Data_CVPR_2025_paper.html)** · CVPR 2025 · VLM · Training-based
- **[MASH-VLM: Mitigating Action-Scene Hallucination in Video-LLMs through Disentangled Spatial-Temporal Representations](https://openaccess.thecvf.com/content/CVPR2025/html/Bae_MASH-VLM_Mitigating_Action-Scene_Hallucination_in_Video-LLMs_through_Disentangled_Spatial-Temporal_Representations_CVPR_2025_paper.html)** · CVPR 2025 · VLM · Training-free
- **[ICT: Image-Object Cross-Level Trusted Intervention for Mitigating Object Hallucination in Large Vision-Language Models](https://openaccess.thecvf.com/content/CVPR2025/html/Chen_ICT_Image-Object_Cross-Level_Trusted_Intervention_for_Mitigating_Object_Hallucination_in_CVPR_2025_paper.html)** · CVPR 2025 · VLM · Training-free
- **[IBD: Alleviating Hallucinations in Large Vision-Language Models via Image-Biased Decoding](https://openaccess.thecvf.com/content/CVPR2025W/TMM-OpenWorld/html/Zhu_IBD_Alleviating_Hallucinations_in_Large_Vision-Language_Models_via_Image-Biased_Decoding_CVPRW_2025_paper.html)** · CVPRW 2025 · VLM · Training-free
- **[HalLoc: Token-level Localization of Hallucinations for Vision Language Models](https://openaccess.thecvf.com/content/CVPR2025/html/Park_HalLoc_Token-level_Localization_of_Hallucinations_for_Vision_Language_Models_CVPR_2025_paper.html)** · CVPR 2025 · VLM · Training-free
- **[Evaluating and Mitigating Object Hallucination in Large Vision-Language Models: Can They Still See Removed Objects?](https://doi.org/10.18653/v1/2025.naacl-long.349)** · NAACL 2025 · VLM · Training-free
- **[Devils in Middle Layers of Large Vision-Language Models: Interpreting, Detecting and Mitigating Object Hallucinations via Attention Lens](https://openaccess.thecvf.com/content/CVPR2025/html/Jiang_Devils_in_Middle_Layers_of_Large_Vision-Language_Models_Interpreting_Detecting_CVPR_2025_paper.html)** · CVPR 2025 · VLM · Training-free
- **[ClearSight: Visual Signal Enhancement for Object Hallucination Mitigation in Multimodal Large Language Models](https://openaccess.thecvf.com/content/CVPR2025/html/Yin_ClearSight_Visual_Signal_Enhancement_for_Object_Hallucination_Mitigation_in_Multimodal_CVPR_2025_paper.html)** · CVPR 2025 · VLM · Training-free
- **[Black-Box Visual Prompt Engineering for Mitigating Object Hallucination in Large Vision Language Models](https://doi.org/10.18653/v1/2025.naacl-short.45)** · NAACL 2025 · VLM · Training-free
- **[Beyond Logit Lens: Contextual Embeddings for Robust Hallucination Detection & Grounding in VLMs](https://doi.org/10.18653/v1/2025.naacl-long.488)** · NAACL 2025 · VLM · Training-free
- **[BIMA: Bijective Maximum Likelihood Learning Approach to Hallucination Prediction and Mitigation in Large Vision-Language Models](https://openaccess.thecvf.com/content/CVPR2025W/Precognition/html/Tran_BIMA_Bijective_Maximum_Likelihood_Learning_Approach_to_Hallucination_Prediction_and_CVPRW_2025_paper.html)** · CVPRW 2025 · VLM · Training-free
- **[Antidote: A Unified Framework for Mitigating LVLM Hallucinations in Counterfactual Presupposition and Object Perception](https://openaccess.thecvf.com/content/CVPR2025/html/Wu_Antidote_A_Unified_Framework_for_Mitigating_LVLM_Hallucinations_in_Counterfactual_CVPR_2025_paper.html)** · CVPR 2025 · VLM · Training-free
- **📋 [3D-GRAND: A Million-Scale Dataset for 3D-LLMs with Better Grounding and Less Hallucination](https://openaccess.thecvf.com/content/CVPR2025/html/Yang_3D-GRAND_A_Million-Scale_Dataset_for_3D-LLMs_with_Better_Grounding_and_CVPR_2025_paper.html)** · CVPR 2025 · VLM · Training-free
- **[Qwen Look Again: Guiding Vision-Language Reasoning Models to Re-attention Visual Information](https://arxiv.org/abs/2505.23558)** · arXiv · VLM · Training-based
- **[Preemptive Hallucination Reduction: An Input-Level Approach for Multimodal Language Model](https://arxiv.org/abs/2505.24007)** · arXiv · VLM · Training-free
- **[OViP: Online Vision-Language Preference Learning for VLM Hallucination](https://arxiv.org/abs/2505.15963)** · arXiv · VLM · Training-based
- **[Mitigating Hallucinations via Inter-Layer Consistency Aggregation in Large Vision-Language Models](https://arxiv.org/abs/2505.12343)** · arXiv · VLM · Training-free
- **[Mitigating Hallucinations in Large Vision-Language Models via Adaptive Attention Calibration](https://arxiv.org/abs/2505.21472)** · arXiv · VLM · Training-free
- **[MTRE: Multi-Token Reliability Estimation for Hallucination Detection in VLMs](https://arxiv.org/abs/2505.11741)** · arXiv · VLM · Training-free
- **📋 [Localizing Before Answering: A Hallucination Evaluation Benchmark for Grounded Medical Multimodal LLMs](https://arxiv.org/abs/2505.00744)** · arXiv · VLM · Training-free
- **[Image Tokens Matter: Mitigating Hallucination in Discrete Tokenizer-based Large Vision-Language Models via Latent Editing](https://arxiv.org/abs/2505.21547)** · arXiv · VLM · Training-free
- **[EmotionHallucer: Evaluating Emotion Hallucinations in Multimodal Large Language Models](https://arxiv.org/abs/2505.11405)** · arXiv · VLM · Training-free
- **[Cross-Image Contrastive Decoding: Precise, Lossless Suppression of Language Priors in Large Vision-Language Models](https://arxiv.org/abs/2505.10634)** · arXiv · VLM · Training-free
- **[Causal-LLaVA: Causal Disentanglement for Mitigating Hallucination in Multimodal Large Language Models](https://arxiv.org/abs/2505.19474)** · arXiv · VLM · Training-free
- **[A Comprehensive Analysis for Visual Object Hallucination in Large Vision-Language Models](https://arxiv.org/abs/2505.01958)** · arXiv · VLM · Training-free
- **[The Mirage of Performance Gains: Why Contrastive Decoding Fails to Mitigate Object Hallucinations in MLLMs?](https://arxiv.org/abs/2504.10020)** · arXiv · VLM · Training-free
- **[TARAC: Mitigating Hallucination in LVLMs via Temporal Attention Real-time Accumulative Connection](https://arxiv.org/abs/2504.04099)** · arXiv · VLM · Training-free
- **[ResNetVLLM-2: Addressing ResNetVLLM's Multi-Modal Hallucinations](https://arxiv.org/abs/2504.14429)** · arXiv · VLM · Training-free
- **[PaMi-VDPO: Mitigating Video Hallucinations by Prompt-Aware Multi-Instance Video Preference Learning](https://arxiv.org/abs/2504.05810)** · arXiv · VLM · Training-based
- **[Low-hallucination Synthetic Captions for Large-Scale Vision-Language Model Pre-training](https://arxiv.org/abs/2504.13123)** · arXiv · VLM · Training-free
- **[Hydra: An Agentic Reasoning Approach for Enhancing Adversarial Robustness and Mitigating Hallucinations in Vision-Language Models](https://arxiv.org/abs/2504.14395)** · arXiv · VLM · Training-free
- **[Generate, but Verify: Reducing Hallucination in Vision-Language Models with Retrospective Resampling](https://arxiv.org/abs/2504.13169)** · arXiv · VLM · Training-free
- **[Efficient Contrastive Decoding with Probabilistic Hallucination Detection - Mitigating Hallucinations in Large Vision Language Models -](https://arxiv.org/abs/2504.12137)** · arXiv · VLM · Training-free
- **[Don't Deceive Me: Mitigating Gaslighting through Attention Reallocation in LMMs](https://arxiv.org/abs/2504.09456)** · arXiv · VLM · Training-free
- **[Visual Description Grounding Reduces Hallucinations and Boosts Reasoning in LVLMs](https://openreview.net/forum?id=3PRvlT8b1R)** · ICLR 2025 · VLM · Training-free
- **[Understanding and Mitigating Hallucination in Large Vision-Language Models via Modular Attribution and Intervention](https://openreview.net/forum?id=Bjq4W7P2Us)** · ICLR 2025 · VLM · Training-free
- **[Self-Introspective Decoding: Alleviating Hallucinations for Large Vision-Language Models](https://openreview.net/forum?id=rsZwwjYHuD)** · ICLR 2025 · VLM · Training-free
- **[Self-Correcting Decoding with Generative Feedback for Mitigating Hallucinations in Large Vision-Language Models](https://openreview.net/forum?id=tTBXePRKSx)** · ICLR 2025 · VLM · Training-free
- **[See What You Are Told: Visual Attention Sink in Large Multimodal Models](https://openreview.net/forum?id=7uDI7w5RQA)** · ICLR 2025 · VLM · Training-free
- **[Reducing Hallucinations in Vision-Language Models via Latent Space Steering](https://openreview.net/forum?id=LBl7Hez0fF)** · ICLR 2025 · VLM · Training-free
- **[Reducing Hallucinations in Large Vision-Language Models via Latent Space Steering](https://openreview.net/forum?id=LBl7Hez0fF)** · ICLR 2025 · VLM · Training-free
- **[PerturboLLaVA: Reducing Multimodal Hallucinations with Perturbative Visual Training](https://openreview.net/forum?id=j4LITBSUjs)** · ICLR 2025 · VLM · Training-free
- **[Mitigating Object Hallucination in MLLMs via Data-augmented Phrase-level Alignment](https://openreview.net/forum?id=yG1fW8igzP)** · ICLR 2025 · VLM · Training-free
- **[Mitigating Modality Prior-Induced Hallucinations in Multimodal Large Language Models via Deciphering Attention Causality](https://openreview.net/forum?id=AV7OXVlAyi)** · ICLR 2025 · VLM · Training-free
- **[Mitigating Hallucinations on Object Attributes using Multiview Images and Negative Instructions](https://doi.org/10.1109/ICASSP49660.2025.10888481)** · ICASSP 2025 · VLM · Training-free
- **[MLLMs Know Where to Look: Training-free Perception of Small Visual Details with Multimodal LLMs](https://openreview.net/forum?id=DgaY5mDdmT)** · ICLR 2025 · VLM · Training-free
- **[MLLM can see? Dynamic Correction Decoding for Hallucination Mitigation](https://openreview.net/forum?id=4z3IguA4Zg)** · ICLR 2025 · VLM · Training-free
- **[Intervening Anchor Token: Decoding Strategy in Alleviating Hallucinations for MLLMs](https://openreview.net/forum?id=zGb4WgCW5i)** · ICLR 2025 · VLM · Training-free
- **[Interpreting and Editing Vision-Language Representations to Mitigate Hallucinations](https://openreview.net/forum?id=94kQgWXojH)** · ICLR 2025 · VLM · Training-free
- **[Explore the Hallucination on Low-level Perception for MLLMs](https://doi.org/10.1109/ICASSP49660.2025.10888437)** · ICASSP 2025 · VLM · Training-free
- **[Do You Keep an Eye on What I Ask? Mitigating Multimodal Hallucination via Attention-Guided Ensemble Decoding](https://openreview.net/forum?id=ziw5bzg2NO)** · ICLR 2025 · VLM · Training-free
- **[Damo: Decoding by Accumulating Activations Momentum for Mitigating Hallucinations in Vision-Language Models](https://openreview.net/forum?id=JUr0YOMvZA)** · ICLR 2025 · VLM · Training-free
- **[UniVRSE: Unified Vision-conditioned Response Semantic Entropy for Hallucination Detection in Medical Vision-Language Models](https://arxiv.org/abs/2503.20504)** · arXiv · VLM · Training-free
- **[TruthPrInt: Mitigating LVLM Object Hallucination Via Latent Truthful-Guided Pre-Intervention](https://arxiv.org/abs/2503.10602)** · arXiv · VLM · Training-free
- **[TPC: Cross-Temporal Prediction Connection for Vision-Language Model Hallucination Reduction](https://arxiv.org/abs/2503.04457)** · arXiv · VLM · Training-free
- **[MedHEval: Benchmarking Hallucinations and Mitigation Strategies in Medical Large Vision-Language Models](https://arxiv.org/abs/2503.02157)** · arXiv · VLM · Training-free
- **[Hallucinatory Image Tokens: A Training-free EAZY Approach on Detecting and Mitigating Object Hallucinations in LVLMs](https://arxiv.org/abs/2503.07772)** · arXiv · VLM · Training-free
- **📋 [Exploring Hallucination of Large Multimodal Models in Video Understanding: Benchmark, Analysis and Mitigation](https://arxiv.org/abs/2503.19622)** · arXiv · VLM · Training-free
- **[Don't Fight Hallucinations, Use Them: Estimating Image Realism using NLI over Atomic Facts](https://arxiv.org/abs/2503.15948)** · arXiv · VLM · Training-free
- **[Attention Hijackers: Detect and Disentangle Attention Hijacking in LVLMs for Hallucination Mitigation](https://arxiv.org/abs/2503.08216)** · arXiv · VLM · Training-free
- **[Who Brings the Frisbee: Probing Hidden Hallucination Factors in Large Vision-Language Model via Causality Analysis](https://doi.org/10.1109/WACV61041.2025.00597)** · WACV 2025 · VLM · Training-free
- **[Make VLM Recognize Visual Hallucination on Cartoon Character Image with Pose Information](https://doi.org/10.1109/WACV61041.2025.00527)** · WACV 2025 · VLM · Training-free
- **[Enhancing Weakly-Supervised Object Detection on Static Images through (Hallucinated) Motion](https://doi.org/10.1109/WACVW65960.2025.00117)** · WACV 2025 · VLM · Training-free
- **[Aerial Mirage: Unmasking Hallucinations in Large Vision Language Models](https://doi.org/10.1109/WACV61041.2025.00537)** · WACV 2025 · VLM · Training-free
- **[Understanding and Evaluating Hallucinations in 3D Visual Language Models](https://arxiv.org/abs/2502.15888)** · arXiv · VLM · Training-free
- **[The Role of Background Information in Reducing Object Hallucination in Vision-Language Models: Insights from Cutoff API Prompting](https://arxiv.org/abs/2502.15389)** · arXiv · VLM · Training-free
- **[SegSub: Evaluating Robustness to Knowledge Conflicts and Hallucinations in Vision-Language Models](https://arxiv.org/abs/2502.14908)** · arXiv · VLM · Training-free
- **[Reducing Hallucinations of Medical Multimodal Large Language Models with Visual Retrieval-Augmented Generation](https://arxiv.org/abs/2502.15040)** · arXiv · VLM · Training-free
- **[Mitigating Object Hallucinations in Large Vision-Language Models via Attention Calibration](https://arxiv.org/abs/2502.01969)** · arXiv · VLM · Training-free
- **[Mitigating Hallucinations in Large Vision-Language Models with Internal Fact-based Contrastive Decoding](https://arxiv.org/abs/2502.01056)** · arXiv · VLM · Training-free
- **📋 [MedHallTune: An Instruction-Tuning Benchmark for Mitigating Medical Hallucination in Vision-Language Models](https://arxiv.org/abs/2502.20780)** · arXiv · VLM · Training-free
- **[MINT: Mitigating Hallucinations in Large Vision-Language Models via Token Reduction](https://arxiv.org/abs/2502.00717)** · arXiv · VLM · Training-free
- **[Exploring Causes and Mitigation of Hallucinations in Large Vision Language Models](https://arxiv.org/abs/2502.16842)** · arXiv · VLM · Training-free
- **[DeepSeek on a Trip: Inducing Targeted Visual Hallucinations via Representation Vulnerabilities](https://arxiv.org/abs/2502.07905)** · arXiv · VLM · Training-free
- **[CutPaste&Find: Efficient Multimodal Hallucination Detector with Visual-aid Knowledge Base](https://arxiv.org/abs/2502.12591)** · arXiv · VLM · Training-free
- **[MoLE: Decoding by Mixture of Layer Experts Alleviates Hallucination in Large Vision-Language Models](https://doi.org/10.1609/aaai.v39i18.34056)** · AAAI 2025 · VLM · Training-free
- **[Mitigating Hallucinations in Large Vision-Language Models by Adaptively Constraining Information Flow](https://doi.org/10.1609/aaai.v39i22.34512)** · AAAI 2025 · VLM · Training-free
- **[Evaluating Image Hallucination in Text-to-Image Generation with Question-Answering](https://doi.org/10.1609/aaai.v39i25.34827)** · AAAI 2025 · VLM · Training-free
- **[Detecting and Mitigating Hallucination in Large Vision Language Models via Fine-Grained AI Feedback](https://doi.org/10.1609/aaai.v39i24.34744)** · AAAI 2025 · VLM · Training-free
- **[ConVis: Contrastive Decoding with Hallucination Visualization for Mitigating Hallucinations in Multimodal Large Language Models](https://doi.org/10.1609/aaai.v39i6.32689)** · AAAI 2025 · VLM · Training-free
- **[Combating Multimodal LLM Hallucination via Bottom-Up Holistic Reasoning](https://doi.org/10.1609/aaai.v39i8.32913)** · AAAI 2025 · VLM · Training-free
- **[Poison as Cure: Visual Noise for Mitigating Object Hallucinations in LVMs](https://arxiv.org/abs/2501.19164)** · arXiv · VLM · Training-free
- **[PAINT: Paying Attention to INformed Tokens to Mitigate Hallucination in Large Vision-Language Model](https://arxiv.org/abs/2501.12206)** · arXiv · VLM · Training-free
- **📋 [Measuring and Mitigating Hallucinations in Vision-Language Dataset Generation for Remote Sensing](https://arxiv.org/abs/2501.14905)** · arXiv · VLM · Training-free
- **[Evaluating Hallucination in Large Vision-Language Models based on Context-Aware Object Similarities](https://arxiv.org/abs/2501.15046)** · arXiv · VLM · Training-free
- **[EAGLE: Enhanced Visual Grounding Minimizes Hallucinations in Instructional Multimodal Models](https://arxiv.org/abs/2501.02699)** · arXiv · VLM · Training-free
- **[RRHF-V: Ranking Responses to Mitigate Hallucinations in Multimodal Large Language Models with Human Feedback](https://aclanthology.org/2025.coling-main.454/)** · COLING 2025 · VLM · Training-free
- **[Look, Compare, Decide: Alleviating Hallucination in Large Vision-Language Models via Multi-View Multi-Path Reasoning](https://aclanthology.org/2025.coling-main.299/)** · COLING 2025 · VLM · Training-free
- **[Visual Multi-Agent System: Mitigating Hallucination Snowballing via Visual Flow]()** · Unlabeled · VLM · Training-free
- **[RAR: Reversing Visual Attention Re-sinking for Unlocking Potential in Multimodal Large Language Models]()** · Unlabeled · VLM · Training-free
- **[Mitigating Hallucination for Large Vision Language Model by Inter-Modality Correlation Calibration Decoding]()** · Unlabeled · VLM · Training-free
- **[Mitigating Hallucination Through Theory-Consistent Symmetric Multimodal Preference Optimization](http://papers.nips.cc/paper_files/paper/2025/hash/a1718f361df32ff3a1fc224f8673c556-Abstract-Conference.html)** · Unlabeled · VLM · Training-based
- **[Visual hallucination detection in large vision-language models via evidential conflict](https://doi.org/10.1016/j.ijar.2025.109507)** · Int. J. Approx. Reason. 2025 · VLM · Training-free
- **[VDIS: Combating Object Hallucination in Multimodal Large Language Models](https://doi.org/10.1007/978-981-95-5696-0_28)** · PRCV 2025 · VLM · Training-free
- **[Unified Triplet-Level Hallucination Evaluation for Large Vision-Language Models](https://openreview.net/forum?id=iNywrSPpvc)** · TMLR 2025 · VLM · Training-free
- **[Tackling Hallucination from Conditional Models for Medical Image Reconstruction with DynamicDPS](https://doi.org/10.1007/978-3-032-04965-0_56)** · MICCAI 2025 · VLM · Training-free
- **[Reducing extrinsic hallucination in multimodal abstractive summaries with post-processing technique](https://doi.org/10.1007/s00521-024-10895-8)** · Neural Comput. Appl. 2025 · VLM · Training-free
- **📋 [ReSelfVerMM: mitigating hallucination in multimodal LLMs through dataset reconstruction and self-verification](https://doi.org/10.1117/12.3072360)** · Second International Conference on Image Processing and Artificial Intelligence (ICIPAI 2025) 2025 · VLM · Training-free
- **[Prescribing the Right Remedy: Mitigating Hallucinations in Large Vision-Language Models via Targeted Instruction Tuning](https://doi.org/10.1016/j.ins.2025.122361)** · Inf. Sci. 2025 · VLM · Training-based
- **[Mitigating Hallucinations in Large Vision-Language Models via Reasoning Uncertainty-Guided Refinement](https://doi.org/10.1109/TMM.2025.3599076)** · TMM 2025 · VLM · Training-free
- **[Mirage in the Eyes: Hallucination Attack on Multi-modal Large Language Models with Only Attention Sink](https://www.usenix.org/conference/usenixsecurity25/presentation/wang-yining)** · USENIX Security Symposium 2025 · VLM · Training-free
- **[MetaToken: Detecting Hallucination in Image Descriptions by Meta Classification](https://doi.org/10.5220/0013165700003912)** · VISIGRAPP (2) - VISAPP 2025 · VLM · Training-free
- **📋 [Hallucination-Aware Multimodal Benchmark for Gastrointestinal Image Analysis with Large Vision-Language Models](https://doi.org/10.1007/978-3-032-05127-1_23)** · MICCAI 2025 · VLM · Training-free
- **[HalCECE: A Framework for Explainable Hallucination Detection through Conceptual Counterfactuals in Image Captioning](https://doi.org/10.1007/978-3-032-08330-2_5)** · xAI 2025 · VLM · Training-free
- **[DA-DPO: Cost-efficient Difficulty-aware Preference Optimization for Reducing MLLM Hallucinations](https://openreview.net/forum?id=M52CgPcgGx)** · TMLR 2025 · VLM · Training-based
- **[Context-Aware Image Caption Editing via Hallucination-Resistant Visual Instruction Tuning](https://doi.org/10.1109/ICCVW69036.2025.00615)** · ICCVW 2025 · VLM · Training-based
- **[Conditional Hallucinations for Image Compression](https://doi.org/10.1109/DCC62719.2025.00043)** · DCC 2025 · VLM · Training-free
- **[Can We Trust Large Language Models for Video Analysis: An Exploration of Hallucination in Multimodal LLMs](https://doi.org/10.22318/icls2025.704957)** · International Conference of the Learning Sciences 2025 · VLM · Training-free
- **[Beyond Logit Lens: Contextual Embeddings for Robust Hallucination Detection &amp; Grounding in VLMs](https://doi.org/10.18653/v1/2025.naacl-long.488)** · Comput. Linguistics 2025 · VLM · Training-free
- **[Alleviating Hallucination in Large Vision-Language Models with Active Retrieval Augmentation](https://doi.org/10.1145/3742434)** · TOMM 2025 · VLM · Training-free

</details>

<details>
<summary>📅 2024 · 106 papers</summary>

- **[VORD: Visual Ordinal Calibration for Mitigating Object Hallucinations in Large Vision-Language Models](https://arxiv.org/abs/2412.15739)** · arXiv · VLM · Training-free
- **[Towards a Systematic Evaluation of Hallucinations in Large-Vision Language Models](https://arxiv.org/abs/2412.20622)** · arXiv · VLM · Training-free
- **[Hallucination Elimination and Semantic Enhancement Framework for Vision-Language Models in Traffic Scenarios](https://arxiv.org/abs/2412.07518)** · arXiv · VLM · Training-free
- **[Evaluating Hallucination in Text-to-Image Diffusion Models with Scene-Graph based Question-Answering Agent](https://arxiv.org/abs/2412.05722)** · arXiv · VLM · Training-free
- **[Delve into Visual Contrastive Decoding for Hallucination Mitigation of Large Vision-Language Models](https://arxiv.org/abs/2412.06775)** · arXiv · VLM · Training-free
- **[Seeing the Image: Prioritizing Visual Correlation by Contrastive Alignment](http://papers.nips.cc/paper_files/paper/2024/hash/37294f033582ac0064bf90fa557c2573-Abstract-Conference.html)** · NeurIPS 2024 · VLM · Training-free
- **[Multi-Object Hallucination in Vision Language Models](http://papers.nips.cc/paper_files/paper/2024/hash/4ea4a1ea4d9ff273688c8e92bd087112-Abstract-Conference.html)** · NeurIPS 2024 · VLM · Training-free
- **[CODE: Contrasting Self-generated Description to Combat Hallucination in Large Multi-modal Models](http://papers.nips.cc/paper_files/paper/2024/hash/f1592b0d4ab737e18bb1899484d28d96-Abstract-Conference.html)** · NeurIPS 2024 · VLM · Training-free
- **[Alleviating Hallucinations in Large Vision-Language Models through Hallucination-Induced Optimization](http://papers.nips.cc/paper_files/paper/2024/hash/dde040998d82553cf7f689e8ae173d5a-Abstract-Conference.html)** · NeurIPS 2024 · VLM · Training-free
- **📋 [ViBe: A Text-to-Video Benchmark for Evaluating Hallucination in Large Multimodal Models](https://arxiv.org/abs/2411.10867)** · arXiv · VLM · Training-free
- **[VaLiD: Mitigating the Hallucination of Large Vision Language Models by Visual Layer Fusion Contrastive Decoding](https://arxiv.org/abs/2411.15839)** · arXiv · VLM · Training-free
- **[VL-Uncertainty: Detecting Hallucination in Large Vision-Language Model via Uncertainty Estimation](https://arxiv.org/abs/2411.11919)** · arXiv · VLM · Training-free
- **[Thinking Before Looking: Improving Multimodal LLM Reasoning via Mitigating Visual Hallucination](https://arxiv.org/abs/2411.12591)** · arXiv · VLM · Training-free
- **[Seeing Clearly by Layer Two: Enhancing Attention Heads to Alleviate Hallucination in LVLMs](https://arxiv.org/abs/2411.09968)** · arXiv · VLM · Training-free
- **[H-POPE: Hierarchical Polling-based Probing Evaluation of Hallucinations in Large Vision-Language Models](https://arxiv.org/abs/2411.04077)** · arXiv · VLM · Training-free
- **[CATCH: Complementary Adaptive Token-level Contrastive Decoding to Mitigate Hallucinations in LVLMs](https://arxiv.org/abs/2411.12713)** · arXiv · VLM · Training-free
- **[What if...?: Thinking Counterfactual Keywords Helps to Mitigate Hallucination in Large Multi-modal Models](https://doi.org/10.18653/v1/2024.findings-emnlp.626)** · EMNLP 2024 · VLM · Training-free
- **[VGA: Vision GUI Assistant - Minimizing Hallucinations through Image-Centric Fine-Tuning](https://doi.org/10.18653/v1/2024.findings-emnlp.68)** · EMNLP 2024 · VLM · Training-free
- **[V-DPO: Mitigating Hallucination in Large Vision Language Models via Vision-Guided Direct Preference Optimization](https://doi.org/10.18653/v1/2024.findings-emnlp.775)** · EMNLP 2024 · VLM · Training-based
- **[Reference-free Hallucination Detection for Large Vision-Language Models](https://doi.org/10.18653/v1/2024.findings-emnlp.262)** · EMNLP 2024 · VLM · Training-free
- **[Investigating and Mitigating Object Hallucinations in Pretrained Vision-Language (CLIP) Models](https://doi.org/10.18653/v1/2024.emnlp-main.1016)** · EMNLP 2024 · VLM · Training-free
- **[HELPD: Mitigating Hallucination of LVLMs by Hierarchical Feedback Learning with Vision-enhanced Penalty Decoding](https://doi.org/10.18653/v1/2024.emnlp-main.105)** · EMNLP 2024 · VLM · Training-free
- **[Game on Tree: Visual Hallucination Mitigation via Coarse-to-Fine View Tree and Game Theory](https://doi.org/10.18653/v1/2024.emnlp-main.998)** · EMNLP 2024 · VLM · Training-free
- **[FaithScore: Fine-grained Evaluations of Hallucinations in Large Vision-Language Models](https://doi.org/10.18653/v1/2024.findings-emnlp.290)** · EMNLP 2024 · VLM · Training-free
- **[EFUF: Efficient Fine-Grained Unlearning Framework for Mitigating Hallucinations in Multimodal Large Language Models](https://doi.org/10.18653/v1/2024.emnlp-main.67)** · EMNLP 2024 · VLM · Training-based
- **[Does Object Grounding Really Reduce Hallucination of Large Vision-Language Models?](https://doi.org/10.18653/v1/2024.emnlp-main.159)** · EMNLP 2024 · VLM · Training-free
- **[DAMRO: Dive into the Attention Mechanism of LVLM to Reduce Object Hallucination](https://doi.org/10.18653/v1/2024.emnlp-main.439)** · EMNLP 2024 · VLM · Training-free
- **[AutoHallusion: Automatic Generation of Hallucination Benchmarks for Vision-Language Models](https://doi.org/10.18653/v1/2024.findings-emnlp.493)** · EMNLP 2024 · VLM · Training-free
- **[Unraveling Cross-Modality Knowledge Conflict in Large Vision-Language Models](https://arxiv.org/abs/2410.03659)** · arXiv · VLM · Training-free
- **[Magnifier Prompt: Tackling Multimodal Hallucination via Extremely Simple Instructions](https://arxiv.org/abs/2410.11701)** · arXiv · VLM · Training-free
- **[LongHalQA: Long-Context Hallucination Evaluation for MultiModal Large Language Models](https://arxiv.org/abs/2410.09962)** · arXiv · VLM · Training-free
- **[Automatically Generating Visual Hallucination Test Cases for Multimodal Large Language Models](https://arxiv.org/abs/2410.11242)** · arXiv · VLM · Training-free
- **📚 [A Survey of Hallucination in Large Visual Language Models](https://arxiv.org/abs/2410.15359)** · arXiv · VLM · Training-free
- **[Tackling Structural Hallucination in Image Translation with Local Diffusion](https://doi.org/10.1007/978-3-031-73004-7_6)** · ECCV 2024 · VLM · Training-free
- **[Reflective Instruction Tuning: Mitigating Hallucinations in Large Vision-Language Models](https://doi.org/10.1007/978-3-031-73113-6_12)** · ECCV 2024 · VLM · Training-based
- **[RAG-Guided Large Language Models for Visual Spatial Description with Adaptive Hallucination Corrector](https://doi.org/10.1145/3664647.3688990)** · ACM MM 2024 · VLM · Training-free
- **[Paying More Attention to Image: A Training-Free Method for Alleviating Hallucination in LVLMs](https://doi.org/10.1007/978-3-031-73010-8_8)** · ECCV 2024 · VLM · Training-free
- **📋 [HaloQuest: A Visual Hallucination Dataset for Advancing Multimodal Reasoning](https://doi.org/10.1007/978-3-031-72980-5_17)** · ECCV 2024 · VLM · Training-free
- **[Hallu-PI: Evaluating Hallucination in Multi-modal Large Language Models within Perturbed Inputs](https://doi.org/10.1145/3664647.3681251)** · ACM MM 2024 · VLM · Training-free
- **[Hal-Eval: A Universal and Fine-grained Hallucination Evaluation Framework for Large Vision Language Models](https://doi.org/10.1145/3664647.3680576)** · ACM MM 2024 · VLM · Training-free
- **[Exploiting Semantic Reconstruction to Mitigate Hallucinations in Vision-Language Models](https://doi.org/10.1007/978-3-031-73016-0_14)** · ECCV 2024 · VLM · Training-free
- **[Contrastive Region Guidance: Improving Grounding in Vision-Language Models without Training](https://doi.org/10.1007/978-3-031-72986-7_12)** · ECCV 2024 · VLM · Training-free
- **[Combating Visual Question Answering Hallucinations via Robust Multi-Space Co-Debias Learning](https://doi.org/10.1145/3664647.3681663)** · ACM MM 2024 · VLM · Training-free
- **[CLIP-DPO: Vision-Language Models as a Source of Preference for Fixing Hallucinations in LVLMs](https://doi.org/10.1007/978-3-031-73116-7_23)** · ECCV 2024 · VLM · Training-based
- **[BEAF: Observing BEfore-AFter Changes to Evaluate Hallucination in Vision-Language Models](https://doi.org/10.1007/978-3-031-73247-8_14)** · ECCV 2024 · VLM · Training-free
- **[AIGCs Confuse AI Too: Investigating and Explaining Synthetic Image-induced Hallucinations in Large Vision-Language Models](https://doi.org/10.1145/3664647.3681467)** · ACM MM 2024 · VLM · Training-free
- **[Understanding Multimodal Hallucination with Parameter-Free Representation Alignment](https://arxiv.org/abs/2409.01151)** · arXiv · VLM · Training-free
- **[Pre-Training Multimodal Hallucination Detectors with Corrupted Grounding Data](https://arxiv.org/abs/2409.00238)** · arXiv · VLM · Training-free
- **[FIHA: Autonomous Hallucination Evaluation in Vision-Language Models with Davidson Scene Graphs](https://arxiv.org/abs/2409.13612)** · arXiv · VLM · Training-free
- **[EventHallusion: Diagnosing Event Hallucinations in Video LLMs](https://arxiv.org/abs/2409.16597)** · arXiv · VLM · Training-free
- **[VACoDe: Visual Augmented Contrastive Decoding](https://arxiv.org/abs/2408.05337)** · arXiv · VLM · Training-free
- **[Piculet: Specialized Models-Guided Hallucination Decrease for MultiModal Large Language Models](https://arxiv.org/abs/2408.01003)** · arXiv · VLM · Training-free
- **[MedVH: Towards Systematic Evaluation of Hallucination for Large Vision Language Models in the Medical Context](https://arxiv.org/abs/2407.02730)** · arXiv · VLM · Training-free
- **[Interpreting and Mitigating Hallucination in MLLMs through Multi-agent Debate](https://arxiv.org/abs/2407.20505)** · arXiv · VLM · Training-free
- **[Addressing Image Hallucination in Text-to-Image Generation through Factual Image Retrieval](https://arxiv.org/abs/2407.10683)** · arXiv · VLM · Training-free
- **[Visual Hallucinations of Multi-modal Large Language Models](https://doi.org/10.18653/v1/2024.findings-acl.573)** · ACL 2024 · VLM · Training-free
- **[Unified Hallucination Detection for Multimodal Large Language Models](https://doi.org/10.18653/v1/2024.acl-long.178)** · ACL 2024 · VLM · Training-free
- **[Mitigating Hallucinations in Large Vision-Language Models with Instruction Contrastive Decoding](https://doi.org/10.18653/v1/2024.findings-acl.937)** · ACL 2024 · VLM · Training-free
- **[Mitigating Hallucinations in Large Vision-Language Models (LVLMs) via Language-Contrastive Decoding (LCD)](https://doi.org/10.18653/v1/2024.findings-acl.359)** · ACL 2024 · VLM · Training-free
- **[Logical Closed Loop: Uncovering Object Hallucinations in Large Vision-Language Models](https://doi.org/10.18653/v1/2024.findings-acl.414)** · ACL 2024 · VLM · Training-free
- **[Less is More: Mitigating Multimodal Hallucination from an EOS Decision Perspective](https://doi.org/10.18653/v1/2024.acl-long.633)** · ACL 2024 · VLM · Training-free
- **[Investigating and Mitigating the Multimodal Hallucination Snowballing in Large Vision-Language Models](https://doi.org/10.18653/v1/2024.acl-long.648)** · ACL 2024 · VLM · Training-free
- **[VideoHallucer: Evaluating Intrinsic and Extrinsic Hallucinations in Large Video-Language Models](https://arxiv.org/abs/2406.16338)** · arXiv · VLM · Training-free
- **[Measuring the Measurers: Quality Evaluation of Hallucination Benchmarks for Large Vision-Language Models](https://arxiv.org/abs/2406.17115)** · arXiv · VLM · Training-free
- **[Hallucination Mitigation Prompts Long-term Video Understanding](https://arxiv.org/abs/2406.11333)** · arXiv · VLM · Training-free
- **[Do More Details Always Introduce More Hallucinations in LVLM-based Image Captioning?](https://arxiv.org/abs/2406.12663)** · arXiv · VLM · Training-free
- **[Detecting and Evaluating Medical Hallucinations in Large Vision Language Models](https://arxiv.org/abs/2406.10185)** · arXiv · VLM · Training-free
- **[Volcano: Mitigating Multimodal Hallucination through Self-Feedback Guided Revision](https://doi.org/10.18653/v1/2024.naacl-long.23)** · NAACL 2024 · VLM · Training-free
- **[Vista-llama: Reducing Hallucination in Video Language Models via Equal Distance to Visual Tokens](https://doi.org/10.1109/CVPR52733.2024.01249)** · CVPR 2024 · VLM · Training-free
- **📋 [THRONE: An Object-Based Hallucination Benchmark for the Free-Form Generations of Large Vision-Language Models](https://doi.org/10.1109/CVPR52733.2024.02571)** · CVPR 2024 · VLM · Training-free
- **[OPERA: Alleviating Hallucination in Multi-Modal Large Language Models via Over-Trust Penalty and Retrospection-Allocation](https://doi.org/10.1109/CVPR52733.2024.01274)** · CVPR 2024 · VLM · Training-free
- **[Multi-Modal Hallucination Control by Visual Information Grounding](https://doi.org/10.1109/CVPR52733.2024.01356)** · CVPR 2024 · VLM · Training-free
- **[Mitigating Object Hallucinations in Large Vision-Language Models through Visual Contrastive Decoding](https://doi.org/10.1109/CVPR52733.2024.01316)** · CVPR 2024 · VLM · Training-free
- **[Hallucination Augmented Contrastive Learning for Multimodal Large Language Model](https://doi.org/10.1109/CVPR52733.2024.02553)** · CVPR 2024 · VLM · Training-free
- **[Sora Detector: A Unified Hallucination Detection for Large Text-to-Video Models](https://arxiv.org/abs/2405.04180)** · arXiv · VLM · Training-free
- **[RITUAL: Random Image Transformations as a Universal Anti-hallucination Lever in Large Vision Language Models](https://arxiv.org/abs/2405.17821)** · arXiv · VLM · Training-free
- **[NoiseBoost: Alleviating Hallucination with Noise Perturbation for Multimodal Large Language Models](https://arxiv.org/abs/2405.20081)** · arXiv · VLM · Training-free
- **[CrossCheckGPT: Universal Hallucination Ranking for Multimodal Foundation Models](https://arxiv.org/abs/2405.13684)** · arXiv · VLM · Training-free
- **📚 [Hallucination of Multimodal Large Language Models: A Survey](https://arxiv.org/abs/2404.18930)** · arXiv · VLM · Training-free
- **[Visual Hallucination: Definition, Quantification, and Prescriptive Remediations](https://arxiv.org/abs/2403.17306)** · arXiv · VLM · Training-free
- **[Quantity Matters: Towards Assessing and Mitigating Number Hallucination in Large Vision-Language Models](https://arxiv.org/abs/2403.01373)** · arXiv · VLM · Training-free
- **[Pensieve: Retrospect-then-Compare Mitigates Visual Hallucination](https://arxiv.org/abs/2403.14401)** · arXiv · VLM · Training-free
- **[Mitigating Dialogue Hallucination for Large Vision Language Models via Adversarial Instruction Tuning](https://arxiv.org/abs/2403.10492)** · arXiv · VLM · Training-based
- **[ESREAL: Exploiting Semantic Reconstruction to Mitigate Hallucinations in Vision-Language Models](https://arxiv.org/abs/2403.16167)** · arXiv · VLM · Training-free
- **[Towards Alleviating Text-to-Image Retrieval Hallucination for CLIP in Zero-shot Learning](https://arxiv.org/abs/2402.18400)** · arXiv · VLM · Training-free
- **[Skip \n: A Simple Method to Reduce Hallucination in Large Vision-Language Models](https://arxiv.org/abs/2402.01345)** · arXiv · VLM · Training-free
- **[Seeing is Believing: Mitigating Hallucination in Large Vision-Language Models via CLIP-Guided Decoding](https://arxiv.org/abs/2402.15300)** · arXiv · VLM · Training-free
- **📚 [A Survey on Hallucination in Large Vision-Language Models](https://arxiv.org/abs/2402.00253)** · arXiv · VLM · Training-free
- **[Detecting and Preventing Hallucinations in Large Vision Language Models](https://doi.org/10.1609/aaai.v38i16.29771)** · AAAI 2024 · VLM · Training-free
- **[Temporal Insight Enhancement: Mitigating Temporal Hallucination in Multimodal Large Language Models](https://arxiv.org/abs/2401.09861)** · arXiv · VLM · Training-free
- **[Toward a Stable, Fair, and Comprehensive Evaluation of Object Hallucination in Large Vision-Language Models](http://papers.nips.cc/paper_files/paper/2024/hash/c9b551a2e195a209fc0b280de2f7f781-Abstract-Conference.html)** · Unlabeled · VLM · Training-free
- **[RadFlag: A Black-Box Hallucination Detection Method for Medical Vision Language Models](https://proceedings.mlr.press/v259/zhang25c.html)** · Unlabeled · VLM · Training-free
- **[Mitigating Hallucination in Large Multi-Modal Models via Robust Instruction Tuning](https://openreview.net/forum?id=J44HfH4JCg)** · Unlabeled · VLM · Training-based
- **📋 [Hallucination Benchmark in Medical Visual Question Answering](https://openreview.net/forum?id=vxlXqOj4zv)** · Unlabeled · VLM · Training-free
- **[Hallo3D: Multi-Modal Hallucination Detection and Mitigation for Consistent 3D Content Generation](http://papers.nips.cc/paper_files/paper/2024/hash/d75660d6eb0ce31360c768fef85301dd-Abstract-Conference.html)** · Unlabeled · VLM · Training-free
- **[HAIT: Hybrid Adversarial Iterative Training for Mitigating Object Hallucination in Large Vision-Language Models]()** · Unlabeled · VLM · Training-based
- **[Evaluating and Analyzing Relationship Hallucinations in Large Vision-Language Models](https://proceedings.mlr.press/v235/wu24l.html)** · Unlabeled · VLM · Training-free
- **[Analyzing and Mitigating Object Hallucination in Large Vision-Language Models](https://openreview.net/forum?id=oZDJKTlOUe)** · Unlabeled · VLM · Training-free
- **[Temporal Insight Enhancement: Mitigating Temporal Hallucination in Video Understanding by Multimodal Large Language Models](https://doi.org/10.1007/978-3-031-78183-4_29)** · ICPR 2024 · VLM · Training-free
- **[Mitigating Hallucination in Visual-Language Models via Re-Balancing Contrastive Decoding](https://doi.org/10.1007/978-981-97-8620-6_33)** · PRCV 2024 · VLM · Training-free
- **[Mitigating Hallucination in Visual Language Model Segmentation with Negative Sampling](https://doi.org/10.1109/ISCSLP63861.2024.10800691)** · ISCSLP 2024 · VLM · Training-free
- **[Mitigating Fine-Grained Hallucination by Fine-Tuning Large Vision-Language Models with Caption Rewrites](https://doi.org/10.1007/978-3-031-53302-0_3)** · MMM 2024 · VLM · Training-based
- **[Gemini Goes to Med School: Exploring the Capabilities of Multimodal Large Language Models on Medical Challenge Problems &amp; Hallucinations](https://doi.org/10.18653/v1/2024.clinicalnlp-1.3)** · 6th Clinical Natural Language Processing Workshop 2024 · VLM · Training-free
- **[Gemini Goes to Med School: Exploring the Capabilities of Multimodal Large Language Models on Medical Challenge Problems & Hallucinations](https://doi.org/10.18653/v1/2024.clinicalnlp-1.3)** · ClinicalNLP@NAACL 2024 · VLM · Training-free
- **[DENEB: A Hallucination-Robust Automatic Evaluation Metric for Image Captioning](https://doi.org/10.1007/978-981-96-0908-6_10)** · ACCV 2024 · VLM · Training-free
- **[A Unified Hallucination Mitigation Framework for Large Vision-Language Models](https://openreview.net/forum?id=ZVDWzgk6L6)** · TMLR 2024 · VLM · Training-free

</details>

<details>
<summary>📅 2023 · 4 papers</summary>

- **[Evaluating Object Hallucination in Large Vision-Language Models](https://doi.org/10.18653/v1/2023.emnlp-main.20)** · EMNLP 2023 · VLM · Training-free
- **📋 [Negative Object Presence Evaluation (NOPE) to Measure Object Hallucination in Vision-Language Models](https://arxiv.org/abs/2310.05338)** · arXiv · VLM · Training-free
- **[HallE-Control: Controlling Object Hallucination in Large Multimodal Models](https://arxiv.org/abs/2310.01779)** · arXiv · VLM · Training-free
- **[Plausible May Not Be Faithful: Probing Object Hallucination in Vision-Language Pre-training](https://doi.org/10.18653/v1/2023.eacl-main.156)** · EACL 2023 · VLM · Training-free

</details>

<details>
<summary>📅 2022 · 1 papers</summary>

- **[Let there be a clock on the beach: Reducing Object Hallucination in Image Captioning](https://doi.org/10.1109/WACV51458.2022.00253)** · WACV 2022 · VLM · Training-free

</details>

<details>
<summary>📅 2018 · 1 papers</summary>

- **[Object Hallucination in Image Captioning](https://doi.org/10.18653/v1/D18-1437)** · EMNLP 2018 · VLM · Training-free

</details>

</details>

<details>
<summary>🌐 MLLM(Omni) · 28 篇</summary>

<details>
<summary>📅 2026 · 9 papers</summary>

- **📋 [HalluAudio: A Comprehensive Benchmark for Hallucination Detection in Large Audio-Language Models](https://aclanthology.org/2026.acl-long.1797/)** · ACL 2026 · MLLM(Omni) · Training-free
- **[AHA: Aligning Large Audio-Language Models for Reasoning Hallucinations via Counterfactual Hard Negatives](https://aclanthology.org/2026.findings-acl.1464/)** · ACL 2026 · MLLM(Omni) · Training-free
- **[SVHalluc: Benchmarking Speech-Vision Hallucination in Audio-Visual Large Language Models](https://openaccess.thecvf.com/content/CVPR2026/html/Zhang_SVHalluc_Benchmarking_Speech-Vision_Hallucination_in_Audio-Visual_Large_Language_Models_CVPR_2026_paper.html)** · CVPR 2026 · MLLM(Omni) · Training-free
- **[MoD-DPO: Towards Mitigating Cross-modal Hallucinations in Omni LLMs using Modality Decoupled Preference Optimization](https://openaccess.thecvf.com/content/CVPR2026/html/Chaubey_MoD-DPO_Towards_Mitigating_Cross-modal_Hallucinations_in_Omni_LLMs_using_Modality_CVPR_2026_paper.html)** · CVPR 2026 · MLLM(Omni) · Training-based
- **[From Hallucination to Articulation: Language Model-Driven Losses for Ultra Low-Bitrate Neural Speech Coding](https://doi.org/10.1109/icassp55912.2026.11462750)** · ICASSP 2026 · MLLM(Omni) · Training-free
- **[Exploring Audio Hallucination in Egocentric Video Understanding](https://doi.org/10.1109/icassp55912.2026.11460380)** · ICASSP 2026 · MLLM(Omni) · Training-free
- **[On the Nature of Attention Sink that Shapes Decoding Strategy in Omni-LLMs](https://arxiv.org/abs/2603.14337)** · arXiv · MLLM(Omni) · Training-free
- **[PASE: Leveraging the Phonological Prior of WavLM for Low-Hallucination Generative Speech Enhancement](https://doi.org/10.1609/aaai.v40i39.40562)** · AAAI 2026 · MLLM(Omni) · Training-free
- **[OmniDPO: A Preference Optimization Framework to Address Omni-Modal Hallucination](https://doi.org/10.1609/aaai.v40i24.39104)** · AAAI 2026 · MLLM(Omni) · Training-based

</details>

<details>
<summary>📅 2025 · 13 papers</summary>

- **[The Curse of Multi-Modalities: Evaluating Hallucinations of Large Multimodal Models across Language, Visual, and Audio](http://papers.nips.cc/paper_files/paper/2025/hash/9b0b18a77421d45d26c3df5612caefe7-Abstract-Datasets_and_Benchmarks_Track.html)** · NeurIPS 2025 · MLLM(Omni) · Training-free
- **[Mitigating Attention Sinks and Massive Activations in Audio-Visual Speech Recognition with LLMs](https://arxiv.org/abs/2510.22603)** · arXiv · MLLM(Omni) · Training-free
- **📋 [Hallucination Benchmark for Speech Foundation Models](https://arxiv.org/abs/2510.16567)** · arXiv · MLLM(Omni) · Training-free
- **[Evaluating Hallucinations in Audio-Visual Multimodal LLMs with Spoken Queries under Diverse Acoustic Conditions](https://arxiv.org/abs/2510.08581)** · arXiv · MLLM(Omni) · Training-free
- **[VoiceNoNG: Robust High-Quality Speech Editing Model without Hallucinations](https://doi.org/10.21437/Interspeech.2025-431)** · INTERSPEECH 2025 · MLLM(Omni) · Training-free
- **[Teaching Audio-Aware Large Language Models What Does Not Hear: Mitigating Hallucinations through Synthesized Negative Samples](https://doi.org/10.21437/Interspeech.2025-324)** · INTERSPEECH 2025 · MLLM(Omni) · Training-free
- **[Calm-Whisper: Reduce Whisper Hallucination On Non-Speech By Calming Crazy Heads Down](https://doi.org/10.21437/Interspeech.2025-201)** · INTERSPEECH 2025 · MLLM(Omni) · Training-free
- **[Lost in Transcription, Found in Distribution Shift: Demystifying Hallucination in Speech Foundation Models](https://doi.org/10.18653/v1/2025.findings-acl.1190)** · ACL 2025 · MLLM(Omni) · Training-free
- **[AVCD: Mitigating Hallucinations in Audio-Visual Large Language Models through Contrastive Decoding](https://arxiv.org/abs/2505.20862)** · arXiv · MLLM(Omni) · Training-free
- **[Investigation of Whisper ASR Hallucinations Induced by Non-Speech Audio](https://doi.org/10.1109/ICASSP49660.2025.10890105)** · ICASSP 2025 · MLLM(Omni) · Training-free
- **[Can Large Audio-Language Models Truly Hear? Tackling Hallucinations with Multi-Task Assessment and Stepwise Audio Reasoning](https://doi.org/10.1109/ICASSP49660.2025.10888384)** · ICASSP 2025 · MLLM(Omni) · Training-free
- **📋 [AVHBench: A Cross-Modal Hallucination Benchmark for Audio-Visual Large Language Models](https://openreview.net/forum?id=jTEKTdI3K9)** · ICLR 2025 · MLLM(Omni) · Training-free
- **[Reducing Object Hallucination in Large Audio-Language Models via Audio-Aware Decoding](https://doi.org/10.1109/ASRU65441.2025.11434595)** · ASRU 2025 · MLLM(Omni) · Training-free

</details>

<details>
<summary>📅 2024 · 5 papers</summary>

- **📚 [A Comprehensive Survey of Hallucination in Large Language, Image, Video and Audio Foundation Models](https://doi.org/10.18653/v1/2024.findings-emnlp.685)** · EMNLP 2024 · MLLM(Omni) · Training-free
- **[Understanding Sounds, Missing the Questions: The Challenge of Object Hallucination in Large Audio-Language Models](https://doi.org/10.21437/Interspeech.2024-1076)** · INTERSPEECH 2024 · MLLM(Omni) · Training-free
- **[On the Audio Hallucinations in Large Audio-Video Language Models](https://arxiv.org/abs/2401.09774)** · arXiv · MLLM(Omni) · Training-free
- **[Hallucinations in Neural Automatic Speech Recognition: Identifying Errors and Hallucinatory Models](https://arxiv.org/abs/2401.01572)** · arXiv · MLLM(Omni) · Training-free
- **[Careless Whisper: Speech-to-Text Hallucination Harms](https://doi.org/10.1145/3630106.3658996)** · FAccT 2024 · MLLM(Omni) · Training-free

</details>

<details>
<summary>📅 2022 · 1 papers</summary>

- **[Hallucination of Speech Recognition Errors With Sequence to Sequence Learning](https://doi.org/10.1109/TASLP.2022.3145313)** · TASLP 2022 · MLLM(Omni) · Training-free

</details>

</details>

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
