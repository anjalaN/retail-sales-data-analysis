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

# Check the distribution of sales
print("\nSales descriptive statistics:")
print(df["Sales"].describe())

" Calculate the first and third quartiles"
Q1 = df["Sales"].quantile(0.25)
Q3 = df["Sales"].quantile(0.75)

# Calculate the Interquartile Range
IQR = Q3 - Q1
print("\nSales IQR:", IQR)

# Calculate the lower and upper outlier boundaries
lower_bound = Q1 - (1.5 * IQR)
upper_bound = Q3 + (1.5 * IQR)

print("\nLower boundary:", lower_bound)
print("Upper boundary:", upper_bound)

# Identify potential upper outliers
Sales_outliers = df[df["Sales"] > upper_bound]

# Count potential outliers
print("\nNumber of potential Sales outliers:")
print(len(Sales_outliers))

# Calculate the percentage of potential sales outliers
outlier_percentage = (len(Sales_outliers) / len(df)) * 100
print("\nPercentage of potential Sales outliers:")
print(round(outlier_percentage, 2), "%")

# Display the 10 heighest Sales values 
print("\nTop 10 highest Sales records:")
print(Sales_outliers.nlargest(10, "Sales")[["Order ID", "Product Name", "Sales", "Profit"]])

# Display the 10 highest Sales records clearly
print(
    Sales_outliers.nlargest(10, "Sales")[
        ["Order ID", "Product Name", "Sales", "Profit"]
    ].to_string(index=False)
)

# Visualise potential Sales outliers
plt.figure(figsize=(10, 5))

df["Sales"].plot(kind="box")

plt.title("Boxplot of Sales")
plt.ylabel("Sales")

plt.show()
# Check the distribution of Profit
print("\nProfit descriptive statistics:")
print(df["Profit"].describe())

# Calculate the first and third quartiles
Q1_profit = df["Profit"].quantile(0.25)
Q3_profit = df["Profit"].quantile(0.75)

# Calculate the Interquartile Range
IQR_profit = Q3_profit - Q1_profit

print("\nProfit IQR:", IQR_profit)

# Calculate the lower nd upper profit boundaries
lower_bound_profit = Q1_profit - (1.5 * IQR_profit)
upper_bound_profit = Q3_profit + (1.5 * IQR_profit)
print("\nLower Profit boundary:", lower_bound_profit)
print("Upper Profit boundary:", upper_bound_profit)

# Identify potential lower Profit outliers
lower_profit_outliers = df[df["Profit"] < lower_bound_profit]

# Identify potential upper Profit outliers
upper_profit_outliers = df[df["Profit"] > upper_bound_profit]

# Count the potential outliers
print("\nNumber of lower Profit outliers:")
print(len(lower_profit_outliers))

print("\nNumber of upper Profit outliers:")
print(len(upper_profit_outliers))

# Calculate the percentage of lower Profit outliers
lower_percentage = (len(lower_profit_outliers) / len(df)) * 100

# Calculate the percentage of upper Profit outliers
upper_percentage = (len(upper_profit_outliers) / len(df)) * 100

print("\nLower Profit outliers percentage:")
print(round(lower_percentage, 2), "%")

print("\nUpper Profit outliers percentage:")
print(round(upper_percentage, 2), "%")

# Display the 10 lower profit record
print(
    lower_profit_outliers.nsmallest(10, "Profit")[
        ["Order ID", "Product Name", "Sales", "Profit"]
    ].to_string(index=False)
)

# Display the 10 highest Profit records
print(
    upper_profit_outliers.nlargest(10, "Profit")[
        ["Order ID", "Product Name", "Sales", "Profit"]
    ].to_string(index=False)
)
print(
    upper_profit_outliers.nlargest(10, "Profit")[
        ["Order ID", "Product Name", "Sales", "Profit"]
    ].to_string(index=False)
)
plt.figure(figsize=(10, 5))
df["Profit"].plot(kind="box")
plt.title("Boxplot of Profit")
plt.ylabel("Profit")
plt.show()

# Quantity
print(df["Quantity"].describe())
# Calculate the IQR
Q1_quantity = df["Quantity"].quantile(0.25)
Q3_quantity = df["Quantity"].quantile(0.75)

IQR_quantity = Q3_quantity - Q1_quantity
print("Q1:", Q1_quantity)
print("Q3:", Q3_quantity)
print("IQR:", IQR_quantity)

# Calculate the outline boundaries
lower_bound_quantity = Q1_quantity - (1.5 * IQR_quantity)
upper_bound_quantity = Q3_quantity + (1.5 * IQR_quantity)
print("Lower Bound:", lower_bound_quantity)
print("Upper Bound:", upper_bound_quantity)

# Identify upper oulier
quantity_outliers = df[df["Quantity"] > upper_bound_quantity]
print("Number of Quantity outliers:", len(quantity_outliers))

# Calculate the percentage
quantity_outliers_percentage = (
    len(quantity_outliers) / len(df)
) * 100

print("Quantity outliers percentage:", quantity_outliers_percentage, "%")

# Inspect the 19 largest quantities
print(
    quantity_outliers.nlargest(10, "Quantity")[
        ["Order ID", "Product Name", "Quantity", "Sales", "Profit"]
    ].to_string(index=False)
)
# Create a Quantity boxplot
plt.figure(figsize=(10, 5))
df["Quantity"].plot(kind="box")
plt.title("Boxplot of Quantity")
plt.ylabel("Quantity")
plt.show()

# Discount outlier analisis
print(df["Discount"].describe())
# Calculate Q1, Q3 and IQR
Q1_Discount = df["Discount"].quantile(0.25)
Q3_Discount = df["Discount"].quantile(0.75)

IQR_Discount = Q3_Discount - Q1_Discount

print("Q1:", Q1_Discount)
print("Q3:", Q3_Discount)
print("IQR:", IQR_Discount)

# Calculate the lower and upper boundaries
lower_bound_Discount = Q1_Discount - (1.5 * IQR_Discount)
upper_bound_Discount = Q3_Discount + (1.5 * IQR_Discount)

print("Lower Bound:", lower_bound_Discount)
print("Upper Bound:", upper_bound_Discount)

# Identify Discount outliers
discount_outliers = df[df["Discount"] > upper_bound_Discount]

print("Number of Discount outliers:", len(discount_outliers))

# Inspect the highest Discount values
print(
    discount_outliers.nlargest(10, "Discount")[
        ["Order ID", "Product Name", "Discount", "Sales", "Profit"]
    ].to_string(index=False)
) 

# Discount: Create a boxplot
plt.figure(figsize=(10, 5))
df["Discount"].plot(kind="box")
plt.title("Boxplot of Discount")
plt.ylabel("Discount")
plt.show()