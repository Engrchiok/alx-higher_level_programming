#!/usr/bin/python3
def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
    except Exception as e:
        print("Exception: {}".format(e), file = open("/dev/stderr", "w"))
        return False
    return True
