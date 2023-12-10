#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
Lastdigit = abs(number) % 10
if number < 10:
    lastdigit= -(lastdigit)
string=("Lastdigit of {} is {}".format(number, lastdigit))
if lastdigit > 5:
    print(f"{string} and is greater than 5")
elif lastdigit == 0:
    print(f"{string} and is zero")
else:
    print(f"{string} and is less than 6 and not 0")
