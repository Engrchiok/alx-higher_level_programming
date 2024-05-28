#!/usr/bin/python3
def remove(str, n):
    a = list(str)
    b = list(str)
    j = 1
    for i in range(0, len(str)):
        if i == n:
            continue
        b[0] = a[i]
        j += 1
    c = "Ok" + eval(b)
    return c
