#!/usr/bin/python3
for charz in range(ord('z'), ord('a') - 1, -2):
     print("{:c}{:s}".format(charz, chr(charz - 33)), end="")
