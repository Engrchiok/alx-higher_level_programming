#!/usr/bin/python3
"""This module contains a function with prototype
``def inherits_from(obj, a_class)`` that returns `True` if the object is an
instance of a class that inherited (directly or indirectly) from the specified
class, otherwise `False`.
"""


def inherits_from(obj, a_class):
    """A function that returns `True` if the object is an instance of a class
    that inherited (directly or indirectly) from the specified class,
    otherwise False.

    Args:
        obj (instance): This is the object whose inherited classes are being
        checked. It can be any object type.
        a_class (class): This is the inherited class that the object is being
        referenced, whether it was derived from it or not.

    Returns:
        True: if the object is an instance of a class that inherited
        (directly or indirectly) from the specified class.
        False: if otherwise.

    """

    if issubclass(type(obj), a_class) and type(obj) is not a_class:
        return True
    else:
        return False
