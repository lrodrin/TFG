"""
This module implements the DOT file creation

Copyright (c) 2016-2017 Laura Rodriguez Navas <laura.rodriguez.navas@upc.edu>

Distributed under MIT license
[https://opensource.org/licenses/MIT]
"""
import pydot

import src.final.Clan as c

__author__ = 'Laura Rodriguez Navas'
__license__ = 'MIT'

clansList = [{'A'}, {'B'}, {'D'}, {'C'}, {'E'}, {'E', 'D'}, {'A', 'D', 'E'}, {'A', 'B', 'D', 'E'},
             {'A', 'B', 'D', 'C', 'E'}]  # List of clans
external, internal = c.Clan.listClansDivision(clansList)

callgraph = pydot.Dot(graph_type='digraph', compound=True)

# nodes
for e in external:
    callgraph.add_node(pydot.Node("".join(e)))

i = len(internal) - 1
j = i - 1
while i >= 0:
    clusterName = pydot.Cluster("".join(internal[i]))
    subgraph = pydot.Subgraph(rank="same")
    if i != 0:
        clusterName.add_node(pydot.Node("s_%s" % "".join(internal[j]), label=" ", fillcolor="white", fixedsize=True,
                                        width=0.2))
        clusterName.add_node(pydot.Node("s_%s" % "".join(internal[i].difference(internal[j])), label=" ",
                                        fillcolor="white", fixedsize=True, width=0.2))
        subgraph.add_edge(
            pydot.Edge("s_%s" % "".join(internal[i].difference(internal[j])), "s_%s" % "".join(internal[j]),
                       arrowhead="none"))
    else:
        internal_i_aux = internal[i].copy()
        internal_i_aux2 = internal[i].copy()
        clusterName.add_node(
            pydot.Node("s_%s" % "".join(internal_i_aux.pop()), label=" ", fillcolor="white", fixedsize=True, width=0.2))
        clusterName.add_node(
            pydot.Node("s_%s" % "".join(internal_i_aux), label=" ", fillcolor="white", fixedsize=True, width=0.2))
        subgraph.add_edge(
            pydot.Edge("s_%s" % "".join(internal_i_aux2.pop()), "s_%s" % "".join(internal_i_aux2), arrowhead="none"))

    clusterName.add_subgraph(subgraph)
    callgraph.add_subgraph(clusterName)
    i -= 1
    j -= 1

# links
for e in external:
    callgraph.add_edge(pydot.Edge("s_%s" % "".join(e), "".join(e), arrowhead="none"))

i = len(internal) - 2
j = i - 1
while i >= 0:
    if i != 0:
        callgraph.add_edge(pydot.Edge("s_%s" % "".join(internal[i]), "s_%s" % "".join(internal[j]), arrowhead="none",
                                      lhead="cluster_%s" % "".join(internal[i])))
    else:
        internal_i_aux = internal[i].copy()
        callgraph.add_edge(
            pydot.Edge("s_%s" % "".join(internal[i]), "s_%s" % "".join(internal[i].pop()), arrowhead="none",
                       lhead="cluster_%s" % "".join(internal_i_aux)))
    i -= 1
    j -= 1

callgraph.write('dot_file_creation.dot')
