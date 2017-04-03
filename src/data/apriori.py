import six

from src.final.Subset import *

if __name__ == '__main__':
    optionData = int(six.moves.input("Please enter the option for the type of file you provide:\n [1] = ARFF\n [2] = "
                                     "TXT\n"))
    filename = str(input("Please enter the file name you provide:\n"))
    probability = int(input("Please enter the probability for the more frequent subsets creation:\n"))
    moreFrequentSubsets = Subset.moreFrequentSubsets(filename, optionData, 1)  # The more frequents subsets from
    # filename
    print(moreFrequentSubsets)
