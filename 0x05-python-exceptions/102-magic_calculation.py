#!/usr/bin/python3
"""
    Write the Python function def magic_calculation(a, b): 
    that does exactly the same as the Python bytecode
    in Holberton advanced python Exception project
    9. ByteCode -> Python #4
"""


def magic_calculation(a, b):
    result = 0
    for i in range(1, 3):
        try:
            if i > a:
                raise Exception('Too far')
            else:
                result += a ** b / i
        except:
            result = b + a
            break
    return (result)
