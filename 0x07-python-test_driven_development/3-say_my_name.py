#!/usr/bin/python3
# 3-say_my_name.py
""" defines/creates a func that prints a name"""


def say_my_name(first_name, last_name=""):
    """ simply print a name.

    Args:
        first_name (str): 1stname to print.
        last_name (str): lastname to print.
    Raises:
        TypeError: If (first_name/last_name) is'nt a str.
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
