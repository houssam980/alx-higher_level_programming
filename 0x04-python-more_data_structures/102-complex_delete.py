#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    ls_k = list(a_dictionary.keys())
    for value in ls_k:
        if not value in a_dictionary:
            return a_dictionary
        else:
            value == a_dictionary.get(value)
            del a_dictionary[value]
            return (a_dictionary)
