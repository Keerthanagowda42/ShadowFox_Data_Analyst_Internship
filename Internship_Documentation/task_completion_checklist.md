# ShadowFox Data Analyst Internship: Task Completion Checklist

**Repository**: `ShadowFox_Data_Analyst_Internship`  
**Candidate Name**: Keerthana V / ShadowFox Intern  
**Evaluation Date**: October 2026  
**Status Legend**:
- `[COMPLETED]`: Fully implemented, run, verified against actual data, and saved to repository.
- `[NEEDS MANUAL ACTION]`: Requires user's personal GitHub account, webcam recording, or Power BI Desktop UI clicks.
- `[BLOCKED]`: None.

---

## 1. Project 1: Beginner Level (Small Business Sales Performance Analysis)

| Task Item | Required Deliverable | Status | Verification & Evidence |
| :--- | :--- | :---: | :--- |
| **Dataset Preparation** | Raw dataset with deliberate real-world flaws (`raw_sales_data.csv`) | **COMPLETED** | Generated 1,270 records with mixed date formats, duplicates, and missing values. Verified at `Beginner_Sales_Analysis/data/raw_sales_data.csv`. |
| **Data Cleaning** | Cleaning script (`data_cleaning.py`) & clean dataset (`cleaned_sales_data.csv`) | **COMPLETED** | Automated pipeline removed 20 duplicates, imputed 37 missing payments, cleaned currency symbols, validated 1,250 rows. Logged in `analysis/data_cleaning_audit.md`. |
| **Exploratory Data Analysis** | Core KPI calculations & summary tables (`sales_analysis.py`) | **COMPLETED** | Derived Revenue ($180,936.50), Profit ($87,709.30), Margin (48.48%), AOV ($144.75). Exported to `analysis/analysis_results.csv`. |
| **High-Resolution Visualizations** | Visual charts in `charts/` | **COMPLETED** | 5 high-resolution charts generated (Monthly trends, Category margins, Regional performance, Top/Bottom products, Payment distribution). |
| **Spreadsheet Workbook & Dashboard** | Automated 4-tab Excel workbook (`Small_Business_Sales_Dashboard.xlsx`) | **COMPLETED** | Generated using `openpyxl` with Raw Data, Cleaned Data, dynamic Excel formulas (`SUM`, `SUMIFS`, `AVERAGE`), KPI cards, and embedded charts. |
| **Documentation & Reports** | `insights_and_recommendations.md`, `README.md`, `requirements.txt` | **COMPLETED** | Complete strategic reporting, formulas, and installation guide verified. |

---

## 2. Project 2: Intermediate Level (Customer Behaviour, Revenue, and Retention Analytics)

| Task Item | Required Deliverable | Status | Verification & Evidence |
| :--- | :--- | :---: | :--- |
| **Dataset Acquisition & Synthesis** | Multi-year transaction log (`raw_customer_data.csv`) | **COMPLETED** | 2,336 raw transactions across 850 customers spanning Jan 2023 – Dec 2024. |
| **Data Cleaning & Cohort Tagging** | Cleaning pipeline (`customer_cleaning.py`) & `cleaned_customer_data.csv` | **COMPLETED** | Removed 30 duplicates, engineered `Cohort_Month` and `Cohort_Index`, validated 2,306 clean transactions. |
| **Customer Behavior Analytics** | Repeat vs. One-Time Customer Analysis | **COMPLETED** | Repeat customers (46.94% of base) generate 80.88% of revenue ($264,508.51). One-time buyers generate 19.12%. |
| **RFM Segmentation** | 8-Segment RFM framework (`customer_segments.csv`) | **COMPLETED** | Quintile scored across Recency, Frequency, Monetary. Top 200 Champions generate 49.83% of revenue ($162,963.95). |
| **Cohort Retention Matrix** | 24-Month cohort retention matrix & heatmap | **COMPLETED** | Computed customer count and retention rate percentages across 24 cohorts. Saved in `analysis/cohort_retention_matrix.csv`. |
| **Relational SQL Database** | SQLite database (`customer_analytics.db`) & schema | **COMPLETED** | Normalized into `customers`, `products`, and `transactions` tables. Verified in `Intermediate_Customer_Analytics/data/customer_analytics.db`. |
| **Advanced SQL Execution** | 10 Production SQL queries with Window Functions & CTEs | **COMPLETED** | Executed in SQLite (`execute_sql_queries.py`). Verified `DENSE_RANK()`, `LAG()`, `NTILE(5)`, running totals, and exported 10 CSV reports to `reports/`. |
| **Documentation & Reports** | `business_insights.md`, `recommendations.md`, `README.md` | **COMPLETED** | Detailed analytical findings, operational retention pillars, and GitHub documentation complete. |

