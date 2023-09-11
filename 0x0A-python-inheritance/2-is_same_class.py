#!/usr/bin/python3
""" chcek a class"""


def is_same_class(obj, a_class):
    """Is an object(obj) === an instance(a_class) of a given class?

    Args:
        obj (any): object in check
        a_class (type): class to match the type of obj to.
    Returns:
        True if obj ===  an instance of a_class else False
    """

    if type(obj) == a_class:
        return True
    return False
