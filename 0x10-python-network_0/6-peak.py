#!/usr/bin/python3
"""
finds a peak in a list of unsorted integers.
"""


def find_peak(list_of_integers):
    len_list = len(list_of_integers)
    if len_list == 0:
        return

    mid = len_list // 2
    left = list_of_integers[mid - 1]
    pivot = list_of_integers[mid]

    if(mid == len_list - 1 or pivot >= list_of_integers[mid + 1]) and\
      (mid == 0 or pivot >= left):
        return pivot

    elif mid != len_list - 1 and list_of_integers[mid + 1] > pivot:
        return (find_peak(list_of_integers[mid + 1:]))
    return(find_peak(list_of_integers[:mid]))
