"""
This module implements the Structure class

Copyright (c) 2016-2017 Laura Rodriguez Navas <laura.rodriguez.navas@upc.edu>

Distributed under MIT license
[https://opensource.org/licenses/MIT]
"""
from collections import OrderedDict

import pydot

from src.final.Clan import *
from src.final.Graph import *

__author__ = 'Laura Rodriguez Navas'
__license__ = 'MIT'


class Structure:
    @staticmethod
    def createGraphvizStructure(edgesAtributtes, primalClansDict, structureName):
        """
        Create a 2-structure from a dictionary of primal clans specified by primalClansDict

        :param edgesAtributtes: Edges atributtes from a graph
        :param primalClansDict: Dictionary of primal clans
        :param structureName: Dot file name
        :type edgesAtributtes: dict
        :type primalClansDict: dict
        :type structureName: str
        :return: A 2-structure
        """
        callgraph = pydot.Dot(graph_type='digraph', compound=True)

        # creating an external nodes
        for value in primalClansDict.values():  # For each primal clan
            for elem in value:
                if len(elem) == 1:  # If len(primal clan) == 1
                    if not callgraph.get_node("".join(elem)):
                        callgraph.add_node(pydot.Node("".join(elem)))  # Add primal clan value as a node

        # creating subgraphs
        for key, value in primalClansDict.items():  # For each primal clan
            cluster = pydot.Cluster("".join(key))  # Create a cluster
            subgraph = pydot.Subgraph(rank="same")  # Create a subgraph into cluster
            for elem in value:
                cluster.add_node(pydot.Node("s_%s" % "".join(elem), label=" ", fillcolor="white",
                                            fixedsize=True, width=0.2))  # Add primal clan as a node into cluster

            for pair in itertools.combinations(value, 2):  # For each pair primal clan combinations
                subgraph.add_edge(pydot.Edge("s_%s" % "".join(pair[0]), "s_%s" % "".join(pair[1]), arrowhead="none",
                                             color=Clan.getColorClans(edgesAtributtes, pair[0], pair[1])))
                #  Add edge into subgraph
            cluster.add_subgraph(subgraph)  # Add subgraph to cluster
            callgraph.add_subgraph(cluster)  # Add cluster

        # creating edge links for nodes and subgraphs
        for value in primalClansDict.values():  # For each primal clan
            for elem in value:
                if len(elem) == 1:  # If len(primal clan) == 1
                    callgraph.add_edge(
                        pydot.Edge("s_%s" % "".join(elem), "".join(elem), arrowhead="none"))  # Add primal clan
                    # value as a edge

        for i, (key, value) in enumerate(primalClansDict.items()):  # For each primal clan
            if i != 0:  # If not the first primal clan in primalClansDict
                callgraph.add_edge(pydot.Edge("s_%s" % "".join(key), "s_%s" % "".join(value[0]),
                                              arrowhead="none", lhead="cluster_%s" % "".join(key)))  # Add primal clan
                # value as a edge

        callgraph.write(structureName)  # Write a Dot file with all previous information
        print("A %s was created" % structureName)

    @staticmethod
    def decomposition(graph, moreFrequentSubsets):
        """
        Decomposition of graph in primal clans

        :param graph: Networkx's graph
        :param moreFrequentSubsets: More frequents nodes from graph
        :type graph: nx.Graph
        :type moreFrequentSubsets: list
        :return: The edges atributtes from graph and primal clans ordered
        :rtype: dict, dict
        """
        # clansList = Clan.clans(graph, graph.nodes())  # List of clans
        clansList = Clan.frequentClans(graph, moreFrequentSubsets)  # List of clans
        primalClansList = Clan.primalClans(clansList)  # List of primal clans
        EdgesAtributtes = Graph.getColorAttributesFromGraph(graph)  # Edges atributtes from graph
        primalClansDict = OrderedDict(reversed(sorted(Clan.primalClansDict(primalClansList).items(),
                                                      key=lambda t: len(t[0]))))  # Dictionary of primal clans
        # sorted in reverse mode by primal clans length
        return EdgesAtributtes, primalClansDict

    @staticmethod
    def create2Structure(graph, filename, moreFrequentSubsets):
        """
        Create a 2-structure from a type of graph

        :param graph: Networkx's graph
        :param filename: Dot file name
        :param moreFrequentSubsets: More frequents nodes from graph
        :type graph: nx.Graph
        :type filename: str
        :type moreFrequentSubsets: list
        :return: A 2-structure
        """
        EdgesAtributtes, primalClansDict = Structure.decomposition(graph, moreFrequentSubsets)  # Graph decomposition
        Structure.createGraphvizStructure(EdgesAtributtes, primalClansDict, filename)  # Create 2-structure
