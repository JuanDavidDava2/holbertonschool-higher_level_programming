#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    new = []
    if idx >= 0 and idx < len(my_list):
        new = my_list[:]
        new[idx] = element
        return new
    return my_list
