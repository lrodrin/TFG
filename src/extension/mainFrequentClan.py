"""
This module implements a main for the Clan class and test the class with the more frequent clans

Copyright (c) 2016-2017 Laura Rodriguez Navas <laura.rodriguez.navas@upc.edu>

Distributed under MIT license
[https://opensource.org/licenses/MIT]
"""

from src.final.Interface import *

__author__ = 'Laura Rodriguez Navas'
__license__ = 'MIT'

if __name__ == "__main__":
    optionData = int(six.moves.input("Please enter the option for the type of file you provide:\n [1] = ARFF\n [2] = "
                                     "TXT\n"))

    columnNames, rows, cursor, tableName = Interface.inputFileOptions(optionData)  # Manages the data entry

    support = float(six.moves.input("Please enter the support for the more frequent subsets creation:\n"))
    moreFrequentSubsets = Subset.moreFrequentSubsets(tableName, optionData, support)  # Return the more frequents
    #  subsets from filename
    Clan.printFrequentResults(moreFrequentSubsets)