---

## 3. Project 3: Advanced Level (Executive BI Dashboard Using Power BI)

| Task Item | Required Deliverable | Status | Verification & Evidence |
| :--- | :--- | :---: | :--- |
| **Dataset Selection & Rationale** | Multi-year enterprise operations dataset (`raw_business_data.csv`) | **COMPLETED** | Enterprise sales, logistics, and target dataset spanning 2022–2024 (4,235 raw records) justified for star schema and DAX. |
| **Data Transformation & Star Schema** | Transformation pipeline (`data_transformation.py`) & Star Schema CSVs | **COMPLETED** | Exported `Fact_Orders` (4,200 rows), `Fact_Targets` (1,080 rows), `Dim_Date` (1,096 days), `Dim_Products` (1,241 SKUs), `Dim_Customers` (600), `Dim_Geography` (10). |
| **DAX Measures Library** | 28 commented DAX measures (`powerbi_measures.dax`) | **COMPLETED** | Programmed Time Intelligence (`TOTALYTD`, `SAMEPERIODLASTYEAR`), Margin %, SLA Compliance %, Budget Target Variance, and Dynamic Ranking. |
| **Data Dictionary & Schema Mapping** | Schema documentation (`data_dictionary.md`) | **COMPLETED** | Complete entity relationship diagram, column types, descriptions, and foreign key mappings. |
| **Dashboard Design System** | Visual design guide & wireframes (`dashboard_design.md`) | **COMPLETED** | Dark-mode palette (`#0B192C`, `#1E3E62`, `#FF6500`), 3 page wireframes, KPI card coordinates, and drill-through paths. |
| **Implementation Guide** | Step-by-step Power BI Desktop instructions (`powerbi_implementation_guide.md`) | **COMPLETED** | Detailed walkthrough for loading CSVs, connecting relationships, pasting DAX measures, and configuring visual cards. |
| **Dashboard Mockup Renders** | 300 DPI high-resolution visual renders | **COMPLETED** | Executive overview and Logistics SLA compliance page renders saved to `dashboard/` and `charts/`. |
| **Executive Reports & Documentation** | `executive_summary.md`, `recommendations.md`, `README.md` | **COMPLETED** | Full 3-year performance review ($2.93M sales, 38.4% margin, 68.8% on-time SLA) and strategic recommendations. |
| **Power BI Desktop Manual Assembly** | Final `.pbix` file creation | **NEEDS MANUAL ACTION** | Open Power BI Desktop on your personal machine and follow `powerbi_implementation_guide.md` using the prepared CSVs and DAX library. |

---

## 4. Final Submission & Repository Packaging

| Task Item | Required Deliverable | Status | Verification & Evidence |
| :--- | :--- | :---: | :--- |
| **Root Repository Overview** | Root `README.md`, `requirements.txt`, `.gitignore` | **COMPLETED** | Unified portfolio documentation connecting all three levels. |
| **Video Presentation Script** | 3–5 Minute timed walkthrough script (`video_presentation_script.md`) | **COMPLETED** | Complete word-for-word transcript with slide timestamps, camera cues, and key metric callouts. |
| **Screenshot Guide** | Visual artifact checklist (`screenshot_guide.md`) | **COMPLETED** | Clear list of exact screenshots to capture from Excel, SQLite, and Power BI. |
| **GitHub Upload Guide** | Step-by-step Git & GitHub command guide (`github_upload_guide.md`) | **COMPLETED** | Instructions for staging, committing, and pushing the repository. |
| **Self-Recorded Video & Drive Link** | Candidate video recording (3–5 min) | **NEEDS MANUAL ACTION** | Record yourself using Loom, OBS, or Zoom reading the provided script, upload to Google Drive, set sharing to "Anyone with link can view". |
| **GitHub Repository Push** | Public GitHub repository URL | **NEEDS MANUAL ACTION** | Run the provided git push commands to link your local folder to your personal GitHub account. |
