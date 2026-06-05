# Probabilistic Machine Learning — Advanced Topics

Interactive notebooks accompanying **Probabilistic Machine Learning: Advanced Topics**.

---

## 10 - Variational Inference

| | | | |
|---|---|---|---|
| **10.2 - Gradient-based VI** | [Reparameterized VI](../notebooks/pml-2/10-variational-inference/10-2-1-reparameterized_vi.ipynb) | Inferring mRNA synthesis and degradation rates from RNA-seq counts using diagonal, full, and low-rank Gaussian posteriors | $\mathbf{z} = \boldsymbol{\mu} + \mathbf{L}\boldsymbol{\epsilon},\ \boldsymbol{\epsilon} \sim \mathcal{N}(\mathbf{0}, \mathbf{I})$ |

## 21 - Variational Autoencoders

| | | | |
|---|---|---|---|
| **21.2 - VAE Basics** | [VAE Basics](../notebooks/pml-2/21-variational-autoencoders/21-2-1-vae_basics.ipynb) | Learning a 2D latent space of single-cell chromatin accessibility with a Bernoulli decoder and full-covariance Gaussian encoder | $\mathcal{L} = \mathbb{E}_{q_{\boldsymbol{\phi}}(\mathbf{z}\mid\mathbf{x})}[\log p_{\boldsymbol{\theta}}(\mathbf{x}\mid\mathbf{z})] - D_{\mathrm{KL}}(q_{\boldsymbol{\phi}}(\mathbf{z}\mid\mathbf{x})\,\|\,p(\mathbf{z}))$ |
