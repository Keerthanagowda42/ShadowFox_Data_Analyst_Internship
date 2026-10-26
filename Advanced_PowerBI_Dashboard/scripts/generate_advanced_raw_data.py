"""
Advanced Power BI Dashboard
Script: generate_advanced_raw_data.py
Author: ShadowFox Data Analyst Intern
Objective: Generate a comprehensive enterprise retail operations dataset (2022-2024)
           supporting a complete Star Schema, Time Intelligence DAX, Budget Variance,
           Logistics SLAs, and Multi-level Drilldowns.
"""

import random
import numpy as np
import pandas as pd
from datetime import datetime, timedelta

# Set seeds
np.random.seed(2024)
random.seed(2024)

# Sub-categories mapped to Categories
catalog_structure = {
    "Technology": {
        "Phones": [("Smart Phone Pro Max", 899.0, 480.0), ("Compact 5G Phone", 499.0, 270.0), ("Rugged Field Phone", 350.0, 190.0)],
        "Accessories": [("Fast Wireless Charger", 35.0, 14.0), ("Ultra USB-C Hub", 65.0, 28.0), ("Bluetooth Earphones", 85.0, 38.0)],
        "Machines": [("High-Volume Laser Printer", 1250.0, 800.0), ("Enterprise Thermal Labeler", 340.0, 190.0)],
        "Copiers": [("Commercial Color Copier", 2200.0, 1400.0), ("Desktop Multi-Scanner", 420.0, 240.0)]
    },
    "Furniture": {
        "Chairs": [("Ergonomic Task Chair", 240.0, 130.0), ("Executive Leather High-Back", 390.0, 220.0), ("Stackable Conference Chair", 95.0, 50.0)],
        "Tables": [("Modular Conference Table", 850.0, 480.0), ("Height-Adjustable Standing Desk", 450.0, 250.0), ("Coffee Break Table", 160.0, 90.0)],
        "Bookcases": [("5-Tier Wooden Bookcase", 180.0, 95.0), ("Heavy Steel Shelving", 280.0, 150.0)],
        "Furnishings": [("Floor Desk Lamp", 55.0, 24.0), ("Anti-Fatigue Standing Mat", 45.0, 18.0), ("Acoustic Desk Screen", 110.0, 55.0)]
    },
    "Office Supplies": {
        "Storage": [("Locking Steel File Cabinet", 195.0, 110.0), ("Stackable Heavy Totes (4-pk)", 48.0, 22.0)],
        "Binders": [("Heavy-Duty Ring Binder", 12.5, 4.5), ("Presentation Folder Box", 28.0, 11.0)],
        "Paper": [("Premium Multipurpose Ream", 9.5, 4.0), ("Color Cardstock 250-pk", 18.0, 7.5)],
        "Appliances": [("Compact Office Microwave", 145.0, 80.0), ("High-Pressure Espresso Maker", 220.0, 120.0)],
        "Art": [("Dual-Tip Marker Set (36-pk)", 32.0, 12.0), ("Framed Magnetic Whiteboard", 85.0, 38.0)]
    }
}

geography_hierarchy = [
    {"market": "North America", "region": "US East", "country": "United States", "state": "New York", "city": "New York City"},
    {"market": "North America", "region": "US West", "country": "United States", "state": "California", "city": "Los Angeles"},
    {"market": "North America", "region": "US Central", "country": "United States", "state": "Illinois", "city": "Chicago"},
    {"market": "North America", "region": "US South", "country": "United States", "state": "Texas", "city": "Houston"},
    {"market": "Europe", "region": "EU West", "country": "United Kingdom", "state": "Greater London", "city": "London"},
    {"market": "Europe", "region": "EU Central", "country": "Germany", "state": "Bavaria", "city": "Munich"},
    {"market": "Europe", "region": "EU North", "country": "Sweden", "state": "Stockholm", "city": "Stockholm"},
    {"market": "Asia-Pacific", "region": "APAC East", "country": "Japan", "state": "Tokyo", "city": "Tokyo"},
    {"market": "Asia-Pacific", "region": "APAC South", "country": "Australia", "state": "New South Wales", "city": "Sydney"},
    {"market": "Asia-Pacific", "region": "APAC Central", "country": "Singapore", "state": "Central Region", "city": "Singapore"}
]

customer_segments = ["Consumer", "Corporate", "Home Office"]
ship_modes = [("Standard Class", 4, 7), ("Second Class", 2, 4), ("First Class", 1, 3), ("Same Day", 0, 1)]

