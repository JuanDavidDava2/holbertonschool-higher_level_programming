#!/usr/bin/python3
"""
finds a peak in a list of unsorted integers.
"""


def find_peak(list_of_integers):
    list_ = list_of_integers
    if list_ == []:
        return
    if list_ and isinstance(list_, list):
        return max(list_)
    return
