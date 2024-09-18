#!/usr/bin/python3

def search_replace(my_list, search, replace):
    """ replaces all occurrences of an element by another in a new list """
    res = list(map(lambda x: x if x != search else replace, my_list))

#    res = [x if x != search else replace for x in my_list]

#    res = my_list[:]
#    a = 0
#    for i in res:
#        if i == search:
#            res[a] = replace
#        a += 1
    return (res)
