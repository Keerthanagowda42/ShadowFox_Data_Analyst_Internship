"""
Intermediate Customer Analytics
Script: customer_cleaning.py
Author: ShadowFox Data Analyst Intern
Objective: Perform data quality audit, cleaning, validation, and cohort feature engineering
           on raw customer transaction records.
"""

import os
import pandas as pd
import numpy as np

def clean_customer_data(raw_path, cleaned_path, audit_path=None):
    print("=" * 60)
    print("STARTING DATA CLEANING PIPELINE: PROJECT 2")
    print("=" * 60)
    
    if not os.path.exists(raw_path):
        raise FileNotFoundError(f"Raw data file not found at: {raw_path}")
        
    df_raw = pd.read_csv(raw_path)
    initial_rows = len(df_raw)
    print(f"Loaded raw customer transaction dataset: {initial_rows} rows, {len(df_raw.columns)} columns.")
    
    # 1. Deduplication
    dups = df_raw.duplicated(subset=['Transaction_ID']).sum()
    print(f"\n[Step 1] Duplicate Detection: Found {dups} duplicate transactions.")
    df_clean = df_raw.drop_duplicates(subset=['Transaction_ID']).copy()
    rows_after_dedup = len(df_clean)
    print(f"         Remaining unique transactions: {rows_after_dedup}")
    
    # 2. Text Normalization
    print("\n[Step 2] Normalizing text fields...")
    df_clean['Customer_Region'] = df_clean['Customer_Region'].astype(str).str.strip().str.title()
    df_clean['Acquisition_Channel'] = df_clean['Acquisition_Channel'].astype(str).str.strip()
    df_clean['Product_Category'] = df_clean['Product_Category'].astype(str).str.strip()
    df_clean['Product_Name'] = df_clean['Product_Name'].astype(str).str.strip()
    
    # 3. Missing Value Handling
    print("\n[Step 3] Handling missing fields...")
    missing_email_cnt = df_clean['Customer_Email'].isnull().sum()
    if missing_email_cnt > 0:
        # Synthesize fallback email based on customer ID
        df_clean['Customer_Email'] = df_clean['Customer_Email'].fillna(
            df_clean['Customer_ID'].str.lower() + '@unverified.customer.com'
        )
        print(f"         Filled {missing_email_cnt} missing emails with customer ID aliases.")
        
    missing_payment_cnt = df_clean['Payment_Method'].isnull().sum()
    if missing_payment_cnt > 0:
        df_clean['Payment_Method'] = df_clean['Payment_Method'].fillna('Not Disclosed')
        print(f"         Imputed {missing_payment_cnt} missing payment methods with 'Not Disclosed'.")
        
    # 4. Standardizing Dates
    print("\n[Step 4] Parsing transaction dates...")
    df_clean['Transaction_Date'] = pd.to_datetime(df_clean['Transaction_Date'], format='mixed')
    df_clean['Year'] = df_clean['Transaction_Date'].dt.year
    df_clean['Month'] = df_clean['Transaction_Date'].dt.month
    df_clean['Year_Month'] = df_clean['Transaction_Date'].dt.strftime('%Y-%m')
    df_clean['Transaction_Date_Str'] = df_clean['Transaction_Date'].dt.strftime('%Y-%m-%d')
    
    # 5. Financial Calculations Validation
    print("\n[Step 5] Validating calculations...")
    df_clean['Quantity'] = df_clean['Quantity'].astype(int)
    df_clean['Unit_Price'] = df_clean['Unit_Price'].astype(float).round(2)
    df_clean['Discount_Amount'] = df_clean['Discount_Amount'].fillna(0.0).astype(float).round(2)
    
    # Recompute Total_Spend to guarantee 100% mathematical integrity
    df_clean['Total_Spend'] = ((df_clean['Quantity'] * df_clean['Unit_Price']) - df_clean['Discount_Amount']).round(2)
    
    # 6. Customer First Purchase (Cohort Assignment)
    print("\n[Step 6] Engineering Customer Cohort & Tenure...")
    cohort_df = df_clean.groupby('Customer_ID')['Transaction_Date'].min().reset_index()
    cohort_df.columns = ['Customer_ID', 'First_Purchase_Date']
    cohort_df['Cohort_Month'] = cohort_df['First_Purchase_Date'].dt.strftime('%Y-%m')
    
    df_clean = pd.merge(df_clean, cohort_df, on='Customer_ID', how='left')
    
    # Cohort Index (difference in months between transaction and first purchase)
    txn_year = df_clean['Transaction_Date'].dt.year
    txn_month = df_clean['Transaction_Date'].dt.month
    first_year = df_clean['First_Purchase_Date'].dt.year
    first_month = df_clean['First_Purchase_Date'].dt.month
    
    df_clean['Cohort_Index'] = (txn_year - first_year) * 12 + (txn_month - first_month)
    
    # Sort chronologically
    df_clean = df_clean.sort_values(by=['Transaction_Date', 'Transaction_ID']).reset_index(drop=True)
    
    # 7. Export Clean Dataset
    os.makedirs(os.path.dirname(cleaned_path), exist_ok=True)
    df_clean.to_csv(cleaned_path, index=False)
    print(f"\nCleaned dataset saved to: {cleaned_path}")
    print(f"Final records: {len(df_clean)} rows, {len(df_clean.columns)} columns.")
    
    # 8. Audit Log
    audit_content = f"""# Data Cleaning & Transformation Audit - Project 2 (Customer Analytics)

- **Source Dataset**: `raw_customer_data.csv`
- **Cleaned Dataset**: `cleaned_customer_data.csv`
- **Initial Transaction Records**: {initial_rows}
- **Duplicate Records Removed**: {dups}
- **Valid Unique Transactions**: {rows_after_dedup}
- **Distinct Customers**: {df_clean['Customer_ID'].nunique()}
- **Missing Emails Handled**: {missing_email_cnt}
- **Missing Payment Methods Imputed**: {missing_payment_cnt}
- **Date Standardization**: Unified all mixed formats to ISO-8601 (`YYYY-MM-DD`)
- **Engineered Analytical Features**:
  - `Year`, `Month`, `Year_Month`
  - `First_Purchase_Date` (Customer acquisition timestamp)
  - `Cohort_Month` (Initial acquisition cohort)
  - `Cohort_Index` (Elapsed months since acquisition for retention analysis)
  - Recomputed `Total_Spend = (Quantity * Unit_Price) - Discount_Amount`
"""
    if audit_path:
        os.makedirs(os.path.dirname(audit_path), exist_ok=True)
        with open(audit_path, 'w', encoding='utf-8') as f:
            f.write(audit_content)
        print(f"Audit log saved to: {audit_path}")
        
    print("=" * 60)
    print("CUSTOMER DATA CLEANING COMPLETE")
    print("=" * 60)
    return df_clean

if __name__ == "__main__":
    base_dir = r"C:\Users\keert\.gemini\antigravity-ide\scratch\ShadowFox_Data_Analyst_Internship\Intermediate_Customer_Analytics"
    raw_p = os.path.join(base_dir, "data", "raw_customer_data.csv")
    clean_p = os.path.join(base_dir, "data", "cleaned_customer_data.csv")
    audit_p = os.path.join(base_dir, "analysis", "data_cleaning_audit.md")
    
    clean_customer_data(raw_p, clean_p, audit_p)
