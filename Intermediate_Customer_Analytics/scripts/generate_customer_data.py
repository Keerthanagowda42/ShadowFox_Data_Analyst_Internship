"""
Intermediate Customer Analytics
Script: generate_customer_data.py
Author: ShadowFox Data Analyst Intern
Objective: Generate a realistic 2-year customer transaction dataset (2023-2024)
           to support RFM segmentation, Cohort Retention analysis, Pareto analysis,
           repeat vs one-time customer behavior, and SQL analytics.
"""

import random
import numpy as np
import pandas as pd
from datetime import datetime, timedelta

# Set random seed
np.random.seed(101)
random.seed(101)

# Catalog definitions
products = [
    {"id": "PRD-EL01", "name": "Wireless Noise-Canceling Earbuds", "category": "Electronics", "price": 79.99},
    {"id": "PRD-EL02", "name": "Smart Fitness Watch V2", "category": "Electronics", "price": 149.99},
    {"id": "PRD-EL03", "name": "4K Ultra-Portable Monitor", "category": "Electronics", "price": 229.00},
    {"id": "PRD-AP01", "name": "Merino Wool Athletic Pullover", "category": "Apparel", "price": 64.50},
    {"id": "PRD-AP02", "name": "Performance Stretch Chino Pants", "category": "Apparel", "price": 54.00},
    {"id": "PRD-AP03", "name": "All-Weather Breathable Jacket", "category": "Apparel", "price": 119.99},
    {"id": "PRD-HM01", "name": "Ceramic Aroma Diffuser", "category": "Home & Living", "price": 34.50},
    {"id": "PRD-HM02", "name": "Organic Egyptian Cotton Sheets", "category": "Home & Living", "price": 89.00},
    {"id": "PRD-HM03", "name": "Handcrafted Stoneware Dinner Set", "category": "Home & Living", "price": 115.00},
    {"id": "PRD-HB01", "name": "Botanical Hydration Serum (50ml)", "category": "Health & Beauty", "price": 38.00},
    {"id": "PRD-HB02", "name": "Sonic Electric Toothbrush", "category": "Health & Beauty", "price": 69.50},
    {"id": "PRD-SP01", "name": "High-Density Non-Slip Yoga Mat", "category": "Sports & Outdoors", "price": 42.00},
    {"id": "PRD-SP02", "name": "Insulated Stainless Steel Flask (1L)", "category": "Sports & Outdoors", "price": 28.50},
    {"id": "PRD-SP03", "name": "Adjustable Dumbbell Set (Pair)", "category": "Sports & Outdoors", "price": 175.00}
]

regions = ["North America", "Europe", "Asia-Pacific", "Latin America", "Middle East"]
channels = ["Organic Search", "Paid Search", "Email Marketing", "Social Media", "Referral"]
payment_methods = ["Credit Card", "PayPal", "Apple Pay", "Debit Card", "Bank Transfer"]

# Generate 850 distinct customer profiles
num_customers = 850
customers = []
first_names = ["James", "Emma", "Liam", "Olivia", "Noah", "Ava", "Oliver", "Sophia", "Lucas", "Isabella", 
               "Ethan", "Mia", "Aiden", "Charlotte", "Harper", "Benjamin", "Evelyn", "Alex", "Chloe", "Daniel"]
last_names = ["Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Davis", "Rodriguez", "Martinez",
              "Hernandez", "Lopez", "Gonzalez", "Wilson", "Anderson", "Thomas", "Taylor", "Moore", "Jackson", "Martin"]

# Cohort assignment (Month when customer was first acquired)
start_cohort = datetime(2023, 1, 1)
customer_profiles = {}

