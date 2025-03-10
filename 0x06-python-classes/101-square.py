#!/usr/bin/python3
"""This is a module whose content is only one class, named Square."""

class Square:
    """This is a class that creates a square class object."""

    def __init__(self, size=0, position=(0, 0)):
        """This is the instantion function of the class Square.

        Args:
            size (int): This parameter determines the size of the square. It's the length of each side of the square.
            position: This parameter determines the cordinate position of the square object when printed.

        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
            """int: Special attribute needed for computing the size of the square."""

        if type(position) == tuple and len(position) == 2 and position[0] >= 0 <= position[1]:
            self.__position = position
            """int: This is a special attribute needed to specify the cordinate position the the square object."""

        else:
            raise TypeError('position must be a tuple of 2 positive integers')

    def area(self):
        """This is a method that returns the area of the instantiated square object.

        Returns:
            The area of the instantiated square object.

        """

        return (self.__size ** 2)

    @property
    def size(self):
        """The special attribute of size has a getter and setter method."""

        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def my_print(self):
        """This is a Square method that prints the Square object in #."""

        if self.__size == 0:
            print()
        else:
            print('\n' * self.__position[1], end='')
            for _ in range(self.__size):
                print(' ' * self.__position[0], '#' * self.__size, sep='')

    @property
    def position(self):
        """The special attribute of position, has a getter and setter method."""

        return self.__position

    @position.setter
    def position(self, value):
        if type(value) == tuple and len(value) == 2 and value[0] >= 0 <= value[1]:
            self.__position = value

    def __str__(self):
        """This is a special method that returns a default string of the object.

        Returns:
            The output of the self.my_print method.

        """

        if self.__size == 0:
            z = '\n'
        else:
            z = ('\n' * self.__position[1])
            for _ in range(self.__size):
                z += (' ' * self.__position[0]) + ('#' * self.__size)
                if _ < (self.__size - 1):
                    z += ('\n')
        return z
