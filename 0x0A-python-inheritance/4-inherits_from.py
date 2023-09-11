#!/usr/bin/python3
""" Checks An Inherited Class."""


def inherits_from(obj, a_class):
    """is an object an inherited instance of a class?

    Args:
        obj (any): The object to check.
        a_class (type): class to match with type of obj with
    Returns:
        (True) if obj is inherited instance of a_class.
        Else (False).
    """

    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
