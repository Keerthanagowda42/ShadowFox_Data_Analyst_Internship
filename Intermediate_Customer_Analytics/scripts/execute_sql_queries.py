"""
Intermediate Customer Analytics
Script: execute_sql_queries.py
Author: ShadowFox Data Analyst Intern
Objective: Load cleaned customer data into an SQLite relational database,
           execute production SQL queries (CTEs, Window Functions, Aggregations),
           verify output correctness, and export SQL result tables to CSV.
"""

import os
import sqlite3
import pandas as pd

def run_sql_pipeline(base_dir):
    print("=" * 60)
    print("EXECUTING RELATIONAL SQL PIPELINE: PROJECT 2")
    print("=" * 60)
    
    data_dir = os.path.join(base_dir, "data")
    sql_dir = os.path.join(base_dir, "sql")
    reports_dir = os.path.join(base_dir, "reports")
    os.makedirs(reports_dir, exist_ok=True)
    
    db_path = os.path.join(data_dir, "customer_analytics.db")
    cleaned_csv = os.path.join(data_dir, "cleaned_customer_data.csv")
    
    df_clean = pd.read_csv(cleaned_csv)
    
    # Establish connection
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # 1. Populate Dimension: Customers
    df_customers = df_clean[[
        'Customer_ID', 'Customer_Name', 'Customer_Email', 'Customer_Region', 'Acquisition_Channel'
    ]].drop_duplicates(subset=['Customer_ID']).copy()
    df_customers.columns = ['customer_id', 'customer_name', 'customer_email', 'customer_region', 'acquisition_channel']
    df_customers.to_sql('customers', conn, if_exists='replace', index=False)
    print(f"Loaded 'customers' dimension table: {len(df_customers)} records.")
    
    # 2. Populate Dimension: Products
    df_products = df_clean[[
        'Product_ID', 'Product_Name', 'Product_Category', 'Unit_Price'
    ]].drop_duplicates(subset=['Product_ID']).copy()
    df_products.columns = ['product_id', 'product_name', 'product_category', 'unit_price']
    df_products.to_sql('products', conn, if_exists='replace', index=False)
    print(f"Loaded 'products' dimension table: {len(df_products)} records.")
    
    # 3. Populate Fact: Transactions
    df_txns = df_clean[[
        'Transaction_ID', 'Customer_ID', 'Product_ID', 'Transaction_Date_Str',
        'Quantity', 'Unit_Price', 'Discount_Amount', 'Total_Spend', 'Payment_Method'
    ]].copy()
    df_txns.columns = [
        'transaction_id', 'customer_id', 'product_id', 'transaction_date',
        'quantity', 'unit_price', 'discount_amount', 'total_spend', 'payment_method'
    ]
    df_txns.to_sql('transactions', conn, if_exists='replace', index=False)
    print(f"Loaded 'transactions' fact table: {len(df_txns)} records.")
    
    # -------------------------------------------------------------
    # 4. EXECUTE & EXPORT INDIVIDUAL SQL QUERIES
    # -------------------------------------------------------------
    
    queries = {
        "sql_q1_category_revenue": """
            SELECT 
                p.product_category,
                COUNT(t.transaction_id) AS total_transactions,
                SUM(t.quantity) AS total_units_sold,
                ROUND(SUM(t.total_spend), 2) AS category_revenue,
                ROUND(AVG(t.discount_amount), 2) AS avg_discount_given,
                ROUND((SUM(t.total_spend) * 100.0 / (SELECT SUM(total_spend) FROM transactions)), 2) AS revenue_share_pct
            FROM transactions t
            JOIN products p ON t.product_id = p.product_id
            GROUP BY p.product_category
            HAVING SUM(t.total_spend) >= 20000.00
            ORDER BY category_revenue DESC;
        """,
        "sql_q2_acquisition_channels": """
            SELECT 
                c.acquisition_channel,
                COUNT(DISTINCT c.customer_id) AS acquired_customers,
                COUNT(t.transaction_id) AS total_orders,
                ROUND(SUM(t.total_spend), 2) AS total_channel_revenue,
                ROUND(SUM(t.total_spend) / COUNT(t.transaction_id), 2) AS avg_order_value,
                ROUND(SUM(t.total_spend) / COUNT(DISTINCT c.customer_id), 2) AS revenue_per_customer
            FROM customers c
            JOIN transactions t ON c.customer_id = t.customer_id
            GROUP BY c.acquisition_channel
            ORDER BY total_channel_revenue DESC;
        """,
        "sql_q3_repeat_vs_onetime": """
            WITH CustomerOrderStats AS (
                SELECT 
                    customer_id,
                    COUNT(transaction_id) AS total_orders,
                    SUM(total_spend) AS total_customer_spend
                FROM transactions
                GROUP BY customer_id
            )
            SELECT 
                CASE 
                    WHEN total_orders > 1 THEN 'Repeat Customer'
                    ELSE 'One-Time Customer'
                END AS customer_archetype,
                COUNT(customer_id) AS customer_count,
                ROUND(COUNT(customer_id) * 100.0 / (SELECT COUNT(*) FROM CustomerOrderStats), 2) AS customer_share_pct,
                ROUND(SUM(total_customer_spend), 2) AS archetype_revenue,
                ROUND(SUM(total_customer_spend) * 100.0 / (SELECT SUM(total_spend) FROM transactions), 2) AS revenue_share_pct,
                ROUND(AVG(total_customer_spend), 2) AS avg_spend_per_customer
            FROM CustomerOrderStats
            GROUP BY 
                CASE 
                    WHEN total_orders > 1 THEN 'Repeat Customer'
                    ELSE 'One-Time Customer'
                END;
        """,
        "sql_q4_top_10_vip_customers": """
            SELECT 
                c.customer_id,
                c.customer_name,
                c.customer_region,
                c.acquisition_channel,
                COUNT(t.transaction_id) AS total_orders,
                SUM(t.quantity) AS total_units_bought,
                ROUND(SUM(t.total_spend), 2) AS lifetime_spend,
                ROUND(AVG(t.total_spend), 2) AS avg_spend_per_order
            FROM customers c
            JOIN transactions t ON c.customer_id = t.customer_id
            GROUP BY c.customer_id, c.customer_name, c.customer_region, c.acquisition_channel
            ORDER BY lifetime_spend DESC
            LIMIT 10;
        """,
        "sql_q5_top_3_customers_per_region": """
            WITH RegionalCustomerSpend AS (
                SELECT 
                    c.customer_region,
                    c.customer_id,
                    c.customer_name,
                    ROUND(SUM(t.total_spend), 2) AS total_regional_spend,
                    COUNT(t.transaction_id) AS total_orders,
                    DENSE_RANK() OVER (
                        PARTITION BY c.customer_region 
                        ORDER BY SUM(t.total_spend) DESC
                    ) AS regional_rank
                FROM customers c
                JOIN transactions t ON c.customer_id = t.customer_id
                GROUP BY c.customer_region, c.customer_id, c.customer_name
            )
            SELECT 
                customer_region,
                regional_rank,
                customer_id,
                customer_name,
                total_regional_spend,
                total_orders
            FROM RegionalCustomerSpend
            WHERE regional_rank <= 3
            ORDER BY customer_region, regional_rank;
        """,
        "sql_q6_mom_revenue_growth": """
            WITH MonthlySales AS (
                SELECT 
                    strftime('%Y-%m', transaction_date) AS sales_month,
                    COUNT(transaction_id) AS monthly_orders,
                    ROUND(SUM(total_spend), 2) AS monthly_revenue
                FROM transactions
                GROUP BY strftime('%Y-%m', transaction_date)
            )
            SELECT 
                sales_month,
                monthly_orders,
                monthly_revenue,
                LAG(monthly_revenue, 1) OVER (ORDER BY sales_month) AS previous_month_revenue,
                ROUND(
                    (monthly_revenue - LAG(monthly_revenue, 1) OVER (ORDER BY sales_month)) * 100.0 / 
                    LAG(monthly_revenue, 1) OVER (ORDER BY sales_month), 
                    2
                ) AS mom_revenue_growth_pct
            FROM MonthlySales
            ORDER BY sales_month;
        """,
        "sql_q7_cumulative_running_revenue": """
            WITH MonthlyAggregate AS (
                SELECT 
                    strftime('%Y-%m', transaction_date) AS sales_month,
                    ROUND(SUM(total_spend), 2) AS monthly_revenue
                FROM transactions
                GROUP BY strftime('%Y-%m', transaction_date)
            )
            SELECT 
                sales_month,
                monthly_revenue,
                ROUND(
                    SUM(monthly_revenue) OVER (
                        ORDER BY sales_month 
                        ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
                    ), 
                    2
                ) AS cumulative_running_revenue
            FROM MonthlyAggregate
            ORDER BY sales_month;
        """,
        "sql_q8_customer_churn_recency": """
            WITH CustomerRecency AS (
                SELECT 
                    c.customer_id,
                    c.customer_name,
                    c.customer_region,
                    MAX(t.transaction_date) AS last_purchase_date,
                    CAST(ROUND(JULIANDAY('2025-01-01') - JULIANDAY(MAX(t.transaction_date))) AS INTEGER) AS days_since_last_purchase,
                    COUNT(t.transaction_id) AS total_orders,
                    ROUND(SUM(t.total_spend), 2) AS lifetime_value
                FROM customers c
                JOIN transactions t ON c.customer_id = t.customer_id
                GROUP BY c.customer_id, c.customer_name, c.customer_region
            )
            SELECT 
                CASE 
                    WHEN days_since_last_purchase <= 90 THEN 'Active (0-90 Days)'
                    WHEN days_since_last_purchase <= 180 THEN 'Warm (91-180 Days)'
                    WHEN days_since_last_purchase <= 365 THEN 'Cooling Off (181-365 Days)'
                    ELSE 'Churned / Dormant (>365 Days)'
                END AS retention_status,
                COUNT(customer_id) AS customer_count,
                ROUND(COUNT(customer_id) * 100.0 / (SELECT COUNT(*) FROM CustomerRecency), 2) AS pct_of_customers,
                ROUND(SUM(lifetime_value), 2) AS total_segment_value,
                ROUND(AVG(lifetime_value), 2) AS avg_customer_value
            FROM CustomerRecency
            GROUP BY 
                CASE 
                    WHEN days_since_last_purchase <= 90 THEN 'Active (0-90 Days)'
                    WHEN days_since_last_purchase <= 180 THEN 'Warm (91-180 Days)'
                    WHEN days_since_last_purchase <= 365 THEN 'Cooling Off (181-365 Days)'
                    ELSE 'Churned / Dormant (>365 Days)'
                END
            ORDER BY total_segment_value DESC;
        """,
        "sql_q9_monetary_quintiles_ntile": """
            WITH CustomerSpendQuintiles AS (
                SELECT 
                    customer_id,
                    ROUND(SUM(total_spend), 2) AS customer_spend,
                    NTILE(5) OVER (ORDER BY SUM(total_spend) DESC) AS spend_quintile
                FROM transactions
                GROUP BY customer_id
            )
            SELECT 
                spend_quintile AS tier_rank,
                CASE 
                    WHEN spend_quintile = 1 THEN 'Tier 1: Top 20% Spenders (Platinum VIP)'
                    WHEN spend_quintile = 2 THEN 'Tier 2: High Spenders (Gold)'
                    WHEN spend_quintile = 3 THEN 'Tier 3: Moderate Spenders (Silver)'
                    WHEN spend_quintile = 4 THEN 'Tier 4: Low Spenders (Bronze)'
                    ELSE 'Tier 5: Minimum Spenders (Entry)'
                END AS spend_tier_name,
                COUNT(customer_id) AS customer_count,
                ROUND(SUM(customer_spend), 2) AS tier_total_revenue,
                ROUND(MIN(customer_spend), 2) AS min_tier_spend,
                ROUND(MAX(customer_spend), 2) AS max_tier_spend,
                ROUND(AVG(customer_spend), 2) AS avg_tier_spend
            FROM CustomerSpendQuintiles
            GROUP BY spend_quintile
            ORDER BY spend_quintile;
        """,
        "sql_q10_purchase_stage_progression": """
            WITH OrderSequences AS (
                SELECT 
                    transaction_id,
                    customer_id,
                    transaction_date,
                    total_spend,
                    ROW_NUMBER() OVER (
                        PARTITION BY customer_id 
                        ORDER BY transaction_date, transaction_id
                    ) AS order_sequence_number
                FROM transactions
            )
            SELECT 
                CASE 
                    WHEN order_sequence_number = 1 THEN 'First Order (Acquisition)'
                    WHEN order_sequence_number = 2 THEN 'Second Order (First Repeat)'
                    WHEN order_sequence_number BETWEEN 3 AND 5 THEN 'Repeat Order (3-5)'
                    ELSE 'Loyalty Order (>5)'
                END AS purchase_stage,
                COUNT(transaction_id) AS transaction_count,
                ROUND(SUM(total_spend), 2) AS stage_revenue,
                ROUND(AVG(total_spend), 2) AS avg_order_size
            FROM OrderSequences
            GROUP BY 
                CASE 
                    WHEN order_sequence_number = 1 THEN 'First Order (Acquisition)'
                    WHEN order_sequence_number = 2 THEN 'Second Order (First Repeat)'
                    WHEN order_sequence_number BETWEEN 3 AND 5 THEN 'Repeat Order (3-5)'
                    ELSE 'Loyalty Order (>5)'
                END
            ORDER BY stage_revenue DESC;
        """
    }
    
    for q_name, q_sql in queries.items():
        res_df = pd.read_sql_query(q_sql, conn)
        out_file = os.path.join(reports_dir, f"{q_name}.csv")
        res_df.to_csv(out_file, index=False)
        print(f"Executed & Exported {q_name}: {len(res_df)} rows.")
        
    conn.close()
    print("=" * 60)
    print("ALL SQL QUERIES EXECUTED AND EXPORTED TO 'reports/'")
    print("=" * 60)

if __name__ == "__main__":
    base_dir = r"C:\Users\keert\.gemini\antigravity-ide\scratch\ShadowFox_Data_Analyst_Internship\Intermediate_Customer_Analytics"
    run_sql_pipeline(base_dir)
