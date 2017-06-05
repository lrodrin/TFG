"""
This module implements the Structure class

Copyright (c) 2016-2017 Laura Rodriguez Navas <laura.rodriguez.navas@upc.edu>

Distributed under MIT license
[https://opensource.org/licenses/MIT]
"""
from collections import OrderedDict

import pydotplus

from src.extension.Clan import *
from src.extension.Graph import *

__author__ = 'Laura Rodriguez Navas'
__license__ = 'MIT'


class Structure:
    @staticmethod
    def createGraphvizStructure(colorEdgesAtributtes, styleEdgesAtributtes, primalClansDict, structureName):
        """
        Create a 2-structure from a dictionary of primal clans specified by primalClansDict

        :param colorEdgesAtributtes: Color edges atributtes from a graph
        :param styleEdgesAtributtes: Style edges atributtes from a graph
        :param primalClansDict: Dictionary of primal clans
        :param structureName: Dot file name
        :type colorEdgesAtributtes: dict
        :type styleEdgesAtributtes: dict
        :type primalClansDict: dict
        :type structureName: str
        :return: A 2-structure
        """
        structure = pydotplus.graphviz.Dot(strict=True, graph_type="digraph", graph_name=structureName[:-4],
                                           compound="true",
                                           fontname="Verdana",
                                           fontsize=12, newrank="true")
        structure.set_node_defaults(shape="circle")

        # Creating external nodes
        for primals in primalClansDict.values():  # For each primal clan
            for primal in primals:  # For each sub primal clan
                if len(primal) == 1:  # If primal clan is a trivial clan
                    # if not structure.get_node("".join(primal)):
                    # Exclude the repetitive nodes
                    structure.add_node(pydotplus.graphviz.Node("".join(primal)))  # Add node to structure

        # Creating clusters
        for key, values in primalClansDict.items():  # For each primal clan and their sub primal clans
            if len(values) == 2:  # Primitive structure
                cluster = pydotplus.graphviz.Cluster("".join(key), rank="same")  # Create a cluster
            else:
                cluster = pydotplus.graphviz.Cluster("".join(key))  # Create a cluster

            cluster.set_node_defaults(shape="point")

            if len(values) <= 10:
                # Creating edges and nodes inside the cluster
                for primalClan1, primalClan2 in combinations(values, 2):
                    u = "s_%s" % "".join(primalClan1)
                    v = "s_%s" % "".join(primalClan2)
                    if u != v:  # If node cycle not exists
                        edge = pydotplus.graphviz.Edge(u, v, color=Clan.getColorClans(colorEdgesAtributtes, primalClan1,
                                                                                      primalClan2),
                                                       style=Clan.getStyleClans(styleEdgesAtributtes, primalClan1,
                                                                                primalClan2),
                                                       arrowhead="none")

                    if not cluster.get_edge(edge):  # If edge not exists and node cycle also not exists
                        cluster.add_edge(edge)  # Add edge to cluster

            else:
                # Creating nodes inside the cluster
                for primals in primalClansDict.values():  # For each primal clan
                    for primal in primals:  # For each sub primal clan
                        node = pydotplus.graphviz.Node("s_%s" % "".join(primal))
                        if not cluster.get_node(node):  # If edge not exists and node cycle also not exists
                            cluster.add_node(node)  # Add edge to cluster

            structure.add_subgraph(cluster)  # Add cluster to structure

        # Creating external edges
        for values in primalClansDict.values():  # For each sub primal clans
            for primal in values:  # For each sub primal clan
                u = "s_%s" % "".join(primal)
                if primalClansDict.get(frozenset(primal)):  # If primal exists as a key in primalClansDict
                    v = "s_%s" % "".join(primalClansDict.get(frozenset(primal))[0])
                    edge = pydotplus.graphviz.Edge(u, v, lhead="cluster%s" % "".join(u[1:]), arrowhead="none")

                else:  # If primal not exists as a key in primalClansDict
                    v = "".join(primal)
                    edge = pydotplus.graphviz.Edge(u, v, arrowhead="none")

                structure.add_edge(edge)  # Add edge to structure

        structure.write(structureName)  # Write a Dot file with all previous information
        print("A %s was created" % structureName)

    @staticmethod
    def decomposition(graph):
        """
        Decomposition of graph in primal clans

        :param graph: Networkx's graph
        :type graph: nx.Graph
        :return: The edges atributtes from graph and primal clans ordered
        :rtype: dict, dict
        """
        clansList = Clan.clans(graph, graph.nodes())  # List of clans
        primalClansList = Clan.primalClans(clansList)  # List of primal clans
        colorEdgesAtributtes = Graph.getColorAttributesFromGraph(graph)  # Color edges atributtes from graph
        styleEdgesAtributtes = Graph.getStyleAttributesFromGraph(graph)  # Style edges atributtes from graph
        primalClansDict = OrderedDict(reversed(sorted(Clan.primalClansDict(primalClansList).items(),
                                                      key=lambda t: len(t[0]))))  # Dictionary of primal clans
        # sorted in reverse mode by primal clans length
        return colorEdgesAtributtes, styleEdgesAtributtes, primalClansDict

    @staticmethod
    def frequentDecomposition(graph, moreFrequentSubsets):
        """
        Decomposition of graph in primal clans

        :param graph: Networkx's graph
        :param moreFrequentSubsets: More frequents nodes from graph
        :type graph: nx.Graph
        :type moreFrequentSubsets: list
        :return: The edges atributtes from graph and primal clans ordered
        :rtype: dict, dict
        """
        clansList = Clan.frequentClans(moreFrequentSubsets)  # List of more frequent clans
        primalClansList = Clan.primalClans(clansList)  # List of more frequent primal clans
        colorEdgesAtributtes = Graph.getColorAttributesFromGraph(graph)  # Color edges atributtes from graph
        styleEdgesAtributtes = Graph.getStyleAttributesFromGraph(graph)  # Style edges atributtes from graph
        primalClansDict = OrderedDict(reversed(sorted(Clan.primalClansDict(primalClansList).items(),
                                                      key=lambda t: len(t[0]))))  # Dictionary of more frequent
        # primal clans sorted in reverse mode by primal clans length
        return colorEdgesAtributtes, styleEdgesAtributtes, primalClansDict

    @staticmethod
    def create2Structure(graph, filename):
        """
        Create a 2-structure from a type of graph

        :param graph: Networkx's graph
        :param filename: Dot file name
        :type graph: nx.Graph
        :type filename: str
        :return: A 2-structure
        """
        colorEdgesAtributtes, styleEdgesAtributtes, primalClansDict = Structure.decomposition(graph)  # Graph
        # decomposition
        Structure.createGraphvizStructure(colorEdgesAtributtes, styleEdgesAtributtes, primalClansDict, filename)  #
        # Create 2-structure

    @staticmethod
    def createFrequent2Structure(graph, filename, moreFrequentSubsets):
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
        colorEdgesAtributtes, styleEdgesAtributtes, primalClansDict = Structure.frequentDecomposition(graph,
                                                                                                      moreFrequentSubsets)
        # Graph decomposition
        Structure.createGraphvizStructure(colorEdgesAtributtes, styleEdgesAtributtes, primalClansDict, filename)
        # Create 2-structure
