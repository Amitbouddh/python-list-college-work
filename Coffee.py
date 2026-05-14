# =============================
# Coffee Sales Data Science Project
# =============================

# Import Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# -----------------------------
# Step 1: Create Coffee Sales Dataset
# -----------------------------

data = {
    "Day": ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
    "Coffee_Type": ["Latte", "Cappuccino", "Espresso", "Mocha", "Latte", "Espresso", "Cappuccino"],
    "Cups_Sold": [120, 95, 150, 80, 130, 170, 110],
    "Price_Per_Cup": [150, 140, 120, 160, 150, 120, 140]
}

df = pd.DataFrame(data)

# -----------------------------
# Step 2: Show Dataset
# -----------------------------

print("Coffee Shop Dataset")
print(df)

# -----------------------------
# Step 3: Add Revenue Column
# -----------------------------

df["Revenue"] = df["Cups_Sold"] * df["Price_Per_Cup"]

print("\nDataset With Revenue")
print(df)

# -----------------------------
# Step 4: Basic Analysis
# -----------------------------

total_revenue = df["Revenue"].sum()
average_sales = df["Cups_Sold"].mean()
best_day = df.loc[df["Revenue"].idxmax()]

print("\nTotal Revenue =", total_revenue)
print("Average Cups Sold =", average_sales)

print("\nBest Sales Day")
print(best_day)

# -----------------------------
# Step 5: Group By Coffee Type
# -----------------------------

coffee_summary = df.groupby("Coffee_Type")["Revenue"].sum()

print("\nRevenue By Coffee Type")
print(coffee_summary)

# -----------------------------
# Step 6: Plot Graph
# -----------------------------

plt.figure(figsize=(8,5))

plt.bar(df["Day"], df["Revenue"])

plt.title("Coffee Shop Revenue Per Day")
plt.xlabel("Day")
plt.ylabel("Revenue")

plt.show()

# -----------------------------
# Step 7: Pie Chart
# -----------------------------

plt.figure(figsize=(7,7))

plt.pie(
    coffee_summary,
    labels=coffee_summary.index,
    autopct='%1.1f%%'
)

plt.title("Revenue Share By Coffee Type")

plt.show()

# -----------------------------
# Step 8: Save Dataset
# -----------------------------

df.to_csv("coffee_sales.csv", index=False)

print("\nCSV File Saved Successfully!")
