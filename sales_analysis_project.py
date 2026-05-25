from unicodedata import category

import pandas as pd
import matplotlib.pyplot as plt
#===========
# DATA LOADING
#============
df = pd.read_csv(r"Sample - Superstore.csv" , encoding="latin1")
#===============
# DATA EXPLORATION
#===============
print(df.head())
print(df.tail())
print(df.info())
print(df.describe())

# CATEGORY SALES ANALYSIS

category_sales = df.groupby("Category")["Sales"].sum()
print("\nTotal sales by category: ")
print(category_sales)

best_category = category_sales.idxmax()
print("\nThe best selling category:")
print(best_category)

plt.figure(figsize=(5,5))
category_sales.plot(kind="bar")
plt.title("Total Sales by Category")
plt.xlabel("Category")
plt.ylabel("Sales")
plt.show()

# PROFIT ANALYSIS

category_profit = df.groupby("Category")["Sales"].sum()
print("\nTotal Profit by Category")
print(category_profit)

plt.figure(figsize=(8,5))
category_profit.plot(kind="bar")
plt.title("Total Profit by Category")
plt.xlabel("Category")
plt.ylabel("Profit")
plt.show()

# TOP PRODUCTS ANALYSIS

product_sales = df.groupby("Product Name")["Sales"].sum()
top_10_products = product_sales.sort_values(ascending=False).head(10)
print("\nTop 10 Products:")
print(top_10_products)

# REGION SALES ANALYSIS

region_sales = df.groupby("Region")["Sales"].sum()
print("\nTotal Sales BY Region:")
print(region_sales)

plt.figure(figsize=(8,5))
region_sales.plot(kind="bar")
plt.title("Total Sales by Region")
plt.xlabel("Region")
plt.ylabel("Sales")
plt.show()


