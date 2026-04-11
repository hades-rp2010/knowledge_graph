# The Summary Protocol

Every new entry MUST be a single Markdown file titled in `snake_case`. It MUST contain two perspectives in the following order:

---

### Perspective A: The Research Scientist (Science & Future Work)
*Focus: Deep understanding of the "why" and identifying the next research frontier.*

1. **CONCEPTUAL FRAMEWORK:** The high-level mental model (e.g., "Sequence Modeling as Information Routing" or "Thermodynamics as Generative AI").
2. **MECHANISTIC INTUITION:** 
   - Explain why the science actually works at a fundamental level. 
   - *Guidance:* Contrast the new method against the previous paradigm (e.g., "Reframes language from temporal flow to content-addressable graphs"). Avoid high-level fluff; focus on the *mechanism* of the breakthrough.
3. **ARCHITECTURAL LINEAGE:** Where this fits in the timeline. What previous SOTA did it "kill" or supersede?
4. **ADVERSARIAL CRITIQUE:** Objective limitations, potential cherry-picking in results, or missing ablations (the "Reviewer #2" lens).
5. **RESEARCH OPENINGS:** 
   - Based on the flaws or assumptions, what is the specific "Next Paper" that could be written? 
   - *Requirement:* Identify at least one technical bottleneck (e.g., $O(n^2)$ scaling) and one conceptual bottleneck (e.g., "position blind").

---

### Perspective B: The Senior Research Engineer (Execution & Scale)
*Focus: Implementation, performance, and practical application at scale.*

1. **THE DELTA:** One sentence identifying the specific technical innovation compared to the status quo. (e.g., "Replaces Recurrence with Multi-Head Self-Attention").
2. **THE MATHEMATICAL GIST:** 
   - 1-3 "load-bearing" equations. Define all variables. 
   - Explain the "forward pass" logic in terms of matrix dimensions where relevant.
3. **THE RECEIPTS (RESULTS):** 
   - **Numerical Comparison:** Mandatory table/list of exact metrics (e.g., FID, NLL, Acc, BLEU). Define metrics if they are new to the KB.
   - **The Graph Trend:** Descriptive analysis of the primary plot (e.g., "The loss curve follows a Power Law with respect to compute").
4. **IMPLEMENTATION TRAPS:** One specific detail that causes re-implementations to fail (e.g., specific scaling factors, initialization schemes, or warmup schedules).
5. **PRODUCTION & SCALING:** Estimates for VRAM usage, inference latency, and observations on scaling law behavior.

---

## Extraction Rigor
- **No Hallucinations:** If a paper does not provide an exact number, state "Not reported." 
- **Tool Usage:** Use `pdftocairo` or `grep_search` to find exact table values. Do not summarize results from the abstract alone; verify in the "Experiments" section.
