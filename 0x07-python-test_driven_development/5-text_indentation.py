#!/usr/bin/python3
"""This Module solely contains a function that prints a text with 2 new lines after each of these characters: `.`, `?` and `:`.

Function Prototype: def text_indentation(text):
    text must be a string, otherwise raise a TypeError exception with the message text must be a string
    There should be no space at the beginning or at the end of each printed line

"""

def text_indentation(text):
    """A function that prints a text with 2 new lines after each of these characters: `.`, `?` and `:`.
    The function Prototype is  `def text_indentation(text):`

    Args:
        text (str): The only argument needed in the function and it must be a string.

    Raises:
        TypeError: If text argument is not a string

    """

    if type(text) is not str:
        raise TypeError("text must be a string")
    else:
        i = 0
        while i < len(text):
            if text[i] == ' ':
                i += 1
                continue
            elif text[i] != '.' or '?' != text[i] or ':' != text[i]:
                while i < len(text):
                    if text[i] == '.' or '?' == text[i] or ':' == text[i]:
                        break
                    else:
                        print(text[i], end="")
                        i += 1
                    if i == len(text):
                        break
                    if i == ' ' == (i+1):
                        a = i
                        while i < len(text):
                            i += 1
                            if (i + 1) == '.' or (i+1) == '?' or (i+1) == ':':
                                i += 1
                                break
                            if (i+1) != ' ' or (i+1) != '.' or (i+1) == '?' or (i+1) == ':':
                                i = a
                                break
            if i != len(text):
                print(text[i], end="\n\n")
                i += 1
