#!/usr/bin/python3
def search_replace(my_list, search, replace):
    n_list = my_list.copy()
    for i in range(0, len(n_list)):
        if n_list[i] == search:
            n_list[i] = replace
    return n_list
