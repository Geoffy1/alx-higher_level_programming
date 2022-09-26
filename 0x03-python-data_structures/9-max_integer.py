#!/usr/bin/python3
def max_integer(my_list=[]):
    maxi = 0
    if my_list is None or len(my_list) is 0:
        return "None"
    for numberz in range(len(my_list)):
        if my_list[numberz] > maxi:
            maxi = my_list[numberz]
    return maxi
