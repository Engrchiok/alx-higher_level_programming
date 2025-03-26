#!/usr/bin/python3
"""This module contains a function that adds 2 integers.

>>> add_integer(2,1)
3
>>> add_integer(2)
100

The function parameters, `a` and `b` must be integers or floats, otherwise raise a TypeError exception with the message 'a must be an integer or b must be an integer'.
`a` and `b` must be first casted to integers if they are float.
"""

def add_integer(a = None, b=98):
    """Function that adds 2 integers.

    Args:
        a (int): First parameter, which is a positional argument..
        b (int): Second parameter, which is a default argument set to integer `3`.

    Returns:
        int: the addition of a and b.

    Raises:
        TypeError: The arguments a and b for the function, must be an Integer or a float.

    """

    if float is not type(a) is not int: #a must be integers or floats
        raise TypeError("a must be an integer")

    elif int is not type(b) is not float: #b must be integers or floats
        raise TypeError("b must be an integer")

    else:
        if type(a) is float: #a must be first casted to integers if they are float
            a = int(a)
        if type(b) is float: #b must be first casted to integers if they are float
            b = int(b)

    return (a + b)

