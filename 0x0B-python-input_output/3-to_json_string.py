#!/usr/bin/python3
""" Converts a str to json"""
import json


def to_json_string(my_obj):
    """Return json repr of a str object."""
    return json.dumps(my_obj)
