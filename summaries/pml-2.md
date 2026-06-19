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
| **21.3 - VAE Generalizations** | [β-VAE](../notebooks/pml-2/21-variational-autoencoders/21-3-1-beta_vae.ipynb) | Disentangling cell-cycle phase from drug dose in synthetic scRNA-seq, tracing the rate–distortion curve and measuring total correlation as β varies | $\mathcal{L}_\beta = -\mathbb{E}_{q_{\boldsymbol{\phi}}(\mathbf{z}\mid\mathbf{x})}[\log p_{\boldsymbol{\theta}}(\mathbf{x}\mid\mathbf{z})] + \beta\, D_{\mathrm{KL}}(q_{\boldsymbol{\phi}}(\mathbf{z}\mid\mathbf{x})\,\|\,p_{\boldsymbol{\theta}}(\mathbf{z}))$ |
| | [Multimodal VAE](../notebooks/pml-2/21-variational-autoencoders/21-3-3-multimodal_vae.ipynb) | Fusing CITE-seq RNA and surface-protein measurements with a product-of-experts inference network; cross-modal imputation when one modality is missing | $q_{\boldsymbol{\phi}}(\mathbf{z}\mid\mathbf{X}) \propto p(\mathbf{z})\prod_{m=1}^M \tilde{q}(\mathbf{z}\mid\mathbf{x}_m)$ |
| | [Semi-supervised VAE](../notebooks/pml-2/21-variational-autoencoders/21-3-4-semisupervised_vae.ipynb) | Cell-type classification on scRNA-seq with 200 labeled + 4800 unlabeled cells: the M2 model marginalizes over $y$ for unlabeled examples and disentangles cell type from continuous state | $\mathcal{L} = \mathbb{E}_{\mathcal{D}_L}[\mathcal{L}(\mathbf{x},y)] + \mathbb{E}_{\mathcal{D}_U}[\mathcal{U}(\mathbf{x})] + \alpha\,\mathbb{E}_{\mathcal{D}_L}[-\log q_{\boldsymbol{\phi}}(y\mid\mathbf{x})]$ |
| **21.4 - Avoiding Posterior Collapse** | [Posterior Collapse (DNA motifs)](../notebooks/pml-2/21-variational-autoencoders/21-4-1-avoiding_posterior_collapse.ipynb) | A VAE over DNA regulatory sequences with an autoregressive GRU decoder collapses under the vanilla ELBO (latent unused); KL annealing, cyclical annealing, and free bits revive the code | $\mathcal{L}_R' = \sum_i \max\!\left(\lambda,\, D_{\mathrm{KL}}\!\left(q_{\boldsymbol{\phi}}(z_i\mid\mathbf{x})\,\|\,p_{\boldsymbol{\theta}}(z_i)\right)\right)$ |
| | [Posterior Collapse (Perturb-seq)](../notebooks/pml-2/21-variational-autoencoders/21-4-2-perturbation_vae_collapse.ipynb) | A CPA/scGen-style virtual-cell VAE over a Perturb-seq screen: a powerful decoder collapses the perturbation latent so the model predicts "no effect" (the linear-baseline trap); rate, active-unit, knockout-probe, and decoder-usage diagnostics show the same fixes recover the signal | $\mathcal{L} = \mathbb{E}_{q_{\boldsymbol{\phi}}(\mathbf{z}\mid\mathbf{x})}[\log p_{\boldsymbol{\theta}}(\mathbf{x}\mid\mathbf{z})] - \beta_t\, D_{\mathrm{KL}}\!\left(q_{\boldsymbol{\phi}}(\mathbf{z}\mid\mathbf{x})\,\|\,p(\mathbf{z})\right),\ \beta_t: 0 \to 1$ |
