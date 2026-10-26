# Executive Business Intelligence Dashboard Using Power BI

**ShadowFox Data Analyst Internship — Project 3 (Advanced Level)**  
**Author**: ShadowFox Data Analyst Intern  
**Tools**: Power BI Desktop, DAX, Python 3.12, Pandas, NumPy, Star Schema Modeling  
**Status**: Completed and Validated  

---

## 1. Project Title & Business Problem

### Project Title
Executive Business Intelligence Dashboard Using Power BI

### Business Problem
A global commercial enterprise operates across multiple macro trade regions (North America, Europe, Asia-Pacific) distributing commercial technology, office furniture, and operational supplies. Executive leadership requires an integrated, multi-level Business Intelligence reporting solution to:
- Monitor multi-year financial trajectories and Year-over-Year (YoY) revenue velocity.
- Track gross sales against regional and departmental budget targets.
- Evaluate supply chain health, order delivery duration, and On-Time Delivery SLA compliance.
- Support interactive drill-down from macro markets down to individual cities, and from commercial categories down to product SKUs.

### Objectives
1. Build a robust data transformation script in Python to audit, sanitize, and engineer logistics features from multi-year records.
2. Structure and export a certified **6-Table Star Schema** (`Fact_Orders`, `Fact_Targets`, `Dim_Date`, `Dim_Products`, `Dim_Customers`, `Dim_Geography`).
3. Author a production-grade library of **28 DAX measures** covering Time Intelligence (`TOTALYTD`, `SAMEPERIODLASTYEAR`), Budget Variance, SLA tracking, and dynamic ranking.
4. Establish an executive dark-mode design system with visual wireframes and high-resolution dashboard page renders.
5. Provide a step-by-step implementation guide for Microsoft Power BI Desktop.
6. Deliver strategic operational recommendations for executive leadership.

---

## 2. Dataset Selection & Justification

- **Chosen Architecture**: Global Enterprise Retail Operations Log (FY 2022 – FY 2024).
- **Justification**:
  - Contains rich multidimensional entities across time, geography, customers, products, and budget targets.
  - Supports true Star Schema modeling with $1:\text{Many}$ relationships.
  - Unlocks sophisticated DAX Time Intelligence (YoY variance, MTD, rolling averages) and logistical SLA performance tracking.
- **Dataset Scale**:
  - `Fact_Orders`: 4,200 line-item transactions.
  - `Fact_Targets`: 1,080 monthly budget targets.
  - `Dim_Date`: 1,096 continuous calendar days.
  - `Dim_Products`: 1,241 product SKUs across 17 sub-categories.
  - `Dim_Customers`: 600 verified account profiles.
  - `Dim_Geography`: 10 global trade hub territories.

---

## 3. Folder Structure

```
Advanced_PowerBI_Dashboard/
|-- data/
|   |-- raw_business_data.csv          # 4,235 raw records with real-world flaws
|   |-- cleaned_business_data.csv      # 4,200 verified clean records
|   |-- Fact_Orders.csv                # Central transaction fact table
|   |-- Fact_Targets.csv               # Monthly budget targets table
|   |-- Dim_Date.csv                   # Continuous calendar dimension
|   |-- Dim_Products.csv               # Product SKU and hierarchy dimension
|   |-- Dim_Customers.csv              # Customer segment dimension
|   |-- Dim_Geography.csv              # Geographic hierarchy dimension
|
|-- scripts/
|   |-- generate_advanced_raw_data.py  # Multi-year raw data generator
|   |-- data_transformation.py         # Cleaning, feature engineering & star schema builder
|
|-- dax/
|   |-- powerbi_measures.dax           # 28 production DAX measures with documentation
|
|-- dashboard/
|   |-- data_dictionary.md             # Complete data dictionary & schema mapping
|   |-- dashboard_design.md            # Visual layout, design system & wireframes
|   |-- powerbi_implementation_guide.md# Step-by-step Power BI Desktop build guide
|   |-- PowerBI_Executive_Dashboard_Render.png # 300 DPI executive dashboard mockup
|
|-- reports/
|   |-- annual_executive_summary.csv   # Annual financial scorecard
|   |-- executive_summary.md           # C-suite executive briefing report
|   |-- recommendations.md             # Operational & supply chain roadmap
|
|-- charts/
|   |-- executive_overview_page.png    # Page 1 visual render
|   |-- logistics_sla_compliance.png   # Page 2 visual render
|
|-- README.md                          # Comprehensive project documentation
|-- requirements.txt                   # Library dependencies
```

