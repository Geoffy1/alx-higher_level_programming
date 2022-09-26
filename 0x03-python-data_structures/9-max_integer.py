#!/usr/bin/python3
def max_integer(my_list=[]):
    maxim = my_list[0]
    if len(my_list) == 0:
        return "None"
    else:
        for numberz in range(len(my_list)):
            if maxim < my_list[numberz]:
                maxim = my_list[numberz]
        return maxim
