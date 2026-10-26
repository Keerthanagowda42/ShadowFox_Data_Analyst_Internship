# Small Business Sales Performance: Business Insights & Strategic Recommendations

**Project**: Beginner Level - Small Business Sales Performance Analysis & Dashboard  
**Dataset**: FY 2024 Small Business Sales (1,250 Verified Transactions)  
**Author**: ShadowFox Data Analyst Intern  
**Date**: October 2026  

---

## 1. Executive Summary

This study conducted an in-depth performance analysis of a retail small business throughout the fiscal year 2024. Starting with raw, uncurated sales records containing data inconsistencies, currency formatting issues, mixed date formats, missing fields, and duplicate entries, a structured Python data cleaning pipeline was executed. The validated clean dataset contains **1,250 verified transactions** across four primary product categories: **Furniture, Electronics, Office Supplies, and Home & Kitchen**.

The business generated **$180,936.50 in Total Gross Revenue**, producing **$87,709.30 in Net Profit** with an outstanding overall profit margin of **48.48%**. Average Order Value (AOV) settled at **$144.75** across **2,662 units sold**.

```
+-----------------------------------------------------------------------------------+
|                               KEY BUSINESS METRICS                                |
+-----------------------+-------------------------+---------------------------------+
| Total Revenue         | $180,936.50             | Full FY 2024 Gross Receipts     |
| Total Production Cost | $93,227.20              | Cost of Goods Sold (COGS)       |
| Total Net Profit      | $87,709.30              | Gross Margin Spread             |
| Overall Profit Margin | 48.48%                  | High Unit Economics             |
| Total Orders Placed   | 1,250 orders            | Verified Unique Transactions    |
| Total Units Sold      | 2,662 units             | Volume Across Catalog           |
| Average Order Value   | $144.75                 | Revenue / Transaction           |
| Profit Per Order      | $70.17                  | Net Return / Transaction        |
+-----------------------+-------------------------+---------------------------------+
```

---

## 2. Monthly Trends and Seasonality

```
Monthly Revenue Progression (USD):
Jan: $18,216.89 | Feb: $13,603.27 | Mar: $14,231.61 | Apr: $11,644.89
May: $17,817.85 | Jun:  $9,972.42 | Jul: $10,540.87 | Aug: $14,479.02
Sep: $12,114.20 | Oct: $16,049.53 | Nov: $23,036.07 | Dec: $19,229.88
```

### Observations:
1. **Q4 Peak (November - December)**:
   - November recorded the fiscal high of **$23,036.07** in revenue and **$11,123.67** in profit, with Average Order Value rising sharply to **$213.30**.
   - December sustained strong momentum with **$19,229.88** in revenue (308 units sold).
   - This reflects standard Black Friday / Cyber Monday / holiday commercial surges and multi-item basket ordering.
2. **Mid-Year Trough (June - July)**:
   - June represented the annual trough (**$9,972.42** revenue, 183 units, AOV $109.59), followed closely by July (**$10,540.87**).
   - This mid-year lull indicates an absence of promotional campaigns and summer seasonality headwinds.
3. **May Mid-Year Rebound**:
   - May registered a sharp +53.01% MoM surge (**$17,817.85**), driven by corporate Q2 office equipment restocking and spring promotional activities.

---

## 3. Category Performance Analysis

| Category | Total Revenue ($) | Sales Share (%) | Total Profit ($) | Units Sold | Profit Margin (%) |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Furniture** | $74,359.00 | 41.10% | $32,569.00 | 353 | 43.80% |
| **Electronics** | $68,702.12 | 37.97% | $34,803.12 | 995 | 50.66% |
| **Office Supplies** | $21,772.34 | 12.03% | $11,247.64 | 695 | 51.66% |
| **Home & Kitchen** | $16,103.04 | 8.90% | $9,089.54 | 619 | **56.45%** |

### Insights:
- **Revenue Anchors**: **Furniture and Electronics** collectively generate **79.07% ($143,061.12)** of total business revenue. Furniture delivers the highest ticket sizes, while Electronics drives both high ticket size and high volume (995 units).
- **Margin Champions**: While **Home & Kitchen** and **Office Supplies** account for smaller revenue shares (8.90% and 12.03%), they boast the highest profit margins at **56.45%** and **51.66%**, respectively. Low unit costs and high markups create lucrative margin buffers.

---

## 4. Product Deep-Dive (Top & Bottom Performers)

