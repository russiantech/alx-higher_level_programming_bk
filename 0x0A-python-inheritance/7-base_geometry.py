#!/usr/bin/python3
"""base geometry class BaseGeometry."""


class BaseGeometry:
    """Repr base geometry."""

    def area(self):
        """unimplemented for now"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate a param as an int.

        Args:
            name (str): name of param.
            value (int): param to validate.
        Raises:
            TypeError: when value is'nt an int.
            ValueError: If value is less than/equal to 0.
        """

        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
