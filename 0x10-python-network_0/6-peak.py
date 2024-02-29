#!/usr/bin/python3
"""Finds a peak"""


def find_peak(list_of_integers):

    if list_of_integers is None or list_of_integers == []:
        return None
    low = 0
    hight = len(list_of_integers)
    midl = ((hight - low) // 2) + low
    midl = int(midl)
    if hight == 1:
        return list_of_integers[0]
    if hight == 2:
        return max(list_of_integers)
    if list_of_integers[midl] >= list_of_integers[midl - 1] and\
            list_of_integers[midl] >= list_of_integers[midl + 1]:
        return list_of_integers[midl]
    if midl > 0 and list_of_integers[midl] < list_of_integers[midl + 1]:
        return find_peak(list_of_integers[midl:])
    if midl > 0 and list_of_integers[midl] < list_of_integers[midl - 1]:
        return find_peak(list_of_integers[:midl])
