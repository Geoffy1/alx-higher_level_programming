#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in range(len(matrix)):
        for colum in range(len(matrix[row])):
            print("{:d}".format(matrix[row][colum]), end="")
            if colum != (len(matrix[row]) - 1):
                print(" ", end="")
        print("")
