#!/usr/bin/python3
"""This module contains a class ``Square`` that inherits from `Rectangle`
class as its parent class."""

Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """This is a class that inherits from ``Rectangle``"""

    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(self.__size, self.__size)
