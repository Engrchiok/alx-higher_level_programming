#!/usr/bin/python3
def fizzbuzz():
    for a in range(1, 101):
        if a % 3 == 0 and a % 5 == 0:
            print("fizzbuzz ", end="")
        elif a % 3 == 0 and a % 5 != 0:
            print("fizz ", end="")
        elif a % 5 == 0 and a % 3 != 0:
            print("buzz ", end="")
        else:
            print("{} ".format(a), end="")
