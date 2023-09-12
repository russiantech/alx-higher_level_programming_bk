#!/usr/bin/python3
"""Read & Print To STDOUT."""


def read_file(filename=""):
    """ print UTF8 file to stdout."""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
