# TODO - Use list comprehension to convert the list_of_strings to a list of integers
#  Then use the list conversion again to create a new list called result.
#  This list should only contain the even numbers from the list of numbers

list_of_input = input("Enter numbers: ").split()
list_of_integers = [int(x) for x in list_of_input]
result = [no for no in list_of_integers if no % 2 == 0]

print(result)
