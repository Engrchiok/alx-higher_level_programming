#!/usr/bin/python3
"""This module is for a function that prints My name is <first name> <last name>.
The Prototype is `def say_my_name(first_name, last_name=""):`
first_name and last_name must be strings otherwise, raise a TypeError exception with the message first_name must be a string or last_name must be a string
"""

def say_my_name(first_name, last_name=""):
    """Function that prints a given first name and last name.

    args:
        first_name (str): This is expected to be the first name.
        last_name (str): This is expected to be the last name.

    Raises:
        TypeError: if first_name or last_name is not a string.

    """

    if type(first_name) is not str: #first_name must be a string
        raise TypeError("first_name must be a string")
    elif type(last_name) is not str: #last_name must be a string
        raise TypeError("last_name must be a string")
    else:
        print(f"My name is {first_name} {last_name}")
