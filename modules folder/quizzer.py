import random as rand
import numpy as np
import math








def menu():
    flag = True
    while flag == True:
        difficulty = input("Enter your desired difficulty level (1-4) ")
        try:
            int(difficulty)
        except:
            print("Invalid input")
            flag = True
        else:
            difficulty = int(difficulty)
            if difficulty > 1 or difficulty < 1:
                print("Invalid input")
                flag = True
                continue
            else:
                flag = False
                print("Choice accepted")
    match difficulty:
        case 1:
            quiz_easy()




def quiz_easy():
    score = 0
    answers = 0
    easy = False
    operators = ["*","/","+","-","root"]
    questions = input("How many questions would you like to answer? ")
    try:
        int(questions)
    except:
        print("Invalid input, please enter an integer (e.g. 5)")
    else:
        questions = int(questions)
        if questions < 1:
            print("Invalid input. Please enter a number greater than 0.")
    
    for x in range(0,questions):
        operator = operators[rand.randint(0,4)]
        num1 = rand.randint(1,20)
        num2 = rand.randint(1,20)
        if operator == "+":
            answer = num1 + num2
            question = (f"What is {num1} {operator} {num2}?")
        elif operator == "-":
            answer = num1 - num2
            question = (f"What is {num1} {operator} {num2}?")
        elif operator == "*":
            answer = num1 * num2
            question = (f"What is {num1} {operator} {num2}?")
        elif operator == "/":
            while easy == False:
                num1 = rand.randint(1,20)
                num2 = rand.randint(1,20)
                if math.ceil(num1/num2) == num1/num2:
                    easy = True
                    question = (f"What is {num1} {operator} {num2}?")
                    answer = num1/num2
                elif math.ceil != (num1/num2) and math.floor != num1/num2:
                    easy = False
        elif operator == "root":
            num1 = num1**2
            question = (f"What is the square root of {num1}?")
            answer = math.sqrt(num1)

        flag = True
        print(f"Your question is {question}")
        while flag == True:
            playeranswer = input("Enter your answer here: ")
            try:
                int(playeranswer)
            except:
                print("Please enter an integer for your answer. ")
                flag = True
            else:
                playeranswer = int(playeranswer)
                flag = False
        if playeranswer == answer:
            print("Good job! You got it correct!")
            score = score + 1
            answer = answers + 1
            print(f"Your current score is {score} out of {questions}.")
        else:
            answers = answers + 1
            print(f"That answer was incorrect. The answer was actually {answer}! Better luck next time.")
            print(f"Your current score is {score} out of {questions}.")
    print(f"Your final score was {score} out of {questions} questions!")
    if score == questions:
        print("Amazing! You got a full score!")
    elif score < questions and score > questions - 5:
        print("Good job! You got a great score.")
    elif score <= questions - 5 and score > questions - 10:
        print("Nice attempt! You got a decent score.")
    else:
        print("That's not a great score. Better luck next time.")

    restart = input("Would you like to try again? Input 1 to restart, or 2 to end the quiz.")
    flag = True
    while flag == True:
        try:
            int(restart)
        except:
            print("Please select either 1 or 2")
            flag = True
        else:
            restart = int(restart)
            flag = False
    if restart == 1:
        quiz_easy()
    else:
        print("Goodbye!")

menu()
    

    

            



