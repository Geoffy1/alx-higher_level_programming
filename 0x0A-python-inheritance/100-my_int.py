#!/usr/bin/python3
"""100-my_int.
Creates a class to inherit from int.
"""


class MyInt(int):
    """Class inheriting,
    Then reverses behavior of != and ==.
    """

    def __eq__(self, other):
        """Equality becomes inequality."""

        return super().__ne__(other)

    def __ne__(self, other):
        """Inequality becomes equality."""

        return super().__eq__(other)
