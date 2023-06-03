
def factorial(number: int) -> int:
    if number == 0:
        return 1
    return number * factorial(number-1)


def exponential(n: int, x: int) -> float:
    summation = 0
    for i in range(n):
        summation += (x**i) / factorial(i)
    return summation


x = 4
n = 10

print(f"{exponential(x=x, n=n):.3f}")