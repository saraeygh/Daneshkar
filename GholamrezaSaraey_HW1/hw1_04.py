user_input = input("Please insert a string: ")
#ابتدا تمام فواصل رشته ورودی حذف می‌شوند
user_input = "".join(user_input.split())
letter_repeat_count = {}
# اگر در دیکشنری نبود مقدارش ایجاد و یکی به آن افزوده می‌شود. 
# اگر در دیکشنری بود یکی به مقدارش افزوده می‌شود
for letter in user_input:
    if letter not in letter_repeat_count:
        letter_repeat_count.update({letter:1})
    else:
        letter_repeat_count[letter] += 1

print(letter_repeat_count)