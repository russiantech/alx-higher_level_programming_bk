#!/usr/bin/python3
""" def a Rectangle class."""


class Rectangle:
    """Reprs rectangle."""

    def __init__(self, width=0, height=0):
        """Inits a new Rectangle.

        Args:
            width (int): our new rectangle's width.
            height (int): our new rectangle's height.
        """

        self.width = width
        self.height = height

    @property
    def width(self):
        """ will create/return  width of or rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """define/returns height of our rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
