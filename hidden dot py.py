# Clinic vaccine stock (single brand for simplicity)

def dispense(doses, stock):
    stock = stock - doses
    print("Dispensed:", doses, "Remaining:", stock)
    return stock

def restock(amount, stock):
    print("Before restock:", stock)
    stock = stock + amount
    print("After restock:", stock)
    return stock


stock = 50
stock = dispense(5, stock)
stock = restock(10, stock)
print("End of day stock:", stock)
