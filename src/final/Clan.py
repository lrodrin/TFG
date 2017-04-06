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
        Checks if a subSet is a clan of graph 

        :param graph: Networkx's graph
        :param subSet: Subset from graph
        :type graph: nx.Graph
        :type subSet: set
        :return: True if successful, False otherwise
        :rtype: bool
        """
        diff = set(graph.nodes()).difference(subSet)  # Subset formed by all nodes of graph less subSet passed as
        # parameter
        isClan = True
        for external in diff:  # For each subset in diff
            for (u, v) in itertools.combinations(subSet, 2):  # For each pair (u, v) in the subSet combinations
                if graph.has_edge(external, u) and graph.has_edge(external, v):  # If exists the edge (external,
                    # u) and (external, v) in graph
                    colorX = graph.edge[external][u]['color']
                    colorY = graph.edge[external][v]['color']
                    if colorX != colorY:  # If the pair (external, u) and (external, v) not have the same color edge
                        isClan = False
        return isClan

    @staticmethod
    def clans(graph, nodes):
        """
        Return a list of clans from graph sorted by clan's length

        :param graph: Networkx's graph
        :param nodes: Nodes from graph
        :type graph: nx.Graph
        :type nodes: list
        :return: List of clans
        :rtype: list
        """
        clansList = list()
        for subset in Subset.powerSetGenerator(nodes):  # For each subset in nodes
            if Clan.isClan(graph, subset):  # If subset is a clan
                clansList.append(subset)  # Add subset to the clans list

        return sorted(clansList)

    @staticmethod
    def frequentClans(graph, moreFrequentSubsets):
        """
        Return a list of more frequent clans from graph sorted by clan's length

        :param graph: Networkx's graph
        :param moreFrequentSubsets: More frequents nodes from graph
        :type graph: nx.Graph
        :type moreFrequentSubsets: list
        :return: List of more frequent clans
        :rtype: list
        """
        clansList = list()
        for subset in moreFrequentSubsets:  # For each subset in more frequent subsets
            if Clan.isClan(graph, subset):  # If subset is a clan
                clansList.append(subset)  # Add subset to the clans list

        return sorted(clansList)

    @staticmethod
    def trivialClans(clansList, cardinality):
        """
        Return a list of trivial clans from a list of clans specified by clansList

        :param clansList: List of clans
        :param cardinality: A maximal cardinality matching in a graph
        :type clansList: list
        :type cardinality: int
        :return: List of trivial clans
        :rtype: list
        """
        trivialClansList = list()
        for clan in clansList:
            if len(clan) == 1 or cardinality == len(clan):  # If clan is a trivial clan
                trivialClansList.append(clan)

        return sorted(trivialClansList)

    @staticmethod
    def primalClans(clansList):
        """
        Return a list of primal clans from a list of clans specified by clansList

        :param clansList: List of clans
        :type clansList: list
        :return: List of primal clans
        :rtype: list
        """
        noPrimalClans = defaultdict(bool)
        primalClansList = list()
        for i, key in enumerate(clansList):  # For each clan in clansList
            for j in range(i + 1, len(clansList)):
                intersection = clansList[i] & clansList[j]  # clansList[i] intersection clansList[j]
                if len(intersection) != 0 and intersection < clansList[i] and intersection < clansList[j]:
                    # If exist an overlapping, the clan is not a primal clan
                    noPrimalClans[frozenset(clansList[i])] = True
                    noPrimalClans[frozenset(clansList[j])] = True

        for clan in clansList:
            if not noPrimalClans.get(frozenset(clan)):  # If not exist overlapping the clan is a primal clan
                primalClansList.append(clan)

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
                if primalClansList[j].issubset(primalClansList[i]):  # If primalClansList[j] is a subset of
                    # primalClansList[i]
                    for k in range(j + 1, i):  # Search if between primalClansList[j] and primalClansList[i]
                        # there are more primal clans
                        if primalClansList[k].issubset(primalClansList[i]) and primalClansList[j].issubset(
                                primalClansList[k]):  # If primalClansList[k] is a subset of primalClansList[i] and
                            # primalClansList[j] is a subset of primalClansList[k]
                            break
                    else:
                        primalClansDict[frozenset(primalClansList[i])].append(primalClansList[j])  # Add primal clan
                        #  to primal clans dict

        return primalClansDict

    @staticmethod
    def getColorClans(colorEdgesAttributes, primalClan1, primalClan2):
        """
        Get the color edge between two primal clans specified by primalClan_1 and primalClan2

        :param colorEdgesAttributes: Color edges atributtes from a graph
        :param primalClan1: Primal clan
        :param primalClan2: Primal clan
        :type colorEdgesAttributes: dict
        :type primalClan1: set
        :type primalClan2: set
        :return: Color edge attribute between primalClan1 and primalClan2
        :rtype: str
        """
        for key, color in colorEdgesAttributes.items():  # For each primal clan and their color attribute
            if (key[0] in primalClan1 and key[1] in primalClan2) or (
                            key[1] in primalClan1 and key[0] in primalClan2):  # If primalClan1 and primalClan2 have
                #  the same color in colorEdgesAttributes
                return color

    @staticmethod
    def printResults(graph):
        """
        Print the results of the main Clan execution:
            - A list of clans
            - A list of trivial clans
            - A list of primal clans
            - A dictionary of primal clans

        :param graph: Networkx's graph
        :type graph: nx.Graph
        """
        clansList = Clan.clans(graph, graph.nodes())  # Create clans list
        print("\nList of clans:\n%s\n" % clansList)
        trivialClansList = Clan.trivialClans(clansList, Graph.getMaxCardinalityFromGraph(graph))  # Create trivial clans
        # list
        print("List of trivial clans:\n%s\n" % trivialClansList)
        primalClansList = Clan.primalClans(clansList)  # Create primal clans list
        print("List of primal clans:\n%s\n" % primalClansList)
        primalClansDict = Clan.primalClansDict(primalClansList)  # Create primal clans dictionary
        print("Dictionary of primal clans:\n%s" % primalClansDict)

    @staticmethod
    def printFrequentResults(graph, moreFrequentSubsets):
        """
        Print the results of the main Clan execution:
            - A list of more frequents clans
            - A list of more frequents trivial clans
            - A list of more frequents primal clans
            - A dictionary of more frequents primal clans

        :param graph: Networkx's graph
        :param moreFrequentSubsets: More frequents nodes from graph
        :type graph: nx.Graph
        :type moreFrequentSubsets: list
        """
        clansList = Clan.frequentClans(graph, moreFrequentSubsets)  # Create clans list
        print("\nList of clans:\n%s\n" % clansList)
        trivialClansList = Clan.trivialClans(clansList, Graph.getMaxCardinalityFromGraph(graph))  # Create trivial clans
        # list
        print("List of trivial clans:\n%s\n" % trivialClansList)
        primalClansList = Clan.primalClans(clansList)  # Create primal clans list
        print("List of primal clans:\n%s\n" % primalClansList)
        primalClansDict = Clan.primalClansDict(primalClansList)  # Create primal clans dictionary
        print("Dictionary of primal clans:\n%s" % primalClansDict)
