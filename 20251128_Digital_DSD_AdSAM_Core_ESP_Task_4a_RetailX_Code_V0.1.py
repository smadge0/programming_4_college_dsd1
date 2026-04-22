import pandas as pd
import matplotlib.pyplot as plt

#Outputs the main menu and checks the user input
def main_menu():
    flag = True

    while flag:

        print("-"*66)
        print("---------- RetailX Sales Analysis Module ------------- ")
        print("-"*66)
        print("")
        print("--------------------- Main Menu --------------------- ")
        print("1. Total sales by product")
        print("2. Total sales by category")
        print("3. Gross income and total profit by product")

        choice = input('Enter your number selection here: ')

        if choice.isdigit():
            flag = False
        else:
            flag = True

    return int(choice)

#Generates submenu of available product codes and allows user to select a product to view
def get_product_id ():

    df = pd.read_csv("Task4a_RetailX_data.csv")

    product_codes = df["Product ID"].unique().tolist()

    flag = True

    while flag:

        print("-"*66)
        print("---------- RetailX Sales Analysis Module ------------- ")
        print("-"*66)
        print("")
        print("--------------------- Main Menu --------------------- ")
        print("Select a product code:")
        for i in range(len(product_codes)):
            print(i+1, " ", product_codes[i])

        selection = input('Enter your number selection here: ')

        if selection.isdigit():
            selection = int(selection)
            flag = False
        else:
            flag = True

        
        product_ID = product_codes[selection -1]
   
    print("You have selected product id:",product_ID)
    return product_ID

#gets and converts user input from string to date format
def get_date(start_end):
    
    flag = True
    
    while flag:
        date = input('Please enter {} date for your date range (DD/MM/YYYY) : '.format(start_end))

        try:
           pd.to_datetime(date, format="%d/%m/%Y")
        except:
            print("Sorry, you did not enter a valid date")
            flag = True
        else:
            flag = False
    
    return date

#extracts data based on product ID within a user specified date range.
def get_data_by_ID_and_date(product_id, start_date, end_date):
    all_data = pd.read_csv("Task4a_RetailX_data.csv")
    product_data = all_data.loc[all_data["Product ID"] == product_id].copy()

    product_data["Date"]= pd.to_datetime(product_data["Date"], format="%d/%m/%Y", errors="raise")
    
    date_range = (product_data["Date"] >= pd.to_datetime(start_date, format="%d/%m/%Y")) & \
                  (product_data["Date"] <= pd.to_datetime(end_date,format="%d/%m/%Y" ))
    
    extracted_data = product_data.loc[date_range]



    return extracted_data

#generates a total of the number of items sold for the extracted data
def calculate_total_sale (date_ID, product_id, start_date, end_date):
    total_sales = date_ID["Qty Sold"].sum()
    print('The total number of sales for product {}, between {} and {} was: {}'.format(product_id, start_date, end_date, total_sales))



def get_category():
    df = pd.read_csv("Task4a_RetailX_data.csv")
    categories = pd.unique(df["Category"])
    print(categories)
    flag = True
    while flag:
            print("-"*66)
            print("---------- RetailX Sales Analysis Module ------------- ")
            print("-"*66)
            print("")
            print("--------------------- Main Menu --------------------- ")
            print("Select a product code:")
            for i in range(len(categories)):
                print(i+1, " ", categories[i])

            selection = input('Enter your number selection here: ')

            if selection.isdigit():
                selection = int(selection)
                if selection > len(categories):
                    flag = True
                else:
                    flag = False
            else:
                flag = True

        
            category = categories[selection -1]
   
    print("You have selected category:",category)
    return category



def calculate_category_sales(start_date,end_date,category):
    df = pd.read_csv('Task4a_RetailX_data.csv')
    categorydf = df[df['Category'] == category]

    categorydf["Date"]= pd.to_datetime(categorydf["Date"], format="%d/%m/%Y", errors="raise").copy()

    date_range = (categorydf["Date"] >= pd.to_datetime(start_date, format="%d/%m/%Y")) & \
                  (categorydf["Date"] <= pd.to_datetime(end_date,format="%d/%m/%Y" ))
    dateddf = categorydf.loc[date_range]


    choice = input("Would you like the total sales data for your chosen category or the sales data from your selected time frame?\n1. Total\n2. Time frame\n>> ")
    if choice == "1":
        print(f"The total number of sales in {category} was {sum(categorydf["Qty Sold"])}")
    elif choice == "2":
        print(f"The total number of sales between for {category} between {start_date} and {end_date} was {sum(dateddf['Qty Sold'])} ")
    else:
        print("invalid choice slime")
        #i forgot to make a while loop and i don't wanna go back and move everything
        calculate_category_sales(start_date,end_date,category)

def profit_calculator(product_id):
    df = pd.read_csv("Task4a_RetailX_data.csv")
    product_df = df[df['Product ID'] == product_id]
    cost = pd.unique(product_df['Cost Price'])
    earning = pd.unique(product_df['Sales Price'])
    money_spent = cost[0] * sum(product_df['Qty Sold'])
    money_earnt = earning[0] * sum(product_df['Qty Sold'])
    total_profit = money_earnt - money_spent
    print(f"The gross earnings from the product with the ID of {product_id} was £{round(money_earnt, 2)}.\nAfter taking away the cost of the sales, the total overall profit was £{round(total_profit, 2)}")
    plt.bar(['Gross income','Total profit'],[money_earnt,total_profit],width=0.6,align="center")
    plt.show()

    
    
    


main_menu_choice = main_menu()

if main_menu_choice == 1:
    product_id = get_product_id()
    start_date = get_date("start")
    end_date = get_date("end")
    date_ID = get_data_by_ID_and_date(product_id, start_date, end_date)
    calculate_total_sale (date_ID, product_id, start_date, end_date)
elif main_menu_choice == 2:
    category = get_category()
    start_date = get_date("start")
    end_date = get_date("end")
    calculate_category_sales(start_date,end_date,category)
elif main_menu_choice == 3:
    product_id = get_product_id()
    profit_calculator(product_id)
    

else:
    print("yo slime thats not a valid choice. pick between 1 and 3 gang.")




