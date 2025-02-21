#!/usr/bin/python3
if __name__ == main:
    def safe_print_list(my_list=[], x=0):
        for i in range(x):
            try:
                print(my_list[i], end='')
            except IndexError:
                i -= 2
        print('')
        return int(i + 1)
