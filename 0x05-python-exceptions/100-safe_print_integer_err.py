#!/usr/bin/python3
def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
    except (ValueError, TypeError) as e:
        with open("/dev/stderr", "w") as f:
            f.write("Exception: {} \n".format(e))
        return False
    return True
