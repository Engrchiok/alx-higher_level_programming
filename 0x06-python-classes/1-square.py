#!/usr/bin/python3
"""This is a module whose content is only one class, named Square."""

class Square:
    """This is a class that creates a square class object."""

    def __init__(self, size):
        """This is the instantion function of the class `Square`.

        Args:
            size (int): This parameter determines the size of the square object instantiated.

        """
        
        self.__size = size
        """int: Class instatiation function private variable."""

