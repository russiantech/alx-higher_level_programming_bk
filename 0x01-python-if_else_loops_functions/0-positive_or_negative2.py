#!/usr/bin/python3
import random
number = random.randint(-10, 10)
match number:
    case x if x > 0:
        result = f"{x} is a positive"
    case 0:
        result = f"{x} is zero"
    case x if x < 0:
        result = f"{x} is a negative"
    case _:
        result = f"Invalid {number}"

print(result)
