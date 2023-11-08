#!/usr/bin/python3
def common_elements(set_1, set_2):
    nw_set = set_1.symmetric_difference(set_2)
    return nw_set
