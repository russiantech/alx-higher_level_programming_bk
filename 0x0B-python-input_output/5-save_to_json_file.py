#!/usr/bin/python3
"""Save/write a json to a text file"""
import json


def save_to_json_file(my_obj, filename):
    """Save a json object to text file using JSON repr."""
    with open(filename, "w") as f:
        json.dump(my_obj, f)
