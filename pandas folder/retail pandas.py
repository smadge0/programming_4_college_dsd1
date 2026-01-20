import pandas as pd
import matplotlib.pyplot as plt

salesdf = pd.read_csv("retail_sales_1M_dataset.csv")
#print(salesdf.head(5))
total_revenue = round(salesdf['price'].sum(), 2)
productsales = salesdf['product'].value_counts()
productprices = pd.unique(salesdf['price'])
uniqueproducts = pd.unique(salesdf['product'])
uniquecategories = pd.unique(salesdf['category'])
#print(f"Total sales: £{total_revenue}")
#print(products)
#print(productprices, uniqueproducts)

print(productsales)

for item in uniqueproducts:
    item_sales = salesdf[salesdf['product'] == item]
    item_revenue = round(item_sales['price'].sum(), 2)
    item_count = item_sales['product'].count()
    print(f"{item}: £{item_revenue} from {item_count} sales")

for item in uniquecategories:
    category_sales = salesdf[salesdf['category'] == item]
    category_revenue = round(category_sales['price'].sum(), 2)
    category_count = category_sales['product'].count()
    print(f"{item}: £{category_revenue} from {category_count} sales")

print(item_sales.sort_values(by = item_revenue, ascending = False).head(10))