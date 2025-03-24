#!/usr/bin/python3
"""This module contains a function that adds 2 integers.

>>> add_integer(2,1)
3
>>> add_integer(2)
100
"""

def add_integer(a, b=98):
    """Function that adds 2 integers.
    a and b must be integers or floats, otherwise raise a TypeError exception with the message 'a must be an integer or b must be an integer'
    a and b must be first casted to integers if they are float

    Returns:
        int: the addition of a and b

    """

    if float is not type(a) is not int:
        raise TypeError("a must be an integer")
    elif int is not type(b) is not float:
        raise TypeError("b must be an integer")
    else:
        if type(a) is float:
            a = int(a)
        if type(b) is float:
            b = int(b)
    return (a + b)

