#!/usr/bin/python3
"""python class object/attr to json"""


def class_to_json(obj):
    """Returns dict repr of a simple data structure."""
    return obj.__dict__
