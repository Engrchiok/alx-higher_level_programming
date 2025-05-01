#!/usr/bin/python3
"""This is a Module that contains a function with prototype
`def is_kind_of_class(obj, a_class):` that returns ``True`` if the object is
an instance of, or if the object is an instance of a class that inherited
from, the specified class ; otherwise ``False``.
"""


def is_kind_of_class(obj, a_class):
    """A function that returns ``True`` if the object is an instance of, or if
    the object is an instance of a class that inherited from the specified
    class, otherwise ``False``.

    Args:
        obj (object): Parameter can be any instantiated object of any class.
        a_class (class): This parameter is the class that is referenced to
        whether the first parameter `obj` is an instance of it.

    Returns:
        True: if the object is an instance of, or if the object is an instance
        of a class that inherited from the specified class.
        False: if otherwise.

    """

    if isinstance(obj, a_class):
        return True
    else:
        return False
