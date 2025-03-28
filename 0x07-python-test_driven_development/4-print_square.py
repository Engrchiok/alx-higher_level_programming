#!/usr/bin/python3
"""This module solely contains a function that prints a square with the character #.
Prototype: def print_square(size):.
size is the size length of the square
size must be an integer, otherwise raise a TypeError exception with the message size must be an integer
if size is less than 0, raise a ValueError exception with the message size must be >= 0
if size is a float and is less than 0, raise a TypeError exception with the message size must be an integer
"""

def print_square(size):
    """Function that prints a square with the character #.
    The function has a Prototype `def print_square(size):`.

    Args:
        size (int): The only argument of the function and it must be an integer.

    Raises:
        TypeError: if size is not an integer, or if size is a float and less than zero.
        ValueError: If size is less than zero

    """

    if type(size) is not int:
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    elif type(size) is float and size < 0:
        raise TypeError("size must be an integer")
    else:
        for length in range(size):
            for breadth in range(size):
                print("#", end="")
            print("")
