#!/usr/bin/python3
"""This module 1-rectangle
Defs a Rectangle class.
"""


class Rectangle:
    """Rect class def by width and height."""

    def __init__(self, width=0, height=0):
        """Initializes a Rect inst.
        Args:
            width: width
            height: height
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Retrieves the width of a Rect inst."""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width of a Rect inst
        Args:
            value: value of the width, a positive integer
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieves the height of a Rect inst."""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height of a Rect inst
        Args:
            value: value of the height,  a positive integer
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
