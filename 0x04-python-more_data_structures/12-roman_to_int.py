#!/usr/bin/python3

def roman_to_int(roman_string):
    """ converts a Roman numeral to an integer """
    if roman_string:
        if type(roman_string) is str:
            i = roman_string
            b = 0
            a = 0
            c = len(i)
            while b < c:
                if i[b] == 'I':
                    if b + 1 < c and i[b + 1] == 'V':
                        a += 4
                        b += 2
                    elif b + 1 < c and i[b + 1] == 'X':
                        a += 9
                        b += 2
                    else:
                        a += 1
                        b += 1
                elif i[b] == 'V':
                    a += 5
                    b += 1
                elif i[b] == 'X':
                    if b + 1 < c and i[b + 1] == 'L':
                        a += 40
                        b += 2
                    elif b + 1 < c and i[b + 1] == 'C':
                        a += 90
                        b += 2
                    else:
                        a += 10
                        b += 1
                elif i[b] == 'L':
                    a += 50
                    b += 1
                elif i[b] == 'C':
                    if b + 1 < c and i[b + 1] == 'D':
                        a += 400
                        b += 2
                    elif b + 1 < c and i[b + 1] == 'M':
                        a += 900
                        b += 2
                    else:
                        a += 100
                        b += 1
                elif i[b]  == 'D':
                    a += 500
                    b += 1
                elif i[b] == 'M':
                    a += 1000
                    b += 1
            return (a)
        else:
            return (0)
    else:
        return (0)
