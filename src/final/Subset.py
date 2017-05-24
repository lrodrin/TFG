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
        newFilename = dataFile + ".ap"  # Name for new AP file
        if option == 1:  # If data file input have the arff type
            dataFile += ".arff"
        elif option == 2:  # If data file input have the txt type
            dataFile += ".txt"

        # System calls to apriori's algorithm who's create the AP data file
        if sys.platform == 'win32':  # Windows platform
            try:
                os.system("apriori.exe -s{0} -C'@%' {1} {2}".format(str(support), str(dataFile.replace("\n", "")),
                                                                    str(newFilename.replace("\n", ""))))

            except OSError as e:
                print("Error to execute the apriori's algorithm in Windows platform:", e)

        elif 'linux' in sys.platform:  # Linux platform
            try:
                os.system("chmod +x apriori")
                os.system("./apriori -s{0} -C'@%' {1} {2}".format(str(support), str(dataFile.replace("\n", "")),
                                                                  str(newFilename.replace("\n", ""))))
            except OSError as e:
                print("Error to execute the apriori's algorithm in Linux platform:", e)

        elif sys.platform == 'darwin':  # Mac platform
            try:
                os.system("./aprioriOSX -s{0} -C'@%' {1} {2}".format(str(support), str(dataFile.replace("\n", "")),
                                                                     str(newFilename.replace("\n", ""))))
            except OSError as e:
                print("Error to execute the apriori's algorithm in Mac platform:", e)

        filename = (Data.openFile(newFilename.replace("\n", "")))  # Open AP data file
        subset = set()
        allElements = set()
        moreFrequentSubsets = list()
        allElementsList = list()
        for line in filename.readlines():  # For each line in AP data file
            for word in line.split(" "):  # For each word in line
                if not word.startswith("("):
                    if ':' in word:  # txt filter
                        subset.add(word.split(":")[1])
                    else:
                        subset.add(word)  # Add word as a subset
                    for elem in word.split(" "):
                        if word not in allElements:
                            if ':' in word:  # txt filter
                                allElements.add(elem.split(":")[1])
                            else:
                                allElements.add(elem)

            moreFrequentSubsets.append(subset)  # Add new subset to the list moreFrequentSubsets
            subset = set()

        filename.close()
        allElementsList.append(allElements)
        if allElements not in moreFrequentSubsets:  # If trivial clan with all the elements not exists in
            # moreFrequentSubsets
            moreFrequentSubsets.extend(allElementsList)  # Add the trivial clan with all the elements

        return moreFrequentSubsets
