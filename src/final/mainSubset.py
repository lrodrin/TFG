"""
This module implements the main for Subset class

Copyright (c) 2016-2017 Laura Rodriguez Navas <laura.rodriguez.navas@upc.edu>

Distributed under MIT license
[https://opensource.org/licenses/MIT]
"""
import six

from src.final.Subset import *
from src.final.simpleGraphs import *

__author__ = 'Laura Rodriguez Navas'
__license__ = 'MIT'

if __name__ == "__main__":
    graph = simpleGraph_1()  # Create a simple graph

    for subset in Subset.powerSetGenerator(graph.nodes()):  # All subsets from a graph
        print(subset)

    optionData = int(six.moves.input("Please enter the option for the type of file you provide:\n [1] = ARFF\n [2] = "
                                     "TXT\n"))
    filename = str(six.moves.input("Please enter the file name you provide:\n"))
    probability = float(six.moves.input("Please enter the probability for the more frequent subsets creation:\n"))
    moreFrequentSubsets = Subset.moreFrequentSubsets(filename, optionData, probability)  # The more frequents subsets
    #  from filename
    print(moreFrequentSubsets)
