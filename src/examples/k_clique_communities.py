import networkx as nx
from matplotlib import pyplot as plt

__author__ = "\"Laura Rodriguez Navas <laura.rodriguez.navas@upc.edu>"""

G = nx.complete_graph(5)

k5 = nx
G.add_edges_from(k5.edges)
c = list(nx.k_clique_communities(G, 6))

print(G.adjacency_list())

nx.draw(G, with_labels=True)
plt.show()
