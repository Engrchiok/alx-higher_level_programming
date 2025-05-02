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
