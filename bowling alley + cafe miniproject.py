menu = [{"Hotdogs":{"Classic":7.00, "Dirty Dog":8.00,"Spicy Mexican":8.00,"Texan BBQ":8.00}, 
         "Nachos":{"Classic":6.00,"Beef Chili":7.50,"Five Bean Chili":7.50},
         "Loaded Fries":{"Classic Chips And Gravy":3.75,"Cheesy Chips":3.75,"Beef or Bean Chili":6.50,"Chicken Tikka":6.50,"Cheese and Bacon":6.25,"Steak and Chips":7.25},
         "Sides":{"Skinny Fries":3.25,"Traditional Chips":3.25,"Curly Fries":3.25,"Mixed House Salad":2.75,"Garlic Bread":3.00,"Crusty Bread Roll":1.00,"8 Onion Rings":3.50}
         }
         ]



orders = {"Prepared":[], 
          "Outstanding":[]
        }



bookings = {"Monday":{"Lane 1":{"12:00":False, "13:00":False, "14:00":False, "15:00":False, "16:00":False, "17:00":False, "18:00":False, "19:00":False, "20:00":False},
                      "Lane 2":{"12:00":False, "13:00":False, "14:00":False, "15:00":False, "16:00":False, "17:00":False, "18:00":False, "19:00":False, "20:00":False},
                      "Lane 3":{"12:00":False, "13:00":False, "14:00":False, "15:00":False, "16:00":False, "17:00":False, "18:00":False, "19:00":False, "20:00":False},
                      "Lane 4":{"12:00":False, "13:00":False, "14:00":False, "15:00":False, "16:00":False, "17:00":False, "18:00":False, "19:00":False, "20:00":False},
                      "Lane 5":{"12:00":False, "13:00":False, "14:00":False, "15:00":False, "16:00":False, "17:00":False, "18:00":False, "19:00":False, "20:00":False},
                      "Lane 6":{"12:00":False, "13:00":False, "14:00":False, "15:00":False, "16:00":False, "17:00":False, "18:00":False, "19:00":False, "20:00":False}},
            "Tuesday":{"Lane 1":{"12:00":False, "13:00":False, "14:00":False, "15:00":False, "16:00":False, "17:00":False, "18:00":False, "19:00":False, "20:00":False},
                      "Lane 2":{"12:00":False, "13:00":False, "14:00":False, "15:00":False, "16:00":False, "17:00":False, "18:00":False, "19:00":False, "20:00":False},
                      "Lane 3":{"12:00":False, "13:00":False, "14:00":False, "15:00":False, "16:00":False, "17:00":False, "18:00":False, "19:00":False, "20:00":False},
                      "Lane 4":{"12:00":False, "13:00":False, "14:00":False, "15:00":False, "16:00":False, "17:00":False, "18:00":False, "19:00":False, "20:00":False},
                      "Lane 5":{"12:00":False, "13:00":False, "14:00":False, "15:00":False, "16:00":False, "17:00":False, "18:00":False, "19:00":False, "20:00":False},
                      "Lane 6":{"12:00":False, "13:00":False, "14:00":False, "15:00":False, "16:00":False, "17:00":False, "18:00":False, "19:00":False, "20:00":False}},
            "Wednesday":{"Lane 1":{"12:00":False, "13:00":False, "14:00":False, "15:00":False, "16:00":False, "17:00":False, "18:00":False, "19:00":False, "20:00":False},
                      "Lane 2":{"12:00":False, "13:00":False, "14:00":False, "15:00":False, "16:00":False, "17:00":False, "18:00":False, "19:00":False, "20:00":False},
                      "Lane 3":{"12:00":False, "13:00":False, "14:00":False, "15:00":False, "16:00":False, "17:00":False, "18:00":False, "19:00":False, "20:00":False},
                      "Lane 4":{"12:00":False, "13:00":False, "14:00":False, "15:00":False, "16:00":False, "17:00":False, "18:00":False, "19:00":False, "20:00":False},
                      "Lane 5":{"12:00":False, "13:00":False, "14:00":False, "15:00":False, "16:00":False, "17:00":False, "18:00":False, "19:00":False, "20:00":False},
                      "Lane 6":{"12:00":False, "13:00":False, "14:00":False, "15:00":False, "16:00":False, "17:00":False, "18:00":False, "19:00":False, "20:00":False}},
            "Thursday":{"Lane 1":{"12:00":False, "13:00":False, "14:00":False, "15:00":False, "16:00":False, "17:00":False, "18:00":False, "19:00":False, "20:00":False},
                      "Lane 2":{"12:00":False, "13:00":False, "14:00":False, "15:00":False, "16:00":False, "17:00":False, "18:00":False, "19:00":False, "20:00":False},
                      "Lane 3":{"12:00":False, "13:00":False, "14:00":False, "15:00":False, "16:00":False, "17:00":False, "18:00":False, "19:00":False, "20:00":False},
                      "Lane 4":{"12:00":False, "13:00":False, "14:00":False, "15:00":False, "16:00":False, "17:00":False, "18:00":False, "19:00":False, "20:00":False},
                      "Lane 5":{"12:00":False, "13:00":False, "14:00":False, "15:00":False, "16:00":False, "17:00":False, "18:00":False, "19:00":False, "20:00":False},
                      "Lane 6":{"12:00":False, "13:00":False, "14:00":False, "15:00":False, "16:00":False, "17:00":False, "18:00":False, "19:00":False, "20:00":False}},
            "Friday":{"Lane 1":{"12:00":False, "13:00":False, "14:00":False, "15:00":False, "16:00":False, "17:00":False, "18:00":False, "19:00":False, "20:00":False},
                      "Lane 2":{"12:00":False, "13:00":False, "14:00":False, "15:00":False, "16:00":False, "17:00":False, "18:00":False, "19:00":False, "20:00":False},
                      "Lane 3":{"12:00":False, "13:00":False, "14:00":False, "15:00":False, "16:00":False, "17:00":False, "18:00":False, "19:00":False, "20:00":False},
                      "Lane 4":{"12:00":False, "13:00":False, "14:00":False, "15:00":False, "16:00":False, "17:00":False, "18:00":False, "19:00":False, "20:00":False},
                      "Lane 5":{"12:00":False, "13:00":False, "14:00":False, "15:00":False, "16:00":False, "17:00":False, "18:00":False, "19:00":False, "20:00":False},
                      "Lane 6":{"12:00":False, "13:00":False, "14:00":False, "15:00":False, "16:00":False, "17:00":False, "18:00":False, "19:00":False, "20:00":False}},
            "Saturday":{"Lane 1":{"12:00":False, "13:00":False, "14:00":False, "15:00":False, "16:00":False, "17:00":False, "18:00":False, "19:00":False, "20:00":False},
                      "Lane 2":{"12:00":False, "13:00":False, "14:00":False, "15:00":False, "16:00":False, "17:00":False, "18:00":False, "19:00":False, "20:00":False},
                      "Lane 3":{"12:00":False, "13:00":False, "14:00":False, "15:00":False, "16:00":False, "17:00":False, "18:00":False, "19:00":False, "20:00":False},
                      "Lane 4":{"12:00":False, "13:00":False, "14:00":False, "15:00":False, "16:00":False, "17:00":False, "18:00":False, "19:00":False, "20:00":False},
                      "Lane 5":{"12:00":False, "13:00":False, "14:00":False, "15:00":False, "16:00":False, "17:00":False, "18:00":False, "19:00":False, "20:00":False},
                      "Lane 6":{"12:00":False, "13:00":False, "14:00":False, "15:00":False, "16:00":False, "17:00":False, "18:00":False, "19:00":False, "20:00":False}}
}          





def booking(bookings):
    available = False
    while available == False:
        newbooking = input("Enter the day you would like to book for: ")
        lane = input("Which lane would you like to book? Enter 1 through 6. \n>> ")
        booktime = input("What time are you booking for? Enter any number between 1 and 8. \n>> ")
        try:
            int(lane)
            int(booktime)
            if int(lane) > 6 or int(booktime) > 8 or int(booktime) < 1:
                print("That's an invalid input! Please try inputting again.")
                booking(bookings)
            else:
                booktime = int(booktime) 
                
        except:
            print("That's an invalid input! Please try inputting again.")
            booking(bookings)
+ 12
        #print(bookings[newbooking.capitalize()])
        




            

booking(bookings)

