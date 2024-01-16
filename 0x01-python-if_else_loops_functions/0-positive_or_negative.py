#!/usr/bin/python3
import random
number = random.randint(-10, 10)
if (number > 0):
    print(f"the number {number :d} is positive")
else:
    if (number == 0):
        print(f"the number {number :d} is zero")
    else:
        if (number < 0):
            print(f"the number {number :d} is negative")
