# # TODO
# 1. Pick a random person from game_data

import random
from game_data import data
PERSONALITY_A = ""
def random_person1():
    personality_A = random.choice(data)
    name = personality_A['name']
    description = personality_A['description']
    country = personality_A['country']
    followers_A = personality_A['follower_count']

    print(f"Compare A: {name}, {description}, {country}")
    return followers_A, personality_A 


def random_person2():
    personality_B = random.choice(data)
    name = personality_B['name']
    description = personality_B['description']
    country = personality_B['country']
    followers_B = personality_B['follower_count']

    print(f"Compare B: {name}, {description}, {country}")
    return followers_B

from art import logo, vs
print(logo)
score = 0
score_increment = 1
failed = False
while not failed:
    # Random person 1 picked
    person1 = random_person1()

    from art import vs
    print(vs)

    # Random person 2 picked
    person2 = random_person2()

    choice = input("Who has more followers? Type 'A' or 'B': ")
    if choice == "A" and person1 > person2:
        score += score_increment
        print(f"You're right! Current score is: {score}")
        got_it_right = True
        while got_it_right:
            retain_personality = {}
            # higher_followers = personality_A
            # print(higher_followers) 
            # retain_personality()
            print(person1)
            got_it_right = False

    elif choice == "A" and person1 < person2:
        failed = True
        print("Oops! You got it wrong.")
    elif choice == "B" and person2 > person1:
        score += score_increment
        print(f"You're right! Current score is: {score}")
    elif choice == "B" and person2 < person1:
        failed = True
        print("Oops! You got it wrong.")




