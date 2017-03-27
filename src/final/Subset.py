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
    def powersetGenerator(aSet):
        """
        Iterator on powerset: all subsets of a set specified by aSet

        :param aSet: List of nodes from Networkx's graph
        :type aSet: list
        :return: A subset
        :rtype: set
        """
        for subset in chain.from_iterable(combinations(aSet, r) for r in range(1, len(aSet) + 1)):
            yield set(subset)
