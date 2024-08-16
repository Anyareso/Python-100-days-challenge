# TODO - Write a list comprehension to create a new list called squared_numbers.
#  This list should contain every number in th list numbers but each number should be squared

numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
squared_numbers = [number*number for number in numbers]
print(squared_numbers)