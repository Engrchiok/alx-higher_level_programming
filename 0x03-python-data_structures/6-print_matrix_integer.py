#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    '''prints matrix of integers'''
    a, b = 0, 0
    for i in matrix:
        for i in matrix[a]:
            print("{:d}".format(i), end = "")
            b += 1
            if len(matrix[a]) > b:
                print(" ", end ="")
        a += 1
        b = 0
        print("")
