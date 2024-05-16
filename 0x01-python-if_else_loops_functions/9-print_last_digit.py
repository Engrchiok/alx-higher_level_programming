#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        lstd = (-number) % 10
    else:
        lstd= number % 10
    print(f"{lstd}", end="")
    return lstd
