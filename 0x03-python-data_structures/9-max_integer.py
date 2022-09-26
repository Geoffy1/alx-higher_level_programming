#!/usr/bin/python3
def max_integer(my_list=[]):
    max = my_list[0]
    if my_list is None or len(my_list) is 0:
        return "None"
    else:
        for numberz in range(len(my_list)):
            if my_list[numberz] > max:
                max = my_list[numberz]
        return max
