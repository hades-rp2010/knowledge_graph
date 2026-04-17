# Academic Research Knowledge Base

Welcome to your structured academic vault. This project is a high-fidelity system for mapping the evolution of machine learning through a dual-perspective lens (Research Scientist & Senior Research Engineer).

## Vision
This vault is more than a collection of summaries; it is a **dynamic graph** of ideas. Every entry is meticulously linked by technical lineage to visualize the trajectory of SOTA.

## Directory Structure (Zotero Aligned)
The folder hierarchy mirrors your **Zotero collection structure** exactly. Research summaries are placed in their respective sub-topic folders (e.g., `NLP/LLMs/`) to maintain a 1:1 mapping with your source PDF library.

- **/NLP, /CogSci, etc.**: The research summaries.
- **INDEX.md**: The high-density database used by the agent.
- **TO_READ.md**: The upcoming research frontier.
- **/agent**: The "Brain" of the system (Protocols, Scripts, Personas).

## The Evolutionary Map
Lineage is tracked using an **Obsidian-native** approach. Check the **YAML frontmatter** of any paper to see its ancestry:
- **`EXTENDS` / `FIXES`**: Links to the paper's ancestors.
- **`DESCENDANTS`**: Links to papers that built upon this work.
- **`TO_READ`**: Papers identified as the next logical step in this specific research path.

## Operational Guide
This Knowledge Base is managed by a specialized **Research KB Manager** skill. Interact with it directly in the Gemini CLI:
- **Add a Paper:** `Ingest [Paper Title/Keywords]`
- **Ask Questions:** `Query [Your scientific question]`
- **Check Integrity:** `Run a lint check`
