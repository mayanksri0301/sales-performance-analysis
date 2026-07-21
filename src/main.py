import pandas as pd
from pathlib import Path

# Project Directory
BASE_DIR = Path(__file__).resolve().parent.parent

# Dataset Path
DATA_PATH = BASE_DIR / "data" / "Sample - Superstore.csv"

print("=" * 60)
print("SALES PERFORMANCE ANALYSIS")
print("=" * 60)

print("\nLoading file:")
print(DATA_PATH)

# Load Dataset
df = pd.read_csv(DATA_PATH, encoding="latin1")

print("\n✅ Dataset Loaded Successfully!")

print(f"\nRows    : {df.shape[0]}")
print(f"Columns : {df.shape[1]}")

print("\nColumn Names:")
print(df.columns.tolist())

print("\nFirst 5 Rows:")
print(df.head())