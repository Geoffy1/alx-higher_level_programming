#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list is None or len(my_list) is 0:
        return None
    max = my_list[0]
    for numz in range(len(my_list)):
        if max < my_list[numz]:
            max = my_list[numz]
    return max
