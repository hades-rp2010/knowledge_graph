import os
import re
import networkx as nx
from pyvis.network import Network

# Configuration
KB_DIR = "/Users/rishabhpatra/Desktop/kb"
OUTPUT_FILE = "kb_graph.html"

# Relationship colors
VERB_COLORS = {
    "EXTENDS": "#4CAF50",    # Green
    "FIXES": "#F44336",      # Red
    "GENERALIZES": "#9C27B0", # Purple
    "PARALLELIZES": "#2196F3",# Blue
    "SPATIALIZES": "#FF9800", # Orange
    "CONCEPTUALIZES": "#795548", # Brown
    "EQUIVALENCE": "#00BCD4", # Cyan
    "DEFAULT": "#9E9E9E"     # Gray
}

def parse_kb():
    G = nx.DiGraph()
    summarized_papers = set()
    
    # 1. First pass: Find all summarized papers
    for root, dirs, files in os.walk(KB_DIR):
        for file in files:
            if file.endswith(".md") and file not in ["README.md", "CHANGELOG.md", "PROMPTS.md", "GEMINI.md"]:
                paper_id = file.replace(".md", "")
                summarized_papers.add(paper_id)
                G.add_node(paper_id, label=paper_id, color="#2196F3", title="Summary exists")

    # 2. Second pass: Parse lineage from frontmatter using regex
    for root, dirs, files in os.walk(KB_DIR):
        for file in files:
            paper_id = file.replace(".md", "")
            if file.endswith(".md") and paper_id in summarized_papers:
                source_paper = paper_id
                path = os.path.join(root, file)
                
                with open(path, 'r') as f:
                    content = f.read()
                    
                # Extract frontmatter block
                if content.startswith('---'):
                    parts = content.split('---', 2)
                    if len(parts) >= 3:
                        frontmatter_block = parts[1]
                        
                        for verb in VERB_COLORS.keys():
                            if verb == "DEFAULT":
                                continue
                            
                            # Robust regex to find the verb and its associated [[paper_id]] links
                            # Matches the verb, followed by anything until the next key (start of line) or end of block
                            pattern = rf"{verb}\s*:(.*?)(?=\n\S|\n---|$)"
                            match = re.search(pattern, frontmatter_block, re.DOTALL)
                            if match:
                                value_part = match.group(1)
                                # Extract all [[paper_id]] from the matched value part
                                target_ids = re.findall(r"\[\[(.*?)\]\]", value_part)
                                
                                for target_id in target_ids:
                                    # Clean ID (handle Obsidian-style anchors/aliases)
                                    target_id = target_id.split('#')[0].split('|')[0].strip()
                                    
                                    # Add node if it doesn't exist (Gray = missing summary)
                                    if target_id not in G:
                                        G.add_node(target_id, label=target_id, color="#CFD8DC", title="Summary missing")
                                    
                                    # Add edge (Ancestor -> Source)
                                    color = VERB_COLORS.get(verb, VERB_COLORS["DEFAULT"])
                                    G.add_edge(target_id, source_paper, label=verb, color=color, font={'align': 'top'})

    return G

def visualize(G):
    net = Network(height="750px", width="100%", bgcolor="#ffffff", font_color="black", directed=True)
    net.from_nx(G)
    
    # Enable physics for better layout
    net.toggle_physics(True)
    net.show_buttons(filter_=['physics'])
    
    net.show(OUTPUT_FILE, notebook=False)
    print(f"Visualization saved to {OUTPUT_FILE}")

if __name__ == "__main__":
    graph = parse_kb()
    visualize(graph)
