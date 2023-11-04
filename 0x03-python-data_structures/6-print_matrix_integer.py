#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        for a in i:
            print("{:d}".format(a), end=" " if a != i[-1] else "")
        print()
