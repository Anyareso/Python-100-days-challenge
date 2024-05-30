programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.", 
    "Function": "A piece of code that you can easily call over and over again."
}
# How to retrieve items from a dictionary
# print(programming_dictionary["Bug"])
# Adding items to a dictionary
programming_dictionary["Loop"] = "The action of doing something over and over again."
print(programming_dictionary)

# Be carful of typos when using dictionaries.
# Be careful to use the correct data type
# e.g., bug = "An error..." the computer will assume bug is an undefined variable
# Keys should be string data type
# It is recommended to start with an empty dictionary
 
# to add items to the dictionary
empty_dictionary = {}
empty_dictionary["Joke"]

# Wipe an existing dictionary
programming_dictionary = {}
print(programming_dictionary)

# Edit an item in dictionary
programming_dictionary["Bug"] = "A moth in your computer."

# Loop through a dictionary
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])