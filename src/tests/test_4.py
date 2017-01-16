import networkx as nx
from community import best_partition
from matplotlib import pyplot as plt

__author__ = "\"Laura Rodriguez Navas <laura.rodriguez.navas@upc.edu>"""


# Graph generator
G = nx.random_graphs.powerlaw_cluster_graph(300, 1, .4)

# Drawing
part = best_partition(G)
values = [part.getColor(node) for node in G.nodes()]

nx.draw_spring(G, cmap=plt.get_cmap('jet'), node_color=values, node_size=30, with_labels=False)
plt.show()