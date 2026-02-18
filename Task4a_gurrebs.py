import pandas as pd
import matplotlib.pyplot as plt

#Displays the main menu and collects choice of menu item

def menu():

    flag = True

    while flag:
        print("###############################################")
        print("Welcome! Please choose an option from the list")
        print("1. Show total sales for a specific item") 
        print("2. Show sales for a specific item during one service")
        print("3. Show highest selling menu item during a certain time period")

        main_menu_choice = input("Please enter the number of your choice (1-3): ")

        try:
            int(main_menu_choice)
        except:
            print("Sorry, you did not enter a valid choice")
            flag = True
        else:
            if int(main_menu_choice) < 1 or int(main_menu_choice) > 3:
                print("Sorry, you did not enter a valid choice")
                flag = True
            else:
                return int(main_menu_choice)    

#Menu item selection form user and validates it
def get_product_choice():

    flag = True

    while flag:
        print("######################################################")
        print("Please choose a menu item form the list:")
        print("Please enter the number of the item (1-8)")
        print("1.  Nachos")
        print("2.  Soup")
        print("3.  Burger")
        print("4.  Brisket")
        print("5.  Ribs")
        print("6.  Corn")
        print("7.  Fries")
        print("8.  Salad")
        print("######################################################")

        menu_list = ["Nachos","Soup","Burger", "Brisket","Ribs","Corn", "Fries", "Salad"]

        item_choice = input("Please enter the number of your choice (1-8): ")

        try:
            int(item_choice)
        except:
            print("Sorry, you did not enter a valid choice")
            flag = True
        else:
            if int(item_choice) < 1 or int(item_choice) > 8:
                print("Sorry, you did not enter a valid choice")
                flag = True
            else:
                item_name = menu_list[int(item_choice)-1]
                return item_name

#Gets user input of start of date range
#Converts to a date to check data entry is in correct format and then returns it as a string
def get_start_date():
    
    flag = True
    
    while flag:
        start_date = input('Please enter start date for your time range (DD/MM/YYYY) : ')

        try:
           pd.to_datetime(start_date)
        except:
            print("Sorry, you did not enter a valid date")
            flag = True
        else:
            flag = False
    
    return start_date

#Gets user input of end of date range
#Converts to a date to check data entry is in correct format and then returns it as a string
def get_end_date():
    
    flag = True
    
    while flag:
        end_date = input('Please enter end date for your time range (DD/MM/YYYY) : ')

        try:
           pd.to_datetime(end_date)
        except:
            print("Sorry, you did not enter a valid date")
            flag = True
        else:
            flag = False
    
    return end_date


#imports data set and extracts data and returns data for a specific menu item within a user defined range
def get_selected_item(item, startdate, enddate):
    df1 = pd.read_csv("Task4a_data.csv") 
    df2 = df1.loc[df1['Menu Item'] == item]
    df3 = df2.loc[:,startdate:enddate]

    return df3

def get_service_time():
    flag = True
    while flag:
        print("######################################################")
        print("Please select a service time:")
        print("1. Lunch")
        print("2. Dinner")
        print("######################################################")
        service = input("Enter the number of your choice (1-2): ")
        try:
            int(service)
        except:
            print("Please enter a valid number (1-2)")
            flag = True
        else:
            if int(service) > 2 or int(service) < 1:
                print("Please enter a valid number (1-2) ")
                flag = True
            else:
                if service == "1":
                    Flag = False
                    service_choice = "Lunch"
                    return service_choice
                elif service == "2":
                    flag = False
                    service_choice = "Dinner"
                    return service_choice
                else:
                    flag = True


def select_from_service(item,service,startdate,enddate):
    df1 = pd.read_csv("Task4a_data.csv")
    df2 = df1.loc[df1['Menu Item'] == item]
    df3 = df2.loc[df1['Service'] == service]
    df4 = df3.loc[:,startdate:enddate]
    
    return df4


def get_highest_seller(startdate,enddate):
    highest_total = 0
    highest_item = ""
    df1 = pd.read_csv("Task4a_data.csv")
    menu_list = ["Nachos","Soup","Burger", "Brisket","Ribs","Corn", "Fries", "Salad"]
    for x in range(len(menu_list)):
        total = 0
        minidf = df1.loc[df1['Menu Item'] == menu_list[x]]
        menuitem = menu_list[x]
        minidf2 = minidf.loc[:,startdate:enddate]
        column_list = minidf2.columns
        for x in range(len(column_list)):
            if "2023" in column_list[x]:
                total = total + minidf[column_list[x]].sum()
            if total > highest_total:
                highest_total = total
                highest_item = menuitem
    print(f"The highest selling item during the time period {startdate} to {enddate} was {highest_item}.")
                

    return highest_total


def get_highest_average(startdate,enddate):
    highest_average = 0
    highest_item = ""
    highest_total = 0
    correctlen = 0
    df1 = pd.read_csv("Task4a_data.csv")
    menu_list = ["Nachos","Soup","Burger", "Brisket","Ribs","Corn", "Fries", "Salad"]
    for x in range(len(menu_list)):
        total = 0
        minidf = df1.loc[df1['Menu Item'] == menu_list[x]]
        menuitem = menu_list[x]
        minidf2 = minidf.loc[:,startdate:enddate]
        column_list = minidf2.columns
        for x in range(len(column_list)):
            if "2023" in column_list[x]:
                total = total + minidf[column_list[x]].sum()
            if total > highest_total:
                highest_total = total
                highest_item = menuitem
                correctlen = len(column_list)
        highest_average = highest_total/correctlen
        print(f"The item with the highest sales on average during the time period {startdate} to {enddate} was {highest_item}")
        return highest_average
    











main_menu = menu()
if main_menu == 1:

    item = get_product_choice()
    start_date = get_start_date()
    end_date = get_end_date()
 
    extracted_data = get_selected_item(item, start_date, end_date)
    
    print("Here is the sales data for {} between dates {} and {}:".format(item, start_date, end_date))
    extract_no_index = extracted_data.to_string(index=False)

    print(extract_no_index)

    #plt.bar(extracted_data[])
elif main_menu == 2:
    item = get_product_choice()
    service_choice = get_service_time()
    start_date = get_start_date()
    end_date = get_end_date()

    extracted_data = select_from_service(item,service_choice,start_date,end_date)
    print("Here is the sales data for the {} during {} between dates {} and {}:".format(item, service_choice, start_date, end_date))
    extract_no_index = extracted_data.to_string(index=False)

    print(extract_no_index)
elif main_menu == 3:
    start_date = get_start_date()
    end_date = get_end_date()

    highest_total = get_highest_seller(start_date,end_date)
    print(f"This item sold a total of {highest_total} units.")
    highest_average = get_highest_average(start_date,end_date)
    print(f"This item sold, on average, {highest_average} units.")

