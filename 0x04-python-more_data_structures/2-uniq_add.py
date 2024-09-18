#!/usr/bin/python3

def uniq_add(my_list=[]):
    """ adds all unique integers in a list """
    a = list(set(my_list))
    b = 0
    for i in a:
        b += i
    return (b)
