#!/usr/bin/python3
"""This Module solely contains a function that prints a text with 2 new lines after each of these characters: `.`, `?` and `:`.

Function Prototype: def text_indentation(text):
    text must be a string, otherwise raise a TypeError exception with the message text must be a string
    There should be no space at the beginning or at the end of each printed line

"""

def text_indentation(*string):
    """A function that prints a text with 2 new lines after each of these characters: `.`, `?` and `:`.
    The function Prototype is  `def text_indentation(text):`

    Args:
        text (str): The only argument needed in the function and it must be a string.

    Raises:
        TypeError: If text argument is not a string

    """

    if len(string) != 1: # making sure the right number of arguments is inputed into the function
        raise ValueError("text_indentaion function requires only one string argument")
    else:
        text = string[0]

    if type(text) is not str: # `text` argument must be a string
        raise TypeError("text must be a string")
    else:
        i = 0
        while i < len(text): # traversing through the string characters
            if text[i] == ' ': # making sure the first character(s) of a new line/paragrapgh isn't a space(s)
                i += 1
                continue
            elif text[i] != '.' or '?' != text[i] or ':' != text[i]: # printing characters till the end of the paragraph
                while i < len(text):
                    if text[i] == '.' or '?' == text[i] or ':' == text[i]:
                        break
                    else:
                        print(text[i], end="")
                        i += 1
                    if i == len(text):
                        break
                    #if text[i] == ' ' and (text[i+1] == '.' or text[i+1] == '?' or text[i+1] == ':'): 
                        #i += 1
                        #break
                    if text[i] == ' ' == text[i+1]: # making sure there are no spaces at the end of the paragraph
                        a = i
                        while i < len(text):
                            i += 1
                            if i == len(text): # text[i + 1] == '.' or text[i+1] == '?' or text[i+1] == ':':
                                # i += 1
                                break
                            if text[i+1] != ' ': #or text[i+1] != '.' or text[i+1] == '?' or text[i+1] == ':':
                                i = a
                                break
            if i != len(text):
                print(text[i], end="\n\n")
                i += 1
