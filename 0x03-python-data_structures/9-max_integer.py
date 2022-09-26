#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) is 0 or my_list is None:
        return None
    max = my_list[0]
    for numz in range(len(my_list)):
        if max < my_list[numz]:
            max = my_list[numz]
    return max
