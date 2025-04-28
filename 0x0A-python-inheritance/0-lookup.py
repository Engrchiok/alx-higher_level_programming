#!/usr/bin/python3
"""Module of a function.
That returns the list of available attributes and methods of an object.
"""


def lookup(obj):
    """A function,
    that returns the list of available attributes and methods of an object.

    Args:
        obj (type): This argument is a class.

    Returns:
        list: returns the list of available attributes,
        and methods of an object.

    """

    return dir(obj)
