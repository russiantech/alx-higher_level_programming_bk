#!/usr/bin/python3
"""Module for finding max int in a list
"""


def max_integer(list=[]):
    """Find n return  max int in a list of ints
        If list  of ints ==[empty], None is returned
    """

    if len(list) == 0:
        return None
    result = list[0]
    i = 1
    while i < len(list):
        if list[i] > result:
            result = list[i]
        i += 1
    return result
