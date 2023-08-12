#!/usr/bin/python3
from calculator_1 import add, sub
"""
 magic_calculation(a, b): that does exactly as
 Python bytecode in the question
"""


def magic_calculation(a, b):
    if a < b:
        c = add(a, b)
        for i in range(4, 6):
            c = add(c, i)
        return (c)
    else:
        return (sub(a, b))
