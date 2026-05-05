# Probabilistic Machine Learning

Interactive notebooks accompanying the **Probabilistic Machine Learning** book.

---

## 3 - Multivariate Models

| | | | |
|---|---|---|---|
| **3.2 - Multivariate Gaussian** | [Marginals and Conditionals (2D)](../notebooks/probabilistic-ml/3-multivariate-models/3-2-3-mvn_marginals_conditionals.ipynb) | Predicting EGFR protein levels from mRNA gene expression | $p(x_1 \mid x_2)$ |
| | [Marginals and Conditionals (5D)](../notebooks/probabilistic-ml/3-multivariate-models/3-2-3-mvn_marginals_conditionals_5d.ipynb) | Comprehensive real estate valuation with 5 correlated features | $p(\mathbf{x}_1 \mid \mathbf{x}_2)$ |
| | [Missing Value Imputation](../notebooks/probabilistic-ml/3-multivariate-models/3-2-5-mvn_missing_value_imputation.ipynb) | Patient health records with missing lab results | $p(\mathbf{x}_h \mid \mathbf{x}_v)$ |
| **3.3 - Linear Gaussian System** | [Bayes Rule for Gaussians](../notebooks/probabilistic-ml/3-multivariate-models/3-3-1-linear_gaussian_blood_pressure.ipynb) | Blood pressure estimation with multiple clinical devices | $p(\mathbf{z} \mid \mathbf{y}) \propto p(\mathbf{y} \mid \mathbf{z})\,p(\mathbf{z})$ |
| | [Bayes Rule with Non-Trivial W](../notebooks/probabilistic-ml/3-multivariate-models/3-3-1-linear_gaussian_derived_health_metrics.ipynb) | Inferring physiological state from derived health metrics | $\mathbf{y} = W\mathbf{z} + \boldsymbol{\epsilon}$ |
| | [Inferring an Unknown Scalar](../notebooks/probabilistic-ml/3-multivariate-models/3-3-3-bayesian_gene_expression_estimation.ipynb) | Bayesian HER2 gene expression estimation from qPCR | $p(\mu \mid \mathbf{y})$ |
| | [Inferring an Unknown Vector](../notebooks/probabilistic-ml/3-multivariate-models/3-3-4-linear_gaussian_elisa_cytokine.ipynb) | Cytokine concentration estimation from noisy ELISA replicates | $p(\mathbf{z} \mid \mathbf{y})$ |
| | [Sensor Fusion](../notebooks/probabilistic-ml/3-multivariate-models/3-3-5-sensor_fusion_cell_state_multiomics.ipynb) | Cell state estimation combining RNA-seq, flow cytometry, and ATAC-seq | $p(\mathbf{z} \mid \mathbf{y}_1, \mathbf{y}_2, \mathbf{y}_3)$ |
| **3.5 - Mixture Models** | [Gaussian Mixture Models](../notebooks/probabilistic-ml/3-multivariate-models/3-5-1-gmm_scrna_cell_types.ipynb) | Cell type discovery in scRNA-seq brain tissue using GMM | $p(\mathbf{x}) = \sum_k \pi_k \mathcal{N}(\mathbf{x} \mid \boldsymbol{\mu}_k, \Sigma_k)$ |

---

## 6 - Information Theory

| | | | |
|---|---|---|---|
| **6.1 - Entropy** | [Entropy](../notebooks/probabilistic-ml/6-information-theory/6-1-1-entropy.ipynb) | Cell state uncertainty in whole cell modeling: discrete, binary, joint, conditional entropy and perplexity | $H(X) = -\sum_k p_k \log p_k$ |
| **6.2 - KL Divergence** | [KL Divergence](../notebooks/probabilistic-ml/6-information-theory/6-2-1-kl_divergence.ipynb) | Comparing gene expression distributions across healthy and diseased tissue | $D_{\text{KL}}(p \| q) = \sum_k p_k \log \frac{p_k}{q_k}$ |
| **6.3 - Mutual Information** | [Mutual Information](../notebooks/probabilistic-ml/6-information-theory/6-3-1-mutual_information.ipynb) | Identifying informative biomarkers for cell state classification | $I(X;Y) = H(X) - H(X \mid Y)$ |

---

## 7 - Linear Algebra

