#!/usr/bin/python3
# magi_calculation does same thing as the commented block below
""" 3           0 LOAD_CONST               1 (98)
 3 LOAD_FAST                0 (a)
 6 LOAD_FAST                1 (b)
 9 BINARY_POWER
10 BINARY_ADD
3           0 LOAD_CONST               1 (98)
 3 LOAD_FAST                0 (a)
 6 LOAD_FAST                1 (b)
 9 BINARY_POWER
10 BINARY_ADD
11 RETURN_VALUE 11 RETURN_VALUE
 """


def magic_calculation(a, b):
    return (98 + a ** b)
