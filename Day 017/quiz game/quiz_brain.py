# TODO 1. Asking the questions
# Challenge 1
# Create a class called QuizBrain
# Write an __init__() method
# Initialize the question_number to 0
# Initialize the question_list to an input.
# Challenge 2
# Create a method called next_question() inside QuizBrain
# This method should retrieve the item at the current question_number from the question list.
# Use the input() function to show the user the Question text and ask for the user's answer.
# Challenge 3
# Create a method called still_has_questions()
# Return a boolean depending on the value of the question_number
# Use the while loop to show the next question until the end
# TODO 2. Checking if the answer was correct
# TODO 3. Checking if we're at the end of the quiz

class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def still_has_questions(self):
        q_no = self.question_number
        q_list = len(self.question_list)
        return q_no < q_list

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False): ")
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right!")
        else:
            print("That's wrong.")
        print(f"The correct answer was: {correct_answer}.")
        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")
