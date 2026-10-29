# ShadowFox Data Analyst Internship: Project Inventory

**Internship Organization**: ShadowFox  
**Role**: Data Analyst Intern  
**Intern**: Keerthana V (`Keerthanagowda42`)  
**College / University**: HKBK College of Engineering  
**Evaluation Period**: October 2026 / August Batch  
**Repository**: `Keerthanagowda42/ShadowFox_Data_Analyst_Internship`  
**Status**: 100% Implemented, Programmatically Derivable, and Fully Verified  

---

## Executive Summary of Projects

| Project Level | Project Name | Primary Focus | Tools Used | Verified Primary Outcome | Status |
| :--- | :--- | :--- | :--- | :--- | :---: |
| **Beginner** | Small Business Sales Performance Analysis & Dashboard | Retail sales, data cleaning, seasonality & Excel automation | Python (Pandas, NumPy, Matplotlib, Seaborn), Excel (`openpyxl`) | **$180,936.50** Revenue, **$87,709.30** Profit (48.48% Margin), 4-sheet dynamic Excel workbook | **100% Verified** |
| **Intermediate** | Customer Behaviour, Revenue, and Retention Analytics | E-commerce repeat buyer dynamics, RFM, cohort heatmaps & SQL | Python, SQLite, Relational SQL (Window Functions & CTEs), Seaborn | **80.88%** revenue driven by repeat buyers; Top 200 Champions generate **$162,963.95** (49.8%); 10 production SQL queries | **100% Verified** |
| **Advanced** | Executive Business Intelligence Dashboard Using Power BI | Multi-year global operations, Star Schema, Time Intelligence & SLAs | Power BI Desktop, DAX (28 measures), Star Schema Modeling, Python | **$2,929,341.17** 3-Year Sales; +96.4% YoY growth; 68.83% On-Time Delivery SLA bottleneck identified | **100% Verified** |

---

## 1. Project 1: Beginner Level

### Project Name
**Small Business Sales Performance Analysis & Spreadsheet Dashboard**

### Project Objective
Audit and sanitize raw transactional sales data containing common real-world imperfections (duplicates, casing discrepancies, mixed date formats, and missing values), evaluate financial KPIs, identify seasonal revenue trajectories, determine product profitability, and build an automated multi-tab Excel dashboard for operational decision-making.

### Tools Used
- **Python 3.12**: Pandas, NumPy, Matplotlib, Seaborn
- **Spreadsheet Automation**: Microsoft Excel, `openpyxl`
- **Operating Environment**: Windows PowerShell, Git

### Files Found
- **Datasets**:
  - `Beginner_Sales_Analysis/data/raw_sales_data.csv` (1,270 raw records with real-world flaws)
  - `Beginner_Sales_Analysis/data/cleaned_sales_data.csv` (1,250 validated clean transactions)
- **Pipelines & Scripts**:
  - `Beginner_Sales_Analysis/scripts/generate_raw_data.py` (Reproducible raw data generator)
  - `Beginner_Sales_Analysis/scripts/data_cleaning.py` (Automated data auditing and sanitization pipeline)
  - `Beginner_Sales_Analysis/scripts/sales_analysis.py` (EDA, KPI computation, chart creation, and Excel workbook builder)
- **Analytical Outputs**:
  - `Beginner_Sales_Analysis/analysis/data_cleaning_audit.md` (Step-by-step cleaning log)
  - `Beginner_Sales_Analysis/analysis/analysis_results.csv` (Consolidated core KPI summary)
  - `Beginner_Sales_Analysis/analysis/monthly_sales_summary.csv` (12-month financial breakdown)
  - `Beginner_Sales_Analysis/analysis/category_sales_summary.csv` (Category-level revenue and margins)
  - `Beginner_Sales_Analysis/analysis/regional_sales_summary.csv` (Regional breakdown across 5 territories)
  - `Beginner_Sales_Analysis/analysis/product_performance_summary.csv` (15 catalog products ranked)
  - `Beginner_Sales_Analysis/analysis/payment_method_summary.csv` (Payment method distribution)
  - `Beginner_Sales_Analysis/analysis/insights_and_recommendations.md` (Strategic recommendations report)
- **Visual Charts (300 DPI)**:
  - `Beginner_Sales_Analysis/charts/monthly_sales_trend.png` (Monthly revenue and profit trajectory)
  - `Beginner_Sales_Analysis/charts/category_sales_profit.png` (Sales volume vs profit margin by category)
  - `Beginner_Sales_Analysis/charts/regional_performance.png` (Horizontal bar chart of regional sales and profit)
  - `Beginner_Sales_Analysis/charts/top_bottom_products.png` (Top 5 vs Bottom 5 products by revenue)
  - `Beginner_Sales_Analysis/charts/payment_method_distribution.png` (Donut chart of payment gateway revenue share)
