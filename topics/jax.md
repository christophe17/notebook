# JAX

Interactive notebooks for learning **JAX** — high-performance numerical computing and machine learning.

---

## 2 - UvA

| | | | |
|---|---|---|---|
| **2.1 - Single-GPU Training** | [Single-GPU Techniques](../notebooks/jax/2-uva/2-1-1-single_gpu_techniques.ipynb) | Protein localization classifier combining mixed precision, gradient checkpointing & accumulation | $\nabla_\theta \mathcal{L} = \frac{1}{K}\sum_{k=1}^{K} \nabla_\theta \mathcal{L}_k$ |
| | [Single-GPU Transformer](../notebooks/jax/2-uva/2-1-2-single_gpu_transformer.ipynb) | DNA sequence transformer with mixed precision, remat, gradient accumulation & layer scanning | $\text{Attention}(Q,K,V) = \text{softmax}_{\text{f32}}\!\left(\frac{QK^\top}{\sqrt{d_k}}\right)\!V$ |
| **2.2 - Multi-Device Training** | [Data Parallelism & FSDP](../notebooks/jax/2-uva/2-2-1-data_parallel_fsdp.ipynb) | Drug response classifier distributed across devices with shard_map, comparing DP and FSDP strategies | $\bar{g} = \frac{1}{N}\sum_{i=1}^{N} g_i$ |

---

## 7 - Recap Project

| | | | |
|---|---|---|---|
| **7.1 - Course Recap** | [Drug Response Prediction](../notebooks/jax/7-recap-project/7-1-1-drug_response_prediction.ipynb) | Predicting cancer drug sensitivity from gene expression using a neural network built from scratch | $\hat{y} = W_2 \cdot \text{relu}(W_1 x + b_1) + b_2$ |
| **7.2 - Full Project** | [Protein Language Model](../notebooks/jax/7-recap-project/7-2-1-protein_language_model.ipynb) | Decoder-only transformer (GPT) trained to model protein sequence grammar | $\text{Attention}(Q,K,V) = \text{softmax}\!\left(\frac{QK^\top}{\sqrt{d_k}}\right)\!V$ |

---
