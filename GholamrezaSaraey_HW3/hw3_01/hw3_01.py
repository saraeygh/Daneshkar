#!/usr/bin/python3

NUM_TXT = [
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
    "ten",
    "eleven",
    "twelve",
    "thirteen",
    "fourteen",
    "fifteen",
    "sixteen",
    "seventeen",
    "eighteen",
    "nineteen",
]
NUM_DIGIT = [
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    "10",
    "11",
    "12",
    "13",
    "14",
    "15",
    "16",
    "17",
    "18",
    "19",
]

with open("Zen.txt", "r+", encoding="utf-8") as f:
    text = f.read()

for i in range(len(NUM_TXT)):
    text = text.replace(NUM_TXT[i] + " )", NUM_DIGIT[i] + ")")

with open("Zen_digit.txt", "w", encoding="utf-8") as f:
    f.write(text)
