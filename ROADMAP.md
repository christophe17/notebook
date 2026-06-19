# TechBio ML — Founder-Track Learning Roadmap

**Primary goal:** acquire enough biotech to **co-found (or join very early) a
capital-light AI-for-bio platform** — the path with real upside for a strong
ML/MLOps engineer. Longevity/anti-aging is the **long-term mission, not company
#1**: enter it later through the platform/tooling door, not via a capital-hungry
therapeutics raise.
**Secondary (optionality):** the same learning makes you hireable as a bio-ML /
MLOps engineer — a free safety net while the founder path matures. ~90% of the
preparation overlaps.
Delivery: hands-on Python + Jupyter notebooks on real public datasets.

> *Founder context (verified deep-research, 2026): TechBio seed/Series-A capital
> is concentrating in AI design platforms (protein/molecule) and biological
> foundation models, with software-margin monetization via pharma licensing
> (Chai/Lilly, Boltz/Pfizer, Noetik/GSK). The defensible moat is **proprietary,
> biology-native data generation**, not model architecture (Bessemer thesis). Top
> funds (Dimension, a16z bio+health, Bessemer, Sofinnova) court ML-native founders
> but treat a pure-software team as a flag: pair ML depth with wet-lab/domain
> depth. This roadmap is the **technical half** of that preparation; the
> wet-lab-cofounder, commercial/BD, and fundraising half are handled outside this
> file by design (see "What this roadmap deliberately does NOT cover").*

**Status & part counts:** each topic heading below carries a **founder-path
priority tag** (🔴 / 🟡 / 🟢 — see the prioritization section). Per-course **build state**
(✅ built · 🚧 in progress · 📋 planned) and the actual part count now live in
each course's own `README.md` under `courses/<NN-slug>/` — that README is the
source of truth for what's on disk vs planned.

**Course sizing.** Each course is sized to its topic, not to a fixed part
count — typical range **~6–12 parts**. Don't pad to hit 12, don't cram to stay
under it. When a topic has a clean cleavage, prefer splitting into `Na`/`Nb`
sub-courses (as Topic 4 did) over stretching a single course thin.

This file is the single source of truth for **what to learn, in what order, and
at what founder-path priority**; each course's `README.md` under `courses/<NN-slug>/`
is the source of truth for that course's build state.

---

## Founder-path prioritization (with job optionality)

The topic sections below are ordered by **learning dependency** (biology
foundations → ML methods → aging edges → engineering). That order is correct for
*understanding*. It is **not** the order to optimize for the founder path.

