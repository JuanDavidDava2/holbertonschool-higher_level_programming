#!/usr/bin/python3
"""
function that reads a text file
"""


def read_file(filename=""):
    """ function that reads UTF8 file and prints to stdout """
    with open(filename, encoding='utf-8') as a_file:
        for i in a_file:
            print(i, end="")
