#!/usr/bin/python3
def uppercase(str):
    a = 0;
    while a < len(str):
        if str[a] >= 'a' and str[a] <= 'z':
            print("{}".format(chr(ord(str[a]) - 32)), end="")
        else:
            print("{}".format(str[a]), end="")
        a += 1
    print("".format())
