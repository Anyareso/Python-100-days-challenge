# 3 lines are outputted as possible areas to hide the treasure
# a, b and c are used as index references
# Where, line 1, second space can be reffered to as A3
# Line 3, third space can be reffered to as B3
# [Position in terms of a/b/c, line in terms of 1/2/3]

line1 = [" ", " ", " " ]
line2 = [" ", " ", " " ]
line3 = [" ", " ", " " ]

map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input("Where do you want to put the treasure?")

letter = position [0].lower()
abc = ["a", "b", "c"]
letter_index = abc.index(letter)
number_index = int(position[1])- 1
map[number_index][letter_index] = "X"

print(f"{line1}\n{line2}\n{line3}")