---

## 4. Star Schema Architecture

```
Dim_Date (1) --------< (*) Fact_Orders (*) >-------- (1) Dim_Products
Dim_Customers (1) ----< (*) Fact_Orders (*) >-------- (1) Dim_Geography
Dim_Date (1) --------< (*) Fact_Targets
```

All relationships are configured with **$1:\text{Many}$ ($1:*$)** cardinality and **Single** cross-filter direction, preventing circular dependencies and ensuring optimal DAX query evaluation.

---

## 5. Core KPIs & Analytical Findings

*Derived from the verified 3-year enterprise dataset:*

| KPI Metric | Verified Value | Benchmark / Target | Assessment |
| :--- | :---: | :---: | :--- |
| **Total Sales Revenue** | **$2,929,341.17** | Baseline | +144% 3-Year Expansion |
| **Total Operating Profit** | **$1,124,915.67** | Baseline | Outstanding earnings quality |
| **Consolidated Margin** | **38.40%** | $\ge 35.0\%$ | Exceeded corporate margin goal |
| **Total Orders** | **4,200** | — | High transaction velocity |
| **On-Time Delivery Rate** | **68.83%** | $\ge 85.0\%$ | **Underperforming SLA Target** |
| **Overall Return Rate** | **4.31%** | $< 5.0\%$ | Healthy quality baseline |
| **Avg Fulfillment Duration** | **3.2 Days** | $\le 4.0\text{ Days}$ | Fast physical dispatch |

### Annual Progression
- **FY 2022**: $542,002.70 Sales | $206,996.20 Profit (38.19% Margin) | 819 Orders
- **FY 2023**: $1,064,395.62 Sales (**+96.38% YoY**) | $404,366.12 Profit (37.99% Margin) | 1,489 Orders
- **FY 2024**: $1,322,942.85 Sales (**+24.29% YoY**) | $513,553.35 Profit (38.82% Margin) | 1,892 Orders

---

## 6. DAX Implementation Highlights

The accompanying [`dax/powerbi_measures.dax`](file:///C:/Users/keert/.gemini/antigravity-ide/scratch/ShadowFox_Data_Analyst_Internship/Advanced_PowerBI_Dashboard/dax/powerbi_measures.dax) file contains 28 measures including:

```dax
// Year-to-Date (YTD) Sales
Sales YTD = TOTALYTD([Total Sales], Dim_Date[Date])

// Prior Year Sales
Sales PY = CALCULATE([Total Sales], SAMEPERIODLASTYEAR(Dim_Date[Date]))

// Year-over-Year Growth %
Sales YoY Growth % = DIVIDE([Total Sales] - [Sales PY], [Sales PY], 0)

// On-Time Delivery Compliance
On-Time Delivery % = DIVIDE(SUM(Fact_Orders[On_Time_Flag]), COUNTROWS(Fact_Orders), 0)

// Budget Target Achievement %
Sales Target Achievement % = DIVIDE([Total Sales], [Total Target Sales], 0)
```

---

## 7. Strategic Recommendations

1. **Overhaul Standard Freight 3PL Carrier Contracts**:
   - Standard Class represents 58% of volume but achieves only 59.2% on-time delivery. Enforce financial penalty clauses for delivery delays past 6 days.
2. **Promote B2B Office Supplies Bundling**:
   - Office Supplies yields a 41.2% profit margin. Bundle stationery and paper consumables with commercial tech hardware to lift average basket margin.
3. **White-Glove Onboarding for Heavy Machinery**:
   - Commercial copiers and printers have an elevated return rate of 7.8%. Provide digital setup guides and virtual installation assistance.

---

## 8. How to Open and Build in Power BI Desktop

Follow the complete step-by-step instructions in [`dashboard/powerbi_implementation_guide.md`](file:///C:/Users/keert/.gemini/antigravity-ide/scratch/ShadowFox_Data_Analyst_Internship/Advanced_PowerBI_Dashboard/dashboard/powerbi_implementation_guide.md):
1. Ingest all 6 CSV files from `Advanced_PowerBI_Dashboard/data/`.
2. Connect relationships in Model view as outlined in the Star Schema.
3. Mark `Dim_Date` as the official Date Table.
4. Copy and paste DAX measures from `Advanced_PowerBI_Dashboard/dax/powerbi_measures.dax`.
5. Arrange canvas visuals using the coordinates and hex color tokens defined in `dashboard/dashboard_design.md`.
6. Save report as `Global_Enterprise_Executive_Dashboard.pbix`.
