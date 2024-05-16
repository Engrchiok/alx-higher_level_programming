#!/usr/bin/python3
def uppercase(str):
    a = 0;
    while a < len(str):
        if str[a] >= 'a' and str[a] <= 'z':
            b = chr(ord(str[a]) - 32)
        else:
            b = str[a]
        print("{}".format(b), end="")
        a += 1
    print("".format())
