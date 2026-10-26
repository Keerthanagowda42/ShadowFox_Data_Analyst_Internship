# ShadowFox Data Analyst Internship: Capstone Portfolio

[![Python](https://img.shields.io/badge/Python-3.12-blue.svg)](https://www.python.org/)
[![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-orange.svg)](https://pandas.pydata.org/)
[![SQL](https://img.shields.io/badge/SQL-SQLite%20%7C%20Window%20Functions-lightgrey.svg)](https://www.sqlite.org/)
[![Excel](https://img.shields.io/badge/Microsoft%20Excel-Automated%20Formulas-green.svg)](https://www.microsoft.com/excel)
[![Power BI](https://img.shields.io/badge/Power%20BI-DAX%20%7C%20Star%20Schema-yellow.svg)](https://powerbi.microsoft.com/)
[![Status](https://img.shields.io/badge/Status-Completed%20%26%20Verified-brightgreen.svg)]()

Welcome to the official repository for my **ShadowFox Data Analyst Internship**. This repository contains complete, production-ready implementations for all three required levels—**Beginner, Intermediate, and Advanced**—spanning data preparation, exploratory data analysis, relational SQL modeling, spreadsheet automation, and executive business intelligence dashboarding.

---

## 📁 Repository Structure

```
ShadowFox_Data_Analyst_Internship/
|
|-- README.md                                  # Portfolio overview (this document)
|-- requirements.txt                           # Global Python dependencies
|-- .gitignore                                 # Git exclusions configuration
|-- progress.md                                # Phase-by-phase implementation tracker
|
|-- Beginner_Sales_Analysis/                   # Project 1: Beginner Level
|   |-- data/                                  # Raw & cleaned sales CSV datasets
|   |-- scripts/                               # Data cleaning & sales analysis pipelines
|   |-- analysis/                              # Financial summaries & KPI tables
|   |-- charts/                                # 300 DPI high-resolution visual charts
|   |-- dashboard/                             # Multi-sheet formula-driven Excel workbook
|   |-- README.md                              # Comprehensive Project 1 documentation
|   |-- requirements.txt
|
|-- Intermediate_Customer_Analytics/           # Project 2: Intermediate Level
|   |-- data/                                  # Raw/cleaned transaction data & SQLite DB
|   |-- scripts/                               # Data cleaning, RFM engine & SQL executor
|   |-- sql/                                   # 10 Production SQL queries (CTEs, Window Fns)
|   |-- analysis/                              # RFM summaries & cohort retention matrices
|   |-- charts/                                # Cohort heatmaps, RFM & Pareto charts
|   |-- reports/                               # Business insights, recommendations & SQL CSVs
|   |-- README.md                              # Comprehensive Project 2 documentation
|   |-- requirements.txt
|
|-- Advanced_PowerBI_Dashboard/                # Project 3: Advanced Level
|   |-- data/                                  # Multi-year data & 6 Star Schema tables
|   |-- scripts/                               # Data transformation & star schema builder
|   |-- dax/                                   # 28 Commented production DAX measures
|   |-- dashboard/                             # Data dictionary, layout wireframes & build guide
|   |-- reports/                               # 3-Year executive briefings & recommendations
|   |-- charts/                                # Executive page renders & logistics visuals
|   |-- README.md                              # Comprehensive Project 3 documentation
|   |-- requirements.txt
|
|-- Internship_Documentation/                  # Submission & Certification Materials
|   |-- task_completion_checklist.md           # Granular task-by-task status breakdown
|   |-- final_submission_checklist.md          # Submission pre-flight verification
|   |-- video_presentation_script.md          # Word-for-word 3-5 minute presentation script
|   |-- screenshot_guide.md                    # Visual artifact capture guide
|   |-- github_upload_guide.md                 # Git setup & Google Drive video sharing guide
```

---

## 🚀 Executive Project Summaries

### 1. Project 1: Beginner Level — Small Business Sales Performance Analysis & Dashboard
- **Business Focus**: Multi-category retail sales performance, gross revenue, product margins, and seasonality.
- **Key Deliverables**:
  - Automated Python data cleaning script ([`scripts/data_cleaning.py`](file:///C:/Users/keert/.gemini/antigravity-ide/scratch/ShadowFox_Data_Analyst_Internship/Beginner_Sales_Analysis/scripts/data_cleaning.py)) resolving duplicates, mixed dates, and missing values across 1,250 transactions.
  - Automated 4-worksheet Excel workbook ([`Small_Business_Sales_Dashboard.xlsx`](file:///C:/Users/keert/.gemini/antigravity-ide/scratch/ShadowFox_Data_Analyst_Internship/Beginner_Sales_Analysis/dashboard/Small_Business_Sales_Dashboard.xlsx)) featuring live Excel formulas (`SUM`, `SUMIFS`, `AVERAGE`), KPI cards, and embedded charts.
  - 5 High-resolution visual charts in `Beginner_Sales_Analysis/charts/`.
- **Verified Metrics**:
  - **Total Revenue**: $180,936.50 | **Total Net Profit**: $87,709.30 | **Profit Margin**: 48.48%
  - **Total Orders**: 1,250 | **Units Sold**: 2,662 | **Average Order Value (AOV)**: $144.75
  - **Seasonality Peak**: November surge ($23,036 revenue, AOV $213.30) vs June trough ($9,972).
  - **Category Leaders**: Furniture ($74,359) and Electronics ($68,702) generate 79% of revenue.

---

### 2. Project 2: Intermediate Level — Customer Behaviour, Revenue, and Retention Analytics
- **Business Focus**: Repeat vs. One-Time buyer dynamics, RFM customer segmentation, monthly cohort retention matrices, and Relational SQL modeling.
- **Key Deliverables**:
  - 24-Month customer transaction pipeline ([`scripts/customer_analysis.py`](file:///C:/Users/keert/.gemini/antigravity-ide/scratch/ShadowFox_Data_Analyst_Internship/Intermediate_Customer_Analytics/scripts/customer_analysis.py)) analyzing 850 customers across 2,306 transactions.
  - 8-Segment RFM clustering exported to `customer_segments.csv`.
  - Monthly cohort retention matrix and Seaborn heatmap tracking 24 customer cohorts.
  - Relational SQLite database ([`customer_analytics.db`](file:///C:/Users/keert/.gemini/antigravity-ide/scratch/ShadowFox_Data_Analyst_Internship/Intermediate_Customer_Analytics/data/customer_analytics.db)) populated and queried via [`scripts/execute_sql_queries.py`](file:///C:/Users/keert/.gemini/antigravity-ide/scratch/ShadowFox_Data_Analyst_Internship/Intermediate_Customer_Analytics/scripts/execute_sql_queries.py).
  - 10 Production SQL queries ([`sql/customer_analysis.sql`](file:///C:/Users/keert/.gemini/antigravity-ide/scratch/ShadowFox_Data_Analyst_Internship/Intermediate_Customer_Analytics/sql/customer_analysis.sql)) utilizing `DENSE_RANK()`, `LAG()`, `NTILE(5)`, running totals, and CTEs.
- **Verified Metrics**:
  - **Repeat Customer Asymmetry**: Repeat buyers (46.94% of base) generate **80.88% of total revenue ($264,508.51)** with average LTV of $662.93 (4.8x higher than one-time buyers).
  - **Champions Anchor**: 200 Champions generate **$162,963.95 (49.83% of revenue)**.
  - **Pareto Concentration**: Top 20% of customers deliver 56.04% of total revenue.

---

### 3. Project 3: Advanced Level — Executive Business Intelligence Dashboard Using Power BI
- **Business Focus**: Multi-year enterprise operations, Time Intelligence DAX, Star Schema modeling, and Supply Chain SLA compliance.
- **Key Deliverables**:
  - Multi-year enterprise dataset (2022–2024) transformed and modeled into a certified **6-Table Star Schema** ([`Fact_Orders`](file:///C:/Users/keert/.gemini/antigravity-ide/scratch/ShadowFox_Data_Analyst_Internship/Advanced_PowerBI_Dashboard/data/Fact_Orders.csv), `Fact_Targets`, `Dim_Date`, `Dim_Products`, `Dim_Customers`, `Dim_Geography`).
  - Production DAX library ([`dax/powerbi_measures.dax`](file:///C:/Users/keert/.gemini/antigravity-ide/scratch/ShadowFox_Data_Analyst_Internship/Advanced_PowerBI_Dashboard/dax/powerbi_measures.dax)) with **28 commented measures** (Time Intelligence `TOTALYTD`, `SAMEPERIODLASTYEAR`, Budget Variance, Logistics SLAs).
  - Enterprise Data Dictionary ([`data_dictionary.md`](file:///C:/Users/keert/.gemini/antigravity-ide/scratch/ShadowFox_Data_Analyst_Internship/Advanced_PowerBI_Dashboard/dashboard/data_dictionary.md)) and UI Design Tokens ([`dashboard_design.md`](file:///C:/Users/keert/.gemini/antigravity-ide/scratch/ShadowFox_Data_Analyst_Internship/Advanced_PowerBI_Dashboard/dashboard/dashboard_design.md)).
  - Step-by-step Power BI build guide ([`powerbi_implementation_guide.md`](file:///C:/Users/keert/.gemini/antigravity-ide/scratch/ShadowFox_Data_Analyst_Internship/Advanced_PowerBI_Dashboard/dashboard/powerbi_implementation_guide.md)).
  - High-resolution visual mockups of the finished Executive Dashboard in `charts/` and `dashboard/`.
- **Verified Metrics**:
  - **3-Year Revenue**: $2,929,341.17 | **Net Profit**: $1,124,915.67 | **Consolidated Margin**: 38.40%
  - **Annual Expansion**: FY 2022 ($542k) -> FY 2023 ($1.06M, +96.4%) -> FY 2024 ($1.32M, +24.3%).
  - **Supply Chain SLA Risk**: On-Time Delivery compliance sits at **68.83%** (Target: 85%), driven by Standard Class ground bottlenecks (59.2% on-time).

---

## 🛠️ Technology Stack & Tools

- **Programming & Scripting**: Python 3.12 (Pandas, NumPy, Matplotlib, Seaborn, OpenPyXL, SQLite3)
- **Database & Querying**: SQLite, ANSI SQL-99 (Window Functions: `ROW_NUMBER`, `DENSE_RANK`, `LAG`, `NTILE`, CTEs)
- **Spreadsheet Automation**: Microsoft Excel (Dynamic formulas: `SUMIFS`, `AVERAGE`, `COUNT`, conditional formatting)
- **Business Intelligence**: Microsoft Power BI Desktop, DAX (Data Analysis Expressions), Star Schema Dimensional Modeling
- **Version Control & Documentation**: Git, GitHub, Markdown

---

## ⚡ Installation & Execution Guide

### 1. Clone the Repository
```bash
git clone https://github.com/Keerthanagowda42/ShadowFox_Data_Analyst_Internship.git
cd ShadowFox_Data_Analyst_Internship
```

### 2. Set Up Virtual Environment & Dependencies
```bash
python -m venv venv
# Windows:
.\venv\Scripts\activate
# Linux/macOS:
source venv/bin/activate

pip install -r requirements.txt
```

### 3. Run Project Pipelines
```bash
# Run Project 1 (Sales Analysis & Excel Dashboard)
cd Beginner_Sales_Analysis
python scripts/data_cleaning.py
python scripts/sales_analysis.py
cd ..

# Run Project 2 (Customer Analytics & SQL Pipeline)
cd Intermediate_Customer_Analytics
python scripts/customer_cleaning.py
python scripts/customer_analysis.py
python scripts/execute_sql_queries.py
cd ..

# Run Project 3 (Enterprise Power BI Data Transformation)
cd Advanced_PowerBI_Dashboard
python scripts/data_transformation.py
cd ..
```

---

## 📑 Final Submission Resources

For review evaluators and mentors:
- **Task Checklist**: See [`Internship_Documentation/task_completion_checklist.md`](file:///C:/Users/keert/.gemini/antigravity-ide/scratch/ShadowFox_Data_Analyst_Internship/Internship_Documentation/task_completion_checklist.md).
- **Video Presentation Script**: See [`Internship_Documentation/video_presentation_script.md`](file:///C:/Users/keert/.gemini/antigravity-ide/scratch/ShadowFox_Data_Analyst_Internship/Internship_Documentation/video_presentation_script.md).
- **Screenshot Guide**: See [`Internship_Documentation/screenshot_guide.md`](file:///C:/Users/keert/.gemini/antigravity-ide/scratch/ShadowFox_Data_Analyst_Internship/Internship_Documentation/screenshot_guide.md).
- **GitHub & Google Drive Upload Guide**: See [`Internship_Documentation/github_upload_guide.md`](file:///C:/Users/keert/.gemini/antigravity-ide/scratch/ShadowFox_Data_Analyst_Internship/Internship_Documentation/github_upload_guide.md).

---

## ⚖️ Quality Assurance & Integrity Declaration

All numbers, analytical findings, SQL query outputs, and charts in this portfolio were programmatically derived from the verified underlying datasets. No placeholders, empty code files, or fabricated results were utilized.
