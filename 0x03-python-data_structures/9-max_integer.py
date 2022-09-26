#!/usr/bin/python3
def max_integer(my_list=[]):
    max = 0
    if len(my_list) == 0:
        return "None"
    else:
        for numberz in range(len(my_list)):
            if max < my_list[numberz]:
                max = my_list[numberz]
    return max
