"""
This module implements the Subset class

Copyright (c) 2016-2017 Laura Rodriguez Navas <laura.rodriguez.navas@upc.edu>

Distributed under MIT license
[https://opensource.org/licenses/MIT]
"""
from itertools import chain, combinations

__author__ = 'Laura Rodriguez Navas'
__license__ = 'MIT'


class Subset(object):
    @staticmethod
    def powerset_generator(aset):
        """
            Iterator on powerset: all subsets of aset

        :param aset: Subset of nodes from NetworkX graph
        :type aset: set
        :return: subset
        :rtype: set
        """
        for subset in chain.from_iterable(combinations(aset, r) for r in range(1, len(aset) + 1)):
            yield set(subset)
