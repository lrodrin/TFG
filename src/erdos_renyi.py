import networkx as nx
from matplotlib import pyplot as plt

__author__ = "\"Laura Rodriguez Navas <laura.rodriguez.navas@upc.edu>"""

# Data input
n = int(input("Please enter a number of nodes: "))
p = float(input("Please enter a probability for the creation of edges: "))

# Graph generator
G = nx.erdos_renyi_graph(n, p)

# Drawing
nx.draw(G)
plt.suptitle("Erdös-Rényi Graph", fontsize=11)
plt.show()
