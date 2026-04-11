# Operational Mandates: Research Knowledge Base (KB)

## 0. Project Context & Source Paths
- **KB Root:** `/Users/rishabhpatra/Desktop/kb/`
- **Zotero Database:** `/Users/rishabhpatra/Zotero/zotero.sqlite`
- **Zotero PDF Storage:** `/Users/rishabhpatra/Zotero/storage/`

## 1. The Summary Protocol
Every new entry MUST be a single Markdown file titled in `snake_case`. It MUST contain two perspectives in the following order:

### Perspective A: The Research Scientist (Science & Future Work)
1. **CONCEPTUAL FRAMEWORK:** The high-level mental model.
2. **MECHANISTIC INTUITION:** Why the science actually works at a fundamental level.
3. **ARCHITECTURAL LINEAGE:** Where this fits in the timeline.
4. **ADVERSARIAL CRITIQUE:** Objective limitations or missing ablations.
5. **RESEARCH OPENINGS:** Specific "Next Paper" ideas or follow-up experiments.

### Perspective B: The Senior Research Engineer (Execution & Scale)
1. **THE DELTA:** One sentence identifying the specific technical innovation.
2. **THE MATHEMATICAL GIST:** 1-3 "load-bearing" equations. Define all variables.
3. **THE RECEIPTS (RESULTS):** Numerical comparison table and descriptive analysis of the primary plot.
4. **IMPLEMENTATION TRAPS:** Specific details that cause re-implementations to fail.
5. **PRODUCTION & SCALING:** VRAM usage, inference latency, and scaling law behavior.

## 2. The Ancestry Protocol (Obsidian Native)
When integrating Paper A that builds on Paper B:
1. **Identify Ancestor:** Locate Paper B in the directory.
2. **Add Ancestor to A (YAML):** In Paper A's YAML frontmatter, add the relationship verb as a key and the ancestor's WikiLink as the value.
   - Example: `EXTENDS: [[attention_is_all_you_need]]`
   - Allowed Verbs: `EXTENDS`, `FIXES`, `GENERALIZES`, `PARALLELIZES`, `SPATIALIZES`, `CONCEPTUALIZES`, `EQUIVALENCE`.
3. **Update Ancestor B (Back-link):** Open Paper B's file and add the descendant to its YAML frontmatter using the reverse relationship or a `DESCENDANTS` list.
   - Preferred: Add `DESCENDANTS: [[[paper_a_id]]]` to Paper B's YAML.

## 3. Directory & Metadata Maintenance
- **Zotero Alignment:** New papers MUST be placed in the folder corresponding to their Zotero sub-collection (e.g., `NLP/LLMs/`).
- **WikiLinks:** Use `[[snake_case_filename]]` for all internal paper references.
- **Master Index:** Every new paper MUST be appended to the table in `/Users/rishabhpatra/Desktop/kb/README.md`.

- **The Log:** Every modification (add/edit/move) MUST be recorded in `/Users/rishabhpatra/Desktop/kb/CHANGELOG.md` with a timestamp.

## 4. Extraction Rigor
- **No Hallucinations:** If a paper does not provide an exact number, state "Not reported." 
- **Tool Usage:** Use `pdftocairo` or `grep_search` to find exact table values. Do not summarize results from the abstract alone; verify in the "Experiments" section.

## 5. The Zotero Lookup Protocol (Automated Discovery)
When the user asks to add a paper by **Title** or **Keywords**:
1. **Run Lookup:** Execute `python zotero_lookup.py "[Title Keywords]"`.
2. **Select Path:** Identify the correct `FULL PATH` and `COLLECTION` from the script output.
3. **Execute Summary:** Proceed with the "Summary Protocol" using the identified PDF path.
4. **Placement:** Save the resulting `.md` file in the folder corresponding to the script's `COLLECTION` output.
