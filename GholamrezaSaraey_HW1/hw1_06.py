# تابعی که بررسی می‌کند عدد ورودی اول است یا نه
def primecheck(number):
    for divisor in range(2,1 + int(number/2)):
        if number%divisor == 0:
            return False
    else:
        return True

#دریافت بازه مورد نظر از کاربر و بررسی و چاپ اعداد اول درون بازه
from_number = int(input("Lower limit (e.g. 11): "))
to_number = int(input("Upper limit (e.g. 20): "))
print ("Prime numbers between", from_number, "and", to_number, "are:")
for num in range(1 + from_number, to_number):
    if primecheck(num) == True:
        print(num)