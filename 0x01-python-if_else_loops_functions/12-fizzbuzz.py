#!/usr/bin/python3
def fizzbuzz():
    a = 1
    while a <= 100:
        if a % 3 == 0 and a % 5 == 0:
            print("fizzbuzz ", end="")
        elif a % 3 == 0 and a % 5 != 0:
            print("fizz ", end="")
        elif a % 5 == 0 and a % 3 != 0:
            print("buzz ", end="")
        else:
            print(f"{a} ", end="")
        a += 1