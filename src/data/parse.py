"""
This module implements rules for parse ARFF and TXT files

Copyright (c) 2016-2017 Laura Rodriguez Navas <laura.rodriguez.navas@upc.edu>

Distributed under MIT license
[https://opensource.org/licenses/MIT]
"""
__author__ = 'Laura Rodriguez Navas'
__license__ = 'MIT'


def replaceCharacter(fi, fo, old, new):
    for line in fi:
        if old in line:
            line = line.replace(old, new)
        fo.write(line)


if __name__ == '__main__':
    filename = str(input("Please enter the file name you want to parse:\n"))
    fi = open(filename, 'r')
    fo = open(filename + ".out", 'w')
    replaceCharacter(fi, fo, "-", "_")
    fi.close()
    fo.close()
