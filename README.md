> 🌐 **English** · [中文](README.zh-CN.md)

# Awesome Hallucination Atlas [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> **Awesome Hallucination Atlas** — A structured, interactive atlas of hallucination research across multimodal LLMs (MLLM / VLM / LLM).
>
> Covers **detection, evaluation, and mitigation** of hallucinations, with multi-dimensional faceted filtering by model type, method type, and year, plus tags for modality and scenario.
>
> Taxonomy is auto-labeled from the **full arXiv abstract text** (1583/2151 papers), not just title keywords.

<p align='center'>
  <img src='https://img.shields.io/badge/Papers-2151-blue' />
  <img src='https://img.shields.io/badge/Abstract--based-1583-9cf' />
  <img src='https://img.shields.io/badge/PRs-Welcome-brightgreen' />
  <img src='https://img.shields.io/static/v1?label=Last%20Update&message=2026-11&color=orange' />
</p>

<p align='center'>
  <a href='https://guangtaolyu.github.io/awesome-hallucination-atlas/'>
    <img alt='Live Website' src='https://img.shields.io/static/v1?label=Live%20Website&message=Visit%20Now&color=8b7cf6&style=for-the-badge' />
  </a>
</p>

> **🌐 Explore the Interactive Website** — [awesome-hallucination-atlas — Live Site](https://guangtaolyu.github.io/awesome-hallucination-atlas/). Faceted filtering, full-text abstract search, and year sorting.
> Prefer offline? Just open [`docs/index.html`](docs/index.html) in any browser — no server needed.

## 📑 Table of Contents

- [Citation](#sec-cite)
- [Data Overview](#sec-overview)
- [Taxonomy](#sec-taxonomy)
- [Trending Directions](#sec-trending)
- [Benchmarks & Evaluation](#sec-benchmark)
- [Surveys](#sec-survey)
- [Paper List](#sec-paperlist)
- [Contributing](#sec-contrib)
- [License](#sec-license)
- [Star History](#sec-stars)

---

<a id="sec-cite"></a>
## 📖 Citation

If you find this repository helpful for your research, we would appreciate citations to our related papers. We also warmly welcome discussions and suggestions: [1004392768@qq.com](mailto:1004392768@qq.com)

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

---

<a id="sec-overview"></a>
## 📊 Data Overview
- **Total papers**：`2151` (deduplicated)
- **With paper link**：`2148` · **With abstract**：`1583` · **With code**：`1177` · **Published at venue**：`1007`
- For papers published at a venue: time and link prioritize the official conference/journal info (DBLP), otherwise arXiv info is used.
- **Year range**：2018 – 2027

### Year Distribution

| Year | Count | Share |
|------|------|------|
| 2027 | 6 | `░░░░░░░░░░░░░░░░░░░░` 0.3%
| 2026 | 952 | `█████████░░░░░░░░░░░` 44.3%
| 2025 | 768 | `███████░░░░░░░░░░░░░` 35.7%
| 2024 | 375 | `███░░░░░░░░░░░░░░░░░` 17.4%
| 2023 | 31 | `░░░░░░░░░░░░░░░░░░░░` 1.4%
| 2022 | 7 | `░░░░░░░░░░░░░░░░░░░░` 0.3%
| 2021 | 5 | `░░░░░░░░░░░░░░░░░░░░` 0.2%
| 2020 | 2 | `░░░░░░░░░░░░░░░░░░░░` 0.1%
| 2019 | 4 | `░░░░░░░░░░░░░░░░░░░░` 0.2%
| 2018 | 1 | `░░░░░░░░░░░░░░░░░░░░` 0.0%


### Model Type

| Model Type | Description | Count |
|----------|------|------|
| **VLM** | Vision-Language Model (LVLM; also covers works that call themselves MLLM but handle only image/video + text) | 815 |
| **MLLM(Omni)** | Omni / full-modal model (audio / speech / any-to-any) | 66 |
| **LLM** | Pure text-based LLM | 1270 |


### Method Type

| Method Type | Description | Count |
|----------|------|------|
| **Training-free** | Training-free (decoding intervention / attention calibration / representation guidance, etc.) | 1873 |
| **Training-based** | Training-based (preference optimization / fine-tuning / RL, etc.) | 278 |


<details>
<summary>📊 Venue Distribution</summary>

### Venue Distribution

> Papers published at a conference / journal are counted by venue (official info prioritized); `arXiv (preprint)` means a preprint not yet officially accepted. Niche journals / small venues, workshops / satellite / co-located events, and venues with only 1 paper are grouped into the “Other” row (details in the collapsible section below). `Unlabeled` marks entries with no resolvable link.

| Venue / Journal | Count | Share |
|-------------|------|------|
| ACL | 153 | `█░░░░░░░░░░░░░░░░░░░` 7.1%
| EMNLP | 112 | `█░░░░░░░░░░░░░░░░░░░` 5.2%
| AAAI | 65 | `█░░░░░░░░░░░░░░░░░░░` 3.0%
| CVPR | 65 | `█░░░░░░░░░░░░░░░░░░░` 3.0%
| NeurIPS | 44 | `░░░░░░░░░░░░░░░░░░░░` 2.0%
| ICLR | 41 | `░░░░░░░░░░░░░░░░░░░░` 1.9%
| NAACL | 38 | `░░░░░░░░░░░░░░░░░░░░` 1.8%
| EACL | 24 | `░░░░░░░░░░░░░░░░░░░░` 1.1%
| ICASSP | 23 | `░░░░░░░░░░░░░░░░░░░░` 1.1%
| ACM MM | 22 | `░░░░░░░░░░░░░░░░░░░░` 1.0%
| ICML | 21 | `░░░░░░░░░░░░░░░░░░░░` 1.0%
| ICCV | 13 | `░░░░░░░░░░░░░░░░░░░░` 0.6%
| TMLR | 12 | `░░░░░░░░░░░░░░░░░░░░` 0.6%
| WACV | 11 | `░░░░░░░░░░░░░░░░░░░░` 0.5%
| COLING | 9 | `░░░░░░░░░░░░░░░░░░░░` 0.4%
| ECCV | 9 | `░░░░░░░░░░░░░░░░░░░░` 0.4%
| Lecture Notes in Networks and Systems | 9 | `░░░░░░░░░░░░░░░░░░░░` 0.4%
| SIGIR | 8 | `░░░░░░░░░░░░░░░░░░░░` 0.4%
| WWW | 8 | `░░░░░░░░░░░░░░░░░░░░` 0.4%
| Comput. Linguistics | 6 | `░░░░░░░░░░░░░░░░░░░░` 0.3%
| IJCAI | 6 | `░░░░░░░░░░░░░░░░░░░░` 0.3%
| IJCNN | 5 | `░░░░░░░░░░░░░░░░░░░░` 0.2%
| INTERSPEECH | 5 | `░░░░░░░░░░░░░░░░░░░░` 0.2%
| KDD | 5 | `░░░░░░░░░░░░░░░░░░░░` 0.2%
| ICME | 4 | `░░░░░░░░░░░░░░░░░░░░` 0.2%
| IJCV | 4 | `░░░░░░░░░░░░░░░░░░░░` 0.2%
| Lecture Notes in Computer Science | 4 | `░░░░░░░░░░░░░░░░░░░░` 0.2%
| TASLP | 4 | `░░░░░░░░░░░░░░░░░░░░` 0.2%
| 18th International Workshop on Semantic Evaluation (SemEval-2024) | 3 | `░░░░░░░░░░░░░░░░░░░░` 0.1%
| CIKM | 3 | `░░░░░░░░░░░░░░░░░░░░` 0.1%
| ECIR | 3 | `░░░░░░░░░░░░░░░░░░░░` 0.1%
| ICPR | 3 | `░░░░░░░░░░░░░░░░░░░░` 0.1%
| IJCNLP-AACL | 3 | `░░░░░░░░░░░░░░░░░░░░` 0.1%
| TAI | 3 | `░░░░░░░░░░░░░░░░░░░░` 0.1%
| TOMM | 3 | `░░░░░░░░░░░░░░░░░░░░` 0.1%
| ASRU | 2 | `░░░░░░░░░░░░░░░░░░░░` 0.1%
| CLEF | 2 | `░░░░░░░░░░░░░░░░░░░░` 0.1%
| Communications in Computer and Information Science | 2 | `░░░░░░░░░░░░░░░░░░░░` 0.1%
| FLLM | 2 | `░░░░░░░░░░░░░░░░░░░░` 0.1%
| ICIC | 2 | `░░░░░░░░░░░░░░░░░░░░` 0.1%
| ICMLA | 2 | `░░░░░░░░░░░░░░░░░░░░` 0.1%
| IEEE Access | 2 | `░░░░░░░░░░░░░░░░░░░░` 0.1%
| IEEE Trans. Software Eng. | 2 | `░░░░░░░░░░░░░░░░░░░░` 0.1%
| IEEE Trans. Vis. Comput. Graph. | 2 | `░░░░░░░░░░░░░░░░░░░░` 0.1%
| IEEE Transactions on Computational Social Systems | 2 | `░░░░░░░░░░░░░░░░░░░░` 0.1%
| Iconic Research and Engineering Journals | 2 | `░░░░░░░░░░░░░░░░░░░░` 0.1%
| International Journal of Computer Applications | 2 | `░░░░░░░░░░░░░░░░░░░░` 0.1%
| MICCAI | 2 | `░░░░░░░░░░░░░░░░░░░░` 0.1%
| ML4H@NeurIPS | 2 | `░░░░░░░░░░░░░░░░░░░░` 0.1%
| NN | 2 | `░░░░░░░░░░░░░░░░░░░░` 0.1%
| Neural Comput. Appl. | 2 | `░░░░░░░░░░░░░░░░░░░░` 0.1%
| PRCV | 2 | `░░░░░░░░░░░░░░░░░░░░` 0.1%
| Proc. ACM Softw. Eng. | 2 | `░░░░░░░░░░░░░░░░░░░░` 0.1%
| Tiny Papers @ ICLR | 2 | `░░░░░░░░░░░░░░░░░░░░` 0.1%
| USENIX Security Symposium | 2 | `░░░░░░░░░░░░░░░░░░░░` 0.1%
| TNNLS | 1 | `░░░░░░░░░░░░░░░░░░░░` 0.0%
| Other | 233 | `██░░░░░░░░░░░░░░░░░░` 10.8%
| arXiv (preprint) | 1114 | `██████████░░░░░░░░░░` 51.8%
| Unlabeled | 12 | `░░░░░░░░░░░░░░░░░░░░` 0.6%

<details>
<summary>“Other” details (159 venues, 233 papers — click to expand)</summary>

| venue | Count |
|-------|------|
| 其他 | 28 |
| SemEval@NAACL | 23 |
| SemEval@ACL | 14 |
| LREC/COLING | 6 |
| SIGIR-AP | 4 |
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
| AAAI Fall Symposia | 1 |
| AAAI Spring Symposia | 1 |
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
| BMVC | 1 |
| BioNLP@ACL | 1 |
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
| Int. J. Data Sci. Anal. | 1 |
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
| SIGGRAPH Posters | 1 |
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
| CCF-A | 462 | `████░░░░░░░░░░░░░░░░` 21.5%
| CCF-B | 240 | `██░░░░░░░░░░░░░░░░░░` 11.2%
| CCF-C | 36 | `░░░░░░░░░░░░░░░░░░░░` 1.7%
| Not in CCF | 1413 | `█████████████░░░░░░░` 65.7%
> 📋 `127` **Benchmark** papers and 📚 `35` **Survey** papers are listed separately (see sections below) and do not affect the method taxonomy.

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

- **Agentic AI / Multi-Agent** — 135 papers tagged `Agent`.
- **RAG / Faithfulness** — 177 papers tagged `RAG`.
- **Reasoning Models** — 410 papers tagged `Reasoning`.
- **Embodied / World Model** — 22 papers tagged `Embodied`.

---

<a id="sec-benchmark"></a>
## 📋 Benchmarks & Evaluation
> 127 evaluation / benchmark / dataset papers are listed separately (also kept in the main list below, marked 📋).

<details open>
<summary>📋 Benchmark List (127 papers — click to collapse / expand)</summary>

- **📋 [They Know Where It Is, But Not What It Says: A Bilingual Hallucination Benchmark of Hadith Recall in Open LLMs](https://arxiv.org/abs/2611.02587)** · arXiv · LLM · Training-free
- **📋 [LexAgentHallu: A Hierarchical Benchmark for Profiling Hallucinations in Legal Agents](https://arxiv.org/abs/2609.09754)** · EMNLP 2026 · LLM · Training-free · 💻[code](https://github.com/TOM-ZHOUch/LexAgentHallu)
- **📋 [SHAM-Bench: A Span-level Hallucination Benchmark Across Multiple Tasks](https://arxiv.org/abs/2610.27370)** · arXiv · LLM · Training-based
- **📋 [ToolHACE: A Dataset for Detecting Hallucinations in Tool-Based LLM Responses](https://arxiv.org/abs/2610.17125)** · arXiv · LLM · Training-free · 💻[code](https://github.com/A1exRey/toolHACE)
- **📋 [PVFH-Bench: Benchmarking Premise-Induced Visual Fixation Hallucinations in Vision-Language Models](https://arxiv.org/abs/2610.14635)** · arXiv · VLM · Training-free · 💻[code](https://github.com/NEUIR/PVFH-Bench)
- **📋 [When Citations Mislead? A Claim-Level Benchmark for Legal Hallucination Detection](https://arxiv.org/abs/2610.10971)** · arXiv · LLM · Training-free
- **📋 [PHRBench: A Behavioral Evaluation of Post-Hallucination Reasoning in LLMs](https://arxiv.org/abs/2610.10455)** · arXiv · LLM · Training-free
- **📋 [DuplexSpeechBench-Document Grounding: Benchmarking Document Grounding and Hallucinations in Voice Agents](https://arxiv.org/abs/2610.00316)** · arXiv · LLM · Training-free
- **📋 [HalluPeer: A Taxonomy-driven Benchmark for Detecting Hallucinations in Scientific Peer Reviews](https://arxiv.org/abs/2609.03580)** · arXiv · LLM · Training-free · 💻[code](https://github.com/Lin-TzuLing/HalluPeer.git)
- **📋 [CHARM: Character Hallucination for Multicultural Role Play Benchmark](https://arxiv.org/abs/2609.01352)** · arXiv · LLM · Training-free · 💻[code](https://github.com/charmbracelet/charm)
- **📋 [KnowHal: A Knowledge-Driven Benchmark for Comprehensive Multimodal Hallucination Evaluation](https://arxiv.org/abs/2608.03782)** · arXiv · VLM · Training-free
- **📋 [HalluTruthQA: A Fine-Grained Benchmark for Hallucination Detection, Localization, and Explanation in Arabic Question Answering](https://arxiv.org/abs/2607.20219)** · arXiv · LLM · Training-free · 💻[code](https://gitlab.com/nlpresearcher/HalluTruthQA)
- **📋 [MissingBench-Verified: Probing Vision-Language Models' Inability to Detect Missing Object Parts](https://arxiv.org/abs/2607.18673)** · arXiv · VLM · Training-free
- **📋 [ArtChart: A Benchmark for Faithful Artistic Chart Generation with Integrated Text Rendering](https://arxiv.org/abs/2607.16060)** · arXiv · VLM · Training-free · 💻[code](https://github.com/Janarthanana/artchart)
- **📋 [HoloCount: A Holistic Visual Counting Benchmark for MLLMs](https://arxiv.org/abs/2607.06420)** · arXiv · VLM · Training-free · 💻[code](https://github.com/MM-MVR/HoloCount)
- **📋 [MoHallBench: A Benchmark for Motion Hallucination in Video Large Language Models](https://arxiv.org/abs/2607.01117)** · arXiv · VLM · Training-free
- **📋 [Rethinking Evaluation for LLM Hallucination Detection: A Desiderata, A New RAG-based Benchmark, New Insights](https://aclanthology.org/2026.acl-long.680/)** · ACL 2026 · LLM · Training-free · 💻[code](https://github.com/Wenbo11/TriviaPlus)
- **📋 [PROBE: PROcess-Based BEnchmark for Hallucination Detection](https://aclanthology.org/2026.findings-acl.2099/)** · ACL 2026 · LLM · Training-free · 💻[code](https://github.com/probe-rs/probe-rs)
- **📋 [INFACT: A Diagnostic Benchmark for Induced Faithfulness and Factuality Hallucinations in Video-LLMs](https://aclanthology.org/2026.acl-long.2062/)** · ACL 2026 · VLM · Training-free · 💻[code](https://github.com/yangjunqi1217/INFACT)
- **📋 [Hallucination Detection in Long-Form Text Generated by LLMs: A Benchmark and a Hyper-Relational Knowledge Graph Approach](https://aclanthology.org/2026.findings-acl.1673/)** · ACL 2026 · LLM · Training-free
- **📋 [HalluAudio: A Comprehensive Benchmark for Hallucination Detection in Large Audio-Language Models](https://aclanthology.org/2026.acl-long.1797/)** · ACL 2026 · MLLM(Omni) · Training-free · 💻[code](https://github.com/Feiyuzhao25/halluaudio)
- **📋 [Born Pragmatic, Trained to Hallucinate? Quantifying the Origins of Contextual Bias in LLMs via the PaCE Benchmark](https://doi.org/10.18653/v1/2026.findings-acl.959)** · ACL 2026 · LLM · Training-based · 💻[code](https://github.com/elpaco-escience/scikit-talk)
- **📋 [How Far Can You Get Without a GPU? A Systematic Benchmark of Lightweight Hallucination Detection Across Question Answering, Dialogue, and Summarisation](https://arxiv.org/abs/2606.29809)** · arXiv · LLM · Training-free · 💻[code](https://github.com/fkriti/hallucination-detection-nli)
- **📋 [MedBench v5: A Dynamic, Process-Oriented, and Hallucination-Aware Benchmark for Clinical Multimodal Models](https://arxiv.org/abs/2606.24155)** · arXiv · VLM · Training-free
- **📋 [A Benchmark for Hallucination Detection in VLMs for Gastrointestinal Endoscopy](https://arxiv.org/abs/2606.24115)** · arXiv · VLM · Training-free
- **📋 [HALAS: A Human-Annotated Dataset of Hallucinations of Modern ASR Systems](https://arxiv.org/abs/2606.23048)** · arXiv · MLLM(Omni) · Training-free · 💻[code](https://github.com/DSP-AGH/HALAS)
- **📋 [SAGE: An Expert-Annotated South Asian GI Endoscopy Dataset for Multimodal Learning and Hallucination Analysis](https://arxiv.org/abs/2606.22144)** · arXiv · VLM · Training-free · 💻[code](https://github.com/roots/sage)
- **📋 [MedHal-Loc: Are "Explainable-by-Architecture" Medical Hallucination Detectors Faithful Localizers? A Localization Benchmark](https://arxiv.org/abs/2606.21517)** · arXiv · LLM · Training-free · 💻[code](https://github.com/green-leo-1/MedHal-Loc)
- **📋 [ClinHallu: A Benchmark for Diagnosing Stage-Wise Hallucinations in Medical MLLM Reasoning](https://arxiv.org/abs/2606.14697)** · arXiv · VLM · Training-free · 💻[code](https://github.com/alibaba-damo-academy/ClinHallu)
- **📋 [OpenHalDet: A Unified Benchmark for Hallucination Detection across Diverse Generation Scenarios](https://arxiv.org/abs/2606.06959)** · arXiv · LLM · Training-free · 💻[code](https://github.com/Nellie179/Hallucination-Detection)
- **📋 [Fine-Grained Multi Image Object Hallucination Benchmark](https://openaccess.thecvf.com/content/CVPR2026/html/Min_Fine-Grained_Multi_Image_Object_Hallucination_Benchmark_CVPR_2026_paper.html)** · CVPR 2026 · VLM · Training-free
- **📋 [ReactBench: A Cause-Driven Benchmark for Multimodal Hallucination via Systematic Evaluation](https://arxiv.org/abs/2605.29579)** · arXiv · VLM · Training-free · 💻[code](https://github.com/millionco/reactbench)
- **📋 [HalluWorld: A Controlled Benchmark for Hallucination via Reference World Models](https://arxiv.org/abs/2605.19341)** · arXiv · LLM · Training-free · 💻[code](https://github.com/DegenAI-Labs/HalluWorld)
- **📋 [PARALLAX: Separating Genuine Hallucination Detection from Benchmark Construction Artifacts](https://arxiv.org/abs/2605.17028)** · arXiv · LLM · Training-free · 💻[code](https://github.com/wagerfield/parallax)
- **📋 [HalluScore: Large Language Model Hallucination Question Answering Benchmark](https://arxiv.org/abs/2605.17007)** · arXiv · LLM · Training-free · 💻[code](https://github.com/aishaalansari57/HalluScore)
- **📋 [Med-StepBench: A Hierarchical Reasoning Framework for Evaluating Hallucinations in Medical Vision-Language Models](https://arxiv.org/abs/2605.10002)** · arXiv · VLM · Training-free
- **📋 [Delulu: A Verified Multi-Lingual Benchmark for Code Hallucination Detection in Fill-in-the-Middle Tasks](https://arxiv.org/abs/2605.07024)** · arXiv · LLM · Training-free · 💻[code](https://github.com/microsoft/delulu)
- **📋 [HalluScan: A Systematic Benchmark for Detecting and Mitigating Hallucinations in Instruction-Following LLMs](https://arxiv.org/abs/2605.02443)** · arXiv · LLM · Training-free · 💻[code](https://github.com/Owen0812/halluscan)
- **📋 [A multilingual hallucination benchmark: MultiWikiQHalluA](https://arxiv.org/abs/2605.02504)** · arXiv · LLM · Training-based
- **📋 [Semantic Layers for Reliable LLM-Powered Data Analytics: A Paired Benchmark of Accuracy and Hallucination Across Three Frontier Models](https://arxiv.org/abs/2604.25149)** · arXiv · LLM · Training-free
- **📋 [DO-Bench: An Attributable Benchmark for Diagnosing Object Hallucination in Vision-Language Models](https://arxiv.org/abs/2604.22822)** · arXiv · VLM · Training-free
- **📋 [DetailVerifyBench: A Benchmark for Dense Hallucination Localization in Long Image Captions](https://arxiv.org/abs/2604.05623)** · arXiv · VLM · Training-free
- **📋 [DHEval: A Dynamic Hallucination Evaluation Protocol Robust to Data Contamination](https://doi.org/10.1109/icassp55912.2026.11462032)** · ICASSP 2026 · LLM · Training-free · 💻[code](https://github.com/spmede/DHEval)
- **📋 [FREAK: A Fine-grained Hallucination Evaluation Benchmark for Advanced MLLMs](https://arxiv.org/abs/2603.19765)** · arXiv · VLM · Training-free · 💻[code](https://github.com/kikohs/freak)
- **📋 [HalDec-Bench: Benchmarking Hallucination Detector in Image Captioning](https://arxiv.org/abs/2603.15253)** · arXiv · VLM · Training-free · 💻[code](https://github.com/dahlian00/HalDec-Bench-Page)
- **📋 [FinReflectKG -- HalluBench: GraphRAG Hallucination Benchmark for Financial Question Answering Systems](https://arxiv.org/abs/2603.20252)** · arXiv · LLM · Training-based
- **📋 [Multi-Hall-SA: A Cross-lingual Benchmark for Multi-Type Hallucination Detection in Low-Resource South African Languages](https://doi.org/10.18653/v1/2026.findings-eacl.330)** · EACL 2026 · LLM · Training-free · 💻[code](https://github.com/elpaco-escience/scikit-talk)
- **📋 [KGHaluBench: A Knowledge Graph-Based Hallucination Benchmark for Evaluating the Breadth and Depth of LLM Knowledge](https://doi.org/10.18653/v1/2026.findings-eacl.206)** · EACL 2026 · LLM · Training-free · 💻[code](https://github.com/elpaco-escience/scikit-talk)
- **📋 [GHOST: Getting to the Bottom of Hallucinations with A Multi-round Consistency Benchmark](https://doi.org/10.1109/WACV61042.2026.00596)** · WACV 2026 · LLM · Training-free · 💻[code](https://github.com/TryGhost/Ghost)
- **📋 [FFE-Hallu: Hallucinations in Fixed Figurative Expressions: A Benchmark of Idioms and Proverbs in the Persian Language](https://doi.org/10.18653/v1/2026.eacl-long.241)** · EACL 2026 · LLM · Training-free · 💻[code](https://github.com/elpaco-escience/scikit-talk)
- **📋 [Constructing a Dataset for Hallucination Detection in Japanese Summarization with Fine-grained Faithfulness Labels](https://doi.org/10.18653/v1/2026.eacl-srw.15)** · EACL 2026 · LLM · Training-free · 💻[code](https://github.com/elpaco-escience/scikit-talk)
- **📋 [ManiBench: A Benchmark for Testing Visual-Logic Drift and Syntactic Hallucinations in Manim Code Generation](https://arxiv.org/abs/2603.13251)** · arXiv · VLM · Training-free · 💻[code](https://github.com/nabin2004/ManiBench)
- **📋 [Halluverse-M^3: A multitask multilingual benchmark for hallucination in LLMs](https://arxiv.org/abs/2602.06920)** · arXiv · LLM · Training-free
- **📋 [HalluHard: A Hard Multi-Turn Hallucination Benchmark](https://arxiv.org/abs/2602.01031)** · arXiv · LLM · Training-free · 💻[code](https://github.com/fan1dy/halluhard)
- **📋 [MHB: Medical Hallucination Benchmark for Large Language Models in Complex Clinical Tasks](https://doi.org/10.1609/aaai.v40i45.41243)** · AAAI 2026 · LLM · Training-free · 💻[code](https://github.com/justiceamoh/mhb)
- **📋 [ESG-Bench: Benchmarking Long-Context ESG Reports for Hallucination Mitigation](https://doi.org/10.1609/aaai.v40i46.41281)** · AAAI 2026 · LLM · Training-based · 💻[code](https://github.com/GateNLP/ESG_Bench)
- **📋 [Causal-HalBench: Uncovering LVLMs Object Hallucinations Through Causal Intervention](https://doi.org/10.1609/aaai.v40i40.40712)** · AAAI 2026 · VLM · Training-free · 💻[code](https://github.com/zhexu-ustc/Causal-HalBench)
- **📋 [TempHalluc-Bench: Evaluating Temporal Hallucination in VideoLLM-Based Video Search and Information Extraction](https://doi.org/10.5120/ijca-1aef39d4b120)** · International Journal of Computer Applications 2026 · VLM · Training-free
- **📋 [EH-Benchmark Ophthalmic Hallucination Benchmark and Agent-Driven Top-Down Traceable Reasoning Workflow](https://doi.org/10.1016/j.inffus.2025.103631)** · INFFUS 2026 · VLM · Training-free · 💻[code](https://github.com/ppxy1/EH-Benchmark)
- **📋 [CDH-Bench: A Commonsense-Driven Hallucination Benchmark for Evaluating Visual Fidelity in Vision-Language Models](https://doi.org/10.1007/978-981-92-3504-9_17)** · ICIC 2026 · VLM · Training-free · 💻[code](https://github.com/hardware-and-co/cdh-linux-bench)
- **📋 [AutoHall: Automated Factuality Hallucination Dataset Generation for Large Language Models](https://doi.org/10.1109/taslpro.2025.3635038)** · TASLP 2026 · LLM · Training-free · 💻[code](https://github.com/zouyingcao/AutoHall)
- **📋 [BHRAM-IL: A Benchmark for Hallucination Recognition and Assessment in Multiple Indian Languages](https://arxiv.org/abs/2512.01852)** · arXiv · LLM · Training-free · 💻[code](https://github.com/sambhashana/BHRAM-IL)
- **📋 [PHANTOM: A Benchmark for Hallucination Detection in Financial Long-Context QA](http://papers.nips.cc/paper_files/paper/2025/hash/b8badadce3f482ba340ff870f4894441-Abstract-Datasets_and_Benchmarks_Track.html)** · NeurIPS 2025 · LLM · Training-free · 💻[code](https://github.com/ramokz/phantom-camera)
- **📋 [AHa-Bench: Benchmarking Audio Hallucinations in Large Audio-Language Models](http://papers.nips.cc/paper_files/paper/2025/hash/1169afa8ad13c98239f0b666b099e159-Abstract-Datasets_and_Benchmarks_Track.html)** · NeurIPS 2025 · MLLM(Omni) · Training-free · 💻[code](https://github.com/AHa-Bench/AHa-Bench)
- **📋 [MUCH: A Multilingual Claim Hallucination Benchmark](https://arxiv.org/abs/2511.17081)** · arXiv · LLM · Training-free · 💻[code](https://github.com/orailix/much)
- **📋 [What Color Is It? A Text-Interference Multimodal Hallucination Benchmark](https://arxiv.org/abs/2511.13400)** · arXiv · VLM · Training-free
- **📋 [MedHallu: A Comprehensive Benchmark for Detecting Medical Hallucinations in Large Language Models](https://doi.org/10.18653/v1/2025.emnlp-main.143)** · EMNLP 2025 · LLM · Training-free · 💻[code](https://github.com/elpaco-escience/scikit-talk)
- **📋 [Challenging Multilingual LLMs: A New Taxonomy and Benchmark for Unraveling Hallucination in Translation](https://arxiv.org/abs/2510.24073)** · arXiv · LLM · Training-free
- **📋 [Confabulations from ACL Publications (CAP): A Dataset for Scientific Hallucination Detection](https://arxiv.org/abs/2510.22395)** · arXiv · LLM · Training-free
- **📋 [Hallucination Benchmark for Speech Foundation Models](https://arxiv.org/abs/2510.16567)** · arXiv · MLLM(Omni) · Training-free · 💻[code](https://github.com/SALT-Research/SHALLOW)
- **📋 [SHALE: A Scalable Benchmark for Fine-grained Hallucination Evaluation in LVLMs](https://doi.org/10.1145/3746027.3758308)** · ACM MM 2025 · VLM · Training-free · 💻[code](https://github.com/kgiszczak/shale)
- **📋 [MIHBench: Benchmarking and Mitigating Multi-Image Hallucinations in Multimodal Large Language Models](https://doi.org/10.1145/3746027.3754993)** · ACM MM 2025 · VLM · Training-free · 💻[code](https://github.com/dhzhang41-tech/MIHBench-DAB-reproduction)
- **📋 [PerHalluEval: Persian Hallucination Evaluation Benchmark for Large Language Models](https://arxiv.org/abs/2509.21104)** · arXiv · LLM · Training-free
- **📋 [MIRAGE-Bench: LLM Agent is Hallucinating and Where to Find Them](https://arxiv.org/abs/2507.21017)** · arXiv · LLM · Training-free · 💻[code](https://github.com/sunblaze-ucb/mirage-bench)
- **📋 [TreeCut: A Synthetic Unanswerable Math Word Problem Dataset for LLM Hallucination Evaluation](https://doi.org/10.18653/v1/2025.acl-short.84)** · ACL 2025 · LLM · Training-free · 💻[code](https://github.com/j-bagel/treecut-math)
- **📋 [Reefknot: A Comprehensive Benchmark for Relation Hallucination Evaluation, Analysis and Mitigation in Multimodal Large Language Models](https://doi.org/10.18653/v1/2025.findings-acl.322)** · ACL 2025 · VLM · Training-free · 💻[code](https://github.com/JackChen-seu/Reefknot)
- **📋 [HalluLens: LLM Hallucination Benchmark](https://doi.org/10.18653/v1/2025.acl-long.1176)** · ACL 2025 · LLM · Training-free · 💻[code](https://github.com/elpaco-escience/scikit-talk)
- **📋 [CCHall: A Novel Benchmark for Joint Cross-Lingual and Cross-Modal Hallucinations Detection in Large Language Models](https://doi.org/10.18653/v1/2025.acl-long.1485)** · ACL 2025 · LLM · Training-free · 💻[code](https://github.com/elpaco-escience/scikit-talk)
- **📋 [PhD: A ChatGPT-Prompted Visual Hallucination Evaluation Dataset](https://openaccess.thecvf.com/content/CVPR2025/html/Liu_PhD_A_ChatGPT-Prompted_Visual_Hallucination_Evaluation_Dataset_CVPR_2025_paper.html)** · CVPR 2025 · VLM · Training-free · 💻[code](https://github.com/GoogleCloudPlatform/tensorflow-without-a-phd)
- **📋 [How LLMs React to Industrial Spatio-Temporal Data? Assessing Hallucination with a Novel Traffic Incident Benchmark Dataset](https://doi.org/10.18653/v1/2025.naacl-industry.4)** · NAACL 2025 · LLM · Training-free · 💻[code](https://github.com/elpaco-escience/scikit-talk)
- **📋 [FaithBench: A Diverse Hallucination Benchmark for Summarization by Modern LLMs](https://doi.org/10.18653/v1/2025.naacl-short.38)** · NAACL 2025 · LLM · Training-free · 💻[code](https://github.com/elpaco-escience/scikit-talk)
- **📋 [3D-GRAND: A Million-Scale Dataset for 3D-LLMs with Better Grounding and Less Hallucination](https://openaccess.thecvf.com/content/CVPR2025/html/Yang_3D-GRAND_A_Million-Scale_Dataset_for_3D-LLMs_with_Better_Grounding_and_CVPR_2025_paper.html)** · CVPR 2025 · VLM · Training-free
- **📋 [MultiHal: Multilingual Dataset for Knowledge-Graph Grounded Evaluation of LLM Hallucinations](https://arxiv.org/abs/2505.14101)** · arXiv · LLM · Training-free · 💻[code](https://github.com/ernlavr/multihal)
- **📋 [HalluMix: A Task-Agnostic, Multi-Domain Benchmark for Real-World Hallucination Detection](https://arxiv.org/abs/2505.00506)** · arXiv · LLM · Training-free · 💻[code](https://github.com/intoexistence/RAG-Hallumix)
- **📋 [Localizing Before Answering: A Hallucination Evaluation Benchmark for Grounded Medical Multimodal LLMs](https://arxiv.org/abs/2505.00744)** · arXiv · VLM · Training-free
- **📋 [MedHal: An Evaluation Dataset for Medical Hallucination Detection](https://arxiv.org/abs/2504.08596)** · arXiv · LLM · Training-free · 💻[code](https://github.com/green-leo-1/MedHal-Loc)
- **📋 [How to Detect and Defeat Molecular Mirage: A Metric-Driven Benchmark for Hallucination in LLM-based Molecular Comprehension](https://arxiv.org/abs/2504.12314)** · arXiv · LLM · Training-free · 💻[code](https://github.com/XuzhaoLi/ro-arxiv-daily)
- **📋 [K-HALU: Multiple Answer Korean Hallucination Benchmark for Large Language Models](https://openreview.net/forum?id=VnLhUogHYE)** · ICLR 2025 · LLM · Training-free · 💻[code](https://github.com/J-Seo/K-HALU)
- **📋 [AVHBench: A Cross-Modal Hallucination Benchmark for Audio-Visual Large Language Models](https://openreview.net/forum?id=jTEKTdI3K9)** · ICLR 2025 · MLLM(Omni) · Training-free · 💻[code](https://github.com/kaist-ami/AVHBench)
- **📋 [OAEI-LLM-T: A TBox Benchmark Dataset for Understanding Large Language Model Hallucinations in Ontology Matching](https://arxiv.org/abs/2503.21813)** · arXiv · LLM · Training-free
- **📋 [Exploring Hallucination of Large Multimodal Models in Video Understanding: Benchmark, Analysis and Mitigation](https://arxiv.org/abs/2503.19622)** · arXiv · VLM · Training-based · 💻[code](https://github.com/Hongcheng-Gao/HAVEN)
- **📋 [Poly-FEVER: A Multilingual Fact Verification Benchmark for Hallucination Detection in Large Language Models](https://arxiv.org/abs/2503.16541)** · arXiv · LLM · Training-free · 💻[code](https://github.com/HanzhiZhang-Ulrica/Poly-Fever_LLaMA3.1)
- **📋 [HalluVerse25: Fine-grained Multilingual Benchmark Dataset for LLM Hallucinations](https://arxiv.org/abs/2503.07833)** · arXiv · LLM · Training-free
- **📋 [Bi'an: A Bilingual Benchmark and Model for Hallucination Detection in Retrieval-Augmented Generation](https://arxiv.org/abs/2502.19209)** · arXiv · LLM · Training-free · 💻[code](https://github.com/OpenSPG/KAG)
- **📋 [MedHallBench: A New Benchmark for Assessing Hallucination in Medical Large Language Models](https://proceedings.mlr.press/v281/zuo25b.html)** · AAAI Bridge Program 2025 · LLM · Training-free
- **📋 [MHBench: Demystifying Motion Hallucination in VideoLLMs](https://doi.org/10.1609/aaai.v39i4.32463)** · AAAI 2025 · VLM · Training-free · 💻[code](https://github.com/xzhouzeng/MHBench)
- **📋 [CodeHalu: Investigating Code Hallucinations in LLMs via Execution-based Verification](https://doi.org/10.1609/aaai.v39i24.34717)** · AAAI 2025 · LLM · Training-free · 💻[code](https://github.com/yuchen814/CodeHalu)
- **📋 [Measuring and Mitigating Hallucinations in Vision-Language Dataset Generation for Remote Sensing](https://arxiv.org/abs/2501.14905)** · arXiv · VLM · Training-free
- **📋 [KG-FPQ: Evaluating Factuality Hallucination in LLMs with Knowledge Graph-based False Premise Questions](https://aclanthology.org/2025.coling-main.698/)** · COLING 2025 · LLM · Training-free · 💻[code](https://github.com/yanxuzhu/KG-FPQ)
- **📋 [MedHallTune: An Instruction-Tuning Benchmark for Mitigating Medical Hallucination in Vision-Language Models](https://doi.org/10.1109/tmi.2026.3719326)** · Other · VLM · Training-free · 💻[code](https://github.com/russellyq/MedHallTune)
- **📋 [ReSelfVerMM: mitigating hallucination in multimodal LLMs through dataset reconstruction and self-verification](https://doi.org/10.1117/12.3072360)** · Second International Conference on Image Processing and Artificial Intelligence (ICIPAI 2025) 2025 · VLM · Training-free
- **📋 [Hallucination-Aware Multimodal Benchmark for Gastrointestinal Image Analysis with Large Vision-Language Models](https://doi.org/10.1007/978-3-032-05127-1_23)** · MICCAI 2025 · VLM · Training-free · 💻[code](https://github.com/bhattarailab/Hallucination-Aware-VLM)
- **📋 [ChartInsighter: An Approach for Mitigating Hallucination in Time-series Chart Summary Generation with A Benchmark Dataset](https://doi.org/10.1109/TVCG.2025.3567122)** · IEEE Trans. Vis. Comput. Graph. 2025 · LLM · Training-free · 💻[code](https://github.com/wangfen01/ChartInsighter)
- **📋 [C-FAITH: A Chinese Fine-Grained Benchmark for Automated Hallucination Evaluation](https://doi.org/10.1145/3746252.3761604)** · CIKM 2025 · LLM · Training-free · 💻[code](https://github.com/liuliu115621/Test-for-data-loss)
- **📋 [The HalluRAG Dataset: Detecting Closed-Domain Hallucinations in RAG Applications Using an LLM's Internal States](https://arxiv.org/abs/2412.17056)** · arXiv · LLM · Training-based · 💻[code](https://github.com/F4biian/HalluRAG)
- **📋 [ERBench: An Entity-Relationship based Automatically Verifiable Hallucination Benchmark for Large Language Models](http://papers.nips.cc/paper_files/paper/2024/hash/5ef9853a6cdea40ae3e301a6d8dc32b5-Abstract-Datasets_and_Benchmarks_Track.html)** · NeurIPS 2024 · LLM · Training-free · 💻[code](https://github.com/erbench/erbench)
- **📋 [ViBe: A Text-to-Video Benchmark for Evaluating Hallucination in Large Multimodal Models](https://arxiv.org/abs/2411.10867)** · arXiv · VLM · Training-free · 💻[code](https://github.com/mkocabas/VIBE)
- **📋 [DAHL: Domain-specific Automated Hallucination Evaluation of Long-Form Text through a Benchmark Dataset in Biomedicine](https://arxiv.org/abs/2411.09255)** · arXiv · LLM · Training-free · 💻[code](https://github.com/rldv1/dahl)
- **📋 [ToolBeHonest: A Multi-level Hallucination Diagnostic Benchmark for Tool-Augmented Large Language Models](https://doi.org/10.18653/v1/2024.emnlp-main.637)** · EMNLP 2024 · LLM · Training-free · 💻[code](https://github.com/elpaco-escience/scikit-talk)
- **📋 [DiaHalu: A Dialogue-level Hallucination Evaluation Benchmark for Large Language Models](https://doi.org/10.18653/v1/2024.findings-emnlp.529)** · EMNLP 2024 · LLM · Training-free · 💻[code](https://github.com/elpaco-escience/scikit-talk)
- **📋 [Collu-Bench: A Benchmark for Predicting Language Model Hallucinations in Code](https://arxiv.org/abs/2410.09997)** · arXiv · VLM · Training-free · 💻[code](https://github.com/PavlovaElina/collu-bench_pipeline)
- **📋 [HaloQuest: A Visual Hallucination Dataset for Advancing Multimodal Reasoning](https://doi.org/10.1007/978-3-031-72980-5_17)** · ECCV 2024 · VLM · Training-free · 💻[code](https://github.com/ZhecanJamesWang/HaloQuest)
- **📋 [Order Matters in Hallucination: Reasoning Order as Benchmark and Reflexive Prompting for Large-Language-Models](https://arxiv.org/abs/2408.05093)** · arXiv · LLM · Training-free · 💻[code](https://github.com/XieZikai/ReflexivePrompting)
- **📋 [DefAn: Definitive Answer Dataset for LLMs Hallucination Evaluation](https://arxiv.org/abs/2406.09155)** · arXiv · LLM · Training-free · 💻[code](https://github.com/ashikiut/DefAn)
- **📋 [HalluDial: A Large-Scale Benchmark for Automatic Dialogue-Level Hallucination Evaluation](https://arxiv.org/abs/2406.07070)** · arXiv · LLM · Training-free · 💻[code](https://github.com/FlagOpen/HalluDial)
- **📋 [THRONE: An Object-Based Hallucination Benchmark for the Free-Form Generations of Large Vision-Language Models](https://doi.org/10.1109/CVPR52733.2024.02571)** · CVPR 2024 · VLM · Training-free · 💻[code](https://github.com/throneproj/Throne)
- **📋 [RefChecker: Reference-based Fine-grained Hallucination Checker and Benchmark for Large Language Models](https://arxiv.org/abs/2405.14486)** · arXiv · LLM · Training-free · 💻[code](https://github.com/amazon-science/RefChecker)
- **📋 [The Hallucinations Leaderboard -- An Open Effort to Measure Hallucinations in Large Language Models](https://arxiv.org/abs/2404.05904)** · arXiv · LLM · Training-free
- **📋 [HypoTermQA: Hypothetical Terms Dataset for Benchmarking Hallucination Tendency of LLMs](https://doi.org/10.18653/v1/2024.eacl-srw.9)** · EACL 2024 · LLM · Training-free · 💻[code](https://github.com/elpaco-escience/scikit-talk)
- **📋 [OAEI-LLM: A Benchmark Dataset for Understanding Large Language Model Hallucinations in Ontology Matching](https://ceur-ws.org/Vol-3953/361.pdf)** · HGAIS@ISWC 2024 · LLM · Training-free · 💻[code](https://github.com/ellenzhuwang/AMD-v2)
- **📋 [MASSIVE Multilingual Abstract Meaning Representation: A Dataset and Baselines for Hallucination Detection](https://doi.org/10.18653/v1/2024.starsem-1.1)** · 13th Joint Conference on Lexical and Computational Semantics (*SEM 2024) 2024 · LLM · Training-free · 💻[code](https://github.com/elpaco-escience/scikit-talk)
- **📋 [Hallucination Benchmark in Medical Visual Question Answering](https://openreview.net/forum?id=vxlXqOj4zv)** · Tiny Papers @ ICLR 2024 · VLM · Training-free
- **📋 [German Also Hallucinates! Inconsistency Detection in News Summaries with the Absinth Dataset](https://aclanthology.org/2024.lrec-main.680)** · LREC/COLING 2024 · LLM · Training-free
- **📋 [Detection, Diagnosis, and Explanation: A Benchmark for Chinese Medial Hallucination Evaluation](https://aclanthology.org/2024.lrec-main.428)** · LREC/COLING 2024 · LLM · Training-free
- **📋 [HalOmi: A Manually Annotated Benchmark for Multilingual Hallucination and Omission Detection in Machine Translation](https://doi.org/10.18653/v1/2023.emnlp-main.42)** · EMNLP 2023 · LLM · Training-free · 💻[code](https://github.com/elpaco-escience/scikit-talk)
- **📋 [A New Benchmark and Reverse Validation Method for Passage-level Hallucination Detection](https://doi.org/10.18653/v1/2023.findings-emnlp.256)** · EMNLP 2023 · LLM · Training-free · 💻[code](https://github.com/elpaco-escience/scikit-talk)
- **📋 [Negative Object Presence Evaluation (NOPE) to Measure Object Hallucination in Vision-Language Models](https://arxiv.org/abs/2310.05338)** · arXiv · VLM · Training-free

</details>

<a id="sec-survey"></a>
## 📚 Surveys
> 35 survey / review / taxonomy papers are listed separately (also kept in the main list below, marked 📚).

<details open>
<summary>📚 Survey List (35 papers — click to collapse / expand)</summary>

- **📚 [AI Slop and Hallucinations in Vulnerability Assessment: A Survey on Reasoning Failures and Trustworthy Mitigation](https://arxiv.org/abs/2608.25667)** · arXiv · LLM · Training-free
- **📚 [Model stability and hallucination under the data-knowledge dual-drive paradigm: a survey](https://doi.org/10.1117/12.3110427)** · ICML 2026 · LLM · Training-free
- **📚 [Distorted or Fabricated? A Survey on Hallucination in Video LLMs](https://aclanthology.org/2026.findings-acl.1325/)** · ACL 2026 · VLM · Training-free · 💻[code](https://github.com/hukcc/Awesome-Video-Hallucination)
- **📚 [DECK: A Consistency x Confidence Taxonomy of LLM Hallucinations](https://arxiv.org/abs/2606.02289)** · arXiv · LLM · Training-free · 💻[code](https://github.com/visgl/deck.gl)
- **📚 [A Geometric Taxonomy of Hallucinations in LLMs](https://arxiv.org/abs/2602.13224)** · arXiv · LLM · Training-free · 💻[code](https://github.com/Borealiscodes/Geometric-Hallucination-Taxonomy)
- **📚 [Hallucination Detection, Verification, and Correction in Generative AI: A Comprehensive Survey](https://doi.org/10.1016/j.nlp.2026.100231)** · Other · LLM · Training-free
- **📚 [Survey on Hallucination in Reasoning Large Language Model: Evaluation, Taxonomy, Intervention, and Open Issues](https://doi.org/10.3724/2096-7004.di.2025.0131)** · Data Intell. 2026 · LLM · Training-free
- **📚 [Loki’s Dance of Illusions: A Comprehensive Survey of Hallucination in Large Language Models](https://doi.org/10.1109/tcss.2026.3661295)** · IEEE Transactions on Computational Social Systems 2026 · LLM · Training-free
- **📚 [Large language models hallucination: A comprehensive survey](https://doi.org/10.1016/j.cosrev.2026.100970)** · Comput. Sci. Rev. 2026 · LLM · Training-free
- **📚 [House of Mirrors: A Survey on Hallucination Detection and Mitigation via Decoding Techniques in Language Models](https://doi.org/10.1007/978-3-032-03072-6_9)** · Lecture Notes in Networks and Systems 2026 · LLM · Training-free
- **📚 [Hallucinations in LLMs: A Lifecycle-Based Survey of Causes, Detection, Mitigation, and Prevention](https://doi.org/10.1007/s41060-026-01214-6)** · Int. J. Data Sci. Anal. 2026 · LLM · Training-free
- **📚 [Hallucination to truth: a review of fact-checking and factuality evaluation in large language models](https://doi.org/10.1007/s10462-025-11454-w)** · Artif. Intell. Rev. 2026 · LLM · Training-based
- **📚 [Attribution Techniques for Mitigating Hallucinated Information in RAG Systems: A Survey](https://doi.org/10.1109/ICAIIC68212.2026.11454197)** · ICAIIC 2026 · LLM · Training-free · 💻[code](https://github.com/IgnacioValenzuelaM/Smina_Redocking)
- **📚 [A Taxonomy of Machine Hallucination in Radiology](https://doi.org/10.1148/ryai.250203)** · Radiology: Artificial Intelligence 2026 · LLM · Training-free
- **📚 [A Survey of Multimodal Hallucination Evaluation and Detection](https://doi.org/10.1007/s11263-026-02756-9)** · IJCV 2026 · VLM · Training-free
- **📚 [A Survey of Hallucination in Large Language Models](https://doi.org/10.12677/airr.2026.151016)** · Artificial Intelligence and Robotics Research 2026 · LLM · Training-free
- **📚 [A Concise Review of Hallucinations in LLMs and their Mitigation](https://arxiv.org/abs/2512.02527)** · arXiv · LLM · Training-free
- **📚 [Mitigating Hallucination in Large Language Models (LLMs): An Application-Oriented Survey on RAG, Reasoning, and Agentic Systems](https://arxiv.org/abs/2510.24476)** · arXiv · LLM · Training-free · 💻[code](https://github.com/ovxncdev/llm-hallucination-normalization)
- **📚 [Review of Hallucination Understanding in Large Language and Vision Models](https://arxiv.org/abs/2510.00034)** · arXiv · VLM · Training-free
- **📚 [LLM-based Agents Suffer from Hallucinations: A Survey of Taxonomy, Methods, and Directions](https://arxiv.org/abs/2509.18970)** · arXiv · LLM · Training-free · 💻[code](https://github.com/nans6/agent-evals)
- **📚 [A comprehensive taxonomy of hallucinations in Large Language Models](https://arxiv.org/abs/2508.01781)** · arXiv · VLM · Training-free
- **📚 [🧜Siren’s Song in the AI Ocean: A Survey on Hallucination in Large Language Models](https://doi.org/10.1162/coli.a.16)** · Comput. Linguistics 2025 · LLM · Training-free
- **📚 [Hallucination Detection in Foundation Models for Decision-Making: A Flexible Definition and Review of the State of the Art](https://doi.org/10.1145/3716846)** · ACM Comput. Surv. 2025 · LLM · Training-based
- **📚 [A Scoping Review of Natural Language Processing in Addressing Medically Inaccurate Information: Errors, Misinformation, and Hallucination](https://doi.org/10.1016/j.jbi.2025.104866)** · J. Biomed. Informatics 2025 · LLM · Training-free
- **📚 [A Review of Faithfulness Metrics for Hallucination Assessment in Large Language Models](https://doi.org/10.1109/JSTSP.2025.3579203)** · IEEE J. Sel. Top. Signal Process. 2025 · LLM · Training-free
- **📚 [A Comprehensive Survey of Hallucination in Large Language, Image, Video and Audio Foundation Models](https://doi.org/10.18653/v1/2024.findings-emnlp.685)** · EMNLP 2024 · MLLM(Omni) · Training-free · 💻[code](https://github.com/elpaco-escience/scikit-talk)
- **📚 [A Survey of Hallucination in Large Visual Language Models](https://arxiv.org/abs/2410.15359)** · arXiv · VLM · Training-free · 💻[code](https://github.com/rolandosegundo/tv2)
- **📚 [Can Knowledge Graphs Reduce Hallucinations in LLMs? : A Survey](https://doi.org/10.18653/v1/2024.naacl-long.219)** · NAACL 2024 · LLM · Training-free · 💻[code](https://github.com/elpaco-escience/scikit-talk)
- **📚 [Hallucination of Multimodal Large Language Models: A Survey](https://arxiv.org/abs/2404.18930)** · arXiv · VLM · Training-free · 💻[code](https://github.com/showlab/Awesome-MLLM-Hallucination)
- **📚 [A Survey of Automatic Hallucination Evaluation on Natural Language Generation](https://arxiv.org/abs/2404.12041)** · arXiv · LLM · Training-free · 💻[code](https://github.com/KNZLink/KNZLink)
- **📚 [A Survey on Large Language Model Hallucination via a Creativity Perspective](https://arxiv.org/abs/2402.06647)** · arXiv · LLM · Training-free
- **📚 [A Survey on Hallucination in Large Vision-Language Models](https://arxiv.org/abs/2402.00253)** · arXiv · VLM · Training-free
- **📚 [LightHouse: A Survey of AGI Hallucination](https://arxiv.org/abs/2401.06792)** · arXiv · VLM · Training-free · 💻[code](https://github.com/GoogleChrome/lighthouse)
- **📚 [A Comprehensive Survey of Hallucination Mitigation Techniques in Large Language Models](https://arxiv.org/abs/2401.01313)** · arXiv · LLM · Training-free
- **📚 [Cognitive Mirage: A Review of Hallucinations in Large Language Models](https://ceur-ws.org/Vol-3818/paper2.pdf)** · LKM@IJCAI 2024 · LLM · Training-free

</details>

<a id="sec-paperlist"></a>
## 📚 Paper List
> The complete list is split into **per-year files** so GitHub renders all of it (READMEs are silently truncated past 500 KiB). Browse by year below, or use the interactive site for full abstracts and faceted search.

| Year | Papers | File |
|---|---|---|
| 2027 | 6 | [2027.md](papers/2027.md) |
| 2026 | 952 | [2026.md](papers/2026.md) |
| 2025 | 768 | [2025.md](papers/2025.md) |
| 2024 | 375 | [2024.md](papers/2024.md) |
| 2023 | 31 | [2023.md](papers/2023.md) |
| 2022 | 7 | [2022.md](papers/2022.md) |
| 2021 | 5 | [2021.md](papers/2021.md) |
| 2020 | 2 | [2020.md](papers/2020.md) |
| 2019 | 4 | [2019.md](papers/2019.md) |
| 2018 | 1 | [2018.md](papers/2018.md) |

- [Full index by year](PAPERS.md)
- [Live Site · abstract search & filters](https://guangtaolyu.github.io/awesome-hallucination-atlas/)

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
