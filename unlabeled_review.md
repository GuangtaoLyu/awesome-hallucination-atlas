# 未标注（venue 为空）论文反向核查报告

> 数据快照：当前 `docs/papers.json` 共 1055 篇，其中 **venue 为空 178 篇**。

> 方法：对 151 个带 DOI 的链接用 **Crossref API** 反查 `container-title`；arXiv/其它链接/无链接单独归类。

## 一、总览

- **A. 可解析到正规 venue（建议回填）**：64 篇
  - 其中能定 CCF 级：**A 12 / B 44 / C 3**（其余 0 篇为 NeurIPS/ICLR 等 CCF-A 或 CL 期刊，详见下方）
- **B. DOI 但 venue 未解析 / 非 CCF 目录（真·未收录或需人工）**：87 篇
- **C. 其它链接（OpenReview / papers.nips.cc 等在投或 workshop）**：19 篇
- **D. 无链接（无从解析）**：8 篇

> 若把 A 组 64 篇回填 venue，「未标注」将从 178 降到约 114，且 EMNLP/AAAI/ICASSP 等被低估的顶会数量会回升、CCF 分布更准。


## A. 可解析到正规 venue（建议回填）（64）

- [2026] **CCF-A** · Global-Local Confidence Fusion for Hallucination Detection in Mathematical Reasoning Task
- [2026] **CCF-A** · LLM-CAS: Dynamic Neuron Perturbation for Real-Time Hallucination Correction
- [2026] **CL** · RusHallu-RAG: benchmarking hallucination detection for Russian RAG
- [2026] **CL** · The Double-Lock Framework: A Multi-Layered System for Grounded Retrieval-Augmented Generation and Hallucination Mitigation
- [2026] **CCF-C** · Being Kind Isn&apos;t Always Being Safe: Diagnosing Affective Hallucination in LLMs
- [2026] **CCF-C** · Reasoning&apos;s Razor: Reasoning Improves Accuracy but Hurts Recall at Critical Operating Points in Safety and Hallucination Detection
- [2026] **CCF-B** · Constrained Paraphrase Consistency for LLM Hallucination Detection
- [2026] **CCF-B** · Cross Paraphrastic Invariance Learning for Hallucination Detection
- [2026] **CCF-B** · CVSTIM: Mitigating Object Hallucination in Mllms Via Co-Occurrence Guided Visual Stimulation
- [2026] **CCF-B** · DHEval: A Dynamic Hallucination Evaluation Protocol Robust to Data Contamination
- [2026] **CCF-B** · Exploring Audio Hallucination in Egocentric Video Understanding
- [2026] **CCF-B** · From Hallucination to Articulation: Language Model-Driven Losses for Ultra Low-Bitrate Neural Speech Coding
- [2026] **CCF-B** · Hallucination Detection Via Internal States and Structured Reasoning Consistency in Large Language Models
- [2026] **CCF-B** · Mitigating Hallucination in Financial Retrieval-Augmented Generation Via Fine-Grained Knowledge Verification
- [2026] **CCF-B** · Multi-Agent Brainstorming for Interpreting and Mitigating Hallucination in Multimodal-LLM
- [2026] **CCF-B** · Semantic Reformulation Entropy for Robust Hallucination Detection in QA Tasks
- [2026] **CCF-A** · Model stability and hallucination under the data-knowledge dual-drive paradigm: a survey
- [2025] **CCF-A** · Is LLMs Hallucination Usable? LLM-based Negative Reasoning for Fake News Detection
- [2025] **CCF-A** · RaDIO: Real-Time Hallucination Detection with Contextual Index Optimized Query Formulation for Dynamic Retrieval Augmented Generation
- [2025] **CL** · Beyond Logit Lens: Contextual Embeddings for Robust Hallucination Detection &amp; Grounding in VLMs
- [2025] **CL** · GOLFer: Smaller LMs-Generated Documents Hallucination Filter &amp; Combiner for Query Expansion in Information Retrieval
- [2025] **CL** · 🧜Siren’s Song in the AI Ocean: A Survey on Hallucination in Large Language Models
- [2025] **CCF-B** · Chain-of-Thought Prompting Obscures Hallucination Cues in Large Language Models: An Empirical Evaluation
- [2025] **CCF-B** · HalluDetect: Detecting, Mitigating, and Benchmarking Hallucinations in Conversational Systems in the Legal Domain
- [2025] **CCF-B** · Logit Space Constrained Fine-Tuning for Mitigating Hallucinations in LLM-Based Recommender Systems
- [2025] **CCF-B** · MRFD: Multi-Region Fusion Decoding with Self-Consistency for Mitigating Hallucinations in LVLMs
- [2025] **CCF-B** · ReLoop: &quot;Seeing Twice and Thinking Backwards&quot; via Closed-loop Training to Mitigate Hallucinations in Multimodal understanding
- [2025] **CCF-B** · Explore the Hallucination on Low-level Perception for MLLMs
- [2025] **CCF-B** · Mitigating Hallucinations on Object Attributes using Multiview Images and Negative Instructions
- [2025] **CCF-A** · VLM3KG:A Hallucination Mitigation Method for Vision-Language Models based on Multimodal Knowledge Graph
- [2024] **CCF-A** · Detecting and Preventing Hallucinations in Large Vision Language Models
- [2024] **CCF-A** · Mitigating Large Language Model Hallucinations via Autonomous Knowledge Graph-Based Retrofitting
- [2024] **CCF-A** · Visual Hallucination Elevates Speech Recognition
- [2024] **CCF-B** · A Comprehensive Survey of Hallucination in Large Language, Image, Video and Audio Foundation Models
- [2024] **CCF-B** · DiaHalu: A Dialogue-level Hallucination Evaluation Benchmark for Large Language Models
- [2024] **CCF-B** · Does Fine-Tuning LLMs on New Knowledge Encourage Hallucinations?
- [2024] **CCF-B** · Does Object Grounding Really Reduce Hallucination of Large Vision-Language Models?
- [2024] **CCF-B** · Embedding and Gradient Say Wrong: A White-Box Method for Hallucination Detection
- [2024] **CCF-B** · Enhanced Hallucination Detection in Neural Machine Translation through Simple Detector Aggregation
- [2024] **CCF-B** · FaithScore: Fine-grained Evaluations of Hallucinations in Large Vision-Language Models
- [2024] **CCF-B** · Game on Tree: Visual Hallucination Mitigation via Coarse-to-Fine View Tree and Game Theory
- [2024] **CCF-B** · HalluMeasure: Fine-grained Hallucination Measurement Using Chain-of-Thought Reasoning
- [2024] **CCF-B** · Investigating and Mitigating Object Hallucinations in Pretrained Vision-Language (CLIP) Models
- [2024] **CCF-B** · Knowledge-Centric Hallucination Detection
- [2024] **CCF-B** · Lookback Lens: Detecting and Mitigating Contextual Hallucinations in Large Language Models Using Only Attention Maps
- [2024] **CCF-B** · Machine Translation Hallucination Detection for Low and High Resource Languages using Large Language Models
- [2024] **CCF-B** · Medico: Towards Hallucination Detection and Correction with Multi-source Evidence Fusion
- [2024] **CCF-B** · Mitigating Hallucination in Fictional Character Role-Play
- [2024] **CCF-B** · Mitigating Open-Vocabulary Caption Hallucinations
- [2024] **CCF-B** · Navigating Hallucinations for Reasoning of Unintentional Activities
- [2024] **CCF-B** · Reference-free Hallucination Detection for Large Vision-Language Models
- [2024] **CCF-B** · Small Agent Can Also Rock! Empowering Small Language Models as Hallucination Detector
- [2024] **CCF-B** · ToolBeHonest: A Multi-level Hallucination Diagnostic Benchmark for Tool-Augmented Large Language Models
- [2024] **CCF-B** · VGA: Vision GUI Assistant - Minimizing Hallucinations through Image-Centric Fine-Tuning
- [2024] **CCF-B** · What if...?: Thinking Counterfactual Keywords Helps to Mitigate Hallucination in Large Multi-modal Models
- [2024] **CCF-B** · Zero-Resource Hallucination Prevention for Large Language Models
- [2024] **CCF-B** · Alleviating Hallucinations Via Supportive Window Indexing in Abstractive Summarization
- [2024] **CCF-A** · Roberta with Low-Rank Adaptation and Hierarchical Attention for Hallucination Detection in LLMs
- [2024] **CCF-A** · On Early Detection of Hallucinations in Factual Question Answering
- [2024] **CCF-B** · On Large Language Models&apos; Hallucination with Regard to Known Facts
- [2023] **CCF-C** · Looking for a Needle in a Haystack: A Comprehensive Study of Hallucinations in Neural Machine Translation
- [2023] **CCF-B** · SAC3: Reliable Hallucination Detection in Black-Box Language Models via Semantic-aware Cross-check Consistency: Reliable Hallucination Detection in Black-Box Language Models via Semantic-aware Cross-check Consistency
- [2023] **CCF-A** · &quot;Why is this misleading?&quot;: Detecting News Headline Hallucinations with Explanations
- [2021] **CCF-B** · The Curious Case of Hallucinations in Neural Machine Translation

