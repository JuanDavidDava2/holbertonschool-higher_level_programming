#!/usr/bin/python3
"""
check if they are of the same class
"""


def is_kind_of_class(obj, a_class):
    """return True if is the same class otherwise False."""
    if isinstance(obj, a_class):
        return True
    else:
        return False
