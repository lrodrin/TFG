import random

import networkx as nx
from matplotlib import pyplot as plt

__author__ = "\"Laura Rodriguez Navas <laura.rodriguez.navas@upc.edu>"""

# Data input
n = int(input("Please enter a number of nodes: "))
p = float(input("Please enter a probability for the creation of edges: "))
c = int(input("Please enter a number of colors: "))

# Verifying data input
colors_list = ['blue', 'green', 'red', 'cyan', 'magenta', 'yellow', 'black', 'white']

if c > len(colors_list):
    print("Ups! It is not a valid number. The number of colors may not be greater than 7! Try it again ...")
    c = int(input("Please enter a number of colors: "))

# Graph generator
G = nx.erdos_renyi_graph(n, p)

# For each edge of graph the color attribute is assigned randomly
for (u, v) in G.edges():
    G.edge[u][v]['color'] = random.choice(colors_list[0:c])

# Color sequence with the same length as graph.edges()
edge_color_list = [G[u][v]['color'] for (u, v) in G.edges()]

# Drawing with the color sequence
# nx.draw(graph, edge_color=edge_color_list)
# plt.suptitle("Erdös-Rényi Graph with color sequence", fontsize=11)
nx.draw(G, edge_color=edge_color_list, with_labels=nx.spring_layout(G))
plt.suptitle("Erdös-Rényi Graph with color sequence and labels", fontsize=11)
plt.show()

nx.nx_pydot.write_dot(G, 'erdos_renyi_colors.dot')
