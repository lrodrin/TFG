"""
This module implements the Subset class

Copyright (c) 2016-2017 Laura Rodriguez Navas <laura.rodriguez.navas@upc.edu>

Distributed under MIT license
[https://opensource.org/licenses/MIT]
"""
import os
from itertools import chain, combinations

import sys

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
    def moreFrequentSubsets(dataFile, option, probability):
        """
        Return the more frequent subsets from data file specified by dataFile

        :param dataFile: Data file
        :param option: Specifies type of dataFile
        :param probability: The probability for the more frequent subsets creation
        :type dataFile: file
        :type option: int
        :type probability: float
        :return: The more frequent subsets
        :rtype: list
        """
        # Create and/or open AP data file
        newFilename = dataFile + ".ap"
        if not os.path.exists(newFilename):  # If not exists a AP filename
            if option == 1:
                dataFile += ".arff"
            elif option == 2:
                dataFile += ".txt"

            if sys.platform == 'win32':  # Windows platform
                os.system("apriori.exe -s{0} -C'@%' {1} {2}".format(str(probability), str(dataFile), str(newFilename)))
            # elif sys.platform == 'darwin':  # Mac platform
            #     os.system("apriori.exe -s1 -C'@%' {0} {1}".format(str(dataFile), str(newFilename)))
            # elif sys.platform == 'linux2':  # Linux platform
            #     os.system("apriori.exe -s1 -C'@%' {0} {1}".format(str(dataFile), str(newFilename)))
            # TODO OS X and Ubuntu

        file = Data.openFile(newFilename)   # Open data file

        subset = set()
        moreFrequentSubsets = list()
        for line in file.readlines():  # For each line in filename
            for word in line.split(" "):  # For each word in line
                if not word.startswith("("):
                    subset.add(word)  # Add word as a subset
            moreFrequentSubsets.append(frozenset(subset))
            subset = set()

        return moreFrequentSubsets
