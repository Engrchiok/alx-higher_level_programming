#!/usr/bin/python3
"""
This is a module whose content is only one class, named Square.
"""

class Square:
    """
    This is a class that creates a square class object.
    """

    def __init__(self, size):
        """This is the instantion function of the class `Square`.

        Args:
            self: The first parameter which represents the instantiated object.
            size (int): The second parameter.

        """
        
        self.__size = size
        """
        int: Class instatiation function private variable.
        """

