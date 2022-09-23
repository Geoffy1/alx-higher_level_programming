#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    numberz = len(sys.argv)
    if numberz == 1:
        print("{} arguments.".format(numberz - 1))
    elif numberz == 2:
        print("{} argument:".format(numberz - 1))
    else:
        print("{} arguments:".format(numberz - 1))

    for i in range(1, numberz):
        print("{}: {}".format(i, sys.argv[i]))
