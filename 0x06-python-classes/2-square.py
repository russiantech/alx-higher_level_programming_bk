#!/usr/bin/python3
""" Square class definition"""


class Square:
    """Res a square."""

    def __init__(self, size=0):
        """Inits a new Square.
        Args:
            size (int): size of new square class.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
