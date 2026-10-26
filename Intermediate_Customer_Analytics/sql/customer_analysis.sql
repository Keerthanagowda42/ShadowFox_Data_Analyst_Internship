-- ==============================================================================
-- ShadowFox Data Analyst Internship - Project 2: Intermediate Level
-- SQL Script: customer_analysis.sql
-- Topic: Customer Behaviour, Revenue, and Retention Analytics
-- Database Engine: SQLite / ANSI SQL-99 Compatible
-- ==============================================================================

-- ------------------------------------------------------------------------------
-- 1. DATABASE SCHEMA DEFINITION (DDL)
-- ------------------------------------------------------------------------------

DROP TABLE IF EXISTS transactions;
DROP TABLE IF EXISTS customers;
DROP TABLE IF EXISTS products;

-- Customers Dimension Table
CREATE TABLE customers (
    customer_id VARCHAR(20) PRIMARY KEY,
    customer_name VARCHAR(100) NOT NULL,
    customer_email VARCHAR(150),
    customer_region VARCHAR(50),
    acquisition_channel VARCHAR(50)
);

-- Products Dimension Table
CREATE TABLE products (
    product_id VARCHAR(20) PRIMARY KEY,
    product_name VARCHAR(150) NOT NULL,
    product_category VARCHAR(50),
    unit_price DECIMAL(10, 2)
);

-- Transactions Fact Table
CREATE TABLE transactions (
    transaction_id VARCHAR(20) PRIMARY KEY,
    customer_id VARCHAR(20),
    product_id VARCHAR(20),
    transaction_date DATE NOT NULL,
    quantity INTEGER NOT NULL,
    unit_price DECIMAL(10, 2) NOT NULL,
    discount_amount DECIMAL(10, 2) DEFAULT 0.00,
    total_spend DECIMAL(10, 2) NOT NULL,
    payment_method VARCHAR(50),
    FOREIGN KEY (customer_id) REFERENCES customers (customer_id),
    FOREIGN KEY (product_id) REFERENCES products (product_id)
);

-- ------------------------------------------------------------------------------
-- 2. BUSINESS QUESTIONS & ANALYTICAL SQL QUERIES
-- ------------------------------------------------------------------------------

-- ------------------------------------------------------------------------------
-- Business Question 1:
-- Which product categories generate the highest total revenue, units sold,
-- and average discount? Filter out categories generating under $20,000.
-- Concepts: SELECT, SUM, AVG, GROUP BY, HAVING, ORDER BY
-- ------------------------------------------------------------------------------
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


-- ------------------------------------------------------------------------------
-- Business Question 2:
-- Which customer acquisition channels drive the most revenue and highest 
-- Average Order Value (AOV)?
-- Concepts: INNER JOIN, Multi-table Aggregation, Derived Metric
-- ------------------------------------------------------------------------------
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


-- ------------------------------------------------------------------------------
-- Business Question 3:
-- What is the exact breakdown between Repeat Customers (>1 order) vs 
-- One-Time Customers in terms of head count, total revenue, and average spend?
-- Concepts: Common Table Expressions (CTE), CASE WHEN, Aggregations
-- ------------------------------------------------------------------------------
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


-- ------------------------------------------------------------------------------
-- Business Question 4:
-- Who are the Top 10 High-Value VIP customers across the business,
-- what is their total spend, order count, and primary region?
-- Concepts: JOIN, GROUP BY, ORDER BY, LIMIT
-- ------------------------------------------------------------------------------
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


-- ------------------------------------------------------------------------------
-- Business Question 5:
-- Rank the top 3 highest-spending customers within EACH geographic region.
-- Concepts: Window Function (DENSE_RANK() OVER PARTITION BY)
-- ------------------------------------------------------------------------------
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


-- ------------------------------------------------------------------------------
-- Business Question 6:
-- What is the Month-over-Month (MoM) revenue trajectory and growth percentage
-- across the entire 24-month study period?
-- Concepts: CTE, Date Formatting, Window Function (LAG() OVER ORDER BY)
-- ------------------------------------------------------------------------------
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


-- ------------------------------------------------------------------------------
-- Business Question 7:
-- Calculate the cumulative running total revenue generated month-by-month.
-- Concepts: Window Function (SUM() OVER ORDER BY ROWS UNBOUNDED PRECEDING)
-- ------------------------------------------------------------------------------
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


-- ------------------------------------------------------------------------------
-- Business Question 8:
-- Customer Churn & Recency Risk: Calculate the days since last purchase for
-- each customer relative to study cutoff ('2025-01-01') and categorize their status.
-- Concepts: MAX(date), JULIANDAY Date Arithmetic, CASE WHEN, GROUP BY
-- ------------------------------------------------------------------------------
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


-- ------------------------------------------------------------------------------
-- Business Question 9:
-- Segment customers into 5 Monetary tiers using NTILE(5) for VIP campaigns.
-- Concepts: Window Function NTILE(5), Subquery, Tier Aggregation
-- ------------------------------------------------------------------------------
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


-- ------------------------------------------------------------------------------
-- Business Question 10:
-- Order Sequence Tracking: Identify each transaction's chronological sequence
-- number per customer and flag first-time orders vs subsequent re-orders.
-- Concepts: Window Function (ROW_NUMBER() OVER PARTITION BY ORDER BY)
-- ------------------------------------------------------------------------------
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
