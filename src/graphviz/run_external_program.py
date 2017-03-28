"""
This module implements the call for Graphviz program that is associated with a dot file

Copyright (c) 2016-2017 Laura Rodriguez Navas <laura.rodriguez.navas@upc.edu>

Distributed under MIT license
[https://opensource.org/licenses/MIT]
"""

import os
import subprocess
import sys

__author__ = 'Laura Rodriguez Navas'
__license__ = 'MIT'


def openGraphviz(filename):
    """
    Call the Graphviz program that is associated with a Dot file specified by filename

    :param filename: Dot file
    :type filename: str
    """
    if sys.platform == 'win32':  # Windows platform
        os.startfile(filename)
    else:  # Linux platform
        subprocess.call(['open', '-a', 'Graphviz.app', filename])


if __name__ == '__main__':
    openGraphviz('graphviz.dot')