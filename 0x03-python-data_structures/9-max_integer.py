#!/usr/bin/python3
def max_integer(my_list=[]):
    maximu = 0
    if len(my_list) == 0:
        return "None"
    else:
        for numberz in range(len(my_list)):
            if maximu < my_list[numberz]:
                maximu = my_list[numberz]
        return maximu
