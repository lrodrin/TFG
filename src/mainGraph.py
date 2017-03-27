import src.Graph

__author__ = "\"Laura Rodriguez Navas <laura.rodriguez.navas@upc.edu>"""

if __name__ == "__main__":
    g = {"a": ["d"],
         "b": ["c"],
         "c": ["b", "c", "d", "e"],
         "d": ["a", "c"],
         "e": ["c"],
         "f": []
         }

    graph = src.Graph.Graph(g)

    print("Vertices of initGraph:")
    print(graph.vertices())

    print("Edges of initGraph:")
    print(graph.edges())

    print("Add vertex:")
    graph.add_vertex("z")

    print("Vertices of initGraph:")
    print(graph.vertices())

    print("Add an edge:")
    graph.add_edge({"a", "z"})

    print("Vertices of initGraph:")
    print(graph.vertices())

    print("Edges of initGraph:")
    print(graph.edges())

    print('Adding an edge {"x","y"} with new vertices:')
    graph.add_edge({"x", "y"})

    print("Vertices of initGraph:")
    print(graph.vertices())

    print("Edges of initGraph:")
    print(graph.edges())
