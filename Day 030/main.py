# FileNotFoundError
# try:
#     file = open("a_file.txt")
#     a_dictionary = {"key" : "value"}
#     print(a_dictionary["sdfsdf"])
# except FileNotFoundError:
#     file = open("a_file.txt", "w")
#     file.write("something")
# except KeyError as error_message:
#     print(f"The key {error_message} does not exist.")
# else:
#     content = file.read()
#     print(content)
# finally:
#     raise TypeError("This is an error that i made up")

height = float(input("Enter your height: "))
weight = int(input("Enter your weight: "))

if height > 3:
    raise ValueError("Human height should not be over 3 meters.")

bmi = weight / height ** 2
print(bmi)