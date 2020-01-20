#!/usr/bin/python3
"""
class MyList that inherits from list:
"""


class MyList(list):
    """initialize MyList"""
    def _init_(self):
        pass
    """print list"""
    def print_sorted(self):
        print(sorted(self))
