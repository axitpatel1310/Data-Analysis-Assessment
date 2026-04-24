import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style="whitegrid")

# ==============================
# 1. LOAD DATA
# ==============================
df = pd.read_csv("Sales Data PDA 4052.csv")

print("Preview of dataset:")
print(df.head())

# ==============================
# 2. DATA INSPECTION
# ==============================
print("\nDataset Info:")
print(df.info())

print("\nDescriptive Statistics:")
print(df.describe())

print("\nColumn Names:")
print(df.columns)

# ==============================
# 3. BEFORE PREPROCESSING CHECK
# ==============================
print("\nMissing values BEFORE cleaning:")
print(df.isnull().sum())

print("\nDuplicate rows BEFORE cleaning:")
print(df.duplicated().sum())

# ==============================
# 4. DATA PREPROCESSING
# ==============================

# Handle missing values
df = df.dropna()

# Remove duplicates
df = df.drop_duplicates()

# Fix data types
df["Total Sales"] = pd.to_numeric(df["Total Sales"], errors="coerce")

# Clean text columns
df["Sales Person"] = df["Sales Person"].str.strip().str.title()
df["Priority"] = df["Priority"].str.strip().str.title()

# ==============================
# 5. AFTER PREPROCESSING CHECK
# ==============================
print("\nMissing values AFTER cleaning:")
print(df.isnull().sum())

print("\nDuplicate rows AFTER cleaning:")
print(df.duplicated().sum())

print("\nUpdated Data Types:")
print(df.dtypes)

# ==============================
# 6. BASIC STATISTICAL ANALYSIS
# ==============================
print("\nKey Statistics for Total Sales:")
print("Mean:", df["Total Sales"].mean())
print("Median:", df["Total Sales"].median())
print("Standard Deviation:", df["Total Sales"].std())

# ==============================
# 7. PRIORITY CHECK
# ==============================
print("\nUnique Priority Values:")
print(df["Priority"].unique())

# ==============================
# 8. OUTLIER DETECTION
# ==============================
Q1 = df["Total Sales"].quantile(0.25)
Q3 = df["Total Sales"].quantile(0.75)
IQR = Q3 - Q1

lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR

outliers = df[(df["Total Sales"] < lower) | (df["Total Sales"] > upper)]
print("\nOutliers detected:")
print(outliers)

# OPTIONAL: Remove outliers (uncomment if needed)
# df = df[(df["Total Sales"] >= lower) & (df["Total Sales"] <= upper)]

# ==============================
# 9. EDA - SALES BY SALESPERSON
# ==============================
sales_by_person = df.groupby("Sales Person")["Total Sales"].sum().sort_values(ascending=False)

print("\nSales by Salesperson:")
print(sales_by_person)

plt.figure(figsize=(10,5))
sales_by_person.plot(kind="bar")
plt.title("Total Sales by Salesperson")
plt.xlabel("Sales Person")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# ==============================
# 10. DISTRIBUTION ANALYSIS
# ==============================
plt.figure(figsize=(8,5))
sns.histplot(df["Total Sales"], bins=20, kde=True)
plt.title("Distribution of Total Sales")
plt.show()

# ==============================
# 11. OUTLIER VISUALISATION
# ==============================
plt.figure(figsize=(8,5))
sns.boxplot(x=df["Total Sales"])
plt.title("Boxplot of Total Sales")
plt.show()

# ==============================
# 12. PRIORITY VS SALES
# ==============================
plt.figure(figsize=(8,5))
sns.boxplot(x="Priority", y="Total Sales", data=df, order=["Low", "Medium", "High"])
plt.title("Sales Distribution by Priority")
plt.show()

# ==============================
# 13. CORRELATION ANALYSIS
# ==============================
priority_map = {"Low": 1, "Medium": 2, "High": 3}
df["Priority_Num"] = df["Priority"].map(priority_map)

print("\nEncoded Priority Values:")
print(df[["Priority", "Priority_Num"]].head())

corr = df[["Priority_Num", "Total Sales"]].corr()

print("\nCorrelation Matrix:")
print(corr)

plt.figure(figsize=(6,4))
sns.heatmap(corr, annot=True)
plt.title("Correlation Heatmap")
plt.show()

# ==============================
# 14. FINAL VERIFICATION
# ==============================
print("\nFinal Dataset Check:")
print(df.info())
print(df.isnull().sum())