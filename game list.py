games = [["Big John Bonanza", False, False, False],["Big John's Big Breakout", False, False, False], ["Bosh Simulator", False, False, False], ["Big John 2: Electric Boogaloo", False, False, False], ["Big John: Finale of Johnathan", False, False, False], ["The Return of John: The Boshening", False, False, False]]
def gamedisplay(games):
    print("Current list of games: ")
    for x in range (0,len(games)):
        print(f"Game number {x+1} is {games[x][0]}")


def gamestatus(games):
    keepgoing = True
    gamedisplay(games)
    updategame = input("Would you like to update the status of a game? (Y/N) ")
    while keepgoing == True:
        if updategame == "Y":
            statuschange = input("What would you like to do? You can either:\nSet a favourite (F) \nSet a game to played (P) \n Set a game to currently playing (C) ")
            if statuschange == "F":
                favourite = input("Enter the title of the game you want to set as your favourite: ")
                for x in range(0,len(games)):
                    if favourite == games[x][0]:
                        games[x][1] = True
                print(f"{favourite} has been set to a favourite.")
            elif statuschange == "P":
                played = input("Enter the title of the game you want to set as played: ")
                for x in range(0,len(games)):
                    if played == games[x][0]:
                        games[x][2] = True
                print(f"{played} has been set to played.")
            elif statuschange == "C":
                current = input("Enter the title of the game you want to set as currently playing: ")
                for x in range(0,len(games)):
                    if current == games[x][0]:
                        games[x][1] = True
                print(f"{favourite} has been set to currently playing.")
        keepgoing = input("Would you like to change the status of another game? (Y/N) ")
        if keepgoing == "Y":
            keepgoing = True
        else:
            keepgoing = False
            print("Okay.")
            statuslist(games)


        


    

def statuslist(games):
    statuscheck = input("Would you like to check your favourite games, your played games, or the games you are currently playing? Enter F, P or C respectively. ")
    if statuscheck == "F":
        for x in range(0,len(games)):
            if games[x][1] == True:
                print(games[x][0])
    elif statuscheck == "P":
          for x in range(0,len(games)):
            if games[x][2] == True:
                print(games[x][0])     
    elif statuscheck == "C":
           for x in range(0,len(games)):
            if games[x][2] == True:
                print(games[x][0])          


gamestatus(games)