for c_idx in range(1, num_customers + 1):
    c_id = f"CUST-{1000 + c_idx}"
    fn = random.choice(first_names)
    ln = random.choice(last_names)
    name = f"{fn} {ln}"
    email = f"{fn.lower()}.{ln.lower()}{random.randint(10, 99)}@example.com"
    region = random.choice(regions)
    channel = random.choice(channels)
    
    # Customer initial acquisition date (between Jan 2023 and Dec 2024)
    acq_month_offset = random.randint(0, 22) # up to Nov 2024
    first_purchase_date = start_cohort + timedelta(days=acq_month_offset * 30 + random.randint(1, 28))
    
    # Customer loyalty archetype: One-time (55%), Occasional (30%), Champion/Loyal (15%)
    archetype = np.random.choice(["one_time", "occasional", "loyal"], p=[0.52, 0.33, 0.15])
    
    customer_profiles[c_id] = {
        "id": c_id,
        "name": name,
        "email": email,
        "region": region,
        "channel": channel,
        "first_purchase": first_purchase_date,
        "archetype": archetype
    }

# Generate transactions
transactions = []
end_study_date = datetime(2024, 12, 31)
txn_counter = 1

for c_id, profile in customer_profiles.items():
    archetype = profile["archetype"]
    first_dt = profile["first_purchase"]
    
    if archetype == "one_time":
        num_orders = 1
    elif archetype == "occasional":
        num_orders = random.randint(2, 5)
    else: # loyal
        num_orders = random.randint(6, 14)
        
    current_dt = first_dt
    for o_idx in range(num_orders):
        if current_dt > end_study_date:
            break
            
        prod = random.choice(products)
        qty = np.random.choice([1, 2, 3, 4], p=[0.60, 0.25, 0.10, 0.05])
        unit_price = prod["price"]
        
        # Occasional discount
        discount = 0.0
        if random.random() < 0.25:
            discount = round(unit_price * qty * random.choice([0.05, 0.10, 0.15, 0.20]), 2)
            
        total_spend = round((unit_price * qty) - discount, 2)
        payment = random.choice(payment_methods)
        
        # Format date with raw variations
        dt_str = current_dt.strftime("%Y-%m-%d")
        if txn_counter % 29 == 0:
            dt_str = current_dt.strftime("%m/%d/%Y")
        elif txn_counter % 47 == 0:
            dt_str = current_dt.strftime("%d-%m-%Y")
            
        # Inconsistent region
        raw_reg = profile["region"]
        if txn_counter % 33 == 0:
            raw_reg = raw_reg.lower()
        elif txn_counter % 51 == 0:
            raw_reg = f" {raw_reg} "
            
        # Missing email or payment
        raw_email = profile["email"]
        if txn_counter % 41 == 0:
            raw_email = None
            
        raw_payment = payment
        if txn_counter % 37 == 0:
            raw_payment = None
            
        transactions.append({
            "Transaction_ID": f"TXN-{10000 + txn_counter}",
            "Customer_ID": c_id,
            "Customer_Name": profile["name"],
            "Customer_Email": raw_email,
            "Customer_Region": raw_reg,
            "Acquisition_Channel": profile["channel"],
            "Transaction_Date": dt_str,
            "Product_ID": prod["id"],
            "Product_Name": prod["name"],
            "Product_Category": prod["category"],
            "Quantity": qty,
            "Unit_Price": unit_price,
            "Discount_Amount": discount,
            "Total_Spend": total_spend,
            "Payment_Method": raw_payment
        })
        txn_counter += 1
        
        # Advance date for next order
        days_gap = random.randint(15, 90)
        current_dt = current_dt + timedelta(days=days_gap)

df_txns = pd.DataFrame(transactions)

# Inject intentional duplicate rows (approx 30 duplicates)
dups = df_txns.sample(n=30, random_state=101)
df_txns = pd.concat([df_txns, dups], ignore_index=True)

# Shuffle
df_txns = df_txns.sample(frac=1.0, random_state=101).reset_index(drop=True)

# Save raw dataset
out_path = r"C:\Users\keert\.gemini\antigravity-ide\scratch\ShadowFox_Data_Analyst_Internship\Intermediate_Customer_Analytics\data\raw_customer_data.csv"
df_txns.to_csv(out_path, index=False)
print(f"Generated raw customer transaction dataset with {len(df_txns)} records at: {out_path}")