| | | | |
|---|---|---|---|
| **7.0 - Foundations** | [Scalar, Vector, and Matrix Products](../notebooks/probabilistic-ml/7-linear-algebra/7-0-1-scalar_vector_matrix_products.ipynb) | Basic multiplication shapes and the dimension compatibility rule | $c = \mathbf{a}^T\mathbf{b},\ \mathbf{c} = A\mathbf{b},\ C = AB$ |
| | [Inner Product (Dot Product)](../notebooks/probabilistic-ml/7-linear-algebra/7-0-2-inner_product.ipynb) | Measuring alignment and similarity between vectors | $\mathbf{a}^T\mathbf{b} = \sum_i a_i b_i$ |
| | [Outer Product](../notebooks/probabilistic-ml/7-linear-algebra/7-0-3-outer_product.ipynb) | Creating matrices from vectors and building covariance | $\mathbf{a}\mathbf{b}^T$ |
| | [Matrix-Vector Multiplication](../notebooks/probabilistic-ml/7-linear-algebra/7-0-4-matrix_vector_multiplication.ipynb) | Geometric transformations: rotation, scaling, shearing | $\mathbf{y} = A\mathbf{x}$ |
| | [Matrix-Matrix Multiplication](../notebooks/probabilistic-ml/7-linear-algebra/7-0-5-matrix_matrix_multiplication.ipynb) | Composing transformations and the associativity property | $(AB)C = A(BC)$ |
| | [Quadratic Forms](../notebooks/probabilistic-ml/7-linear-algebra/7-0-6-quadratic_forms.ipynb) | Weighted distance and Mahalanobis | $\mathbf{x}^T W \mathbf{x}$ |
| | [The A B A.T Pattern](../notebooks/probabilistic-ml/7-linear-algebra/7-0-7-aba_transpose_pattern.ipynb) | Transforming covariance through linear maps | $\Sigma_y = A\Sigma_x A^T$ |
| | [Schur Complement](../notebooks/probabilistic-ml/7-linear-algebra/7-0-8-schur_complement.ipynb) | Block matrix operations and Gaussian conditioning | $M/D = A - BD^{-1}C$ |
| **7.3 - Matrix Inversion** | [Factor Model Covariance](../notebooks/probabilistic-ml/7-linear-algebra/7-3-factor_model_covariance_explained.ipynb) | Building gene expression covariance from transcription factor pathways | $\Sigma = WW^T + \Psi$ |
| | [Low-Rank Covariance Update](../notebooks/probabilistic-ml/7-linear-algebra/7-3-low_rank_covariance_update_explained.ipynb) | Why adding $XX^T$ to a covariance matrix models new pathway exposures | $\Sigma' = \Sigma + XX^T$ |
| | [Sherman-Morrison Formula](../notebooks/probabilistic-ml/7-linear-algebra/7-3-sherman_morrison_single_tf.ipynb) | Rank-1 precision updates when discovering a single transcription factor | $(A + \mathbf{u}\mathbf{v}^T)^{-1}$ |
| | [Matrix Inversion Lemma (Woodbury)](../notebooks/probabilistic-ml/7-linear-algebra/7-3-matrix_inversion_lemma_grn.ipynb) | Efficient precision matrix updates for gene regulatory network inference | $(A + UCV)^{-1}$ |
| **7.4 - Eigenvalue Decomposition** | [Geometry of Quadratic Forms](../notebooks/probabilistic-ml/7-linear-algebra/7-4-4-geometry_quadratic_forms.ipynb) | Ellipsoidal level sets applied to protein binding affinity in drug discovery | $\mathbf{x}^T A\mathbf{x} = c$ |
| **7.5 - Singular Value Decomposition** | [SVD](../notebooks/probabilistic-ml/7-linear-algebra/7-5-svd_gene_expression.ipynb) | Gene expression profiling: discovering latent biological programs with SVD | $A = USV^T$ |
| **7.6 - Matrix Decompositions** | [Cholesky Sampling from MVN](../notebooks/probabilistic-ml/7-linear-algebra/7-6-3-1-cholesky_mvn_sampling.ipynb) | Clinical trial simulation with correlated patient biomarkers | $\Sigma = LL^T$ |


---

## 8 - Optimization

