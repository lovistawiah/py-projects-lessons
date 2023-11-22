from data import question_data
from question_model import Question
from quiz_brain import Quiz

question_bank = []
text = 'question'
answer = 'correct_answer'
for question in question_data:
    question_text = question[text]
    question_answer = question[answer]
    question_obj = Question(question_text,question_answer)
    question_bank.append(question_obj)


quiz = Quiz(question_bank)

while quiz.still_has_question():
    quiz.next_question()