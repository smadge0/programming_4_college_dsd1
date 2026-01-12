loans = [{"loan_id":1,"student_name":"John Marston","student_id":"S12345","device_type":"laptop","device_id":"L-001","date_out":"24-11-2025","due_back":"01-12-2025","returned":False},
         {"loan_id":2,"student_name":"Arthur Morgan","student_id":"S54321","device_type":"tablet","device_id":"T-001","date_out":"10-11-2025","due_back":"24-11-2025","returned":True}
         ]

def loanchecker(loans):
    id = input("Enter the ID of the loan you wish to view: ")
    try:
        int(id)
    except:
        print("Please enter a valid loan ID. (Must be an integer.)")
        loanchecker(loans)
    id = int(id)
    for x in range(0,len(loans)):
        if loans[x]["loan_id"] == id:
            print(f"ID found\nLoan information: {loans[x]}")
        else:
            print("Loan ID not found. Please try another loan ID.")


def loanchanger(loans):
    changes = True
    while changes == True:
        start = input("Would you like to update or delete a loan's information? ")
        if start == "update":
            update = input("Enter the ID of the loan you want to update: ")
            try:
                int(update)
            except:
                print("Invalid ID entered. Please try again.")
                continue

            for x in range(0,len(loans)):
                if loans[x]["loan_id"] == int(update):
                    print("ID found.")
                else:
                    print("Loan ID not found. Please try another loan ID.")
            field = input("Which field are you trying to update? Enter returned or due_back) ")
            if field == "returned":
                returned = input("Has the device been returned? (y/n) ")
                if returned == "y":
                    loans[int(update)][field] = True
                elif returned == "n":
                    loans[int(update)][field] = False
                    keepgoing = input("Would you like to update/delete any other information? (y/n) ")
                    if keepgoing == "y":
                        continue
                    else:
                        changes = False
            elif field == ""

loanchanger(loans)


