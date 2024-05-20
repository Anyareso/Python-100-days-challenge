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