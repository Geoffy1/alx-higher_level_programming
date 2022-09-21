#!/usr/bin/python3
def remove_char_at(str, n):
    fashion = ''
    m = 0
    for charz in str:
        if m != n:
            fashion += str[m]
        m += 1
    return fashion
