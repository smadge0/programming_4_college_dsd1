import csv


leaderboard = {}
x = 0

def leaderboardmaker(leaderboard):
    with open("scores.csv","r") as file:
        reader = csv.reader(file)
        for line in reader:
            line[1] = int(line[1])
            leaderboard[line[0]] = line[1]
        print(leaderboard)
        #has not yet been sorted . crying emoji





def add_score(username, score):
     with open("scores.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([username, score])
    

def show_scores():
    with open("scores.csv", "r", newline="") as file:
        reader = csv.reader(file)
        for line in reader:
            print(f"{line[0]} scored {line[1]}")

def main():
    while True:
        print("\n1. Add score")
        print("2. Show all scores")
        print("3. Show leaderboard")
        print("4. Quit")
        choice = input("Choose an option: ")

        if choice == "1":
            username = input("Enter username: ")
            score = int(input("Enter score: "))
            add_score(username, score)
        elif choice == "2":
            show_scores()
        elif choice == "3":
            leaderboardmaker(leaderboard)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()