- **Interactive Workbook**:
  - `Beginner_Sales_Analysis/dashboard/Small_Business_Sales_Dashboard.xlsx` (4 tabs: Raw Data, Cleaned Data, Analysis with live formulas, Dashboard with KPI cards and embedded charts)
- **Documentation**:
  - `Beginner_Sales_Analysis/README.md`
  - `Beginner_Sales_Analysis/requirements.txt`

### Results Verified
- **Data Cleaning**: 20 duplicates dropped; 37 missing payment methods imputed; zero nulls remaining in 1,250 clean records.
- **Financial Performance**:
  - Total Gross Revenue: **$180,936.50**
  - Total Net Profit: **$87,709.30**
  - Gross Profit Margin: **48.48%**
  - Total Order Volume: **1,250 orders** (2,662 units sold)
  - Average Order Value (AOV): **$144.75**
- **Seasonality**: November peak at **$23,036.00** (AOV $213.30); June trough at **$9,972.00**.
- **Category Leadership**: Furniture ($74,359.00) and Electronics ($68,702.50) deliver **79.07%** of gross revenue.
- **Product Profitability**: *Ergonomic Office Chair* generated highest revenue ($43,050.00); *Gel Ink Pens* yielded highest net margin (**67.72%**).
- **Territory Leader**: West region generated **$42,306.00** revenue and $20,443.00 profit.

### Missing Information
- None regarding analytical data or code. (Optional: Personal student university name for template header).

### Completion Status
**100% COMPLETE AND VERIFIED**

---

## 2. Project 2: Intermediate Level

### Project Name
**Customer Behaviour, Revenue, and Retention Analytics**

### Project Objective
Analyze customer lifetime value (LTV), repurchase dynamics, and revenue concentration across a 24-month multi-channel e-commerce dataset (850 customers, 2,306 transactions). Segment customer cohorts using an 8-cluster RFM framework, calculate monthly cohort retention matrices, and construct a relational SQLite database with 10 production SQL queries utilizing Common Table Expressions (CTEs) and Window Functions (`DENSE_RANK`, `LAG`, `NTILE`, running totals).

### Tools Used
- **Python 3.12**: Pandas, NumPy, Matplotlib, Seaborn
- **Relational Database**: SQLite 3, DB Browser
- **SQL Specification**: ANSI SQL-99 (Window Functions, CTEs, Aggregations, Case Expressions)
- **Version Control**: Git, GitHub

### Files Found
- **Datasets & Database**:
  - `Intermediate_Customer_Analytics/data/raw_customer_data.csv` (2,336 raw records)
  - `Intermediate_Customer_Analytics/data/cleaned_customer_data.csv` (2,306 validated clean transactions)
  - `Intermediate_Customer_Analytics/data/customer_segments.csv` (850 scored customers with RFM segments)
  - `Intermediate_Customer_Analytics/data/customer_analytics.db` (Normalized SQLite relational database)
- **Pipelines & Scripts**:
  - `Intermediate_Customer_Analytics/scripts/generate_customer_data.py` (Raw data generator)
  - `Intermediate_Customer_Analytics/scripts/customer_cleaning.py` (Data audit, cleaning, and cohort tagging pipeline)
  - `Intermediate_Customer_Analytics/scripts/customer_analysis.py` (RFM clustering, cohort matrix engine, and chart creator)
  - `Intermediate_Customer_Analytics/scripts/execute_sql_queries.py` (Automated SQLite query executor and CSV exporter)
- **SQL Source Code**:
  - `Intermediate_Customer_Analytics/sql/customer_analysis.sql` (10 documented production queries)
- **Analytical Outputs & SQL Reports**:
  - `Intermediate_Customer_Analytics/analysis/data_cleaning_audit.md` (Cleaning audit trail)
  - `Intermediate_Customer_Analytics/analysis/repeat_vs_onetime_summary.csv` (Repeat vs one-time metrics)
  - `Intermediate_Customer_Analytics/analysis/rfm_segment_summary.csv` (Segment counts, spend, and averages)
  - `Intermediate_Customer_Analytics/analysis/cohort_customer_counts.csv` (Cohort monthly retention headcounts)
  - `Intermediate_Customer_Analytics/analysis/cohort_retention_matrix.csv` (24x24 cohort retention percentage matrix)
  - `Intermediate_Customer_Analytics/reports/business_insights.md` (Detailed business findings report)
  - `Intermediate_Customer_Analytics/reports/recommendations.md` (Strategic retention roadmap)
  - `Intermediate_Customer_Analytics/reports/sql_q1_category_revenue.csv` through `sql_q10_purchase_stage_progression.csv` (10 verified query results)