### Top 5 Revenue Drivers:
1. **Ergonomic Office Chair** (Furniture): **$43,281.00** Sales | $18,711.00 Profit | 189 Units (43.23% Margin)
2. **Standing Desk Converter** (Furniture): **$31,078.00** Sales | $13,858.00 Profit | 164 Units (44.59% Margin)
3. **Noise-Cancelling Headphones** (Electronics): **$28,198.12** Sales | $14,098.12 Profit | 188 Units (50.00% Margin)
4. **Mechanical Keyboard** (Electronics): **$16,828.13** Sales | $8,413.13 Profit | 187 Units (49.99% Margin)
5. **Heavy-Duty Paper Shredder** (Office Supplies): **$15,118.11** Sales | $7,180.11 Profit | 189 Units (47.49% Margin)

*Takeaway*: The top 3 products account for **$102,557.12 (56.68%)** of all enterprise revenue. The business is heavily anchored in work-from-home and office ergonomics.

### Lowest 5 Revenue Products:
1. **A4 Copy Paper (Ream)**: $1,623.50 Sales | 191 Units | $897.70 Profit (55.29% Margin)
2. **Gel Ink Pens (12-pack)**: $1,974.48 Sales | 152 Units | $1,336.08 Profit (67.67% Margin)
3. **Mesh Desk Organizer**: $3,056.25 Sales | 163 Units | $1,833.75 Profit (60.00% Margin)
4. **Wireless Mouse**: $3,222.76 Sales | 124 Units | $1,672.76 Profit (51.90% Margin)
5. **Stainless Steel Water Bottle**: $4,137.93 Sales | 207 Units | $2,378.43 Profit (57.48% Margin)

*Takeaway*: Low absolute revenues do not imply failure—items like Gel Ink Pens yield **67.67% margin** and A4 Copy Paper moved 191 units. These serve as high-margin cross-sell candidates rather than standalone revenue engines.

---

## 5. Regional & Channel Performance

| Region | Revenue ($) | Share (%) | Profit ($) | Orders | AOV ($) | Margin (%) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **West** | $38,351.59 | 21.20% | $18,528.59 | 253 | $151.59 | 48.31% |
| **Central** | $37,386.35 | 20.66% | $18,083.45 | 252 | $148.36 | 48.37% |
| **East** | $37,015.36 | 20.46% | $17,708.66 | 255 | $145.16 | 47.84% |
| **North** | $34,160.88 | 18.88% | $16,731.58 | 247 | $138.30 | 48.98% |
| **South** | $34,022.32 | 18.80% | $16,657.02 | 243 | $140.01 | 48.96% |

- Regional distribution is well-balanced (~19% to 21% per territory).
- The **West Region** commands the lead with **$38,351.59** in sales and highest AOV ($151.59).
- Profit margins across all regions are remarkably consistent (47.8% - 49.0%), indicating uniform pricing discipline and lack of regional discounting slippage.

---

## 6. Practical Business Recommendations

### Recommendation 1: High-Margin Product Bundling
- **Action**: Pair flagship low-margin/high-revenue furniture (Ergonomic Office Chair, Standing Desk Converter) with high-margin desk accessories (Gel Ink Pens, Mesh Desk Organizer, Ceramic Mug Set, Smart Surge Protector).
- **Target Impact**: Elevate Average Order Value (AOV) from $144.75 to >$175 while lifting aggregate margin on furniture orders by +4 to +6 percentage points.

### Recommendation 2: Mid-Year Promotional Campaign (June - July Counter-Cyclical Strategy)
- **Action**: Launch an annual "Mid-Year Workstation Refresh" or "Back-to-Work Summer Sale" during June and July.
- **Target Impact**: Mitigate the mid-year slump (trough of $9,972 in June) by offering seasonal discounts on slow-moving inventory to maintain consistent cash flow.

### Recommendation 3: Premium Tier Extension in Electronics
- **Action**: Electronics delivered $68,702.12 at a 50.66% margin with 995 units moved. Introduce complementary premium accessories (e.g., Dual-Monitor Arms, 4K USB-C Docks).
- **Target Impact**: Capitalize on high tech-affinity in the West and Central regions.

### Recommendation 4: Dynamic Reorder Points for Q4 Inventory
- **Action**: In Q4, sales volume jumped by over 45%. Buffer supply chain lead times by initiating purchase orders for Ergonomic Chairs and Noise-Cancelling Headphones 90 days ahead in August.
- **Target Impact**: Eliminate stock-outs during peak November-December retail velocity.

---

## 7. Deliverables Checklist & Verification

- [x] Raw data cleaned and separated (`raw_sales_data.csv` -> `cleaned_sales_data.csv`)
- [x] Python cleaning script automated (`data_cleaning.py`)
- [x] Python analysis script with KPIs and charts (`sales_analysis.py`)
- [x] Excel workbook generated (`Small_Business_Sales_Dashboard.xlsx`) with Raw Data, Cleaned Data, Analysis (formulas), and Dashboard tabs
- [x] Visual charts exported in 300 DPI to `charts/`
- [x] Strategic insights and recommendations documented
