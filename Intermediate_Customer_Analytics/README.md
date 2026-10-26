# Customer Behaviour, Revenue, and Retention Analytics

**ShadowFox Data Analyst Internship — Project 2 (Intermediate Level)**  
**Author**: ShadowFox Data Analyst Intern  
**Tools**: Python 3.12, Pandas, NumPy, SQLite, SQL (Window Functions & CTEs), Matplotlib, Seaborn  
**Status**: Completed and Validated  

---

## 1. Project Title & Business Problem

### Project Title
Customer Behaviour, Revenue, and Retention Analytics

### Business Problem
A modern direct-to-consumer e-commerce brand has accumulated over 24 months of customer transaction data across five product categories and five marketing acquisition channels. The management team faces critical operational questions:
- What percentage of newly acquired customers return for repeat purchases versus dropping off after their initial order?
- How is revenue distributed across behavioral customer segments (RFM)?
- Are customer retention rates stabilizing over time or decaying across newer monthly cohorts?
- How can advanced SQL analytics (CTEs, Window Functions, and Ranking) identify high-value VIP buyers and customers at risk of churn?

### Objectives
1. Build an automated data cleaning and cohort transformation pipeline in Python.
2. Conduct RFM Segmentation (Recency, Frequency, Monetary) to classify 850 customers into 8 behavioral clusters.
3. Calculate monthly cohort retention heatmaps tracking customer persistence over 24 months.
4. Construct and execute 10 production-grade SQL queries in SQLite covering Window Functions (`ROW_NUMBER`, `DENSE_RANK`, `LAG`, `NTILE`, running totals) and Common Table Expressions (CTEs).
5. Generate high-resolution visual reports and actionable retention recommendations.

---

## 2. Dataset Description & Source

- **Dataset Type**: Multi-Year Omnichannel Customer Transaction Log (Jan 1, 2023 – Dec 31, 2024).
- **Source**: Structured realistic customer behavior and transaction log, synthesized for reproducible benchmarking with injected dirty data (duplicates, missing fields, mixed dates).
- **Key Fields**:
  - `Transaction_ID`: Unique order identifier (e.g., `TXN-10001`).
  - `Customer_ID`: Unique customer profile key (e.g., `CUST-1001` through `CUST-1850`).
  - `Customer_Name`, `Customer_Email`, `Customer_Region`, `Acquisition_Channel`.
  - `Transaction_Date`: Order date in mixed raw formats (`YYYY-MM-DD`, `MM/DD/YYYY`, `DD-MM-YYYY`).
  - `Product_ID`, `Product_Name`, `Product_Category`, `Unit_Price`.
  - `Quantity`, `Discount_Amount`, `Total_Spend`, `Payment_Method`.
  - `Cohort_Month` & `Cohort_Index`: Derived analytical fields for cohort retention.

---

## 3. Folder Structure

```
Intermediate_Customer_Analytics/
|-- data/
|   |-- raw_customer_data.csv          # 2,336 raw records with real-world flaws
|   |-- cleaned_customer_data.csv      # 2,306 verified unique transactions
|   |-- customer_segments.csv          # 850 scored customers with RFM categories
|   |-- customer_analytics.db          # Relational SQLite database
|
|-- scripts/
|   |-- generate_customer_data.py      # Reproducible raw data generator
|   |-- customer_cleaning.py           # Data audit, cleaning & cohort transformation
|   |-- customer_analysis.py           # RFM segmentation, cohort matrices & charts
|   |-- execute_sql_queries.py         # Relational SQLite executor & report exporter
|
|-- sql/
|   |-- customer_analysis.sql          # 10 production SQL queries (DDL, CTEs, Window Fns)
|
|-- analysis/
|   |-- data_cleaning_audit.md         # Data cleaning audit log
|   |-- repeat_vs_onetime_summary.csv  # Repeat vs one-time customer comparison
|   |-- rfm_segment_summary.csv        # Segment counts, revenue, and average metrics
|   |-- cohort_customer_counts.csv     # Raw customer counts by cohort and month index
|   |-- cohort_retention_matrix.csv    # Monthly retention percentages matrix
|   |-- channel_performance_summary.csv# Marketing acquisition performance
|   |-- category_performance_summary.csv# Category revenue and unit sales
|   |-- monthly_revenue_summary.csv    # 24-month revenue trajectory
|
|-- reports/
|   |-- business_insights.md           # Comprehensive analytical findings report
|   |-- recommendations.md             # Operational retention roadmap
|   |-- sql_q1_category_revenue.csv    # SQL Query 1 output
|   |-- sql_q2_acquisition_channels.csv# SQL Query 2 output
|   |-- sql_q3_repeat_vs_onetime.csv   # SQL Query 3 output
|   |-- sql_q4_top_10_vip_customers.csv# SQL Query 4 output
|   |-- sql_q5_top_3_customers_per_region.csv # SQL Query 5 output
|   |-- sql_q6_mom_revenue_growth.csv  # SQL Query 6 output
|   |-- sql_q7_cumulative_running_revenue.csv # SQL Query 7 output
|   |-- sql_q8_customer_churn_recency.csv # SQL Query 8 output
|   |-- sql_q9_monetary_quintiles_ntile.csv # SQL Query 9 output
|   |-- sql_q10_purchase_stage_progression.csv # SQL Query 10 output
|
|-- charts/
|   |-- rfm_segments_distribution.png  # Segment revenue vs customer head count
|   |-- cohort_retention_heatmap.png   # 24-month retention rate heatmap
|   |-- customer_revenue_pareto.png    # Lorenz curve (80/20 customer concentration)
|   |-- repeat_vs_onetime_revenue.png  # Pie chart comparison of repeat vs one-time
|   |-- monthly_revenue_trend.png      # 24-month revenue trajectory area chart
|
|-- README.md                          # Comprehensive project documentation
|-- requirements.txt                   # Library dependencies
```

