#!/usr/bin/python3

def no_c(my_string):
    '''removes all "c" and "C" characters'''
    if my_string == None:
        return
    if type(my_string) != str:
        return
    a = ""
    for i in my_string:
        if i == 'c' or i == 'C':
            continue
        else:
            a += i
    return (a)

