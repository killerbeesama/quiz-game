import os 

class QuizBrain:
    
    def __init__(self,question_list) -> None:
        self.question_number = 0
        self.question_list = question_list
        self.score = 0
        self.total = 0


    def next_question(self):
        current_question = self.question_list[self.question_number]
        user_input = input(f"Q.{self.question_number+1}: {current_question.text} (True or False):\n").title() 
        os.system("cls")
        if user_input == "True" or user_input == "False":
            self.question_number += 1
            self.total += 1     
            if user_input == current_question.answer:
                self.score += 1
                print("You got it right!")
            else:
                print("That's wrong.")
            print(f"The correct answer was: {current_question.answer}.")
        else:
            print("Type in a correct input and try again.")
        print(f"Your current score is: {self.score}/{self.total}")
        
            
        

