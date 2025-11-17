def bestmusic():
    objectivelybestmusic = ["Butcher Vanity ft. Yi Xi", "FIRE!!! ft. Kasane Teto", "BIRDBRAIN ft. Kasane Teto", "WEATHERGIRL ft. Eleanor Forte ", "FLOP ERA ft Akita Neru"]
    objectivelybestartists = ["FLAVOR FOLEY", "JamieP + Vane Lily", "JamieP", "FLAVOR FOLEY", "ePiaeon"]
    print("the objectively (my opinion is fact) best songs are: ")
    for x in range (0,5):
        print(f"{objectivelybestmusic[x]} by {objectivelybestartists[x]}")


def yourslop():
    yoursongs = []
    yourartists = []
    print("\nok enter your top 5 favourite songs: ")
    for x in range(0,5):
        song = input(f"song {x+1}: ")
        artist = input("enter the artist of that song: ")
        yoursongs.append(song)
        yourartists.append(artist)
    print("ok now i will print your . whatever the hell  you entered it probably sucks dude 👺")
    for x in range(0,5):
        print(f"your song {x+1}: {yoursongs[x]}")
        print(f"that song's artist: {yourartists[x]}")
    return yoursongs



    
    
