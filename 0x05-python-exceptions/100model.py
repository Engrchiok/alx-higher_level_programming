#!/usr/bin/python3
def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return True
    except Exception as e:
        with open("/dev/stderr", "w") as f:
            f.write("Exception: {} \n".format(e))
        return False
