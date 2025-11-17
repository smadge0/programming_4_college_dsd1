def balancecalc(calc,currentbalance):
    if calc == "withdraw":
        val = float(input("How much are you withdrawing (£X.XX)"))
        currentbalance = currentbalance - val
        confirm = input(f"Your balance after this withdrawal will be £{currentbalance}, confirm withdrawal? (yes/no)")
        if confirm == "yes":
            print(f"Withdrawal complete! Your current balance is now {currentbalance}.")
        if confirm == "no":
            currentbalance = currentbalance + val
            print(f"Withdrawal cancelled. Your current balance is now {currentbalance}.")
    elif calc == "deposit":
        val = float(input("How much are you depositing? (£X.XX) "))
        currentbalance = currentbalance + val
        confirm = input(f"Your balance after this deposit will be £{currentbalance}, confirm deposit? (yes/no)")
        if confirm == "yes":
            print(f"Your current balance is now {currentbalance}.")
        if confirm == "no":
            currentbalance = currentbalance - val
            print(f"Deposit cancelled. Your current balance is now {currentbalance}.")




def bankasker(currentbalance):
    money = input("Would you like to see your balance? (yes/no) ")
    if money == "yes":
        print(f"{currentbalance}")
        calc = input("Would you like to withdraw or deposit? (withdraw/deposit/no)")
    if money == "no":
        print("baller")
    if calc == "no":
        print("Okay, have a nice day.")
    else:
        balancecalc(calc,currentbalance)


currentbalance = float(input("What is your current balance? (X.XX)"))
bankasker(currentbalance)