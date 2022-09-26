#!/usr/bin/python3
def max_integer(my_list=[]):
    maximo = 0
    if len(my_list) == 0:
        return "None"
    else:
        for numberz in range(len(my_list)):
            if maximo < my_list[numberz]:
                maximo = my_list[numberz]
        return maximo
