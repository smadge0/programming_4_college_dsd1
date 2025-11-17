def patientfile():
    global age
    global height
    global weight
    name = input("Enter patient name: ")
    age = int(input("Enter patient age: "))
    height = float(input("Enter patient height (cm): " ))
    weight = float(input("Enter patient weight (kg): "))

    print(f"Patient name: {name}\nPatient age: {age}.\nPatient height: {height}cm\nPatient weight: {weight}kg")  
    menu()

    return name, age, height, weight
 



def bmicalc(height,weight):
    bmi = weight / (height / 100) ** 2
    print(f"Patient BMI is {round(bmi, 2)}")
    if bmi < 18.5 and bmi > 0:
        bmicategory = "Underweight"
        print("BMI is under 18.5. Patient is underweight.")
    elif bmi >= 18.5 and bmi < 25:
        bmicategory = "Healthy weight"
        print("BMI is in the healthy range.")
    elif bmi >= 25 and bmi < 30:
        bmicategory = "Overweight"
        print("BMI is over 25. Patient is possibly overweight.")
    elif bmi > 30:
        bmicategory = "Obese"
        print("BMI is over 30. Patient is possibly at risk of obesity.")
    else:
        bmicategory = "huh ???"
        print("Invalid BMI returned, please enter patient info correctly.")
        patientfile()
    print(f"Patient BMI category is: {bmicategory}")
    menu()

def dontoverdose(maxdose, age):
    if age <= 1 and age > 0:
        maxdose = maxdose - 500
    elif age > 1 and age <= 4:
        maxdose = maxdose - 400
    elif age > 4 and age <= 11:
        maxdose = maxdose - 250
    elif age > 11 and age <= 17:
        maxdose = maxdose - 50
    elif age > 17:
        maxdose = maxdose
    else:
        print(" ??? ?why is the age wrong. fix it. please")
        patientfile()
    dailydose = float(input("How much of the medicine has the patient taken today (milligrams): "))
    if dailydose < maxdose:
        safedose = True
        print(f"Patient has taken {dailydose}mg of medicine. This is under the safe maximum dosage limit.")
    elif dailydose == maxdose:
        safedose = True
        print(f"Patient has taken {dailydose}mg of mediicne. This is the maximum safe dosage limit.")
    elif dailydose > maxdose:
        safedose = False
        print(f"Patient has taken {dailydose}mg of medicine. This is over the safe maximum dosage limit.")
        menu()

    return safedose


def carecosts(DAYSTAY, SURGERY, MEDICINE, CONSULTCOST):
    stays = int(input("How many days was the patient in care for (if any? Enter 0 if not applicable.) "))
    hadsurgery = input("Did the patient have surgery? (Y/N) ")
    medcost = int(input("How many times was the patient administered medicine? "))
    consultation = input("Did the patient get a consulation? (Y/N) ")
    
    costs = (stays * DAYSTAY) + (medcost * MEDICINE)
    if hadsurgery == "Y":
        costs = costs + SURGERY
    
    if consultation == "Y":
        totalcosts = (costs + CONSULTCOST) * 1.2
    elif consultation == "N":
        totalcosts = costs * 1.2
    print(f"The total cost for this patient's treatment will be £{totalcosts}")
    menu()
    

    
def menu():
    action = input("What would you like to do? (Patient file must be entered to access other options: Patient file, Care cost, Dose check, BMI Calculation or enter 'end' to end the program.")
    if action.lower == "patient file":
        patientfile()
    elif action.lower == "care cost":
        carecosts(DAYSTAY, SURGERY, MEDICINE, CONSULTCOST)
    elif action.lower == "dose check":
        dontoverdose(maxdose, age)
    elif action.lower == "bmi calculation":
        bmicalc(height,weight)
    elif action.lower =="end":
        print("Program ended.")
   









DAYSTAY = 50
SURGERY = 200
MEDICINE = 100
CONSULTCOST = 150
maxdose = 750
checked = False
calced = False
carecosts(DAYSTAY, SURGERY, MEDICINE, CONSULTCOST)











