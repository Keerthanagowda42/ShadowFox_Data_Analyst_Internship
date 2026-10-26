"""
Script to generate realistic raw sales dataset for Project 1: Small Business Sales Performance Analysis.
Contains realistic data quality issues (duplicates, mixed case, trailing spaces, missing values, string currency)
to demonstrate data cleaning proficiency.
"""
import random
import numpy as np
import pandas as pd
from datetime import datetime, timedelta

# Set seed for reproducible results
np.random.seed(42)
random.seed(42)

products_catalog = [
    {"product": "Wireless Mouse", "category": "Electronics", "unit_price": 25.99, "unit_cost": 12.50},
    {"product": "Mechanical Keyboard", "category": "Electronics", "unit_price": 89.99, "unit_cost": 45.00},
    {"product": "HD Webcam 1080p", "category": "Electronics", "unit_price": 54.50, "unit_cost": 28.00},
    {"product": "Noise-Cancelling Headphones", "category": "Electronics", "unit_price": 149.99, "unit_cost": 75.00},
    {"product": "USB-C Multiport Hub", "category": "Electronics", "unit_price": 39.99, "unit_cost": 18.00},
    {"product": "Ergonomic Office Chair", "category": "Furniture", "unit_price": 229.00, "unit_cost": 130.00},
    {"product": "Standing Desk Converter", "category": "Furniture", "unit_price": 189.50, "unit_cost": 105.00},
    {"product": "Mesh Desk Organizer", "category": "Office Supplies", "unit_price": 18.75, "unit_cost": 7.50},
    {"product": "Gel Ink Pens (12-pack)", "category": "Office Supplies", "unit_price": 12.99, "unit_cost": 4.20},
    {"product": "Heavy-Duty Paper Shredder", "category": "Office Supplies", "unit_price": 79.99, "unit_cost": 42.00},
    {"product": "A4 Copy Paper (Ream)", "category": "Office Supplies", "unit_price": 8.50, "unit_cost": 3.80},
    {"product": "Ceramic Coffee Mug Set", "category": "Home & Kitchen", "unit_price": 24.00, "unit_cost": 10.00},
    {"product": "Stainless Steel Water Bottle", "category": "Home & Kitchen", "unit_price": 19.99, "unit_cost": 8.50},
    {"product": "LED Desk Lamp", "category": "Home & Kitchen", "unit_price": 34.99, "unit_cost": 16.00},
    {"product": "Smart Surge Protector", "category": "Electronics", "unit_price": 29.99, "unit_cost": 14.00}
]

regions = ["North", "South", "East", "West", "Central"]
payment_methods = ["Credit Card", "Debit Card", "PayPal", "Bank Transfer", "Cash on Delivery"]

start_date = datetime(2024, 1, 1)
end_date = datetime(2024, 12, 31)
date_range_days = (end_date - start_date).days

records = []
num_orders = 1250

for i in range(1, num_orders + 1):
    order_id = f"ORD-2024-{1000 + i}"
    random_days = random.randint(0, date_range_days)
    order_dt = start_date + timedelta(days=random_days)
    
    prod_item = random.choice(products_catalog)
    product_name = prod_item["product"]
    category = prod_item["category"]
    
    # Seasonality boost for Q4 (Oct-Dec)
    if order_dt.month in [11, 12]:
        qty = np.random.choice([1, 2, 3, 4, 5, 6, 8], p=[0.30, 0.25, 0.18, 0.12, 0.08, 0.04, 0.03])
    else:
        qty = np.random.choice([1, 2, 3, 4, 5], p=[0.45, 0.28, 0.15, 0.08, 0.04])
    
    unit_price = prod_item["unit_price"]
    unit_cost = prod_item["unit_cost"]
    
    sales = round(qty * unit_price, 2)
    cost = round(qty * unit_cost, 2)
    profit = round(sales - cost, 2)
    
    region = random.choice(regions)
    payment = random.choice(payment_methods)
    
    # Introduce deliberate raw data dirty variations:
    # 1. Date format inconsistency
    if i % 15 == 0:
        date_str = order_dt.strftime("%m/%d/%Y")
    elif i % 23 == 0:
        date_str = order_dt.strftime("%d-%m-%Y")
    else:
        date_str = order_dt.strftime("%Y-%m-%d")
        
    # 2. Inconsistent category text
    raw_cat = category
    if i % 17 == 0:
        raw_cat = category.lower()
    elif i % 29 == 0:
        raw_cat = category.upper()
    elif i % 37 == 0:
        raw_cat = f"  {category}  "
    elif i % 59 == 0 and category == "Office Supplies":
        raw_cat = "Office-Supplies"

    # 3. Inconsistent region
    raw_region = region
    if i % 19 == 0:
        raw_region = region.lower()
    elif i % 31 == 0:
        raw_region = f"{region} "
        
    # 4. Inconsistent product name with spaces
    raw_product = product_name
    if i % 21 == 0:
        raw_product = f" {product_name} "
        
    # 5. Missing values in Payment Method (approx 3%)
    raw_payment = payment
    if i % 33 == 0:
        raw_payment = None
        
    # 6. String currency formatting in Unit Price / Sales for a few rows
    raw_price = unit_price
    if i % 43 == 0:
        raw_price = f"${unit_price:.2f}"
        
    records.append({
        "Order ID": order_id,
        "Order Date": date_str,
        "Product": raw_product,
        "Category": raw_cat,
        "Quantity": qty,
        "Unit Price": raw_price,
        "Sales": sales,
        "Cost": cost,
        "Profit": profit,
        "Region": raw_region,
        "Payment Method": raw_payment
    })

# Convert to DataFrame
df_raw = pd.DataFrame(records)

# 7. Add deliberate duplicate rows (approx 20 duplicates)
duplicates = df_raw.sample(n=20, random_state=42)
df_raw = pd.concat([df_raw, duplicates], ignore_index=True)

# Shuffle rows
df_raw = df_raw.sample(frac=1.0, random_state=42).reset_index(drop=True)

# Save to destination
output_path = r"C:\Users\keert\.gemini\antigravity-ide\scratch\ShadowFox_Data_Analyst_Internship\Beginner_Sales_Analysis\data\raw_sales_data.csv"
df_raw.to_csv(output_path, index=False)
print(f"Generated raw sales data with {len(df_raw)} records at: {output_path}")