## B. DOI 但 venue 未解析 / 非 CCF（真·未收录或需人工）（87）

- [2027] **Springer(未解析)** · A Multi-agent Framework for Factuality Hallucination Detection Using Complex Knowledge Graph  _(Lecture Notes in Computer Science)_
- [2027] **Springer(未解析)** · Beyond Statistical Divergence: A Hybrid Calibration Framework for Decoupling Hallucination in Large Language Models  _(Lecture Notes in Computer Science)_
- [2027] **Springer(未解析)** · Combining NotebookLM and Gemini Gems to Reduce Hallucination and Curriculum Misalignment in Programming Education: System Design and Early Evidence  _(Lecture Notes in Computer Science)_
- [2027] **Springer(未解析)** · Quantum Entropy–Driven Temperature Scaling for Hallucination Mitigation in Generative Models  _(Lecture Notes in Networks and Systems)_
- [2027] **Springer(未解析)** · Uncovering Reasoning Failures: Hallucination Detection via Semantic Probing and Attention Tracking  _(Lecture Notes in Computer Science)_
- [2026] **IEEE(未解析)** · A Hybrid Framework for Hallucination Detection in Large Language Models  _(IEEE Transactions on Artificial Intelligence)_
- [2026] **IEEE(未解析)** · AutoHall: Automated Factuality Hallucination Dataset Generation for Large Language Models  _(IEEE Transactions on Audio, Speech and Language Pr)_
- [2026] **IEEE(未解析)** · Beware of the Woozle Effect: Exploring and Mitigating Hallucination Propagation in Multi-Agent Debate  _(IEEE Transactions on Audio, Speech and Language Pr)_
- [2026] **IEEE(未解析)** · GraphHall: A Graph-Based Framework for Hallucination Detection in Large Language Models  _(IEEE Transactions on Artificial Intelligence)_
- [2026] **IEEE(未解析)** · Loki’s Dance of Illusions: A Comprehensive Survey of Hallucination in Large Language Models  _(IEEE Transactions on Computational Social Systems)_
- [2026] **IEEE(未解析)** · Mitigating Hallucination in Multimodal Information Systems: A Comparative Analysis of Modular LLM Architectures  _(IEEE Transactions on Computational Social Systems)_
- [2026] **IEEE(未解析)** · Mitigating LLM Hallucination Snowballing in Multiagent Systems via Context-Aware Semantic Consistency Reasoning  _(IEEE Transactions on Neural Networks and Learning )_
- [2026] **IEEE(未解析)** · Mitigating Multimodal Hallucination Through Effective and Perception-Aware Granularity Alignment  _(IEEE Transactions on Audio, Speech and Language Pr)_
- [2026] **IEEE(未解析)** · MVRL: A Multi-stage Training Framework for Value Alignment and Hallucination Suppression in Large Language Models  _(2026 IEEE International Conference on Pattern Reco)_
- [2026] **IEEE(未解析)** · PromptFishing: Active Hallucination Inducement to Distinguish LLMs From Humans  _(IEEE Transactions on Information Forensics and Sec)_
- [2026] **Springer(未解析)** · A CNN-Based Framework for Addressing Hallucination Phenomena: Mitigating Limitations Across Multimodal and Clinical Contexts  _(Lecture Notes in Networks and Systems)_
- [2026] **Springer(未解析)** · A Knowledge Graph Approach Towards Detecting Large Language Model Hallucination  _(Lecture Notes in Networks and Systems)_
- [2026] **Springer(未解析)** · AI Hallucination Prediction: A Novel Approach for Preventing False AI Outputs  _(Lecture Notes in Networks and Systems)_
- [2026] **Springer(未解析)** · Enhancing Factual Consistency in Large Language Models: An Integrative Paradigm of Grounding and Self-Prompting Methods for Hallucination Minimization  _(Lecture Notes in Networks and Systems)_
- [2026] **Springer(未解析)** · House of Mirrors: A Survey on Hallucination Detection and Mitigation via Decoding Techniques in Language Models  _(Lecture Notes in Networks and Systems)_
- [2026] **Springer(未解析)** · HyGen—A Hybrid Automation Testing Approach for Reducing Hallucination in LLM-Based Applications  _(Lecture Notes in Networks and Systems)_
- [2026] **其它:2026 23rd International Learning and Tec** · Lawsuit AraRAG: A Retrieval-Augmented Generation Framework for Arabic Legal Document Understanding and Hallucination Reduction  _(2026 23rd International Learning and Technology Co)_
- [2026] **其它:2026 29th International Conference on Co** · Mitigating Hallucination on Hallucination in RAG via Ensemble Voting  _(2026 29th International Conference on Computer Sup)_
- [2026] **其它:2026 7th International Conference on Int** · A Real-Time Verification Framework for Hallucination and Bias Detection in AI Generated Text  _(2026 7th International Conference on Intelligent C)_
- [2026] **其它:2026 International Conference on Compute** · Hallucination Detection in Large Language Models using Self Consistency Signals  _(2026 International Conference on Computer Networks)_
- [2026] **其它:2026 International Conference on Signal ** · Hallucination Mitigation for EEG-to-Text Generation via Multi-Source Semantic Augmentation and Latent Space Regularization  _(2026 International Conference on Signal Image Proc)_
- [2026] **其它:ACM Transactions on Asian and Low-Resour** · Synonym Knowledge Graph Enhanced Language Model for Inconsistent Hallucination Detection  _(ACM Transactions on Asian and Low-Resource Languag)_
- [2026] **其它:ACM Transactions on Software Engineering** · Hallucination to Consensus: Multi-Agent LLMs for End-to-End JUnit Test Generation  _(ACM Transactions on Software Engineering and Metho)_
- [2026] **其它:Advanced International Journal for Resea** · Agentic Data Architecture (Ada): Eliminating The Api Layer For Hallucination-Free, Sub-100ms Enterprise AI Agents  _(Advanced International Journal for Research)_
- [2026] **其它:Advances in Computer Science Research** · Comprehensive to the Textual Hallucination in Generative AI  _(Advances in Computer Science Research)_
- [2026] **其它:Advances in Machine Learning &amp; Artif** · Analog Hawking Radiation in Transformer Neural Networks: Discrete Geometric Horizons, Information Thermodynamics, and Hallucination Suppression  _(Advances in Machine Learning &amp; Artificial Inte)_
- [2026] **其它:Advances in Transdisciplinary Engineerin** · Mitigating Visual Hallucination in Multimodal Event Extraction via Constrained Prompting  _(Advances in Transdisciplinary Engineering)_
- [2026] **其它:Adversarial Machine Learning** · Data Leakage and Model Hallucination  _(Adversarial Machine Learning)_
- [2026] **其它:Applications of Neuro-Symbolic Artificia** · Adversarial Abductive Dialogue Framework with Reinforcement for Tackling LLM Hallucination  _(Applications of Neuro-Symbolic Artificial Intellig)_
- [2026] **其它:Artificial Intelligence and Robotics Res** · A Survey of Hallucination in Large Language Models  _(Artificial Intelligence and Robotics Research)_
- [2026] **其它:Communications in Computer and Informati** · DHI: Leveraging Diverse Hallucination Induction for Enhanced Contrastive Factuality Control in Large Language Models  _(Communications in Computer and Information Science)_
- [2026] **其它:Communications in Computer and Informati** · Shadows in the Attention: Contextual Perturbation and Representation Drift in the Dynamics of Hallucination in LLMs  _(Communications in Computer and Information Science)_
- [2026] **其它:Computer and Decision Making: An Interna** · Hallucination Detection in Large Language Models via Multi-Granular Uncertainty Quantification  _(Computer and Decision Making: An International Jou)_
- [2026] **其它:INTERNATIONAL JOURNAL OF CREATIVE RESEAR** · Trustworthiness, Hallucination, and Evaluation in Large Language Models  _(INTERNATIONAL JOURNAL OF CREATIVE RESEARCH THOUGHT)_
- [2026] **其它:Iconic Research and Engineering Journals** · A Multi-Metric Evaluation Perspective on Hallucination Detection in Low-Resource Governance Documents  _(Iconic Research and Engineering Journals)_
- [2026] **其它:Iconic Research and Engineering Journals** · Hallucination Detection, Categorization, and Mitigation in Large Language Models: A Cross-Domain Evaluation Framework  _(Iconic Research and Engineering Journals)_
- [2026] **其它:International Journal of Advanced Resear** · Detectra-AI Response Hallucination Detector  _(International Journal of Advanced Research in Scie)_
- [2026] **其它:International Journal of Computer Applic** · TempHalluc-Bench: Evaluating Temporal Hallucination in VideoLLM-Based Video Search and Information Extraction  _(International Journal of Computer Applications)_
- [2026] **其它:International Journal of Engineering and** · A Context-Aware Hallucination Detection Framework for Large Language Models in High-Stakes Domains  _(International Journal of Engineering and Computer )_
- [2026] **其它:International Journal of Innovative Rese** · Slopsquatting and package-hallucination in LLMS  _(International Journal of Innovative Research in Te)_
- [2026] **其它:International Journal of Research Public** · Hallucination Detection and Mitigation in Large Language Models Using Lightweight Inference-Time Models  _(International Journal of Research Publication and )_
- [2026] **其它:Proceedings of the International Confere** · The Immutable Hallucination: A Critical Analysis of AI-Blockchain Integration in Healthcare  _(Proceedings of the International Conference on Art)_
- [2026] **其它:RIGGS: Journal of Artificial Intelligenc** · Analisis Implementasi Artificial Intelligence dalam Audit Keuangan Atas Kasus Hallucination AI Deloitte Australia 2025  _(RIGGS: Journal of Artificial Intelligence and Digi)_
- [2026] **其它:Radiology: Artificial Intelligence** · A Taxonomy of Machine Hallucination in Radiology  _(Radiology: Artificial Intelligence)_
- [2025] **IEEE(未解析)** · Hallucination-Free Automatic Question &amp; Answer Generation for Intuitive Learning  _(2025 IEEE International Conference on Image Proces)_
- [2025] **Springer(未解析)** · Few-Shot Optimized Framework for Hallucination Detection in Resource-Limited NLP Systems  _(Lecture Notes in Networks and Systems)_
- [2025] **其它:2025 16th International Conference on E-** · AI Hallucination in the Context of Education: Exploring College Students’ Use of Generative AI for Academic Tasks  _(2025 16th International Conference on E-Education,)_
- [2025] **其它:2025 2nd International Conference on Com** · RAG Technology for Reliable Medical Retrieval and Hallucination Mitigation  _(2025 2nd International Conference on Computer Comm)_
- [2025] **其它:2025 Cyber Awareness and Research Sympos** · Persona Vectors in Controlling Hallucination of Small Large Language Models: A Safety-Oriented Analysis  _(2025 Cyber Awareness and Research Symposium (CARS))_
- [2025] **其它:2025 Eighth International Conference on ** · Confident but Incorrect: Mitigating Hallucination and Overconfidence in Agentic AI Coders  _(2025 Eighth International Conference on Image Info)_
- [2025] **其它:2025 International Conference on Artific** · AI Hallucination and Strategies to Overcome: Enhancing Human-AI Interaction  _(2025 International Conference on Artificial Intell)_
- [2025] **其它:2025 Multimedia University Engineering C** · Countering AI Hallucination by Utilizing a Concept-Aware Model  _(2025 Multimedia University Engineering Conference )_
- [2025] **其它:Artificial Intelligence and Applications** · Synthetic Data in AI: Performance Gains versus Hallucination Risk  _(Artificial Intelligence and Applications)_
- [2025] **其它:Artificial Intelligence and Machine Lear** · Hallucination Detection and Confidence Calibration for Large Language Model Outputs: Reproducible Experiments on HaluEval  _(Artificial Intelligence and Machine Learning Revie)_
- [2025] **其它:Communications in Humanities Research** · An Analysis on AI Hallucination from the Perspective of Media Archaeology  _(Communications in Humanities Research)_
- [2025] **其它:Companion Proceedings of the ACM on Web ** · Uncertainty-Aware Fusion: An Ensemble Framework for Mitigating Hallucinations in Large Language Models  _(Companion Proceedings of the ACM on Web Conference)_
- [2025] **其它:Frontiers in Emerging Artificial Intelli** · Agentic Legal Intake: A Multi-Agent Framework For Hallucination-Free, Audit-Ready AI Screening In Mass-Tort Litigation  _(Frontiers in Emerging Artificial Intelligence and )_
- [2025] **其它:ICCK Transactions on Emerging Topics in ** · Beyond Hallucination: Generative AI as a Catalyst for Human Creativity and Cognitive Evolution  _(ICCK Transactions on Emerging Topics in Artificial)_
- [2025] **其它:International Journal of Artificial Inte** · Ethical Prompt Design for Health Equity: Preventing Hallucination and Addressing Bias in AI Diagnoses  _(International Journal of Artificial Intelligence, )_
- [2025] **其它:International Journal of Artificial Inte** · S-AI-ANTI HALLUCINATION: A BIO-INSPIRED AND CONFIDENCE-AWARE SPARSE AI FRAMEWORK FOR RELIABLE GENERATIVE SYSTEMS  _(International Journal of Artificial Intelligence &)_
- [2025] **其它:International Journal of Computer Applic** · GRAVITI: Grounded Retrieval Generation Framework for VideoLLM Hallucination Mitigation  _(International Journal of Computer Applications)_
- [2025] **其它:International Journal of Science and Res** · Generative AI in Medical Pharmacology: Balancing Educational Benefits and Hallucination Risks  _(International Journal of Science and Research (IJS)_
- [2025] **其它:Journal of Vision** · Stroboscopic hallucination spatial frequency corresponds to strobe stimulation temporal frequency  _(Journal of Vision)_
- [2025] **其它:Natural Language Processing Journal** · WITHDRAWN: Ambiguity processing in Large Language Models: Detection, resolution, and the path to hallucination  _(Natural Language Processing Journal)_
- [2025] **其它:Open Research Europe** · Comparison of explainability methods for hallucination analysis in LLMs  _(Open Research Europe)_
- [2025] **其它:Proceedings of The Third Arabic Natural ** · AraHalluEval: A Fine-grained Hallucination Evaluation Framework for Arabic LLMs  _(Proceedings of The Third Arabic Natural Language P)_
- [2025] **其它:Proceedings of the International Confere** · Can We Trust Large Language Models for Video Analysis: An Exploration of Hallucination in Multimodal LLMs  _(Proceedings of the International Conference of the)_
- [2025] **其它:Proceedings of the International Confere** · The hallucination problem in Generative Artificial Intelligence: accuracy and trust in digital learning  _(Proceedings of the International Conference on Vir)_
- [2025] **其它:Schizophrenia Research: Cognition** · Multidimensionality of hallucination-like experiences: A factor structure refinement of the Launay-Slade Hallucination Scale  _(Schizophrenia Research: Cognition)_
- [2025] **其它:Second International Conference on Image** · ReSelfVerMM: mitigating hallucination in multimodal LLMs through dataset reconstruction and self-verification  _(Second International Conference on Image Processin)_
- [2025] **其它:Studies in Computational Intelligence** · Hallucination and Panic in Autonomous Systems  _(Studies in Computational Intelligence)_
- [2024] **IEEE(未解析)** · Evaluating Hallucination in Medical Prompt Responses: A Comparative Study of ChatGPT-4 and ChatGPT-4o  _(2024 IEEE International Conference on Communicatio)_
- [2024] **Springer(未解析)** · Can Hallucination Reduction in LLMs Improve Online Sexism Detection?  _(Lecture Notes in Networks and Systems)_
- [2024] **其它:2024 7th International Conference on Pat** · Alleviating Action Hallucination for LLM-based Embodied Agents via Inner and Outer Alignment  _(2024 7th International Conference on Pattern Recog)_
- [2024] **其它:European Conference on e-Learning** · The Problem of AI Hallucination and How to Solve It  _(European Conference on e-Learning)_
- [2024] **其它:Proceedings of the 13th Joint Conference** · MASSIVE Multilingual Abstract Meaning Representation: A Dataset and Baselines for Hallucination Detection  _(Proceedings of the 13th Joint Conference on Lexica)_
- [2024] **其它:Proceedings of the 18th International Wo** · AILS-NTUA at SemEval-2024 Task 6: Efficient model tuning for hallucination detection and analysis  _(Proceedings of the 18th International Workshop on )_
- [2024] **其它:Proceedings of the 18th International Wo** · DUTh at SemEval-2024 Task 6: Comparing Pre-trained Models on Sentence Similarity Evaluation for Detecting of Hallucinations and Related Observable Overgeneration Mistakes  _(Proceedings of the 18th International Workshop on )_
- [2024] **其它:Proceedings of the 18th International Wo** · HIT-MI&amp;T Lab at SemEval-2024 Task 6: DeBERTa-based Entailment Model is a Reliable Hallucination Detector  _(Proceedings of the 18th International Workshop on )_
- [2024] **其它:Proceedings of the 6th Clinical Natural ** · Gemini Goes to Med School: Exploring the Capabilities of Multimodal Large Language Models on Medical Challenge Problems &amp; Hallucinations  _(Proceedings of the 6th Clinical Natural Language P)_
- [2024] **其它:Proceedings of the 7th BlackboxNLP Works** · LLM Internal States Reveal Hallucination Risk Faced With a Query  _(Proceedings of the 7th BlackboxNLP Workshop: Analy)_
- [2020] **其它:International Journal For Multidisciplin** · Structural Hallucination in LLMs: A Formal Characterization and Mitigation Method  _(International Journal For Multidisciplinary Resear)_

## C. 其它链接（19）

- [2025] **其它链接** · Benford&apos;s Curse: Tracing Digit Bias to Numerical Hallucination in LLMs
- [2025] **其它链接** · Mitigating Hallucination Through Theory-Consistent Symmetric Multimodal Preference Optimization
- [2024] **其它链接** · Analyzing and Mitigating Object Hallucination in Large Vision-Language Models
- [2024] **其它链接** · Coarse-to-Fine Highlighting: Reducing Knowledge Hallucination in Large Language Models
- [2024] **其它链接** · ERBench: An Entity-Relationship based Automatically Verifiable Hallucination Benchmark for Large Language Models
- [2024] **其它链接** · Estimating the Hallucination Rate of Generative AI
- [2024] **其它链接** · Evaluating and Analyzing Relationship Hallucinations in Large Vision-Language Models
- [2024] **其它链接** · Explicitly Stating Assumptions Reduces Hallucinations in Natural Language Inference
- [2024] **其它链接** · Hallo3D: Multi-Modal Hallucination Detection and Mitigation for Consistent 3D Content Generation
- [2024] **其它链接** · Hallucination Benchmark in Medical Visual Question Answering
- [2024] **其它链接** · HaloScope: Harnessing Unlabeled LLM Generations for Hallucination Detection
- [2024] **其它链接** · How Language Model Hallucinations Can Snowball
- [2024] **其它链接** · INSIDE: LLMs&apos; Internal States Retain the Power of Hallucination Detection
- [2024] **其它链接** · Leveraging Hallucinations to Reduce Manual Prompt Dependency in Promptable Segmentation
- [2024] **其它链接** · Looks Too Good To Be True: An Information-Theoretic Analysis of Hallucinations in Generative Restoration Models
- [2024] **其它链接** · Mitigating Hallucination in Large Multi-Modal Models via Robust Instruction Tuning
- [2024] **其它链接** · RadFlag: A Black-Box Hallucination Detection Method for Medical Vision Language Models
- [2024] **其它链接** · Self-contradictory Hallucinations of Large Language Models: Evaluation, Detection and Mitigation
- [2024] **其它链接** · Toward a Stable, Fair, and Comprehensive Evaluation of Object Hallucination in Large Vision-Language Models

## D. 无链接（8）

- [2025] **无链接** · RAR: Reversing Visual Attention Re-sinking for Unlocking Potential in Multimodal Large Language Models
- [2024] **无链接** · CausalLens: Sensitivity-Guided Multi-Head Causal Intervention for Hallucination Mitigation in Large Vision-Language Models
- [2024] **无链接** · ELV-Halluc: Benchmarking Semantic Aggregation Hallucinations in Video Understanding
- [2024] **无链接** · Envision, Attend, Then Respond: Counterfactual Hallucination Mitigation in Large Vision-Language Models
- [2024] **无链接** · Fine-Grained Multi Image Object Hallucination Benchmark
- [2024] **无链接** · HAIT: Hybrid Adversarial Iterative Training for Mitigating Object Hallucination in Large Vision-Language Models
- [2024] **无链接** · Same Attention, Different Truths: Put Logit-Lens over Visual Attention to Detect and Mitigate LVLM Object Hallucination
- [2024] **无链接** · Unstitching the Chimera: Frame-Level Risk and Train-Free Mitigation for Video Hallucination

## 三、值得注意的点

1. **疑似漏网的经典 CV 技术义论文**：`Visual Hallucination Elevates Speech Recognition`（AAAI 2024）—— "visual hallucination" 作为提升语音识别的方法，属 CV 技术义，当前 `OFF_TOPIC` 未覆盖（原正则只匹配 "for speech recognition"）。建议补规则后删除。
2. **ccf.json 缺口**：`CL`（*Computational Linguistics* 期刊，CCF-B）未登记，导致 A 组中 5 篇 CL 论文当前 CCF 显示为空（实为 CCF-B）。建议补 `"CL":"B"`。
3. A 组中大量为 EMNLP/AAAI/ICASSP 的正经幻觉检测/缓解论文，质量无问题，回填 venue 即可。