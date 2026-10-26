# Enterprise Data Dictionary & Star Schema Model

**Project**: Advanced Level - Executive Business Intelligence Dashboard Using Power BI  
**Author**: ShadowFox Data Analyst Intern  
**Date**: October 2026  

---

## 1. Relational Star Schema Architecture

The data architecture is structured as a dimensional Star Schema optimized for high-performance analytical queries and DAX time-intelligence calculations in Power BI Desktop.

```
                    +-----------------------+
                    |       Dim_Date        |
                    +-----------------------+
                    | Date (PK)             |
                    | Year, Quarter, Month  |
                    +-----------+-----------+
                                | 1
                                |
                                | *
+--------------------+      +---+-------------------+      +--------------------+
|   Dim_Customers    |      |      Fact_Orders      |      |    Dim_Products    |
+--------------------+      +-----------------------+      +--------------------+
| Customer_ID (PK)   |1   * | Order_ID              | *   1| Product_ID (PK)    |
| Customer_Name      +------+ Order_Date (FK)       +------+ Product_Name       |
| Segment            |      | Ship_Date             |      | Category           |
+--------------------+      | Ship_Mode             |      | Sub_Category       |
                            | Customer_ID (FK)      |      +--------------------+
                            | Product_ID (FK)       |
+--------------------+      | Geography_ID (FK)     |      +--------------------+
|   Dim_Geography    |1   * | Sales                 | *   1|    Fact_Targets    |
+--------------------+------+ Quantity              |------+--------------------+
| Geography_ID (PK)  |      | Discount              |      | Target_Month       |
| City, State        |      | Profit                |      | Category, Region   |
| Region, Market     |      | Shipping_Cost         |      | Target_Sales       |
+--------------------+      | Returned              |      | Target_Profit      |
                            | Delivery_Days         |      +--------------------+
                            | On_Time_Flag          |
                            +-----------------------+
```

---

## 2. Table Schemas & Column Dictionaries

### Table 1: `Fact_Orders` (Central Fact Table)
- **Granularity**: One record per line-item order.
- **Record Count**: 4,200 rows.

| Column Name | Data Type | Nullable | Description / Business Logic |
| :--- | :--- | :---: | :--- |
| `Order_ID` | String (Alphanumeric) | No | Unique operational order reference (e.g., `CA-2024-100234`). |
| `Order_Date` | Date (`YYYY-MM-DD`) | No | Date when the customer confirmed checkout. Foreign Key -> `Dim_Date[Date]`. |
| `Ship_Date` | Date (`YYYY-MM-DD`) | No | Date when order physically departed distribution facility. |
| `Ship_Mode` | String (Categorical) | No | Delivery tier (`Standard Class`, `Second Class`, `First Class`, `Same Day`). |
| `Customer_ID` | String (Alphanumeric) | No | Foreign Key -> `Dim_Customers[Customer_ID]`. |
| `Product_ID` | String (Alphanumeric) | No | Foreign Key -> `Dim_Products[Product_ID]`. |
| `Geography_ID` | String (Alphanumeric) | No | Foreign Key -> `Dim_Geography[Geography_ID]`. |
| `Sales` | Decimal (Currency) | No | Gross billed revenue after customer discounts (`$#,##0.00`). |
| `Quantity` | Integer | No | Count of product units sold (1 to 6). |
| `Discount` | Decimal (Percentage) | No | Promotional discount percentage applied (0.00 to 0.30). |
| `Profit` | Decimal (Currency) | No | Net operational margin (`Sales - Cost`). |
| `Shipping_Cost`| Decimal (Currency) | No | Freight and logistical delivery fee paid. |
| `Returned` | String (`Yes`/`No`) | No | Indicator whether order was flagged for return/refund. |
| `Delivery_Days`| Integer | No | Elapsed fulfillment duration (`Ship_Date - Order_Date`). |
| `On_Time_Flag` | Integer (`0`/`1`) | No | Binary SLA compliance flag based on shipping service class. |

