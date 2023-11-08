#!/usr/bin/python3
def search_replace(my_list, search, replace):
    nw_list = []
    for iter in range (len(my_list)):
        my_list[search] = replace
        my_list = nw_list
