from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from data_trivia import trivia_data

# Playing Data file
# question_bank = []
#
# for question in question_data:
#     question_text = question["text"]
#     question_answer = question["answer"]
#     new_question = Question(q_text=question_text, q_answer=question_answer)
#     question_bank.append(new_question)


# Playing Trivia data Api questions
question_trivia = []

for question in trivia_data:
    question_trivia.append(Question(question["question"], question["correct_answer"]))

# Game using trivia data question
ask_question = QuizBrain(question_trivia)

while ask_question.still_has_question():
    ask_question.next_question()

# To print end of game info:
# already added in QuizBrain still_has_question
# can be put at the end of the while loop
# print("You've completed the quiz")
# print(f"Your final score is: {quiz.score/quiz.question_number}")
