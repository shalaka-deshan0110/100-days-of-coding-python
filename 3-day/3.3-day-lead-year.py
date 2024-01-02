""" This program determines if a year is a leap year or not. """


year = int(input("Enter a year: "))

if year % 4 == 0:
    if year % 100 == 0 and year % 400 != 0:
        print(year, "is not a leap year.")
    else:
        print(year, "is a leap year.")
else:
    print(year, "is not a leap year.")