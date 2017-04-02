"""
This module implements rules for parse ARFF and TXT files

Copyright (c) 2016-2017 Laura Rodriguez Navas <laura.rodriguez.navas@upc.edu>

Distributed under MIT license
[https://opensource.org/licenses/MIT]
"""
import glob

__author__ = 'Laura Rodriguez Navas'
__license__ = 'MIT'

# TODO replace char - for _ in TXT file because SQLite not accept this char

list_of_files = glob.glob('contact_lenses.arff')  # create the list of file
for file_name in list_of_files:
    FI = open(file_name, 'r')
    FO = open(file_name + ".out", 'w')
    for line in FI:
        if "-" in line:
            line = line.replace("-", "_")
        FO.write(line)

    FI.close()
    FO.close()
