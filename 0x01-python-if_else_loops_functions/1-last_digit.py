#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    l_d = ((-1 * number) % 10) * -1
else:
    l_d = number % 10
if (l_d % 10) > 5:
    print(f"Last digit of {number:d} is {l_d:d} and is greater than 5")
elif (l_d % 10) == 0:
    print(f"Last digit of {number:d} is {l_d:d} and is 0")
else:
    print(f"Last digit of {number:d} is {l_d:d} and is less than 6 and not 0")
