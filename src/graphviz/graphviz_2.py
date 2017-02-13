import pydot

node1 = pydot.Node(1)
node2 = pydot.Node(2)
node3 = pydot.Node(3)
node4 = pydot.Node(4)

P = pydot.Dot()
P.add_edge(pydot.Edge(node1, node2))
P.add_edge(pydot.Edge(node2, node3))
P.add_edge(pydot.Edge(node1, node4))

S = pydot.Subgraph(rank='same')
S.add_node(node3)
S.add_node(node4)
P.add_subgraph(S)
P.write('graphviz_2.dot')