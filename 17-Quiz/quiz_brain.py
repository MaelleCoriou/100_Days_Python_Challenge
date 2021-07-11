class QuizBrain:

    def __init__(self, q_list):
        # Get track of the question's number
        self.question_number = 0
        # Get the data list
        self.question_list = q_list
        # Get track of the score
        self.score = 0

    def still_has_question(self):
        # Get the length of the list
        turns = len(self.question_list)
        # Returns False when all questions are printed to stop the while loop
        if self.question_number < turns:
            return True
        else:
            print("You've completed the quiz.")
            print(f"Your final score is: {self.score}/{self.question_number}")
            return False
        # shorter solution, will return a boolean
        # return self.question_number < len(self.question_list)

    def next_question(self):
        # Get the question position in the list with question_number index
        current_question = self.question_list[self.question_number]
        # Add 1 to each question asked
        self.question_number += 1
        # Print the number question + current question text using text attribute from question class
        answer = input(f"Q.{self.question_number}: {current_question.text} (True/False)?:")
        # Calls the function check answer and pass the current attributes
        self.check_answer(answer, current_question.answer)

    def check_answer(self, answer, correct_answer):
        if correct_answer.lower() == answer.lower():
            self.score += 1
            print("You got it right!")
        else:
            print(f"You're wrong.")
        print(f"The correct answer was: {correct_answer}.")
        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")



