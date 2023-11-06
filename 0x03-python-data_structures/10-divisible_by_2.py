#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    nw_list = ()
    for iter in range(len(my_list)):
        if nw_list[iter] == my_list[iter] * 2:
            return nw_list , True
        else:
            return nw_list, False
