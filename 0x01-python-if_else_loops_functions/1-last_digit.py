#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
print(f"Last digit of {number} is", end=" ")
lastd = number
if lastd < 0:
    lastd *= -1
while lastd // 10 != 0:
    lastd %= 10
if number < 0:
    lastd *= -1
print(f"{lastd}", end=" ")
if lastd > 5:
    print(f"and is greater than 5")
elif lastd == 0:
    print(f"and is 0")
elif lastd < 6 and lastd != 0:
    print(f"and is less than 6 and not 0")
else:
    pass
