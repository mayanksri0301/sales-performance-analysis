import pandas as pd
from pathlib import Path

# Project Directory
BASE_DIR = Path(__file__).resolve().parent.parent

# Dataset Path
DATA_PATH = BASE_DIR / "data" / "Sample - Superstore.csv"

# Load Dataset
df = pd.read_csv(DATA_PATH, encoding="latin1")

print("=" * 60)
print("DATASET INFORMATION")
print("=" * 60)

# Shape
print("\nShape of Dataset:")
print(df.shape)

# Column Names
print("\nColumn Names:")
print(df.columns.tolist())

# Data Types
print("\nData Types:")
print(df.dtypes)

# Missing Values
print("\nMissing Values:")
print(df.isnull().sum())

# Duplicate Rows
print("\nDuplicate Rows:")
print(df.duplicated().sum())

# Summary Statistics
print("\nSummary Statistics:")
print(df.describe(include="all"))