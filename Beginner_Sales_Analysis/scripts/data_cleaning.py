"""
Small Business Sales Performance Analysis
Script: data_cleaning.py
Author: ShadowFox Data Analyst Intern
Objective: Perform professional data cleaning, validation, and transformation on raw sales data.
"""

import os
import pandas as pd
import numpy as np

def clean_sales_data(raw_data_path, cleaned_data_path, audit_log_path=None):
    print("=" * 60)
    print("STARTING DATA CLEANING PIPELINE: PROJECT 1")
    print("=" * 60)
    
    # 1. Load raw dataset
    if not os.path.exists(raw_data_path):
        raise FileNotFoundError(f"Raw data file not found at: {raw_data_path}")
        
    df_raw = pd.read_csv(raw_data_path)
    initial_rows = len(df_raw)
    initial_cols = len(df_raw.columns)
    print(f"Loaded raw dataset with {initial_rows} rows and {initial_cols} columns.")
    
    # 2. Duplicate Detection and Removal
    duplicate_count = df_raw.duplicated().sum()
    print(f"\n[Step 1] Duplicate Check: Found {duplicate_count} duplicate rows.")
    df_clean = df_raw.drop_duplicates().copy()
    rows_after_dedup = len(df_clean)
    print(f"         Rows remaining after de-duplication: {rows_after_dedup}")
    
    # 3. Column Names Formatting
    df_clean.columns = df_clean.columns.str.strip()
    
    # 4. Cleaning Text Columns (Product, Category, Region)
    print("\n[Step 2] Cleaning Text Columns...")
    df_clean['Product'] = df_clean['Product'].astype(str).str.strip()
    
    # Normalize category names
    df_clean['Category'] = df_clean['Category'].astype(str).str.strip().str.title()
    df_clean['Category'] = df_clean['Category'].replace({'Office-Supplies': 'Office Supplies'})
    
    # Normalize region names
    df_clean['Region'] = df_clean['Region'].astype(str).str.strip().str.title()
    
    # 5. Handling Missing Values
    print("\n[Step 3] Missing Value Assessment:")
    missing_summary = df_clean.isnull().sum()
    print(missing_summary[missing_summary > 0])
    
    # Payment Method missing imputation
    missing_payments = df_clean['Payment Method'].isnull().sum()
    if missing_payments > 0:
        print(f"         Imputing {missing_payments} missing 'Payment Method' records with 'Not Specified'.")
        df_clean['Payment Method'] = df_clean['Payment Method'].fillna('Not Specified').astype(str).str.strip()
    
    # 6. Data Type Conversion and Currency Cleaning
    print("\n[Step 4] Type Conversion & Currency Formatting...")
    # Clean Unit Price: remove potential '$' and convert to float
    df_clean['Unit Price'] = (
        df_clean['Unit Price']
        .astype(str)
        .str.replace('$', '', regex=False)
        .str.strip()
        .astype(float)
    )
    
    # Ensure Quantity is integer
    df_clean['Quantity'] = df_clean['Quantity'].astype(int)
    
    # Ensure Cost and Sales are floats
    df_clean['Sales'] = df_clean['Sales'].astype(float).round(2)
    df_clean['Cost'] = df_clean['Cost'].astype(float).round(2)
    
    # 7. Standardizing Dates
    print("\n[Step 5] Standardizing Dates...")
    df_clean['Order Date'] = pd.to_datetime(df_clean['Order Date'], format='mixed')
    df_clean['Order Date'] = df_clean['Order Date'].dt.strftime('%Y-%m-%d')
    
    # 8. Business Rule Validation & Analytical Feature Engineering
    print("\n[Step 6] Business Rule Validation & Derived Columns...")
    # Validate Profit calculation: Profit = Sales - Cost
    df_clean['Profit'] = (df_clean['Sales'] - df_clean['Cost']).round(2)
    
    # Calculate Profit Margin %
    df_clean['Profit Margin %'] = np.where(
        df_clean['Sales'] > 0,
        ((df_clean['Profit'] / df_clean['Sales']) * 100).round(2),
        0.0
    )
    
    # Derived temporal columns for time series analysis
    date_dt = pd.to_datetime(df_clean['Order Date'])
    df_clean['Year'] = date_dt.dt.year
    df_clean['Month'] = date_dt.dt.month
    df_clean['Month Name'] = date_dt.dt.strftime('%b')
    df_clean['Year-Month'] = date_dt.dt.strftime('%Y-%m')
    df_clean['Quarter'] = 'Q' + date_dt.dt.quarter.astype(str)
    
    # Sort logically by Order Date and Order ID
    df_clean = df_clean.sort_values(by=['Order Date', 'Order ID']).reset_index(drop=True)
    
    # 9. Save Cleaned Dataset
    os.makedirs(os.path.dirname(cleaned_data_path), exist_ok=True)
    df_clean.to_csv(cleaned_data_path, index=False)
    print(f"\n[Step 7] Cleaned dataset successfully saved to: {cleaned_data_path}")
    print(f"         Final record count: {len(df_clean)} rows, {len(df_clean.columns)} columns.")
    
    # 10. Audit Log / Summary Report
    audit_report = f"""# Data Cleaning Audit Log - Project 1 (Small Business Sales)

## Summary of Operations:
- **Raw File**: {os.path.basename(raw_data_path)}
- **Cleaned File**: {os.path.basename(cleaned_data_path)}
- **Initial Row Count**: {initial_rows}
- **Duplicates Identified and Removed**: {duplicate_count}
- **Rows After De-duplication**: {rows_after_dedup}
- **Missing 'Payment Method' Imputed**: {missing_payments} (Imputed value: 'Not Specified')
- **Categories Normalized**: Title-cased and standardized ('Office-Supplies' -> 'Office Supplies')
- **Regions Standardized**: Title-cased and whitespace trimmed
- **Price/Sales Cleaned**: Stripped '$' currency symbols and enforced float64
- **Date Standardization**: Parsed mixed formats ('MM/DD/YYYY', 'DD-MM-YYYY', 'YYYY-MM-DD') into ISO-8601 ('YYYY-MM-DD')
- **Feature Engineering**: Added `Profit Margin %`, `Year`, `Month`, `Month Name`, `Year-Month`, `Quarter`
- **Integrity Validation**: Recalculated `Profit = Sales - Cost` to guarantee mathematical consistency
- **Final Cleaned Record Count**: {len(df_clean)} rows, {len(df_clean.columns)} columns
"""
    if audit_log_path:
        os.makedirs(os.path.dirname(audit_log_path), exist_ok=True)
        with open(audit_log_path, 'w', encoding='utf-8') as f:
            f.write(audit_report)
        print(f"         Audit log saved to: {audit_log_path}")

    print("=" * 60)
    print("DATA CLEANING COMPLETED SUCCESSFULLY")
    print("=" * 60)
    return df_clean

if __name__ == "__main__":
    base_dir = r"C:\Users\keert\.gemini\antigravity-ide\scratch\ShadowFox_Data_Analyst_Internship\Beginner_Sales_Analysis"
    raw_path = os.path.join(base_dir, "data", "raw_sales_data.csv")
    cleaned_path = os.path.join(base_dir, "data", "cleaned_sales_data.csv")
    audit_path = os.path.join(base_dir, "analysis", "data_cleaning_audit.md")
    
    clean_sales_data(raw_path, cleaned_path, audit_path)
