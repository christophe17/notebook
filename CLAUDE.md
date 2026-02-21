# CLAUDE.md

## Project Overview

This is a project containing interactive notebooks that accompany the **Probabilistic Machine Learning** book. Each notebook provides real-world examples illustrating mathematical concepts from specific chapters.

## Structure

- **README.md** contains the summary with links to all notebooks
- Titles are organized on **two levels** (e.g., "3 - Multivariate Models" → "3.2 - Multivariate Gaussian")
- Each chapter has a **single 4-column table** (no headers):
  - **Column 1**: Sub-chapter label in bold (e.g., **3.2 - Multivariate Gaussian**), only on the first row of each group
  - **Column 2**: Mathematical concept name (as a link to the notebook)
  - **Column 3**: Real-world application description
  - **Column 4**: Key formula in LaTeX (using `$...$` syntax for universal rendering)

## Titles

- Keep titles **simple and direct** — use the concept name only
- Avoid filler words like "Understanding", "Explained", "Introduction to", etc.

## Naming Convention

Notebooks follow the pattern: `X-Y-Z-title.ipynb`

- **X-Y-Z** corresponds to the chapter/section numbers (e.g., `3-2-3` for Chapter 3.2.3)
- **title** is a short descriptive name using underscores (e.g., `mvn_marginals_conditionals`)

Example: `3-2-3-mvn_marginals_conditionals.ipynb` for a notebook about Chapter 3.2.3

## Notebook Guidelines

Each notebook should:
- Use a **real-world scenario** to illustrate the concept, preferably from the **biotech** field when possible
- Create **fake but realistic data** when needed
- Include **step-by-step explanations** of formulas from the chapter
- Provide **visualizations** to build intuition
- Be self-contained and runnable independently
