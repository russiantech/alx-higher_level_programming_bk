#!/usr/bin/python3
"""Still on  Square class"""


class Square:
    """Reps a square."""

    def __init__(self, size=0):
        """Inits a new square.
        Args:
            size (int): size of the new square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """will return current area of this square."""
        return (self.__size * self.__size)
