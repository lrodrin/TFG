import pydot

callgraph = pydot.Dot(graph_type='digraph', fontname="Verdana", compound='true')

cluster_foo = pydot.Cluster('foo', label='foo')
callgraph.add_subgraph(cluster_foo)

node_foo = pydot.Node('foo_method_1', label='method_1')
cluster_foo.add_node(node_foo)

cluster_bar = pydot.Cluster('bar', label='Component1')
callgraph.add_subgraph(cluster_bar)

node_bar = pydot.Node('bar_method_a')
cluster_bar.add_node(node_bar)

callgraph.add_edge(pydot.Edge(node_foo, node_bar, ltail=cluster_foo.get_name(), lhead=cluster_bar.get_name()))

callgraph.write('graphviz_5.dot')
