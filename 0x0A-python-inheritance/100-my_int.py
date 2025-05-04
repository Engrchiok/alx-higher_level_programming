#!/usr/bin/python3
"""This is a module that contains a class ``MyInt`` that inherits from `int`.
``MyInt`` is a rebel. MyInt has `==` and `!=` operators inverted.
"""


class MyInt(int):
    """A class ``MyInt`` that inherits from `int`."""

    def __init__(self, value):
        self.value = value

    def __eq__(self, other):
        return (self.value != other)

    def __ne__(self, other):
        return (self.value == other)
