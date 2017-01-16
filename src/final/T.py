"""
This module implements the T class

Copyright (c) 2016-2017 Laura Rodriguez Navas <laura.rodriguez.navas@upc.edu>

Distributed under MIT license
[https://opensource.org/licenses/MIT]
"""
import pydot
import src.final.Clan as c

__author__ = 'Laura Rodriguez Navas'
__license__ = 'MIT'


class T(object):
    @staticmethod
    def createTestructure(clansList):
        """
            Create a T-strcuture from a list of clans

        :param clansList: List of clans
        :type clansList: list of sets
        :return: DOT file
        """
        external, internal = c.Clan.division(clansList)

        callgraph = pydot.Dot(graph_type='digraph', compound=True)

        # creating nodes
        for external_nodes in external:  # For each clan that len() == 1
            callgraph.add_node(pydot.Node("".join(external_nodes)))  # Add external node to file

        # creating subgraphs
        i = len(internal) - 1
        j = i - 1
        while i >= 0:  # Run list of clans in reverse mode
            cluster = pydot.Cluster("".join(internal[i]))  # Create a cluster cluster
            internalSubgraph = pydot.Subgraph(rank="same")  # Create a subgraph from cluster cluster
            if i != 0:
                cluster.add_node(
                    pydot.Node("s_%s" % "".join(internal[j]), label=" ", fillcolor="white", fixedsize=True,
                               width=0.2))  # Add actual node/clan to cluster
                cluster.add_node(pydot.Node("s_%s" % "".join(internal[i].difference(internal[j])), label=" ",
                                            fillcolor="white", fixedsize=True, width=0.2))  # Add actual node/clan
                # difference from internal actual clan and internal previous clan to cluster
                internalSubgraph.add_edge(
                    pydot.Edge("s_%s" % "".join(internal[i].difference(internal[j])), "s_%s" % "".join(internal[j]),
                               arrowhead="none"))  # Add edge from second node/clan to first node/clan in
                # internalSubgraph difference from internal actual clan and internal previous clan to cluster
            else:  # Last iteration
                internal_i_aux = internal[i].copy()  # Copy from actual clan
                internal_i_aux2 = internal[i].copy()  # A sedcond copy from actual clan
                # Add nodes for each element from the last clan in internals
                cluster.add_node(
                    pydot.Node("s_%s" % "".join(internal_i_aux.pop()), label=" ", fillcolor="white", fixedsize=True,
                               width=0.2))
                cluster.add_node(
                    pydot.Node("s_%s" % "".join(internal_i_aux), label=" ", fillcolor="white", fixedsize=True,
                               width=0.2))
                # Add edge for nodes from the last clan in internals
                internalSubgraph.add_edge(
                    pydot.Edge("s_%s" % "".join(internal_i_aux2.pop()), "s_%s" % "".join(internal_i_aux2),
                               arrowhead="none"))

            cluster.add_subgraph(internalSubgraph)  # Add subgraph to cluster
            callgraph.add_subgraph(cluster)  # Add cluster to file
            i -= 1
            j -= 1

        # creating links for nodes and subgraphs
        for external_nodes in external:  # For each clan that len() == 1
            callgraph.add_edge(pydot.Edge("s_%s" % "".join(external_nodes), "".join(external_nodes), arrowhead="none"))
            # Add edge from subgraph node/clan to external node/clan

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

        callgraph.write('T.dot')  # Write a DOT file with previous information
