#!/usr/bin/python3
"""This module contains a class ``BaseGeometry`` that inherits from `object`
class as its parent class."""

BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """This is a class that inherits from ``BaseGeometry``"""

    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.__width = width

        self.integer_validator("height", height)
        self.__height = height
