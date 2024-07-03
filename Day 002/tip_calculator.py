# Bill calculator example
# if the bill was $150.00, split between 5 people, with 12% tip 
# each person should pay (150.00/5)* 1.12 = 33.6
# format the result to 2 decimal places = 33.60

print("\033c")
print("Welcome to the Tip Calculator")
bill = float(input("What was the total bill?\n"))
tip = int(input("How much tip would you like to give? 10, 12 or 15?\n"))
split = int(input("How many people to split the bill?\n"))

tip_percentage = tip/100
bill_plus_tip = bill + (bill * tip_percentage)
bill_per_person = bill_plus_tip / split
total = "{:.2f}".format(bill_per_person)

print(f"Your total bill per person is {total}")
