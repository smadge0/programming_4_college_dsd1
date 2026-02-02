import pandas as pd
import matplotlib as mpl
import random as rand

df = pd.read_csv("pixelvault game sales.csv")
def simpleinfo(df):
    print(df.head(5))
    print(df.tail(5))
    print(df.describe())
    print(df.info())

def nullcheck(df):
    columns = df.columns
    for x in range(len(columns)):
        if df[columns[x]].isnull().sum() > 0:
            print(f'Column "{columns[x]}" has {df[columns[x]].isnull().sum()} null values.')

def categorysales(df):
    valid = False
    categories = pd.unique(df['category'])
    while valid == False:
        print("Choose a category to check the sales of: ")
        print(">>> 1. RPG ")
        print(">>> 2. Puzzle ")
        print(">>> 3. Shooter ")
        print(">>> 4. Action ")
        print(">>> 5. Simulation ")
        print(">>> 6. Racing ")
        print(">>> 7. Strategy ")
        choice = input(">>> ")
        try:
            choice == int(choice)
        except:
            print("Please select a valid number from the list.")
            Valid = False
        else:
            if int(choice) > 7:
                print("Please select a valid number from the list.")
                valid = False
                continue
            else:
                minidf = df[df['category'] == categories[int(choice)-1]]
                print(f"you sold this many: {minidf['quantity'].sum()}")


#print(nullcheck(df))
#print(df.duplicated())
#simpleinfo(df)
categorysales(df)


