import networkx as nx

__author__ = "\"Laura Rodriguez Navas <laura.rodriguez.navas@upc.edu>"""

G = nx.Graph()  # Create an empty graph structure (a “null graph”) with no nodes and no edges

# Adding edges and edges attributes
G.add_edges_from([('A', 'B'), ('B', 'D'), ('B', 'E'), ('D', 'E')], color='red')
G.add_edges_from([('A', 'C'), ('B', 'C'), ('C', 'D'), ('C', 'E')], color='black')
G.add_edges_from([('A', 'D'), ('A', 'E')], color='blue')

nx.nx_pydot.write_dot(G, 'write_dot.dot')    # Return a pydot graph from G.