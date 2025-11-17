def bloodcounter():
    weight = float(input("How much does the person weigh? (in KG)"))
    totalblood = weight * (10 ** 3) * 0.07
    bloodloss = float(input("How much blood have they lost (in millilitres): "))
    if bloodloss < totalblood * 0.15:
        print("This is below the safe amount to lose. The person should recover with no adverse effects")
    elif bloodloss > totalblood * 0.15:
        print("too much blood!!! 😨😨 helppp helpt jhme helppPpm them!!!")



bloodcounter()














