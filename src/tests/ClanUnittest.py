"""
This module implements the test for Clan class

Copyright (c) 2016-2017 Laura Rodriguez Navas <laura.rodriguez.navas@upc.edu>

Distributed under MIT license
[https://opensource.org/licenses/MIT]
"""
import unittest
import src.final.Clan as c

__author__ = 'Laura Rodriguez Navas'
__license__ = 'MIT'


class TestClan(unittest.TestCase):
    def test_isATrivialClan(self):
        self.assertTrue(isTrivialClan({'A'}, 1))


if __name__ == '__main__':
    unittest.main()