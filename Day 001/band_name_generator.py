# This is a  simple band name generator
# i.e., creates a name for your band name based on your city and pet's name
# steps to follow:
#1. Create a greeting for your program.
#2. Ask the user for the city that they grew up in.
#3. Ask the user for the name of a pet.
#4. Combine the name of their city and pet and show them their band
#5. Make sure the input cursor shows on a new line:
# Solution: https://replit.com/@appbrewery/band-name-generator-end


print("\033c")
print("Greetings friend. \nWelcome to the Band Name Generator!")
city = input("What city did you grow up in? \n")
pet = input("What is the name of your pet? \n")
print("Your band name could be " + city + " " + pet + "!")

