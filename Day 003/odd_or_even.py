# Using the modulo operator, even numbers have a remainder of 0
# i.e 6 % 2 = 0
# While for odd numbers the remainder is 1

number = int(input("Enter a number:"))
if number % 2 == 0:
    print("The number is even!")
else:
    print("The number is odd!")