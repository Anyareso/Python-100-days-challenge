# This program selects a random name from a list of names.
# The person selected will pay for everybody's food bill.

# Start by inputing the people present at the table
# Get the total number of names
# Pick out a random person from the list by using the random number
import random

names_string = input("Enter the names of people present at the table")
names = names_string.split(",")
num_items = len(names)
random_choice = random.randint(0, num_items - 1)
random_name = names[random_choice]

print(f"{random_name} is going to buy the meal today!")