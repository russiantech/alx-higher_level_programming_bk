#!/usr/bin/python3
"""Rectangle class that inherits from BaseGeometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Repr a rectangle that inherits from BaseGeometry."""

    def __init__(self, width, height):
        """Inits our new Rectangle.

        Args:
            width (int): width of our new Rectangle.
            height (int): height of our new Rectangle.
        """

        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """The area of our rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """print() & str() repr of a Rectangle."""
        string = "[" + str(self.__class__.__name__) + "] "
        string += str(self.__width) + "/" + str(self.__height)
        return string
