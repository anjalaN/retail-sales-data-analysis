import pandas as pd
import matplotlib.pyplot as plt

# Define the path to our excel file
file_path = "data/raw/sample_-_superstore.xls"
# Load the excel file into a Dataframe
df = pd.read_excel(file_path)
#Display the first 5 rows
print(df.head())
# Display the dataset dimension
print("\nDataset shape:", df.shape)
# Display all column names
print("\nColumn names:", df.columns.to_list())
# Display dataset information
df.info()
# Check missing values
print("\nMissing values per column:")
print(df.isnull().sum())
# Ccheck duplicate rows
print("\nNumber of dublicate rows:", df.duplicated().sum())
# Display descriptive statistics
print("\nDescriptive statistics:")
print(df.describe())
# Select numerical columns
numeric_columns = ["Sales", "Quantity", "Discount", "Profit"]
# Display descriptive satistics for selected columns
print(df[numeric_columns].describe())
# Analyse average profit by discount
discount_analysis = df.groupby("Discount")["Profit"].mean()
print("\nAverage profit by discount:")
print(discount_analysis)

# Calculate average profit by discount
discount_analysis = df.groupby("Discount")["Profit"].mean()


#Create a bar chart
discount_analysis.plot(kind="bar", figsize=(10, 5))

# Add chart title and labels
plt.title("Average Profit by Discount")
plt.xlabel("Discount")
plt.ylabel("Average Profit")
plt.axhline(y=0, color="red", linestyle="--")
# Calculate total sales and profit by category
category_analysis = df.groupby("Category")[["Sales", "Profit"]].sum()

print("\nSales and Profit by Category")
print(category_analysis)

# Calculate total sales and profit by category
category_analysis = df.groupby("Category")[["Sales", "Profit"]].sum()

# Display the results
print("\nSales and Profit by Category:")
print(category_analysis)

# Calculate profit margin by category
category_analysis["Profit Margin (%)"] = (
    category_analysis["Profit"] / category_analysis["Sales"]
) * 100

# Display the results
print("\nCategory Profit Margin:")
print(category_analysis)

# Plot profit margin by category
category_analysis["Profit Margin (%)"].plot(
    kind="bar",
    figsize=(8, 5)
)

# Add chart title and labels
plt.title("Profit Margin by Category")
plt.xlabel("Category")
plt.ylabel("Profit Margin (%)")

# Display the chart
plt.tight_layout()

plt.show()
# Check column data types
print("\nColumn data types:")
print(df.dtypes)
# Check whether any order was shipped before it was placed
invalid_dates = df[df["Ship Date"] < df["Order Date"]]

print("\nOrders shipped before order date:")
print("Number of invalid dates:", len(invalid_dates))

# Check minimum and maximum values
print("\nMinimum values:")
print(df[["Sales", "Quantity", "Discount", "Profit"]].min())

print("\nMaximum values:")
print(df[["Sales", "Quantity", "Discount", "Profit"]].max())

# Count record with discount of 30% or more
high_discount = df[df["Discount"] >= 0.30]
print("\nRecords with discounts of 30% or more:")
print("Number of record", len(high_discount))

# Calculate percentage of high-discount records
percentage = (len(high_discount)/ len(df)) * 100
print("\nPercentage of high-discount records:")
print(round(percentage, 2), "%")

" Compare average profit between discount groups"
df["Discount Group"] = df["Discount"].apply(
    lambda x: "High Discount" if x >= 0.30 else "Low Discount"
)
profit_comparison = df.groupby("Discount Group")["Profit"].mean()

print("\nAverage profit by discount group:")
print(profit_comparison)

# Compare average profit by category and group
category_discount_analysis = df.groupby(
    ["Category", "Discount Group"]
)["Profit"].mean()
print("\nAverage profit by category and discount group:")
print(category_discount_analysis)

# Create a grouped bar chart
category_discount_analysis.unstack().plot(
    kind="bar",
    figsize=(10, 6)
)

# Add chart title and labels
plt.title("Average Profit by Category and Discount Group")
plt.xlabel("Product Category")
plt.ylabel("Average Profit")
plt.axhline(y=0, color="red", linestyle="--")

# Display the chart
plt.tight_layout()
plt.show()