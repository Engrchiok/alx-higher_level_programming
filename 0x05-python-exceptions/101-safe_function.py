#!/usr/bin/python3
def safe_function(fct, *args):
    try:
        return fct(*args)
    except Exception as e:
        with open("/dev/stderr", "w") as stderr:
            stderr.write("Exception: {}\n".format(e))
        return None
