# Small Business Sales Performance Analysis & Dashboard

**ShadowFox Data Analyst Internship — Project 1 (Beginner Level)**  
**Author**: ShadowFox Data Analyst Intern  
**Tools**: Python 3.12, Pandas, NumPy, Matplotlib, Seaborn, Excel (openpyxl)  
**Status**: Completed and Validated  

---

## 1. Project Title & Business Problem

### Project Title
Small Business Sales Performance Analysis and Spreadsheet Dashboard

### Business Problem
A retail small business operates across multiple product categories (Furniture, Electronics, Office Supplies, Home & Kitchen) and five geographical regions. The executive leadership lacks visibility into sales trends, category margins, seasonal demand spikes, and product-level profitability. Furthermore, the incoming sales records suffer from real-world data quality issues (duplicate orders, inconsistent text casing, mixed date formats, and missing payment attributes). 

### Objectives
1. Build an automated Python data cleaning pipeline to audit and sanitize raw operational records.
2. Conduct exploratory data analysis to calculate core financial and operational KPIs.
3. Identify seasonal revenue trajectories, high-margin product opportunities, and regional dynamics.
4. Construct an automated, interactive Excel workbook with formula-driven KPI cards, category summary tables, and embedded high-resolution dashboards.
5. Provide actionable, data-backed strategic recommendations for executive leadership.

---

## 2. Dataset Description & Source

- **Dataset Type**: Small Business Transaction Log (Fiscal Year 2024).
- **Source**: Structured retail transaction dataset designed to simulate omnichannel small business sales with injected real-world data imperfections.
- **Attributes**:
  - `Order ID`: Unique alphanumeric identifier (e.g., ORD-2024-1001).
  - `Order Date`: Transaction timestamp in mixed raw formats (`YYYY-MM-DD`, `MM/DD/YYYY`, `DD-MM-YYYY`).
  - `Product`: Item name across 15 distinct catalog offerings.
  - `Category`: High-level business vertical (Furniture, Electronics, Office Supplies, Home & Kitchen).
  - `Quantity`: Number of units purchased per transaction (1 to 8 units).
  - `Unit Price`: Retail selling price per unit.
  - `Cost`: Production / wholesale acquisition cost.
  - `Sales`: Gross transaction amount (`Quantity * Unit Price`).
  - `Profit`: Net return (`Sales - Cost`).
  - `Region`: Geographic sales territory (North, South, East, West, Central).
  - `Payment Method`: Customer payment gateway (Credit Card, Debit Card, PayPal, Cash on Delivery, Bank Transfer).

---

## 3. Folder Structure

```
Beginner_Sales_Analysis/
|-- data/
|   |-- raw_sales_data.csv               # 1,270 raw records with imperfections
|   |-- cleaned_sales_data.csv           # 1,250 validated clean transactions
|
|-- scripts/
|   |-- generate_raw_data.py             # Reproducible raw data generation script
|   |-- data_cleaning.py                 # Automated audit, cleaning & validation pipeline
|   |-- sales_analysis.py                # EDA, KPI engine, chart generator & Excel builder
|
|-- analysis/
|   |-- data_cleaning_audit.md           # Audit trail of cleaning operations
|   |-- analysis_results.csv             # Core KPI metrics summary
|   |-- monthly_sales_summary.csv        # Month-by-month financial performance
|   |-- category_sales_summary.csv       # Category revenue, profit, and margins
|   |-- regional_sales_summary.csv       # Geographic performance comparison
|   |-- product_performance_summary.csv  # 15-product ranking by revenue & margin
|   |-- payment_method_summary.csv       # Payment method distribution
|   |-- insights_and_recommendations.md  # Detailed analytical business report
|
|-- charts/
|   |-- monthly_sales_trend.png          # High-resolution monthly revenue & profit trend
|   |-- category_sales_profit.png        # Dual-axis category sales vs profit margin
|   |-- regional_performance.png         # Horizontal bar chart of regional sales & profit
|   |-- top_bottom_products.png          # Comparison of top 5 vs bottom 5 products
|   |-- payment_method_distribution.png  # Donut chart of payment gateway revenue share
|
|-- dashboard/
|   |-- Small_Business_Sales_Dashboard.xlsx # 4-sheet formatted Excel workbook
|
|-- README.md                            # Comprehensive project documentation
|-- requirements.txt                     # Python library dependencies
```

