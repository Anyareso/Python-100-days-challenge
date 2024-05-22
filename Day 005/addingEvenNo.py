# Program adds even numbers from 1 to a particular no
# User inputs the particular number
# Find all even no between 1 and the particular no
# Then add them up
# Input should not go beyond 100

target = int(input('Enter the end of the number the range should end in.'))
total = 0
for number in range (2, target + 1, 2):
    total += number
    print(f"All the even numbers between 1 and {target} are: {number}")
print(f"The sum of all even numbers is: {total}" )
