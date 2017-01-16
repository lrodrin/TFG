import matplotlib.pyplot as plt
import networkx as nx
import community

__author__ = "\"Laura Rodriguez Navas <laura.rodriguez.navas@upc.edu>"""

G = nx.erdos_renyi_graph(30, 0.05)

# First compute the best partition
partition = community.best_partition(G)

# Drawing
size = float(len(set(partition.values())))
pos = nx.spring_layout(G)
count = 0.
for com in set(partition.values()):
    count += 1.
    list_nodes = [nodes for nodes in partition.keys()
                  if partition[nodes] == com]
    nx.draw_networkx_nodes(G, pos, list_nodes, node_size=20,
                           node_color=str(count / size))

nx.draw_networkx_edges(G, pos, alpha=0.5)
plt.show()