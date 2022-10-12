#!/usr/bin/python3
"""a class Square to define a square
by: (based on 3-square.py)
"""


class Square:
    """Square class of private attribute -
    size.
    """

    def __init__(self, size=0):
        """Initializes the size variable as a private
        instance artribute
        """
        self.__size = size

    @property
    def size(self):
        """retrieves size of square"""
        return self.__size

    @size.setter
    def size(self, size_value):
        """Gets the set size"""
        self.__size = size_value

        if not isinstance(size_value, int):
            raise TypeError("size must be an integer")
        elif size_value < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """returns the current square area"""
        return self.__size ** 2
