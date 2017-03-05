import random
import networkx as nx
from matplotlib import pyplot as plt

__author__ = "\"Laura Rodriguez Navas <laura.rodriguez.navas@upc.edu>"""

# Data input
n = int(input("Please enter a number of nodes: "))
p = float(input("Please enter a probability for the creation of edges: "))
c = int(input("Please enter a number of colors: "))

# Verifying data input
colors_list = 'bgrcmyk'
if c > len(colors_list):
    print("Ups! It is not a valid number. The number of colors may not be greater than 7! Try it again ...")
    c = int(input("Please enter a number of colors: "))

# Graph generator
G = nx.erdos_renyi_graph(n, p)

edge_labels = dict()

# For each edge of graph the color attribute is assigned randomly
for (u, v) in G.edges():
    G.edge[u][v]['color'] = random.choice(colors_list[0:c])
    edge_labels[(u, v)] = G.edge[u][v]['color']  # Label the edges with the selected color attribute

# Color sequence with the same length as graph.edges()
edge_color_list = [G[u][v]['color'] for (u, v) in G.edges()]

pos = nx.spring_layout(G)  # Establish the positions of nodes / edges / labels

# Drawing with the color sequence
nx.draw_networkx(G, pos=pos, edge_color=edge_color_list)  # Draw it all without labels
nx.draw_networkx_edge_labels(G, pos=pos, edge_labels=edge_labels)
plt.suptitle("Erdös-Rényi Graph with color sequence and labels", fontsize=11)
plt.axis('off')
plt.show()
