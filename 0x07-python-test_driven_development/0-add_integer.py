#!/usr/bin/python3
"""
This module has one funct that adds up 2 int
"""


def add_integer(a, b=98):
    """Return the sum of two integers or floats as ints
    Args:
        a: first
        b: second
    Returns:
        Sum of the 2 args
    Raises:
        TypeError: If either of the args not an int or a float
    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
