# Probabilistic Machine Learning

Interactive notebooks accompanying the **Probabilistic Machine Learning** book.

---

## 3 - Multivariate Models

| | | | |
|---|---|---|---|
| **3.2 - Multivariate Gaussian** | [Marginals and Conditionals (2D)](notebooks/3-multivariate-models/3-2-3-mvn_marginals_conditionals.ipynb) | Predicting EGFR protein levels from mRNA gene expression | $p(x_1 \mid x_2)$ |
| | [Marginals and Conditionals (5D)](notebooks/3-multivariate-models/3-2-3-mvn_marginals_conditionals_5d.ipynb) | Comprehensive real estate valuation with 5 correlated features | $p(\mathbf{x}_1 \mid \mathbf{x}_2)$ |
| | [Missing Value Imputation](notebooks/3-multivariate-models/3-2-5-mvn_missing_value_imputation.ipynb) | Patient health records with missing lab results | $p(\mathbf{x}_h \mid \mathbf{x}_v)$ |
| **3.3 - Linear Gaussian System** | [Bayes Rule for Gaussians](notebooks/3-multivariate-models/3-3-1-linear_gaussian_blood_pressure.ipynb) | Blood pressure estimation with multiple clinical devices | $p(\mathbf{z} \mid \mathbf{y}) \propto p(\mathbf{y} \mid \mathbf{z})\,p(\mathbf{z})$ |
| | [Bayes Rule with Non-Trivial W](notebooks/3-multivariate-models/3-3-1-linear_gaussian_derived_health_metrics.ipynb) | Inferring physiological state from derived health metrics | $\mathbf{y} = W\mathbf{z} + \boldsymbol{\epsilon}$ |
| | [Inferring an Unknown Scalar](notebooks/3-multivariate-models/3-3-3-bayesian_temperature_estimation.ipynb) | Bayesian temperature estimation in industrial monitoring | $p(\mu \mid \mathbf{y})$ |
| | [Inferring an Unknown Vector](notebooks/3-multivariate-models/3-3-4-linear_gaussian_gps_localization.ipynb) | GPS localization of vehicle position from noisy measurements | $p(\mathbf{z} \mid \mathbf{y})$ |
| | [Sensor Fusion](notebooks/3-multivariate-models/3-3-5-sensor_fusion_autonomous_vehicle.ipynb) | Autonomous vehicle localization combining GPS, LiDAR, and camera | $p(\mathbf{z} \mid \mathbf{y}_1, \mathbf{y}_2, \mathbf{y}_3)$ |
| **3.5 - Mixture Models** | [Gaussian Mixture Models](notebooks/3-multivariate-models/3-5-1-gmm_customer_segmentation.ipynb) | Customer segmentation for retail analytics using GMM | $p(\mathbf{x}) = \sum_k \pi_k \mathcal{N}(\mathbf{x} \mid \boldsymbol{\mu}_k, \Sigma_k)$ |

---

## 7 - Linear Algebra

| | | | |
|---|---|---|---|
| **7.0 - Foundations** | [Scalar, Vector, and Matrix Products](notebooks/7-linear-algebra/7-0-1-scalar_vector_matrix_products.ipynb) | Basic multiplication shapes and the dimension compatibility rule | $c = \mathbf{a}^T\mathbf{b},\ \mathbf{c} = A\mathbf{b},\ C = AB$ |
| | [Inner Product (Dot Product)](notebooks/7-linear-algebra/7-0-2-inner_product.ipynb) | Measuring alignment and similarity between vectors | $\mathbf{a}^T\mathbf{b} = \sum_i a_i b_i$ |
| | [Outer Product](notebooks/7-linear-algebra/7-0-3-outer_product.ipynb) | Creating matrices from vectors and building covariance | $\mathbf{a}\mathbf{b}^T$ |
| | [Matrix-Vector Multiplication](notebooks/7-linear-algebra/7-0-4-matrix_vector_multiplication.ipynb) | Geometric transformations: rotation, scaling, shearing | $\mathbf{y} = A\mathbf{x}$ |
| | [Matrix-Matrix Multiplication](notebooks/7-linear-algebra/7-0-5-matrix_matrix_multiplication.ipynb) | Composing transformations and the associativity property | $(AB)C = A(BC)$ |
| | [Quadratic Forms](notebooks/7-linear-algebra/7-0-6-quadratic_forms.ipynb) | Weighted distance and Mahalanobis | $\mathbf{x}^T W \mathbf{x}$ |
| | [The A B A.T Pattern](notebooks/7-linear-algebra/7-0-7-aba_transpose_pattern.ipynb) | Transforming covariance through linear maps | $\Sigma_y = A\Sigma_x A^T$ |
| | [Schur Complement](notebooks/7-linear-algebra/7-0-8-schur_complement.ipynb) | Block matrix operations and Gaussian conditioning | $M/D = A - BD^{-1}C$ |
| **7.3 - Matrix Inversion** | [Factor Model Covariance](notebooks/7-linear-algebra/7-3-factor_model_covariance_explained.ipynb) | Building gene expression covariance from transcription factor pathways | $\Sigma = WW^T + \Psi$ |
| | [Low-Rank Covariance Update](notebooks/7-linear-algebra/7-3-low_rank_covariance_update_explained.ipynb) | Why adding $XX^T$ to a covariance matrix models new pathway exposures | $\Sigma' = \Sigma + XX^T$ |
| | [Sherman-Morrison Formula](notebooks/7-linear-algebra/7-3-sherman_morrison_single_tf.ipynb) | Rank-1 precision updates when discovering a single transcription factor | $(A + \mathbf{u}\mathbf{v}^T)^{-1}$ |
| | [Matrix Inversion Lemma (Woodbury)](notebooks/7-linear-algebra/7-3-matrix_inversion_lemma_grn.ipynb) | Efficient precision matrix updates for gene regulatory network inference | $(A + UCV)^{-1}$ |
| **7.4 - Eigenvalue Decomposition** | [Geometry of Quadratic Forms](notebooks/7-linear-algebra/7-4-4-geometry_quadratic_forms.ipynb) | Ellipsoidal level sets applied to protein binding affinity in drug discovery | $\mathbf{x}^T A\mathbf{x} = c$ |
| **7.5 - Singular Value Decomposition** | [SVD](notebooks/7-linear-algebra/7-5-svd_gene_expression.ipynb) | Gene expression profiling: discovering latent biological programs with SVD | $A = USV^T$ |
| **7.6 - Matrix Decompositions** | [Cholesky Sampling from MVN](notebooks/7-linear-algebra/7-6-3-1-cholesky_mvn_sampling.ipynb) | Clinical trial simulation with correlated patient biomarkers | $\Sigma = LL^T$ |


---

## 8 - Optimization

| | | | |
|---|---|---|---|
| **8.1 - The EM Algorithm** | [Expectation-Maximization (EM)](notebooks/8-optimization/8-1-1-em_algorithm.ipynb) | Medical diagnosis with latent disease types using Gaussian mixtures | $\mathcal{Q}(\boldsymbol{\theta}, \boldsymbol{\theta}^{\text{old}})$ |
