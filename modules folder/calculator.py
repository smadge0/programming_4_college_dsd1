import math
import random as rand
import datetime as date

def t1():
    number = float(input("emter a number: "))
    root = math.sqrt(number)
    square = math.pow(number,2)
    upper = math.ceil(number)
    lower = math.floor(number)
    circle = math.pi * square

    print(f"The square root is {round(root,2)}, the squared number is {round(square,2)}, the number rounded up is {upper}, the number rounded down is {lower}, the area of a circle with that number as the radius is {round(circle,2)}")


def t2():
    lives = 3
    wins = 0
    rounds = 0
    while lives > 0:
        dice1 = rand.randint(1,6)
        dice2 = rand.randint(1,6)
        totalscore = dice1+dice2
        print(f"Your score was {totalscore}.")
        if totalscore == 7 or totalscore == 11:
            wins = wins + 1
            rounds = rounds + 1
            lives = 0
            winpercent = (wins/rounds)*100
            print("You win!")
            print(f"Your current win percentage is: {round(winpercent,2)}%")
            choice = input("Play again? (Y/N)")
            choice = choice.lower()
            if choice == "y" or choice == "n":
                lives = 3
            else:
                print("Goodbye!")
        else:
            rounds = rounds + 1
            lives = lives - 1
            if wins > 0:
                winpercent = (wins/rounds)*100
            else:
                winpercent = 0
            print(f"Your current win percentage is: {round(winpercent,2)}%")
            print(f"You have {lives} lives remaining.")
            print("Try again")

def t3():
    currentdate = date.datetime.now()
    print(f"Today's date is {currentdate.strftime('%d/%m/%Y')}")
    birthday = input("Enter your birthday: (DD/MM/YYYY) ").split("/")
    birthdate = date.datetime(int(birthday[2]),int(birthday[1]),int(birthday[0]))
    print(birthdate)
    age = currentdate.year - birthdate.year - ((currentdate.month,currentdate.day) < (birthdate.month, birthdate.day))
    print(age)
    nextbday = date.datetime(currentdate.year,int(birthdate[1]),int(birthdate[0]))
    daystogo = nextbday - currentdate
    print(f"There are {daystogo} days remaining until your birthday")

        
    
  


t3()

    