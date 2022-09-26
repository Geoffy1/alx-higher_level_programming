#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for sublist in matrix:
        for element in range(len(sublist)):
            print("{:d}".format(sublist[element]), end=" ")
            if element != len(sublist) - 1:
                print(" ", end="")
        print("")
