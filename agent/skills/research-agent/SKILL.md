---
name: research-kb-manager
description: Interactive tools and protocols for managing the academic research knowledge base (Ingest, Query, Lint). Use this when adding papers, asking research questions, or maintaining wiki integrity.
---

# Research Knowledge Base Manager

This skill provides the **Workflow Controller** for managing your research vault. It coordinates the interaction between scripts, reference protocols, and the user.

## Core Operations

### 1. Ingest (Socratic Mode)
Use this to add new Papers, Blogs, or Theses.
- **Workflow**:
  1. **Lookup**: Run `scripts/zotero_lookup.py`.
  2. **Facts**: Present "Load-bearing Facts" from the source.
  3. **Discussion**: Wait for the user to lead a scientific discussion.
  4. **Draft**: Propose a summary ONLY when requested. **Follow `references/summary_protocol.md` strictly.**
  5. **Write**: Save to `/papers`, `/blogs`, or `/theses`.
  6. **Link**: Apply `references/ancestry_protocol.md`.
  7. **Register**: Perform the **Index & Graph Update**.

### 2. Query
Use this to synthesize knowledge from the vault.
- **Workflow**:
  1. **Search**: Query the `INDEX.md` and the workspace.
  2. **Analyze**: Use the graph to trace lineages.
  3. **Respond**: Provide dual-perspective answers (Scientist/Engineer).
  4. **Deep Dive**: Use `google_web_search` for external context.

### 3. Lint
Use this to verify KB health.
- **Workflow**:
  1. **Audit**: Validate the vault against `references/lint_rules.md`.
  2. **Report & Fix**: Highlight gaps and apply corrections with approval.

---

## Common Sub-Operations

### Index & Graph Update
Mandatory for every modification:
1. **INDEX.md**: Update the master table using the columns defined in `references/ancestry_protocol.md`.
2. **CHANGELOG.md**: Record the event with a timestamp.
3. **Graph**: Run `source .venv/bin/activate && python agent/skills/research-agent/scripts/vis.py`.

---

## Procedural Principles
- **Delegation**: Do not invent formats. Always defer to the `references/` folder for summary and linking rules.
- **Interactivity**: The user is the Lead Researcher. Present evidence, ask for intuition, and wait for confirmation.
- **Dual-Perspective**: Every discussion and output MUST balance the **Research Scientist** and **Sr. Research Engineer** personas.
