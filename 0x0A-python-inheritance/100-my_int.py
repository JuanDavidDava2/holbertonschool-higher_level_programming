#!/usr/bin/python3
"""class MyInt that inherits from int"""


class MyInt(int):
    """class MyInte"""

    def __eq__(self, value):
        return self.real != value

    def __ne__(self, value):
        return self.real == value
