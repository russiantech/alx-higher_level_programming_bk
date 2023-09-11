#!/usr/bin/python3
""" MyInt clas inherits from int."""


class MyInt(int):
    """is int( == and !=) ?."""

    def __eq__(self, value):
        """Replace/Override (==) with (!=) behavior."""
        return self.real != value

    def __ne__(self, value):
        """Replace/Override (!=) with ( ==) behavior."""
        return self.real == value
