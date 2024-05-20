# Under the list fruits, there are 3 items
# The for loops iterantes and prints every fruit under 'fruits list'
# For the second print statement, it gets executed after the first print statement then adds 'Pie' to the fruit for each fruit
# The last line of code is outside the loop
# This means that it won't iterate through each item on the list but rather displays the list as a whole

fruits = ["Apple", "Peach", "Pearl"]
for fruit in fruits:
    print(fruit)
    print(fruit + "Pie")

print(fruits)

# Using ranges with for loop
# Displays the numbers between 1 and 10
# Skips the 3rd no
# I.e, displays numbers 1, 4, 7 and 10
for number in range (1, 11, 3):
    print(number)

# Displaying the sum of the numbers between range of 1 to 100
total = 0
for number in range(1, 101):
    total += number
print(total)