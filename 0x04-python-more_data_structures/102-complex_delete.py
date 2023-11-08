#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    ls_key = list(a_dictionary.keys())
    for va in ls_key:
        if value == a_dictionary.get(va):
            del a_dictionary[va]
            return (a_dictionary)
