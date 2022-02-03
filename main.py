from question_model import Question
from data import question_data
from quiz_brain import QuizBrain


question_bank = []

for i in question_data:
    question = Question(i['text'],i['answer'])
    question_bank.append(question)

quiz_brain = QuizBrain(question_bank)

game_continue = True
while game_continue:
    quiz_brain.next_question()
    if quiz_brain.total == len(question_bank):
        game_continue = False
        print("You've completed the quiz")
        print(f"Your final score was: {quiz_brain.score}/{quiz_brain.total}")