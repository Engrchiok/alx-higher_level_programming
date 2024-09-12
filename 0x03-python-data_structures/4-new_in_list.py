#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    '''returns a copy of list replaced at an index'''
    a = my_list[:]
    a[idx] = element
    return (a)
