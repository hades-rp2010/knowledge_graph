---
name: research-kb-manager
description: Interactive tools and protocols for managing the academic research knowledge base (Ingest, Query, Lint). Use this when the user wants to add papers, ask research questions, or maintain wiki integrity.
---

# Research Knowledge Base Manager

This skill provides the procedural logic for managing a high-fidelity research vault. It is designed for **interactive collaboration** between Gemini and the user.

## Core Operations

### 1. Ingest
Use this operation to add a new paper from your Zotero collection.
- **Workflow**:
  ...
  5. **Link**: Apply the [ancestry_protocol.md](references/ancestry_protocol.md).
  6. **Queue**: If the discussion reveals follow-up papers, add them to the `TO_READ.md` ledger and the paper's YAML.
  7. **Register**: Perform the **Index & Graph Update**.

### 2. Query
Use this operation to answer complex research questions based on the KB.
- **Workflow**:
  1. **Search**: Search the workspace using `grep_search` and the `README.md` index.
  2. **Analyze**: Use the lineage graph (visualized via `vis.py` or Obsidian) to find related concepts.
  3. **Synthesize**: Answer with citations. Support text, matplotlib charts, or numerical tables.
  4. **Deep Dive**: Use `google_web_search` or `web_fetch` for external context if needed.
  5. **Insert Back**: If the answer is high-quality, offer to write it into a new or existing wiki page.
  6. **Register**: Perform the **Index & Graph Update** if new pages were created.

### 3. Lint
Use this operation to maintain KB health.
- **Workflow**:
  1. **Check**: Validate the workspace against [lint_rules.md](references/lint_rules.md).
  2. **Report**: Alert the user to broken links, missing index entries, or lineage gaps.
  3. **Review**: Wait for user confirmation or corrections.
  4. **Fix**: Apply the agreed-upon corrections.

---

## Common Sub-Operations

### Index & Graph Update
Every time a file is added, moved, or its lineage changes:
1. **README.md**: Append/update the paper in the master table with exactly these columns:
   - **Paper**: `[[id]]`
   - **Anchor**: Scientific Framework (e.g., Information Theory).
   - **Scientist Gist**: Mechanistic intuition.
   - **Engineer Delta**: Technical innovation.
   - **Next Step**: Identified research opening.
   - **Category**: Zotero path.
   - **Metric**: Primary SOTA result.
2. **CHANGELOG.md**: Record the change with a timestamp.
3. **Graph**: Run `source .venv/bin/activate && python agent/skills/research-agent/scripts/vis.py` to regenerate the standalone graph.

---

## Procedural Guidance
- **Internet Usage**: Always supplement internal KB data with `google_web_search` when the user asks for "recent developments" or "further deep dives."
- **Visuals**: When asked for comparisons, prioritize generating `matplotlib` charts or Markdown tables for clarity.
- **Collaboration**: In the **Ingest** phase, do NOT write the wiki until you have discussed the "Gist" with the user.
