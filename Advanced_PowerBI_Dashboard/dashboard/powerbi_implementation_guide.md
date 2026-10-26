# Power BI Desktop: Step-by-Step Implementation Guide

**Project**: Advanced Level - Executive Business Intelligence Dashboard  
**Author**: ShadowFox Data Analyst Intern  
**Target Environment**: Microsoft Power BI Desktop (Free / Pro)  
**Data Model**: Certified 6-Table Star Schema  
**Date**: October 2026  

---

## 1. Prerequisites & Environment Setup

1. Download and install **Microsoft Power BI Desktop** (Free download from [microsoft.com/powerbi](https://www.microsoft.com/powerbi) or the Microsoft Store).
2. Locate the prepared data files generated in your project folder:
   - `Advanced_PowerBI_Dashboard/data/Fact_Orders.csv`
   - `Advanced_PowerBI_Dashboard/data/Fact_Targets.csv`
   - `Advanced_PowerBI_Dashboard/data/Dim_Date.csv`
   - `Advanced_PowerBI_Dashboard/data/Dim_Products.csv`
   - `Advanced_PowerBI_Dashboard/data/Dim_Customers.csv`
   - `Advanced_PowerBI_Dashboard/data/Dim_Geography.csv`
   - `Advanced_PowerBI_Dashboard/dax/powerbi_measures.dax`

---

## 2. Step 1: Ingest Data via Power Query

1. Open Power BI Desktop and start with a **Blank Report**.
2. Click **Home** > **Get Data** > **Text/CSV**.
3. Select and load each of the 6 files sequentially:
   - Load `Dim_Date.csv` -> Verify `Date` is typed as **Date**.
   - Load `Dim_Customers.csv` -> Verify `Customer_ID` is **Text**.
   - Load `Dim_Products.csv` -> Verify `Product_ID` is **Text**.
   - Load `Dim_Geography.csv` -> Verify `Geography_ID` is **Text**.
   - Load `Fact_Orders.csv` -> Verify `Sales`, `Profit`, and `Shipping_Cost` are **Decimal Number**; `Quantity` and `Delivery_Days` are **Whole Number**.
   - Load `Fact_Targets.csv` -> Verify `Target_Sales` and `Target_Profit` are **Decimal Number**.
4. In the Power Query ribbon, click **Close & Apply**.

---

## 3. Step 2: Establish Model Relationships (Star Schema)

1. Switch to the **Model View** (icon on the left navigation bar).
2. Configure the following **1-to-Many ($1:*$)** single-direction relationships:

| From Table (Dimension) | Primary Key Column | To Table (Fact) | Foreign Key Column | Cardinality | Cross Filter |
| :--- | :--- | :--- | :--- | :---: | :---: |
| `Dim_Date` | `Date` | `Fact_Orders` | `Order_Date` | $1:*$ | Single |
| `Dim_Customers` | `Customer_ID` | `Fact_Orders` | `Customer_ID` | $1:*$ | Single |
| `Dim_Products` | `Product_ID` | `Fact_Orders` | `Product_ID` | $1:*$ | Single |
| `Dim_Geography` | `Geography_ID` | `Fact_Orders` | `Geography_ID` | $1:*$ | Single |
| `Dim_Date` | `Date` | `Fact_Targets` | `Target_Month` | $1:*$ | Single |

3. **Mark Date Table**:
   - Right-click `Dim_Date` in the Data pane > Select **Mark as date table** > Select `Date` column > Click **OK**.

---

## 4. Step 3: Implement DAX Measures Table

1. In the **Home** tab, click **Enter Data**.
2. Name the table `_Measures` and click **Load**.
3. Open [`Advanced_PowerBI_Dashboard/dax/powerbi_measures.dax`](file:///C:/Users/keert/.gemini/antigravity-ide/scratch/ShadowFox_Data_Analyst_Internship/Advanced_PowerBI_Dashboard/dax/powerbi_measures.dax).
4. Right-click `_Measures` in the Data pane > Select **New measure**.
5. Copy and paste each measure:
   - Core: `Total Sales`, `Total Profit`, `Profit Margin %`, `Total Orders`.
   - Time Intelligence: `Sales YTD`, `Sales PY`, `Sales YoY Growth %`.
   - Logistics: `On-Time Delivery %`, `Return Rate %`, `Avg Delivery Days`.
   - Budget Variance: `Total Target Sales`, `Sales Target Variance`, `Sales Target Achievement %`.
6. Set the formatting for each measure in the **Measure Tools** ribbon:
   - Currency (`$#,##0`): `Total Sales`, `Total Profit`, `Sales YTD`, `Sales PY`.
   - Percentage (`0.0%`): `Profit Margin %`, `Sales YoY Growth %`, `On-Time Delivery %`, `Return Rate %`.

---

## 5. Step 4: Build Report Page 1 — Executive Overview

1. Rename the page tab to **Executive Overview**.
2. **Page Background**:
   - Click Canvas > **Format Page** > **Canvas background** > Color: `#0B192C` (Transparency: 0%).
3. **KPI Cards (Top Banner)**:
   - Insert a **Card (New)** or 5 individual **Card** visuals.
   - Field 1: `Total Sales` ($2.93M) | Subtitle: `Sales YoY Growth %` (+24.3%).
   - Field 2: `Total Profit` ($1.12M) | Subtitle: Margin 38.4%.
   - Field 3: `On-Time Delivery %` (68.8%) | Target: 85.0%.
   - Field 4: `Return Rate %` (4.3%) | Target: <5.0%.
   - Format: Background `#1E3E62`, Font Color `#FFFFFF`, Metric Size 24pt Bold.
4. **Visual 1: Monthly Revenue Trajectory**:
   - Visual Type: **Line Chart**.
   - X-axis: `Dim_Date[Month_Name]` (Sorted by `Dim_Date[Month_Number]`).
   - Y-axis: `[Total Sales]`.
   - Legend: `Dim_Date[Year]`.
   - Line Colors: 2022 (`#94A3B8`), 2023 (`#38BDF8`), 2024 (`#FF6500`).
5. **Visual 2: Category Revenue Breakdown**:
   - Visual Type: **Donut Chart**.
   - Legend: `Dim_Products[Category]`.
   - Values: `[Total Sales]`.
   - Colors: Technology (`#3B82F6`), Furniture (`#10B981`), Office Supplies (`#F59E0B`).
6. **Visual 3: Regional Sales & Profit**:
   - Visual Type: **Clustered Column Chart**.
   - X-axis: `Dim_Geography[Region]`.
   - Y-axis: `[Total Sales]` and `[Total Profit]`.
7. **Slicers (Top Right)**:
   - Add Slicer: `Dim_Date[Year]` (Dropdown / Tile).
   - Add Slicer: `Dim_Geography[Market]` (Dropdown).

---

## 6. Step 5: Build Report Page 2 — Logistics & Operational SLA

1. Add a new page tab: **Logistics & SLA Compliance**.
2. Background: `#0B192C`.
3. **Visual 4: Delivery Duration by Ship Mode**:
   - Visual Type: **Clustered Bar Chart**.
   - Y-axis: `Fact_Orders[Ship_Mode]`.
   - X-axis: `[Avg Delivery Days]`.
   - Data Labels: On.
4. **Visual 5: SLA Compliance Rate**:
   - Visual Type: **Clustered Bar Chart**.
   - Y-axis: `Fact_Orders[Ship_Mode]`.
   - X-axis: `[On-Time Delivery %]`.
   - Color: `#10B981`.
5. **Visual 6: Territory SLA Heatmap**:
   - Visual Type: **Matrix Visual**.
   - Rows: `Dim_Geography[Region]`.
   - Columns: `Fact_Orders[Ship_Mode]`.
   - Values: `[On-Time Delivery %]`, `[Return Rate %]`.
   - Conditional Formatting: Background color rules (Green for $\ge 75\%$, Red for $<60\%$).

---

## 7. Step 6: Build Report Page 3 — Product & Customer Deep Dive

1. Add a new page tab: **Product Deep Dive**.
2. **Drill-Through Setup**:
   - In Page Format, expand **Page information** > Set **Page type** to **Drill-through**.
   - Add `Dim_Products[Category]` to the Drill-through fields.
3. **Visual 7: Sub-Category Profitability Matrix**:
   - Visual Type: **Matrix**.
   - Rows: `Dim_Products[Category]`, `Dim_Products[Sub_Category]`.
   - Values: `[Total Sales]`, `[Total Profit]`, `[Profit Margin %]`.
4. **Visual 8: Top 10 Products Ranking**:
   - Visual Type: **Table Visual**.
   - Columns: `Dim_Products[Product_Name]`, `[Total Sales]`, `[Profit Margin %]`, `[Product Sales Rank]`.
   - Filter Pane: Add visual-level filter on `[Is Top 10 Product] == 1`.

---

## 8. Step 7: Final Validation & Saving

1. Click through all slicers (Year, Market, Category) to verify that cards, charts, and drill-downs cross-filter dynamically.
2. Click **File** > **Save As** > Save as `Global_Enterprise_Executive_Dashboard.pbix` in your `Advanced_PowerBI_Dashboard/dashboard/` folder.
3. Capture full-screen screenshots of the pages for inclusion in your GitHub portfolio README.
