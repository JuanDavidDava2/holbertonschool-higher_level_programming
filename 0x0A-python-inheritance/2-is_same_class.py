#!/usr/bin/python3
"""
check if they are of the same class
"""


def is_same_class(obj, a_class):
    """return True if is the same class otherwise False."""
    if type(obj) is a_class:
        return True
    else:
        return False
