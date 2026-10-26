# Executive Business Intelligence Dashboard: Design Specification

**Project**: Advanced Level - Executive Business Intelligence Dashboard Using Power BI  
**Author**: ShadowFox Data Analyst Intern  
**Date**: October 2026  

---

## 1. Visual Design Philosophy & Aesthetics

This executive dashboard is engineered for C-suite decision-makers (CEO, COO, CFO, VP of Sales). The interface employs modern **executive dark-mode aesthetics** paired with high-contrast data visualization standards:

- **Minimalist Cognitive Load**: Critical numbers (KPIs) are immediately visible without scrolling.
- **Visual Hierarchy**: Core financial KPIs occupy the top banner, followed by macro trends, regional dynamics, and granular operational drill-downs.
- **Consistent Color Semantics**: Colors convey strict functional meaning—green indicates profit and SLA compliance; red signals negative variance and returns; orange highlights focal metrics.

---

## 2. Design System & Palette Tokens

| Token Name | Hex Code | Visual Application |
| :--- | :---: | :--- |
| **Canvas Background** | `#0B192C` | Deep Midnight Dark Canvas |
| **Container / Card Background** | `#1E3E62` | Surface cards with subtle 8px border radius |
| **Primary Metric Accent** | `#FF6500` | Active highlights, focus series, and KPI indicators |
| **Corporate Navy Accent** | `#0284C7` | Primary time series, line charts, and bar series |
| **Positive / Growth Green** | `#10B981` | Profit margins, positive YoY growth, On-Time SLA |
| **Warning / Alert Red** | `#DC2626` | Return rates, target shortfalls, supply delays |
| **Primary Text Header** | `#FFFFFF` | Large titles and KPI numeric card values |
| **Secondary Sub-Text** | `#94A3B8` | Axis labels, captions, footnotes, and legends |

**Typography**: Segoe UI / Segoe UI Semibold (standard Power BI native font family for cross-platform rendering).

---

## 3. Page Layout Wireframes & Visual Architecture

### Page 1: Executive Overview (`1920 x 1080` Canvas)

```
+---------------------------------------------------------------------------------------------------------+
| [LOGO] GLOBAL ENTERPRISE PERFORMANCE DASHBOARD | FY 2022 - 2024               [Year Slicer] [Market Slicer]|
+---------------------------------------------------------------------------------------------------------+
|  [TOTAL SALES]     |  [TOTAL PROFIT]    |  [PROFIT MARGIN]   |  [ON-TIME SLA]     |  [RETURN RATE]      |
|    $2.93M          |    $1.12M          |      38.4%         |      68.8%         |      4.3%           |
|    ▲ +24.3% YoY    |    ▲ +27.0% YoY    |    Target: 35.0%   |    Target: 85.0%   |    Target: <5.0%    |
+-----------------------------------------+--------------------+--------------------+---------------------+
|                                         |                                                               |
|  VISUAL 1: Monthly Revenue Trajectory   |  VISUAL 2: Category Revenue Breakdown                         |
|  (Line & Area Chart comparing           |  (Donut Chart: Technology 45%,                                |
|   2022 vs 2023 vs 2024 YoY Trends)      |   Furniture 34%, Office Supplies 21%)                         |
|                                         |                                                               |
+-----------------------------------------+--------------------+------------------------------------------+
|                                                              |                                          |
|  VISUAL 3: Regional Sales & Profit Comparison                |  VISUAL 4: Customer Segment Performance  |
|  (Clustered Column Chart across 10 Operational Territories)  |  (Horizontal Bar Chart: Consumer vs      |
|                                                              |   Corporate vs Home Office)              |
|                                                              |                                          |
+--------------------------------------------------------------+------------------------------------------+
```

---

### Page 2: Logistics & Operational SLA Compliance

```
+---------------------------------------------------------------------------------------------------------+
| LOGISTICS & FULFILLMENT MONITORING                                      [Ship Mode Slicer] [Date Range] |
+---------------------------------------------------------------------------------------------------------+
|  [AVG DELIVERY DAYS]   |  [ON-TIME ORDERS]    |  [LATE DELIVERIES]   |  [SHIPPING EXPENSE]              |
|       3.2 Days         |       2,891          |        1,309         |      $84,210                     |
+------------------------+----------------------+----------------------+----------------------------------+
|                                               |                                                         |
|  VISUAL 5: Average Delivery Days by Ship Mode |  VISUAL 6: On-Time Delivery SLA Compliance Rate (%)     |
|  - Same Day: 0.8 days                         |  - Same Day: 92.4% SLA Pass                             |
|  - First Class: 2.1 days                      |  - First Class: 78.6% SLA Pass                          |
|  - Second Class: 3.2 days                     |  - Second Class: 65.4% SLA Pass                         |
|  - Standard Class: 5.1 days                   |  - Standard Class: 59.2% SLA Pass                       |
|                                               |                                                         |
+-----------------------------------------------+---------------------------------------------------------+
|                                                                                                         |
|  VISUAL 7: Territory Delivery Heatmap & Late Order Distribution                                         |
|  (Matrix Visual: Region vs Ship Mode with conditional formatting on SLA pass/fail)                      |
|                                                                                                         |
+---------------------------------------------------------------------------------------------------------+
```

---

### Page 3: Product & Customer Deep Dive (Drill-Through Target)

```
+---------------------------------------------------------------------------------------------------------+
| COMMERCIAL PORTFOLIO & PROFITABILITY DRILL-DOWN                            [Category Slicer] [Segment]  |
+---------------------------------------------------------------------------------------------------------+
|  VISUAL 8: Sub-Category Profitability Matrix  |  VISUAL 9: Dynamic Top 10 Products by Revenue           |
|  - Copiers: 46.2% margin                      |  1. Smart Phone Pro Max: $184,200 (Rank 1)              |
|  - Machines: 42.1% margin                     |  2. Commercial Color Copier: $148,000 (Rank 2)          |
|  - Phones: 38.4% margin                       |  3. High-Volume Laser Printer: $112,500 (Rank 3)        |
|  - Chairs: 37.9% margin                       |  4. Ergonomic Task Chair: $89,400 (Rank 4)              |
|  - Binders: 54.1% margin                      |  5. Modular Conference Table: $74,200 (Rank 5)          |
|                                               |  ... Top 10 Pareto Dynamic Selector                     |
+-----------------------------------------------+---------------------------------------------------------+
|                                                                                                         |
|  VISUAL 10: Customer Lifetime Value (LTV) Distribution & Order Frequency Scatter Plot                   |
|  (X-axis: Total Orders, Y-axis: Total Spend, Bubble Size: Profit Margin, Color: Segment)                |
|                                                                                                         |
+---------------------------------------------------------------------------------------------------------+
```

---

## 4. Interactive Slicers & Navigation Pathways

1. **Global Header Slicers**:
   - `Year` (Dropdown / Tile: `2022`, `2023`, `2024`).
   - `Market` (Dropdown: `North America`, `Europe`, `Asia-Pacific`).
   - `Customer Segment` (Horizontal Button Pills: `Consumer`, `Corporate`, `Home Office`).
2. **Drill-Down & Hierarchies**:
   - **Geographic Hierarchy**: `Market` -> `Region` -> `Country` -> `State` -> `City`.
   - **Product Hierarchy**: `Category` -> `Sub_Category` -> `Product_Name`.
3. **Drill-Through Target**:
   - Right-click any Product or Category on Page 1 -> Select *"Drill-through to Product Deep Dive"* to open filtered Page 3.
