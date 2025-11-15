#!/usr/bin/python3
import random
number = random.randint(-10, 10)
a = number
if a>0:
    print (f"{a} is positive")
elif number == 0:
    print("is zero")
else: 
    print (f"{a} is negative")
