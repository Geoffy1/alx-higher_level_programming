#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list is None:
        return None
    elif my_list:
        max = my_list[0]
        for element in my_list:
            if element > most:
                most = element
        return most
