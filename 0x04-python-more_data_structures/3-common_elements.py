#!/usr/bin/python3

def common_elements(set_1, set_2):
    """ returns a set of common elements in two sets """
    a = set()
    for i in set_1:
        for j in set_2:
            if j == i:
                a.add(j)
    return (a)
