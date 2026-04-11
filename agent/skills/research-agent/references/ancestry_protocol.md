# The Ancestry Protocol (Obsidian Native)

When integrating a new Paper A:

1. **Identify Ancestors:** Search the Knowledge Base for any papers this new work builds upon.
2. **Rule of Foundation (Roots):**
   - If **no ancestor** exists in the KB, leave the relationship keys empty. 
   - The paper is now a **ROOT** of its own lineage.
   - (Optional) Add `ROOT: true` to the YAML for organizational clarity.
3. **Linkage (YAML Frontmatter):**
   - Add the relationship verb as a key and the ancestor's WikiLink as the value.
   - **Allowed Verbs:** `EXTENDS`, `FIXES`, `GENERALIZES`, `PARALLELIZES`, `SPATIALIZES`, `CONCEPTUALIZES`, `EQUIVALENCE`.
   - **Multi-Parent Rule:** If a paper bridges multiple fields or ancestors, use a YAML list:
     ```yaml
     EXTENDS: 
       - "[[attention_is_all_you_need]]"
       - "[[another_foundational_paper]]"
     ```
4. **Back-linking:**
   - Open all Ancestor files and add Paper A to their `DESCENDANTS` list in the YAML.
   - Format: `DESCENDANTS: ["[[paper_a_id]]"]`

## Maintenance
- **WikiLinks:** Use `[[snake_case_filename]]` for all internal paper references.
- **Master Index (README.md):** Every new paper MUST be appended to the table in `/Users/rishabhpatra/Desktop/kb/README.md` with the following columns:
    1. **Paper**: `[[id]]`
    2. **Theoretical Anchor**: High-level scientific framework.
    3. **Scientist Gist**: Core mechanistic intuition.
    4. **Engineer Delta**: Specific technical innovation.
    5. **Next Step**: The identified research opening.
    6. **Category**: Folder path (e.g., NLP/LLMs).
    7. **Metric**: Primary SOTA result.
- **The Log:** Every modification (add/edit/move) MUST be recorded in `/Users/rishabhpatra/Desktop/kb/CHANGELOG.md` with a timestamp.
