#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    '''returns a copy of list replaced at an index'''
    if idx < 0:
        return (my_list)
    elif idx >= len(my_list):
        return (my_list)
    else:
        a = my_list[:]
        a[idx] = element
        return (a)
