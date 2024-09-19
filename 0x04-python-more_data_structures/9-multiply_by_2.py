#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    """ returns a new dictionary with all values multiplied by 2 """
    a = a_dictionary.copy()
    for i in a:
        a[i] *= 2
    return (a)
