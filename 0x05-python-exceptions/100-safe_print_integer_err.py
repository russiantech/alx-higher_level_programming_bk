#!/usr/bin/python3

import sys

"""
    Print an int using "{:d}".format().

    If ValueError occurs, print corresponding
    err msg to standard erro(stderr.)

    Args:
        value (int): int to print.

    Returns:
        If(TypeError|ValueError occurs) 0 else 1
"""


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return (True)
    except (TypeError, ValueError):
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return (False)
