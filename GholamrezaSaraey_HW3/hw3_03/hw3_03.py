#!/usr/bin/python3


def apply_discount(price: int, discount: float = 0.0) -> int:
    """
    Apply Discount Percent and Calculate Final Price
    """
    final_price = int(price * (1 - discount))
    assert 0 < final_price <= price, "Why this AssertionError never Raised!"
    return final_price


# Inputs, P: Price, D: Discount
P = 10
D = 0.2

print(apply_discount(P, D))
