""" BELOW: Imported all necessary modules to make the system work."""
from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

""" BELOW: Iterating throgh the bank of question (data.py). """
for obj in range (0, len(question_data)):
    x = question_data[obj]["question"]
    y = question_data[obj]["correct_answer"]
    question = Question(x, y)
    question_bank.append(question)

quiz = QuizBrain(question_bank)

""" BELOW: while loop that keeps the question coming."""
while quiz.still_has_question() == True:
    quiz.next_question()

print(f"Your final score is: {quiz.score}/{quiz.question_number}")
