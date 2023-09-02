#!/usr/bin/python3
""" class Square."""


class Square:
    """Reps a square."""

    def __init__(self, size):
        """Inits new square.
        Args:
            size (int): size of new square.
        """
        self.size = size

    @property
    def size(self):
        """will get or set current size of this square."""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """will return current area of this square."""
        return (self.__size * self.__size)

    def my_print(self):
        """will Print square with char #."""
        for i in range(0, self.__size):
            [print("#", end="") for j in range(self.__size)]
            print("")
        if self.__size == 0:
            print("")