---

## 4. Analytical Methodology & Business Questions

### 1. Repeat vs. One-Time Customer Analysis
- **Empirical Metric**:
  - Repeat Customers: **399 (46.94% of base)** generate **$264,508.51 (80.88% of revenue)** with average spend of **$662.93**.
  - One-Time Customers: **451 (53.06% of base)** generate **$62,545.03 (19.12% of revenue)** with average spend of **$138.68**.
- **Conclusion**: Repeat purchasers drive over 4x higher customer lifetime value.

### 2. RFM Segmentation Framework
- **Recency ($R$)**: Days since last order relative to study snapshot (`2025-01-01`).
- **Frequency ($F$)**: Total lifetime order transactions.
- **Monetary ($M$)**: Cumulative lifetime customer spend.
- **Scoring**: Customers are ranked and binned into quintiles ($1-5$).

| Segment Name | Customer Count | Revenue ($) | Share (%) | Avg. Spend ($) | Avg. Recency |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Champions** | 200 | $162,963.95 | 49.83% | $814.82 | 85 days |
| **Loyal Customers** | 210 | $96,739.15 | 29.58% | $460.66 | 285 days |
| **Needs Attention** | 172 | $29,087.88 | 8.89% | $169.12 | 551 days |
| **New / Promising** | 86 | $12,496.12 | 3.82% | $145.30 | 125 days |
| **Hibernating** | 85 | $10,380.91 | 3.17% | $122.13 | 373 days |
| **Lost / Churned** | 47 | $7,136.72 | 2.18% | $151.85 | 636 days |
| **Potential Loyalists**| 34 | $4,802.08 | 1.47% | $141.24 | 290 days |
| **At Risk Spenders** | 16 | $3,446.73 | 1.05% | $215.42 | 512 days |

### 3. Pareto 80/20 Concentration
- The top 20% of customers generate **56.04% of total enterprise revenue ($183,281.00)**.
- The top 30% account for **69.80%** of total revenue.

### 4. Cohort Retention Matrix
- Across all cohorts, the sharpest attrition happens between acquisition month ($M_0 = 100\%$) and month 1 ($M_1 \approx 18\% - 24\%$).
- Cohorts stabilize at a persistent retention baseline between **12% and 16%** throughout months 3 through 12.

---

## 5. SQL Implementation & Advanced Features

The accompanying [`sql/customer_analysis.sql`](file:///C:/Users/keert/.gemini/antigravity-ide/scratch/ShadowFox_Data_Analyst_Internship/Intermediate_Customer_Analytics/sql/customer_analysis.sql) script demonstrates enterprise SQL competencies:

1. **Common Table Expressions (CTEs)**: Used extensively in Q3, Q5, Q6, Q7, Q8, Q9, Q10 to decouple complex multi-stage calculations.
2. **Window Functions**:
   - `DENSE_RANK() OVER (PARTITION BY Customer_Region ORDER BY Total_Spend DESC)`: Identifies top 3 VIP spenders in each region without rank gaps.
   - `LAG(monthly_revenue, 1) OVER (ORDER BY sales_month)`: Computes Month-over-Month (MoM) revenue growth velocity.
   - `SUM(monthly_revenue) OVER (ORDER BY sales_month ROWS UNBOUNDED PRECEDING)`: Generates cumulative running revenue.
   - `NTILE(5) OVER (ORDER BY SUM(total_spend) DESC)`: Bins customer database into five equal monetary spending quintiles for tiered marketing campaigns.
   - `ROW_NUMBER() OVER (PARTITION BY customer_id ORDER BY transaction_date)`: Labels customer transaction sequences (`First Order`, `Second Order`, etc.).
3. **Date Calculations & Categorization**:
   - `JULIANDAY('2025-01-01') - JULIANDAY(MAX(transaction_date))` to calculate customer churn dormancy in days.

---

## 6. Business Recommendations

1. **Bridge the First-to-Second Purchase Gap**:
   - Deploy automated Day 3 (delivery), Day 10 (guide), and Day 21 (incentive discount) email flows.
   - Target: Transition 15% of the 451 one-time buyers into repeat purchasers, unlocking ~$35,000+ in margin.
2. **Launch a Dedicated VIP Platinum Tier for Champions**:
   - Protect the top 200 Champions ($162,963.95 revenue) with exclusive perks, early product drops, and priority shipping.
3. **Reactivate "At Risk Spenders"**:
   - 16 high-value customers with multi-order history have been inactive for >500 days. Target them with dedicated win-back promotions.
4. **Channel Budget Reallocation**:
   - Paid and Organic Search generate superior AOV ($142 – $148). Reallocate underperforming social media budgets toward high-intent search keywords.

---

## 7. How to Run the Project

```bash
# 1. Navigate to directory
cd Intermediate_Customer_Analytics

# 2. Install dependencies
pip install -r requirements.txt

# 3. (Optional) Regenerate raw dataset
python scripts/generate_customer_data.py

# 4. Clean data and engineer cohort attributes
python scripts/customer_cleaning.py

# 5. Run RFM analysis, cohort retention, and generate charts
python scripts/customer_analysis.py

# 6. Build SQLite database, execute SQL queries, and export reports
python scripts/execute_sql_queries.py
```
