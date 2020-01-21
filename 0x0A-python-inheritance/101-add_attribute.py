#!/usr/bin/python3


def add_attribute(obj, att, val):
    """adds a new attribute"""
    if not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")
    setattr(obj, att, val)
