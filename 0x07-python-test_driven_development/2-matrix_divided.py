#!/usr/bin/python3
"""This module contains a function with two parameters ``matrix`` and ``div``. This function is expected to divide all elements of a matrix.
``matrix`` must be a list of lists of integers or floats, otherwise raise a TypeError exception with the message `matrix must be a matrix (list of lists) of integers/floats`.
Each row of the `matrix` must be of the same size, otherwise raise a TypeError exception with the message `Each row of the matrix must have the same size`.
``div`` must be a number (integer or float), otherwise raise a TypeError exception with the message `div must be a number`.
``div`` can’t be equal to 0, otherwise raise a ZeroDivisionError exception with the message `division by zero`.
All elements of the matrix should be divided by ``div``, rounded to 2 decimal places.
"""

def matrix_divided(*inp):
    """This is a function called ``matrix_divided``, that divides all elements of a matrix.

    Args:
        matrix (list): the first parameter which is a list of lists.
        div (int): second and last parameter which is a divisor to all the element of the first parameter, ``matrix``.

    Returns:
        list: A new matrix, which is a list of a lists.

    Raises:
        TypeError: if matrix is not a matrix (list of lists) of integers/floats. if each row of the matrix is not the same size. if div is not a number
        ZeroDivisionError: if the division is by zero

    """

    if len(inp) != 2:
        raise Exception("This function requires two arguments")
    else:
        matrix, div = inp[0], inp[1]

    if type(matrix) is not list: #``matrix`` must be a list
        try:
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        except TypeError as t:
            return t
    elif type(matrix) is list:
        for i in range(len(matrix)):
            if type(matrix[i]) is not list: #``matrix`` must be a list of lists
                try:
                    raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
                except TypeError as t:
                    return t
            elif i > 0 and (len(matrix[i]) != len(matrix[i - 1])): #Each row of the `matrix` must be of the same size
                try:
                    raise TypeError("Each row of the matrix must have the same size")
                except TypeError as t:
                    return t
            else:
                try:
                    for n in matrix[i]:
                        if (int is not type(n) is not float): #``matrix`` must be a list of lists of integers or floats
                            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
                except TypeError as t:
                    return t
    
    if (float is not type(div) is not int): #``div`` must be a number (integer or float)
        try:
            raise TypeError("div must be a number")
        except TypeError as t:
            return t
    elif div == 0: #``div`` can’t be equal to 0
        try:
            raise TypeError("division by zero")
        except TypeError as t:
            return t
    else: #Returns a new matrix, which is a list of a lists
        newm = list()
        for i in range(len(matrix)):
            newm.append(list())
            for j in matrix[i]:
                newm[i].append(float(f"{(j/div):.2f}"))
        return newm