---

## 4. Data Cleaning Pipeline

The automated script [`scripts/data_cleaning.py`](file:///C:/Users/keert/.gemini/antigravity-ide/scratch/ShadowFox_Data_Analyst_Internship/Beginner_Sales_Analysis/scripts/data_cleaning.py) performs the following seven steps:

1. **Duplicate Detection & Removal**:
   - Detected 20 duplicate orders across the 1,270 raw entries.
   - Preserved initial valid records and dropped duplicates, leaving exactly 1,250 clean rows.
2. **Text Normalization**:
   - Trimmed leading/trailing whitespaces across `Product`, `Category`, and `Region`.
   - Converted `Category` and `Region` into proper Title Case.
   - Standardized typographical anomalies (e.g., `'Office-Supplies'` -> `'Office Supplies'`).
3. **Missing Value Imputation**:
   - Identified 37 null entries in `Payment Method`.
   - Imputed missing entries with `'Not Specified'` to maintain categorical transparency without dropping transaction revenue.
4. **Data Type Standardization**:
   - Cleaned `Unit Price` by stripping currency strings (`'$'`) and casting to `float64`.
   - Enforced integer typing on `Quantity` and decimal precision on `Sales`, `Cost`, and `Profit`.
5. **Date Standardization**:
   - Parsed mixed date representations into unified ISO-8601 (`YYYY-MM-DD`).
6. **Feature Engineering**:
   - Derived `Year`, `Month`, `Month Name`, `Year-Month`, `Quarter`, and `Profit Margin %`.
7. **Mathematical Integrity Verification**:
   - Validated that `Profit == Sales - Cost` and `Sales == Quantity * Unit Price`.

---

## 5. Analytical Methodology & KPIs

### Core Business Formulas
$$\text{Average Order Value (AOV)} = \frac{\text{Total Revenue}}{\text{Total Orders}}$$

$$\text{Profit Margin (\%)} = \left(\frac{\text{Total Profit}}{\text{Total Revenue}}\right) \times 100$$

$$\text{Average Profit Per Order} = \frac{\text{Total Profit}}{\text{Total Orders}}$$

$$\text{Month-over-Month Growth (\%)} = \left(\frac{\text{Sales}_{t} - \text{Sales}_{t-1}}{\text{Sales}_{t-1}}\right) \times 100$$

### Verified KPI Output Table
*Derived directly from the verified dataset:*

| KPI Metric | Exact Value | Business Interpretation |
| :--- | :---: | :--- |
| **Total Revenue** | **$180,936.50** | Aggregate sales across FY 2024 |
| **Total Production Cost** | **$93,227.20** | Total Cost of Goods Sold (COGS) |
| **Total Net Profit** | **$87,709.30** | Net operational earnings |
| **Overall Profit Margin** | **48.48%** | Highly profitable business unit economics |
| **Total Orders** | **1,250** | Verified customer order volume |
| **Total Units Sold** | **2,662** | Product volume shipped |
| **Average Order Value (AOV)** | **$144.75** | Average spend per customer order |
| **Average Profit Per Order** | **$70.17** | Net yield returned per checkout |

---

## 6. Key Findings Based on Actual Outputs

1. **Seasonality & Q4 Surge**:
   - Revenue peaked in **November ($23,036.07)** and **December ($19,229.88)**, driven by high basket sizes (AOV hit $213.30 in Nov).
   - The mid-year low occurred in **June ($9,972.42)** and **July ($10,540.87)**, indicating a seasonal summer drop-off.
2. **Category Dynamics**:
   - **Furniture** is the largest revenue contributor (**$74,359.00**, 41.10% share), followed by **Electronics** (**$68,702.12**, 37.97% share). Together, they comprise **79.07%** of business volume.
   - **Home & Kitchen** commands the highest margin (**56.45%**), followed by **Office Supplies** (**51.66%**).
3. **Product Highlights**:
   - Top 3 revenue drivers: **Ergonomic Office Chair ($43,281.00)**, **Standing Desk Converter ($31,078.00)**, and **Noise-Cancelling Headphones ($28,198.12)**.
   - Lowest revenue products: **A4 Copy Paper ($1,623.50)** and **Gel Ink Pens ($1,974.48)**; however, Gel Ink Pens generate the highest profit margin in the entire catalog (**67.67%**).
4. **Territory Distribution**:
   - Performance across territories is evenly balanced: West ($38,351.59), Central ($37,386.35), East ($37,015.36), North ($34,160.88), South ($34,022.32). Profit margins remain stable across all regions (47.8% – 49.0%).

---

## 7. Spreadsheet & Excel Dashboard Architecture

The generated workbook [`dashboard/Small_Business_Sales_Dashboard.xlsx`](file:///C:/Users/keert/.gemini/antigravity-ide/scratch/ShadowFox_Data_Analyst_Internship/Beginner_Sales_Analysis/dashboard/Small_Business_Sales_Dashboard.xlsx) features four specialized worksheets:

1. **Sheet 1: `Raw Data`**:
   - Preserves unedited original raw records (1,270 rows) for compliance and audit trail.
2. **Sheet 2: `Cleaned Data`**:
   - Fully standardized data (1,250 rows) with accounting number formatting (`$#,##0.00`), styled header rows, and formatted borders.
3. **Sheet 3: `Analysis`**:
   - Live Excel formulas calculating executive metrics:
     - `=SUM('Cleaned Data'!G2:G1251)` (Total Revenue)
     - `=SUM('Cleaned Data'!I2:I1251)` (Total Profit)
     - `=COUNTA('Cleaned Data'!A2:A1251)` (Total Orders)
     - `=C5/C8` (Average Order Value)
     - `=(C7/C5)*100` (Profit Margin %)
     - `=SUMIFS('Cleaned Data'!$G$2:$G$1251, 'Cleaned Data'!$D$2:$D$1251, A16)` (Category Revenue)
4. **Sheet 4: `Dashboard`**:
   - Executive dark-mode banner, formatted KPI cards, monthly performance tables, and embedded high-resolution visual charts.

---

## 8. Strategic Business Recommendations

1. **Cross-Sell High-Margin Accessories**:
   - Bundle high-revenue, lower-margin furniture (Ergonomic Office Chair, Standing Desk) with high-margin accessories (Gel Ink Pens at 67.7% margin, Mesh Desk Organizer at 60.0% margin) to increase average basket margin.
2. **Launch a Mid-Year Summer Sale**:
   - Run a targeted promotional campaign in June/July to boost volume during the annual trough ($9.9k - $10.5k revenue).
3. **Proactive Q4 Supply Chain Planning**:
   - Because Q4 volume surges by 45%, trigger supply reorders for top items (Chairs, Desks, Headphones) 90 days in advance (by August) to avoid stockouts.
4. **Territory Retargeting**:
   - Expand corporate B2B sales outreach in the North and South territories to bring them in line with the top-performing West region.

---

## 9. Installation & Execution Guide

### Prerequisites
- Python 3.9+ (Python 3.12 recommended)
- Microsoft Excel or LibreOffice Calc (for viewing `.xlsx`)

### Step-by-Step Execution
```bash
# 1. Navigate to the project directory
cd Beginner_Sales_Analysis

# 2. Install dependencies
pip install -r requirements.txt

# 3. (Optional) Re-generate raw data
python scripts/generate_raw_data.py

# 4. Run data cleaning pipeline
python scripts/data_cleaning.py

# 5. Run exploratory data analysis and build Excel dashboard
python scripts/sales_analysis.py
```

---

## 10. Project Verification & Limitations

- **Verification**: All numbers in this report, the CSV files, and the Excel sheets were verified through Python execution.
- **Limitations**: The dataset spans one fiscal year (2024), which provides seasonal insight within the year but precludes multi-year Year-over-Year (YoY) comparison.
- **Future Improvements**: Connect real-time POS or SQL databases to auto-refresh the Excel workbook via Power Query or Python scheduling.
