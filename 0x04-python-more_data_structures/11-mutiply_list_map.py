#!/usr/bin/python3
""" returns a list with * val multiplied by a num\
        without using any loops."""


def multiply_list_map(my_list=[], number=0):
    return (list(map((lambda i: i * number), my_list)))
