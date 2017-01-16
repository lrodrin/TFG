import matplotlib.pyplot as plt
import networkx as nx
import community as community

__author__ = "\"Laura Rodriguez Navas <laura.rodriguez.navas@upc.edu>"""

# Graph generator
G = nx.random_graphs.powerlaw_cluster_graph(300, 1, .4)

# Drawing
part = community.best_partition(G)
values = [part.get(node) for node in G.nodes()]

nx.draw_spring(G, cmap=plt.get_cmap('jet'), node_color=values, node_size=30, with_labels=False)
mod = community.modularity(part, G)
print("modularity:", mod)
