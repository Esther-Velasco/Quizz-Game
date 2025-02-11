from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

#Create a for loop to iterate over the question_data
#Create a question object from each entry in question_data
#Append each Question object to question_bank
question_bank = []

for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    question_object = Question(question_text, question_answer)
    question_bank.append(question_object)
    
quiz = QuizBrain(question_bank)

while quiz.still_has_questions() == True:
    quiz.next_question()
    
print("\n")
print("You have completed the quiz")
print(f"Your final score is {quiz.score}/{len(question_bank)}")



