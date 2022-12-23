#!/usr/bin/python3
"""
Contain a fn that prints a square
"""


def print_square(size):
    """This fn prints a square with the character #
    Args:
        size (int): This reps the length of the square
    Raises:
        TypeError: If size is not an int
        TypeError: If size is a float and less than 0
        ValueError: If size is less than 0
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    elif isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    for n in range(0, size):
        for m in range(size):
            print("#", end="")
        print("")
