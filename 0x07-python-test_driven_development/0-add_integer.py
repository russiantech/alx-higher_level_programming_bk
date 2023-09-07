#!/usr/bin/python3
""" creates/defines an int addition function."""


def add_integer(a, b=98):
    """

    Return int addition of a and b.

    Float args are typecasted to int b4 addition is done.

    Raises:
        TypeError: WHen None of (a or b) is an integer and a float.
    """

    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
