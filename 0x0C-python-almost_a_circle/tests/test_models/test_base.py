#!/usr/bin/python3
"""Unittest for base.py"""

from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import unittest
import json
import pep8
import unittest


class Testpep8(unittest.TestCase):
    """Simple pep8 testing"""
    def test_pep8(self):
        msg = "Found code style errors (and warning)."
        style = pep8.StyleGuide(quiet=True)
        fileRectangle = "models/rectangle.py"
        fileRectangleTest = "tests/test_models/test_rectangle.py"
        fileBase = "models/base.py"
        fileBaseTest = "tests/test_models/test_base.py"
        fileSquare = "models/square.py"
        fileSquareTest = "tests/test_models/test_square.py"
        check = style.check_files([fileRectangle, fileRectangleTest,
                                   fileBase, fileBaseTest, fileSquare,
                                   fileSquareTest])
        self.assertEqual(check.total_errors, 0, msg)


class TestBase(unittest.TestCase):
    """ Test all of i think """

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        self.b1 = Base()
        self.b2 = Base()
        self.b3 = Base(-7)
        self.b4 = Base(12)
        self.b5 = Base("test")
        self.b6 = Base(3.1)
        self.b7 = Base()

    def tearDown(self):
        pass

    def test_A_simpleTest(self):
        self.assertEqual(self.b1.id, 1)
        self.assertEqual(self.b2.id, 2)
        self.assertEqual(self.b3.id, -7)
        self.assertEqual(self.b4.id, 12)
        self.assertEqual(self.b5.id, "test")
        self.assertEqual(self.b6.id, 3.1)
        self.assertEqual(self.b7.id, 3)

    def test_B_json_string(self):
        r1 = Rectangle(10, 7, 2, 8, 1)
        dic = r1.to_dictionary()
        jsonDic = Base.to_json_string([dic])
        self.assertEqual(type(jsonDic), str)

    def test_C_json_string2(self):
        r1 = Rectangle(10, 7, 2, 8, 1)
        dic = r1.to_dictionary()
        jsonDic = Base.to_json_string([dic])
        list = json.loads(jsonDic)
        self.assertEqual(list, [dic])

if __name__ == "__main__":
    unittest.main()
