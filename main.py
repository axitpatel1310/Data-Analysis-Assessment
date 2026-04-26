import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_excel("Sales Data PDA 4052.xlsx")
print("Columns:", df.columns)
print(df.head())
print(df.shape)

# Check data types
print(df.info())

# Summary statistics
print(df.describe())

# Check missing values
print(df.isnull().sum())

# Example handling
df = df.dropna()
print(df.isnull().sum())

# Convert date column
df['date'] = pd.to_datetime(df['date'], errors='coerce')

# Standardise text columns
df['sales_person'] = df['sales_person'].str.strip().str.title()
df['priority'] = df['priority'].str.strip().str.title()

# Remove non-meaningful category
df = df[df['priority'] != 'NotSpecified']

# Encode priority
priority_map = {
    'Low': 1,
    'Medium': 2,
    'High': 3,
    'Critical': 4
}

df['priority_encoded'] = df['priority'].map(priority_map)

# IQR method
Q1 = df['value'].quantile(0.25)
Q3 = df['value'].quantile(0.75)
IQR = Q3 - Q1

# Filter outliers
df = df[(df['value'] >= Q1 - 1.5 * IQR) & (df['value'] <= Q3 + 1.5 * IQR)]

# Aggregate sales per salesperson
sales_person = df.groupby('sales_person')['value'].sum().sort_values(ascending=False)

# Plot
sales_person.plot(kind='bar')
plt.title("Total Sales by Salesperson")
plt.xlabel("Salesperson")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Aggregate sales over time
sales_time = df.groupby('date')['value'].sum()

# Plot
sales_time.plot(kind='line')
plt.title("Total Sales Over Time")
plt.xlabel("Date")
plt.ylabel("Total Sales")
plt.tight_layout()
plt.show()

# Scatter plot
sns.scatterplot(data=df, x='priority', y='value')
plt.title("Priority vs Sales Value")
plt.xlabel("Priority")
plt.ylabel("Sales")
plt.tight_layout()
plt.show()

# Calculate correlation
correlation = df['priority_encoded'].corr(df['value'])
print("Correlation between priority and sales:", correlation)
