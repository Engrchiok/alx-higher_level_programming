#!/usr/bin/python3
"""This module contains a class `Rectangle` that defines a rectangle."""


class Rectangle:
    """Rectangle class, with Private instance attributes `width` & `height`."""

    def __init__(self, width=0, height=0):
        """This is the Instantation method.

            Args:
                width (int, optional): The width of the triangle.
                It has a default value oy zero.
                heigth (int, optional): The heigth of the triangle.
                It has a default value oy zero.

        """

        self.width = width
        self.height = height

    @property
    def width(self):
        """int: The getter method returns the property value of width.
        The setter method ensures the set value for the property is an integer.
        And not less than zero.

            Raises:
                TypeError: If width is not an integer.
                ValueError: If width is less than zero.

        """

        return self.__width

    @property
    def height(self):
        """int: The getter method returns the property value of width.
        The setter method ensures the set value for the property is an integer.
        And not less than zero.

            Raises:
                TypeError: If width is not an integer.
                ValueError: If width is less than zero.

        """

        return self.__height

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
