#!/usr/bin/python3
for m in range(0, 10):
    for n in range(0, 10):
        if m < n:
            print("{}{}".format(m,n), end="")
            if m < 8:
                print(", ", end="")
print("\n", end="")
