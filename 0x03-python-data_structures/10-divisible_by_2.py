#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    nw_nlist = []
    for iter in range(len(my_list)):
        if my_list[iter] % 2 == 0:
             nw_nlist.append(True)
        else:
            nw_nlist.append(False)
    return nw_nlist
