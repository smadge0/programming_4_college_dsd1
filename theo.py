import random

def addscores():
    name = input("Enter your name: ")
    score = input("Enter your score:")
    if name == "" or score == "":
       print("Please enter values into both fields.")
       addscores()
    else:
       try:
          int(score)
       except:
          print("Please enter a number into the score field.")
          addscores()
    with open("scoresfile.txt","a") as file:
       file.write(f"Name: {name}, Score: {score}\n\n")
    morescore = input("Enter another player's info? (y/n)")
    if morescore == "y":
       addscores()
    elif morescore == "n":
       print("yeah ok")

def readscores():
   with open("scoresfile.txt","r") as file:
      for line in file:
         print(line)

def clearscores():
   with open("scoresfile.txt","w") as file:
      file.write("")


plssaywhattodo = input("what do you want")
if plssaywhattodo == "addscores":
   addscores()
elif plssaywhattodo == "readscores":
   readscores()
elif plssaywhattodo == "clearscores":
   clearscores()
else:
   print("wrong answer")





