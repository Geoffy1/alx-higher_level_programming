#!/usr/bin/python3
def uppercase(str):
    for m in str:
        if ord(m) >= 97 and ord(m) <= 122:
             print(chr(ord(m) - 32), end="")
        else:
            print(m, end="")
