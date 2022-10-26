#!/usr/bin/python3
"""2-is_same_class.
Checks if an object is an instance of a class.
"""


def is_same_class(obj, a_class):
    """Func to determine if obj is an instance of a_class.
    Args:
        - obj: object
        - a_class: class to verify
    Returns: True if obj is an instance of a_class,
    False if otherwise
    """

    return True if type(obj) is a_class else False