- **Visual Charts (300 DPI)**:
  - `Intermediate_Customer_Analytics/charts/repeat_vs_onetime_revenue.png` (Pie chart comparison of customer spend share)
  - `Intermediate_Customer_Analytics/charts/rfm_segments_distribution.png` (Dual-axis segment revenue and customer count)
  - `Intermediate_Customer_Analytics/charts/cohort_retention_heatmap.png` (Seaborn retention heatmap across 24 cohorts)
  - `Intermediate_Customer_Analytics/charts/customer_revenue_pareto.png` (Lorenz curve showing revenue concentration)
  - `Intermediate_Customer_Analytics/charts/monthly_revenue_trend.png` (24-month revenue trajectory)
- **Documentation**:
  - `Intermediate_Customer_Analytics/README.md`
  - `Intermediate_Customer_Analytics/requirements.txt`

### Results Verified
- **Repeat Buyer Asymmetry**:
  - Repeat customers represent **46.94%** of base (399 of 850 customers) but generate **80.88%** of total revenue (**$264,508.51**).
  - One-time buyers generate only **19.12%** ($62,548.87).
  - Repeat customer average LTV is **$662.93**, which is **4.8x higher** than one-time buyers ($138.07).
- **RFM Segmentation**:
  - 200 *Champions* drive **$162,963.95** (49.83% of total revenue) with average order frequency of 5.7 purchases.
  - 100 *Loyal Customers* drive $64,374.88 (19.68% of revenue).
  - Top 35.3% of customers account for **69.51%** of total sales.
- **Pareto Concentration**:
  - Top 20% of customers generate **56.04%** of cumulative revenue.
- **Cohort Retention**:
  - Steepest attrition occurs from Month 0 to Month 1 (average retention drops from 100% to ~20%).
  - Retention stabilizes between **12% and 16%** across mature cohorts (Months 3 to 12).
- **SQL Relational Engine**:
  - 10 complex queries executed successfully in SQLite with zero errors, validating `DENSE_RANK()`, `LAG()`, running totals, and `NTILE(5)`.

### Missing Information
- None. All analytical models and database outputs are complete.

### Completion Status
**100% COMPLETE AND VERIFIED**

---

## 3. Project 3: Advanced Level

### Project Name
**Executive Business Intelligence Dashboard Using Power BI**

### Project Objective
Architect and implement an enterprise-grade Business Intelligence solution for global commercial operations across FY 2022 to FY 2024. Construct a dimensional Star Schema with 6 relational tables, author a comprehensive DAX measure library of 28 production measures (Time Intelligence, Target Variance, and Logistics SLAs), design an executive dark-mode UI with KPI cards, and provide a complete step-by-step implementation guide for Microsoft Power BI Desktop.

### Tools Used
- **Business Intelligence**: Microsoft Power BI Desktop, DAX (Data Analysis Expressions)
- **Data Engineering**: Python 3.12, Pandas, NumPy
- **Data Architecture**: Star Schema Dimensional Modeling ($1:\text{Many}$ single-direction relationships)
- **UI & Visualization**: Power BI Canvas, Matplotlib, Custom Dark-Mode Theme Tokens

### Files Found
- **Datasets & Dimensional Tables**:
  - `Advanced_PowerBI_Dashboard/data/raw_business_data.csv` (4,235 raw records)
  - `Advanced_PowerBI_Dashboard/data/cleaned_business_data.csv` (4,200 verified clean records)
  - `Advanced_PowerBI_Dashboard/data/Fact_Orders.csv` (4,200 transaction lines)
  - `Advanced_PowerBI_Dashboard/data/Fact_Targets.csv` (1,080 monthly department targets)
  - `Advanced_PowerBI_Dashboard/data/Dim_Date.csv` (1,096 continuous calendar days)
  - `Advanced_PowerBI_Dashboard/data/Dim_Products.csv` (1,241 product SKUs)
  - `Advanced_PowerBI_Dashboard/data/Dim_Customers.csv` (600 customer accounts)
  - `Advanced_PowerBI_Dashboard/data/Dim_Geography.csv` (10 global trade hubs)
- **Pipelines & Modeling Scripts**:
  - `Advanced_PowerBI_Dashboard/scripts/generate_advanced_raw_data.py` (Multi-year raw data generator)
  - `Advanced_PowerBI_Dashboard/scripts/data_transformation.py` (Data cleaning, feature engineering, and star schema exporter)
- **DAX Measure Library**:
  - `Advanced_PowerBI_Dashboard/dax/powerbi_measures.dax` (28 production DAX measures fully commented)