| | | | |
|---|---|---|---|
| **8.1 - The EM Algorithm** | [Expectation-Maximization (EM)](../notebooks/probabilistic-ml/8-optimization/8-1-1-em_algorithm.ipynb) | Medical diagnosis with latent disease types using Gaussian mixtures | $\mathcal{Q}(\boldsymbol{\theta}, \boldsymbol{\theta}^{\text{old}})$ |
| **8.2 - First-Order Methods** | [Gradient Descent](../notebooks/probabilistic-ml/8-optimization/8-2-1-gradient_descent.ipynb) | Drug dose-response curve fitting with gradient descent, line search, and momentum | $\boldsymbol{\theta}_{t+1} = \boldsymbol{\theta}_t - \eta_t \nabla \mathcal{L}(\boldsymbol{\theta}_t)$ |
| **8.3 - Second-Order Methods** | [Newton, BFGS, and Trust Regions](../notebooks/probabilistic-ml/8-optimization/8-3-1-second_order_methods.ipynb) | Enzyme kinetics parameter estimation with Hessian-based optimizers | $\boldsymbol{\theta}_{t+1} = \boldsymbol{\theta}_t - \eta_t \mathbf{H}_t^{-1} \nabla \mathcal{L}(\boldsymbol{\theta}_t)$ |
| **8.4 - Stochastic Gradient Descent** | [SGD, Scheduling, and Adam](../notebooks/probabilistic-ml/8-optimization/8-4-1-stochastic_gradient_descent.ipynb) | Predicting drug sensitivity from gene expression with adaptive optimizers | $\boldsymbol{\theta}_{t+1} = \boldsymbol{\theta}_t - \eta_t \mathbf{M}_t^{-1} \nabla \mathcal{L}(\boldsymbol{\theta}_t, z_t)$ |

---

## 9 - Linear Discriminant Analysis

| | | | |
|---|---|---|---|
| **9.2 - Gaussian Discriminant Analysis** | [Gaussian Discriminant Analysis](../notebooks/probabilistic-ml/9-linear-discriminant-analysis/9-2-gaussian_discriminant_analysis.ipynb) | NSCLC cancer subtype classification from blood protein biomarkers | $p(y=c \mid \mathbf{x}) \propto \pi_c \mathcal{N}(\mathbf{x} \mid \boldsymbol{\mu}_c, \boldsymbol{\Sigma}_c)$ |
| **9.3 - Naive Bayes Classifiers** | [Naive Bayes Classifiers](../notebooks/probabilistic-ml/9-linear-discriminant-analysis/9-3-naive_bayes_classifiers.ipynb) | Antimicrobial compound screening from molecular fingerprints | $p(\mathbf{x} \mid y=c) = \prod_d p(x_d \mid y=c, \theta_{dc})$ |

---

## 10 - Logistic Regression

| | | | |
|---|---|---|---|
| **10.2 - Binary Logistic Regression** | [Binary Logistic Regression](../notebooks/probabilistic-ml/10-logistic-regression/10-2-binary_logistic_regression.ipynb) | Predicting tumor drug response from gene expression biomarkers | $p(y \mid \mathbf{x}) = \sigma(\mathbf{w}^\top \mathbf{x} + b)$ |
| **10.3 - Multinomial Logistic Regression** | [Multinomial Logistic Regression](../notebooks/probabilistic-ml/10-logistic-regression/10-3-multinomial_logistic_regression.ipynb) | Classifying NSCLC tumor subtypes from gene expression biomarkers | $p(y=c \mid \mathbf{x}) = \text{softmax}(W\mathbf{x})_c$ |

---

## 11 - Linear Regression

| | | | |
|---|---|---|---|
| **11.2 - Least Squares** | [Least Squares Linear Regression](../notebooks/probabilistic-ml/11-linear-regression/11-2-1-least_squares_linear_regression.ipynb) | Predicting protein abundance from mRNA expression in whole cell modeling | $\hat{\mathbf{w}} = (\mathbf{X}^\top\mathbf{X})^{-1}\mathbf{X}^\top\mathbf{y}$ |
| **11.3 - Ridge Regression** | [Ridge Regression](../notebooks/probabilistic-ml/11-linear-regression/11-3-1-ridge_regression.ipynb) | Predicting drug sensitivity from high-dimensional gene expression profiles | $\hat{\mathbf{w}} = (\mathbf{X}^\top\mathbf{X} + \lambda\mathbf{I})^{-1}\mathbf{X}^\top\mathbf{y}$ |
| **11.4 - Lasso Regression** | [Lasso Regression](../notebooks/probabilistic-ml/11-linear-regression/11-4-1-lasso_regression.ipynb) | Identifying antibiotic resistance biomarkers from bacterial gene expression | $\hat{\mathbf{w}} = \arg\min \|\mathbf{X}\mathbf{w}-\mathbf{y}\|^2 + \lambda\|\mathbf{w}\|_1$ |
| **11.7 - Bayesian Linear Regression** | [Bayesian Linear Regression](../notebooks/probabilistic-ml/11-linear-regression/11-7-1-bayesian_linear_regression.ipynb) | Predicting protein abundance from transcriptomics with full posterior uncertainty | $p(\mathbf{w} \mid \mathcal{D}) = \mathcal{N}(\hat{\mathbf{w}}, \hat{\boldsymbol{\Sigma}})$ |

