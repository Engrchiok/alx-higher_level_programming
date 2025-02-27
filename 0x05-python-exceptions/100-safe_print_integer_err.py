#!/usr/bin/python3
from sys import stderr as erm
def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
    except Exception as e:
        print('Exception: ', e, file = erm)
        return False
    else:
        return True
