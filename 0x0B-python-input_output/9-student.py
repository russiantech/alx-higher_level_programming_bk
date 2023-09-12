#!/usr/bin/python3
"""Our Student Class."""


class Student:
    """Reprs a student."""

    def __init__(self, first_name, last_name, age):
        """Inits a new Student.

        Args:
            first_name (str): student's first-name.
            last_name (str):student's last-name.
            age (int): student's age.
        """

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Get dict repr of the Student obj."""
        return self.__dict__
