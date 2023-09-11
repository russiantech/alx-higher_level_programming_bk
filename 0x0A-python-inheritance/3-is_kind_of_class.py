#!/usr/bin/python3
"""check a class against an inherited instance"""


def is_kind_of_class(obj, a_class):
    """is an object (obj) an instance or \
            inherited instance of a class(a_class)?

    Args:
        obj (any): object to check.
        a_class (type): class to match the type of obj with
    Returns:
    True where obj is an instance or inherited instance of a_class
    Else False.
    """

    if isinstance(obj, a_class):
        return True
    return False
