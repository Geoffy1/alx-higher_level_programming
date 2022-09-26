#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for sublist in matrix:
        for colu in sublist:
             print("{:d}".format(colu), end=" " if colu != sublist[-1] else "")
        print("")
