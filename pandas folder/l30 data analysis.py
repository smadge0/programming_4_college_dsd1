import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("amazon_sales_dataset.csv")

def task1(df):
    print(df.columns)

def task2(df):
    print(df['quantity_sold'].sum())
    print(df['total_revenue'].mean())

def task3(df):
    categorysalesdf = df[['product_category','quantity_sold']]
    plot_data = categorysalesdf.groupby('product_category')['quantity_sold'].sum()
    plot_data.plot(kind='bar',color='red',bottom=24000)
    plt.title(f'Total Quantity Sold by Product Category')
    plt.xlabel('Product Category')
    plt.ylabel('Quantity Sold')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.grid()
    plt.show()


task3(df)

    