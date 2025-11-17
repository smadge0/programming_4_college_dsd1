
passedexam = False

def infotaker():
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    testscore = float(input("Enter the score you got on your most recent test (1-100): "))
    if testscore >= 50 and testscore <= 100:
         passedexam = True
         print(f"Good job {name}! You passed your exam with a score of {testscore}! Most {age} year olds fail this exam!")
    elif testscore < 50 and testscore >= 0:
         print(f"Unfortunately {name}, you failed your exam. A score of {testscore} is not enough to pass. Better luck next time!")
    else:
          print(f"Sorry {name}, that's an invalid entry! Try again.")
          infotaker()
infotaker()
