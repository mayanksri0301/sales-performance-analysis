import pandas as pd
from pathlib import Path

# Project Directory
BASE_DIR = Path(__file__).resolve().parent.parent

# Dataset Path
DATA_PATH = BASE_DIR / "data" / "Sample - Superstore.csv"

# Load Dataset
df = pd.read_csv(DATA_PATH, encoding="latin1")

print("=" * 60)
print("DATA CLEANING")
print("=" * 60)

# -----------------------------
# Remove unwanted encoded column
# -----------------------------
if "è®°å½\x95æ\x95°" in df.columns:
    df.drop(columns=["è®°å½\x95æ\x95°"], inplace=True)

# -----------------------------
# Convert Date Columns
# -----------------------------
df["Order.Date"] = pd.to_datetime(df["Order.Date"])
df["Ship.Date"] = pd.to_datetime(df["Ship.Date"])

# -----------------------------
# Remove Duplicate Rows
# -----------------------------
duplicates = df.duplicated().sum()
print(f"\nDuplicate Rows: {duplicates}")

df.drop_duplicates(inplace=True)

# -----------------------------
# Missing Values
# -----------------------------
print("\nMissing Values:")
print(df.isnull().sum())

print("\nDataset Shape After Cleaning:")
print(df.shape)

print("\nData Types:")
print(df.dtypes)

# -----------------------------
# Save Clean Dataset
# -----------------------------
OUTPUT_PATH = BASE_DIR / "data" / "cleaned_sales.csv"

df.to_csv(OUTPUT_PATH, index=False)

print("\n✅ Cleaned dataset saved as:")
print(OUTPUT_PATH)