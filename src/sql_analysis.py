import sqlite3
import pandas as pd
from pathlib import Path

# Project Directory
BASE_DIR = Path(__file__).resolve().parent.parent

# Load Cleaned Dataset
df = pd.read_csv(BASE_DIR / "data" / "cleaned_sales.csv")

# Create SQLite Database
conn = sqlite3.connect(BASE_DIR / "sales.db")

# Store Dataset
df.to_sql("sales", conn, if_exists="replace", index=False)

print("=" * 60)
print("SQL ANALYSIS")
print("=" * 60)

queries = {

"1. Total Sales": """
SELECT ROUND(SUM(Sales),2) AS Total_Sales
FROM sales;
""",

"2. Total Profit": """
SELECT ROUND(SUM(Profit),2) AS Total_Profit
FROM sales;
""",

"3. Sales by Category": """
SELECT Category,
ROUND(SUM(Sales),2) AS Sales
FROM sales
GROUP BY Category
ORDER BY Sales DESC;
""",

"4. Profit by Category": """
SELECT Category,
ROUND(SUM(Profit),2) AS Profit
FROM sales
GROUP BY Category
ORDER BY Profit DESC;
""",

"5. Sales by Region": """
SELECT Region,
ROUND(SUM(Sales),2) AS Sales
FROM sales
GROUP BY Region
ORDER BY Sales DESC;
""",

"6. Top 10 Customers": """
SELECT Customer_Name,
ROUND(SUM(Sales),2) AS Sales
FROM (
SELECT
`Customer.Name` AS Customer_Name,
Sales
FROM sales
)
GROUP BY Customer_Name
ORDER BY Sales DESC
LIMIT 10;
""",

"7. Top 10 Products": """
SELECT Product_Name,
ROUND(SUM(Sales),2) AS Sales
FROM (
SELECT
`Product.Name` AS Product_Name,
Sales
FROM sales
)
GROUP BY Product_Name
ORDER BY Sales DESC
LIMIT 10;
""",

"8. Average Discount": """
SELECT ROUND(AVG(Discount),2) AS Avg_Discount
FROM sales;
""",

"9. Average Shipping Cost": """
SELECT ROUND(AVG(`Shipping.Cost`),2) AS Avg_Shipping_Cost
FROM sales;
"""

}

for title, query in queries.items():

    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)

    result = pd.read_sql(query, conn)
    print(result)

conn.close()

print("\n✅ SQL Analysis Completed Successfully!")