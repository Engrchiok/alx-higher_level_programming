#!/usr/bin/python3

def best_score(a_dictionary):
    """ returns a key with the biggest integer value """
    if a_dictionary:
        a = int()
        for i in a_dictionary.keys():
            if a < a_dictionary[i]:
                a = a_dictionary[i]
                b = i
        return (b)
    else:
        return (None)
