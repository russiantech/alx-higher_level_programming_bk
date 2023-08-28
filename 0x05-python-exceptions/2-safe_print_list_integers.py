#!/usr/bin/python3
"""
    Print 1st int  x elements of a list.

    Args:
        my_list (list): list of x elements.
        x (int): num of elements of my_list to print.

    Returns:
        numb of elements printed.
"""


def safe_print_list_integers(my_list=[], x=0):
    ret = 0
    for i in range(0, x):
        try:
            print("{:d}".format(my_list[i]), end="")
            ret += 1
        except (ValueError, TypeError):
            continue
    print("")
    return (ret)
