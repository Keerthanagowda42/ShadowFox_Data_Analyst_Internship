# Customer Behaviour, Revenue, and Retention Analytics: Business Insights Report

**Project**: Intermediate Level - Customer Behaviour, Revenue, and Retention Analytics  
**Dataset**: 24-Month E-Commerce Transaction Log (850 Distinct Customers, 2,306 Transactions)  
**Author**: ShadowFox Data Analyst Intern  
**Date**: October 2026  

---

## 1. Executive Analytics Summary

An empirical customer analytics study was conducted across **2,306 verified transactions** from January 2023 through December 2024, representing **850 unique customers** and generating **$327,053.54 in Total Portfolio Revenue** with an Average Transaction Value of **$141.83**.

By implementing RFM Segmentation (Recency, Frequency, Monetary), Monthly Cohort Retention matrices, Lorenz/Pareto concentration curves, and Relational SQL modeling, this report addresses the critical drivers of customer lifetime value and revenue retention.

```
+-----------------------------------------------------------------------------------+
|                        CUSTOMER PORTFOLIO SUMMARY METRICS                         |
+------------------------------+--------------------+-------------------------------+
| Total Portfolio Revenue      | $327,053.54        | 24-Month Study Total          |
| Total Orders / Transactions  | 2,306              | Completed Checkout Events     |
| Total Unique Customers       | 850 customers      | Distinct Buyer Profiles       |
| Total Units Purchased        | 3,662 units        | Product Volume Delivered      |
| Average Order Value (AOV)    | $141.83            | Portfolio Mean Basket Size    |
| Average Customer Lifetime LTV| $384.77            | Mean Lifetime Spend / Customer|
| Repeat Customer Revenue Share| 80.88%             | Revenue from >1 Order Buyers  |
+------------------------------+--------------------+-------------------------------+
```

---

## 2. Repeat vs. One-Time Customer Dynamics

The empirical data reveals a striking structural asymmetry between repeat buyers and single-purchase customers:

| Customer Type | Customer Count | Customer Share (%) | Total Revenue ($) | Revenue Share (%) | Avg. Customer LTV ($) |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **One-Time Customers** | 451 | 53.06% | $62,545.03 | **19.12%** | $138.68 |
| **Repeat Customers** | 399 | 46.94% | $264,508.51 | **80.88%** | **$662.93** |
| **Total / Overall** | **850** | **100.00%** | **$327,053.54** | **100.00%** | **$384.77** |

### Key Takeaway:
Although repeat customers represent under half of the active customer base (**46.94%**), they generate **$264,508.51 (80.88%)** of all enterprise revenue. On average, a repeat buyer delivers **4.78x higher lifetime value ($662.93)** compared to a one-time buyer ($138.68). This confirms that customer retention—not customer acquisition—is the primary engine of business solvency.

---

## 3. RFM Customer Segmentation Analysis

Using quintile-based scoring ($1-5$) across Recency (days since last purchase), Frequency (order count), and Monetary (lifetime spend), customers were categorized into 8 behavioral segments:

| Customer Segment | Customer Count | Share (%) | Total Revenue ($) | Rev Share (%) | Avg Recency | Avg Frequency | Avg LTV ($) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Champions** | 200 | 23.53% | **$162,963.95** | **49.83%** | 85 days | 5.70 orders | **$814.82** |
| **Loyal Customers** | 210 | 24.71% | **$96,739.15** | **29.58%** | 285 days | 3.21 orders | **$460.66** |
| **Needs Attention** | 172 | 20.24% | $29,087.88 | 8.89% | 551 days | 1.14 orders | $169.12 |
| **New / Promising** | 86 | 10.12% | $12,496.12 | 3.82% | 125 days | 1.00 orders | $145.30 |
| **Hibernating** | 85 | 10.00% | $10,380.91 | 3.17% | 373 days | 1.00 orders | $122.13 |
| **Lost / Churned** | 47 | 5.53% | $7,136.72 | 2.18% | 636 days | 1.00 orders | $151.85 |
| **Potential Loyalists** | 34 | 4.00% | $4,802.08 | 1.47% | 290 days | 1.00 orders | $141.24 |
| **At Risk Spenders** | 16 | 1.88% | $3,446.73 | 1.05% | 512 days | 2.75 orders | $215.42 |

### Critical Behavioral Findings:
1. **The Core Anchor (Champions & Loyal Customers)**:
   - **410 customers (48.24% of base)** generate **$259,703.10 (79.41%)** of all revenue.
   - Champions alone purchase an average of 5.70 times, delivering $814.82 each.
2. **At Risk Spenders**:
   - A high-value cohort of 16 multi-order customers has lapsed past 512 days without an order. These require immediate win-back campaigns.
3. **The Needs Attention Pool**:
   - 172 buyers ($29,087.88 revenue) are cooling off (551 days average recency). Without re-engagement, they slide into permanent churn.

---

## 4. Pareto 80/20 Concentration

- Cumulative Lorenz curve analysis proves strong revenue concentration: **The top 20% of customers account for 56.04% of total cumulative revenue ($183,281.00)**.
- The top 30% of customers account for **69.80%** of total revenue.
- Conversely, the bottom 50% of the customer base accounts for less than 17% of total revenue.

---

## 5. Cohort Monthly Retention & Churn Analysis

- **Initial Drop-Off (Month 1)**: Across all 2023 cohorts, the steep drop occurs between Month 0 (acquisition) and Month 1, where retention drops from 100% to between **18.5% and 24.3%**.
- **Long-Tail Stabilization**: Customers who survive the Month 1 drop remain loyal, stabilizing at **12% to 16% retention** across Month 3 through Month 12.
- **SQL Churn Classification**:
  - **Active (0-90 Days)**: 183 customers (21.53%) responsible for **$113,018.41** (highest avg value: $617.59).
  - **Warm (91-180 Days)**: 113 customers (13.29%) responsible for **$53,083.09**.
  - **Cooling Off (181-365 Days)**: 220 customers (25.88%) responsible for **$81,972.58**.
  - **Dormant / Churned (>365 Days)**: 334 customers (39.29%) responsible for **$78,979.46**.

---

## 6. Channel and Category Revenue Contributions

### Channel Attribution:
- **Organic Search**: $70,999.48 (174 customers, AOV $141.72)
- **Paid Search**: $70,993.61 (179 customers, AOV $147.90)
- **Email Marketing**: $68,565.41 (173 customers, AOV $143.14)
- **Social Media**: $58,824.20 (170 customers, AOV $137.44)
- **Referral**: $57,670.84 (154 customers, AOV $137.97)

### Category Contributions:
- **Electronics**: $118,627.97 (**36.27% share**) - High ticket, flagship growth driver.
- **Sports & Outdoors**: $65,157.12 (**19.92% share**) - Consistent repeat reorder category.
- **Apparel**: $60,408.20 (**18.47% share**).
- **Home & Living**: $56,999.19 (**17.43% share**).
- **Health & Beauty**: $25,861.06 (**7.91% share**).
