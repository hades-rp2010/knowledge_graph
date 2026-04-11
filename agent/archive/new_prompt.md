### TASK:
Your task is to create an agent for me with 3 operations. This should be an agent that can be invoked from the gemini-cli and operations may be invoked from the agent . The operations are ingest, query, and lint, with their descriptions below:


## Operation 1: Ingest
This agent's responsibility is to process a new source file, which will be a document present in the zotero collection, under a subcollection. The processing involves reading the source, discussing takeaways with the user (ie, me), write the wiki in the specified format based on the takeaways, then update the index and link relevant wikis in the workspace (may be from the same folder, or from other folders containing wikis in the workspace).

## Operation 2: Query
I ask a question to the agent, and the agent searches through the workspace, using the index and the graph linkages to find out relevant pages, reads them, synthesizes an answer with citations (this can either be wiki page, a website, a paper on arxiv etc). The answers can be in the form of text in a markdown page, a chart in matplotlib, a comparison table for numbers. **Good answers can then be inserted back into wikis**: the agent then writes down the good answers in either the relevant pages already present or a new page. it should also be able to then update the indexes and the lineage graph to include the new page.

## Operation 3: Lint
Periodically called, this operation should check the integrity of the wiki. Check out the index and lineage graph to spot links to non-existing pages, or wrong linkages. It should then alert me and wait for my review, and apply my corrections to the workspace. 

## Suggested comments
- The update index, update graph, seems like a repetitive action, and I will leave it up to you to decide if you'd like to extract this into a common new sub-operation or tool which can then be invoked by each of the operations. I could however be suffering from a very high-level view of the process and this may not be feasible, in which case you may keep them in their own operation spaces
- Both the ingest operations may need to reference the internet for suggested readings or further deep dives.