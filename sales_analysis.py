import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load Dataset
df = pd.read_csv("SampleSuperstore.csv")

print("First 5 Rows")
print(df.head())

print("\nDataset Info")
print(df.info())

print("\nMissing Values")
print(df.isnull().sum())

print("\nSummary Statistics")
print(df.describe())

# Category Wise Sales
plt.figure(figsize=(8,5))
sns.barplot(x="Category", y="Sales", data=df)
plt.title("Category Wise Sales")
plt.savefig("category_sales.png")
plt.show()

# Sales Distribution
plt.figure(figsize=(8,5))
sns.histplot(df["Sales"], bins=30, kde=True)
plt.title("Sales Distribution")
plt.savefig("sales_distribution.png")
plt.show()

# Profit by Category
plt.figure(figsize=(8,5))
sns.barplot(x="Category", y="Profit", data=df)
plt.title("Profit by Category")
plt.savefig("profit_category.png")
plt.show()

# Correlation Heatmap
plt.figure(figsize=(6,4))
sns.heatmap(
    df[["Sales","Profit","Quantity","Discount"]].corr(),
    annot=True,
    cmap="coolwarm"
)
plt.title("Correlation Matrix")
plt.savefig("correlation_heatmap.png")
plt.show()

print("\nProject Completed Successfully!")