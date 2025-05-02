#!/usr/bin/python3
"""This module contains a class ``BaseGeometry`` that inherits from `object`
class as its parent class."""


class BaseGeometry(object):
    """A class inheriting from `object` class as its parent class"""

    def area(self):
        """This is a class method.

        Raises:
            Exception: With message, ``area() is not implemented``.

        """

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """This is a class method that validates `value`.

        Args:
            name: This is the name of the value object.
            value: This is object value being validated.

        Raises:
            TypeError: if ``value`` is not an integer.
            ValueError: if ``value`` is less than or equal to zero.

        """

        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError(f"{name} must be greater than 0")
        else:
            return value


class Rectangle(BaseGeometry):
    """This is a class that inherits from ``BaseGeometry``"""

    def __init__(self, width, height):
        self.__width = self.integer_validator("width", width)
        self.__height = self.integer_validator("height", height)
