end = False
scores = []

print("Enter as many test scores as necessary")

while end == False:
    score = int(input("Enter a test score: "))
    scores.append(score)
    loop = input("Would you like to enter another score? Yes/No: ")
    if loop == "Yes":
        end = False
    elif loop == "No":
        end = True
    else:
        print("Invalid entry.")
        end = True
        
    

print(scores)
for x in range(0,len(scores)+1):
    total = sum(scores)

average = total / len(scores)
print("The average test score was", str(average))
        


