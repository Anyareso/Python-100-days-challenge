# reading a file
with open("../../../Desktop/my_file.txt") as file:
    contents = file.read()
    print(contents)

# writing a file
# with open("my_file.txt", mode="a") as file:
#     file.write("\nI cannot be much louder.")
