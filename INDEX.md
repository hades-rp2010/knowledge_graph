# Academic Research Index
Note: This is a high-density, machine-readable index for the Research KB Manager. Do not manually edit the table structure as it is used for automated querying and graph generation.

| Paper | Anchor | Scientist Gist | Engineer Delta | Next Step | Category | Metric |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| [[attention_is_all_you_need]] | Sequence Modeling | Soft-dictionary lookup | Parallelizable MHA | O(n) attention approximations | papers | 28.4 BLEU |
| [[bert_pre_training_of_deep_bidirectional_transformers_for_language_understanding]] | Representation Learning | Bidirectional context | Masked LM | Longer sequence limit | papers | 80.5 GLUE |
| [[language_models_are_few_shot_learners]] | Generative Modeling | Scaling laws | 175B parameters | Alignment with intent | papers | SOTA (Zero-shot) |
| [[training_language_models_to_follow_instructions_with_human_feedback]] | Alignment & Safety | Human-in-the-loop | RLHF | Handling hallucination | papers | 1.3B > 175B Pref |
| [[roformer_enhanced_transformer_with_rotary_position_embedding]] | Neural Architectures | Relative rotation | RoPE | Long-context stability | papers | TBD |

## Directory Structure (Type-Based)
The vault uses a shallow, type-based folder structure:
- /papers: Peer-reviewed conference and journal papers.
- /blogs: Technical blog posts and intuition-first summaries.
- /theses: PhD and Master dissertations.

## The Evolutionary Map
Check individual file YAML frontmatter (e.g., EXTENDS, FIXES, DESCENDANTS) to see how ideas extend, fix, or generalize their ancestors.
