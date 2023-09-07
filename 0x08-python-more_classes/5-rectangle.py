#!/usr/bin/python3
""" creates/defines our Rectangle class."""


class Rectangle:
    """Repr our rectangle."""

    def __init__(self, width=0, height=0):
        """Inits our new Rectangle.

        Args:
            width (int): width of our new rectangle.
            height (int): height of our new rectangle.
        """

        self.width = width
        self.height = height

    @property
    def width(self):
        """ get or se width of our Rectangle."""
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
        """ will get or set height of our Rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ returns area of our Rectangle."""
        return (self.__width * self.__height)

    def perimeter(self):
        """returns the perimeter of our Rectangle."""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        """
        returns printable repr of our Rectangle.
        repr our rectangle having the '#' char
        """

        if self.__width == 0 or self.__height == 0:
            return ("")

        rect = []
        for i in range(self.__height):
            [rect.append('#') for j in range(self.__width)]
            if i != self.__height - 1:
                rect.append("\n")
        return ("".join(rect))

    def __repr__(self):
        """ returns str repr of our Rectangle."""
        rect = "Rectangle(" + str(self.__width)
        rect += ", " + str(self.__height) + ")"
        return (rect)

    def __del__(self):
        """ prints msg for any deletion of our Rectangle."""
        print("Bye rectangle...")
