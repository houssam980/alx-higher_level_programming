#!/usr/bin/python3
def search_replace(my_list, search, replace):
    nw_list = []
    for elem in my_list:
        if elem == search:
            nw_list.append(replace)
        else:
            nw_list.append(elem)
    return nw_list
