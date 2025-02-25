#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    a, b = str(), 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end='')
        except (ValueError, TypeError):
            pass
        else:
            a = a + str(i)
    print()
    for _ in a:
        b += 1
    return b
