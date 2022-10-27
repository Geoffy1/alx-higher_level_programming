#!/usr/bin/python3
"""It inherits from the list class"""


class MyList(list):
    """A class inheriting from list"""
    def print_sorted(self):
        """prints a sorted list"""
        print(sorted(self))
