def parcel_code():
    incorrects = 0
    while True:
        parcelcode = input("Enter a parcel code: ")
        if len(parcelcode) != 7:
            print("Invalid code. The code must be 7 digits long.")
            continue
        else:
            try:
                int(parcelcode)
            except:
                print("Invalid code. Code must only include integers.")
            else:
                incorrects = code_checker(parcelcode,incorrects)
                code_checker(parcelcode,incorrects)



def code_checker(parcel_code,incorrects):
    totalvalue = 0
    checksum = parcel_code[6]
    code = parcel_code[0:6]
    for x in range(len(code)):
        number = code[x]
        number = int(number)
        numbervalue = number * (x+1)
        totalvalue = totalvalue + numbervalue
    remainder = totalvalue % 10
    print(totalvalue)
    print(remainder)
    if remainder == int(checksum):
        print("Valid code")
    else:
        print("Invalid code")
        incorrects = incorrects + 1
        print(f"{incorrects} incorrect attempts.")
        


    


parcel_code()


