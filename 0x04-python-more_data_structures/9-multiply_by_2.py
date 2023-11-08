#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    nw_dictionary = a_dictionary.copy()
    for i in nw_dictionary:
        nw_dictionary[i] = i * 2
        return nw_dictionary
