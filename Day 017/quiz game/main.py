# TODO 1. Write a for loop to iterate over the question data.
# TODO 2. Create a Question object from each entry in question_data
# TODO 3. Append each Question object to the question_bank
from question_model import Question
from data import question_data

question_bank = []

for item in question_data:
    question = Question(item['text'], item['answer'])
    question_bank.append(question)
  
