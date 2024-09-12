#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    '''prints integers reversed'''
    b = -1
    for i in my_list:
        print("{}".format(my_list[b]))
        b -= 1
