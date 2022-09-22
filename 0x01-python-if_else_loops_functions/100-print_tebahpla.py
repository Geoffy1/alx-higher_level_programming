#!/usr/bin/python3
for m in range(ord('z'), ord('a') - 1, -2):
    print("{:c}{:s}".format(m, chr(m - 33)), end="")
