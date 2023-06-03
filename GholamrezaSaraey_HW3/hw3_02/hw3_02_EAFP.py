#!/usr/bin/python3

import math


def division(num: int | float, den: int | float) -> float:
    """
    Divide numerator by denominator.
    :num -> as fraction numerator
    :den -> as fraction denominator
    """
    return num / den


# You can change inputs here:
NUM = 2  # Numerator
DEN = 0  # Denominator

try:
    print(division(NUM, DEN))
except TypeError:
    print("Insert integer or float numbers.")
except ZeroDivisionError:
    print(-math.inf, "or", math.inf, " -> Denominator cant be zero!")
