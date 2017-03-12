"""
This module implements the Subset class

Copyright (c) 2016-2017 Laura Rodriguez Navas <laura.rodriguez.navas@upc.edu>

Distributed under MIT license
[https://opensource.org/licenses/MIT]
"""
from itertools import chain, combinations

__author__ = 'Laura Rodriguez Navas'
__license__ = 'MIT'


class Subset:
    @staticmethod
    def powerset_generator(aset):
        """
        Iterator on powerset: all subsets of aset

        :param aset: Subsets from NetworkX's graph
        :type aset: set
        :return: subset
        :rtype: set
        """
        for subset in chain.from_iterable(combinations(aset, r) for r in range(1, len(aset) + 1)):
            yield set(subset)

    @staticmethod
    def powerset_list(nodes):
        """
        Return a list that contains all subsets from a graph

        :param nodes: Nodes from a graph
        :type nodes: list
        :return: List of all subsets from a graph
        :rtype: list
        """
        subsetList = list()
        for subset in Subset.powerset_generator(nodes):  # Subset iterator of each set in nodes
            subsetList.append(subset)  # Add subset to the list
        return subsetList
