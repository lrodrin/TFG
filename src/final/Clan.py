"""
This module implements the Clan class

Copyright (c) 2016-2017 Laura Rodriguez Navas <laura.rodriguez.navas@upc.edu>

Distributed under MIT license
[https://opensource.org/licenses/MIT]
"""
import itertools
from collections import defaultdict

from src.final.Subset import *

__author__ = 'Laura Rodriguez Navas'
__license__ = 'MIT'


class Clan:
    @staticmethod
    def isClan(graph, subSet):
        """
        Checks if subset of the graph is a clan

        :param graph: Networkx's graph
        :param subSet: Subset from graph
        :type graph: nx.Graph
        :type subSet: set
        :return: b == True if successful, b == False otherwise
        :rtype: bool
        """
        diff = set(graph.nodes()).difference(subSet)  # Subset formed by all nodes of graph less subset passed as
        # argument
        b = True
        for external in diff:  # For each subset of diff
            for (x, y) in itertools.combinations(subSet, 2):  # For each pair (x, y) in the subset combinations
                if graph.has_edge(external, x) and graph.has_edge(external, y):
                    colorX = graph.edge[external][x]['color']
                    colorY = graph.edge[external][y]['color']
                    if colorX != colorY:  # Pair (x, y) not the same colored
                        b = False
        return b

    @staticmethod
    def isTrivialClan(subSet, cardinality):
        """
        Checks if subset of a graph is a trivial clan

        :param subSet: Subset from a graph
        :param cardinality: Maximal number of matched edges from a Graph
        :type subSet: set
        :type cardinality: int
        :return: b == True if successful, b == False otherwise
        :rtype: bool
        """
        if len(subSet) == 1 or cardinality == len(subSet):  # Clan that contains one element or all nodes from a graph
            return True
        else:
            return False

    @staticmethod
    def clans(graph, nodes):
        """
        Return a list of clans from a Graph sorted by length

        :param graph: Networkx's Graph
        :param nodes: Nodes from graph
        :type graph: nx.Graph
        :type nodes: list
        :return: List of clans
        :rtype: list
        """
        clansList = []
        listNodes = Subset.powerset_list(nodes)
        for subset in listNodes:  # For each subset in listNodes
            if Clan.isClan(graph, subset):  # If subset is a clan of graph
                clansList.append(subset)  # Add subset to the clans list
        return sorted(clansList)

    @staticmethod
    def trivialClans(nodes, cardinality):
        """
        Return a list of trivial clans from a graph sorted by length

        :param nodes: Nodes from a graph
        :param cardinality: A maximal cardinality matching in a graph
        :type nodes: list
        :type cardinality: int
        :return: List of trivial clans
        :rtype: list
        """
        trivialClansList = []
        listNodes = Subset.powerset_list(nodes)  # List that contains all subsets from a graph
        for subset in listNodes:  # For each subset in listNodes
            if Clan.isTrivialClan(subset, cardinality):  # If subset is a trivial clan of a graph
                trivialClansList.append(subset)  # Add subset to the trivial clans list
        return sorted(trivialClansList)

    @staticmethod
    def primalClans(clansList):
        """
        Returns a list of the primal clans sorted by length

        :param clansList: List of clans
        :type clansList: list
        :return: List of primal clans
        :rtype: list
        """
        potentialPrimals = defaultdict(bool)  # Creates and initializes a dictionary from a list of clans
        primalClansList = []
        for i, key in enumerate(clansList):  # For each elem in clansList
            for j in range(i + 1, len(clansList)):
                intersection = clansList[i] & clansList[j]  # clansList[i] ∩ clansList[j]
                if len(intersection) == 0 or intersection == clansList[i] or intersection == clansList[j]:
                    # If not exist overlapping the subset is a potential primal clan
                    potentialPrimals[frozenset(clansList[i])] = True
                    potentialPrimals[frozenset(clansList[j])] = True

        for key, value in potentialPrimals.items():  # For each subset in potentialPrimals
            if potentialPrimals[key]:  # If subset is a primal clan
                primalClansList.append(key)  # Add clan to primal clans list
        return sorted(primalClansList, key=len)

    @staticmethod
    def primalClansSubsets(primalClansList):
        """
        Groups together the primal clans

        :param primalClansList: List of primal clans
        :type primalClansList: list
        :return: A primalClansSubsets with the primal clans combinations are subsets
        :rtype: dict
        """
        primalClansSubsets = defaultdict(list)
        for i in range(len(primalClansList) - 1, 0, -1):
            for j in range(i - 1, -1, -1):
                if primalClansList[j].issubset(primalClansList[i]):
                    for k in range(j + 1, i):
                        if primalClansList[k].issubset(primalClansList[i]) and primalClansList[j].issubset(
                                primalClansList[k]):
                            break
                    else:
                        primalClansSubsets[frozenset(primalClansList[i])].append(primalClansList[j])
        return primalClansSubsets

    @staticmethod
    def getColorClans(EdgesAtributtes, primalClan_1, primalClan_2):
        """
        Get the color edge from a graph between two primal clans

        :param EdgesAtributtes: Edges atributtes from a graph
        :param primalClan_1: One primal clan
        :param primalClan_2: Second primal clan
        :type EdgesAtributtes: dict
        :type primalClan_1: set
        :type primalClan_2: set
        :return: Color edge between primalClan_1 and primalClan_2
        :rtype: str
        """
        for key, color in EdgesAtributtes.items():  # For each primal clan and color
            if (key[0] in primalClan_1 and key[1] in primalClan_2) or (
                            key[1] in primalClan_1 and key[0] in primalClan_2):
                return color