**Goal of this layer:** get *dangerous* in one capital-light AI-for-bio vertical
fast — deep enough to lead the ML, recognize a real data moat, and evaluate a
wet-lab co-founder — **without finishing all 13 topics first**. Biology is the
literacy layer; ML/MLOps is your engine; vertical depth is what the company gets
built on. The same stack also keeps you hireable (early-employee #1–20), so
nothing here is wasted if you join before you found.

### Read in phases, not in number order

- **Phase 0 — Orient (cheap, ~2–4 weeks): choose a vertical with eyes open.**
  No new notebook. Survey what each AI-for-bio vertical actually does, the data
  moat it rests on, and how it monetizes (license vs. tool vs. therapeutic).
  Output: a one-page decision doc naming your 1–2 candidate verticals. This step
  exists to dissolve the "everything is fuzzy" problem *before* you sink months
  into the wrong depth.
- **Phase 1 — Common core (every vertical needs it):** Topic **1** (gene
  regulation, skim) · Topic **2** (single-cell) · Topic **13** (MLOps — your
  existing strength, re-pointed at bio FMs). Just-enough biology to read papers +
  your engineering spine.
- **Phase 2 — Vertical depth — ✅ CHOSEN 2026-06-03: Track B** (A & C retained for
  future optionality, not built now):
  - **Track A — Protein / antibody / molecule design** → Topics **7 + 9**.
    Hottest founder vertical, rewards the ML edge most, software-margin licensing
    proven (Chai/Lilly, Boltz/Pfizer). Territory: Chai, Boltz, Cradle, Generate.
  - **Track B — Biological foundation models / virtual cell** → Topics **8 + 6**
    (+ **5** conversant-only). **← ACTIVE.** Entered via the **eval / perturbation-
    benchmark layer** (see `docs/strategy/track-b-mvp-spec.md`), *not* by training FMs to license
    weights — the capital-light, MLOps-native door. Verified 2026: pure-play
    virtual-cell licensing barely exists yet (one deal, Noetik/GSK), and scFMs don't
    reliably beat linear baselines — that gap *is* the whitespace the MVP exploits.
  - **Track C — Multi-omics / clinical-data / diagnostics platform** → Topic **2
    deep** + clinical/longitudinal data. Closest to classic data-platform ML; the
    moat is proprietary outcome-linked data.
- **Phase 3 — The data-moat engine (technical whitespace):** active learning,
  experimental design, Bayesian optimization, closed-loop *design → assay →
  retrain*. Promoted from a deferred companion to a first-class skill, because the
  verified 2026 thesis is that *proprietary data generation*, not model
  architecture, is the defensible moat. See the Math & Methods companion below.
- **Phase 4 — Aging mission depth (deferred, optional):** Topics **3, 4b, 10, 11,
  12**. Where longevity lives — open it once you have a platform, credibility, and
  capital, or when a specific company/interview demands it.

### Three tiers by founder ROI

| Tier | Topics | Why | Posture |
|---|---|---|---|
| **🔴 Core founder engine** | **8**, **6** (Track B — ✅ active) · **13** (MLOps spine) · **7**, **9** (Track A — parked) | The verticals attracting seed/Series-A capital *and* where an ML-native founder leads rather than supports. MLOps is the substrate under all of them. | Track B active: go deep **08 → 06**, entered via the eval / perturbation-benchmark layer (`docs/strategy/track-b-mvp-spec.md`). Keep MLOps always-on; ship a public, runnable artifact. |
| **🟡 Common core / credibility floor** | **1** (gene regulation), **2** (single-cell genomics), **5** (DNA/RNA LMs — conversant, off MVP path), **4a** (epigenetic clocks) | Lingua franca to read papers, talk to scientists, and evaluate a bench co-founder. 5 stays conversant-level (sequence-to-function is a different modality from the perturbation MVP); 4a is a cheap aging differentiator, not the spine. | Enough to be conversant. Don't over-polish — diminishing returns. |
| **🟢 Mission depth — deferred** | **3** (hallmarks), **4b** (frontier clocks), **10** (reprogramming), **11** (senescence), **12** (longevity GWAS) | Aging-specific and mostly capital-hungry (therapeutics). The mission, not company #1. (Topic 8 moved to the active engine — it's Track B's virtual-cell frontier.) | Open on demand only. Do not let these block choosing a vertical or building. |

### What to do next, in order

1. **Run Phase 0 and write the one-page decision doc.** Highest-leverage move on
   the whole roadmap right now: you cannot prioritize depth until you've named the
   vertical. Cheap, fast, dissolves the fuzziness.
2. **Stand up the common core (Phase 1).** Skim Topics 1–2 for literacy; treat
   Topic 13 (MLOps) as the always-on spine — it's your pre-existing edge and the
   exact gap most TechBio orgs have.
3. **Go deep in ONE Phase-2 track** and ship a *public, runnable* artifact from it
   (deployed model / honest benchmark / OSS PR). A shipped thing signals "builds";
   a notebook signals "studied." The first is worth ~5×, for both founding and
   getting hired early.
4. **Add the Phase-3 data-moat engine** (active learning / experimental design) as
   soon as you have a vertical — it's what turns a wet lab into a compounding data
   advantage instead of a model wrapper.

### What this roadmap deliberately does NOT cover

By design (technical-only scope), three **founder-critical** tracks live *outside*
this file and must be developed in parallel — do not mistake a finished technical
roadmap for founder-readiness:

1. **Wet-lab / assay literacy + co-founder search** — enough bench understanding
   to grasp the data moat and to recruit/evaluate a domain co-founder (top funds
   flag pure-software teams).
2. **Commercial layer** — TechBio business models (license vs. tool vs.
   therapeutic), pharma BD/licensing mechanics, GTM.
3. **Fundraising** — investor map (Dimension, a16z bio+health, Bessemer,
   Sofinnova, Healthspan Capital) and the raise itself.

> **Anti-pattern to avoid:** treating this as a 13-topic completion checklist.
> The founder move is Phase 0 → common core → ONE vertical deep → a shipped
> artifact, with the co-founder search running in parallel. The marginal
> mission-depth notebook (Tier 🟢) is worth far less than getting dangerous in one
> vertical.

---

## Foundations (biology you can't skip)

### 1. Gene regulation  · **🟡 common core**
TFs, enhancers, chromatin, epigenetics, 3D genome, ncRNAs.
**Why for aging:** epigenetic clocks and partial reprogramming both operate here.
**Tools:** `biopython`, `pyranges`, `bioframe`, `cooler`, `cooltools`, `gimmemotifs`,
`logomaker`, `dna_features_viewer`, `pyGenomeTracks`.

### 2. Single-cell genomics  · **🟡 common core**
scRNA-seq, scATAC-seq, CITE-seq, spatial, multi-omics integration.
**Why for aging:** aging is fundamentally cell-state heterogeneity and loss of identity.
**Tools:** `scanpy`, `anndata`, `muon`, `scvi-tools`, `squidpy`, `cellrank`.

### 3. Hallmarks of aging  · **🟢 mission depth — deferred**
Genomic instability, telomere attrition, epigenetic alterations, loss of proteostasis,
disabled macroautophagy, deregulated nutrient sensing, mitochondrial dysfunction,
cellular senescence, stem-cell exhaustion, altered intercellular communication,
chronic inflammation, dysbiosis. *(López-Otín 2023 framework.)*
**Why for aging:** the conceptual map linking biology to measurable assays.

### 4. Aging clocks  · **🟡 common core (4a)** · **🟢 mission depth (4b)**
**Why for aging:** *the* benchmark for "did my intervention work."

Split into two courses to keep the methylation core focused and let the
multi-modal / frontier work breathe (the 12-part-per-topic frame was
forcing redundancy with Course 3 and DL-cargo-cult padding):

- **4a. Epigenetic clocks**  · **🟡 common core**
  Horvath, Hannum, PhenoAge, GrimAge, DunedinPACE, tissue specificity,
  mortality validation, causal clocks (Ying et al. DamAge / CausAge),
  intervention trials.
  **Tools:** `pyaging`, `biolearn`, scikit-learn ElasticNet, `lifelines`.
- **4b. Multi-modal & frontier clocks**  · **🟢 mission depth**
  Transcriptomic (Peters / Pasta), proteomic + organ-specific
  (Lehallier / Oh / Argentieri), deep-learning clocks (AltumAge family),
  single-cell pseudo-bulk vs per-cell-type clocks, multi-omic capstone.
  **Tools:** `pyaging`, `biolearn`, `pytorch`, `scvi-tools`, `shap`.

---

## ML for biology (your edge)

### 5. DNA / RNA language models  · **🟡 Track B — conversant, off the MVP critical path**
*MVP status (2026-06-05): demoted.* Sequence-to-function is a **different modality**
from the single-cell / perturbation MVP — none of its models/data/metrics touch this
topic. Keep at *conversant* level (Course 01 Part XI loads Enformer on one locus —
enough to read the papers); the depth pass below is **optional**, deferred until a
sequence-level data-generation angle makes it concrete.

Predict expression, accessibility, splicing, variant effects from sequence.
**Models:** Enformer, Borzoi, AlphaGenome, Evo 2, NTv3 (Nucleotide Transformer),
DNABERT-2, Caduceus, ChromBPNet, Pangolin, SpliceAI.
**Tools:** `grelu` (umbrella), `transformers`, `enformer-pytorch`, `alphagenome`,
`evo2`, model-specific repos.
*Relationship to Foundations:* course 01 Part XI **introduces** sequence-to-function
models (load Enformer, run on one locus, interpret).

This topic is the **depth
pass** — fine-tuning, Enformer vs Borzoi vs AlphaGenome comparisons, variant
effect prediction at scale, attention analysis, training a small model from
scratch.

### 6. Single-cell foundation models  · **🔴 core founder engine** (Track B — *baselines for the MVP*)
*MVP status (2026-06-05): study these as the **baselines to profile** (zero-shot
embeddings + failure modes), not as build targets — you benchmark them, you don't
train your own.*
Cell-type annotation, perturbation prediction, in-silico knockout, batch integration.
**Models:** Geneformer V2, scGPT, scFoundation, UCE, TranscriptFormer, CellFM,
scPRINT, scBERT (superseded), scimilarity; State (Arc Institute) on Tahoe-100M
for the perturbation frontier.
**Tools:** Hugging Face, model-specific repos, `scvi-tools`, CZI Virtual Cells Platform.
*Relationship to Foundations:* course 02 Part XI **introduces** scFMs (zero-shot
embeddings, cell-type annotation with Geneformer).

This topic is the **depth
pass** — zero-shot vs fine-tuning trade-offs, perturbation prediction, model-family
comparisons, batch-effect handling at scale, failure modes.

### 7. Protein structure & language models  · **🔴 core founder engine** (Track A)
Target ID, protein design, engineered TFs, antibody design.
**Models:** AlphaFold 3, OpenFold3, Boltz-2, Chai-1 / Chai-2, ESM-2 / ESM C /
ESM-3, RFdiffusion3, LigandMPNN, BoltzGen, Germinal, IgGM.
**Tools:** `alphafold3`, `openfold3`, `boltz`, `esm`, `rfdiffusion3`,
`ligandmpnn`, `boltzgen`, `colabfold` (MSA front-end), `biotite`, `py3Dmol`.

### 8. Perturbation modeling  · **🔴 Track B — the MVP itself** · virtual-cell / perturbation frontier
*MVP status (2026-06-05): this **is** the first artifact — the models/data/benchmarks
below map 1:1 onto `docs/strategy/track-b-mvp-spec.md`. Centre of gravity for Track B; reach it fast.*
The causal layer: *what happens if we knock out X*. Critical for aging-target ID.
**Data:** Perturb-seq (Norman 2019, Replogle 2022, X-Atlas/Orion 2025,
Multiome Perturb-seq, Perturb-Multimodal), chemical Perturb-seq (Tahoe-100M).
**Models:** PCA-linear baseline (Ahlmann-Eltze 2025), GEARS, CPA, scGen,
Biolord, scLAMBDA, scGPT-Perturb, Geneformer-Perturb, **State** (Arc Institute).
**Benchmarks:** PerturBench (ICLR 2025), PertEval-scFM (ICML 2025).

### 9. Generative models for small molecules  · **🔴 core founder engine** (Track A)
Senolytics, geroprotectors, mTOR/AMPK modulators, NAD+ boosters.
**Models:** equivariant GNNs (MACE, NequIP, e3nn), diffusion-docking
(DiffDock-L, Boltz-2), structure-based generation (DiffSBDD-M, TargetDiff,
Pocket2Mol), modern joint diffusion (DiffGui, BInD), property-guided
(DrugDiff, G2D-Diff), universal binder (BoltzGen), Smer-Barreto 2023 +
SenolyticSynergy 2025 senolytic case study.
**Tools:** `rdkit`, `chemprop`, `deepchem`, `pytorch-geometric`, `boltz`,
`diffdock-l`, `diffsbdd`, `mace-torch`, `nequip`, `boltzgen`.

---

## Aging-specific edges

### 10. Partial reprogramming  · **🟢 mission depth — deferred**
Yamanaka factors (OSKM), in-vivo rejuvenation, transient reprogramming.
**Why for aging:** the most striking rejuvenation signal in the literature
(Altos Labs, Retro Biosciences, NewLimit). Few public benchmarks → research opportunity.

### 11. Cellular senescence  · **🟢 mission depth — deferred** (build on demand)
p16/p21/SASP markers, senolytic screens, senescence cell-state classifiers.
**Tools:** `scanpy` + custom senescence signatures (SenMayo, CellAge).

### 12. Longevity GWAS & multi-omics  · **🟢 mission depth — deferred**
Genotype → phenotype → lifespan. Centenarian and exceptional-longevity studies.
**Datasets:** UK Biobank, FinnGen, eMERGE, LonGenity, NECS.
**Tools:** `hail`, `plink2-py`, `pyGWAS`, Mendelian randomization stacks.

---

## Engineering for biology ML (your strength)

### 13. MLOps for biology foundation models  · **🔴 core founder engine — the always-on spine**
The engineering substrate under every other course. Distributed training of
genomic and single-cell FMs (FSDP / DeepSpeed / Accelerate), fine-tuning at
scale (LoRA / adapters / full FT), eval harnesses biologists trust (PerturBench-
style, leave-donor-out, multiple-comparison-safe), population-scale inference
(variant scoring under quantization), experiment tracking + model registry
(W&B / MLflow / DVC), GPU cluster economics (SLURM vs Kubernetes, spot vs
on-demand), and an end-to-end capstone on an aging cohort.
**Why for aging:** the SOTA work the user wants to do — tissue-adapted Enformer
on aging cohorts, UK-Biobank-scale variant scoring, retraining scFMs on
longitudinal atlases — is MLOps work. Courses 1–12 give the biology vocabulary
and ML-method toolkit; Course 13 is how you actually ship.
**Tools:** `pytorch` FSDP, `deepspeed`, `accelerate`, `lightning`, `peft`,
`bitsandbytes`, `vllm`, `triton-inference-server`, `wandb`, `mlflow`, `dvc`,
`hydra`, `skypilot`, `ray`.

**Delivery format — hybrid notebook + `scripts/`.** This is the *only*
course on the roadmap that breaks the notebook-only invariant. Honest
answer to "can all of this be learned in notebooks?": **no, not all of
it.** Roughly 60–70% fits Jupyter cleanly; the rest doesn't, and
pretending otherwise would make this course the weakest in the roadmap.
The per-part split:

- **Fits in a notebook (notebook-only):**
  - Part I (lifecycle map) — pure analysis
  - Part II (data pipelines) — loaders are notebook-natural; benchmark on a subset
  - Part V (fine-tuning) — LoRA / adapter / full-FT runs are single-process, runnable in-cell
  - Part VI (eval harness) — harness code develops in a notebook, gets exported as a library
  - Part VIII (tracking + registry) — W&B / MLflow API calls run fine in notebooks; the state lives remotely
  - Part IX cost calculator — parametric Python
- **Awkward in a notebook (the notebook becomes a *runbook + reader*, not a runner):**
  - Part III (FSDP multi-node Borzoi) — needs `torchrun` / `accelerate launch` across processes; Jupyter is single-kernel
  - Part IV (distributed scGPT) — same
  - Part VII (Triton serving) — serving is a long-running daemon, not a cell
- **Doesn't fit at all:**
  - Part IX cluster bits (SLURM sbatch, Kubernetes YAML) — these are YAML + CLI, not Python
  - Part X capstone's drift-monitor cron, serving endpoint — production-shaped

**Chosen approach: hybrid (notebook + `scripts/`).** For Parts
III / IV / VII / IX-cluster / X, the artifact is a `scripts/` directory
(`train.py`, `launch.sh`, `serve.py`, `*.yaml`) and the notebook becomes
the **runbook**: documents what each script does, shows the
`accelerate launch …` / `sbatch …` / `tritonserver …` command, fetches
W&B run results, and renders comparison tables from TSVs the script
wrote. The reader executes the multi-process / daemon / cluster code
**from a terminal** (locally if they have GPUs, or on a rented Lambda /
CoreWeave / Modal box).

**Alternatives considered and rejected:**

1. *Drop the genuinely distributed parts* — cut III / IV / VII to
   single-GPU demos with "here's how it scales" prose. Keeps the
   notebook-only invariant but teaches less, and would leave the
   user unprepared for the actual SOTA workloads they're targeting.
2. *Spin distributed parts into a separate non-notebook companion* —
   an `engineering/` directory of pure-script projects alongside the
   notebook course. Fragments Course 13 across two delivery surfaces;
   harder for the reader to navigate.

The hybrid trade is the right one because the user is learning to
**ship** — running `accelerate launch` from a terminal is part of the
job, and a notebook pretending it isn't would be cargo-cult MLOps. The
[Course 13 README](courses/13-mlops-biology-fms/README.md) makes the
per-part notebook-vs-`scripts/` split explicit and the builder
generates both artifacts for hybrid parts.

---

## Math & Methods companions (cross-cutting)

These are not sequential topics — they are mathematical / methodological tools
that apply across multiple roadmap topics above. The user already has solid
calculus (differential, stochastic) and standard ML math, which makes the Tier 1
items unusually high-leverage.

### Tier 1 — high leverage, compounds with existing math background

**Stochastic modeling of gene expression**
Master equations, Gillespie SSA, Langevin / chemical SDEs for transcription
bursting, Fokker-Planck for cell-state distributions. Maps directly to stochastic
calculus.
**Why for aging:** single-cell aging signatures are noise + drift; epigenetic
clocks partly capture stochastic accumulation.
**Tools:** `gillespy2`, `tellurium`, `pymc`, `pyro`.
**Connects to topics:** 1, 2, 6.

**Dynamical systems & cell-fate attractors**
Bifurcations, basins of attraction, Waddington landscapes as potentials, ODE/PDE
biology.
**Why for aging:** aging = attractor shift; rejuvenation = attractor escape.
Partial reprogramming literature uses this framework explicitly.
**Tools:** `scipy.integrate`, `pyDSTool`, `dynamo` (ML-aware), `cellrank`.
**Connects to topics:** 8, 10, 11.

**Causal inference**
DAGs, do-calculus, instrumental variables, Mendelian randomization, fine-mapping,
counterfactual reasoning.
**Why for aging:** the biggest methodological gap in longevity research is
distinguishing causal aging drivers from correlated biomarkers. UK Biobank + MR
is how non-RCT causal claims get made. This is arguably as important as any of
the 12 biology topics for actual drug discovery.
**Tools:** `dowhy`, `econml`, `pgmpy`, `causal-learn`, `MR-Base`/`TwoSampleMR` (R).
**Connects to topics:** 8, 12.

**Active learning & experimental design — the data-moat engine**
Bayesian optimization, acquisition functions, sequential / optimal experimental
design, closed-loop *design → assay → retrain*, active learning for
labeling-expensive biology.
**Why for the founder path:** the verified 2026 TechBio thesis (Bessemer) is that
the defensible moat is *proprietary, biology-native data generation*, not model
architecture. The ML discipline that turns a wet lab into a **compounding data
advantage** — rather than a thin model wrapper over public data — is active
learning + experimental design. This is the skill that lets an ML founder build a
moat. (Phase 3 of the prioritization layer.)
**Tools:** `botorch`, `ax-platform`, `scikit-optimize`, `gpytorch`, `modAL`.
**Connects to topics:** 7, 9 (design loops), 6/8 (perturbation & virtual-cell
loops), plus any proprietary data-generation platform.

### Tier 2 — useful, more specialized

**Information theory in biology**
Shannon entropy, mutual information, transfer entropy. Sequence logos are bits;
TF–target inference uses MI; single-cell embedding metrics use KL.
**Connects to topics:** 1, 6.

**Graph theory + Graph Neural Networks**
PPI networks, GRNs, molecular graphs, equivariant GNNs.
**Tools:** `networkx`, `pytorch-geometric`, `dgl`, `e3nn`.
**Connects to topics:** 9, plus GRN inference across 1, 2, 6.

**Optimal transport**
Single-cell trajectory inference, domain adaptation, perturbation alignment.
**Tools:** `pot`, `moscot`, `wot` (Waddington-OT).
**Connects to topics:** 2, 8, 10.

### Tier 3 — defer until you hit them

- **Biophysics / molecular dynamics** — abstracted away by ESM/AlphaFold for ML
  purposes. Pick up if going deep on protein design (Topic 7).
- **Statistical genetics theory** (LD, fine-mapping, heritability decomposition) —
  pick up when reaching Topic 12.
- **Reinforcement learning** — natural when hitting drug design or sequential
  decision problems (Topic 9). *(Active learning / experimental design has been
  promoted to Tier 1 above — it's the data-moat engine for the founder path.)*

### Note on systems biology and GRNs

- **Systems biology** is essentially Tier 1 stochastic modeling + dynamical
  systems applied to biology. Treat as a unifying frame, not a separate topic.
- **GRN inference** is already covered: Boolean GRNs in Topic 1 (Part VIII),
  implicit GRN learning in Topic 6 single-cell foundation models. The math *of*
  GRN inference (Bayesian networks, causal discovery) lives under Tier 1 causal
  inference above.

### Supplementary reading — when a notebook isn't enough

The course is calibrated for an ML engineer targeting SOTA in anti-aging
biotech, so most topics teach a working vocabulary, not textbook foundations.
Don't pre-load with books — do the notebook first, then reach for these only
when downstream work makes you wish you understood more.

| Topic / Part | Notebook gives you | Reach for a book when… | Recommended supplement |
|---|---|---|---|
| **Topic 1 / Part VII — Dynamics & Signaling** | Hill functions, ODE simulation, Gillespie SSA, 3 canonical circuits (repressilator, toggle, FFL), 4 aging hooks (inflammaging, p53 plateau, circadian dampening, noise rise). Skips kinase-cascade biology, SDEs / chemical Langevin / Fokker-Planck, formal bifurcation theory, master equation depth, parameter inference. | You're working on perturbation modeling (Topic 8) or partial reprogramming (Topic 10) and want to reason about circuit motifs more deeply than the notebook's tour. | **Alon, *An Introduction to Systems Biology* (2nd ed., 2019)** — canonical follow-up; chapters on FFLs, oscillators, robustness map 1:1 onto the notebook. |
| **Topic 1 / Part VII — Dynamics & Signaling (stochastic)** | Gillespie SSA from scratch, telegraph model, Fano factor, super-Poissonian bursting. Skips formal master equation, chemical Langevin, parameter inference. | You're *fitting* biophysical models to data (rare on the SOTA anti-aging ML path right now). | **Wilkinson, *Stochastic Modelling for Systems Biology*** — proper SDE / master-equation treatment. Skip unless a specific project demands it. |

When `gene-regulation ML` is the destination (Topics 5–6, foundation models),
the notebook alone is enough — bursting + circuit motifs are the conceptual
hooks needed to read scGPT / Geneformer papers critically. Move on rather
than supplementing.

---

## Practical Python ecosystem (cross-cutting)

| Layer | Libraries |
|---|---|
| Sequence / interval | `biopython`, `pyfaidx`, `pysam`, `pyranges`, `bioframe` |
| Single-cell | `scanpy`, `anndata`, `muon`, `scvi-tools`, `cellrank`, `squidpy` |
| 3D genome | `cooler`, `cooltools`, `pairtools` |
| Visualization | `dna_features_viewer`, `pyGenomeTracks`, `logomaker`, `py3Dmol`, `nglview` |
| Cheminformatics | `rdkit`, `deepchem`, `torchdrug` |
| ML | `pytorch`, `pytorch-lightning`, `transformers`, `pytorch-geometric` |
| Stats / GWAS | `hail`, `statsmodels`, `scikit-learn` |

---

## Course build order (founder-path) — ✅ Track B active

**Chosen vertical (2026-06-03): Track B — biological foundation models / virtual
cell.** Rationale: best fit for an ML/MLOps-native founder; the user is already
skilled here. Tracks A and C are **parked below, not deleted** — retained for
future optionality (a pivot, a second product, or an early-employee move).

Sequenced to the phases above, not to topic numbers. Most courses already exist
(see each course's `README.md`); this is the order to *prioritize and deepen*
under Track B, not a from-scratch plan.

### Phase 1 — Common core (do first)
1. **Course 02 (single-cell genomics)** — now first-class, not just literacy: it's
   the data substrate for every single-cell FM. Deepen, don't skim.
2. **Course 01 (gene regulation)** — skim for literacy; enough to read FM papers.
3. **Course 13 (MLOps)** — stand up as the always-on spine. For Track B this is not
   optional flavor: training / fine-tuning / eval / serving FMs *is* the work, and
   it's your pre-existing edge.

### Phase 2 — Track B depth (the spine of the company)
**Re-weighted 2026-06-05 to the MVP** (see `docs/strategy/track-b-mvp-spec.md`): the first
artifact is a **perturbation-prediction eval harness + a baseline-aware method**,
entered via the eval layer — *not* by training FMs to license weights. So Course 08
is the centre of gravity, reached fast; 05 drops off the critical path.
4. **Course 08 (perturbation modeling)** — **the MVP itself.** Predict the effect of
   a knockout / drug; GEARS, CPA, State, the Ahlmann-Eltze PCA-linear baseline,
   PerturBench / PertEval-scFM. Topic 8's model/data/benchmark list maps **1:1** onto
   the MVP spec. This is where the eval-harness whitespace and the moat live.
5. **Course 06 (single-cell foundation models)** — needed as **baselines to profile**,
   not as build targets: Geneformer, scGPT, UCE, State zero-shot + their failure
   modes. Course 02 Part XI already gives enough scFM literacy to *start* Course 08;
   deepen 06 alongside/just before, focused on benchmarking rather than training your
   own scFM.
6. **Course 05 (DNA/RNA language models)** — **demoted off the MVP critical path.**
   Sequence-to-function (Enformer, Borzoi, AlphaGenome, Evo 2) is a *different
   modality* from single-cell perturbation — zero of the MVP's models/data/metrics
   touch it. Keep at **conversant** level (Course 01 Part XI already loads Enformer on
   one locus); the full depth pass is optional, deferred until a sequence-level
   data-generation angle makes it concrete.

### Phase 3 — Data-moat engine (what makes it defensible) — **promote early**
7. **Active-learning / experimental-design module** (Tier-1 Math companion) layered
   onto the perturbation / virtual-cell loop: closed-loop *predict → assay →
   retrain*, plus the eval harness that proves predictions are useful. **Start as
   soon as the harness exists** — the calibrated-uncertainty layer in the MVP feeds
   straight into experiment selection. This is the answer to "why isn't this a
   commoditized wrapper" — own the data-generation loop and the eval, not the weights.

### Phase 4 — Mission depth (deferred, on demand)
- Courses 03, 04b, 10, 11, 12 — longevity / aging depth, opened only when a
  platform / company / interview makes a specific one concrete.

---

### Parked for future optionality (NOT building now — kept intentionally)
- **Track A — protein / molecule design:** Course 07 + Course 09. Revisit with a
  bench co-founder + capital, or via an early-employee move.
- **Track C — multi-omics / clinical-data platform:** Course 02 deep + a clinical /
  longitudinal-data course. Strongest moat (proprietary outcome-linked data) but a
  data-access / GTM challenge more than an ML one.
