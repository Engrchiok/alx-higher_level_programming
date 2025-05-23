#!/usr/bin/python3
"""This module contains a class `Rectangle` that defines a rectangle."""


class Rectangle:
    """This is a class `Rectangle` that defines a rectangle.
    With Private instance attribute `width`.
    And with Private instance attribute `height`.

    Attribute:
        count (int): The number of the objects of the class instantiated.

    """

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """This is the Instantation method.

            Args:
                width (int, optional): This is the width of the triangle.
                It has a default value of 0.
                It's optional value must be an integer and not less than zero.
                heigth (int, optional): This is the heigth of the triangle.
                It has a default value of 0.
                It's optional value must be an integer and not less than zero.

        """

        self.width = width
        self.height = height
        type(self).number_of_instances += 1

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

    def area(self):
        """int: Returns the rectangle area."""

        return (self.width * self.height)

    def perimeter(self):
        """int: Returns the rectangle perimeter."""

        if self.width == 0 or self.height == 0:
            return 0
        return ((self.width + self.height) * 2)

    def __str__(self):
        a = str()
        if self.width == 0 or self.height == 0:
            return a
        else:
            for _ in range(self.__height):
                a += "#" * self.__width
                if _ < self.__height - 1:
                    a += "\n"
        return a

    def __repr__(self):
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
