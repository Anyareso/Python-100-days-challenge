# Official rock, paper, scissors rules
# Rock beats scissors
# Scissors beats paper
# Paper beats rock

# Things to consider:
# How to decide who won and who lost
# How to get the computer to choose a random shape between rock, paper and scissors
# How to make sure the game works as it should

# Breaking down problem
# 1. Generating random number between 1 and 3
# 2. Putting down the logic on how to win
# 3. Thony

import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game_images = [rock, paper, scissors]
user_choice = int(input("What do you choose? Type 0 for rock, 1 for paper and 2 for scissors\n"))
if user_choice >= 3 or user_choice < 0 :
    print("You typed an invalid number, You lose!")
else:
    print(game_images[user_choice])

    computer_choice = random.randint(0,2)
    print("Computer chose:")
    print(game_images[computer_choice])

    if user_choice == 0 and computer_choice == 2:
        print("You win!")
    elif computer_choice == 0 and user_choice == 2:
        print("You lose!")
    elif computer_choice > user_choice:
        print("You lose!")
    elif user_choice > computer_choice:
        print("You win!")
    elif computer_choice == user_choice:
        print("It's a draw")
