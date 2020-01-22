#!/usr/bin/python3
"""
function that writes a string to a text file.
"""


def write_file(filename="", text=""):
    """function that writes a string to a text file"""
    with open(filename, encoding="UTF-8", mode="w") as a_file:
        return a_file.write(text)
