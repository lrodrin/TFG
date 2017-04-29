"""
This module creates the more frequents subsets from an AP file

Copyright (c) 2016-2017 Laura Rodriguez Navas <laura.rodriguez.navas@upc.edu>

Distributed under MIT license
[https://opensource.org/licenses/MIT]
"""
import six

from src.final.Subset import *

if __name__ == '__main__':
    optionData = int(six.moves.input("Please enter the option for the type of file you provide:\n [1] = ARFF\n [2] = "
                                     "TXT\n"))
    filename = str(six.moves.input("Please enter the file name you provide:\n"))
    support = float(six.moves.input("Please enter the probability for the more frequent subsets creation:\n"))
    moreFrequentSubsets = Subset.moreFrequentSubsets(filename, optionData, support)  # The more frequents subsets
    #  from filename
    print(moreFrequentSubsets)
