# از کاربر می‌پرسیم چه تعداد لپتاپ را مقایسه می‌کند
user_input = int(input("how many laptops do you wanna compللللللللللللللللللللللللللللللللللللللللللللللللللffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffare? "))

laptops = {}

# قیمت و کیفیت لپتاپ‌ها را از کاربر می‌گیریم و در دیکشنری می‌ریزیم
for laptop in range (user_input):
    print("Laptop number", laptop+1, "cost: ", end='')
    input_cost = int(input())
    print("Laptop number", laptop+1, "quality: ", end='')
    input_quality = int(input())
    laptops.update({input_cost:input_quality})

# لیست سورت شده قیمت لپاپ‌ها را مشخص می‌کنیم
# در یک حلقه بررسی می‌کنیم که آیا کیفیت لپتاپ‌ها هم با افزایش قیمت، افزایش می‌یابد یا خیر
# هرجا مشخص شود قیمت افزایش یافته ولی کیفیت کاهشی بوده، فلگ ترو می‌شود 

costs = sorted(laptops.keys())
flag = False
for i in range (len(laptops)-1):
    if laptops[costs[i]] >= laptops[costs[i+1]]:
        flag = True
        break

print("Not Founded" if flag == False else "Founded")