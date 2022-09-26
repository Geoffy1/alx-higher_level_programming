#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for sublist in matrix:
        print(" ".join(map(str, sublist)))
