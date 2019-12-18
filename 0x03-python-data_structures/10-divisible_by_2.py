#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if my_list != [] or my_list is not None:
        out_list = my_list[:]
        j = 0
        for i in out_list:
            out_list[j] = i % 2 == 0
            j += 1
        return out_list
