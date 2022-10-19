#!/usr/bin/python3
"""Task 3-rectangle
Defs a Rectangle class.
"""


class Rectangle:
    """Rectangle class given by width and height."""

    def __init__(self, width=0, height=0):
        """Initializes a Rect.
        Args:
            width: width of the rect
            height: height of the rect
        """
        self.width = width
        self.height = height

    def __str__(self):
        """Returns a nice informal and printable string representation
        of a Rectangle instance, filled with the '#' character."""
        if self.__height == 0 or self.__width == 0:
            return ''
        rec_str = ''
        for i in range(self.__height):
            for j in range(self.__width):
                rec_str += '#'
            rec_str += '\n'
        return rec_str[:-1]

    @property
    def width(self):
        """Retrieves the width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width
        Args:
            value: value of the +width
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieves the height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height
        Args:
            value: value of the +height
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculates the area
        Returns:
            Area
        """
        return self.__width * self.__height

    def perimeter(self):
        """Calculates the perimeter
        Returns:
            Perimeter
        """
        if self.__height == 0 or self.__width == 0:
            return 0
        return 2 * (self.__width + self.__height)
