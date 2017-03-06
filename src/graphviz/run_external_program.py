"""
This module implements the call for Graphviz program that is associated with a file

Copyright (c) 2016-2017 Laura Rodriguez Navas <laura.rodriguez.navas@upc.edu>

Distributed under MIT license
[https://opensource.org/licenses/MIT]
"""

import os
import subprocess
import sys

__author__ = 'Laura Rodriguez Navas'
__license__ = 'MIT'


def open_graphviz(program, filename):
    if sys.platform == 'win32':
        os.startfile(filename)
    else:
        subprocess.run(['open', '-a', program, filename])


open_graphviz('/Applications/Graphviz.app', 'graphviz.dot')
