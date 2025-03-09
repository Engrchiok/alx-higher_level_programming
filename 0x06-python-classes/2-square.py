#!/usr/bin/python3
"""
This is a module whose content is only one class, named Square.
"""

class Square:
    """This is a class that creates a square class object."""

    def __init__(self, size=0):
        """This is the instantion function of the class Square.

        Args:
            size (int): This parameter determines the size of the square. It's the length of each side of the square.

        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
            """int: Special attribute needed for computing the size of the square."""

