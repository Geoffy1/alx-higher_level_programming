#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list is None or len(my_list) is 0:
        return "None"
    max = my_list[0]
    for numberz in my_list:
        if max < my_list[numberz]:
            max = my_list[numberz]
    return max
