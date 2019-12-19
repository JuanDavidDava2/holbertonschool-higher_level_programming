#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    new = set(set_1 ^ set_2)
    return new
