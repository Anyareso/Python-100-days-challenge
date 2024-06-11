import random
from game_data import data
from art import logo, vs
from replit import clear

print(logo)

score = 0
score_increment = 1
# Function containing the terms of the game
def game():
    global score
    person1 = random_person1()
    while True:
        print(vs)
        person2 = random_person2(person1)
        choice = input("Who has more followers? Type 'A' or 'B': ").upper()
        if choice == "A" and person1['follower_count'] > person2['follower_count']:
            score += score_increment
            print(f"You're right! Current score is: {score}")
            clear()
            print(logo)
            print(f"Compare A: {person1['name']}, {person1['description']}, {person1['country']}")
            print(f"You're right! Current score is: {score}")
        elif choice == "A" and person1['follower_count'] < person2['follower_count']:
            print(f"Sorry, that's wrong. Final score is: {score}")
            break
        elif choice == "B" and person2['follower_count'] > person1['follower_count']:
            score += score_increment
            print(f"You're right! Current score is: {score}")
            clear()
            print(logo)
            print(f"Compare A: {person2['name']}, {person2['description']}, {person2['country']}")
            print(f"You're right! Current score is: {score}")
            person1 = person2
        elif choice == "B" and person2['follower_count'] < person1['follower_count']:
            print(f"Sorry, that's wrong. Final score is: {score}")
            break
        else:
            print(f"Sorry, that's wrong. Final score: {score}")
            break

def random_person1():
    personality_A = random.choice(data)
    print(f"Compare A: {personality_A['name']}, {personality_A['description']}, {personality_A['country']}")
    return personality_A

def random_person2(person1):
    personality_B = random.choice(data)
    # Ensuring person1 and person2 are not the same
    while personality_B == person1:
        personality_B = random.choice(data)
    print(f"Compare B: {personality_B['name']}, {personality_B['description']}, {personality_B['country']}")
    return personality_B

game()  # Start the game