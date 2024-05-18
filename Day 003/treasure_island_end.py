print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

task1 = input("You're at a crossroad. Where do you want to go? Type 'left' or 'right' ")
if task1 == "left":
    print("You are at a lake. There is an island at the middle of the lake. Type 'wait' to wait for a boat. Type 'swim' to swim across. ")
    task2 = input("What do you choose to do now?")
    if task2 == "wait":
        print("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow, one blue.")
        task3 = input("Which color do you choose?")
        if task3 == "blue":
            print("You enter a room with beasts. Game over!")
        elif task3 == "red":
            print("It's a room full of fire. Game Over!")
        elif task3 == "yellow":print("You've found the treasure. You win!!")
        else:
            print("You chose a door that doesn't exist. Game over.")
    else:
        print("You get attacked by an angry trout. Game Over!")
else:
    print("You fell into a hole. Game Over")