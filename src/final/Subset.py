"""
This module implements the Subset class

Copyright (c) 2016-2017 Laura Rodriguez Navas <laura.rodriguez.navas@upc.edu>

Distributed under MIT license
[https://opensource.org/licenses/MIT]
"""
import os

import sys
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
    def moreFrequentSubsets(dataFile, option, support):
        """
        Return the more frequent subsets from ARFF data file specified by dataFile

        :param dataFile: Data file
        :param option: Specifies type of dataFile
        :param support: The probability for the more frequent subsets creation
        :type dataFile: str
        :type option: int
        :type support: float
        :return: The more frequent subsets
        :rtype: list
        """
        # Create if not exists and open AP data file
        newFilename = dataFile + ".ap"
        if not os.path.exists(newFilename):  # If not exists a AP filename
            if option == 1:  # If data file input have the arff type
                dataFile += ".arff"
            elif option == 2:  # If data file input have the txt type
                dataFile += ".txt"

            # System calls to apriori's algorithm who's create the AP data file
            if sys.platform == 'win32':  # Windows platform
                os.system("apriori.exe -s{0} -C'@%' {1} {2}".format(str(support), str(dataFile.replace("\n", "")),
                                                                    str(newFilename.replace("\n", ""))))
            elif sys.platform == 'linux2':  # Linux platform
                os.system("./apriori -s{0} -C'@%' {1} {2}".format(str(support), str(dataFile.replace("\n", "")),
                                                                  str(newFilename.replace("\n", ""))))
            elif sys.platform == 'darwin':  # Mac platform
                os.system("./aprioriOSX -s{0} -C'@%' {1} {2}".format(str(support), str(dataFile.replace("\n", "")),
                                                                   str(newFilename.replace("\n", ""))))

        print(newFilename)
        filename = (Data.openFile(newFilename.replace("\n", "")))  # Open AP data file
        subset = set()
        moreFrequentSubsets = list()
        for line in filename.readlines():  # For each line in AP data file
            for word in line.split(" "):  # For each word in line
                if not word.startswith("("):
                    subset.add(word)  # Add word as a subset
            moreFrequentSubsets.append(frozenset(subset))  # Add new subset to the list moreFrequentSubsets
            subset = set()

        return moreFrequentSubsets
