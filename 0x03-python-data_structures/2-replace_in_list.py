#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    ''' function replaces list element at an index '''
    if idx < 0:
        return (my_list)
    elif idx >= len(my_list):
        return (my_list)
    else:
        my_list[idx] = element
        return (my_list)
