#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        numz = (number * -1) % 10
        last = number % 10
    print(numz, end='')
    return (last)
