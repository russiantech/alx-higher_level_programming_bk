#!/usr/bin/python3
"""adds attributes to an objects(obj)"""


def add_attribute(obj, att, value):
    """add an attribute to an object.

    Args:
        obj (any): object to add an attr to.
        att (str): name of attr to add to obj.
        value (any): value of att.
    Raises:
        TypeError: where attr of obj cannot be added.
    """

    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
