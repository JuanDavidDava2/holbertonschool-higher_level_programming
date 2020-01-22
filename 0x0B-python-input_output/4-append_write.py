#!/usr/bin/python3
"""
function that appends a string at the end of a text file.
"""


def append_write(filename="", text=""):
    with open(filename, "a", encoding='utf-8') as f:
        return f.write(text)
