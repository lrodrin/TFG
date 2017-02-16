"""
This module implements the Estructura class

Copyright (c) 2016-2017 Laura Rodriguez Navas <laura.rodriguez.navas@upc.edu>

Distributed under MIT license
[https://opensource.org/licenses/MIT]
"""
from collections import defaultdict

import pydot
import src.final.Clan as c

__author__ = 'Laura Rodriguez Navas'
__license__ = 'MIT'


# TODO com tractar els colors

class Estructura(object):
    @staticmethod
    def create_2structure(primalsList, graphEdgesAtributtes, primalsDict):
        """
            Create a 2-structure from a list of clans

        :param graphEdgesAtributtes: List of edges atributtes from a Graph
        :param primalsList: List of clans
        :type primalsList: list of sets
        :return: DOT file
        """
        external, internal = c.Clan.listClansDivision(primalsList)  # primalsList divided into two lists
        callgraph = pydot.Dot(graph_type='digraph', compound=True)

        # creating nodes
        for value in primalsDict.values():  # For each primal clan that len() == 1
            for elem in value:
                if len(elem) == 1:
                    callgraph.add_node(pydot.Node("".join(elem)))  # Add external nodes to file

        # creating subgraphs
        # for x in combinations....
        # i = len(internal) - 1
        # j = i - 1
        # while i >= 0:  # Run list of clans in reverse mode
        #     cluster = pydot.Cluster("".join(internal[i]))  # Create a cluster cluster
        #     internalSubgraph = pydot.Subgraph(rank="same")  # Create a subgraph from cluster cluster
        #     diff = sorted(internal[i].difference(internal[j]))
        #     # diff = "".join(internal[i].difference(internal[j]))
        #     if i != 0:
        #         cluster.add_node(
        #             pydot.Node("s_%s" % "".join(internal[j]), label=" ", fillcolor="white", fixedsize=True,
        #                        width=0.2))  # Add actual node/clan to cluster
        #         cluster.add_node(pydot.Node("s_%s" % "".join(diff), label=" ",
        #                                     fillcolor="white", fixedsize=True, width=0.2))  # Add actual node/clan
        #         # difference from internal actual clan and internal previous clan to cluster
        #         internalSubgraph.add_edge(
        #             pydot.Edge("s_%s" % "".join(diff), "s_%s" % "".join(internal[j]),
        #                        arrowhead="none", color=Estructura.getColor(graphEdgesAtributtes, diff)))
        #         # Add edge from second node/clan to first node/clan in internalSubgraph difference from
        #         # internal actual clan and internal previous clan to cluster
        #     else:  # Last iteration
        #         internal_i_aux = internal[i].copy()  # Copy from actual clan
        #         internal_i_aux2 = internal[i].copy()  # A sedcond copy from actual clan
        #         # Add nodes for each element from the last clan in internals
        #         cluster.add_node(
        #             pydot.Node("s_%s" % "".join(internal_i_aux.pop()), label=" ", fillcolor="white", fixedsize=True,
        #                        width=0.2))
        #         cluster.add_node(
        #             pydot.Node("s_%s" % "".join(internal_i_aux), label=" ", fillcolor="white", fixedsize=True,
        #                        width=0.2))
        #         # Add edge for nodes from the last clan in internals
        #         internalSubgraph.add_edge(
        #             pydot.Edge("s_%s" % "".join(internal_i_aux2.pop()), "s_%s" % "".join(internal_i_aux2),
        #                        arrowhead="none",
        #                        color=Estructura.getColor(graphEdgesAtributtes, "".join(internal_i_aux2))))
        #
        #     cluster.add_subgraph(internalSubgraph)  # Add subgraph to cluster
        #     callgraph.add_subgraph(cluster)  # Add cluster to file
        #     i -= 1
        #     j -= 1

        # creating links for nodes and subgraphs
        for value in primalsDict.values():  # For each primal clan that len() == 1
            for elem in value:
                if len(elem) == 1:
                    callgraph.add_edge(
                        pydot.Edge("s_%s" % "".join(elem), "".join(elem), arrowhead="none"))

        i = len(internal) - 2
        j = i - 1
        while i >= 0:  # Run list of clans in reverse mode
            if i != 0:
                # Add edge from internal node/clan in subgraph to cluster
                callgraph.add_edge(
                    pydot.Edge("s_%s" % "".join(internal[i]), "s_%s" % "".join(internal[j]), arrowhead="none",
                               lhead="cluster_%s" % "".join(internal[i])))
            else:
                # Add the last edge from internal node/clan in subgraph to cluster
                internal_i_aux = internal[i].copy()  # Copy from actual clan
                callgraph.add_edge(
                    pydot.Edge("s_%s" % "".join(internal[i]), "s_%s" % "".join(internal[i].pop()), arrowhead="none",
                               lhead="cluster_%s" % "".join(internal_i_aux)))
            i -= 1
            j -= 1

        callgraph.write('Estructura.dot')  # Write a DOT file with previous information

    @staticmethod
    def getColor(graphEdgesAtributtes, clan1, clan2):
        for k, v in graphEdgesAtributtes.items():
            if (k[0] in clan1 and k[1] in clan2) or (k[1] in clan1 and k[0] in clan2):
                return v

    @staticmethod
    def nose(primalsList):
        d = defaultdict(list)
        for i in range(len(primalsList) - 1, 0, -1):
            for j in range(i - 1, -1, -1):
                if primalsList[j].issubset(primalsList[i]):
                    for k in range(j + 1, i):
                        if primalsList[k].issubset(primalsList[i]) and primalsList[j].issubset(primalsList[k]):
                            break
                    else:
                        d[frozenset(primalsList[i])].append(primalsList[j])
        return d
