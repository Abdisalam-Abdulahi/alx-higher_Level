#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    '''
    class for testing
    '''
    def test_MaxInteger(self):
        ''' test max_integer '''
        self.assertEqual(max_integer([1, 2, 5, 8, 9]), 9)
        self.assertEqual(max_integer([1, 2, 18, 8, 9]), 18)
        self.assertEqual(max_integer([100]), 100)
        self.assertEqual(max_integer([-1, -2, -95, 8, 10]), 10)
        self.assertEqual(max_integer([0, 0, 0, 0, 0]), 0)
        self.assertEqual(max_integer([-1, -2, -5, -8, -9]), -1)
        self.assertEqual(max_integer([]), None)
