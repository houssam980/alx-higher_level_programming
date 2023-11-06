#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    nw_nlist = []
    for iter in range(len(my_list)):
        if my_list[iter] % 2 == 0:
            return nw_nlist , True
        else:
            return nw_nlist, False
