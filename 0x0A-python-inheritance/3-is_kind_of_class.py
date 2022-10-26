#!/usr/bin/python3
"""3-is_kind_of_class.
"""


def is_kind_of_class(obj, a_class):
    """Finds if obj is an instance of a_class or a class
    is inherited.
    Args:
        - obj: object
        - a_class: class to eval
    Returns: True or False
    """

    return isinstance(obj, a_class)
