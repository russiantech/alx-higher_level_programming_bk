#!/usr/bin/python3
"""Squar class definition."""


class Square:
    """Reps this  square class."""

    def __init__(self, size=0):
        """Initialize a new square.
        Args:
            size (int): size of this new square.
        """
        self.size = size

    @property
    def size(self):
        """will Get or set current size of this square."""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """ will return current area of this square."""
        return (self.__size * self.__size)
