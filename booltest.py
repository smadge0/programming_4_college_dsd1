num = int(input("Enter a number: "))
check = (num >= 0 and num <= 100)
print(check)
if check == True:
    print("That number is between 1 and 100!")
elif check == False:
    print("That number wasn't between 1 and 100.")
