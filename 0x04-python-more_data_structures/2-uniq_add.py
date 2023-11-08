#!/usr/bin/python3
def uniq_add(my_list=[]):
    s = 0
    nw_list = []
    for n in my_list:
        if n not in nw_list:
            s += n
            nw_list.append(n)
        return s
