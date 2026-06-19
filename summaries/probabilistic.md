# Probability Distributions

Interactive notebooks covering the main probability distributions — their parameters, shapes, and use cases.

---

## 1 - Discrete Distributions

| | | | |
|---|---|---|---|
| **1.1 - Bernoulli & Binomial** | [Bernoulli](../notebooks/probabilistic/1-discrete/1-1-1-bernoulli.ipynb) | Single coin flip: success/failure of a PCR amplification | $p(x) = p^x (1-p)^{1-x}$ |
| | [Binomial](../notebooks/probabilistic/1-discrete/1-1-2-binomial.ipynb) | Number of cells expressing a marker out of N sampled | $p(k) = \binom{n}{k} p^k (1-p)^{n-k}$ |
| **1.2 - Categorical & Multinomial** | [Categorical](../notebooks/probabilistic/1-discrete/1-2-1-categorical.ipynb) | Cell type assignment among K possible types | $p(x = k) = \pi_k$ |
| | [Multinomial](../notebooks/probabilistic/1-discrete/1-2-2-multinomial.ipynb) | Read counts across K genes in an RNA-seq sample | $p(\mathbf{x}) = \frac{n!}{\prod_k x_k!} \prod_k \pi_k^{x_k}$ |
| **1.3 - Poisson** | [Poisson](../notebooks/probabilistic/1-discrete/1-3-1-poisson.ipynb) | mRNA transcript counts per cell in steady state | $p(k) = \frac{\lambda^k e^{-\lambda}}{k!}$ |
| **1.4 - Geometric & Negative Binomial** | [Geometric](../notebooks/probabilistic/1-discrete/1-4-1-geometric.ipynb) | Trials until first successful CRISPR edit | $p(k) = (1-p)^{k-1} p$ |
| | [Negative Binomial](../notebooks/probabilistic/1-discrete/1-4-2-negative_binomial.ipynb) | Overdispersed RNA-seq counts (Poisson + Gamma rate) | $p(k) = \binom{k+r-1}{k} (1-p)^r p^k$ |
| **1.5 - Count Noise Models in scRNA-seq** | [Poisson & NB in scRNA-seq](../notebooks/probabilistic/1-discrete/1-5-1-scrnaseq_noise_models.ipynb) | Technical sampling + biological variability in single-cell counts | $\mathrm{Var}(Y) = \mu + \mu^2 / r$ |

---

## 2 - Continuous Univariate Distributions

| | | | |
|---|---|---|---|
| **2.1 - Uniform** | [Uniform](../notebooks/probabilistic/2-continuous/2-1-1-uniform.ipynb) | Uninformative prior over a bounded parameter | $p(x) = \frac{1}{b-a}$ |
| **2.2 - Normal / Gaussian** | [Normal](../notebooks/probabilistic/2-continuous/2-2-1-normal.ipynb) | Measurement noise on a continuous lab readout | $p(x) = \frac{1}{\sqrt{2\pi\sigma^2}} e^{-\frac{(x-\mu)^2}{2\sigma^2}}$ |
| **2.3 - Exponential** | [Exponential](../notebooks/probabilistic/2-continuous/2-3-1-exponential.ipynb) | Waiting time between Poisson-distributed transcription events | $p(x) = \lambda e^{-\lambda x}$ |
| **2.4 - Gamma** | [Gamma](../notebooks/probabilistic/2-continuous/2-4-1-gamma.ipynb) | Prior over a positive rate (e.g. enzyme kinetics constant) | $p(x) = \frac{\beta^\alpha}{\Gamma(\alpha)} x^{\alpha-1} e^{-\beta x}$ |
| **2.5 - Beta** | [Beta](../notebooks/probabilistic/2-continuous/2-5-1-beta.ipynb) | Prior over a binding-site occupancy probability | $p(x) = \frac{x^{\alpha-1}(1-x)^{\beta-1}}{B(\alpha,\beta)}$ |
| **2.6 - Student-t** | [Student-t](../notebooks/probabilistic/2-continuous/2-6-1-student_t.ipynb) | Robust regression with heavy-tailed measurement errors | $p(x) \propto \left(1 + \frac{x^2}{\nu}\right)^{-(\nu+1)/2}$ |
| **2.7 - Chi-squared** | [Chi-squared](../notebooks/probabilistic/2-continuous/2-7-1-chi_squared.ipynb) | Sum-of-squares test statistic | $p(x) = \frac{1}{2^{k/2}\Gamma(k/2)} x^{k/2-1} e^{-x/2}$ |
| **2.8 - Laplace** | [Laplace](../notebooks/probabilistic/2-continuous/2-8-1-laplace.ipynb) | Sparsity-inducing prior (L1 / lasso) | $p(x) = \frac{1}{2b} e^{-\lvert x-\mu \rvert / b}$ |
| **2.9 - Cauchy** | [Cauchy](../notebooks/probabilistic/2-continuous/2-9-1-cauchy.ipynb) | Heavy-tailed prior with undefined moments | $p(x) = \frac{1}{\pi \gamma \left[1 + \left(\frac{x-x_0}{\gamma}\right)^2\right]}$ |
| **2.10 - Log-normal** | [Log-normal](../notebooks/probabilistic/2-continuous/2-10-1-log_normal.ipynb) | Gene expression levels (multiplicative noise on log-scale) | $p(x) = \frac{1}{x\sigma\sqrt{2\pi}} e^{-\frac{(\ln x - \mu)^2}{2\sigma^2}}$ |

