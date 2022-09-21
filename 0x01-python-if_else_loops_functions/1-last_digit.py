#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
les_6 = 'and is less than 6 and not 0'
print("Last digit of", end=" ")
if (number % 10 > 5):
    print(f"{number} is {number % 10} {'and is greater than 5'}")
elif (number % 10 == 0):
    print(f"{number} is {number % 10} {'and is 0'}")
elif (number < 0):
    print(f"{number} is {((number * -1) % 10) * -1} {les_6}")
else:
    print(f"{number} is {number % 10} {les_6}")
