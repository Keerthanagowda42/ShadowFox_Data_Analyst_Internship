"""
Intermediate Customer Analytics
Script: customer_analysis.py
Author: ShadowFox Data Analyst Intern
Objective: Perform RFM customer segmentation, cohort retention analysis,
           Pareto 80/20 analysis, repeat vs one-time customer behavior,
           and export visual charts and analytical summaries.
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

PRIMARY_COLOR = '#1E3E62'
SECONDARY_COLOR = '#0B192C'
ACCENT_COLOR = '#FF6500'

def run_customer_analytics(base_dir):
    data_dir = os.path.join(base_dir, "data")
    analysis_dir = os.path.join(base_dir, "analysis")
    charts_dir = os.path.join(base_dir, "charts")
    
    os.makedirs(analysis_dir, exist_ok=True)
    os.makedirs(charts_dir, exist_ok=True)
    
    cleaned_path = os.path.join(data_dir, "cleaned_customer_data.csv")
    df = pd.read_csv(cleaned_path)
    df['Transaction_Date'] = pd.to_datetime(df['Transaction_Date'])
    
    print("=" * 60)
    print("EXECUTING ADVANCED CUSTOMER BEHAVIOR & RFM ANALYTICS")
    print("=" * 60)
    
    total_revenue = df['Total_Spend'].sum()
    total_transactions = len(df)
    unique_customers = df['Customer_ID'].nunique()
    total_units = df['Quantity'].sum()
    avg_txn_value = total_revenue / total_transactions
    
    print(f"Total Portfolio Revenue: ${total_revenue:,.2f}")
    print(f"Total Transactions: {total_transactions:,}")
    print(f"Unique Customers: {unique_customers:,}")
    print(f"Average Transaction Value: ${avg_txn_value:,.2f}")
    
    # ---------------------------------------------------------
    # 1. REPEAT VS ONE-TIME CUSTOMER ANALYSIS
    # ---------------------------------------------------------
    cust_orders = df.groupby('Customer_ID').agg(
        Order_Count=('Transaction_ID', 'count'),
        Total_Customer_Spend=('Total_Spend', 'sum'),
        Customer_Name=('Customer_Name', 'first'),
        Customer_Region=('Customer_Region', 'first'),
        Acquisition_Channel=('Acquisition_Channel', 'first')
    ).reset_index()
    
    cust_orders['Customer_Type'] = np.where(cust_orders['Order_Count'] > 1, 'Repeat Customer', 'One-Time Customer')
    
    repeat_summary = cust_orders.groupby('Customer_Type').agg(
        Customer_Count=('Customer_ID', 'count'),
        Total_Revenue=('Total_Customer_Spend', 'sum'),
        Avg_Revenue_Per_Cust=('Total_Customer_Spend', 'mean')
    ).reset_index()
    
    repeat_summary['Customer_Share_%'] = (repeat_summary['Customer_Count'] / unique_customers * 100).round(2)
    repeat_summary['Revenue_Share_%'] = (repeat_summary['Total_Revenue'] / total_revenue * 100).round(2)
    repeat_summary['Avg_Revenue_Per_Cust'] = repeat_summary['Avg_Revenue_Per_Cust'].round(2)
    
    print("\n--- REPEAT VS ONE-TIME CUSTOMERS ---")
    print(repeat_summary.to_string(index=False))
    repeat_summary.to_csv(os.path.join(analysis_dir, "repeat_vs_onetime_summary.csv"), index=False)
    
    # ---------------------------------------------------------
    # 2. RFM (RECENCY, FREQUENCY, MONETARY) SEGMENTATION
    # ---------------------------------------------------------
    # Reference snapshot date for Recency: day after latest transaction in dataset
    snapshot_date = df['Transaction_Date'].max() + pd.Timedelta(days=1)
    
    rfm = df.groupby('Customer_ID').agg(
        Recency_Days=('Transaction_Date', lambda x: (snapshot_date - x.max()).days),
        Frequency=('Transaction_ID', 'count'),
        Monetary_Value=('Total_Spend', 'sum'),
        Customer_Name=('Customer_Name', 'first'),
        Customer_Email=('Customer_Email', 'first'),
        Customer_Region=('Customer_Region', 'first'),
        Acquisition_Channel=('Acquisition_Channel', 'first'),
        First_Purchase=('Transaction_Date', 'min'),
        Last_Purchase=('Transaction_Date', 'max')
    ).reset_index()
    
    # Scoring (1-5 quintiles). For Recency, lower days = higher score
    rfm['R_Score'] = pd.qcut(rfm['Recency_Days'], q=5, labels=[5, 4, 3, 2, 1]).astype(int)
    
    # Frequency can have ties, so use rank(method='first') or custom bins
    rfm['F_Score'] = pd.qcut(rfm['Frequency'].rank(method='first'), q=5, labels=[1, 2, 3, 4, 5]).astype(int)
    rfm['M_Score'] = pd.qcut(rfm['Monetary_Value'].rank(method='first'), q=5, labels=[1, 2, 3, 4, 5]).astype(int)
    
    rfm['RFM_Score'] = rfm['R_Score'].astype(str) + rfm['F_Score'].astype(str) + rfm['M_Score'].astype(str)
    
    # Customer Segment mapping based on R and F scores
    def assign_segment(row):
        r = row['R_Score']
        f = row['F_Score']
        m = row['M_Score']
        
        if r >= 4 and f >= 4:
            return 'Champions'
        elif (r >= 3 and f >= 3) or (f >= 4 and m >= 4):
            return 'Loyal Customers'
        elif r >= 4 and f <= 2:
            return 'New / Promising'
        elif r >= 3 and f == 2:
            return 'Potential Loyalists'
        elif r <= 2 and f >= 4:
            return 'At Risk Spenders'
        elif r <= 2 and f >= 2:
            return 'Needs Attention'
        elif r == 1 and f == 1:
            return 'Lost / Churned'
        else:
            return 'Hibernating'
            
    rfm['Customer_Segment'] = rfm.apply(assign_segment, axis=1)
    
    # Export RFM customer segments
    rfm_export_path = os.path.join(data_dir, "customer_segments.csv")
    rfm.to_csv(rfm_export_path, index=False)
    
    # Segment Summary
    segment_summary = rfm.groupby('Customer_Segment').agg(
        Customer_Count=('Customer_ID', 'count'),
        Total_Revenue=('Monetary_Value', 'sum'),
        Avg_Recency_Days=('Recency_Days', 'mean'),
        Avg_Frequency=('Frequency', 'mean'),
        Avg_Spend_Per_Customer=('Monetary_Value', 'mean')
    ).reset_index()
    
    segment_summary['Customer_Share_%'] = (segment_summary['Customer_Count'] / unique_customers * 100).round(2)
    segment_summary['Revenue_Share_%'] = (segment_summary['Total_Revenue'] / total_revenue * 100).round(2)
    segment_summary = segment_summary.sort_values(by='Total_Revenue', ascending=False)
    
    print("\n--- RFM SEGMENT PERFORMANCE ---")
    print(segment_summary.to_string(index=False))
    segment_summary.to_csv(os.path.join(analysis_dir, "rfm_segment_summary.csv"), index=False)
    
    # ---------------------------------------------------------
    # 3. PARETO 80/20 ANALYSIS
    # ---------------------------------------------------------
    rfm_sorted = rfm.sort_values(by='Monetary_Value', ascending=False).reset_index(drop=True)
    rfm_sorted['Cumulative_Spend'] = rfm_sorted['Monetary_Value'].cumsum()
    rfm_sorted['Cumulative_Revenue_%'] = (rfm_sorted['Cumulative_Spend'] / total_revenue) * 100
    rfm_sorted['Customer_Rank'] = rfm_sorted.index + 1
    rfm_sorted['Cumulative_Customer_%'] = (rfm_sorted['Customer_Rank'] / unique_customers) * 100
    
    # Top 20% customers revenue share
    top_20_pct_cust_count = int(np.ceil(unique_customers * 0.20))
    top_20_pct_rev_share = rfm_sorted.loc[top_20_pct_cust_count - 1, 'Cumulative_Revenue_%']
    print(f"\nPareto Insight: Top 20% of customers generate {top_20_pct_rev_share:.2f}% of total revenue!")
    
    # ---------------------------------------------------------
    # 4. MONTHLY COHORT RETENTION ANALYSIS
    # ---------------------------------------------------------
    # Group by Cohort Month and Cohort Index
    cohort_data = df.groupby(['Cohort_Month', 'Cohort_Index'])['Customer_ID'].nunique().reset_index()
    cohort_pivot = cohort_data.pivot(index='Cohort_Month', columns='Cohort_Index', values='Customer_ID')
    
    # Calculate Retention Percentage relative to Cohort Size (Month 0)
    cohort_sizes = cohort_pivot.iloc[:, 0]
    retention_matrix = cohort_pivot.divide(cohort_sizes, axis=0) * 100
    
    cohort_pivot.to_csv(os.path.join(analysis_dir, "cohort_customer_counts.csv"))
    retention_matrix.to_csv(os.path.join(analysis_dir, "cohort_retention_matrix.csv"))
    
    # ---------------------------------------------------------
    # 5. CHANNEL, CATEGORY & REGIONAL REVENUE BREAKDOWNS
    # ---------------------------------------------------------
    df_channel = df.groupby('Acquisition_Channel').agg(
        Total_Revenue=('Total_Spend', 'sum'),
        Unique_Customers=('Customer_ID', 'nunique'),
        Transactions=('Transaction_ID', 'count')
    ).reset_index()
    df_channel['Revenue_Share_%'] = (df_channel['Total_Revenue'] / total_revenue * 100).round(2)
    df_channel['AOV'] = (df_channel['Total_Revenue'] / df_channel['Transactions']).round(2)
    df_channel = df_channel.sort_values(by='Total_Revenue', ascending=False)
    df_channel.to_csv(os.path.join(analysis_dir, "channel_performance_summary.csv"), index=False)
    
    df_cat = df.groupby('Product_Category').agg(
        Total_Revenue=('Total_Spend', 'sum'),
        Units_Sold=('Quantity', 'sum'),
        Transactions=('Transaction_ID', 'count')
    ).reset_index()
    df_cat['Revenue_Share_%'] = (df_cat['Total_Revenue'] / total_revenue * 100).round(2)
    df_cat = df_cat.sort_values(by='Total_Revenue', ascending=False)
    df_cat.to_csv(os.path.join(analysis_dir, "category_performance_summary.csv"), index=False)
    
    # Monthly Revenue Trend
    df_monthly = df.groupby('Year_Month').agg(
        Revenue=('Total_Spend', 'sum'),
        Active_Customers=('Customer_ID', 'nunique'),
        Transactions=('Transaction_ID', 'count')
    ).reset_index()
    df_monthly.to_csv(os.path.join(analysis_dir, "monthly_revenue_summary.csv"), index=False)
    
    # ---------------------------------------------------------
    # 6. VISUALIZATION GENERATION
    # ---------------------------------------------------------
    print("\nGenerating charts for Customer Analytics...")
    
    # Chart 1: RFM Segments Distribution (Customers vs Revenue)
    fig, ax1 = plt.subplots(figsize=(12, 6), dpi=300)
    ax2 = ax1.twinx()
    
    seg_sorted = segment_summary.sort_values(by='Total_Revenue', ascending=True)
    y_pos = np.arange(len(seg_sorted))
    
    b1 = ax1.barh(y_pos - 0.2, seg_sorted['Total_Revenue'], height=0.38, color=PRIMARY_COLOR, label='Total Revenue ($)', alpha=0.9)
    b2 = ax2.barh(y_pos + 0.2, seg_sorted['Customer_Count'], height=0.38, color=ACCENT_COLOR, label='Customer Count', alpha=0.9)
    
    ax1.set_yticks(y_pos)
    ax1.set_yticklabels(seg_sorted['Customer_Segment'], fontweight='bold')
    ax1.xaxis.set_major_formatter('${x:,.0f}')
    ax1.set_xlabel('Total Revenue Generated ($)', fontweight='bold', color=PRIMARY_COLOR)
    ax2.set_xlabel('Number of Customers', fontweight='bold', color=ACCENT_COLOR)
    ax1.set_title('Customer Segmentation (RFM): Revenue Contribution vs Customer Base', fontsize=14, pad=15)
    ax2.grid(False)
    
    fig.legend(loc='lower right', bbox_to_anchor=(0.95, 0.15), frameon=True)
    plt.tight_layout()
    fig.savefig(os.path.join(charts_dir, "rfm_segments_distribution.png"), dpi=300)
    plt.close()
    
    # Chart 2: Cohort Retention Heatmap
    # Filter for first 12 cohorts and 10 months for clean visualization
    viz_retention = retention_matrix.iloc[:12, :10]
    
    fig, ax = plt.subplots(figsize=(13, 7), dpi=300)
    sns.heatmap(
        viz_retention,
        annot=True,
        fmt='.1f',
        cmap='Blues',
        linewidths=0.5,
        cbar_kws={'label': 'Retention Rate (%)'},
        ax=ax
    )
    ax.set_title('Customer Cohort Monthly Retention Rate (%) [2023 - 2024]', fontsize=14, pad=15)
    ax.set_xlabel('Months Since Customer Acquisition (Cohort Index)', fontweight='bold')
    ax.set_ylabel('Acquisition Cohort (Year-Month)', fontweight='bold')
    plt.tight_layout()
    fig.savefig(os.path.join(charts_dir, "cohort_retention_heatmap.png"), dpi=300)
    plt.close()
    
    # Chart 3: Pareto 80/20 Customer Curve
    fig, ax = plt.subplots(figsize=(10, 5.5), dpi=300)
    ax.plot(rfm_sorted['Cumulative_Customer_%'], rfm_sorted['Cumulative_Revenue_%'], color='#2563EB', linewidth=3, label='Lorenz Cumulative Curve')
    ax.plot([0, 100], [0, 100], color='#94A3B8', linestyle='--', linewidth=1.5, label='Equal Distribution Baseline')
    
    # Mark 20% customer line
    ax.axvline(x=20, color='#DC2626', linestyle=':', linewidth=2)
    ax.axhline(y=top_20_pct_rev_share, color='#DC2626', linestyle=':', linewidth=2)
    ax.scatter([20], [top_20_pct_rev_share], color='#DC2626', s=80, zorder=5)
    ax.annotate(f'Top 20% Customers = {top_20_pct_rev_share:.1f}% Revenue',
                xy=(20, top_20_pct_rev_share), xytext=(28, top_20_pct_rev_share - 10),
                arrowprops=dict(facecolor='#DC2626', shrink=0.08, width=1.5, headwidth=6),
                fontweight='bold', fontsize=10, color='#DC2626')
                
    ax.set_title('Customer Concentration (Pareto 80/20 Cumulative Revenue)', fontsize=13, pad=15)
    ax.set_xlabel('Cumulative % of Total Customers', fontweight='bold')
    ax.set_ylabel('Cumulative % of Total Revenue', fontweight='bold')
    ax.yaxis.set_major_formatter('{x:.0f}%')
    ax.xaxis.set_major_formatter('{x:.0f}%')
    ax.legend(loc='lower right', frameon=True)
    plt.tight_layout()
    fig.savefig(os.path.join(charts_dir, "customer_revenue_pareto.png"), dpi=300)
    plt.close()
    
    # Chart 4: Repeat vs One-Time Customers Comparison
    fig, (ax_cust, ax_rev) = plt.subplots(1, 2, figsize=(12, 5), dpi=300)
    
    colors_pie = ['#3B82F6', '#F97316']
    
    ax_cust.pie(
        repeat_summary['Customer_Count'],
        labels=repeat_summary['Customer_Type'],
        autopct='%1.1f%%',
        startangle=120,
        colors=colors_pie,
        wedgeprops=dict(width=0.4, edgecolor='w', linewidth=2)
    )
    ax_cust.set_title('Customer Base Breakdown', fontweight='bold', fontsize=12)
    
    ax_rev.pie(
        repeat_summary['Total_Revenue'],
        labels=repeat_summary['Customer_Type'],
        autopct='%1.1f%%',
        startangle=120,
        colors=colors_pie,
        wedgeprops=dict(width=0.4, edgecolor='w', linewidth=2)
    )
    ax_rev.set_title('Revenue Contribution Breakdown', fontweight='bold', fontsize=12)
    
    fig.suptitle('Repeat Customers vs One-Time Buyers: Disproportionate Impact', fontsize=14, fontweight='bold')
    plt.tight_layout()
    fig.savefig(os.path.join(charts_dir, "repeat_vs_onetime_revenue.png"), dpi=300)
    plt.close()
    
    # Chart 5: 24-Month Revenue Trajectory
    fig, ax = plt.subplots(figsize=(12, 5), dpi=300)
    ax.plot(df_monthly['Year_Month'], df_monthly['Revenue'], marker='o', color='#0284C7', linewidth=2.5, markersize=6)
    ax.fill_between(df_monthly['Year_Month'], df_monthly['Revenue'], color='#BAE6FD', alpha=0.5)
    ax.set_title('24-Month E-Commerce Revenue Trajectory (2023 - 2024)', fontsize=13, pad=15)
    ax.set_xlabel('Year-Month', fontweight='bold')
    ax.set_ylabel('Total Revenue ($)', fontweight='bold')
    ax.yaxis.set_major_formatter('${x:,.0f}')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    fig.savefig(os.path.join(charts_dir, "monthly_revenue_trend.png"), dpi=300)
    plt.close()
    
    print("All charts successfully generated and saved to 'charts/' directory.")
    print("=" * 60)
    print("CUSTOMER ANALYTICS PIPELINE COMPLETED")
    print("=" * 60)

if __name__ == "__main__":
    base_p = r"C:\Users\keert\.gemini\antigravity-ide\scratch\ShadowFox_Data_Analyst_Internship\Intermediate_Customer_Analytics"
    run_customer_analytics(base_p)
