#!/usr/bin/python3
"""
Print x elememts of a list.
Args:
        my_list (list) : list of  elements
        x (int): num of elements to print from my_list.

    Returns: num of elements printed.
"""


def safe_print_list(my_list=[], x=0):
    ret = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            ret += 1
        except IndexError:
            break
    print("")
    return (ret)
