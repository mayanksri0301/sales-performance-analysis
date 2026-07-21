import pandas as pd
from pathlib import Path

# Project Directory
BASE_DIR = Path(__file__).resolve().parent.parent

# Load Cleaned Dataset
DATA_PATH = BASE_DIR / "data" / "cleaned_sales.csv"

df = pd.read_csv(DATA_PATH)

print("=" * 60)
print("BUSINESS ANALYSIS")
print("=" * 60)

# ---------------------------------
# Total Sales
# ---------------------------------
print("\n1. Total Sales")
print(f"₹ {df['Sales'].sum():,.2f}")

# ---------------------------------
# Total Profit
# ---------------------------------
print("\n2. Total Profit")
print(f"₹ {df['Profit'].sum():,.2f}")

# ---------------------------------
# Total Orders
# ---------------------------------
print("\n3. Total Orders")
print(df["Order.ID"].nunique())

# ---------------------------------
# Sales by Category
# ---------------------------------
print("\n4. Sales by Category")
print(df.groupby("Category")["Sales"].sum().sort_values(ascending=False))

# ---------------------------------
# Profit by Category
# ---------------------------------
print("\n5. Profit by Category")
print(df.groupby("Category")["Profit"].sum().sort_values(ascending=False))

# ---------------------------------
# Sales by Region
# ---------------------------------
print("\n6. Sales by Region")
print(df.groupby("Region")["Sales"].sum().sort_values(ascending=False))

# ---------------------------------
# Top 10 Products
# ---------------------------------
print("\n7. Top 10 Products")
print(df.groupby("Product.Name")["Sales"].sum().sort_values(ascending=False).head(10))

# ---------------------------------
# Top 10 Customers
# ---------------------------------
print("\n8. Top 10 Customers")
print(df.groupby("Customer.Name")["Sales"].sum().sort_values(ascending=False).head(10))

# ---------------------------------
# Average Discount
# ---------------------------------
print("\n9. Average Discount")
print(round(df["Discount"].mean(), 2))

# ---------------------------------
# Average Shipping Cost
# ---------------------------------
print("\n10. Average Shipping Cost")
print(round(df["Shipping.Cost"].mean(), 2))