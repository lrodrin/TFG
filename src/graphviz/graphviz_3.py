import pydot


def main():
    callgraph = pydot.Dot(graph_type='digraph', fontname="Verdana")

    # Use pydot.Cluster to render boundary around subgraph
    cluster_foo = pydot.Cluster('foo', label='foo')

    # pydot.Node(name,attrib=''')
    # Assign unique name to each node, but labels can be arbitrary
    cluster_foo.add_node(pydot.Node('foo_method_1', label='method_1'))
    cluster_foo.add_node(pydot.Node('foo_method_2', label='method_2'))
    cluster_foo.add_node(pydot.Node('foo_method_3', label='method_3'))

    # in order to get node in parent graph to point to
    # subgraph, need to use Graph.add_subgraph()
    # calling Subgraph.add_parent() doesn't seem to do anything.
    callgraph.add_subgraph(cluster_foo)

    cluster_bar = pydot.Cluster('bar')
    cluster_bar.add_node(pydot.Node('bar_method_a'))
    cluster_bar.add_node(pydot.Node('bar_method_b'))
    cluster_bar.add_node(pydot.Node('bar_method_c'))
    callgraph.add_subgraph(cluster_bar)

    cluster_baz = pydot.Cluster('baz')
    cluster_baz.add_node(pydot.Node('baz_method_1'))
    cluster_baz.add_node(pydot.Node('baz_method_b'))
    cluster_baz.add_node(pydot.Node('baz_method_3'))
    cluster_baz.add_node(pydot.Node('baz_method_c'))
    callgraph.add_subgraph(cluster_baz)

    # create edge between two main nodes:
    # when creating edges, don't need to
    # predefine the nodes
    callgraph.add_edge(pydot.Edge("main", "sub"))

    # create edge to subgraph
    callgraph.add_edge(pydot.Edge("main", "bar_method_a"))

    callgraph.add_edge(pydot.Edge("bar_method_a", "bar_method_c"))
    callgraph.add_edge(pydot.Edge("bar_method_a", "foo_method_2"))

    callgraph.add_edge(pydot.Edge("foo_method_2", "baz_method_3"))

    callgraph.add_edge(pydot.Edge("bar_method_b", "foo_method_1"))
    callgraph.add_edge(pydot.Edge("bar_method_b", "foo_method_2"))
    callgraph.add_edge(pydot.Edge("baz_method_b", "baz_method_1"))

    callgraph.add_edge(pydot.Edge("foo_method_2", "foo_method_3"))
    callgraph.add_edge(pydot.Edge("bar_method_c", "baz_method_c"))
    callgraph.add_edge(pydot.Edge("bar_method_b", "baz_method_b"))

    # output:
    # write dot file, then render as png
    callgraph.write('graphviz_3.dot')


if __name__ == "__main__":
    main()
