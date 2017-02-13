import networkx as nx

clansList = [{'A'}, {'B'}, {'D'}, {'C'}, {'E'}, {'E', 'D'}, {'A', 'D', 'E'}, {'A', 'B', 'D', 'E'},
             {'A', 'B', 'D', 'C', 'E'}]

primalList = [{'D', 'E'}, {'A', 'D', 'E'}, {'A', 'B', 'D', 'E'}]

G = nx.DiGraph()

for i in range(len(clansList)):
    for j in range(i + 1, len(clansList)):
        if clansList[i] < clansList[j]:
            G.add_edge(frozenset(clansList[j]), frozenset(clansList[i]))

nx.nx_pydot.write_dot(G, 'graphviz_4.dot')