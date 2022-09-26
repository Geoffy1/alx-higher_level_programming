#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    first_list = []
    for numz in range(len(my_list)):
        if my_list[numz] % 2 == 0:
            first_list.append(True)
        else:
            first_list.append(False)
    return first_list

