"""
This module implements a program that looping a list of files and change the imports

Copyright (c) 2016-2017 Laura Rodriguez Navas <laura.rodriguez.navas@upc.edu>

Distributed under MIT license
[https://opensource.org/licenses/MIT]
"""
import glob
import os

__author__ = 'Laura Rodriguez Navas'
__license__ = 'MIT'


def changeImport(FI, FO):
    for line in FI.readlines():
        if line.startswith("from"):
            if "src.final." in line.split(" ")[1]:
                newLine = line.split(" ")[1].lstrip("src.final.")
                line = str(line.split(" ")[0]) + " " + newLine + " " + str(line.split(" ")[2]) + " " + str(
                    line.split(" ")[3])
            elif "src." in line.split(" ")[1]:
                newLine = line.split(" ")[1].lstrip("src")
                line = str(line.split(" ")[0]) + " " + newLine.lstrip(".") + " " + str(line.split(" ")[2]) + " " + str(
                    line.split(" ")[3])
        FO.write(line)


if __name__ == '__main__':
    path = "*.py"
    for filename in glob.glob(path):
        fi = open(filename, 'r')
        fo = open(filename + ".out", 'w')
        changeImport(fi, fo)
        fi.close()
        fo.close()
        os.system("cp %s %s" % (str(filename) + ".out", str(filename)))
