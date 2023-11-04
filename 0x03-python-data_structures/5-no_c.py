#!/usr/bin/env python3
def no_c(my_string):
    nw_str = my_string.translate({ord(ite): None for ite in "cC"})
    return nw_str
