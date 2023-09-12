#!/usr/bin/python3
"""loads/reads an object as json."""
import json


def load_from_json_file(filename):
    """load Python object from a json data repr."""
    with open(filename) as f:
        return json.load(f)
