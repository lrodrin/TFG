"""
This module implements the Estructura class

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


class Estructura:
    @staticmethod
    def create2structure(EdgesAtributtes, primalClansDict, filename):
        # TODO modificar la mida de cada cluster i els nodes
        """
        Create a 2-structure from a dictionary of primal clans specified by primalClansDict

        :param EdgesAtributtes: Edges atributtes from a graph
        :param primalClansDict: Dictionary of primal clans
        :param filename: Dot file name
        :type EdgesAtributtes: dict
        :type primalClansDict: dict
        :type filename: str
        :return: A 2-structure
        """
        callgraph = pydot.Dot(graph_type='digraph', compound=True)

        # creating an external nodes
        for value in primalClansDict.values():  # For each primal clan
            for elem in value:
                if len(elem) == 1:  # If len(primal clan) == 1
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
                                             color=Clan.getColorClans(EdgesAtributtes, pair[0], pair[1])))
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

        callgraph.write(filename)  # Write a Dot file with all previous information
        print("2-structure %s was created" % filename)

    @staticmethod
    def decomposition(graph, nodes):
        """
        Decomposition of graph in clans and primal clans

        :param graph: Networkx's graph
        :param nodes: Nodes from graph
        :type graph: nx.Graph
        :type nodes: list
        :return: The edges atributtes from graph and a dictionary of primal clans
        :rtype: dict, dict
        """
        clansList = Clan.clans(graph, nodes)  # List of clans
        primalClansList = Clan.primalClans(clansList)  # List of primal clans
        EdgesAtributtes = Graph.createDictFromGraph(graph)  # Dictionary of edges atributtes from graph
        primalClansDict = OrderedDict(reversed(sorted(Clan.primalClansDict(primalClansList).items(),
                                                      key=lambda t: len(t[0]))))  # Dictionary of primal clans
        # sorted in reverse mode by primal clans length
        return EdgesAtributtes, primalClansDict

    @staticmethod
    def plain2structure(plainGraph, nodes, filename):
        """
        Create a plain 2-structure from a plain graph specified by plainGraph

        :param plainGraph: Networkx's graph
        :param nodes: Nodes from graph
        :param filename: Dot file name
        :type plainGraph: nx.Graph
        :type nodes: list
        :type filename: str
        :return: A plain 2-structure
        """
        EdgesAtributtes, primalClansDict = Estructura.decomposition(plainGraph, nodes)  # Decomposition
        Estructura.create2structure(EdgesAtributtes, primalClansDict, filename)  # Create 2-structure

    @staticmethod
    def linear2structure(linearGraph, nodes, filename):
        """
        Create a linear 2-structure from a linear graph specified by linearGraph

        :param linearGraph: Networkx's graph
        :param nodes: Nodes from graph
        :param filename: Dot file name
        :type linearGraph: nx.Graph
        :type nodes: list
        :type filename: str
        :return: A linear 2-structure
        """
        EdgesAtributtes, primalClansDict = Estructura.decomposition(linearGraph, nodes)  # Decomposition
        Estructura.create2structure(EdgesAtributtes, primalClansDict, filename)  # Create 2-structure

    @staticmethod
    def exponential2structure(exponentialGraph, nodes, filename):
        """
        Create an exponential 2-structure from a exponential graph specified by exponentialGraph

        :param exponentialGraph: Networkx's graph
        :param nodes: Nodes from graph
        :param filename: Dot file name
        :type exponentialGraph: nx.Graph
        :type nodes: list
        :type filename: str
        :return: A exponential 2-structure
        """
        EdgesAtributtes, primalClansDict = Estructura.decomposition(exponentialGraph, nodes)  # Decomposition
        Estructura.create2structure(EdgesAtributtes, primalClansDict, filename)  # Create
        # 2-structure
