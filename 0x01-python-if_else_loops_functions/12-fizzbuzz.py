#!/usr/bin/python3
def fizzbuzz():
    for numz in range(1, 101):
        if numz % 15 == 0:
            print("FizzBuzz", end=" ")
        elif numz % 3 == 0:
            print("Fizz", end=" ")
        elif numz % 5 == 0:
            print("Buzz", end=" ")
        else:
            print(numz, end=" ")