---

## 3 - Multivariate Distributions

| | | | |
|---|---|---|---|
| **3.1 - Multivariate Normal** | [Multivariate Normal](../notebooks/probabilistic/3-multivariate/3-1-1-multivariate_normal.ipynb) | Joint distribution over correlated gene expression levels | $p(\mathbf{x}) = \mathcal{N}(\mathbf{x} \mid \boldsymbol{\mu}, \Sigma)$ |
| **3.2 - Multivariate Student-t** | [Multivariate Student-t](../notebooks/probabilistic/3-multivariate/3-2-1-multivariate_student_t.ipynb) | Robust joint distribution with heavy tails | $p(\mathbf{x}) \propto \left(1 + \frac{1}{\nu}(\mathbf{x}-\boldsymbol{\mu})^\top \Sigma^{-1} (\mathbf{x}-\boldsymbol{\mu})\right)^{-(\nu+d)/2}$ |
| **3.3 - Dirichlet** | [Dirichlet](../notebooks/probabilistic/3-multivariate/3-3-1-dirichlet.ipynb) | Prior over cell-type proportions in a tissue sample | $p(\boldsymbol{\pi}) = \frac{1}{B(\boldsymbol{\alpha})} \prod_k \pi_k^{\alpha_k - 1}$ |
| **3.4 - Wishart** | [Wishart](../notebooks/probabilistic/3-multivariate/3-4-1-wishart.ipynb) | Prior over a precision matrix | $p(\Lambda) \propto \lvert\Lambda\rvert^{(\nu-d-1)/2} e^{-\frac{1}{2}\text{tr}(V^{-1}\Lambda)}$ |
| **3.5 - Inverse-Wishart** | [Inverse-Wishart](../notebooks/probabilistic/3-multivariate/3-5-1-inverse_wishart.ipynb) | Prior over a covariance matrix | $p(\Sigma) \propto \lvert\Sigma\rvert^{-(\nu+d+1)/2} e^{-\frac{1}{2}\text{tr}(V\Sigma^{-1})}$ |

---

## 4 - Conjugate Priors & Exponential Family

| | | | |
|---|---|---|---|
| **4.1 - Exponential Family** | [Exponential Family](../notebooks/probabilistic/4-conjugate/4-1-1-exponential_family.ipynb) | Unified form covering Normal, Bernoulli, Poisson, Gamma, ... | $p(x \mid \boldsymbol{\eta}) = h(x) \exp\!\big(\boldsymbol{\eta}^\top T(x) - A(\boldsymbol{\eta})\big)$ |
| **4.2 - Conjugate Pairs** | [Beta-Bernoulli](../notebooks/probabilistic/4-conjugate/4-2-1-beta_bernoulli.ipynb) | Sequential updating of a success probability | $\text{Beta}(\alpha + k, \beta + n - k)$ |
| | [Dirichlet-Multinomial](../notebooks/probabilistic/4-conjugate/4-2-2-dirichlet_multinomial.ipynb) | Updating cell-type proportions from observed counts | $\text{Dir}(\boldsymbol{\alpha} + \mathbf{x})$ |
| | [Gamma-Poisson](../notebooks/probabilistic/4-conjugate/4-2-3-gamma_poisson.ipynb) | Updating a Poisson rate from observed counts | $\text{Gamma}(\alpha + \sum x_i,\ \beta + n)$ |
| | [Normal-Normal (known variance)](../notebooks/probabilistic/4-conjugate/4-2-4-normal_normal.ipynb) | Updating a mean from noisy measurements | $\mathcal{N}(\mu_n, \sigma_n^2)$ |
| | [Normal-Inverse-Gamma](../notebooks/probabilistic/4-conjugate/4-2-5-normal_inverse_gamma.ipynb) | Jointly updating mean and variance | $\text{NIG}(\mu_n, \lambda_n, \alpha_n, \beta_n)$ |
