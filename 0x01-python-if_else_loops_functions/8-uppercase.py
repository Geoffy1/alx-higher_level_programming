#!/usr/bin/python3
def uppercase(str):
    for m in str:
        if ord(m) >= 97 and ord(m) <= 122:
            char = chr(ord(m) - 32)
        else:
            char = m
        print("{:s}".format(char), end="")
    print('')
