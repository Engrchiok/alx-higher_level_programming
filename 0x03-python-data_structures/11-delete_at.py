#!/usr/bin/python3

def delete_at(my_list=[], idx=0):
    if idx < 0 or idx >= len(my_list):
        return (my_list)
    del my_list[idx]
    return (my_list)
    '''deletes an item at a specific position in a list'''
"""    a = 0
    b = len(my_list)
    for i in my_list:
        if a != idx:
            my_list[a] = i
            a += 1
        else:
            idx = None
    if b > a:
        lst = my_list[:-1]
        my_list.clear()
        my_list.insert(0, lst)
    return (lst)"""
#    del my_list[idx]
#    return (my_list)
