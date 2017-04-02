"""
This module implements the Subset class

Copyright (c) 2016-2017 Laura Rodriguez Navas <laura.rodriguez.navas@upc.edu>

Distributed under MIT license
[https://opensource.org/licenses/MIT]
"""
import os
from itertools import chain, combinations

from src.final.Data import *

__author__ = 'Laura Rodriguez Navas'
__license__ = 'MIT'


class Subset:
    @staticmethod
    def powerSetGenerator(nodes):
        """
        Generate all subsets of a list of nodes from a graph

        :param nodes: List of nodes from Networkx's graph
        :type nodes: list
        :return: A subset from graph
        :rtype: set
        """
        for subset in chain.from_iterable(combinations(nodes, r) for r in range(1, len(nodes) + 1)):
            yield set(subset)

    @staticmethod
    def convertDataToSet(dataFile):
        """
        Return the more frequent subsets from data file specified by dataFile

        :param dataFile: Data file
        :type dataFile: file
        :return: The more frequent subsets
        :rtype: list
        """
        filename = dataFile + ".ap"

        # Open and/or creates AP data file
        if not os.path.exists(filename):  # If exists filename
            # TODO crida al programa apriori
            pass
        file = Data.openFile(filename)

        subset = set()
        moreFrequentSubsets = list()
        for line in file.readlines():  # For each line in filename
            for word in line.split(" "):  # For each word in line
                if not word.startswith("("):
                    subset.add(word)  # Add word as a subset
            moreFrequentSubsets.append(frozenset(subset))
            subset = set()

        return moreFrequentSubsets
