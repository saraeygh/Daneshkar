#! /usr/bin/python3

from datetime import datetime
import jdatetime

# you can input any bith date and time, just meet the style.
BIRTH = "1995-09-20 23:05:00"

# Here we get the year, month, hour, minute and second of birth
date, time = BIRTH.split(" ")
year, month, day = map(int, date.split("-"))
hour, minute, second = map(int, time.split(":"))
BIRTH = datetime(year, month, day, hour, minute, second)

# Here we calculate how many seconds passed
life_passed = datetime.now() - BIRTH
print("SECTION 1: Seconds Passed = ", life_passed.total_seconds())

# Days and minutes till nest birthday.
today = datetime.today()
current_year_birthday = datetime(today.year, BIRTH.month, BIRTH.day)
next_year_birthday = datetime(today.year + 1, BIRTH.month, BIRTH.day)
if today < current_year_birthday:
    seconds = (current_year_birthday - today).total_seconds()
    days = seconds // 86400
    minutes = seconds // 60
    print(
        "SECTION 2:",
        f"Happy birthday in advance, {days} days or {minutes} minutes ahead :)",
    )
else:
    seconds = (next_year_birthday - today).total_seconds()
    days = seconds // 86400
    minutes = seconds // 60
    print(
        "SECTION 2:",
        f"Happy birthday in advance, {days} days or {minutes} minutes ahead :)",
    )

# Birthday based on Persian calender
gregorian_date = datetime(year, month, day)
jalali_date = jdatetime.date.fromgregorian(date=gregorian_date)
print("SECTION 3: Birthday in Persian calender =", jalali_date)
