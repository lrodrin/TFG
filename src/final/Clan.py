"""
This module implements the Clan class

Copyright (c) 2016-2017 Laura Rodriguez Navas <laura.rodriguez.navas@upc.edu>

Distributed under MIT license
[https://opensource.org/licenses/MIT]
"""
from collections import defaultdict

from src.final.Graph import *
from src.final.Subset import *

__author__ = 'Laura Rodriguez Navas'
__license__ = 'MIT'


class Clan:
    @staticmethod
    def isClan(graph, subSet):
        """
        Checks if subSet of a initGraph is a clan

        :param graph: Networkx's initGraph
        :param subSet: subSet from initGraph
        :type graph: nx.Graph
        :type subSet: set
        :return: isClan == True if successful, isClan == False otherwise
        :rtype: bool
        """
        diff = set(graph.nodes()).difference(subSet)  # subSet formed by all nodes of initGraph less subset passed as
        # argument
        isClan = True
        for external in diff:  # For each subset of diff
            for (x, y) in itertools.combinations(subSet, 2):  # For each pair (x, y) in the subset combinations
                colorX = graph.edge[external][x]['color']
                colorY = graph.edge[external][y]['color']
                if colorX != colorY:  # (external, x) and (external, y) not have the same color edge
                    isClan = False
        return isClan

    @staticmethod
    def isTrivialClan(subSet, cardinality):
        """
        Checks if subSet of a initGraph is a trivial clan

        :param subSet: Subset from a initGraph
        :param cardinality: Maximal number of matched edges from a initGraph
        :type subSet: set
        :type cardinality: int
        :return: True if successful, False otherwise
        :rtype: bool
        """
        if len(subSet) == 1 or cardinality == len(subSet):  # subSet that contains one element or all nodes from a
            # initGraph
            return True
        else:
            return False

    @staticmethod
    def clans(graph, nodes):
        """
        Return a list of clans from initGraph sorted by subset length

        :param graph: Networkx's initGraph
        :param nodes: Nodes from initGraph
        :type graph: nx.Graph
        :type nodes: list
        :return: List of clans
        :rtype: list
        """
        clansList = list()
        for subset in Subset.powersetGenerator(nodes):  # For each subset in nodes
            if Clan.isClan(graph, subset):  # If subset is a clan
                clansList.append(subset)  # Add subset to the clans list
        return sorted(clansList)

    @staticmethod
    def trivialClans(nodes, cardinality):
        """
        Return a list of trivial clans from a initGraph sorted by subset length

        :param nodes: Nodes from a initGraph
        :param cardinality: A maximal cardinality matching in a initGraph
        :type nodes: list
        :type cardinality: int
        :return: List of trivial clans
        :rtype: list
        """
        trivialClansList = list()
        for subset in Subset.powersetGenerator(nodes):  # For each subset in nodes
            if Clan.isTrivialClan(subset, cardinality):  # If subset is a trivial clan
                trivialClansList.append(subset)  # Add subset to the trivial clans list
        return sorted(trivialClansList)

    @staticmethod
    def primalClans(clansList):
        """
        Returns a list of the primal clans sorted by primal clans length

        :param clansList: List of clans
        :type clansList: list
        :return: List of primal clans
        :rtype: list
        """
        potentialPrimalClans = defaultdict(bool)  # Creates and initializes a dictionary of booleans
        primalClansList = list()
        for i, key in enumerate(clansList):  # For each clan in clansList
            for j in range(i + 1, len(clansList)):
                intersection = clansList[i] & clansList[j]  # clansList[i] ∩ clansList[j]
                if len(intersection) == 0 or intersection == clansList[i] or intersection == clansList[j]:
                    # If not exist overlapping, the clan is a potential primal clan
                    potentialPrimalClans[frozenset(clansList[i])] = True
                    potentialPrimalClans[frozenset(clansList[j])] = True

        for key, value in potentialPrimalClans.items():  # For each potential primal clan in potentialPrimalClans
            if potentialPrimalClans[key]:  # If potential primal clan is a primal clan
                primalClansList.append(key)  # Add primal clan to primal clans list
        return sorted(primalClansList, key=len)

    @staticmethod
    def primalClansDict(primalClansList):
        """
        Returns a reversed dictionary of the primal clans. Keys are primal clans and their values are the primal
        clans that contains each key

        :param primalClansList: List of primal clans
        :type primalClansList: list
        :return: A primal clans dictionary
        :rtype: dict
        """
        primalClansDict = defaultdict(list)  # Creates and initializes a dictionary of list
        for i in range(len(primalClansList) - 1, 0, -1):  # For each primal clan
            for j in range(i - 1, -1, -1):
                if primalClansList[j].issubset(primalClansList[i]):  # If primalClansList[j] is subset of
                    # primalClansList[i]
                    for k in range(j + 1, i):  # Searching if between primalClansList[j] and primalClansList[i]
                        # there are more primal clans
                        if primalClansList[k].issubset(primalClansList[i]) and primalClansList[j].issubset(
                                primalClansList[k]):  # If primalClansList[k] is subset of primalClansList[i] and
                            # primalClansList[j] is subset of primalClansList[k]
                            break
                    else:
                        primalClansDict[frozenset(primalClansList[i])].append(primalClansList[j])  # Add primal clan
                        #  to primal clans dict
        return primalClansDict

    @staticmethod
    def getColorClans(EdgesAtributtes, primalClan1, primalClan2):
        """
        Get the color edge between two primal clans specified by primalClan_1 and primalClan2

        :param EdgesAtributtes: Edges atributtes from a initGraph
        :param primalClan1: Primal clan
        :param primalClan2: Primal clan
        :type EdgesAtributtes: dict
        :type primalClan1: set
        :type primalClan2: set
        :return: Color edge between primalClan1 and primalClan2
        :rtype: str
        """
        for key, color in EdgesAtributtes.items():  # For each primal clan
            if (key[0] in primalClan1 and key[1] in primalClan2) or (
                            key[1] in primalClan1 and key[0] in primalClan2):  # If primalClan1 and primalClan2 have
                #  the same color in EdgesAtributtes
                return color
