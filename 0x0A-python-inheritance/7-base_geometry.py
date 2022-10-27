#!/usr/bin/python3
"""Defs a base geometry class BaseGeometry"""


class BaseGeometry:
    """Class reps a base geometry"""

    def area(self):
        """method still not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates a value as an int
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
