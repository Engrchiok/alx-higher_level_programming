#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        a / b
    except ZeroDivisionError:
        return None
    else:
        return (a / b)
    finally:
        if b:
            print("Inside result: {}".format(a/b))
        else:
            print("Inside result: {}".format('None'))
