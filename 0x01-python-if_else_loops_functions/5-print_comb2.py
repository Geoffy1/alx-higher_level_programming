#!/usr/bin/python3
for m in range(0, 100):
    if m == 99:
        print(m)
    else:
        print(f"{m:0>2d}", end = ", ")
