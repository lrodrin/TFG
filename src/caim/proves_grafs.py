from math import log

import networkx as nx
import numpy as np
from matplotlib import pyplot as plt


def drange(start, stop, step):
    r = start
    while r < stop:
        yield r
        r *= step


nodes = range(2, 50)
mitjanes = []

# Erdos-renyi
for nnodes in nodes:
    p = log(nnodes) / nnodes
    # graph = nx.erdos_renyi_graph(nnodes, p)
    # graph = nx.fast_gnp_random_graph(nodes, p)
    d = nx.floyd_warshall(nx.erdos_renyi_graph(nnodes, p))
    l = []
    for v in d:
        l.extend([x for x in d[v].values() if x > 0])
    mitjanes.append(2 * (sum(l)) / (nnodes * (nnodes - 1)))

plt.plot(nodes, mitjanes, 'ro', linewidth=2.0)
plt.xlabel('Number of nodes')
plt.ylabel('Average Shortets Path')
plt.show()

# Watts-Strongatz
G = nx.Graph()
mitjanes = []
clustering = []
probabilitat = drange(0.0001, 1.1, 10)
probabilitat = [0.0001, 0.0005, 0.001, 0.005, 0.01, 0.05, 0.1, 0.133, 0.166, 0.2, 0.233, 0.266, 0.3, 0.433, 0.466, 0.5,
                0.533, 0.566, 0.6, 0.633, 0.666, 0.7, 0.733, 0.766, 0.8, 0.833, 0.866, 0.9, 0.933, 0.966, 1.]
nnodes = 200
mitjanesMillorades = []
clusteringMillorat = []

for p in probabilitat:
    G = nx.watts_strogatz_graph(nnodes, 4, p)
    c = nx.floyd_warshall(G)
    clustering.append(nx.transitivity(G))
    l = []
    for v in c:
        l.extend([x for x in c[v].values() if x > 0])
    mitjanes.append(2 * (sum(l)) / (nnodes * (nnodes - 1)))

for mitja in mitjanes:
    mitjanesMillorades.append(mitja / mitjanes[0])

for c in clustering:
    clusteringMillorat.append(c / clustering[0])

# print probs
# print mitjanesMillorades
# print clusteringMillorat

# plt.plot(probs, mitjanesMillorades, 'ro')
# plt.plot(probs, clusteringMillorat, 'ro')
plt.plot(probabilitat, mitjanesMillorades, 'b-', probabilitat, clusteringMillorat, 'g-')
plt.xlabel('Probability')
plt.ylabel('Average Shortets Path/Clustering')
plt.show()

# afegim un node
G.add_node(1)

# afegim mes nodes
G.add_nodes_from([2, 3])
G.add_nodes_from(range(100, 110))

# afegim una aresta
G.add_edge(1, 2)
nx.draw_networkx(G)
plt.title('Graf graph - nodes [2,3,100-110] - arestes[2,3]')
plt.show()

# afegim mes arestes
G.add_edges_from([(1, 3), (2, 3)])
H = nx.Graph()
H.add_path([100, 101, 102, 103, 104, 105, 106, 107, 108, 109])
G.add_edges_from(H.edges())
nx.draw_networkx(G)
plt.title('Graf graph - afegim arestes')
plt.show()

# atributs dels grafs, nodes i arestes
lt = [chr(x) for x in range(ord('a'), ord('z') + 1)]
D = nx.Graph()
D.add_nodes_from(lt)
nx.draw_networkx(D)
plt.title("Graf D - nodes ['a','z']")
plt.show()
nx.draw_networkx(D, node_size=500, node_color="lightgray")  # node_size per defecte=300
plt.title("Graf D - canviem mida i color dels nodes")
plt.show()
a = np.random.choice(lt, 30, replace=True)
D.add_edges_from([(a[i], a[i + 1]) for i in range(0, len(a) - 1)])
nx.draw_networkx(D)
plt.title("Graf D - afegim 15 arestes entre nodes a values'atzar")
plt.show()

# nombre de nodes d'un graf
len(G)

# consultar els nodes d'un graf
G.nodes()

# consultar les arestes d'un graf
G.edges()

# components connexos d'un graf
H = nx.connected_component_subgraphs(G)
print(len(H), "components")
nx.draw_networkx(H[0])
plt.title("Graf H - primer component del graf graph")
plt.show()
nx.draw_networkx(H[1])
plt.title("Graf H - segon component del graf graph")
plt.show()

# guardar la imatge d'un graf
nx.draw_networkx(G)
plt.savefig('grafG.png')

# carregar un graf (p.e., a partir d'una llista d'arestes)
f = open("edges.txt", 'r')
N = nx.read_edgelist(f)
f.close()
nx.draw_networkx(N)
plt.title("Graf N - arestes llegides de fitxer")
plt.show()

# generadors de grafs
ER = nx.erdos_renyi_graph(80, .1)
nx.draw(ER)
plt.title("Graf ER - Erdos_Renyi (80,0.1)")
plt.show()

WS = nx.watts_strogatz_graph(24, 4, .3)
nx.draw(WS)
plt.title("Graf WS - Watts_Strogatz (24,4,0.3)")
plt.show()

BA = nx.barabasi_albert_graph(100, 2)
nx.draw(BA)
plt.title("Graf BA - Barabasi_Albert (100,2)")
plt.show()