# Generate 600 distinct customers
customers_list = []
for cid in range(1, 601):
    c_key = f"CUST-{2000 + cid}"
    c_name = f"Customer_{cid}"
    c_seg = random.choice(customer_segments)
    geo = random.choice(geography_hierarchy)
    customers_list.append({
        "Customer_ID": c_key,
        "Customer_Name": c_name,
        "Segment": c_seg,
        "City": geo["city"],
        "State": geo["state"],
        "Country": geo["country"],
        "Region": geo["region"],
        "Market": geo["market"]
    })

start_date = datetime(2022, 1, 1)
end_date = datetime(2024, 12, 31)
total_days = (end_date - start_date).days

num_records = 4200
records = []

for i in range(1, num_records + 1):
    order_id = f"CA-{2022 + (i % 3)}-{100000 + i}"
    
    # Simulate upward trend across 2022-2024
    day_offset = int(np.random.beta(a=1.5, b=1.0) * total_days)
    order_dt = start_date + timedelta(days=min(day_offset, total_days))
    
    cust = random.choice(customers_list)
    
    # Pick product
    cat = random.choice(list(catalog_structure.keys()))
    subcat = random.choice(list(catalog_structure[cat].keys()))
    prod_name, unit_price, unit_cost = random.choice(catalog_structure[cat][subcat])
    prod_id = f"PRD-{cat[:2].upper()}-{subcat[:3].upper()}-{random.randint(101, 199)}"
    
    # Shipping info
    ship_mode, min_d, max_d = random.choice(ship_modes)
    ship_days = random.randint(min_d, max_d + 1)
    ship_dt = order_dt + timedelta(days=ship_days)
    shipping_cost = round(random.uniform(5.0, 35.0) + (unit_price * 0.02), 2)
    
    qty = np.random.choice([1, 2, 3, 4, 5, 6], p=[0.45, 0.25, 0.15, 0.08, 0.04, 0.03])
    
    # Occasional discount
    discount_rate = np.random.choice([0.0, 0.05, 0.10, 0.15, 0.20, 0.30], p=[0.55, 0.15, 0.12, 0.10, 0.05, 0.03])
    gross_sales = round(qty * unit_price, 2)
    net_sales = round(gross_sales * (1.0 - discount_rate), 2)
    total_cost = round(qty * unit_cost, 2)
    profit = round(net_sales - total_cost, 2)
    
    # Return status (approx 4.5% returns)
    returned = "Yes" if random.random() < 0.045 else "No"
    
    # Inject dirty data features for cleaning demonstration:
    # 1. Dates in mixed format
    dt_str = order_dt.strftime("%Y-%m-%d")
    if i % 31 == 0:
        dt_str = order_dt.strftime("%m/%d/%Y")
    elif i % 53 == 0:
        dt_str = order_dt.strftime("%d-%m-%Y")
        
    ship_str = ship_dt.strftime("%Y-%m-%d")
    if i % 37 == 0:
        ship_str = ship_dt.strftime("%m/%d/%Y")
        
    # 2. Text casing
    raw_cat = cat
    if i % 29 == 0:
        raw_cat = cat.lower()
        
    raw_region = cust["Region"]
    if i % 43 == 0:
        raw_region = f"  {cust['Region']}  "
        
    # 3. Missing postal codes or phone
    raw_segment = cust["Segment"]
    if i % 67 == 0:
        raw_segment = None
        
    records.append({
        "Order_ID": order_id,
        "Order_Date": dt_str,
        "Ship_Date": ship_str,
        "Ship_Mode": ship_mode,
        "Customer_ID": cust["Customer_ID"],
        "Customer_Name": cust["Customer_Name"],
        "Segment": raw_segment,
        "City": cust["City"],
        "State": cust["State"],
        "Country": cust["Country"],
        "Region": raw_region,
        "Market": cust["Market"],
        "Product_ID": prod_id,
        "Category": raw_cat,
        "Sub_Category": subcat,
        "Product_Name": prod_name,
        "Sales": net_sales,
        "Quantity": qty,
        "Discount": discount_rate,
        "Profit": profit,
        "Shipping_Cost": shipping_cost,
        "Returned": returned
    })

df_raw = pd.DataFrame(records)

# Add duplicate rows
dups = df_raw.sample(n=35, random_state=2024)
df_raw = pd.concat([df_raw, dups], ignore_index=True)
df_raw = df_raw.sample(frac=1.0, random_state=2024).reset_index(drop=True)

out_file = r"C:\Users\keert\.gemini\antigravity-ide\scratch\ShadowFox_Data_Analyst_Internship\Advanced_PowerBI_Dashboard\data\raw_business_data.csv"
df_raw.to_csv(out_file, index=False)
print(f"Generated raw enterprise business dataset with {len(df_raw)} records at: {out_file}")
