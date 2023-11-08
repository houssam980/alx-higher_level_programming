#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    li_ky = list(a_dictionary.keys())
    for va_dic in li_ky:
        if value == a_dictionary.get(va_dic):
            del a_dictionary[va_dic]
            return (a_dictionary)
