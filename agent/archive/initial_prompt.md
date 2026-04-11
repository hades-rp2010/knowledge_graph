Create a knowledge base from a collection of academic papers. Iterate through the child directories of the specified input folder (e.g., `/Users/rishabhpatra/Zotero/storage`).
     For each directory containing a PDF file, extract its content and generate a comprehensive markdown summary. Save each summary as a `.md` file in the designated output
     directory (e.g., `/Users/rishabhpatra/Desktop/kb/`), naming the file using the paper's title formatted in snake_case (e.g., `the_paper_title.md`). 
 
Each markdown summary MUST include the following structured sections:
1. **Abstract:** A brief overview of the paper's abstract.
2. **Main Idea & Motivation:** The core proposition of the paper, why this specific approach has not been done before, and the limitations or problems with existing methods that it addresses.
3. **Experimental Setup:** A detailed description of the methodology and environment used to test the proposed idea.
4. **Results:** A summary of the empirical findings, including descriptions of key graphs, charts, or tables that illustrate the results.
5. **Mathematical Formulation:** Any relevant mathematics, equations, or proofs provided in the paper to validate the new idea.


---

Act as a Senior Research Engineer distilling a paper into its "Minimalist Gist." Your goal is to strip away academic boilerplate and reveal the core "delta" (innovation). Use      plain but technically precise language.

 Structure the summary into these 5 specific sections:

 1. THE DELTA (1-2 Sentences):
 Identify the exact technical change this paper proposes compared to the status quo. What is the one thing they did differently?

 2. THE PROBLEM & INTUITION:
 - Why was the previous state-of-the-art (SOTA) "broken" or inefficient?
    - Explain the new solution using a high-level intuition that a senior developer could implement. Avoid "academic-ese."

 3. THE MATHEMATICAL GIST:
 - Provide the 1-3 "Load-Bearing" equations that define the innovation.
 - Define the variables concisely.
 - Explain how these equations mathematically enforce the "Delta" mentioned above.

 4. THE "MONEY SHOT" (RESULTS & COMPARISONS):
 - METRICS: List the specific primary metrics used (e.g., FID score, Bits/dim, Top-1 Acc).
 - BASELINES: Which specific models were they trying to beat? (e.g., "Outperforms PixelCNN++ and standard VAEs").
 - THE GRAPH: Describe the single most important plot/table in the paper. What does the x/y axis show, and what ise "gap" that proves this method works?

 5. IMPLEMENTATION THOUGHTS (THE "MIN-GPT" VIEW):
 If you were to write a 100-line "min-[PaperName].py" script, what would be the core loop or kernel? Identify the most important architectural detail (e.g., a specific masking
      pattern or a loss weighting trick).