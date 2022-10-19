#!/usr/bin/python3
"""Task 5-rectangle
Defs a Rect class.
"""


class Rectangle:
    """Rect class defd by width and height."""

    def __init__(self, width=0, height=0):
        """Initializes a Rect inst.
        Args:
            width: width of the rect
            height: height of the rect
        """
        self.width = width
        self.height = height

    def __str__(self):
        """Returns a printable string representation
        of a Rect inst, filled with the '#' character."""
        if self.__height == 0 or self.__width == 0:
            return ''
        rec_str = ''
        for i in range(self.__height):
            for j in range(self.__width):
                rec_str += '#'
            rec_str += '\n'
        return rec_str[:-1]

    def __repr__(self):
        """Return a string representation of a Rect inst
        able to recreate a new instance by using eval()
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Deletes a Rect inst"""
        print("Bye rectangle...")

    @property
    def width(self):
        """Retrieves the width of a Rect inst."""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width of a Rect inst
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
        """Retrieves the height of a Rect inst."""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height of a Rect inst
        Args:
            value: value of the +height
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculates the area of a Rect inst
        Returns:
            Area of the the rect
        """
        return self.__width * self.__height

    def perimeter(self):
        """Calculates the perimeter of a Rect inst
        Returns:
            Perimeter of the rect
        """
        if self.__height == 0 or self.__width == 0:
            return 0
        return 2 * (self.__width + self.__height)
