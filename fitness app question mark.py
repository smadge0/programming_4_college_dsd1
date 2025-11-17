def calorieburner():
    calspermin = int(input("How many calories do you burn per minute during your workout? "))
    workouttime = int(input("How many minutes were you exercising for? "))
    calsburnt = calspermin * workouttime
    print(f"You have burnt {calsburnt} calories during this workout. Good job!")
    goback = input("Would you like to return to the menu? (Enter Y or N): ")
    if goback == "Y" or goback == "y":
        menu()
    elif goback == "N" or goback == "n":
        print("Okay! Have a good day.")
    

def stepconverter():
    steps = int(input("How many steps have you walked? "))
    distance = steps / 1300
    print(f"You have walked {distance} kilometres. Good job!")
    goback = input("Would you like to return to the menu? (Enter Y or N): ")
    if goback == "Y" or goback == "y":
        menu()
    elif goback == "N" or goback == "n":
        print("Okay! Have a good day.")
    

def medstimer():
    medtime = int(input("How many minutes are left until the next dose? "))
    medhours = medtime // 60
    medmins = medtime % 60
    print(f"It is {medhours} hours and {medmins} minutes until your next dose.")
    goback = input("Would you like to return to the menu? (Enter Y or N): ")
    if goback == "Y" or goback == "y":
        menu()
    elif goback == "N" or goback == "n":
        print("Okay! Have a good day.")
    
def medusage():
    medsperpack = int(input("How many tablets are in each pack? "))
    packs = int(input("How many packs of tablets are being distributed? "))
    totaltablets = int(input("How many tablets in total are there? "))
    leftovermeds = totaltablets % (medsperpack * packs)
    fullpacks = totaltablets // (medsperpack * packs)
    print(f"There will be a total of {fullpacks} packs distributed, with {leftovermeds} tablets left over.")
    goback = input("Would you like to return to the menu? (Enter Y or N): ")
    if goback == "Y" or goback == "y":
        menu()
    elif goback == "N" or goback == "n":
        print("Okay! Have a good day.")

def heartrecovery():
    resttime = 0
    heartrate = int(input("What is your current heart rate? "))
    restrate = int(input("What is your resting heart rate? "))
    while heartrate > restrate:
        resttime = resttime + 1
        heartrate = heartrate * (0.9 ** resttime)
        if heartrate >= restrate:
            print(f"After {resttime} minute(s), your heart rate will be {int(heartrate)}")
        elif heartrate < restrate:
            print(f"After {resttime} minute(s), your heart rate will be {restrate}")
    goback = input("Would you like to return to the menu? (Enter Y or N): ")
    if goback == "Y" or goback == "y":
        menu()
    elif goback == "N" or goback == "n":
        print("Okay! Have a good day.")


def menu():
    choice = input("What would you like to do? \nEnter 1 for calories burnt. \nEnter 2 for converting steps to kilometres. \nEnter 3 to convert minutes until a medicine dose into hours and minutes. \nEnter 4 to calculate leftover tablets from distributing pack. \nEnter 5 for a heart rate recovery model. \nYour choice: ")
    if choice == "1":
        calorieburner()
    elif choice == "2":
        stepconverter()
    elif choice == "3":
        medstimer()
    elif choice == "4":
        medusage()
    elif choice == "5":
        heartrecovery()

























