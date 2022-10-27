#!/usr/bin/python3
"""Defines a function that adds attr to objs"""


def add_attribute(obj, att, value):
    """Adds a new attr to an obj if possible
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
