#!/usr/bin/python3
import sys

def safe_print_integer_err(value):
    """
    Prints an integer and returns True if successful.
    Prints an error message to stderr and returns False if not an integer.
    """
    try:
        print("{:d}".format(value))
        return True
    except Exception as e:
        print("Exception: {}".format(e), file=sys.stderr)
        return False
