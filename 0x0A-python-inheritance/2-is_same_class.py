#!/usr/bin/python3
"""This module contains a function with Prototype
`def is_same_class(obj, a_class):`
that returis ``True`` if the object is exactly
an instance of the specified class ; otherwise ``False``.
"""


def is_same_class(obj, a_class):
    """function that returns ``True`` if the object is exactly an instance
    of the specified class ; otherwise ``False``.
    """

    if type(obj) is a_class:
        return True
    else:
        return False
