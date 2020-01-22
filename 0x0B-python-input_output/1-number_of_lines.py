#!/usr/bin/python3
"""
function that returns the number of lines of a text file:
"""


def number_of_lines(filename=""):
    """ returns number of lines in file """
    with open(filename, 'r') as f:
        lines = sum(1 for line in f)
    f.closed
    return lines
