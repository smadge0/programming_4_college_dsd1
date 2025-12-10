valid = False



def encryption(key):
    result = ""
    message = input("What is the message you would like to encrypt? ")
    for char in message:
        if char.isupper():
            result += chr((ord(char) - 65 + key) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) - 97 + key) % 26 + 97)
        elif char.isalpha:
            result += char
    return result




def decryption(key):
    result = ""
    message = input("Enter the message you are trying to decrypt: ")
    trykey = int(input("Enter the key you want to use: "))
    for char in message:
        if char.isupper():
                result += chr((ord(char) - 65 - trykey) % 26 + 65)
        elif char.islower():
                result += chr((ord(char) - 97 - trykey) % 26 + 97)
        elif char.isalpha():
                result += char
    return result



def menu(key):
    whattodo = input("Are you encrypting or decrypting a message? (Enter E or D): ")
    if whattodo == "e":
        result = encryption(key)
        print(f"Your encrypted message is {result}")
        
    elif whattodo == "d":
        result = decryption(key)
        print(result)
        goagain = input("Would you like to decrypt/encrypt another message? (y/n): ")


while valid == False:
   key = int(input("How many places would you like to shift your characters by? (1-25) "))
   if key < 1 or key > 25:
       print("Invalid key entry, please try again.")
       continue
   else:
       valid = True
menu(key)

