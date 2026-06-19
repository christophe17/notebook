# Primer for Step 1: Simulating scRNA-seq with Cell Type and Continuous State

This primer explains Step 1 of `21-3-4-semisupervised_vae.ipynb` slowly, from the modeling idea to each code block.

## 1. What Step 1 Is Trying to Create

The semi-supervised VAE in this notebook needs data with two kinds of structure:

1. A **discrete label** `y`: the cell type.
2. A **continuous latent state** `z_star`: a hidden biological state inside each cell type.

In the notebook, the discrete labels are:

```python
cell_types = ['T cell', 'B cell', 'Monocyte', 'NK cell']
```

The continuous state is two-dimensional:

```python
K_TRUE = 2
```

You can think of `y` as answering "what kind of cell is this?" and `z_star` as answering "what state is this cell in within that type?"

This matches the M2 semi-supervised VAE idea:

```text
x is generated from both y and z
```

where:

- `y` captures cell type.
- `z` captures remaining continuous variation.
- `x` is the observed gene-expression vector.

## 2. Dataset Size and Shape

The first constants define the synthetic dataset:

```python
N = 6000
D = 30
C = 4
K_TRUE = 2
```

Meaning:

- `N = 6000`: simulate 6000 cells.
- `D = 30`: each cell has 30 gene-expression features.
- `C = 4`: there are 4 cell types.
- `K_TRUE = 2`: the hidden continuous state has 2 dimensions.

So the final expression matrix `X_all` will have shape:

```text
6000 cells x 30 genes
```

## 3. Reproducible Randomness

The notebook uses:

```python
rng = np.random.default_rng(0)
```

This creates a random number generator with a fixed seed. The point is not biology; the point is reproducibility. Every time the notebook runs, it creates the same synthetic dataset.

## 4. Cell-Type-Specific Means: `mu_y`

This line creates one mean expression vector per cell type:

```python
mu_y = rng.normal(0.0, 0.45, size=(C, D)).astype(np.float32)
```

The shape is:

```text
mu_y.shape == (4, 30)
```

Interpretation:

- Each row corresponds to one cell type.
- Each column corresponds to one gene.
- `mu_y[k]` is the average expression pattern for cell type `k`.

So if a cell is a T cell, it starts near the T-cell mean vector. If it is a B cell, it starts near the B-cell mean vector, and so on.

This is the synthetic version of marker genes: different cell types tend to have different baseline expression profiles.

## 5. Continuous State Directions: `W_z`

The next line creates directions in gene-expression space that are controlled by the hidden continuous state:

```python
W_z = rng.normal(0.0, 0.9, size=(D, K_TRUE)).astype(np.float32)
```

The shape is:

```text
W_z.shape == (30, 2)
```

Interpretation:

- `z_star` lives in a 2-dimensional hidden space.
- `W_z` maps that 2-dimensional hidden state into the 30-dimensional gene-expression space.

Later, the notebook uses:

```python
z_star @ W_z.T
```

The shape calculation is:

```text
z_star:    (6000, 2)
W_z.T:     (2, 30)
result:    (6000, 30)
```

So every cell gets a 30-gene expression shift caused by its hidden continuous state.

This is important because cells of the same type are not identical. A T cell can vary by activation, cell-cycle phase, stress response, or other continuous biological processes.

## 6. Class Proportions: `pi_true`

The notebook makes the cell types mildly imbalanced:

```python
pi_true = np.array([0.30, 0.25, 0.25, 0.20])
```

These are the probabilities of sampling each class:

- T cell: 30%
- B cell: 25%
- Monocyte: 25%
- NK cell: 20%

Then labels are sampled:

```python
y_all = rng.choice(C, size=N, p=pi_true)
```

The result:

```text
y_all.shape == (6000,)
```

Each entry is an integer from `0` to `3`, identifying one cell's type.

## 7. Ground-Truth Continuous State: `z_star`

The hidden state is sampled independently for every cell:

```python
z_star = rng.normal(0.0, 1.0, size=(N, K_TRUE)).astype(np.float32)
```

The shape is:

```text
z_star.shape == (6000, 2)
```

Each cell has two hidden coordinates. These are not labels; they are continuous factors.

The model trained later will not see `z_star`. It is only used to generate the fake data. Later, the VAE will try to learn its own latent representation `z` from `x`.

## 8. The Actual Data-Generating Equation

