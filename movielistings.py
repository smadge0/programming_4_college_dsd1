movies = ["Friday the 13th", "Friday the 13th Part II", "Friday the 13th Part III", "Friday the 13th: The Final Chapter", "Friday the 13th: A New Beginning", "Friday the 13th Part VI: Jason Lives", "Friday the 13th Part VII: The New Blood", "Friday the 13th Part VIII: Jason Takes Manhattan", "Jason Goes to Hell: The Final Friday", "Jason X", "Freddy vs. Jason", "Friday the 13th (2009 reboot)"]

def addmovie (movies):
    added = int(input("How many movies would you like to add to the listings? "))
    for x in range(0, added):
        movie = input("Enter the movie you want to add: ")
        print(f"Movies added: {x+1}")
        movies.append(movie)
    goback = input("Return to menu? (y/n) ")
    if goback == "y":
        menu()
    else:
        print("Program ending")
    return movies

def removie(movies):
    removed = int(input("How many movies would you liek to remove from the listings? "))
    for x in range(0, removed):
        movie = input("Enter the name of the movie you want to remove (Case sensitive): ")
        movies.remove(movie)
        print(f"Movies removed: {x+1}")
        print("The new list is:")
        for x in range(0, len(movies)):
            print(movies[x])
    goback = input("Return to menu? (y/n) ")
    if goback == "y":
        menu()
    else:
        print("Program ending")
    return movies




def menu(movies):
    navigator = input("Where would you like to go?\nEnter 1 to display the current list of movies.\nEnter 2 to add movies to the list.\nEnter 3 to remove movies from the list.\n Enter here: ")
    if navigator == "1":
        for x in range (0,len(movies)):
            print(movies[x])
            menu()
    elif navigator == "2":
        addmovie(movies)
    elif navigator == "3":
        removie(movies)

menu(movies)      



    