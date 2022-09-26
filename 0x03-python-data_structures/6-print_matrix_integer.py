#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for sublist in matrix:
        for colu in sublist:
             print("{:d}".format(col), end=" " if col != row[-1] else "")
        print("")
