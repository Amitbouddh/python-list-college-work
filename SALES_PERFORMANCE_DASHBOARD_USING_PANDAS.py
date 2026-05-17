# =========================================================
# 📊 SALES PERFORMANCE DASHBOARD USING PANDAS
# =========================================================

import pandas as pd

# Load dataset with encoding fix
sales_data = pd.read_csv(
    r"try\tasks\Sample - Superstore.csv",
    encoding='latin1'
)

# Display first 5 rows
print(sales_data.head())


# =========================================================
# STEP 2 — DATASET INFORMATION
# =========================================================

print("\n=================================================")
print("📊 DATASET INFO")
print("=================================================")

print(sales_data.info())


# =========================================================
# STEP 3 — TOTAL SALES & PROFIT
# =========================================================

print("\n=================================================")
print("💰 SALES & PROFIT BY REGION AND CATEGORY")
print("=================================================")

region_category_summary = sales_data.groupby(
    ['Region', 'Category']
)[['Sales', 'Profit']].sum()

print(region_category_summary)


# =========================================================
# STEP 4 — AGGREGATION FUNCTIONS
# =========================================================

print("\n=================================================")
print("📈 MULTIPLE AGGREGATIONS")
print("=================================================")

aggregation = sales_data.groupby(
    'Region'
).agg({

    'Sales': ['sum', 'mean', 'max'],
    'Profit': ['sum', 'mean']

})

print(aggregation)


# =========================================================
# STEP 5 — TOP 3 SUB-CATEGORIES
# =========================================================

print("\n=================================================")
print("🏆 TOP 3 SUB-CATEGORIES IN EACH REGION")
print("=================================================")

top_subcategories = sales_data.groupby(
    ['Region', 'Sub-Category']
)['Sales'].sum().reset_index()

top_subcategories = top_subcategories.sort_values(
    by=['Region', 'Sales'],
    ascending=[True, False]
)

top_3 = top_subcategories.groupby(
    'Region'
).head(3)

print(top_3)


# =========================================================
# STEP 6 — PROFIT MARGIN COLUMN
# =========================================================

sales_data['Profit Margin %'] = (

    sales_data['Profit']
    /
    sales_data['Sales']

) * 100

print("\n=================================================")
print("📌 PROFIT MARGIN")
print("=================================================")

print(

    sales_data[
        ['Sales', 'Profit', 'Profit Margin %']
    ].head()

)


# =========================================================
# STEP 7 — PIVOT TABLE
# =========================================================

print("\n=================================================")
print("📊 PIVOT TABLE")
print("=================================================")

pivot = pd.pivot_table(

    sales_data,

    values='Sales',

    index='Region',

    columns='Segment',

    aggfunc='mean'

)

print(pivot)


# =========================================================
# STEP 8 — NEGATIVE PROFIT MONTHS
# =========================================================

sales_data['Order Date'] = pd.to_datetime(
    sales_data['Order Date']
)

sales_data['Month'] = sales_data[
    'Order Date'
].dt.month_name()

monthly_profit = sales_data.groupby(
    'Month'
)['Profit'].sum()

negative_profit_months = monthly_profit[
    monthly_profit < 0
]

print("\n=================================================")
print("📉 MONTHS WITH NEGATIVE PROFIT")
print("=================================================")

print(negative_profit_months)


# =========================================================
# STEP 9 — APPLY + LAMBDA
# =========================================================

sales_data['Sales Category'] = sales_data[
    'Sales'
].apply(

    lambda x:
    'High' if x > 500
    else 'Low'

)

print("\n=================================================")
print("🔥 SALES CATEGORY")
print("=================================================")

print(

    sales_data[
        ['Sales', 'Sales Category']
    ].head()

)


# =========================================================
# BONUS CHALLENGE
# =========================================================

sales_data.set_index(
    'Order Date',
    inplace=True
)

quarterly_sales = sales_data[
    'Sales'
].resample('Q').sum()

print("\n=================================================")
print("📅 QUARTERLY SALES")
print("=================================================")

print(quarterly_sales)


# =========================================================
# FINAL MESSAGE
# =========================================================

print("\n=================================================")
print("✅ SALES ANALYSIS COMPLETED SUCCESSFULLY!")
print("=================================================")