---

## 13 - Neural Networks for Tabular Data

| | | | |
|---|---|---|---|
| **13.1 - Backpropagation** | [Backpropagation for an MLP](../notebooks/probabilistic-ml/13-neural-network-for-tabular-data/13-1-1-backpropagation_mlp.ipynb) | Classifying bacterial antibiotic resistance from genomic features | $\boldsymbol{\delta}_2 = (U^\top \boldsymbol{\delta}_1) \odot H(\mathbf{z})$ |

---

## 16 - Exemplar-based Methods

| | | | |
|---|---|---|---|
| **16.2 - Learning Distance Metrics** | [Learning Distance Metrics](../notebooks/probabilistic-ml/16-exemplar-based-methods/16-2-1-learning_distance_metrics.ipynb) | Drug compound similarity from molecular descriptors using LMNN, NCA, and deep metric learning | $d_M(\mathbf{x}, \mathbf{x}') = \sqrt{(\mathbf{x} - \mathbf{x}')^\top M (\mathbf{x} - \mathbf{x}')}$ |
| **16.3 - Kernel Density Estimation** | [Kernel Density Estimation](../notebooks/probabilistic-ml/16-exemplar-based-methods/16-3-1-kernel_density_estimation.ipynb) | Non-parametric profiling of single-cell flow cytometry, T-cell classification, and dose-response regression | $p(x \mid \mathcal{D}) = \frac{1}{N}\sum_n K_h(x - x_n)$ |

---

## 17 - Kernel Methods

| | | | |
|---|---|---|---|
| **17.1 - Mercer Kernels** | [Mercer Kernels](../notebooks/probabilistic-ml/17-kernel-methods/17-1-1-mercer_kernels.ipynb) | Cell phenotype similarity from gene expression using RBF, Matern, ARD, and kernel combination | $\kappa(\mathbf{x}, \mathbf{x}') = \exp\!\left(-\frac{\|\mathbf{x} - \mathbf{x}'\|^2}{2\ell^2}\right)$ |
| **17.2 - Gaussian Processes** | [Gaussian Processes](../notebooks/probabilistic-ml/17-kernel-methods/17-2-1-gaussian_processes.ipynb) | Predicting enzyme activity across temperature conditions with GP prior, posterior, and marginal likelihood | $p(\mathbf{f}_* \mid \mathcal{D}) = \mathcal{N}(\boldsymbol{\mu}_*, \mathbf{K}_{*,*} - \mathbf{K}_{X,*}^\top \mathbf{K}_\sigma^{-1} \mathbf{K}_{X,*})$ |
| **17.3 - Support Vector Machines** | [Support Vector Machines](../notebooks/probabilistic-ml/17-kernel-methods/17-3-1-support_vector_machines.ipynb) | Classifying bacterial cells as stressed vs. normal with hard/soft margin, kernel trick, and SVR | $f(\mathbf{x}) = \sum_{n \in \mathcal{S}} \alpha_n \tilde{y}_n \kappa(\mathbf{x}_n, \mathbf{x}) + \hat{w}_0$ |
| | [Kernel Ridge Regression](../notebooks/probabilistic-ml/17-kernel-methods/17-3-9-kernel_ridge_regression.ipynb) | Predicting enzyme activity from substrate concentration using the kernel trick | $f(\mathbf{x}) = \mathbf{k}^\top(\mathbf{K} + \lambda \mathbf{I})^{-1}\mathbf{y}$ |

---

## 18 - Trees, Forests, Bagging, and Boosting

