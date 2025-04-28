#!/usr/bin/python3
"""A Module that has a class `MyList` that inherits from `list`.
It has a Public instance method with prototype `def print_sorted(self)`,
that prints the list, but sorted (ascending sort)
All the elements of the list will be assumed to be of type int.
"""

class MyList(list):
    """A class `MyList` that inherits from `list`"""

    def print_sorted(self):
        """Method that prints the list, but sorted (ascending sort)"""

        print(sorted(self))
