__author__ = "\"Laura Rodriguez Navas <laura.rodriguez.navas@upc.edu>"""


graph = {"a": ["c"],
         "b": ["c", "e"],
         "c": ["a", "b", "d", "e"],
         "d": ["c"],
         "e": ["c", "b"],
         "f": []
         }


def generate_edges(g):
    """ returns a list of all nodes """
    edges = []
    for node in g:
        for neighbour in g[node]:
            edges.append((node, neighbour))

    return edges


print(generate_edges(graph))


def find_isolated_nodes(g):
    """ returns a list of isolated nodes """
    isolated = []
    for node in g:
        if not g[node]:
            isolated += node
    return isolated


print(find_isolated_nodes(graph))
