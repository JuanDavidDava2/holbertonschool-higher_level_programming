#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        llen = sum(1 for i in my_list)
        if llen < x:
            print(*my_list, sep="")
            return llen
        else:
            print(*my_list[:x], sep="")
            return x
    except:
        print("error")
