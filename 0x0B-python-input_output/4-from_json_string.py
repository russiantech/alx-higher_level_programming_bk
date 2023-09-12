#!/usr/bin/python3
# 6-from_json_string.py
"""python object repr of a json str"""
import json


def from_json_string(my_str):
    """Return Python object repr of a json str."""
    return json.loads(my_str)
