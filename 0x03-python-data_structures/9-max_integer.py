#!/usr/bin/python3

def max_integer(my_list=[]):
    '''finds the biggest integer of a list'''
    if my_list:
        a = my_list[0]
        for i in my_list:
            if i > a:
                a = i
        return (a)
    else:
        return (None)
