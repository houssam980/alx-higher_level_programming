#!/usr/bin/python3
def search_replace(my_list, search, replace):
    nw_list = []
    for iter in range (len(my_list)):
        if iter == search:
            nw_list.append(replace)
        else:
            nw_list.append(iter)
            return nw_list
