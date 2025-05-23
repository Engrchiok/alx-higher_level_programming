#!/usr/bin/python3
"""This module contains a class `Rectangle` that defines a rectangle."""


class Rectangle:
    """This is a class `Rectangle` that defines a rectangle.
    With Private instance attribute `width`.
    And with Private instance attribute `height`.

    Attribute:
        count (int): The number of the objects of the class instantiated.
        print_symbol (str): This is the symbol that print() and str() returns.

    """

    number_of_instances = 0
    print_symbol = '#'

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
                a += str(self.print_symbol) * self.__width
                if _ < self.__height - 1:
                    a += "\n"
        return a

    def __repr__(self):
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        type(self).number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """This is a Static method, ``def bigger_or_equal(rect_1, rect_2)``.
        It returns the biggest rectangle based on the area.

        Args:
            rect_1: This is the first positional parameter.
            it must be the area of an object of class `Rectangle`.
            rect_2: This is the first positional parameter.
            It must be the area of an object of class `Rectangle`.

        Raises:
            TypeError: If either rect_1 or rect_2 is not of class `Rectangle`.

        Returns:
            int: The biggest area between the two Rectangle objects.
            Or the equal area if they are both equal.

        """

        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        elif type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        elif rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """Class method with prototype ``def square(cls, size=0)``.
        Returns a new Rectangle instance with width == height == size.

        Args:
            size (int): The only parameter of the class method.
            And it has a default value of zero.

        """

        return cls(size, size)
