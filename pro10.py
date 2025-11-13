Aim: To implementation of PageRank on Scholarly Citation Network.
Description:
Objective: To implement the PageRank algorithm on a Scholarly Citation Network to determine the relative importance of research papers based on citations, similar to how Google ranks web pages.
Conceptual Overview:
 What is PageRank?
PageRank is an algorithm originally developed by Google to rank web pages. It assigns a numerical weight to each node (e.g., a webpage or paper) based on the number and quality of links (citations) it receives.
In the context of scholarly citations:
•	Each node represents a research paper.
•	A directed edge from paper A to paper B implies that A cites B.
•	A paper that is cited by many important papers gets a higher PageRank score.
Why PageRank for Citation Networks?
•	Helps identify influential or foundational research papers.
•	Better than just counting citations, since it also considers who is citing the paper.
•	Useful in literature reviews, recommender systems, and academic search engines.
Program:
# Install required library
!pip install -q networkx matplotlib
import networkx as nx
import matplotlib.pyplot as plt
#  Step 1: Simulate a Scholarly Citation Network
# Nodes represent papers, edges represent citations (Paper A cites Paper B)
citation_edges = [
    ("Paper1", "Paper2"),
    ("Paper1", "Paper3"),
    ("Paper2", "Paper3"),
    ("Paper3", "Paper4"),
    ("Paper4", "Paper5"),
    ("Paper5", "Paper1"),  # Circular citation
    ("Paper6", "Paper2"),
    ("Paper7", "Paper2"),
    ("Paper7", "Paper4"),
    ("Paper8", "Paper4"),
]
#  Step 2: Create a directed graph
G = nx.DiGraph()
G.add_edges_from(citation_edges)
#  Step 3: Visualize the graph
plt.figure(figsize=(8, 6))
pos = nx.spring_layout(G, seed=42)
nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=2000, arrows=True, font_size=12)
plt.title(" Scholarly Citation Network")
plt.show()
#  Step 4: Compute PageRank
pagerank_scores = nx.pagerank(G, alpha=0.85)
#  Step 5: Display PageRank scores
print("\n PageRank Scores (Influence of Papers):")
sorted_scores = sorted(pagerank_scores.items(), key=lambda x: x[1], reverse=True)
for paper, score in sorted_scores:
    print(f"{paper}: {score:.4f}")
Output:
 
PageRank Scores (Influence of Papers):
Paper4: 0.2177
Paper3: 0.2060
Paper5: 0.2038
Paper1: 0.1920
Paper2: 0.1243
Paper6: 0.0188
Paper7: 0.0188
Paper8: 0.0188
	
