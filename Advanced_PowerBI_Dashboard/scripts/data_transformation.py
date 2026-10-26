"""
Advanced Power BI Dashboard
Script: data_transformation.py
Author: ShadowFox Data Analyst Intern
Objective: Clean raw enterprise business data, engineer operational metrics,
           generate Power BI Star Schema dimension & fact tables,
           and create high-resolution dashboard visuals.
"""

import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

# Matplotlib configuration
plt.style.use('seaborn-v0_8-whitegrid' if 'seaborn-v0_8-whitegrid' in plt.style.available else 'default')
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.size'] = 10
plt.rcParams['axes.titlesize'] = 12
plt.rcParams['axes.titleweight'] = 'bold'
plt.rcParams['axes.labelsize'] = 10
plt.rcParams['axes.labelweight'] = 'bold'
plt.rcParams['figure.titlesize'] = 14
plt.rcParams['figure.titleweight'] = 'bold'

PRIMARY_NAVY = '#0B192C'
SECONDARY_BLUE = '#1E3E62'
ACCENT_ORANGE = '#FF6500'
SUCCESS_GREEN = '#10B981'
ALERT_RED = '#DC2626'

def transform_enterprise_data(base_dir):
    print("=" * 60)
    print("STARTING ADVANCED ENTERPRISE DATA TRANSFORMATION PIPELINE")
    print("=" * 60)
    
    data_dir = os.path.join(base_dir, "data")
    charts_dir = os.path.join(base_dir, "charts")
    dashboard_dir = os.path.join(base_dir, "dashboard")
    reports_dir = os.path.join(base_dir, "reports")
    
    os.makedirs(charts_dir, exist_ok=True)
    os.makedirs(dashboard_dir, exist_ok=True)
    os.makedirs(reports_dir, exist_ok=True)
    
    raw_path = os.path.join(data_dir, "raw_business_data.csv")
    cleaned_path = os.path.join(data_dir, "cleaned_business_data.csv")
    
    df_raw = pd.read_csv(raw_path)
    initial_rows = len(df_raw)
    print(f"Loaded raw enterprise dataset with {initial_rows} records.")
    
    # 1. Deduplication
    dups = df_raw.duplicated().sum()
    print(f"\n[Step 1] Duplicate Detection: {dups} duplicate records identified.")
    df_clean = df_raw.drop_duplicates().copy()
    print(f"         Clean records after de-duplication: {len(df_clean)}")
    
    # 2. Text Normalization
    print("\n[Step 2] Text normalization & Category cleansing...")
    df_clean['Category'] = df_clean['Category'].astype(str).str.strip().str.title()
    df_clean['Sub_Category'] = df_clean['Sub_Category'].astype(str).str.strip().str.title()
    df_clean['Region'] = df_clean['Region'].astype(str).str.strip()
    df_clean['Market'] = df_clean['Market'].astype(str).str.strip()
    df_clean['Ship_Mode'] = df_clean['Ship_Mode'].astype(str).str.strip()
    
    # 3. Missing Value Imputation
    missing_segment = df_clean['Segment'].isnull().sum()
    if missing_segment > 0:
        print(f"\n[Step 3] Imputing {missing_segment} missing Segment values with 'Consumer' (mode).")
        df_clean['Segment'] = df_clean['Segment'].fillna('Consumer')
        
    # 4. Standardizing Dates & Logistics Features
    print("\n[Step 4] Parsing dates and engineering delivery logistics...")
    df_clean['Order_Date'] = pd.to_datetime(df_clean['Order_Date'], format='mixed')
    df_clean['Ship_Date'] = pd.to_datetime(df_clean['Ship_Date'], format='mixed')
    
    df_clean['Delivery_Days'] = (df_clean['Ship_Date'] - df_clean['Order_Date']).dt.days
    
    # On-Time Delivery Flag
    # Standard: <=6 days, Second: <=4 days, First: <=3 days, Same Day: <=1 day
    def check_ontime(row):
        mode = row['Ship_Mode']
        days = row['Delivery_Days']
        if mode == 'Same Day' and days <= 1:
            return 1
        elif mode == 'First Class' and days <= 3:
            return 1
        elif mode == 'Second Class' and days <= 4:
            return 1
        elif mode == 'Standard Class' and days <= 6:
            return 1
        else:
            return 0
            
    df_clean['On_Time_Flag'] = df_clean.apply(check_ontime, axis=1)
    
    # Format date strings for database/Power BI compatibility
    df_clean['Order_Date_Str'] = df_clean['Order_Date'].dt.strftime('%Y-%m-%d')
    df_clean['Ship_Date_Str'] = df_clean['Ship_Date'].dt.strftime('%Y-%m-%d')
    df_clean['Order_Year'] = df_clean['Order_Date'].dt.year
    df_clean['Order_Quarter'] = 'Q' + df_clean['Order_Date'].dt.quarter.astype(str)
    df_clean['Order_Year_Month'] = df_clean['Order_Date'].dt.strftime('%Y-%m')
    df_clean['Profit_Margin_%'] = np.where(df_clean['Sales'] > 0, ((df_clean['Profit'] / df_clean['Sales']) * 100).round(2), 0.0)
    
    # Sort chronologically
    df_clean = df_clean.sort_values(by=['Order_Date', 'Order_ID']).reset_index(drop=True)
    
    # Save unified cleaned dataset
    df_clean.to_csv(cleaned_path, index=False)
    print(f"\nSaved cleaned enterprise business dataset to: {cleaned_path}")
    
    # -------------------------------------------------------------
    # 5. GENERATE POWER BI STAR SCHEMA TABLES
    # -------------------------------------------------------------
    print("\n[Step 5] Building Star Schema Relational Tables for Power BI...")
    
    # Table 1: Dim_Geography
    df_geo = df_clean[['City', 'State', 'Country', 'Region', 'Market']].drop_duplicates().reset_index(drop=True)
    df_geo['Geography_ID'] = [f"GEO-{100 + i}" for i in range(len(df_geo))]
    geo_path = os.path.join(data_dir, "Dim_Geography.csv")
    df_geo.to_csv(geo_path, index=False)
    print(f"         Exported Dim_Geography: {len(df_geo)} records.")
    
    # Merge Geography_ID back into clean data
    df_clean = pd.merge(df_clean, df_geo, on=['City', 'State', 'Country', 'Region', 'Market'], how='left')
    
    # Table 2: Dim_Customers
    df_cust = df_clean[['Customer_ID', 'Customer_Name', 'Segment']].drop_duplicates(subset=['Customer_ID']).reset_index(drop=True)
    cust_path = os.path.join(data_dir, "Dim_Customers.csv")
    df_cust.to_csv(cust_path, index=False)
    print(f"         Exported Dim_Customers: {len(df_cust)} records.")
    
    # Table 3: Dim_Products
    df_prod = df_clean[['Product_ID', 'Product_Name', 'Category', 'Sub_Category']].drop_duplicates(subset=['Product_ID']).reset_index(drop=True)
    prod_path = os.path.join(data_dir, "Dim_Products.csv")
    df_prod.to_csv(prod_path, index=False)
    print(f"         Exported Dim_Products: {len(df_prod)} records.")
    
    # Table 4: Dim_Date
    start_cal = datetime(2022, 1, 1)
    end_cal = datetime(2024, 12, 31)
    date_range = pd.date_range(start_cal, end_cal)
    
    dim_date = pd.DataFrame({'Date': date_range})
    dim_date['Date_Key'] = dim_date['Date'].dt.strftime('%Y-%m-%d')
    dim_date['Year'] = dim_date['Date'].dt.year
    dim_date['Quarter'] = 'Q' + dim_date['Date'].dt.quarter.astype(str)
    dim_date['Quarter_Year'] = dim_date['Quarter'] + ' ' + dim_date['Year'].astype(str)
    dim_date['Month_Number'] = dim_date['Date'].dt.month
    dim_date['Month_Name'] = dim_date['Date'].dt.strftime('%b')
    dim_date['Month_Year'] = dim_date['Date'].dt.strftime('%b %Y')
    dim_date['Year_Month_Sort'] = dim_date['Date'].dt.strftime('%Y%m').astype(int)
    dim_date['Day_of_Week'] = dim_date['Date'].dt.day_name()
    dim_date['Is_Weekend'] = dim_date['Date'].dt.dayofweek.isin([5, 6]).astype(int)
    dim_date['Fiscal_Year'] = 'FY' + dim_date['Year'].astype(str)
    dim_date['Fiscal_Quarter'] = 'FQ' + dim_date['Date'].dt.quarter.astype(str)
    
    date_path = os.path.join(data_dir, "Dim_Date.csv")
    dim_date.to_csv(date_path, index=False)
    print(f"         Exported Dim_Date: {len(dim_date)} continuous calendar days.")
    
    # Table 5: Fact_Orders
    fact_cols = [
        'Order_ID', 'Order_Date_Str', 'Ship_Date_Str', 'Ship_Mode',
        'Customer_ID', 'Product_ID', 'Geography_ID',
        'Sales', 'Quantity', 'Discount', 'Profit', 'Shipping_Cost',
        'Returned', 'Delivery_Days', 'On_Time_Flag'
    ]
    df_fact = df_clean[fact_cols].copy()
    df_fact.rename(columns={'Order_Date_Str': 'Order_Date', 'Ship_Date_Str': 'Ship_Date'}, inplace=True)
    fact_path = os.path.join(data_dir, "Fact_Orders.csv")
    df_fact.to_csv(fact_path, index=False)
    print(f"         Exported Fact_Orders: {len(df_fact)} transaction rows.")
    
    # Table 6: Fact_Targets (Budget Variance Analytics)
    # Generate realistic monthly sales and profit targets by Category and Region
    targets = []
    unique_months = df_clean['Order_Year_Month'].unique()
    unique_cats = df_clean['Category'].unique()
    unique_regs = df_clean['Region'].unique()
    
    for ym in unique_months:
        dt_month = pd.to_datetime(ym + "-01")
        for cat in unique_cats:
            for reg in unique_regs:
                # Calculate actual for benchmark
                actual_sales = df_clean[
                    (df_clean['Order_Year_Month'] == ym) & 
                    (df_clean['Category'] == cat) & 
                    (df_clean['Region'] == reg)
                ]['Sales'].sum()
                
                # Base target around actual with slight variation (+/- 10%)
                target_sales = round(max(actual_sales * np.random.uniform(0.92, 1.12), 1500.0), 2)
                target_profit = round(target_sales * 0.40, 2)
                
                targets.append({
                    "Target_Month": ym + "-01",
                    "Year_Month": ym,
                    "Category": cat,
                    "Region": reg,
                    "Target_Sales": target_sales,
                    "Target_Profit": target_profit
                })
                
    df_targets = pd.DataFrame(targets)
    targets_path = os.path.join(data_dir, "Fact_Targets.csv")
    df_targets.to_csv(targets_path, index=False)
    print(f"         Exported Fact_Targets: {len(df_targets)} monthly target records.")
    
    # -------------------------------------------------------------
    # 6. COMPUTE EXACT EXECUTIVE METRICS & AUDIT
    # -------------------------------------------------------------
    tot_sales = df_clean['Sales'].sum()
    tot_profit = df_clean['Profit'].sum()
    tot_orders = df_clean['Order_ID'].nunique()
    tot_qty = df_clean['Quantity'].sum()
    tot_margin = (tot_profit / tot_sales) * 100
    ontime_pct = (df_clean['On_Time_Flag'].sum() / len(df_clean)) * 100
    return_pct = (df_clean['Returned'].value_counts().get('Yes', 0) / len(df_clean)) * 100
    avg_delivery = df_clean['Delivery_Days'].mean()
    
    # Annual breakdown
    annual_summary = df_clean.groupby('Order_Year').agg(
        Total_Sales=('Sales', 'sum'),
        Total_Profit=('Profit', 'sum'),
        Orders=('Order_ID', 'nunique'),
        Units=('Quantity', 'sum')
    ).reset_index()
    annual_summary['Profit_Margin_%'] = ((annual_summary['Total_Profit'] / annual_summary['Total_Sales']) * 100).round(2)
    annual_summary['YoY_Sales_Growth_%'] = (annual_summary['Total_Sales'].pct_change() * 100).fillna(0).round(2)
    annual_summary.to_csv(os.path.join(reports_dir, "annual_executive_summary.csv"), index=False)
    
    print("\n--- EXECUTIVE METRIC BENCHMARKS ---")
    print(f"Total Portfolio Revenue (3-Year): ${tot_sales:,.2f}")
    print(f"Total Portfolio Profit:           ${tot_profit:,.2f}")
    print(f"Overall Profit Margin:            {tot_margin:.2f}%")
    print(f"Total Orders:                     {tot_orders:,}")
    print(f"On-Time Delivery Rate:            {ontime_pct:.2f}%")
    print(f"Overall Return Rate:              {return_pct:.2f}%")
    print(f"Average Order Fulfillment:        {avg_delivery:.1f} days")
    print(annual_summary.to_string(index=False))
    
    # -------------------------------------------------------------
    # 7. GENERATE HIGH-RESOLUTION DASHBOARD VISUAL RENDERS
    # -------------------------------------------------------------
    print("\nGenerating Executive Dashboard Page Visuals...")
    
    # Page 1 Visual: Executive Summary Dashboard
    fig = plt.figure(figsize=(16, 9), dpi=300)
    fig.patch.set_facecolor('#0B192C')
    
    gs = fig.add_gridspec(3, 3, height_ratios=[0.25, 0.9, 0.9], hspace=0.35, wspace=0.25)
    
    # Top KPI Banner
    ax_top = fig.add_subplot(gs[0, :])
    ax_top.axis('off')
    kpis_text = (
        f"GLOBAL ENTERPRISE OPERATIONS BI DASHBOARD\n"
        f"TOTAL SALES: ${tot_sales/1e6:.2f}M  |  TOTAL PROFIT: ${tot_profit/1e6:.2f}M  |  MARGIN: {tot_margin:.1f}%  |  ON-TIME DELIVERY: {ontime_pct:.1f}%  |  RETURN RATE: {return_pct:.1f}%"
    )
    ax_top.text(0.5, 0.5, kpis_text, ha='center', va='center', fontsize=13, fontweight='bold', color='#FFFFFF',
                bbox=dict(boxstyle='round,pad=0.8', facecolor='#1E3E62', edgecolor='#FF6500', linewidth=2))
                
    # Visual 1: YoY Monthly Revenue Trend
    ax1 = fig.add_subplot(gs[1, :2])
    ax1.set_facecolor('#1E3E62')
    df_ym = df_clean.groupby(['Order_Year_Month', 'Order_Year']).agg(Monthly_Sales=('Sales', 'sum')).reset_index()
    for yr, col in [(2022, '#94A3B8'), (2023, '#38BDF8'), (2024, '#FF6500')]:
        sub_yr = df_ym[df_ym['Order_Year'] == yr]
        ax1.plot(range(len(sub_yr)), sub_yr['Monthly_Sales'], marker='o', linewidth=2.5, label=f'{yr} Revenue', color=col)
    ax1.set_title('Monthly Revenue Trajectory by Fiscal Year', color='#FFFFFF', fontsize=11)
    ax1.set_ylabel('Sales ($)', color='#FFFFFF', fontweight='bold')
    ax1.set_xticks(range(12))
    ax1.set_xticklabels(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'], color='#FFFFFF')
    ax1.yaxis.set_major_formatter('${x:,.0f}')
    ax1.tick_params(colors='#FFFFFF')
    ax1.legend(facecolor='#0B192C', edgecolor='w', labelcolor='#FFFFFF')
    
    # Visual 2: Category Revenue Breakdown Donut
    ax2 = fig.add_subplot(gs[1, 2])
    ax2.set_facecolor('#0B192C')
    cat_sales = df_clean.groupby('Category')['Sales'].sum()
    wedges, texts, autotexts = ax2.pie(
        cat_sales, labels=cat_sales.index, autopct='%1.1f%%',
        startangle=140, colors=['#3B82F6', '#10B981', '#F59E0B'],
        wedgeprops=dict(width=0.4, edgecolor='#0B192C', linewidth=2)
    )
    plt.setp(texts, color='#FFFFFF', weight='bold')
    plt.setp(autotexts, color='#0B192C', weight='bold')
    ax2.set_title('Category Revenue Share', color='#FFFFFF', fontsize=11)
    
    # Visual 3: Regional Sales & Profit
    ax3 = fig.add_subplot(gs[2, :2])
    ax3.set_facecolor('#1E3E62')
    reg_perf = df_clean.groupby('Region').agg(Sales=('Sales', 'sum'), Profit=('Profit', 'sum')).reset_index().sort_values(by='Sales', ascending=False)
    x_idx = np.arange(len(reg_perf))
    ax3.bar(x_idx - 0.2, reg_perf['Sales'], width=0.4, label='Sales ($)', color='#2563EB')
    ax3.bar(x_idx + 0.2, reg_perf['Profit'], width=0.4, label='Profit ($)', color='#10B981')
    ax3.set_xticks(x_idx)
    ax3.set_xticklabels(reg_perf['Region'], color='#FFFFFF', rotation=30, ha='right')
    ax3.yaxis.set_major_formatter('${x:,.0f}')
    ax3.tick_params(colors='#FFFFFF')
    ax3.set_title('Regional Sales & Profit Comparison', color='#FFFFFF', fontsize=11)
    ax3.legend(facecolor='#0B192C', edgecolor='w', labelcolor='#FFFFFF')
    
    # Visual 4: Customer Segment Contribution
    ax4 = fig.add_subplot(gs[2, 2])
    ax4.set_facecolor('#1E3E62')
    seg_perf = df_clean.groupby('Segment')['Sales'].sum().sort_values()
    ax4.barh(seg_perf.index, seg_perf.values, color='#F97316', alpha=0.9)
    ax4.set_title('Customer Segment Performance', color='#FFFFFF', fontsize=11)
    ax4.xaxis.set_major_formatter('${x:,.0f}')
    ax4.tick_params(colors='#FFFFFF')
    for i, v in enumerate(seg_perf.values):
        ax4.text(v * 0.5, i, f"${v/1000:,.0f}k", color='#FFFFFF', fontweight='bold', va='center')
        
    dashboard_render_path = os.path.join(dashboard_dir, "PowerBI_Executive_Dashboard_Render.png")
    fig.savefig(dashboard_render_path, dpi=300, facecolor=fig.get_facecolor(), edgecolor='none')
    fig.savefig(os.path.join(charts_dir, "executive_overview_page.png"), dpi=300, facecolor=fig.get_facecolor(), edgecolor='none')
    plt.close()
    
    # Page 2 Visual: Logistics & Operational SLA Dashboard
    fig2, (ax_s1, ax_s2) = plt.subplots(1, 2, figsize=(14, 6), dpi=300)
    fig2.patch.set_facecolor('#0B192C')
    
    # Ship Mode Delivery Days vs On-Time %
    ship_summary = df_clean.groupby('Ship_Mode').agg(
        Avg_Days=('Delivery_Days', 'mean'),
        OnTime_Pct=('On_Time_Flag', lambda x: (x.sum()/len(x))*100),
        Orders=('Order_ID', 'count')
    ).reset_index()
    
    ax_s1.set_facecolor('#1E3E62')
    b_days = ax_s1.bar(ship_summary['Ship_Mode'], ship_summary['Avg_Days'], color='#38BDF8', width=0.5)
    ax_s1.set_title('Average Delivery Duration by Shipping Mode (Days)', color='#FFFFFF', fontsize=12)
    ax_s1.set_ylabel('Days', color='#FFFFFF', fontweight='bold')
    ax_s1.tick_params(colors='#FFFFFF')
    for b in b_days:
        h = b.get_height()
        ax_s1.annotate(f'{h:.1f}d', xy=(b.get_x() + b.get_width()/2, h), xytext=(0, 3),
                       textcoords="offset points", ha='center', va='bottom', color='#FFFFFF', fontweight='bold')
                       
    ax_s2.set_facecolor('#1E3E62')
    b_ot = ax_s2.bar(ship_summary['Ship_Mode'], ship_summary['OnTime_Pct'], color='#10B981', width=0.5)
    ax_s2.set_title('On-Time Delivery SLA Compliance Rate (%)', color='#FFFFFF', fontsize=12)
    ax_s2.set_ylabel('Compliance %', color='#FFFFFF', fontweight='bold')
    ax_s2.yaxis.set_major_formatter('{x:.0f}%')
    ax_s2.set_ylim(0, 115)
    ax_s2.tick_params(colors='#FFFFFF')
    for b in b_ot:
        h = b.get_height()
        ax_s2.annotate(f'{h:.1f}%', xy=(b.get_x() + b.get_width()/2, h), xytext=(0, 3),
                       textcoords="offset points", ha='center', va='bottom', color='#FFFFFF', fontweight='bold')
                       
    plt.tight_layout()
    fig2.savefig(os.path.join(charts_dir, "logistics_sla_compliance.png"), dpi=300, facecolor=fig2.get_facecolor(), edgecolor='none')
    plt.close()
    
    print(f"Executive Power BI dashboard visual renders saved to: {dashboard_dir} and {charts_dir}")
    print("=" * 60)
    print("ENTERPRISE DATA TRANSFORMATION COMPLETED SUCCESSFULLY")
    print("=" * 60)

if __name__ == "__main__":
    base_p = r"C:\Users\keert\.gemini\antigravity-ide\scratch\ShadowFox_Data_Analyst_Internship\Advanced_PowerBI_Dashboard"
    transform_enterprise_data(base_p)
