# Knowledge Base Maintenance Prompts

Use these prompts to load context into a new Gemini session or to process new materials.

## Prompt A: Context & Purpose (The "System Load")
```text
I am working on a Research Knowledge Base (KB) located at /Users/rishabhpatra/Desktop/kb/. 
The purpose of this KB is to distill complex AI/ML research into two perspectives: 
1) Senior Research Engineer (The Karpathy Gist): Focuses on the technical delta, implementation traps, and numerical receipts.
2) Principal Investigator (The Lab PI): Focuses on conceptual frameworks, theoretical significance, and architectural history.

The directory mirrors my Zotero collection hierarchy. Every paper summary includes a "## THE LINEAGE" section modeling the Genealogy of Ideas (Ancestors vs. Descendants). 

Your task is to help me maintain this wiki by adding new papers or updating existing ones while strictly adhering to these two personas and the lineage logic.
```

## Prompt B: Summarize & Integrate (The "Paper Adder")
```text
Summarize the paper [Paper Name/Path] and integrate it into the KB. 

Follow these requirements:
1. PERSPECTIVES: Provide both 'Senior Research Engineer' and 'Principal Investigator' summaries.
2. THE RECEIPTS: Extract exact numerical results from tables and describe specific trends in graphs.
3. THE TRAPS: Identify common implementation pitfalls or critical architectural details (e.g., Batch Norm handling).
4. THE LINEAGE: 
   - Identify Ancestors: Which papers in this KB does it build on? Use verbs like EXTENDS, FIXES, GENERALIZES.
   - Update Ancestors: Open the ancestor files and add this new paper to their 'Descendants' section.
5. INDEXING: Append a 1-line gist of this paper to the master table in /Users/rishabhpatra/Desktop/kb/README.md.
6. LOGGING: Add an entry to /Users/rishabhpatra/Desktop/kb/CHANGELOG.md.
```

## Prompt C: The Persistent Log (The "Auditor")
```text
Read /Users/rishabhpatra/Desktop/kb/CHANGELOG.md and provide a summary of the most recent additions. 
Ensure that for every paper added in the last session, the corresponding README.md entry and the 'LINEAGE' sections in ancestor papers were also updated.
```
