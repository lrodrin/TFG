import networkx as nx

clansList = [{'E'}, {'B'}, {'A'}, {'C'}, {'D'}, {'E', 'D'}, {'E', 'A', 'D'}, {'E', 'B', 'A', 'D'},
             {'E', 'B', 'A', 'C', 'D'}]

G = nx.DiGraph()
G.add_node(frozenset(clansList[len(clansList) - 1]))

G.add_edge(frozenset(clansList[len(clansList) - 1]), frozenset(clansList[7]))
G.add_edge(frozenset(clansList[len(clansList) - 1]), frozenset(clansList[3]))

G.add_edge(frozenset(clansList[7]), frozenset(clansList[6]))
G.add_edge(frozenset(clansList[7]), frozenset(clansList[1]))


G.add_edge(frozenset(clansList[6]), frozenset(clansList[5]))
G.add_edge(frozenset(clansList[6]), frozenset(clansList[2]))

G.add_edge(frozenset(clansList[5]), frozenset(clansList[0]))
G.add_edge(frozenset(clansList[5]), frozenset(clansList[4]))

# write dot file to use with graphviz
nx.nx_pydot.write_dot(G, 'graphviz.dot')
