import networkx as nx

__author__ = "\"Laura Rodriguez Navas <laura.rodriguez.navas@upc.edu>"""

e = [(1, 2), (1, 3), (2, 3), (2, 4), (3, 4), (3, 5), (3, 6), (4, 5), (4, 6), (5, 6), (7, 8)]
G = nx.Graph(e)
G.add_node(9)

# Return the clique number (size of the largest clique) for graph
print(nx.graph_clique_number(G))

# Returns the number of maximal cliques for each node
print(nx.number_of_cliques(G))
