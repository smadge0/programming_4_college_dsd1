def nametaker():
    #take the user's name
    name = input("Enter your first name: ")
    secondname = input("Enter your second name: ")
    #take the length of both first and last names
    length1 = len(name)
    length2 = len(secondname)
    #calculate total length of full name
    total = length1 + length2
    #if name is too long, display error and restart. otherwise, print name and its length.
    if total > 20:
         print("That name is too long! Try again.")
         nametaker()
    else:
        print("Hello,", name, secondname+"!")
        print("Your name is", str(total), "characters long!") #print's user's name and length

nametaker()