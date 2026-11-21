from enum import Enum
from math import ceil


class Errors(Enum):
    REPEAT = 1
    INVALID = 2


MONTHS_DAY = {
    "January": 31,
    "February": 28,
    "March": 31,
    "April": 30,
    "May": 31,
    "June": 30,
    "July": 31,
    "August": 31,
    "September": 30,
    "October": 31,
    "November": 30,
    "December": 31,
}


with open("B/Precip.txt") as f:
    f.readline() # заглушка
    town = f.readline().strip()
    month, year = f.readline().strip().split(", ")

    line = 1

    errors = []
    days = {i: "NA" for i in range(1, MONTHS_DAY[month] + 1)}
    total = []

    while a := f.readline().split():
        day, amount = a
        day = int(day)

        if day in days:
            if days[day] == "NA":
                days[day] = float(amount)
                total += [float(amount)]
            else:
                errors.append((Errors.REPEAT, day, line))
        else:
            errors.append((Errors.INVALID, day, line))

        line += 1

    print(
f"""
Programmer: Tsimur Siuko
CS 1044 Project 5 Fall 2008

Precipitation report for {town} during {month}, {year}
""")

    if errors:
        print("Error         Day       Line")
        keys = {Errors.REPEAT: "Repeated", Errors.INVALID: "Invalid"}
        for i in sorted(errors, key=lambda a: a[2]):
            print(f"{keys[i[0]]:<11} {i[1]:>5} {i[2]:>10}")
        print()

    print("Day Amount Graph")
    for i in range(1, MONTHS_DAY[month] + 1):
        if days[i] != 'NA':
            print(f"{i:<3} {days[i]:<5.2f} {"*" * ceil(days[i] / 0.25)}")
        else:
            print(f"{i:<5} {days[i]:<5}")

    print(
f"""
Minimum     Maximum     Average
{min(total):>7.2f}     {max(total):>7.2f}     {sum(total) / MONTHS_DAY[month]:>7.2f}
""")
