"""
This module implements the Clan class

Copyright (c) 2016-2017 Laura Rodriguez Navas <laura.rodriguez.navas@upc.edu>

Distributed under MIT license
[https://opensource.org/licenses/MIT]
"""
import itertools
from collections import defaultdict
import src.final.Subset as it

__author__ = 'Laura Rodriguez Navas'
__license__ = 'MIT'


class Clan(object):
    @staticmethod
    def isClan(Graph, subSet):
        """
        Checks if subset of the graph is a clan

        :param Graph: Networkx's Graph
        :param subSet: Subset from Graph
        :type Graph: nx.Graph
        :type subSet: set
        :return: b
        :rtype: True if successful, False otherwise
        """
        diff = set(Graph.nodes()).difference(subSet)  # Subset formed by all nodes of G less subset passed as argument
        b = True
        for external in diff:  # For each subset of diff
            for (x, y) in itertools.combinations(subSet, 2):  # For each pair (x, y) in the subset combinations
                color_x = Graph.edge[external][x]['color']
                color_y = Graph.edge[external][y]['color']
                if color_x != color_y:  # Pair (x, y) not the same colored
                    b = False
        return b

    @staticmethod
    def isTrivialClan(subSet, cardinality):
        """
        Checks if clan is trivial

        :param subSet: It is a subset clan
        :param cardinality: maximal number of matched edges from a graph
        :type subSet: set
        :type cardinality: int
        :return: b
        :rtype: True if successful, False otherwise
        """
        if len(subSet) == 1 or cardinality == len(subSet):  # Clan that contains one element or all nodes from a graph
            return True
        else:
            return False

    @staticmethod
    def clans(Graph, setNodes):
        """
            Return a list of clans from a Graph sorted by length

        :param Graph: Networkx's Graph
        :param setNodes: Set of nodes from Graph
        :type Graph: nx.Graph
        :type setNodes: set
        :return: List of clans
        :rtype: list
        """
        clansList = []  # Empty list
        listNodes = it.Subset.powerset_list(setNodes)
        for subset in listNodes:    # For each subset in listNodes
            if Clan.isClan(Graph, subset):  # If subset is a clan of Graph
                clansList.append(subset)  # Add subset to the clans list
        return sorted(clansList)

    @staticmethod
    def trivialClans(setNodes, cardinality):
        """
            Return a list of trivial clans from a Graph sorted by length

        :param setNodes: Set of nodes from a graph
        :param cardinality: A maximal cardinality matching in the graph
        :type setNodes: set
        :type cardinality: int
        :return: List of trivial clans
        :rtype: list
        """
        trivialClansList = []  # Empty list
        listNodes = it.Subset.powerset_list(setNodes)
        for subset in listNodes:  # For each subset in listNodes
            if Clan.isTrivialClan(subset, cardinality):  # If subset is a clan of Graph G
                trivialClansList.append(subset)  # Add subset to the clans list
        return sorted(trivialClansList)

    @staticmethod
    def primalClans(listClans):
        """
            Returns a list with the primal clans sorted by length

            :param listClans: List of clans
            :type listClans: list of sets
            :return: primals
            :rtype: list
        """
        potential_primals = defaultdict(bool)  # Creates and initializes a dictionary from a list of clans
        primals = []  # Empty list
        for i, key in enumerate(listClans):  # For each elem in listClans
            for j in range(i + 1, len(listClans)):  # For each elem+1 in listClans
                intersection = listClans[i] & listClans[j]
                if len(intersection) == 0 or intersection == listClans[i] or intersection == listClans[j]:
                    # If not exist overlapping mark the value of potential_primals True
                    potential_primals[frozenset(listClans[i])] = True
                    potential_primals[frozenset(listClans[j])] = True

        for key, value in potential_primals.items():  # Creates a list with a primal clans of potential_primals
            if potential_primals[key]:  # If is a primal clan
                primals.append(key)  # Add clan to primals list
        return sorted(primals)
