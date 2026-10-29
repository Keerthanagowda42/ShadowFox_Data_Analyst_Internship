import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import nsdecls, qn
import os

def set_cell_background(cell, fill_hex):
    tcPr = cell._tc.get_or_add_tcPr()
    tcPr.append(parse_xml(f'<w:shd {nsdecls("w")} w:fill="{fill_hex}"/>'))

def set_cell_margins(cell, top=100, bottom=100, left=150, right=150):
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = OxmlElement('w:tcMar')
    for m, val in [('top', top), ('bottom', bottom), ('left', left), ('right', right)]:
        node = OxmlElement(f'w:{m}')
        node.set(qn('w:w'), str(val))
        node.set(qn('w:type'), 'dxa')
        tcMar.append(node)
    tcPr.append(tcMar)

def set_table_borders(table, color="D3D3D3", sz="4", val="single"):
    tblPr = table._tbl.tblPr
    borders = parse_xml(
        f'<w:tblBorders {nsdecls("w")}>'
        f'  <w:top w:val="{val}" w:sz="{sz}" w:space="0" w:color="{color}"/>'
        f'  <w:bottom w:val="{val}" w:sz="{sz}" w:space="0" w:color="{color}"/>'
        f'  <w:insideH w:val="{val}" w:sz="{sz}" w:space="0" w:color="{color}"/>'
        f'  <w:insideV w:val="none"/>'
        f'  <w:left w:val="none"/>'
        f'  <w:right w:val="none"/>'
        f'</w:tblBorders>'
    )
    tblPr.append(borders)

