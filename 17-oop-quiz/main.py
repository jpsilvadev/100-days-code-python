from question_model import Question
from data2 import question_data
from quiz_brain import QuizBrain

question_bank = [
    Question(question_data[i]["question"], question_data[i]["correct_answer"])
    for i, question in enumerate(question_data)
]


quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print(
    f"You've completed the quiz\n"
    f"Your final score was: {quiz.score}/{quiz.question_number}!"
)
