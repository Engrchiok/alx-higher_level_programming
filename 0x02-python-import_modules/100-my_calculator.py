#!/usr/bin/python3

"""Imports all functions and handles basic operations."""
if __name__ == "__main__":
    from sys import argv
    from calculator_1 import add, sub, mul, div
    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit (1)
    if argv[2] != "+" and argv[2] != "-" and argv[2] != "/" and argv[2] != "*":
        print("Unknown operator. Available operators: +, -, * and /", argv[2])
        exit (1)
    a,b,c = int(argv[1]), argv[2], int(argv[3])
    print(f"{a} {b} {c} = {a + c if b == '+' else a - c if b == '-' else a * c if b == '*' else a / c}")