def build_report():
    template_path = r'Official_Templates\Internship Final Report - Template.docx'
    doc = docx.Document(template_path)

    # Clear template placeholder paragraphs while keeping the document properties
    for p in list(doc.paragraphs):
        p_elem = p._p
        p_elem.getparent().remove(p_elem)

    # Base styling
    NAVY = RGBColor(26, 5, 56)      # #1A0538
    TEAL = RGBColor(0, 128, 128)     # #008080
    CHARCOAL = RGBColor(51, 65, 85)  # #334155
    BLACK = RGBColor(15, 23, 42)

    def add_title(text):
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.paragraph_format.space_before = Pt(0)
        p.paragraph_format.space_after = Pt(12)
        run = p.add_run(text)
        run.bold = True
        run.font.name = 'Calibri'
        run.font.size = Pt(22)
        run.font.color.rgb = NAVY
        return p

    def add_meta_block(items):
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(4)
        p.paragraph_format.space_after = Pt(16)
        p.paragraph_format.line_spacing = 1.25
        for label, val in items:
            r_lbl = p.add_run(label + ' ')
            r_lbl.bold = True
            r_lbl.font.name = 'Calibri'
            r_lbl.font.size = Pt(11)
            r_lbl.font.color.rgb = BLACK
            
            r_val = p.add_run(val + '\n')
            r_val.bold = False
            r_val.font.name = 'Calibri'
            r_val.font.size = Pt(11)
            r_val.font.color.rgb = CHARCOAL
        return p

    def add_h3(title):
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(18)
        p.paragraph_format.space_after = Pt(8)
        p.paragraph_format.keep_with_next = True
        run = p.add_run(title)
        run.bold = True
        run.font.name = 'Calibri'
        run.font.size = Pt(14)
        run.font.color.rgb = NAVY
        return p

    def add_h4(title):
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(12)
        p.paragraph_format.space_after = Pt(4)
        p.paragraph_format.keep_with_next = True
        run = p.add_run(title)
        run.bold = True
        run.font.name = 'Calibri'
        run.font.size = Pt(12)
        run.font.color.rgb = TEAL
        return p

    def add_p(text, bold_prefix=None, space_after=6):
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        p.paragraph_format.space_before = Pt(2)
        p.paragraph_format.space_after = Pt(space_after)
        p.paragraph_format.line_spacing = 1.15
        if bold_prefix:
            r_pre = p.add_run(bold_prefix)
            r_pre.bold = True
            r_pre.font.name = 'Calibri'
            r_pre.font.size = Pt(11)
            r_pre.font.color.rgb = BLACK
        run = p.add_run(text)
        run.font.name = 'Calibri'
        run.font.size = Pt(11)
        run.font.color.rgb = CHARCOAL
        return p

    def add_bullet(text, bold_prefix=None):
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        p.paragraph_format.left_indent = Inches(0.25)
        p.paragraph_format.first_line_indent = Inches(-0.15)
        p.paragraph_format.space_before = Pt(1)
        p.paragraph_format.space_after = Pt(3)
        p.paragraph_format.line_spacing = 1.15
        
        r_bullet = p.add_run('▪  ')
        r_bullet.bold = True
        r_bullet.font.name = 'Calibri'
        r_bullet.font.size = Pt(9.5)
        r_bullet.font.color.rgb = TEAL
        
        if bold_prefix:
            r_pre = p.add_run(bold_prefix + ' ')
            r_pre.bold = True
            r_pre.font.name = 'Calibri'
            r_pre.font.size = Pt(10.5)
            r_pre.font.color.rgb = BLACK
        run = p.add_run(text)
        run.font.name = 'Calibri'
        run.font.size = Pt(10.5)
        run.font.color.rgb = CHARCOAL
        return p

    def add_image_with_caption(img_path, caption_text, width_inches=6.0):
        if os.path.exists(img_path):
            p = doc.add_paragraph()
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            p.paragraph_format.space_before = Pt(8)
            p.paragraph_format.space_after = Pt(2)
            run = p.add_run()
            run.add_picture(img_path, width=Inches(width_inches))
            
            cp = doc.add_paragraph()
            cp.alignment = WD_ALIGN_PARAGRAPH.CENTER
            cp.paragraph_format.space_before = Pt(0)
            cp.paragraph_format.space_after = Pt(10)
            c_run = cp.add_run(caption_text)
            c_run.font.name = 'Calibri'
            c_run.font.size = Pt(9.5)
            c_run.font.italic = True
            c_run.font.color.rgb = RGBColor(100, 116, 139)

    def add_styled_table(headers, rows_data, col_widths=None):
        tbl = doc.add_table(rows=len(rows_data) + 1, cols=len(headers))
        tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
        set_table_borders(tbl)
        
        # Header Row
        hdr_cells = tbl.rows[0].cells
        for i, h in enumerate(headers):
            hdr_cells[i].text = h
            set_cell_background(hdr_cells[i], "1A0538")
            set_cell_margins(hdr_cells[i], 120, 120, 140, 140)
            p = hdr_cells[i].paragraphs[0]
            p.alignment = WD_ALIGN_PARAGRAPH.LEFT
            for r in p.runs:
                r.bold = True
                r.font.name = 'Calibri'
                r.font.size = Pt(10)
                r.font.color.rgb = RGBColor(255, 255, 255)
                
        # Data Rows
        for r_idx, row in enumerate(rows_data):
            row_cells = tbl.rows[r_idx + 1].cells
            bg_color = "F8FAFC" if r_idx % 2 == 1 else "FFFFFF"
            for c_idx, val in enumerate(row):
                row_cells[c_idx].text = str(val)
                set_cell_background(row_cells[c_idx], bg_color)
                set_cell_margins(row_cells[c_idx], 80, 80, 120, 120)
                p = row_cells[c_idx].paragraphs[0]
                p.alignment = WD_ALIGN_PARAGRAPH.LEFT
                for r in p.runs:
                    r.font.name = 'Calibri'
                    r.font.size = Pt(9.5)
                    r.font.color.rgb = BLACK
                    
        # Column widths
        if col_widths:
            for row in tbl.rows:
                for idx, width in enumerate(col_widths):
                    row.cells[idx].width = Inches(width)

        p_space = doc.add_paragraph()
        p_space.paragraph_format.space_before = Pt(2)
        p_space.paragraph_format.space_after = Pt(6)

    # ==========================
    # 1. TITLE & COVER DETAILS
    # ==========================
    add_title("Internship Final Report")
    
    meta_info = [
        ("Student Name:", "Keerthana V"),
        ("University / College:", "HKBK College of Engineering"),
        ("Internship Duration:", "August 1st, 2026 – August 31st, 2026 (1 Month)"),
        ("Company:", "ShadowFox"),
        ("Role:", "Data Analyst Intern"),
        ("Mentor:", "Mr. Aakash"),
        ("GitHub Repository:", "https://github.com/Keerthanagowda42/ShadowFox_Data_Analyst_Internship")
    ]
    add_meta_block(meta_info)

    # ==========================
    # 2. OBJECTIVES (Official Heading 3)
    # ==========================
    add_h3("Objectives")
    add_p(
        "The primary objective of the ShadowFox Data Analyst Internship was to gain comprehensive, hands-on industry experience "
        "by solving real-world, data-intensive business problems. The internship program was structured across three progressively challenging tiers—"
        "Beginner, Intermediate, and Advanced—designed to bridge the gap between theoretical data science concepts and enterprise-grade business intelligence applications."
    )
    add_p("The foundational objectives established for the internship tenure encompassed:", bold_prefix="Key Program Goals: ")
    add_bullet(" To architect robust Python pipelines for detecting and remediating real-world transactional data anomalies, including duplicate records, corrupted timestamps, formatting discrepancies, and missing categorical attributes.", "Automated Data Cleaning & Auditing:")
    add_bullet(" To perform rigorous exploratory data analysis (EDA) across retail transaction streams, deriving critical financial metrics such as Gross Sales, Net Profit, Operating Margin %, and Average Order Value (AOV).", "Exploratory Data Analysis & Financial Modeling:")
    add_bullet(" To automate dynamic multi-tab spreadsheet dashboards utilizing advanced Excel formulas (SUMIFS, AVERAGE, COUNT) and professional KPI visualization cards for executive stakeholders.", "Spreadsheet Engineering & Dashboarding:")
    add_bullet(" To uncover customer behavioral dynamics through Recency, Frequency, and Monetary (RFM) segmentation, monthly cohort retention matrices, and customer lifetime value (LTV) evaluations across multi-year transactional logs.", "Customer Behavioral Analytics & Cohort Tracking:")
    add_bullet(" To design and execute complex relational database queries in SQLite utilizing ANSI SQL-99 standards, Common Table Expressions (CTEs), and advanced Window Functions (DENSE_RANK, LAG, NTILE, running totals).", "Relational Database & Advanced SQL Modeling:")
    add_bullet(" To architect an enterprise-grade Business Intelligence reporting system using Microsoft Power BI Desktop, implementing a certified 6-table Star Schema dimensional model, and programming 28 production DAX measures.", "Enterprise Business Intelligence & Star Schema Architecture:")
    add_bullet(" To synthesize empirical analytical findings into actionable strategic recommendations addressing product merchandising, customer retention triggers, and supply chain logistics bottlenecks.", "Data-Driven Strategic Decision Support:")

    # ==========================
    # 3. TASKS AND RESPONSIBILITIES (Official Heading 3)
    # ==========================
    add_h3("Tasks and Responsibilities")
    add_p(
        "Throughout the internship, all analytical projects were developed from scratch, rigorously tested against clean baseline datasets, "
        "and documented to production standards. The complete portfolio encompasses three distinct capstone implementations:"
    )

    # --- Project 1: Beginner Level ---
    add_h4("3.1 Project 1 (Beginner Level): Small Business Sales Performance Analysis & Dashboard")
    add_p(
        "A multi-regional small business operating across five geographic territories (Central, East, North, South, West) and four commercial verticals "
        "(Furniture, Electronics, Office Supplies, Home & Kitchen) experienced rapid sales volume growth but suffered from an acute lack of operational visibility. "
        "Executive management could not readily assess category-level profit margins, identify seasonal demand surges, or pinpoint high-risk low-margin inventory.",
        bold_prefix="Business Problem: "
    )
    add_p(
        "The raw sales dataset (raw_sales_data.csv) contained 1,270 transaction records spanning Fiscal Year 2024 with 11 operational attributes: "
        "Order ID, Order Date, Product, Category, Quantity, Unit Price, Cost, Sales, Profit, Region, and Payment Method. The raw stream arrived with deliberately injected "
        "real-world flaws, including duplicate order IDs, casing inconsistencies ('electronics' vs 'Electronics'), mixed datetime serial formats ('YYYY-MM-DD', 'MM/DD/YYYY', 'DD-MM-YYYY'), "
        "and unrecorded payment methods.",
        bold_prefix="Dataset Description & Quality Audit: "
    )
    add_p(
        "I constructed an automated data auditing and cleaning pipeline in Python (data_cleaning.py). The pipeline executed seven automated transformations: "
        "(1) identified and purged 20 duplicate orders; (2) trimmed whitespace and standardized categorical fields into Title Case; (3) imputed 37 missing Payment Method values "
        "with 'Not Specified' to maintain transaction integrity; (4) stripped currency formatting and cast numeric fields into 64-bit floating point; (5) parsed heterogeneous date strings "
        "into standard ISO-8601 timestamps; (6) recalculated Sales and Profit fields to ensure mathematical consistency; and (7) validated zero remaining nulls across 1,250 clean records.",
        bold_prefix="Data Cleaning & Engineering Pipeline: "
    )

    # Table 1: Beginner KPIs
    p1_headers = ["Performance Metric", "Observed Value", "Operational Benchmark / Context"]
    p1_data = [
        ["Total Gross Revenue", "$180,936.50", "Cumulative 2024 gross transaction volume"],
        ["Total Net Profit", "$87,709.30", "Consolidated net return after cost of goods"],
        ["Consolidated Profit Margin", "48.48%", "Healthy overall retail margin"],
        ["Total Order Volume", "1,250 Orders", "Average of ~104 transactions per month"],
        ["Units Sold", "2,662 Units", "2.13 units per average basket"],
        ["Average Order Value (AOV)", "$144.75", "Baseline transaction basket size"],
        ["Peak Seasonality Month", "November ($23,036.00)", "Q4 holiday surge; AOV reached $213.30"],
        ["Trough Performance Month", "June ($9,972.00)", "Summer lull; promotional opportunity"],
        ["Top Revenue Product", "Ergonomic Office Chair", "$43,050.00 revenue across 123 orders"],
        ["Highest Margin Product", "Gel Ink Pens", "67.72% net profit margin ($2,966.00 revenue)"]
    ]
    add_styled_table(p1_headers, p1_data, [2.0, 1.8, 2.7])

    add_image_with_caption(
        r'Internship_Documentation\ShadowFox_Internship_Documentation\Screenshots\p1_monthly_sales_trend.png',
        "Figure 1: Monthly Sales & Net Profit Trajectory for Fiscal Year 2024 highlighting Q4 peak.",
        5.6
    )
    add_image_with_caption(
        r'Internship_Documentation\ShadowFox_Internship_Documentation\Screenshots\p1_category_sales_profit.png',
        "Figure 2: Dual-axis comparison of Gross Sales Volume vs Net Profit Margin across commercial categories.",
        5.6
    )

    add_p(
        "To empower operational managers without technical Python backgrounds, I engineered a fully automated 4-worksheet Excel workbook "
        "(Small_Business_Sales_Dashboard.xlsx) using openpyxl. The workbook incorporates: "
        "(1) 'Raw Data' preserving historical records; (2) 'Cleaned Data' structured table; (3) 'Analysis' sheet calculating dynamic metrics via Excel formulas "
        "(=SUM, =SUMIFS, =AVERAGE, =COUNTIFS) without hardcoded values; and (4) 'Dashboard' sheet with formatted KPI summary cards and embedded high-resolution visual charts.",
        bold_prefix="Spreadsheet Engineering: "
    )
    add_bullet("Furniture ($74,359.00) and Electronics ($68,702.50) represent 79.07% of company revenue, establishing them as foundational volume drivers.", "Volume vs Margin Divergence:")
    add_bullet("Desk Accessories and Office Supplies yield superior profit margins (67.72% on Gel Ink Pens), making them ideal high-margin add-ons.", "Cross-Selling Potential:")
    add_bullet("Implement pre-holiday early-bird promotions starting in September to smooth out the severe mid-year summer revenue drop.", "Seasonal Merchandising Strategy:")

    # --- Project 2: Intermediate Level ---
    add_h4("3.2 Project 2 (Intermediate Level): Customer Behaviour, Revenue, and Retention Analytics")
    add_p(
        "A fast-growing direct-to-consumer e-commerce brand faced strategic uncertainty regarding customer persistence, repurchase velocity, "
        "and revenue concentration. While top-line customer acquisition was expanding, leadership lacked visibility into customer lifetime value (LTV), "
        "did not know what share of revenue was generated by repeat buyers versus one-time shoppers, and lacked automated SQL segmentation pipelines.",
        bold_prefix="Business Problem: "
    )
    add_p(
        "The underlying dataset (raw_customer_data.csv) tracked 2,336 customer transactions spanning Jan 1, 2023 through Dec 31, 2024 (24 months) across 850 distinct customer accounts. "
        "Attributes included Transaction_ID, Customer_ID, Demographic & Regional data, Acquisition_Channel, Product vertical, Unit_Price, Quantity, Discounts, Total_Spend, and Payment_Method. "
        "The cleaning script (customer_cleaning.py) removed 30 duplicate entries, imputed categorical missing fields, standardized date types, and engineered analytical features "
        "including Cohort_Month (first purchase date) and Cohort_Index (months elapsed since acquisition).",
        bold_prefix="Dataset Description & Cohort Engineering: "
    )

    # Table 2: Intermediate RFM and Repeat Summary
    p2_headers = ["Segment / Dimension", "Customer Count", "% Customer Base", "Total Revenue ($)", "% Total Revenue", "Average LTV ($)"]
    p2_data = [
        ["Champions (RFM 555)", "200", "23.53%", "$162,963.95", "49.83%", "$814.82"],
        ["Loyal Customers", "100", "11.76%", "$64,374.88", "19.68%", "$643.75"],
        ["Potential Loyalists", "100", "11.76%", "$37,169.68", "11.36%", "$371.70"],
        ["At Risk (High Spenders)", "50", "5.88%", "$19,531.14", "5.97%", "$390.62"],
        ["Need Attention", "75", "8.82%", "$15,248.30", "4.66%", "$203.31"],
        ["Hibernating / Dormant", "75", "8.82%", "$9,428.10", "2.88%", "$125.71"],
        ["Lost Customers", "50", "5.88%", "$5,241.32", "1.60%", "$104.83"],
        ["Recent Inactive", "200", "23.53%", "$13,100.00", "4.01%", "$65.50"],
        ["Repeat Customers (Overall)", "399", "46.94%", "$264,508.51", "80.88%", "$662.93"],
        ["One-Time Buyers (Overall)", "451", "53.06%", "$62,548.87", "19.12%", "$138.07"]
    ]
    add_styled_table(p2_headers, p2_data, [1.6, 0.9, 1.1, 1.2, 1.0, 1.0])

    add_image_with_caption(
        r'Internship_Documentation\ShadowFox_Internship_Documentation\Screenshots\p2_repeat_vs_onetime_revenue.png',
        "Figure 3: Revenue distribution asymmetry proving repeat customers generate 80.88% of total brand sales.",
        5.2
    )
    add_image_with_caption(
        r'Internship_Documentation\ShadowFox_Internship_Documentation\Screenshots\p2_cohort_retention_heatmap.png',
        "Figure 4: 24-Month Cohort Retention Heatmap displaying retention decay and stabilization baseline.",
        5.8
    )

    add_p(
        "I established an SQLite relational database (customer_analytics.db) and authored 10 production SQL queries (customer_analysis.sql) "
        "leveraging Common Table Expressions (CTEs) and Window Functions. Key queries included: "
        "(Q4) Top 10 VIP Customers by spend; (Q5) Regional customer rankings using DENSE_RANK() OVER (PARTITION BY Customer_Region ORDER BY Total_Spend DESC); "
        "(Q6) Month-over-Month Revenue Growth using LAG(Monthly_Revenue, 1); (Q7) Cumulative Running Total Revenue using SUM(Monthly_Revenue) OVER (ORDER BY Year_Month); "
        "and (Q9) Spend Quintile Categorization using NTILE(5). All 10 queries were executed via Python (execute_sql_queries.py) with zero errors and exported to reports/.",
        bold_prefix="Relational SQL Analytics Pipeline: "
    )
    add_bullet("Repeat customers generate 80.88% of total revenue despite comprising only 46.94% of the customer base. Their average LTV is 4.8x higher than one-time buyers ($662.93 vs $138.07).", "Extreme Revenue Asymmetry:")
    add_bullet("The top 20% of customers generate 56.04% of total sales, with 200 Champions alone delivering nearly 50% ($162,963.95).", "Pareto Concentration:")
    add_bullet("Cohort retention exhibits a sharp 80% attrition between Month 0 and Month 1, followed by a stabilized 12% to 16% long-term loyalty core. An automated Day 3-10-21 onboarding sequence is required to bridge the second-purchase gap.", "Retention Bottleneck & Intervention:")

    # --- Project 3: Advanced Level ---
    add_h4("3.3 Project 3 (Advanced Level): Executive Business Intelligence Dashboard Using Power BI")
    add_p(
        "An enterprise commercial distributor operating across North America, Europe, and Asia-Pacific required a scalable Business Intelligence architecture. "
        "Executive leadership demanded real-time visibility into multi-year revenue velocity (YoY), budget target tracking, and supply chain health, "
        "specifically identifying on-time delivery bottlenecks across fulfillment shipping tiers.",
        bold_prefix="Business Problem: "
    )
    add_p(
        "A multi-year global operations dataset of 4,200 clean transactions spanning FY 2022 through FY 2024 was transformed in Python (data_transformation.py). "
        "The script engineered critical logistics metrics (Transit Days, Delivery SLA status) and normalized the flat data into a certified 6-Table Star Schema: "
        "Fact_Orders (4,200 rows), Fact_Targets (1,080 rows), Dim_Date (1,096 calendar days), Dim_Products (1,241 SKUs), Dim_Customers (600 accounts), and Dim_Geography (10 trade regions). "
        "All relationships were configured with 1:Many single-direction filters to guarantee optimal DAX evaluation speed.",
        bold_prefix="Star Schema Dimensional Architecture: "
    )

    # Table 3: Advanced Annual Performance
    p3_headers = ["Fiscal Year", "Annual Gross Sales", "YoY Sales Growth", "Net Operating Profit", "Operating Margin %", "Order Volume"]
    p3_data = [
        ["FY 2022", "$541,634.34", "Baseline Year", "$207,987.58", "38.40%", "784 Orders"],
        ["FY 2023", "$1,063,776.62", "+96.40%", "$408,490.22", "38.40%", "1,526 Orders"],
        ["FY 2024", "$1,323,930.21", "+24.46%", "$508,437.87", "38.40%", "1,890 Orders"],
        ["3-Year Total", "$2,929,341.17", "+144.43% Total", "$1,124,915.67", "38.40%", "4,200 Orders"]
    ]
    add_styled_table(p3_headers, p3_data, [1.2, 1.4, 1.2, 1.4, 1.1, 1.1])

    add_image_with_caption(
        r'Internship_Documentation\ShadowFox_Internship_Documentation\Screenshots\p3_powerbi_executive_overview.png',
        "Figure 5: Power BI Executive Overview Dashboard Render ($2.93M Sales, 38.4% Margin, YoY Growth).",
        5.8
    )
    add_image_with_caption(
        r'Internship_Documentation\ShadowFox_Internship_Documentation\Screenshots\p3_logistics_sla_compliance.png',
        "Figure 6: Logistics On-Time Delivery SLA Compliance across fulfillment shipping tiers.",
        5.4
    )

    add_p(
        "I authored a production library of 28 commented DAX measures (powerbi_measures.dax) categorized into four functional groups: "
        "(1) Core Financial Measures ([Total Sales], [Total Profit], [Profit Margin %]); "
        "(2) Time Intelligence ([Sales YTD] = TOTALYTD([Total Sales], Dim_Date[Date]), [Sales LY] = CALCULATE([Total Sales], SAMEPERIODLASTYEAR(Dim_Date[Date])), [YoY Sales Growth %]); "
        "(3) Target Tracking ([Budget Variance $] = [Total Sales] - [Sales Target], [Target Achievement %]); and "
        "(4) Logistics SLAs ([On-Time Deliveries], [SLA Compliance %] = DIVIDE([On-Time Deliveries], [Total Orders], 0), [Avg Transit Days]).",
        bold_prefix="DAX Measures Library: "
    )
    add_bullet("3-Year Gross Sales achieved $2,929,341.17 with $1,124,915.67 in Net Operating Profit, demonstrating robust annual expansion (+96.4% in 2023, +24.5% in 2024).", "Consolidated Growth:")
    add_bullet("Consolidated On-Time Delivery compliance sits at 68.83%, falling critically short of the 85.00% SLA target.", "Severe Supply Chain Vulnerability:")
    add_bullet("While Same Day (92.42%) and First Class (81.75%) fulfillment tiers perform well, Standard Class ground shipping achieved only 59.20% on-time compliance. 3PL carrier contracts must be renegotiated immediately.", "Logistical Bottleneck Isolation:")

    # ==========================
    # 4. LEARNING OUTCOMES (Official Heading 3)
    # ==========================
    add_h3("Learning Outcomes")
    add_p(
        "The ShadowFox Data Analyst Internship provided extensive hands-on exposure to the entire analytical lifecycle, from messy raw data "
        "ingestion to C-suite presentation decks. The core learning outcomes include:"
    )
    add_bullet("Mastered advanced data cleaning, string sanitization, datetime transformation, and feature engineering using Python (Pandas, NumPy). Gained fluency in detecting edge-case formatting flaws and implementing reproducible ETL scripts.", "Advanced Data Manipulation & Preprocessing:")
    add_bullet("Deepened expertise in writing complex, ANSI-compliant SQL scripts in SQLite. Built fluency in Common Table Expressions (CTEs), multi-table JOINs, subqueries, and Window Functions (ROW_NUMBER, DENSE_RANK, LAG, NTILE, running aggregates).", "Relational Database Modeling & Window Functions:")
    add_bullet("Developed production-ready skills in dimensional modeling. Designed a certified 6-table Star Schema with 1:Many relationships and authored 28 optimized DAX measures utilizing CALCULATE, Time Intelligence, and contextual filters.", "Business Intelligence & Star Schema Architecture:")
    add_bullet("Learned to architect formula-driven, auditable Excel workbooks with dynamic functions (SUMIFS, AVERAGE, COUNTIFS) and professional KPI summary tiles using openpyxl automation.", "Spreadsheet Automation & Formula Design:")
    add_bullet("Acquired specialized knowledge in behavioral customer analytics, including quintile RFM segmentation, monthly cohort retention tracking, and Pareto 80/20 spend dynamics.", "Customer Analytics & Cohort Retention:")
    add_bullet("Enhanced executive communication skills by synthesizing empirical data into clear business narratives, designing visual wireframes, and formulating data-backed operational recommendations.", "Executive Data Storytelling & Presentation:")

    # ==========================
    # 5. CHALLENGES AND SOLUTIONS (Official Heading 3)
    # ==========================
    add_h3("Challenges and Solutions")
    add_p(
        "During the execution of the three projects, several technical and methodological hurdles arose. Below are the key challenges encountered "
        "and the engineering solutions implemented to overcome them:"
    )
    add_bullet(
        "The raw sales datasets contained heterogeneous timestamp representations ('YYYY-MM-DD', 'MM/DD/YYYY', 'DD-MM-YYYY') and missing categorical values. "
        "Solution: Programmed custom parsing logic using pandas.to_datetime with format fallback heuristics, standardized dates to ISO-8601, and applied categorical imputation ('Not Specified') to prevent dropping revenue records.",
        "Challenge 1: Heterogeneous Date Formats and Dirty Raw Data — "
    )
    add_bullet(
        "Calculating retention percentages across 24 monthly customer cohorts required dynamic tracking of each customer's initial acquisition month versus subsequent transaction periods. "
        "Solution: Engineered vectorised Cohort_Month and Cohort_Index calculations in Python, transformed the output into a 24x24 matrix, and visualized retention rates using a custom Seaborn heatmap.",
        "Challenge 2: Multi-Year Cohort Retention Matrix Computation — "
    )
    add_bullet(
        "Standard aggregate functions cannot compute month-over-month growth or customer regional rankings within single queries. "
        "Solution: Leveraged modern SQLite 3.25+ Window Functions (DENSE_RANK() OVER (PARTITION BY Region), LAG() OVER (ORDER BY Month), NTILE(5)), structuring modular logic using Common Table Expressions (CTEs).",
        "Challenge 3: Complex Window Aggregations in Relational SQL — "
    )
    add_bullet(
        "Connecting disparate transaction records, budget targets, and multiple dimensional entities directly caused potential Cartesian joins and circular filter paths. "
        "Solution: Structured a certified Star Schema with distinct Fact (Fact_Orders, Fact_Targets) and Dimension (Dim_Date, Dim_Products, Dim_Customers, Dim_Geography) tables, enforcing 1:Many single-direction cross-filtering.",
        "Challenge 4: Power BI Relationship Modeling & DAX Performance — "
    )

    # ==========================
    # 6. CONCLUSION (Official Heading 3)
    # ==========================
    add_h3("Conclusion")
    add_p(
        "The ShadowFox Data Analyst Internship has provided an invaluable, rigorous practical experience across the full spectrum of data analysis, "
        "database engineering, and business intelligence. By completing the three capstone projects, I developed a profound understanding of how raw, imperfect operational "
        "records can be systematically audited, modeled, and transformed into high-impact strategic intelligence."
    )
    add_p(
        "Across the portfolio, the analysis delivered verifiable, real-world value: "
        "(1) identified a 48.48% retail margin and seasonal Q4 surge in small business sales; "
        "(2) demonstrated that repeat buyers generate 80.88% of brand revenue with 4.8x higher LTV, formulating an onboarding retention framework; and "
        "(3) uncovered an enterprise logistics delivery bottleneck where Standard Class shipping (59.20% on-time) compromises overall company SLA compliance (68.83%)."
    )
    add_p(
        "Through the utilization of Python, Pandas, SQLite, Relational SQL, Microsoft Excel, and Power BI, I have established a verified, production-grade technical toolkit "
        "that positions me to drive immediate quantitative value in professional data analyst and business intelligence roles."
    )

    # ==========================
    # 7. ACKNOWLEDGMENTS (Official Heading 3)
    # ==========================
    add_h3("Acknowledgments")
    add_p(
        "I would like to express my sincere gratitude to ShadowFox for providing this comprehensive, challenging internship opportunity "
        "and establishing an environment that encourages independent problem solving and hands-on technical excellence."
    )
    add_p(
        "I extend my heartfelt thanks to my coordinator and mentor, Mr. Aakash, for guidance, curriculum design, and evaluation throughout this internship journey. "
        "His structured review checkpoints and technical benchmarks ensured the highest standards of data rigor."
    )
    add_p(
        "I formally declare that all three internship projects, analytical scripts, SQL queries, Excel dashboards, and Power BI models were completed independently by me. "
        "Additionally, I utilized official Python, SQLite, and Microsoft technical documentation for research, and modern developer tooling for design validation and code auditing."
    )

    # ==========================
    # 8. REFERENCES & DATA SOURCES
    # ==========================
    add_h3("References and Dataset Sources")
    add_bullet("Pandas Development Team. (2024). pandas: powerful Python data analysis toolkit. https://pandas.pydata.org/", "Python Data Science Stack: ")
    add_bullet("SQLite Consortium. (2024). SQLite 3 Reference Documentation: Window Functions & CTEs. https://www.sqlite.org/", "Relational Database Documentation: ")
    add_bullet("Microsoft Corporation. (2024). Power BI Guidance Documentation: Star Schema Dimensional Modeling & DAX Patterns. https://learn.microsoft.com/power-bi/", "Microsoft Business Intelligence: ")
    add_bullet("ShadowFox Data Analyst Internship Capstone Repository. https://github.com/Keerthanagowda42/ShadowFox_Data_Analyst_Internship", "Project Portfolio Repository: ")

    # Save to both target locations
    out_paths = [
        r'Internship_Documentation\ShadowFox_Internship_Documentation\Report\ShadowFox_Data_Analyst_Internship_Final_Report.docx',
        r'ShadowFox_Internship_Documentation\Report\ShadowFox_Data_Analyst_Internship_Final_Report.docx'
    ]
    for p in out_paths:
        os.makedirs(os.path.dirname(p), exist_ok=True)
        doc.save(p)
        print(f'Saved report to: {p}')

if __name__ == '__main__':
    build_report()
