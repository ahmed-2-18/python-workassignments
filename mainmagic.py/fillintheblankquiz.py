
questions =[
    {"Question":"What is 2x5", "Answer": 10,},
    {"Question": "What is 15x2", "Answer": 30},
    {"Question": "What is 100x2","Answer": 200},
    {"Question": "What is 50x2","Answer": 100},
    {"Question": "What is 25x2","Answer": 50},
    {"Question": "What is 25+2","Answer": 27},   ]

correctAnswers = []

wrongAnswers = []


def askQuestion(questionText, actualAnswer):
    while True:
        print(questionText)
        userAnswer = input()
        userAnswer = int(userAnswer)
        if userAnswer == actualAnswer:
            return True
        else:
            wrongAnswers.append(questionText)
            print("Try again")
       
        





def main():
    for each in questions:
        correctOrNot = askQuestion(each["Question"], each["Answer"])
        if correctOrNot == True:
            correctAnswers.append(each)
        else:
            wrongAnswers.append(each)


    return

main()

print("Your correct answers were:      ")
print(correctAnswers)
print("Your wrong answers were:        ")
print(wrongAnswers)