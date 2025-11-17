arcade = {
    "Space Invaders": {"Status":"Working Order", "Category":"Shooter"}, 
    "Pac-Man":{"Status":"Working Order", "Category":"Maze Chase"}, 
    "Lane Master XTreme":{"Status":"Needs Service", "Category":"Bowling"}, 
    "Fix-it Felix Jr.":{"Status":"Working Order", "Category":"Wreck-it Ralph"}, 
    "Street Fighter":{"Status":"Needs Service", "Category":"2D Fighter"}
}


def viewmachines(arcade):
    for key in arcade.keys():
        print(key)



def addmachines(arcade):
    newmachine = input("Name of new machine: ")
    machinestatus = input("Current status of new machine: ")
    machinecategory = input("Category of new machine: ")
    arcade.update({newmachine: {"Status":machinestatus, "Category":machinecategory}})
    viewmachines(arcade)

def updatestatus(arcade):
    print("Which machine's status are you updating? ")
    viewmachines(arcade)
    updatedmachine = input("Input here: ")
    status = input("What is the status of this machine? ")
    arcade[updatedmachine]["Status"] = status
    print("Status updated.")

def removemachine(arcade):
    print("Which machine is being removed? ")
    viewmachines(arcade)
    gonegame = input("Input here: ")
    del arcade[gonegame]
    print("Current list of machines: ")
    viewmachines(arcade)

def brokenmachines(arcade):
    broken = 0
    for key in arcade.keys():
        if arcade[key]["Status"] == "Needs Service":
            broken = broken + 1
    print(f"There are currently {broken} machines out of order. ")





