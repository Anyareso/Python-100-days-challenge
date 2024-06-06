import random

print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")
random_number = random.randint(1, 100) 
print(f"Pssst, the correct answer is {random_number}")

difficulty_level = input("Choose a difficult. Type 'easy' or 'hard': ")

guesses = 0

end_game = False

def check_guess():
    global end_game
    if guess > random_number:
        print("Too high\nGuess again")
    elif guess < random_number:
        print("Too low\nGuess again")
    else:
        print(f"You got it. The answer was {random_number}")
        end_game = True

while not end_game:
    if difficulty_level == "easy":
        guesses = 10
        print(f"You have {guesses} attempts remaining to guess the number. ")
        guess = int(input("Make a guess:"))
        check_guess()
        guesses -= 1

        if guesses == 0:
            end_game = True
        else:
            print(f"You have {guesses} attempts remaining to guess the number. ")
        

    else:
        guesses = 5
        while guesses > 0:
            print(f"You have {guesses} attempts remaining to guess the number. ")
            guess = int(input("Make a guess:"))
            check_guess()
            guesses -= 1
     
            if guesses == 0:
                end_game = True
                print("Out of Guesses")
            # else:
                # guesses -= 1
                # print(f"You have {guesses} attempts remaining to guess the number. ")
