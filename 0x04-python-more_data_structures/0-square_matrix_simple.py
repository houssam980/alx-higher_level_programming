#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    nw_mtrx = []
    for iter in matrix:
        rest = list(map(lambda x: x**2, iter))
        nw_mtrx.append(rest)
        return nw_mtrx
