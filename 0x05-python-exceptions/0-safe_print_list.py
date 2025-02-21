#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    for i in range(x):
        try:
            print(my_list[i], end='')
        except Exception:
            i -= 2
    print('')
    return int(i + 1)
