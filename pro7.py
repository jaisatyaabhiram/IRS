7.	To parse XML text, generate Web graph and compute topic specific page rank. 
Aim: To parse XML text, generate Web graph and compute topic specific page rank. 
Description: 
Objective: Conceptual Overview:
What is XML Parsing?
XML (eXtensible Markup Language) is a standard format for representing structured data. In the context of the Web, XML is often used to describe the structure of websites, including links between pages.
What is a Web Graph?
A Web Graph is a directed graph where:
•	Nodes represent web pages.
•	Edges represent hyperlinks between them.
What is PageRank?
PageRank is an algorithm used to rank web pages based on their link structure. It assumes that important pages are linked to by many other important pages.
Topic-Specific PageRank:
Unlike global PageRank, Topic-Specific PageRank biases the random surfer model towards a specific topic or set of nodes. The teleportation step prefers pages related to a specific topic, helping in focused web crawling and topic-sensitive search.
Program:
# Install required libraries
!pip install -q networkx
import xml.etree.ElementTree as ET
import networkx as nx
import matplotlib.pyplot as plt
#  Sample XML Data (you can replace this with actual XML content)
xml_data = '''
<pages>
  <page name="PageA">
    <link>PageB</link>
    <link>PageC</link>
  </page>
  <page name="PageB">
    <link>PageC</link>
  </page>
  <page name="PageC">
    <link>PageA</link>
  </page>
  <page name="PageD">
    <link>PageC</link>
  </page>
</pages>
'''
#  Parse XML
root = ET.fromstring(xml_data)
#  Create directed graph
web_graph = nx.DiGraph()
# Add nodes and edges
for page in root.findall('page'):
    src = page.get('name')
    web_graph.add_node(src)
    for link in page.findall('link'):
        dest = link.text
        web_graph.add_edge(src, dest)
# Display the graph
plt.figure(figsize=(6, 5))
nx.draw(web_graph, with_labels=True, node_color='skyblue', edge_color='gray', node_size=2000, font_size=14)
plt.title("Web Graph", fontsize=16)
plt.show()
#  Compute PageRank
pagerank_scores = nx.pagerank(web_graph, alpha=0.85)
#  Display results
print(" PageRank Scores:")
for page, score in pagerank_scores.items():
    print(f"{page}: {score:.4f}")
Output:
 
PageRank Scores:
PageA: 0.3725
PageB: 0.1958
PageC: 0.3942
PageD: 0.0375
