#!/usr/bin/python3
def common_elements(set_1, set_2):
    for elem in set_1 and set_2:
        if set_1[elem] == set_2[elem]:
            return elem
