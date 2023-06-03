#!/usr/bin/python3
# Released under GPLv3+ License, 2022.

def sum_digits(number: int) -> int:
    return sum(map(int, str(number)))

digit = 2135

while digit >= 10:
    digit = sum_digits(digit)

print (digit)