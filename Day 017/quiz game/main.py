from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
# TODO 1. Write a for loop to iterate over the question data.
for item in question_data:
    # TODO 2. Create a Question object from each entry in question_data
    question = Question(item['question'], item['correct_answer'])
    # TODO 3. Append each Question object to the question_bank
    question_bank.append(question)

quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
