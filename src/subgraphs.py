import itertools
import networkx as nx
from matplotlib import pyplot as plt

__author__ = "\"Laura Rodriguez Navas <laura.rodriguez.navas@upc.edu>"""

g = nx.Graph()
g.add_edge(1, 2)
g.add_edge(1, 3)
g.add_edge(1, 7)
g.add_edge(2, 4)
g.add_edge(3, 4)
g.add_edge(3, 5)
g.add_edge(3, 6)
g.add_edge(4, 5)
g.add_edge(5, 6)
g.add_edge(6, 7)

nx.draw(g)
plt.show()

target = nx.Graph()
target.add_edge(1, 2)
target.add_edge(2, 3)

l = []
for sub_nodes in itertools.combinations(g.nodes(), len(target.nodes())):
    subg = g.subgraph(sub_nodes)
    if nx.is_connected(subg) and nx.is_isomorphic(subg, target):
        print(subg.edges())
        l.append(sub_nodes)

nx.draw(target, edge_list=l, with_labels=nx.spring_layout(target))
plt.show()