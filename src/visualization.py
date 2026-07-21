import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# Project Directory
BASE_DIR = Path(__file__).resolve().parent.parent

# Load Cleaned Dataset
df = pd.read_csv(BASE_DIR / "data" / "cleaned_sales.csv")

# Images Folder
IMAGE_DIR = BASE_DIR / "images"
IMAGE_DIR.mkdir(exist_ok=True)

# -------------------------
# Sales by Category
# -------------------------
plt.figure(figsize=(6,5))
df.groupby("Category")["Sales"].sum().plot(kind="bar")
plt.title("Sales by Category")
plt.ylabel("Sales")
plt.tight_layout()
plt.savefig(IMAGE_DIR / "sales_by_category.png")
plt.close()

# -------------------------
# Profit by Category
# -------------------------
plt.figure(figsize=(6,5))
df.groupby("Category")["Profit"].sum().plot(kind="bar")
plt.title("Profit by Category")
plt.ylabel("Profit")
plt.tight_layout()
plt.savefig(IMAGE_DIR / "profit_by_category.png")
plt.close()

# -------------------------
# Sales by Region
# -------------------------
plt.figure(figsize=(10,5))
df.groupby("Region")["Sales"].sum().sort_values().plot(kind="barh")
plt.title("Sales by Region")
plt.tight_layout()
plt.savefig(IMAGE_DIR / "sales_by_region.png")
plt.close()

# -------------------------
# Monthly Sales Trend
# -------------------------
df["Order.Date"] = pd.to_datetime(df["Order.Date"])
monthly_sales = df.groupby(df["Order.Date"].dt.to_period("M"))["Sales"].sum()

plt.figure(figsize=(12,5))
monthly_sales.plot()
plt.title("Monthly Sales Trend")
plt.ylabel("Sales")
plt.tight_layout()
plt.savefig(IMAGE_DIR / "monthly_sales.png")
plt.close()

# -------------------------
# Discount Distribution
# -------------------------
plt.figure(figsize=(6,5))
plt.hist(df["Discount"], bins=20)
plt.title("Discount Distribution")
plt.tight_layout()
plt.savefig(IMAGE_DIR / "discount_distribution.png")
plt.close()

# -------------------------
# Shipping Cost Distribution
# -------------------------
plt.figure(figsize=(6,5))
plt.hist(df["Shipping.Cost"], bins=20)
plt.title("Shipping Cost Distribution")
plt.tight_layout()
plt.savefig(IMAGE_DIR / "shipping_cost_distribution.png")
plt.close()

print("=" * 60)
print("ALL VISUALIZATIONS CREATED SUCCESSFULLY")
print("=" * 60)