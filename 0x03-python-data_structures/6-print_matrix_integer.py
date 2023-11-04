#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in range(len(matrix)):
        for a in range((len(matrix[i]))):
            if (a < (len(matrix[i])) - 1):
                print("{:d}".format(matrix[i][a]), end=' ')
            else:
                print("{:d}".format(matrix[i][a]), end='')
            print()
