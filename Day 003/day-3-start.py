#Rollercoaster height checker
#For one to be on the ride, their height has to be more than 120m
# As per their age, ticket prices differ for children, youth and adults
# Incase one wants to be taken a picture, an extra $3 is charged
# At the end display their total bill

print("Welcome to the rollercoaster!")
height =  int(input("What is your height in centimeters?"))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("How old are you?"))
    if age < 12:
        bill = 5
        print("Child tickets are $5")
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7")
    else:
        bill = 12
        print("Adult tickets are $12")

    wants_photo = input("Do you want a photo taken? Y or N")
    if wants_photo == "Y":
        bill = bill + 3
    
    print(f"Your total bill is {bill}")
else:
    print("Sorry, you have to grow taller before you can ride.")