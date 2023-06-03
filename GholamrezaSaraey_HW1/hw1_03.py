user_input = input("Insert string: ")
# جداسازی رشته‌های وارد شده و سپس اتصال همه آن‌ها و حذف تمام فواصل
user_input = "".join(user_input.split())
vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
#تک‌تک المان‌های رشته‌ ورودی کاربر بررسی و شروط گفته شده اعمال و در خروجی زیر قرار گرفته و نهایتا چاپ می‌شوند
output = ""
#در حلقه زیر حروف صدادار با نقطه جایگزین شده و حروف بزرگ کوچک نوشته شده و برعکس
for letter in user_input:
    if letter in vowels:
        output += "."
    elif letter.isupper() == True:
        output += letter.lower()
    else:
        output += letter.upper()

print(output)