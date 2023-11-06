#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    nw_tple = ()
    tuple_f = tuple_a + (0, 0)
    tuple_s = tuple_b + (0, 0)
    nw_tple = tuple_f[0] + tuple_s[0], tuple_f[1] + tuple_s[1]
    return nw_tple
