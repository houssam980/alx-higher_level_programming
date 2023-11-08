#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    nw_dicti = {}
    for i, in a_dictionary:
        nw_dicti[i] = a_dictionary[i].copy * 2
        return nw_dicti
