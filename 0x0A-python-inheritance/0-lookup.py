#!/usr/bin/python3
"""0-lookup
A list of available attr and methods of an object.
"""


def lookup(obj):
    """Returns that list of attr and methods.
    Args:
        - obj: object
    """

    return dir(obj)
