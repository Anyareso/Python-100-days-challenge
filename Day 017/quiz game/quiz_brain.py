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

    def still_has_questions(self):
        q_no = self.question_number
        q_list = len(self.question_list)
        return q_no < q_list

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        input(f"Q.{self.question_number}: {current_question.text} (True/False): ")
