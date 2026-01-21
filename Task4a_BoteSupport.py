import pandas as pd
import csv
import matplotlib.pyplot as plt

# Outputs the initial menu and validates the input
def main_menu():
    flag = True

    while flag:

        print("####################################################")
        print("############# Botes Parcels CRM System #############")
        print("####################################################")
        print("")
        print("########### Please select an option ################")
        print("### 1. Total issues by type")
        print("### 2. Time taken to resolve issues by type")
        print("### 3. Resolution of issues by region")


        choice = input('Enter your number selection here: ')

        try:
            int(choice)
        except:
            print("Sorry, you did not enter a valid option")
            flag = True
        else:
            choice = int(choice)
            if choice <= 3:
                print('Choice accepted!')
                flag = False
            else:
                print("Sorry, you did not enter a valid option")
                flag = True

    return choice

  # Submenu for totals, provides type and range check validation for the input and returns issue type as a string
def total_menu():
    flag = True

    while flag:

        print("####################################################")
        print("############## Total issues by type ################")
        print("####################################################")
        print("")
        print("########## Please select an issue type ##########")
        print("### 1. Customer Account Issue")   
        print("### 2. Delivery Issue") 
        print("### 3. Collection Issue")  
        print("### 4. Service Complaint")

        choice = input('Enter your number selection here: ')

        try:
            int(choice)
        except:
            print("Sorry, you did not enter a valid option")
            flag = True
        else:
            choice = int(choice)
            if choice <= 4:
                print('Choice accepted!')
                flag = False
            else:
                print("Sorry, you did not enter a valid option")
                flag = True

    issueTypeList = ["Customer Account Issue", "Delivery Issue", "Collection Issue", "Service Complaint"]
    

    issueType = issueTypeList[choice-1]
  
    return issueType     

# Creates a new dataframe then counts the number of occurences of the requested issue type

def get_total_data(total_menu_choice):
    
    issues = pd.read_csv("Task4a_data.csv")
    
    total = issues['Issue Type'].value_counts()[total_menu_choice]

    msg = "The total number of issues logged as a {} was: {}".format(total_menu_choice, total)
    return msg


def issue_time_calc():

    issues = pd.read_csv("Task4a_data.csv")
    timePerIssue = {}
    for issue in pd.unique(issues['Issue Type']):
        small_df = issues[issues['Issue Type'] == issue]
        
        issueTime = sum(small_df['Days To Resolve'])/len(small_df['Days To Resolve'])
    print(issueTime)
    


    

def region_menu():
    flag = True

    while flag:

        print("####################################################")
        print("############## Issues and solutions by region ################")
        print("####################################################")
        print("")
        print("########## Please select a region ##########")
        print("### 1. South West")   
        print("### 2. West Midlands") 
        print("### 3. London")  
        print("### 4. North Wales")
        print("### 5. South East")   
        print("### 6. East of England") 
        print("### 7. North East")  
        print("### 8. East Midlands")
        print("### 9. Scotland")   
        print("### 10. Yorkshire and The Humber") 
        print("### 11. South Wales")  
        print("### 12. North West")
        print("### 13. Northern Ireland")
        choice = input('Enter your number selection here: ')

        try:
            int(choice)
        except:
            print("Sorry, you did not enter a valid option")
            flag = True
        else:
            choice = int(choice)
            if choice <= 13:
                print('Choice accepted!')
                flag = False
            else:
                print("Sorry, you did not enter a valid option")
                flag = True
        
        regionList = ['South West', 'West Midlands', 'London', 'North Wales', 'South East',
                      'East of England', 'North East', 'East Midlands', 'Scotland',
                      'Yorkshire and The Humber', 'South Wales', 'North West', 'Northern Ireland']

        region = regionList[choice-1]
  
        return region
    
def get_region_solutions(region_menu_choice):
    print("balls")



main_menu_choice = main_menu()
if main_menu_choice ==  1:
    total_menu_choice = total_menu()
    print(get_total_data(total_menu_choice))
elif main_menu_choice == 2:
    print(issue_time_calc())
elif main_menu_choice == 3:
    region_menu_choice = region_menu()