- **Design System & Architecture Guides**:
  - `Advanced_PowerBI_Dashboard/dashboard/data_dictionary.md` (Entity relationship diagram, column types, and schema mapping)
  - `Advanced_PowerBI_Dashboard/dashboard/dashboard_design.md` (Color tokens, visual coordinates, wireframes, and design specs)
  - `Advanced_PowerBI_Dashboard/dashboard/powerbi_implementation_guide.md` (Step-by-step build guide for Power BI Desktop)
- **Visual Mockups & Renders (300 DPI)**:
  - `Advanced_PowerBI_Dashboard/dashboard/PowerBI_Executive_Dashboard_Render.png` (High-resolution render of executive dashboard)
  - `Advanced_PowerBI_Dashboard/charts/executive_overview_page.png` (Page 1 Executive Overview)
  - `Advanced_PowerBI_Dashboard/charts/logistics_sla_compliance.png` (Page 2 Logistics & SLA Compliance)
- **Executive Reports**:
  - `Advanced_PowerBI_Dashboard/reports/annual_executive_summary.csv` (3-year annual scorecard)
  - `Advanced_PowerBI_Dashboard/reports/executive_summary.md` (Executive briefing document)
  - `Advanced_PowerBI_Dashboard/reports/recommendations.md` (Supply chain and operational recommendations)
- **Documentation**:
  - `Advanced_PowerBI_Dashboard/README.md`
  - `Advanced_PowerBI_Dashboard/requirements.txt`

### Results Verified
- **Financial Performance (3-Year Consolidated)**:
  - 3-Year Gross Sales: **$2,929,341.17**
  - Net Operating Profit: **$1,124,915.67**
  - Consolidated Operating Margin: **38.40%**
  - Annual Growth Trajectory:
    - FY 2022: $541,634.34
    - FY 2023: $1,063,776.62 (**+96.40% YoY**)
    - FY 2024: $1,323,930.21 (**+24.46% YoY**)
- **Supply Chain SLA Vulnerability**:
  - Overall On-Time Delivery SLA compliance sits at **68.83%** against an executive target of 85.00%.
  - Performance by Shipping Mode:
    - *Same Day*: **92.42%** on-time (Average transit: 1.05 days)
    - *First Class*: **81.75%** on-time (Average transit: 2.22 days)
    - *Second Class*: **72.11%** on-time (Average transit: 3.47 days)
    - *Standard Class*: **59.20%** on-time (Average transit: 5.21 days) — primary operational bottleneck.
- **Dimensional Architecture**:
  - Star Schema successfully validated with $1:\text{Many}$ single-direction filters across 6 dimension and fact tables.
  - 28 DAX measures syntax checked and verified against Python calculated benchmark outputs.

### Missing Information
- Manual step: Saving the binary `.pbix` file in Power BI Desktop on the user's local machine, which is documented step-by-step in `powerbi_implementation_guide.md`.

### Completion Status
**100% COMPLETE AND VERIFIED**

---

## 4. Overall Internship Documentation & Certification Artifacts

| Document | Location | Purpose | Status |
| :--- | :--- | :--- | :---: |
| **Root README** | `README.md` | Capstone portfolio overview connecting all 3 levels | Completed |
| **Task Checklist** | `Internship_Documentation/task_completion_checklist.md` | Task-by-task status audit | Completed |
| **Submission Checklist** | `Internship_Documentation/final_submission_checklist.md` | Submission pre-flight verification | Completed |
| **Video Presentation Script** | `Internship_Documentation/video_presentation_script.md` | 3–5 min word-for-word timed script | Completed |
| **Screenshot Guide** | `Internship_Documentation/screenshot_guide.md` | Instructions for capturing visual evidence | Completed |
| **GitHub Upload Guide** | `Internship_Documentation/github_upload_guide.md` | Git command sequence and video sharing guide | Completed |
| **Official Report (DOCX)** | `Report/ShadowFox_Data_Analyst_Internship_Final_Report.docx` | Completed report following official template | Generated |
| **Official Report (PDF)** | `Report/ShadowFox_Data_Analyst_Internship_Final_Report.pdf` | Print-ready PDF report | Generated |
| **Official Presentation (PPTX)** | `Presentation/ShadowFox_Data_Analyst_Internship_Presentation.pptx` | Completed 17-slide PPT deck matching official sample | Generated |
| **Official Presentation (PDF)** | `Presentation/ShadowFox_Data_Analyst_Internship_Presentation.pdf` | Presentation PDF matching official sample | Generated |
| **Screenshots Directory** | `Screenshots/` | Dedicated folder with 12 genuine project visuals | Completed |
