"""
This module implements the Estructura class

Copyright (c) 2016-2017 Laura Rodriguez Navas <laura.rodriguez.navas@upc.edu>

Distributed under MIT license
[https://opensource.org/licenses/MIT]
"""
import os
from collections import defaultdict
import itertools
import pydot
import sys

import subprocess

__author__ = 'Laura Rodriguez Navas'
__license__ = 'MIT'

# TODO modificar la mida del cluster y los redondeles redondos en vez de elípticos


class Estructura:
    @staticmethod
    def create_2structure(graphEdgesAtributtes, primalsDict, filename):
        """
            Create a 2-structure from a list of clans

        :param graphEdgesAtributtes: Dictionary of edges atributtes from a Graph
        :param primalsDict: List of primal clans
        :param filename: DOT file name
        :type graphEdgesAtributtes: dict
        :type primalsDict: dict of frozenset
        :type filename: str
        :return: A 2-structure
        :rtype: DOT file
        """
        callgraph = pydot.Dot(graph_type='digraph', compound=True)

        # creating external nodes
        for value in primalsDict.values():  # For each primal clan values
            for elem in value:
                if len(elem) == 1:  # If primal clan value is len() == 1
                    callgraph.add_node(pydot.Node("".join(elem)))  # Add primal clan value as a node

        # creating subgraphs
        for key, value in primalsDict.items():  # For each primal clan
            cluster = pydot.Cluster("".join(key))  # Create a cluster
            subgraph = pydot.Subgraph(rank="same")  # Create a subgraph into cluster
            for elem in value:
                cluster.add_node(pydot.Node("s_%s" % "".join(elem), label=" ", fillcolor="white",
                                            fixedsize=True, width=0.2))  # Add primal clan value as a node into cluster

            for pair in itertools.combinations(value, 2):  # For each pair of combinations from primal clan values
                subgraph.add_edge(pydot.Edge("s_%s" % "".join(pair[0]), "s_%s" % "".join(pair[1]), arrowhead="none",
                                             color=Estructura.getColorClans(graphEdgesAtributtes, pair[0], pair[1])))
                #  Add edge into subgraph
            cluster.add_subgraph(subgraph)  # Add subgraph to cluster
            callgraph.add_subgraph(cluster)  # Add cluster to DOT file

        # creating edge links for nodes and subgraphs
        for value in primalsDict.values():  # For each primal clan values
            for elem in value:
                if len(elem) == 1:  # If primal clan value is len() == 1
                    callgraph.add_edge(
                        pydot.Edge("s_%s" % "".join(elem), "".join(elem), arrowhead="none"))  # Add primal clan
                    # values as a edge

        for i, (key, value) in enumerate(primalsDict.items()):  # For each primal clan
            if i != 0:  # If not the first primal clan in primalsDict
                callgraph.add_edge(pydot.Edge("s_%s" % "".join(key), "s_%s" % "".join(value[0]),
                                              arrowhead="none", lhead="cluster_%s" % "".join(key)))  # Add primal clan
                # values as a edge

        callgraph.write(filename)  # Write a DOT file with all previous information

    @staticmethod
    def primalSubsets(primalsList):
        """
            Return a dictionary with all subsets from a primal clans list

        :param primalsList: List of primal clans
        :type primalsList: list
        :return: A dictionary with the subsets from primalsList
        :rtype: dict
        """
        dictionary = defaultdict(list)  # Empty dictionary
        for i in range(len(primalsList) - 1, 0, -1):
            for j in range(i - 1, -1, -1):
                if primalsList[j].issubset(primalsList[i]):
                    for k in range(j + 1, i):
                        if primalsList[k].issubset(primalsList[i]) and primalsList[j].issubset(primalsList[k]):
                            break
                    else:
                        dictionary[frozenset(primalsList[i])].append(primalsList[j])
        return dictionary

    @staticmethod
    def getColorClans(graphEdgesAtributtes, primalClan_1, primalClan_2):
        """
            Get the color edge between two primal clans

        :param graphEdgesAtributtes: Dictionary of edges atributtes from a Graph
        :param primalClan_1: Primal clan
        :param primalClan_2: Primal clan
        :type graphEdgesAtributtes: dict
        :type primalClan_1: set
        :type primalClan_2: set
        :return: Color edge between primalClan_1 and primalClan_2
        :rtype: str
        """
        for key, value in graphEdgesAtributtes.items():  # For each primal clan
            if (key[0] in primalClan_1 and key[1] in primalClan_2) or (
                    key[1] in primalClan_1 and key[0] in primalClan_2):
                return value

    @staticmethod
    def openGraphviz(program, filename):
        """
            Call the Graphviz program that is associated with a 2-structure file

        :param program: Path to Graphviz program
        :param filename: Path to 2-structure file
        """
        if sys.platform == 'win32':  # Windows platform
            os.startfile(filename)
        else:  # Linux platform
            subprocess.run(['open', '-a', program, filename])
