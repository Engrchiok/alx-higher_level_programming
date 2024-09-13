#!/usr/bin/python3

def multiple_returns(sentence):
    '''returns tuple of string length and first chatacter of a sentence'''
    if len(sentence) == 0:
        return (0, None)
#        sentence[0] = None
    return (len(sentence), sentence[0])
