#!/usr/bin/python3
""" Rectangle subclass Square."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Repr a square."""

    def __init__(self, size):
        """Inits our new square.

        Args:
            size (int): size of our new square.
        """

        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
