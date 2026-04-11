# Wiki Integrity Rules (Linting)

## 1. Index Completeness
- Every `.md` file in the knowledge base (except protocol/meta files) MUST have an entry in the `README.md` index table.
- The index table MUST contain all 7 mandatory columns: Paper, Anchor, Scientist Gist, Engineer Delta, Next Step, Category, Metric.
- The `Category` in the index table MUST match the folder path (e.g., `NLP/LLMs`).

## 2. Link Integrity
- All `[[WikiLinks]]` in YAML frontmatter MUST resolve to an existing `.md` file in the workspace or be acknowledged as an unresolved `TO_READ` link.
- All `[[WikiLinks]]` in the body MUST resolve.

## 3. Bi-Directional Lineage
- If Paper A `EXTENDS` Paper B, Paper B SHOULD have Paper A in its `DESCENDANTS` list.
- If Paper B has Paper A in its `DESCENDANTS`, Paper A SHOULD have a relationship link (e.g., `EXTENDS`, `FIXES`) back to Paper B.

## 4. TO-READ Management
- Any paper listed in `TO_READ.md` that now has a corresponding `.md` file in the workspace MUST be removed from the `TO_READ.md` ledger.
- The `TO_READ` keys in YAML frontmatter should periodically be reviewed for resolution.

## 5. Frontmatter Standards
- Every paper MUST have a YAML frontmatter block.
- Supported verbs: `EXTENDS`, `FIXES`, `GENERALIZES`, `PARALLELIZES`, `SPATIALIZES`, `CONCEPTUALIZES`, `EQUIVALENCE`.

## 6. File Naming
- All paper files MUST be `snake_case.md`.
