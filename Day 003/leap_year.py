# Program that checks if an year is a leap year or not
# A leap year is divisible by 4 with no remainder
# Except every year that is evenly divisible by 100 with no remainder
# Leap year is divisible by 400 with no remainder
# e.g 2000 / 4 = 500 (leap)
# 2000 / 100 = 20 (not leap)
# 2000 / 400 = 5 (leap)
# concluding 2000 is indeed a leap year

year = int(input("Enter any year\n"))
if year % 4 != 0:
    print(f"{year} is not a leap year")
elif year % 100 != 0:
    print(f"{year} is not a leap year")
elif year % 400 != 0:
    print(f"{year} is not a leap year")
else:
    print(f"{year} is a leap year")

