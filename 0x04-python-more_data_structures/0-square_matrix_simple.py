#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    """ computes the square value of all integers of a matrix """
    res = []
    for i in matrix:
        res.append(list(map(lambda x: x ** 2, i)))
    return (res)
