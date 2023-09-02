#!/usr/bin/python3
"""Def MagicClass that matches exactly a bytecode provided in this  Alx task"""

import math


class MagicClass:
    """Repr a circle."""

    def __init__(self, radius=0):
        """Inits  MagicClass.
        Arg:
            radius (float or int): radius of this new MagicClass.
        """

        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """ will return area of this MagicClass."""
        return (self.__radius ** 2 * math.pi)

    def circumference(self):
        """ will return circumference of this MagicClass."""
        return (2 * math.pi * self.__radius)
