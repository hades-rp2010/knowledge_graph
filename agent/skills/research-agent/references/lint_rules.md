# Wiki Integrity Rules (Linting)

## 1. Index Completeness (INDEX.md)
- Every `.md` file in `/papers`, `/blogs`, or `/theses` MUST have an entry in `INDEX.md`.
- The index table MUST contain exactly 7 columns: Paper, Anchor, Scientist Gist, Engineer Delta, Next Step, Category, Metric.
- **Next Step vs TO_READ:** The `Next Step` column is for **High-Level Research Ideas**. Actual paper links belong in `TO_READ.md`.

## 2. Theoretical Anchor Taxonomy (ML-Oriented)
To maintain a searchable graph, only use the following approved Anchors. 
*Note: This taxonomy is dynamic and may be updated as the KB grows.*
- **Sequence Modeling:** (Transformers, RNNs, SSMs, Attention)
- **Representation Learning:** (Pre-training, Embeddings, NLU)
- **Generative Modeling:** (Autoregression, Diffusion, GANs, VAEs)
- **Reinforcement Learning:** (Policy Gradients, Q-Learning, MDPs)
- **Alignment & Safety:** (RLHF, Reward Modeling, Robustness)
- **Neural Architectures:** (Structural innovations, Layer norms, Positional embeddings)
- **Optimization & Scaling:** (Scaling laws, Convergence, Efficiency)
- **Probabilistic Inference:** (Bayesian ML, Uncertainty, Latent variables)

## 3. Link Integrity
- All `[[WikiLinks]]` in YAML frontmatter MUST resolve to an existing `.md` file or be an unresolved `TO_READ` link.
- Every `DESCENDANTS` link MUST have a corresponding backward relationship.

## 4. Frontmatter & Naming
- Every file MUST have YAML frontmatter following the Ancestry Protocol.
- Approved verbs: `EXTENDS`, `FIXES`, `GENERALIZES`, `PARALLELIZES`, `SPATIALIZES`, `CONCEPTUALIZES`, `EQUIVALENCE`, `EXPLAINS`, `CONSOLIDATES`.
- All files MUST be `snake_case.md`.
