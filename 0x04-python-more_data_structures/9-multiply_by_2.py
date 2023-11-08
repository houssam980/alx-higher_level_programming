#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    nw_dicti = a_dictionary.copy()
    for i, va in nw_dicti.items():
        nw_dicti[i] = va * 2
        return nw_dicti
