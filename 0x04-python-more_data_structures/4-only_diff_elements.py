#!/usr/bin/python3

def only_diff_elements(set_1, set_2):
    """ returns a set of all elements present in only one set """
    a = set()
    a.update(set_1)
    for i in set_2:
        if i not in set_1:
            a.add(i)
        else:
            a.remove(i)
    return (a)
