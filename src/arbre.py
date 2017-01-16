import collections
import json

import networkx as nx

__author__ = "\"Laura Rodriguez Navas <laura.rodriguez.navas@upc.edu>"""


def construct_trees(edges):
    """Given a list of edges [child, parent], return trees. """
    trees = collections.defaultdict(dict)

    for child, parent in edges:
        trees[parent][child] = trees[child]

    # Find roots
    children, parents = zip(*edges)
    roots = set(parents).difference(children)

    return {root: trees[root] for root in roots}


if __name__ == '__main__':
    G = nx.Graph()  # Create an empty graph structure (a “null graph”) with no nodes and no edges

    # Adding edges and edges attributes
    G.add_edges_from([('A', 'B'), ('B', 'D'), ('B', 'E'), ('D', 'E')], color='red')
    G.add_edges_from([('A', 'C'), ('B', 'C'), ('C', 'D'), ('C', 'E')], color='black')
    G.add_edges_from([('A', 'D'), ('A', 'E')], color='blue')
    print(json.dumps(construct_trees(G.edges()), indent=1))
