#!/usr/bin/python3
"""defines new Rectangle class for us"""


class Rectangle:
    """
    -repr our Rectangle.
    Attr:
        number_of_instances (int): num of our Rectangle instances.
        print_symbol (any): symbol used for our str repr.
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        -Inits new Rectangle.
        Args:
            width (int): width of our new rectangle.
            height (int): height of our new rectangle.
        """

        type(self).number_of_instances += 1
        self.width = width
        self.height = height

    @property
    def width(self):
        """ set n return width of our Rectangle."""
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
        """ will set/retrieve height for/of our Rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ will return area of our Rectangle."""
        return (self.__width * self.__height)

    def perimeter(self):
        """ will return perimeter of our Rectangle."""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        returns our Rectangle having greater area.
        Args:
            rect_1 (Rectangle): 1st Rectangle.
            rect_2 (Rectangle): 2nd Rectangle.
        Raises:
            TypeError: when none of (rect_1/rect_2) is actually a Rectangle.
        """

        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return (rect_1)
        return (rect_2)

    @classmethod
    def square(cls, size=0):
        """ will return our new Rectangle having width n height === size.
        Args:
            size (int): width n height of our new Rectangle.
        """

        return (cls(size, size))

    def __str__(self):
        """ str repr of our Rectangle.
        -repr our rectangle with char '#'
        """

        if self.__width == 0 or self.__height == 0:
            return ("")

        rect = []
        for i in range(self.__height):
            [rect.append(str(self.print_symbol)) for j in range(self.__width)]
            if i != self.__height - 1:
                rect.append("\n")
        return ("".join(rect))

    def __repr__(self):
        """ str repr of our Rectangle."""
        rect = "Rectangle(" + str(self.__width)
        rect += ", " + str(self.__height) + ")"
        return (rect)

    def __del__(self):
        """when a Rectangle is deleted, print a msg."""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
