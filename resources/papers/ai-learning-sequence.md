# AI Learning Sequence: Detailed Reading Order

## Overview
This sequence is organized to build concepts progressively. Each article is listed with:
- Reading order number (RO#)
- Phase
- Source
- Article title
- Key prerequisites
- Core concepts covered
- Estimated reading time
- Suggested practice

## Phase 1: Foundations (2015-2017)

| RO# | Source | Article | Prerequisites | Core Concepts | Time | Practice |
|-----|---------|---------|---------------|---------------|------|----------|
| 1.1 | Weng | An Overview of Deep Learning | Python basics | Neural networks, backprop | 2h | Implement basic neural net |
| 1.2 | Distill | Visualizing Neural Networks | 1.1 | Network visualization, activation patterns | 1.5h | Visualize MNIST network |
| 1.3 | Weng | From Autoencoder to Beta-VAE | 1.1, 1.2 | Autoencoders, latent spaces | 2h | Build simple autoencoder |
| 1.4 | Distill | Attention and Augmented RNNs | 1.1-1.3 | Basic attention mechanisms | 2h | Implement attention layer |
| 1.5 | Distill | Why Momentum Really Works | 1.1-1.4 | Optimization techniques | 1.5h | Compare optimizers |
| 1.6 | Weng | Attention Mechanisms | 1.4 | Advanced attention concepts | 2.5h | Attention visualization |
| 1.7 | Distill | Feature Visualization | All above | Feature interpretation | 2h | Visualize CNN layers |

## Phase 2: Advanced Concepts (2018-2019)

| RO# | Source | Article | Prerequisites | Core Concepts | Time | Practice |
|-----|---------|---------|---------------|---------------|------|----------|
| 2.1 | Gradient | A New Look at Deep Learning | Phase 1 | Modern DL landscape | 1h | - |
| 2.2 | Distill | Building Blocks of Interpretability | 1.7 | Model interpretation | 2.5h | Build interpretation tools |
| 2.3 | Weng | Meta Learning | 2.1, 2.2 | Learning to learn | 2h | Implement MAML |
| 2.4 | Gradient | Understanding LSTM Networks | 1.4, 2.1 | Sequential learning | 2h | Build LSTM network |
| 2.5 | Distill | Visualizing Memorization in RNNs | 2.4 | RNN internals | 2h | RNN visualization |
| 2.6 | Weng | Generalized Language Models | 2.4, 2.5 | Early language models | 2.5h | Train small LM |
| 2.7 | Gradient | The Past, Present, and Future of AI Art | 2.1-2.6 | Creative AI | 1h | - |
| 2.8 | Weng | Evolution Strategies | 2.1-2.7 | Alternative training | 2h | Implement simple ES |
| 2.9 | Distill | Weight Standardization | All above | Advanced optimization | 1.5h | Compare norm methods |
| 2.10 | Weng | Meta Reinforcement Learning | All above | Advanced RL concepts | 3h | Build basic RL agent |

## Phase 3: Modern Architecture Era (2020-2021)

| RO# | Source | Article | Prerequisites | Core Concepts | Time | Practice |
|-----|---------|---------|---------------|---------------|------|----------|
| 3.1 | Gradient | The Rise of Self-Supervised Learning | Phase 2 | Modern training paradigms | 1.5h | Implement SimCLR |
| 3.2 | Weng | How to Train Really Large Models | 3.1 | Scaling challenges | 2h | Distributed training |
| 3.3 | Distill | Weight Uncertainty in Neural Networks | 3.2 | Bayesian deep learning | 2.5h | Bayesian neural net |
| 3.4 | Weng | BERT and the Transformer Family | 3.1-3.3 | Modern transformers | 3h | Build transformer block |
| 3.5 | Gradient | A Survey of Transformers | 3.4 | Architecture overview | 2h | Compare architectures |
| 3.6 | Distill | Growing Neural Cellular Automata | 3.1-3.5 | Emergent computation | 2h | Implement NCA |
| 3.7 | Weng | Few-Shot Learning | 3.1-3.6 | Sample efficiency | 2.5h | Few-shot classifier |
| 3.8 | Gradient | The State of AI Ethics | 3.1-3.7 | Ethical considerations | 1.5h | - |
| 3.9 | Weng | Contrastive Representation Learning | 3.1-3.8 | Modern embeddings | 2.5h | Implement ContrastiveLoss |
| 3.10 | Distill | Multimodal Neurons | All above | Cross-modal learning | 2h | Analyze CLIP neurons |

## Phase 4: Large Models & Scaling (2022-2024)

| RO# | Source | Article | Prerequisites | Core Concepts | Time | Practice |
|-----|---------|---------|---------------|---------------|------|----------|
| 4.1 | Weng | Knowledge Graphs | Phase 3 | Structured knowledge | 2h | Build small knowledge graph |
| 4.2 | Gradient | Understanding Chain of Thought | 4.1 | Reasoning patterns | 2h | Implement CoT prompting |
| 4.3 | Weng | Foundation Models | 4.1, 4.2 | Modern architectures | 2.5h | Study architecture papers |
| 4.4 | Gradient | The Rise of Foundation Models | 4.3 | Industry impact | 1.5h | - |
| 4.5 | Weng | Prompting Large Language Models | 4.1-4.4 | Prompt engineering | 2h | Design prompt templates |
| 4.6 | Weng | In-Context Learning | 4.5 | Few-shot prompting | 2.5h | ICL experiments |
| 4.7 | Gradient | AI Alignment Perspectives | 4.1-4.6 | Safety considerations | 1.5h | - |
| 4.8 | Weng | LLM Inference | 4.1-4.7 | Optimization techniques | 2.5h | Implement basic inference |
| 4.9 | Gradient | Modern LLM Architecture Deep Dive | 4.8 | Current SOTA | 2h | Study architecture code |
| 4.10 | Weng | Instruction Tuning | All above | Advanced fine-tuning | 2.5h | Small instruction tuning |

## Reading Tips
1. Complete all prerequisites before moving to an article
2. Do the suggested practice exercises where provided
3. Take notes on:
   - Key concepts and their relationships
   - Questions that arise
   - Connections to previous readings
4. Review phase summaries before moving to next phase

## Estimated Timeline
- Phase 1: 4-5 weeks (13.5h reading + practice)
- Phase 2: 6-7 weeks (19.5h reading + practice)
- Phase 3: 5-6 weeks (21h reading + practice)
- Phase 4: 4-5 weeks (20.5h reading + practice)

Total: ~5-6 months at 5-7 hours/week