| | | | |
|---|---|---|---|
| **18.1 - Tree Ensembles for Biotech** | [Random Forests and Gradient Boosting](../notebooks/probabilistic-ml/18-tree-forest-bagging-boosting/18-1-1-tree_ensembles_biotech.ipynb) | Predicting cancer cell line drug sensitivity from multi-omics (expression + mutations + tissue) with a practical tour of RF, XGBoost-style gradient boosting, feature importance, and partial dependence | $f_m(\mathbf{x}) = f_{m-1}(\mathbf{x}) + \nu F_m(\mathbf{x}; \boldsymbol{\theta}_m)$ |

---

## 20 - Dimensionality Reduction

| | | | |
|---|---|---|---|
| **20.1 - Principal Components Analysis** | [Principal Components Analysis (PCA)](../notebooks/probabilistic-ml/20-dimensionality-reduction/20-1-pca.ipynb) | Discovering latent cell states (growth, stress, quiescence) from single-cell gene expression with reconstruction-vs-variance derivation, eigendecomposition vs SVD, standardisation, scree plots, and profile likelihood | $\hat{\boldsymbol{\Sigma}}\mathbf{w}_k = \lambda_k \mathbf{w}_k$ |
| **20.2 - Factor Analysis** | [Factor Analysis and Probabilistic PCA](../notebooks/probabilistic-ml/20-dimensionality-reduction/20-2-factor-analysis.ipynb) | Inferring transcription-factor activity from heteroscedastic gene expression with the FA generative model, closed-form PPCA, EM algorithm, posterior over latents, and rotational unidentifiability | $\mathbf{C} = \mathbf{W}\mathbf{W}^\top + \boldsymbol{\Psi}$ |
| | [Exponential Family Factor Analysis](../notebooks/probabilistic-ml/20-dimensionality-reduction/20-2-7-exponential_family_pca.ipynb) | Binary PCA on tumor mutation profiles and categorical PCA on SNP genotypes — exponential-family generalisation of FA via low-rank natural parameters, fit by coordinate-ascent variational EM | $p(\mathbf{x}\mid\mathbf{z}) = \prod_d \mathrm{Ber}(x_d\mid\sigma(\mathbf{w}_d^\top\mathbf{z}))$ |
| **20.3 - Autoencoders** | [Autoencoders](../notebooks/probabilistic-ml/20-dimensionality-reduction/20-3-autoencoders.ipynb) | Compact representations of single-cell gene expression — linear AE recovers PCA, nonlinear AE unrolls a curved cell-cycle manifold, denoising AE imputes dropout, contractive AE squashes off-manifold perturbations, sparse AE with $\ell_1$ vs KL targets, VAE with reparameterization for sampling and latent interpolation | $\mathrm{ELBO} = \mathbb{E}_{q_\phi}[\log p_\theta(\mathbf{x}\mid\mathbf{z})] - D_{\mathrm{KL}}(q_\phi \,\|\, p)$ |
| | [Variational Autoencoder — Step by Step](../notebooks/probabilistic-ml/20-dimensionality-reduction/20-3-5-vae_step_by_step.ipynb) | Generating synthetic single-cells from a trained VAE — full ELBO derivation, closed-form Gaussian KL, the reparameterization trick visualised, PyTorch implementation, latent-space exploration, prior sampling, interpolation, and posterior collapse with $\beta$-VAE | $\mathbf{z} = \boldsymbol{\mu}_\phi(\mathbf{x}) + \boldsymbol{\sigma}_\phi(\mathbf{x})\odot\boldsymbol{\epsilon}$ |
| **20.4 - Manifold Learning** | [Manifold Learning](../notebooks/probabilistic-ml/20-dimensionality-reduction/20-4-manifold_learning.ipynb) | Recovering cell-differentiation trajectories from scRNA-seq with the manifold hypothesis, classical/metric/non-metric MDS and Sammon mapping, Isomap with geodesic distances on a kNN graph, Kernel PCA, MVU, LLE with barycentric coordinates, Laplacian eigenmaps and the graph Laplacian, t-SNE with perplexity sweeps, and UMAP — applied to the Swiss roll and a 64-d cell-cycle ring | $\mathcal{L}(\mathbf{Z}) = \sum_{(i,j)\in E} W_{ij} \|\mathbf{z}_i - \mathbf{z}_j\|^2 = 2\,\mathrm{tr}(\mathbf{Z}^\top \mathbf{L}\mathbf{Z})$ |
