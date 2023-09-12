#!/usr/bin/python3
""" def a class Student."""


class Student:
    """Stands for a student."""

    def __init__(self, first_name, last_name, age):
        """Inits a new Student.

        Args:
            first_name (str): student's 1st first-name
            last_name (str): student's last-name.
            age (int): student's age.
        """

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Get dict repr of the Student.
        If attrs is a list of str, represents only those attrbs
        in the list.

        Args:
            attrs (list): student attr to represent(optional).
        """

        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__
