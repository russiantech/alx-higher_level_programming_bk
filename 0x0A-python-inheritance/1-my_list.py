#!/usr/bin/python3
"""MyList class inherits from list in python"""


class MyList(list):
    """Sort the built-in list class."""

    def print_sorted(self):
        """list in sorted asc order."""
        print(sorted(self))
