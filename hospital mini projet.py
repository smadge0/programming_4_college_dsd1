MGCONVRATE = (1/18)
MMOLCONVRATE = (18)
unknown = False
total_patients = 0
FEVER = 38
MAXHEARTRATE = 220
DAILYWATER = 2000

def unitconverter(MGCONVRATE, MMOLCONVRATE,unknown):
    test = input("What type of test did you perform? Enter 'unknown' if that is the case. ")
    if test == "unknown":
        unknown = True
        outcome = int(input("That's fine. If possible, enter the test's result here: "))
        unit = input("What unit was this value in? (mg/dL OR mmol/L) Enter 'unknown' if that is the case. ")
        if unit == "unknown":
            print("Sorry, but this can't be converted if you don't know the unit. Please try and find out what unit this value is and then try again.")
            unitconverter(MGCONVRATE,MMOLCONVRATE,unknown)
        elif unit == "mg/dL":
            converted = outcome * MGCONVRATE
        elif unit == "mmol/L":
            converted = outcome * MMOLCONVRATE
        else:
            print("That's not a valid unit entry. Please try again.")
            unitconverter(MGCONVRATE,MMOLCONVRATE,unknown)
    else:
        outcome = int(input("What number did the test produce? "))
        unit = input("What unit was this value in? (mg/dL OR mmol/L) Enter 'unknown' if that is the case. ")
        if unit == "unknown":
            print("Sorry, but this can't be converted if you don't know the unit. Please try and find out what unit this value is and then try again.")
            unitconverter(MGCONVRATE,MMOLCONVRATE,unknown)
        elif unit == "mg/dL":
            converted = outcome * MGCONVRATE
        elif unit == "mmol/L":
            converted == outcome * MMOLCONVRATE
        else:
            print("That's not a valid unit entry. Please try again.")
            unitconverter(MGCONVRATE,MMOLCONVRATE,unknown)
    if unit == "mg/dL" and unknown == False:
        print(f"You performed a test for {test}. The results for this test were {outcome} {unit}. The converted outcome is {round(converted,2)} mmol/L.")  
    elif unit == "mmol/L" and unknown == False:
        print(f"You performed a test for {test}. The results for this test were {outcome}{unit}. The converted outcome is {round(converted,2)} mg/dL.")
    elif unknown == True and unit == "mmol/L":
        print(f"You performed an unknown test with the outcome of {outcome} {unit}. This has been converted to {round(converted,2)} mg/dL.")
    elif unknown == True and unit == "mg/dL":
        print(f"You performed an unknown test with the outcome of {outcome} {unit}. This has been converted to {round(converted,2)} mmol/L.")
    

    goback = input("Return to menu? (y/n) ")
    if goback == "y":
        menu()
    else:
        print("Okay.")

def tempchecker(FEVER):
    check1 = float(input("Enter the first checked temperature: "))
    check2 = float(input("Enter the second checked temperature: "))
    check3 = float(input("Enter the third checked temperature: "))
    if check1 < 30 or check1 > 45 or check2 < 30 or check2 > 45 or check3 < 30 or check3 > 45:
        print("That is an invalid temperature input. Please ensure you inputted a correct temperature next time.")
        tempchecker(FEVER)
    tempaverage = round((check1+check2+check3) / 3, 2)
    if tempaverage >= FEVER:
        print(f"The average temperature was {tempaverage}. This is above the fever threshold, be careful.")
    elif tempaverage < FEVER:
        print(f"The average temperature was {tempaverage}. This is under the fever threshold.")
    
    goback = input("Return to menu? (y/n) ")
    if goback == "y":
        menu()
    else:
        print("Okay.")
    


def heartmonitor(MAXHEARTRATE):
    morepatients = True
    while morepatients == True:
        age = int(input("Enter the patient's age: "))
        heartrate = int(input("Enter the patient's resting heart rate: "))
        saferate = MAXHEARTRATE - age
        if heartrate > (saferate * 0.85):
            print(f"A resting heart rate of {heartrate} is too high, and could be dangerous.")
        elif heartrate <= (saferate * 0.85) and heartrate >= (saferate * 0.5):
            print(f"A resting heart rate of {heartrate} is in the normal range, and is safe.")
        elif heartrate > (saferate * 0.5) and heartrate > 0:
            print(f"A resting heart rate of {heartrate} is too low, and may be dangerous.")
        elif heartrate <= 0:
            print(f"Your patient is either dead or this is an invalid input.")
        validinput = False
        while validinput == False:
            morepatients = input("Would you like to enter another patient's information? (y/n) ")
            if morepatients == "y":
                validinput = True
                morepatients = True
            elif morepatients == "n":
                print("Okay. No more patients will be entered.")
                validinput = True
                morepatients = False
            else:
                print("Not a Y/N input. Please try again.")
                validinput = False
    goback = input("Return to menu? (y/n) ")
    if goback == "y":
        menu()
    else:
        print("Okay.")


def hydration(DAILYWATER):
    water = int(input("How much water have you drank today (in millilitres)? "))
    difference = DAILYWATER - water
    if difference <= 0:
        print("Good job! You've met your daily water target.")
    elif difference > 0 and difference < 2000:
        print(f"You didn't meet your water target yet today, and you're currently {difference}ml away from your goal.")
    elif difference == 2000:
        print("You haven't drink any water today? You might want to start doing that if you want to meet your goal.")
    elif difference > 2000:
        print("You can't drink negative water. Seriously.")
    
    watering = True
    while watering == True:
        checkagain = input("Would you like to check your water intake again? (y/n)")
        if checkagain == "y":
            watering = False
            hydration(DAILYWATER)
        elif checkagain == "n":
            watering = False
            print("Okay! Good luck reaching your goal tomorrow.")
        else:
            watering = True
            print("That wasn't a y/n input, try again.")
    goback = input("Return to menu? (y/n) ")
    if goback == "y":
        menu()
    else:
        print("Okay.")




def add_patient(total_patients):
    total_patients += 1
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    print("Patient added:", name)
    menu()





def menu():

    access = input("\nWhat would you like to do right now? You can either:\nCheck water\nCheck heart rate\nCheck temperature\nConvert mmol/L and mg/dL\n\nEnter 'Water', 'Heart', 'Temperature', 'Convert' or 'Add': ")
    if access == "Water":
        hydration(DAILYWATER)
    elif access == "Heart":
        heartmonitor(MAXHEARTRATE)
    elif access == "Temperature":
        tempchecker(FEVER)
    elif access == "Convert":
        unitconverter(MGCONVRATE,MMOLCONVRATE,unknown)
    elif access == "Add":
        add_patient(total_patients)
    else:
        print("That's not a valid input.")
        menu()

menu()
    
        


    




    


