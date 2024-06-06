#!/usr/bin/python3
"""Python module that prints the result of the addition of all arguments"""
if __name__ == "__main__":
    from sys import argv
    result = 0
    for a in range(1, len(argv)):
        result += int(argv[a])
    print(f"{result}")
