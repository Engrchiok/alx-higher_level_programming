#!/usr/bin/python3

def weight_average(my_list=[]):
    """ returns the weighted average of all integers tuple """
    if not my_list:
        return (0)
    else:
        a, b, c = my_list, 0, 0
        for i in a:
            b += i[0] * i[1]
            c += i[1]
        d = b / c
    return (d)
