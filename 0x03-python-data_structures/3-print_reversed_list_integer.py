#!/usr/bin/python3
# print int in list in reverse-order

def print_reversed_list_integer(my_list=[]):
    if isinstance(my_list, list):
        my_list.reverse()
        for x in my_list:
            print("{:d}".format(x))
