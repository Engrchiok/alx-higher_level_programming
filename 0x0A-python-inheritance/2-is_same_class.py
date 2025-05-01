#!/usr/bin/python3
"""This module contains a function with Prototype
`def is_same_class(obj, a_class):`
that returis ``True`` if the object is exactly
an instance of the specified class, otherwise ``False``.
"""


def is_same_class(obj, a_class):
    """function that returns ``True`` if the object is exactly an instance
    of the specified class, otherwise ``False``.

    Args:
        obj (object): Parameter can be any instantiated object of any class.
        a_class (class): This parameter is the class that is referenced to
        whether the first parameter `obj` is exactly an instance of it.

    Returns:
        True: if the object is exactly an instance of the specified class.
        False: if otherwise.
    """

    if type(obj) is a_class:
        return True
    else:
        return False
