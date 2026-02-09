import pandas as pd
import matplotlib.pyplot as plt

def main_menu():
    flag = True

    while flag:

        print("#################################################")
        print("############## Snowy Animal Rescue ##############")
        print("#################################################")
        print("")
        print("########### Please select an option #############")
        print("### 1. Average Social Media Interaction Data")
        print("### 2. Most Interacted With Post Type")
        print("### 3. Interaction Data Based On Times")
        print("### 4. Interaction Bar Chart Based On Post Type")
        print("### 5. Interaction Bar Chart Based On Post Time")
        

        choice = input('Enter your number selction here: ')

        try:
            int(choice)
        except:
            print("Sorry, you did not enter a valid option")
            flag = True
        else:
            if int(choice) > 5 or int(choice) < 1:
                print("Sorry, you did not enter a valid option")
                flag = True
            else:
                print('Choice accepted!')
                flag = False

    return choice


def average_menu ():
    df = pd.read_csv("Task4a_data.csv")
    flag = True

    while flag:

        print("#################################################")
        print("############## Average Interaction ##############")
        print("#################################################")
        print("")
        print("########### Please select an option #############")
        print("### 1. Average number of Likes")   
        print("### 2. Average number of Shares") 
        print("### 3. Average number of Comments") 

        choice = input('Enter your number selction here: ')

        try:
            int(choice)
        except:
            print("Sorry, you did not enter a valid option")
            flag = True
        else:
            if int(choice) > 3:
                print("Sorry, you did not enter a valid option")
                flag = True  
            else:
                print("Choice accepted!")
                flag = False

    return choice 


def convert_avg_men_coice(avg_men_choice):
    
    if avg_men_choice == "1":
        avg_choice = "Likes"
    elif avg_men_choice == "2":
        avg_choice = "Shares"
    else:
        avg_choice = "Comments"  
    
    return avg_choice


def get_avg_data(avg_choice):
    
    df = pd.read_csv("Task4a_data.csv")
    extract = df.groupby(['Date'], as_index=False) [avg_choice].mean()
    extract_no_index = extract.to_string(index=False)
    print("Here is a line chart representing the interactions per day: ")
    plt.plot(extract['Date'],extract[avg_choice], marker="o", linestyle="-",color="blue")
    plt.title("Average interactions per day")
    plt.xlabel("Date")
    plt.ylabel(avg_choice)
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
    print("Alongside this, here is the average number of {} each day during the campaign:".format(avg_choice))
    return extract_no_index


def highest_interactions():
    highest_total = 0
    highest_type = ""
    df = pd.read_csv("Task4a_data.csv")
    post_types = pd.unique(df['Post Type'])
    for x in range(0, len(post_types)):
        typesdf = df[df['Post Type'] == post_types[x]]
        total_interactions = (sum(typesdf['Likes']) + sum(typesdf['Shares']) + sum(typesdf['Comments']))
        if total_interactions > highest_total:
            highest_total = total_interactions
            highest_type = post_types[x]
        else:
            continue
    print(f"The post with the most interactions was {highest_type}, with a total of {highest_total} interactions.")


def TOD_interactions():
    highest_total = 0
    highest_time = ""
    lowest_total = 100000
    lowest_time = ""
    flag = True
    df = pd.read_csv("Task4a_data.csv")
    timeslist = pd.unique(df['Time'])
    while flag == True:
        print("Select a time from the following to get an analysis of interactions during that timeframe. ")
        for x in range(len(timeslist)):
            print(f"{x+1}: {timeslist[x]}")
        timechoice = input("Select using the corresponding number: ")
        try:
            int(timechoice)
        except:
            print("Invalid input. Try again.")
            flag = True
        else:
            if int(timechoice) > 9 or int(timechoice) < 1:
                print("Invalid input. Try again.")
                flag = True
            else:
                print("Choice accepted! ")
                flag = False
                timechoice = timeslist[int(timechoice)-1]
            timedf = df[df['Time'] == timechoice]
            print(f"The sum of interactions during the timeframe {timechoice} is {sum(timedf['Likes'])+sum(timedf['Shares'])+sum(timedf['Comments'])} interactions.")
    for x in range(0,len(timeslist)):
        totalsdf = df[df['Time'] == timeslist[x]]
        total_interactions = (sum(totalsdf['Likes']) + sum(totalsdf['Shares']) + sum(totalsdf['Comments']))
        if total_interactions > highest_total:
            highest_total = total_interactions
            highest_time = timeslist[x]
        elif total_interactions < lowest_total:
            lowest_total = total_interactions
            lowest_time = timeslist[x]
        else:
            continue
    print(f"The timeframe where posts are most often interacted with is {highest_time}, with it garnering {highest_total} interactions.")
    print(f"The timeframe with the lowest interaction rate is {lowest_time}, with a total interaction count of {lowest_total}.\nThis is {highest_total-lowest_total} less than the highest timeframe.")       