---

### Table 2: `Dim_Date` (Calendar Dimension)
- **Granularity**: One record per calendar day (Jan 1, 2022 to Dec 31, 2024).
- **Record Count**: 1,096 rows.

| Column Name | Data Type | Description |
| :--- | :--- | :--- |
| `Date` | Date (Primary Key) | Standard calendar date (`YYYY-MM-DD`). |
| `Year` | Integer | Calendar Year (`2022`, `2023`, `2024`). |
| `Quarter` | String | Calendar quarter label (`Q1`, `Q2`, `Q3`, `Q4`). |
| `Quarter_Year` | String | Period display (`Q1 2024`). |
| `Month_Number` | Integer | Month integer index (`1` to `12`). |
| `Month_Name` | String | 3-letter month abbreviation (`Jan`, `Feb`, ...). |
| `Month_Year` | String | Reporting month label (`Jan 2024`). |
| `Year_Month_Sort`| Integer | Chronological sort key (e.g., `202401`). |
| `Day_of_Week` | String | Day name (`Monday`, `Tuesday`, ...). |
| `Is_Weekend` | Integer | Binary weekend indicator (`1` for Sat/Sun, `0` otherwise). |
| `Fiscal_Year` | String | Corporate fiscal year (`FY2022`, `FY2023`, `FY2024`). |

---

### Table 3: `Dim_Products` (Product Dimension)
- **Granularity**: Unique product offerings across catalog.
- **Record Count**: 1,241 unique product configurations.

| Column Name | Data Type | Description |
| :--- | :--- | :--- |
| `Product_ID` | String (Primary Key) | Unique product SKU (e.g., `PRD-TE-PHO-124`). |
| `Product_Name` | String | Full commercial item description. |
| `Category` | String | Primary business vertical (`Technology`, `Furniture`, `Office Supplies`). |
| `Sub_Category` | String | Department category (17 distinct sub-categories). |

---

### Table 4: `Dim_Customers` (Customer Dimension)
- **Granularity**: Distinct customer buyer profile.
- **Record Count**: 600 records.

| Column Name | Data Type | Description |
| :--- | :--- | :--- |
| `Customer_ID` | String (Primary Key) | Customer unique account reference (e.g., `CUST-2001`). |
| `Customer_Name` | String | Customer account full name. |
| `Segment` | String | Market customer tier (`Consumer`, `Corporate`, `Home Office`). |

---

### Table 5: `Dim_Geography` (Territory Dimension)
- **Granularity**: Distinct logistical shipping hubs and territories.
- **Record Count**: 10 records.

| Column Name | Data Type | Description |
| :--- | :--- | :--- |
| `Geography_ID` | String (Primary Key) | Unique territory code (`GEO-100` to `GEO-109`). |
| `City` | String | Destination municipal metro center. |
| `State` | String | State / Province. |
| `Country` | String | Sovereign nation (`United States`, `United Kingdom`, `Germany`, etc.). |
| `Region` | String | Sales management territory (`US East`, `US West`, `EU West`, `APAC South`). |
| `Market` | String | Macro trade zone (`North America`, `Europe`, `Asia-Pacific`). |

---

### Table 6: `Fact_Targets` (Budget & Target Dimension)
- **Granularity**: Monthly sales and profit budget targets by Category and Region.
- **Record Count**: 1,080 rows.

| Column Name | Data Type | Description |
| :--- | :--- | :--- |
| `Target_Month` | Date | First day of target calendar month (`YYYY-MM-01`). |
| `Year_Month` | String | Month sort identifier (`YYYY-MM`). |
| `Category` | String | Product category budget target. |
| `Region` | String | Operational region target. |
| `Target_Sales` | Decimal (Currency) | Budgeted gross revenue objective. |
| `Target_Profit` | Decimal (Currency) | Budgeted net operating profit objective. |
