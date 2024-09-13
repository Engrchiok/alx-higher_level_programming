#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    '''finds all multiples of 2 in a list'''
    a, x = [], 0
    for i in my_list:
        if i % 2 == 0:
            a.append(True)
        else:
            a.append(False)
        x += 1
    return (a)
