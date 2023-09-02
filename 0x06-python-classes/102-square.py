#!/usr/bin/python3
"""class Square."""


class Square:
    """Repr  square."""

    def __init__(self, size=0):
        """Inits new square.
        Args:
            size (int): size of this new square.
        """
        self.size = size

    @property
    def size(self):
        """ will get or set current size for this square."""
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

    def __eq__(self, other):
        """ def == comparision to Square."""
        return self.area() == other.area()

    def __ne__(self, other):
        """ def != comparison to Square."""
        return self.area() != other.area()

    def __lt__(self, other):
        """ def < comparison to Square."""
        return self.area() < other.area()

    def __le__(self, other):
        """ def  <= comparison to Square."""
        return self.area() <= other.area()

    def __gt__(self, other):
        """ def > comparison to Square."""
        return self.area() > other.area()

    def __ge__(self, other):
        """ def >= compmarison to Square."""
        return self.area() >= other.area()
