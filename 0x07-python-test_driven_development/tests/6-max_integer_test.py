#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):

    def test_negative(self):
        self.assertEqual(max_integer([-4, 3, 1, 2]), 3)

    def test_allnegative(self):
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_none(self):
        self.assertEqual(max_integer(), None)

    def test_oneelement(self):
        self.assertEqual(max_integer([1]), 1)

    def test_allzero(self):
        self.assertEqual(max_integer([0, 0, 0, 0]), 0)

    def test_maxend(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

if __name__ == '__main__':
    unittest.main()
