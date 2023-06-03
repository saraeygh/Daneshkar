#!/usr/bin/python3

import math


def division(num: int | float, den: int | float) -> float:
    """Divides num by den.
    :num -> fraction numerator
    :den -> fraction denominator
    """
    return num / den


# Here you can change inputs:
NUM = 3
DEN = 0

if DEN == 0:
    print(-math.inf, "or", math.inf, " -> Denominator cant be zero!")
elif isinstance(NUM, str) or isinstance(DEN, str):
    print("Insert integer of float numbers.")
else:
    print("Division result is:", division(NUM, DEN))
