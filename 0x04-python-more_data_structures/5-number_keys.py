#!/usr/bin/python3
# returns the num of keys in a dict.
def number_keys(a_dictionary):
    num = 0
    list_keys = list(a_dictionary.keys())

    for i in list_keys:
        num += 1

    return (num)
