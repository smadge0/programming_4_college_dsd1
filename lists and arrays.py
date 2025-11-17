def lists():
    energylevels = ["low", "medium", "high", "medium", "low"]
    wellbeingnames = ["fitnessfinley","smoothiesamantha","matchamargaret","athleticalison","thitnesstheo","buffbob"]
    stepcounts = [7355,12380,9738,5603,11739]
    action = input("What would you like to access? You can see: \nDaily energy levels (Enter 1) \nUsernames from the wellbeing app (Enter 2) \nStepcounts from the past week (Enter 3)\n>> ")
    if action == "1":
        action = input("Print whole list (1), print the middle of the list (2), or add something to the list (3)? ")
        if action == "1":
            for x in range(len(energylevels)):
                print(f"Energy level {x}: {energylevels[x]}")
                action = input("")
        elif action == "2":
            print(energylevels[len(energylevels)//2])
        elif action == "3":
            newitem = input("What would you like to add to the list? ")
            energylevels.append(newitem)
    elif action == "2":
        action = input("Print whole list (1), print the middle of the list (2), or add something to the list (3)? ")
        if action == "1":
            for x in range(len(wellbeingnames)):
                print(f"Username {x}: {wellbeingnames[x]}")
                action = input("")
        elif action == "2":
            print(wellbeingnames[len(wellbeingnames)//2])
        elif action == "3":
            newitem = input("What would you like to add to the list? ")
            wellbeingnames.append(newitem)
    elif action == "3":
        action = input("Print whole list (1), print the middle of the list (2), or add something to the list (3)? ")
        if action == "1":
            for x in range(len(stepcounts)):
                print(f"Step count {x}: {stepcounts[x]}")
                action = input("")
        elif action == "2":
            print(stepcounts[len(stepcounts)//2])
        elif action == "3":
            newitem = input("What would you like to add to the list? ")
            stepcounts.append(newitem)



def indexing():
    screentimes = [120,95,140,160,80,100,200]
    print(f"The 3rd value is {screentimes[2]}")
    print(f"The average is {(screentimes[0]+screentimes[1]+screentimes[2])//3}")
    replacement = int(input("What will be the new final value? "))
    screentimes[6] = replacement
    print(f"The new final value is {screentimes[6]}")
    print(f"Highest value: {max(screentimes)}    Lowest value: {min(screentimes)}")


def mixedlists():
    mysafelist = [1,2,3]
    myevilmixture = [1.44,7,3]
    print(max(mysafelist))
    print(max(myevilmixture))
#List prints as normal
#min/max cannot compare numerical and non numerical types


def notiftracker():
    notifs = [34,28,55,40,60,22,18]
    notifs2 = [38,24,55,35,15,20,45]
    print(f"The day with the most notifications was day {notifs.index(max(notifs))+1}.")
    print(f"The day with the least notifications was day {notifs.index(min(notifs))+1}.")
    print(f"The total number of notifications over the week was {sum(notifs)}.")
    newvalue = int(input("Enter the number of notifications from the next day (must be an integer): "))
    notifs.append(newvalue)
    print(f"The list is now: {notifs}")
    print(f"The total number of notifications over the week for user 2 was {sum(notifs2)}.")
    difference = sum(notifs) - sum(notifs2)
    if difference > 0:
        print(f"This was {difference} less than user 1.")
    elif difference == 0:
        print("This was the same as user 1.")
    elif difference < 0:
        print(f"This was {difference} more than user 1.")

notiftracker()

    

    
 