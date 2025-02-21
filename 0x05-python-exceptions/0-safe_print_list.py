#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    c, a = int(), str()
    for i in range(x):
        try:
            a = a + str(my_list[i])
        except IndexError:
            i -= 2
    print(a)
    for b in a:
        c += 1
    return c
