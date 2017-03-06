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


# TODO modificar la mida de cada cluster "y los redondeles redondos en vez de elipticos"


class Estructura:
    @staticmethod
    def create2structure(EdgesAtributtes, primalClansDict, filename):
        """
        Create a 2-structure from a list of primal clans specified by primalClansDict

        :param EdgesAtributtes: Edges atributtes from a graph
        :param primalClansDict: List of primal clans
        :param filename: DOT file name
        :type EdgesAtributtes: dict
        :type primalClansDict: dict
        :type filename: str
        :return: A 2-structure
        :rtype: DOT file
        """
        callgraph = pydot.Dot(graph_type='digraph', compound=True)

        # creating external nodes
        for value in primalClansDict.values():  # For each primal clan values
            for elem in value:
                if len(elem) == 1:  # If primal clan value is len() == 1
                    callgraph.add_node(pydot.Node("".join(elem)))  # Add primal clan value as a node

        # creating subgraphs
        for key, value in primalClansDict.items():  # For each primal clan
            cluster = pydot.Cluster("".join(key))  # Create a cluster
            subgraph = pydot.Subgraph(rank="same")  # Create a subgraph into cluster
            for elem in value:
                cluster.add_node(pydot.Node("s_%s" % "".join(elem), label=" ", fillcolor="white",
                                            fixedsize=True, width=0.2))  # Add primal clan value as a node into cluster

            for pair in itertools.combinations(value, 2):  # For each pair of combinations from primal clan values
                subgraph.add_edge(pydot.Edge("s_%s" % "".join(pair[0]), "s_%s" % "".join(pair[1]), arrowhead="none",
                                             color=Clan.getColorClans(EdgesAtributtes, pair[0], pair[1])))
                #  Add edge into subgraph
            cluster.add_subgraph(subgraph)  # Add subgraph to cluster
            callgraph.add_subgraph(cluster)  # Add cluster to DOT file

        # creating edge links for nodes and subgraphs
        for value in primalClansDict.values():  # For each primal clan values
            for elem in value:
                if len(elem) == 1:  # If primal clan value is len() == 1
                    callgraph.add_edge(
                        pydot.Edge("s_%s" % "".join(elem), "".join(elem), arrowhead="none"))  # Add primal clan
                    # values as a edge

        for i, (key, value) in enumerate(primalClansDict.items()):  # For each primal clan
            if i != 0:  # If not the first primal clan in primalClansDict
                callgraph.add_edge(pydot.Edge("s_%s" % "".join(key), "s_%s" % "".join(value[0]),
                                              arrowhead="none", lhead="cluster_%s" % "".join(key)))  # Add primal clan
                # values as a edge

        callgraph.write(filename)  # Write a DOT file with all previous information
        print("2-structure %s was created" % filename)

    @staticmethod
    def plain2structure(planarGraph, nodes):
        clansList = Clan.clans(planarGraph, nodes)
        primalClansList = Clan.primalClans(clansList)
        EdgesAtributtes = Graph.createDictFromGraph(planarGraph)
        primalClansDict = OrderedDict(reversed(sorted(Clan.primalClansSubsets(primalClansList).items(),
                                                      key=lambda t: len(t[0]))))
        print(clansList, primalClansList, EdgesAtributtes, primalClansDict)
        Estructura.create2structure(EdgesAtributtes, primalClansDict, 'plain2structure.dot')

    @staticmethod
    def linear2structure(linearGraph, nodes):
        clansList = Clan.clans(linearGraph, nodes)
        primalClansList = Clan.primalClans(clansList)
        EdgesAtributtes = Graph.createDictFromGraph(linearGraph)
        primalClansDict = OrderedDict(reversed(sorted(Clan.primalClansSubsets(primalClansList).items(),
                                                      key=lambda t: len(t[0]))))
        print(clansList, primalClansList, EdgesAtributtes, primalClansDict)
        Estructura.create2structure(EdgesAtributtes, primalClansDict, 'linear2structure.dot')

    @staticmethod
    def exponential2structure(exponentialGraph, nodes):
        pass
