#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list:
        max = my_list[0]
        for elemenz in my_list:
            if elemenz > max:
                max = elemenz
        return max
    return None