This is the key line:

```python
X_all = mu_y[y_all] + z_star @ W_z.T + rng.normal(0.0, 0.55, size=(N, D)).astype(np.float32)
```

It implements:

```text
x_n = mu_y[n] + W_z z_n + noise
```

More precisely:

```text
x_n = mu_{y_n} + W_z z_star_n + eta_n
```

where:

- `mu_y[y_all]` gives each cell its cell-type baseline.
- `z_star @ W_z.T` adds continuous within-type variation.
- `rng.normal(...)` adds random noise.

The three terms have the same final shape:

```text
(6000, 30)
```

So `X_all` is the synthetic scRNA-seq expression matrix.

## 9. Why This Is a Good Toy Problem

The notebook deliberately makes the problem neither too easy nor too hard.

The cell-type means are only moderately separated:

```python
mu_y = rng.normal(0.0, 0.45, size=(C, D))
```

The continuous state effect is fairly strong:

```python
W_z = rng.normal(0.0, 0.9, size=(D, K_TRUE))
```

That means cells from the same type can be spread out, and cells from different types can partially overlap. This is useful for a semi-supervised VAE because unlabeled data can help reveal the global structure.

If the clusters were perfectly separated, a tiny supervised classifier would already solve the task. If the clusters completely overlapped, no model could recover useful labels. Step 1 creates a middle ground.

## 10. Standardizing Each Gene

After generating `X_all`, the notebook standardizes each gene:

```python
X_mean = X_all.mean(0)
X_std = X_all.std(0)
X_all = (X_all - X_mean) / X_std
```

This makes each gene approximately:

```text
mean 0, standard deviation 1
```

This is common preprocessing for expression data and helpful for neural networks. Without standardization, genes with larger numerical scale could dominate the loss.

## 11. Creating Labeled, Unlabeled, and Test Splits

The notebook imitates a realistic single-cell setting:

```python
N_LABELED_PER_CLASS = 50
N_TEST = 1000
```

There are:

- `50 * 4 = 200` labeled cells.
- `1000` test cells.
- the rest are unlabeled training cells.

The labeled set is stratified:

```python
for k in range(C):
    members = np.where(y_all == k)[0]
    rng2.shuffle(members)
    labeled_idx.extend(members[:N_LABELED_PER_CLASS].tolist())
```

Stratified means each cell type contributes the same number of labeled examples.

That matters because if labels were chosen completely at random, a rare class might receive too few labels. Here, every class gets 50 labeled cells, so the model at least gets some direct supervision for each class.

## 12. Converting NumPy Arrays to PyTorch Tensors

The notebook then creates tensors:

```python
X_lab = torch.tensor(X_all[labeled_idx])
y_lab = torch.tensor(y_all[labeled_idx], dtype=torch.long)

X_unl = torch.tensor(X_all[unlabeled_idx])

X_tst = torch.tensor(X_all[test_idx])
y_tst = torch.tensor(y_all[test_idx], dtype=torch.long)
```

These are the datasets used later:

- `X_lab`, `y_lab`: labeled training cells.
- `X_unl`: unlabeled training cells.
- `X_tst`, `y_tst`: held-out test cells.

Notice that `X_unl` has no corresponding `y_unl`. The model will still use these cells through the unlabeled M2 objective.

## 13. PCA Sanity Check

Finally, Step 1 uses PCA:

```python
pca = PCA(n_components=2).fit_transform(X_all)
```

PCA compresses the 30-dimensional expression vectors into 2 dimensions for plotting.

The plot is not used for training. It is just a sanity check:

- Are there visible cell-type regions?
- Are the regions partially overlapping?
- Is there spread within each cell type?

That is exactly what we want. The synthetic data should show both discrete cluster structure and continuous variation inside clusters.

## 14. The Big Picture

Step 1 creates data from this recipe:

```text
sample cell type y
sample continuous state z_star
combine cell-type mean and continuous-state shift
add noise
standardize genes
split into labeled, unlabeled, and test sets
plot with PCA
```

This prepares the notebook for the M2 model because the data really does contain the two ingredients M2 is designed to separate:

- `y`: a discrete cell-type variable.
- `z`: a continuous within-type state variable.

The later model will only observe `x`, plus labels for a small subset of cells. Its job is to use both labeled and unlabeled cells to learn a classifier and a useful latent representation.