def interaction_charter():
    flag = True
    while flag == True:
        df = pd.read_csv("Task4a_data.csv")
        likesdf = df[['Post Type','Likes']]
        sharesdf = df[['Post Type', 'Shares']]
        commentsdf = df[['Post Type', 'Comments']]
        print("Would you like a bar chart based on:\n1: Likes based on post type\n2: Shares based on post type\n3: Comments based on post type.")
        typechoice = input("Select your choice by entering the corresponding number: ")
        try:
            int(typechoice)
        except:
            print("Invalid input. Please try again.")
            flag = True
        else:
            if int(typechoice) > 3 or int(typechoice) < 1:
                print("Invalid input. Please try again.")
                flag = True
            else:
                print("Input accepted!")
                typechoice = int(typechoice)
                flag = False
    if typechoice == 1:
        plot_data = likesdf.groupby('Post Type')['Likes'].sum()
        ylabel = "Likes"
    elif typechoice == 2:
        plot_data = sharesdf.groupby('Post Type')['Shares'].sum()
        ylabel = "Shares"
    else:
        plot_data = commentsdf.groupby('Post Type')['Comments'].sum()
        ylabel = "Comments"
    plot_data.plot(kind='bar', color='blue')
    plt.title(f'{ylabel} by Post Type')
    plt.xlabel('Post Type')
    plt.ylabel(ylabel)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def TOD_interaction_charter():
    flag = True
    while flag == True:
        df = pd.read_csv("Task4a_data.csv")
        likesdf = df[['Time','Likes']]
        sharesdf = df[['Time', 'Shares']]
        commentsdf = df[['Time', 'Comments']]
        print("Would you like a bar chart based on:\n1: Likes based on time\n2: Shares based on time\n3: Comments based on time.")
        timechoice = input("Select your choice by entering the corresponding number: ")
        try:
            int(timechoice)
        except:
            print("Invalid input. Please try again.")
            flag = True
        else:
            if int(timechoice) > 3 or int(timechoice) < 1:
                print("Invalid input. Please try again.")
                flag = True
            else:
                print("Input accepted!")
                flag = False
                timechoice = int(timechoice)
    if timechoice == 1:
        plot_data = likesdf.groupby('Time')['Likes'].sum()
        ylabel = "Likes"
    elif timechoice == 2:
        plot_data = sharesdf.groupby('Time')['Shares'].sum()
        ylabel = "Shares"
    else:
        plot_data = commentsdf.groupby('Time')['Comments'].sum()
        ylabel = "Comments"
    plot_data.plot(kind='bar', color='blue')
    plt.title(f'{ylabel} by Post Time')
    plt.xlabel('Post Time')
    plt.ylabel(ylabel)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()




main_menu_choice = main_menu()
if main_menu_choice == "1":
    avg_men_choice = average_menu()
    avg_choice = convert_avg_men_coice(avg_men_choice)
    print(get_avg_data(avg_choice))
elif main_menu_choice == "2":
    highest_interactions()
elif main_menu_choice == "3":
    TOD_interactions()
elif main_menu_choice == "4":
    interaction_charter()
elif main_menu_choice == "5":
    TOD_interaction_charter()


    


