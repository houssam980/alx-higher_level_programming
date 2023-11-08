#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    nw_dic = {}
    for item in a_dictionary:
        nw_dic[item] = a_dictionary[item] * 2
    return nw_dic
