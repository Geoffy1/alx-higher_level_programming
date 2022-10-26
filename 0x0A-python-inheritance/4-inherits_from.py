#!/usr/bin/python3
"""4-inherits_from.
Finds if the object is an instance of a class that inherited
(directly or indirectly) from the specified class."""


def inherits_from(obj, a_class):
    """Det if obj is an instance of a class that is
    inherited.
    Args:
        - obj: object to consider
        - a_class: class to eval
    Returns: True or False
    """

    return isinstance(obj, a_class) and type(obj) != a_class
