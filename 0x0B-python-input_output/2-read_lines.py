#!/usr/bin/python3
"""function that reads n lines of a text file """


def read_lines(filename="", nb_lines=0):
    """ reads nb_lines number of lines, if nb_lines <= 0, reads all """
    with open(filename, 'r') as f:
        lines = sum(1 for line in f)
    if nb_lines <= 0:
        nb_lines = lines
    i = 0
    with open(filename, 'r') as f:
        for line in f:
            i += 1
            if (i > nb_lines):
                break
            print("{:s}".format(line[:-1], end=""))
