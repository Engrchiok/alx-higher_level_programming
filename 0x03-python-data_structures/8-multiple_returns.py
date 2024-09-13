#!/usr/bin/python3

def multiple_returns(sentence):
    '''returns tuple of string length and first chatacter of a sentence'''
    if sentence == None:
        sentence = ''
    return (len(sentence), sentence[0])
