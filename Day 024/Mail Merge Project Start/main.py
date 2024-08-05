# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".
    
# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

invited = open("Input/Names/invited_names.txt", "r")
names = invited.readlines()

template = open("Input/Letters/starting_letter.txt")
letter = template.read()
for people in names:
    stripped_name = people.strip()
    first = letter.replace("[name]", stripped_name)
    # print(first)

    with open(f"Output/ReadyToSend/letter_to_{stripped_name}.txt", mode="w") as completed_letter:
        completed_letter.write(first)
