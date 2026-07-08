import pandas as pd
df = pd.read_csv("data/Superstore.csv", encoding="latin1")

print(df.head())

print(df.info())

print(df.isnull().sum())
# Remove duplicates
df.drop_duplicates(inplace=True)

# Convert Order Date to datetime
df['Order Date'] = pd.to_datetime(df['Order Date'])

# Create new columns
df['Year'] = df['Order Date'].dt.year
df['Month'] = df['Order Date'].dt.month
df['Month_Name'] = df['Order Date'].dt.month_name()

# Create Profit Margin column
df['Profit Margin'] = df['Profit'] / df['Sales']

print("Data cleaning completed ✅")
print(df.head())
total_sales = df['Sales'].sum()
total_profit = df['Profit'].sum()
total_orders = df['Order ID'].nunique()
profit_margin = total_profit / total_sales

print("\n===== KPI SUMMARY =====")
print("Total Sales:", round(total_sales, 2))
print("Total Profit:", round(total_profit, 2))
print("Total Orders:", total_orders)
print("Overall Profit Margin:", round(profit_margin * 100, 2), "%")
print("\n===== CATEGORY ANALYSIS =====")
category_sales = df.groupby('Category')['Sales'].sum().sort_values(ascending=False)
category_profit = df.groupby('Category')['Profit'].sum().sort_values(ascending=False)

print("\nSales by Category:")
print(category_sales)

print("\nProfit by Category:")
print(category_profit)
print("\n===== TOP 10 PRODUCTS BY SALES =====")
top_products = df.groupby('Product Name')['Sales'].sum().sort_values(ascending=False).head(10)
print(top_products)
print("\n===== REGION PERFORMANCE =====")
region_sales = df.groupby('Region')['Sales'].sum().sort_values(ascending=False)
region_profit = df.groupby('Region')['Profit'].sum().sort_values(ascending=False)

print("\nSales by Region:")
print(region_sales)

print("\nProfit by Region:")
print(region_profit)
print("\n===== DISCOUNT VS PROFIT CORRELATION =====")
correlation = df[['Discount','Profit']].corr()
print(correlation)
import matplotlib.pyplot as plt

category_sales.plot(kind='bar')
plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Total Sales")
plt.show()

profit_by_category = df.groupby("Category")["Profit"].sum()

profit_by_category.plot(kind="bar")
plt.title("Profit by Category")
plt.xlabel("Category")
plt.ylabel("Total Profit")
plt.show()

sales_by_region = df.groupby("Region")["Sales"].sum()

sales_by_region.plot(kind="bar")
plt.title("Sales by Region")
plt.xlabel("Region")
plt.ylabel("Total Sales")
plt.show()

plt.scatter(df["Discount"], df["Profit"])
plt.title("Discount vs Profit")
plt.xlabel("Discount")
plt.ylabel("Profit")
plt.show()

df["Order Date"] = pd.to_datetime(df["Order Date"])

monthly_sales = df.groupby(df["Order Date"].dt.to_period("M"))["Sales"].sum()

monthly_sales.plot()
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.show()
