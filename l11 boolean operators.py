def medsSafety():
    weight = float(input("Enter the patient's weight (Kilograms): "))
    age = int(input("Enter the patient's age (Years): "))
    if age > 12 and weight > 40:
        print("It is safe to give this patient the medicine.")
    elif age < 12 or weight < 40:
        print("It is not safe to give this patient the medicine.")
    goback = input("Would you like to return to the menu? Enter Y to return or N to end the program. ")
    if goback == "Y":
        menu()
    elif goback == "N":
        print("Okay, the program will end now. Goodbye!")


def intensiveaccess():
    age = int(input("Enter age (Years): "))
    clear = input("Do they have medical clearance? (Y/N): ")
    if age >= 18 or clear == "Y":
        print("This person can access the intensive zone of the fitness centre.")
    elif age < 18 and clear == "N":
        print("This person is not permitted to enter the intensive zone of the fitness centre.")
    goback = input("Would you like to return to the menu? Enter Y to return or N to end the program. ")
    if goback == "Y":
        menu()
    elif goback == "N":
        print("Okay, the program will end now. Goodbye!")

def sleepalert():
    asleep = input("Is the person asleep? (Y/N): ")
    heartrate = int(input("What is the person's heart rate: "))
    if asleep == "N" and heartrate > 100:
        print("Alert: Heart rate exceeding 100.")
    elif asleep == "Y" or heartrate < 100:
        print("No alert needs to be sent.")
    goback = input("Would you like to return to the menu? Enter Y to return or N to end the program. ")
    if goback == "Y":
        menu()
    elif goback == "N":
        print("Okay, the program will end now. Goodbye!")

def menu():
    navigate = input("If you want to check if a patient can be given medication, enter 1.\n If you want to check if someone can access the intensive zone, enter 2.\n If you want to check if an alert needs to be sent, enter 3.\n If you are done, enter 'end'. \n")
    if navigate == "1":
        medsSafety()
    elif navigate == "2":
        intensiveaccess()
    elif navigate == "3":
        sleepalert()
    elif navigate == "end":
        print("Okay! Program will end.")
    else:
        print("Invalid input. Please try again.")
        menu()

menu()
        