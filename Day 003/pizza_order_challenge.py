# Challenge is to build an automatic pizza order program
# Based on a user's order, their bill will be worked out
# For a small pizza(S): $15
# medium pizza(S): $20
# large pizza(S): $25
# add pepperoni for small pizza(Y or N): + $2
# add pepperoni for medium and large pizza(Y or N): + $3
# add cheese for any size pizza(Y or N): + $1
# After taking the order, display final bill


print("Thank you for choosing Python Pizza Deliveries!")
size  = input("What size of pizza do you want? S, M, or L")
add_pepperoni = input("Do you want pepperoni? Y or N")
extra_cheese = input("Do you want extra cheese? Y or N")

bill = 0

if size == "S":
    bill += 15
elif size == "M":
    bill += 20
else:
    bill += 25

if add_pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3

if extra_cheese == "Y":
    bill += 1

print(f"Your final bill is: ${bill}") 