import pptx
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.enum.shapes import MSO_SHAPE
import os

def create_presentation():
    prs = pptx.Presentation()
    # Set 16:9 widescreen dimensions
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6]

    # Colors matching the official sample PDF
    COLOR_TITLE = RGBColor(15, 23, 42)       # #0F172A
    COLOR_TEAL = RGBColor(0, 168, 181)       # #00A8B5
    COLOR_BODY = RGBColor(51, 65, 85)        # #334155
    COLOR_BG_SHAPE = RGBColor(226, 232, 240) # #E2E8F0
    COLOR_CARD_BG = RGBColor(248, 250, 252)  # #F8FAFC
    COLOR_WHITE = RGBColor(255, 255, 255)
    COLOR_MUTED = RGBColor(100, 116, 139)

    def add_background_decor(slide):
        # Soft geometric accent block on right margin, matching the sample PDF
        shape = slide.shapes.add_shape(
            MSO_SHAPE.RECTANGLE,
            Inches(12.6), Inches(0), Inches(0.733), Inches(7.5)
        )
        shape.fill.solid()
        shape.fill.fore_color.rgb = RGBColor(204, 236, 239)
        shape.line.fill.background()

    def add_slide_header(slide, title_text, slide_number=None):
        add_background_decor(slide)
        
        # Slide Title
        tb = slide.shapes.add_textbox(Inches(0.8), Inches(0.6), Inches(11.0), Inches(0.8))
        tf = tb.text_frame
        tf.word_wrap = True
        tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0
        p = tf.paragraphs[0]
        p.text = title_text
        p.font.name = 'Calibri'
        p.font.size = Pt(28)
        p.font.bold = True
        p.font.color.rgb = COLOR_TITLE
        
        # Teal accent horizontal bar directly under title
        bar = slide.shapes.add_shape(
            MSO_SHAPE.RECTANGLE,
            Inches(0.8), Inches(1.45), Inches(0.8), Inches(0.06)
        )
        bar.fill.solid()
        bar.fill.fore_color.rgb = COLOR_TEAL
        bar.line.fill.background()

        # Slide Number (bottom left, matching sample PDF)
        if slide_number:
            num_box = slide.shapes.add_textbox(Inches(0.8), Inches(6.8), Inches(1.0), Inches(0.4))
            np = num_box.text_frame.paragraphs[0]
            np.text = str(slide_number)
            np.font.name = 'Calibri'
            np.font.size = Pt(12)
            np.font.color.rgb = COLOR_MUTED

    # ==========================================
    # SLIDE 1: TITLE SLIDE (Matching Sample PDF)
    # ==========================================
    s1 = prs.slides.add_slide(blank_layout)
    add_background_decor(s1)
    
    # Title Box in center
    t_box = s1.shapes.add_textbox(Inches(1.5), Inches(2.2), Inches(10.0), Inches(2.2))
    tf1 = t_box.text_frame
    tf1.word_wrap = True
    
    p1 = tf1.paragraphs[0]
    p1.text = "DATA ANALYST"
    p1.font.name = 'Calibri'
    p1.font.size = Pt(44)
    p1.font.bold = True
    p1.font.color.rgb = COLOR_TITLE
    p1.alignment = PP_ALIGN.CENTER
    
    p2 = tf1.add_paragraph()
    p2.text = "Task Presentation"
    p2.font.name = 'Calibri'
    p2.font.size = Pt(36)
    p2.font.color.rgb = COLOR_TEAL
    p2.alignment = PP_ALIGN.CENTER
    
    # Center accent bar
    bar1 = s1.shapes.add_shape(
        MSO_SHAPE.RECTANGLE,
        Inches(6.2), Inches(4.5), Inches(0.9), Inches(0.08)
    )
    bar1.fill.solid()
    bar1.fill.fore_color.rgb = COLOR_TEAL
    bar1.line.fill.background()
    
    # Bottom right author block
    auth_box = s1.shapes.add_textbox(Inches(8.5), Inches(5.2), Inches(3.8), Inches(1.8))
    atf = auth_box.text_frame
    
    ap1 = atf.paragraphs[0]
    ap1.text = "By:"
    ap1.font.name = 'Calibri'
    ap1.font.size = Pt(14)
    ap1.font.color.rgb = COLOR_TEAL
    
    ap2 = atf.add_paragraph()
    ap2.text = "Keerthana V"
    ap2.font.name = 'Calibri'
    ap2.font.size = Pt(18)
    ap2.font.bold = True
    ap2.font.color.rgb = COLOR_TITLE

    ap_col = atf.add_paragraph()
    ap_col.text = "HKBK College of Engineering"
    ap_col.font.name = 'Calibri'
    ap_col.font.size = Pt(13)
    ap_col.font.color.rgb = COLOR_BODY
    
    ap3 = atf.add_paragraph()
    ap3.text = "Data Analyst Intern"
    ap3.font.name = 'Calibri'
    ap3.font.size = Pt(14)
    ap3.font.color.rgb = COLOR_TITLE
    
    ap4 = atf.add_paragraph()
    ap4.text = "August Batch 1 / October 2026"
    ap4.font.name = 'Calibri'
    ap4.font.size = Pt(14)
    ap4.font.color.rgb = COLOR_TEAL

    # ==========================================
    # SLIDE 2: CONTENTS (Matching Sample PDF)
    # ==========================================
    s2 = prs.slides.add_slide(blank_layout)
    add_slide_header(s2, "CONTENTS", 2)
    
    c_box = s2.shapes.add_textbox(Inches(1.2), Inches(2.2), Inches(10.5), Inches(4.2))
    ctf = c_box.text_frame
    
    contents = [
        ("1. ACKNOWLEDGEMENT", "Formal recognition of ShadowFox, coordinators, and declaration of independence."),
        ("2. BEGINNER LEVEL", "Small Business Sales Performance Analysis & Automated Excel Dashboard."),
        ("3. INTERMEDIATE LEVEL", "Customer Behaviour, RFM Segmentation, Cohort Retention & Relational SQL."),
        ("4. ADVANCED LEVEL", "Executive Business Intelligence Dashboard & Logistics SLAs in Power BI."),
        ("5. CONCLUSION & RECOMMENDATIONS", "Consolidated business insights, operational strategy, and learning outcomes.")
    ]
    
    for idx, (title, desc) in enumerate(contents):
        cp = ctf.paragraphs[0] if idx == 0 else ctf.add_paragraph()
        cp.space_before = Pt(14)
        r1 = cp.add_run()
        r1.text = title
        r1.font.name = 'Calibri'
        r1.font.size = Pt(18)
        r1.font.bold = True
        r1.font.color.rgb = COLOR_TITLE
        
        r2 = cp.add_run()
        r2.text = f"  —  {desc}"
        r2.font.name = 'Calibri'
        r2.font.size = Pt(14)
        r2.font.color.rgb = COLOR_BODY

    # ==========================================
    # SLIDE 3: ACKNOWLEDGEMENT (Matching Sample PDF)
    # ==========================================
    s3 = prs.slides.add_slide(blank_layout)
    add_slide_header(s3, "ACKNOWLEDGEMENT", 3)
    
    ack_box = s3.shapes.add_textbox(Inches(1.2), Inches(2.3), Inches(10.5), Inches(4.2))
    atf = ack_box.text_frame
    atf.word_wrap = True
    
    ak1 = atf.paragraphs[0]
    ak1.text = (
        "I would like to express my gratitude to ShadowFox for giving me the opportunity "
        "to present the comprehensive data analytics tasks I have completed during this internship."
    )
    ak1.font.name = 'Calibri'
    ak1.font.size = Pt(17)
    ak1.font.color.rgb = COLOR_BODY
    ak1.space_after = Pt(20)
    
    ak2 = atf.add_paragraph()
    ak2.text = (
        "I would also like to extend my thanks to my coordinator, Mr. Aakash, for guiding me throughout this experience. "
        "I acknowledge that all three capstone projects, automated Python pipelines, relational SQL queries, spreadsheet models, "
        "and Power BI dashboards were completed independently by me. Additionally, I utilized official technical documentation for research "
        "and developer tooling for validating code quality and generating reference ideas."
    )
    ak2.font.name = 'Calibri'
    ak2.font.size = Pt(17)
    ak2.font.color.rgb = COLOR_BODY

    # ==========================================
    # SLIDE 4: BEGINNER LEVEL OVERVIEW
    # ==========================================
    s4 = prs.slides.add_slide(blank_layout)
    add_slide_header(s4, "BEGINNER LEVEL: Overview & Methodology", 4)
    
    b_box = s4.shapes.add_textbox(Inches(1.0), Inches(1.8), Inches(11.0), Inches(5.0))
    btf = b_box.text_frame
    btf.word_wrap = True
    
    bp1 = btf.paragraphs[0]
    bp1.text = "Task: Small Business Sales Performance Analysis & Spreadsheet Dashboard"
    bp1.font.name = 'Calibri'
    bp1.font.size = Pt(18)
    bp1.font.bold = True
    bp1.font.color.rgb = COLOR_TEAL
    bp1.space_after = Pt(14)
    
    bullets_s4 = [
        ("Business Problem: ", "A retail small business lacked visibility into category margins, seasonal demand spikes, and regional product profitability across 1,270 raw transaction records with real-world flaws."),
        ("Data Cleaning Pipeline: ", "Automated Python cleaning script (data_cleaning.py) removed 20 duplicate orders, imputed 37 missing payment methods, normalized casing, parsed mixed date formats, and verified 1,250 clean records."),
        ("Core Verified KPIs: ", "Gross Revenue: $180,936.50 | Net Profit: $87,709.30 | Margin: 48.48% | Orders: 1,250 | Units: 2,662 | Average Order Value (AOV): $144.75."),
        ("Spreadsheet Dashboard: ", "Constructed an automated 4-tab Excel workbook (Small_Business_Sales_Dashboard.xlsx) using dynamic formulas (=SUM, =SUMIFS, =AVERAGE), KPI summary cards, and embedded charts."),
        ("Technical Stack: ", "Python 3.12 (Pandas, NumPy, Matplotlib, Seaborn), Microsoft Excel (openpyxl), Git.")
    ]
    for pre, text in bullets_s4:
        p = btf.add_paragraph()
        p.space_after = Pt(10)
        r_pre = p.add_run()
        r_pre.text = "• " + pre
        r_pre.font.name = 'Calibri'
        r_pre.font.size = Pt(15)
        r_pre.font.bold = True
        r_pre.font.color.rgb = COLOR_TITLE
        
        r_txt = p.add_run()
        r_txt.text = text
        r_txt.font.name = 'Calibri'
        r_txt.font.size = Pt(15)
        r_txt.font.color.rgb = COLOR_BODY

    # Helper for Split Content + Chart Slides
    def add_split_slide(prs, title, slide_num, bullet_items, img_path):
        slide = prs.slides.add_slide(prs.slide_layouts[6])
        add_slide_header(slide, title, slide_num)
        
        # Left Text Box (5.5 inches wide)
        tb = slide.shapes.add_textbox(Inches(0.8), Inches(1.8), Inches(5.6), Inches(5.0))
        tf = tb.text_frame
        tf.word_wrap = True
        
        for idx, (pre, text) in enumerate(bullet_items):
            p = tf.paragraphs[0] if idx == 0 else tf.add_paragraph()
            p.space_after = Pt(12)
            
            r_pre = p.add_run()
            r_pre.text = "• " + pre + " "
            r_pre.font.name = 'Calibri'
            r_pre.font.size = Pt(14)
            r_pre.font.bold = True
            r_pre.font.color.rgb = COLOR_TITLE
            
            r_txt = p.add_run()
            r_txt.text = text
            r_txt.font.name = 'Calibri'
            r_txt.font.size = Pt(14)
            r_txt.font.color.rgb = COLOR_BODY
            
        # Right Image Embed (5.8 inches wide)
        if os.path.exists(img_path):
            slide.shapes.add_picture(
                img_path, Inches(6.6), Inches(1.8), width=Inches(5.7)
            )
        return slide

    # ==========================================
    # SLIDE 5: BEGINNER - MONTHLY TREND
    # ==========================================
    add_split_slide(
        prs,
        "Monthly Sales Trend & Seasonality Analysis",
        5,
        [
            ("Description:", "Time-series line chart tracking monthly Gross Revenue and Net Profit across Fiscal Year 2024."),
            ("Key Peak:", "November surge reached $23,036.00 in sales ($11,363.50 profit) with an AOV of $213.30, driven by Black Friday and Q4 holiday promotions."),
            ("Low Season:", "June represented the lowest revenue month ($9,972.00; AOV $124.65), revealing a distinct summer purchasing lull."),
            ("Strategic Action:", "Launch targeted early-bird campaigns starting in September to extend the seasonal peak and smooth mid-year dips.")
        ],
        r'Internship_Documentation\ShadowFox_Internship_Documentation\Screenshots\p1_monthly_sales_trend.png'
    )

    # ==========================================
    # SLIDE 6: BEGINNER - CATEGORY PERFORMANCE
    # ==========================================
    add_split_slide(
        prs,
        "Category Sales & Profitability Breakdown",
        6,
        [
            ("Description:", "Dual-axis bar and line visualization comparing total gross revenue against net profit margin across 4 retail verticals."),
            ("Volume Dominance:", "Furniture ($74,359.00) and Electronics ($68,702.50) generate 79.07% of consolidated gross company revenue."),
            ("Margin Leaders:", "Office Supplies yield the highest margin percentage (49.95%), led by Gel Ink Pens at an extraordinary 67.72% net profit margin."),
            ("Merchandising Strategy:", "Bundle high-volume furniture with high-margin desk accessories to lift consolidated order profitability.")
        ],
        r'Internship_Documentation\ShadowFox_Internship_Documentation\Screenshots\p1_category_sales_profit.png'
    )

    # ==========================================
    # SLIDE 7: BEGINNER - REGIONAL PERFORMANCE & EXCEL
    # ==========================================
    add_split_slide(
        prs,
        "Regional Performance & Spreadsheet Automation",
        7,
        [
            ("Description:", "Geographic performance analysis across 5 sales territories alongside dynamic Excel dashboard architecture."),
            ("Regional Lead:", "West Region leads overall performance with $42,306.00 in revenue and $20,443.00 in profit, closely followed by Central ($38,685.00)."),
            ("Excel Architecture:", "4-tab workbook (Raw Data, Cleaned Data, Formula Analysis, Dashboard) using dynamic formulas (=SUMIFS, =AVERAGE)."),
            ("Non-Technical Usability:", "Empowers executive decision-makers with interactive KPI tiles and real-time summary calculations.")
        ],
        r'Internship_Documentation\ShadowFox_Internship_Documentation\Screenshots\p1_regional_performance.png'
    )

    # ==========================================
    # SLIDE 8: INTERMEDIATE LEVEL OVERVIEW
    # ==========================================
    s8 = prs.slides.add_slide(blank_layout)
    add_slide_header(s8, "INTERMEDIATE LEVEL: Customer Analytics Overview", 8)
    
    i_box = s8.shapes.add_textbox(Inches(1.0), Inches(1.8), Inches(11.0), Inches(5.0))
    itf = i_box.text_frame
    itf.word_wrap = True
    
    ip1 = itf.paragraphs[0]
    ip1.text = "Task: Customer Behaviour, Revenue, and Retention Analytics"
    ip1.font.name = 'Calibri'
    ip1.font.size = Pt(18)
    ip1.font.bold = True
    ip1.font.color.rgb = COLOR_TEAL
    ip1.space_after = Pt(14)
    
    bullets_s8 = [
        ("Business Problem: ", "A direct-to-consumer e-commerce brand needed to quantify customer persistence, repeat purchase velocity, and RFM spend concentration across 24 months of transactional data."),
        ("Dataset & Cleaning: ", "Evaluated 2,336 raw records across 850 customer accounts spanning 2023–2024. Cleaned 30 duplicates, standardized schemas, and engineered Cohort_Month and Cohort_Index tags."),
        ("Behavioral Segmentation: ", "Implemented an 8-cluster RFM framework (Champions, Loyal Customers, At Risk, etc.) binned via Recency, Frequency, and Monetary quintile scoring."),
        ("Relational Database & SQL: ", "Established an SQLite database (customer_analytics.db) and authored 10 production SQL queries utilizing Common Table Expressions (CTEs) and Window Functions (DENSE_RANK, LAG, NTILE)."),
        ("Key Outcome: ", "Uncovered that repeat buyers generate 80.88% of total revenue and formulated an automated Day 3-10-21 retention sequence.")
    ]
    for pre, text in bullets_s8:
        p = itf.add_paragraph()
        p.space_after = Pt(10)
        r_pre = p.add_run()
        r_pre.text = "• " + pre
        r_pre.font.name = 'Calibri'
        r_pre.font.size = Pt(15)
        r_pre.font.bold = True
        r_pre.font.color.rgb = COLOR_TITLE
        
        r_txt = p.add_run()
        r_txt.text = text
        r_txt.font.name = 'Calibri'
        r_txt.font.size = Pt(15)
        r_txt.font.color.rgb = COLOR_BODY

    # ==========================================
    # SLIDE 9: INTERMEDIATE - REPEAT VS ONE-TIME
    # ==========================================
    add_split_slide(
        prs,
        "Customer Spend Dynamics: Repeat vs One-Time Buyers",
        9,
        [
            ("Description:", "Spend share distribution comparing repeat purchasers against single-order buyers across 850 accounts."),
            ("Massive Asymmetry:", "Repeat buyers make up only 46.94% of the customer base (399 accounts) but drive 80.88% of total revenue ($264,508.51)."),
            ("Lifetime Value Gap:", "Average LTV for repeat buyers is $662.93, representing a 4.8x multiplier over one-time buyers ($138.07)."),
            ("Strategic Focus:", "Allocating marketing budget toward post-purchase reactivation yields dramatically higher ROI than top-of-funnel acquisition alone.")
        ],
        r'Internship_Documentation\ShadowFox_Internship_Documentation\Screenshots\p2_repeat_vs_onetime_revenue.png'
    )

    # ==========================================
    # SLIDE 10: INTERMEDIATE - RFM SEGMENTATION
    # ==========================================
    add_split_slide(
        prs,
        "RFM Customer Segmentation & Spend Concentration",
        10,
        [
            ("Description:", "Customer segmentation framework categorizing 850 accounts across Recency, Frequency, and Monetary quintiles."),
            ("Champions Dominate:", "200 Champions alone account for $162,963.95 (49.83% of total brand sales) with an average of 5.7 purchases per account."),
            ("Pareto Rule Confirmed:", "The top 20% of customers deliver 56.04% of cumulative revenue; top two segments account for 69.51%."),
            ("Targeted Action:", "Deploy automated VIP concierge perks for Champions while launching win-back incentives for the $19.5k 'At Risk' segment.")
        ],
        r'Internship_Documentation\ShadowFox_Internship_Documentation\Screenshots\p2_rfm_segments_distribution.png'
    )

    # ==========================================
    # SLIDE 11: INTERMEDIATE - COHORT RETENTION HEATMAP
    # ==========================================
    add_split_slide(
        prs,
        "24-Month Cohort Retention Heatmap & Churn Dynamics",
        11,
        [
            ("Description:", "Seaborn retention heatmap tracking customer persistence percentage across 24 monthly acquisition cohorts."),
            ("Steep Drop-Off:", "The primary attrition bottleneck occurs between Month 0 and Month 1, where retention drops from 100% to ~20%."),
            ("Stabilized Loyalty Core:", "From Month 3 through Month 12, retention stabilizes at a resilient 12% to 16% long-term baseline."),
            ("Intervention Strategy:", "Implement an automated Day 3-10-21 email sequence to guide first-time buyers toward their critical second purchase.")
        ],
        r'Internship_Documentation\ShadowFox_Internship_Documentation\Screenshots\p2_cohort_retention_heatmap.png'
    )

    # ==========================================
    # SLIDE 12: INTERMEDIATE - RELATIONAL SQL ANALYTICS
    # ==========================================
    s12 = prs.slides.add_slide(blank_layout)
    add_slide_header(s12, "Relational Database & Advanced SQL Analytics", 12)
    
    sql_box = s12.shapes.add_textbox(Inches(1.0), Inches(1.8), Inches(11.0), Inches(5.0))
    stf = sql_box.text_frame
    stf.word_wrap = True
    
    sp1 = stf.paragraphs[0]
    sp1.text = "Production SQL Query Engine (SQLite & ANSI SQL-99)"
    sp1.font.name = 'Calibri'
    sp1.font.size = Pt(18)
    sp1.font.bold = True
    sp1.font.color.rgb = COLOR_TEAL
    sp1.space_after = Pt(14)
    
    bullets_s12 = [
        ("Database Architecture: ", "Normalized 2,306 transactions into relational customers, products, and transactions tables with foreign key constraints in customer_analytics.db."),
        ("Ranking Functions: ", "Query 5 implemented DENSE_RANK() OVER (PARTITION BY Customer_Region ORDER BY Total_Spend DESC) to identify top 3 VIP accounts in each geographic territory."),
        ("Time-Series Analytics: ", "Query 6 utilized LAG(Monthly_Revenue, 1) OVER (ORDER BY Year_Month) to compute exact Month-over-Month (MoM) revenue growth percentages."),
        ("Cumulative Aggregations: ", "Query 7 computed running total revenue across 24 months using SUM(Monthly_Revenue) OVER (ORDER BY Year_Month ROWS UNBOUNDED PRECEDING)."),
        ("Spend Quintile Binning: ", "Query 9 applied NTILE(5) OVER (ORDER BY Total_Spend DESC) to group the customer base into mathematical spend quintiles."),
        ("Verification: ", "All 10 queries executed via Python automation script (execute_sql_queries.py) with zero errors, exporting verified CSV reports.")
    ]
    for pre, text in bullets_s12:
        p = stf.add_paragraph()
        p.space_after = Pt(8)
        r_pre = p.add_run()
        r_pre.text = "• " + pre
        r_pre.font.name = 'Calibri'
        r_pre.font.size = Pt(14)
        r_pre.font.bold = True
        r_pre.font.color.rgb = COLOR_TITLE
        
        r_txt = p.add_run()
        r_txt.text = text
        r_txt.font.name = 'Calibri'
        r_txt.font.size = Pt(14)
        r_txt.font.color.rgb = COLOR_BODY

    # ==========================================
    # SLIDE 13: ADVANCED LEVEL OVERVIEW
    # ==========================================
    s13 = prs.slides.add_slide(blank_layout)
    add_slide_header(s13, "ADVANCED LEVEL: Executive Power BI Dashboard", 13)
    
    adv_box = s13.shapes.add_textbox(Inches(1.0), Inches(1.8), Inches(11.0), Inches(5.0))
    atf = adv_box.text_frame
    atf.word_wrap = True
    
    ap1 = atf.paragraphs[0]
    ap1.text = "Task: Enterprise BI Architecture, Star Schema & Logistics SLAs"
    ap1.font.name = 'Calibri'
    ap1.font.size = Pt(18)
    ap1.font.bold = True
    ap1.font.color.rgb = COLOR_TEAL
    ap1.space_after = Pt(14)
    
    bullets_s13 = [
        ("Business Objective: ", "Architect an enterprise reporting system for a global distributor (FY 2022–2024) to monitor revenue velocity, budget targets, and supply chain delivery compliance."),
        ("Dimensional Star Schema: ", "Engineered 6 relational tables: Fact_Orders (4,200 rows), Fact_Targets (1,080 rows), Dim_Date (1,096 days), Dim_Products (1,241 SKUs), Dim_Customers (600 accounts), Dim_Geography (10 hubs)."),
        ("DAX Measures Library: ", "Authored 28 production DAX measures covering Core Financials, Time Intelligence (TOTALYTD, SAMEPERIODLASTYEAR), Target Variances, and Logistics SLAs."),
        ("Verified 3-Year Metrics: ", "Total Sales: $2,929,341.17 | Net Profit: $1,124,915.67 | Operating Margin: 38.40% | Annual YoY Growth: +96.4% in 2023, +24.5% in 2024."),
        ("Supply Chain Discovery: ", "Identified a critical logistics bottleneck where overall SLA compliance is 68.83% against an 85.00% target, driven by Standard Class ground shipping delays.")
    ]
    for pre, text in bullets_s13:
        p = atf.add_paragraph()
        p.space_after = Pt(10)
        r_pre = p.add_run()
        r_pre.text = "• " + pre
        r_pre.font.name = 'Calibri'
        r_pre.font.size = Pt(15)
        r_pre.font.bold = True
        r_pre.font.color.rgb = COLOR_TITLE
        
        r_txt = p.add_run()
        r_txt.text = text
        r_txt.font.name = 'Calibri'
        r_txt.font.size = Pt(15)
        r_txt.font.color.rgb = COLOR_BODY

    # ==========================================
    # SLIDE 14: ADVANCED - EXECUTIVE DASHBOARD
    # ==========================================
    add_split_slide(
        prs,
        "Executive Financial Scorecard & Growth Velocity",
        14,
        [
            ("Description:", "High-resolution Power BI dashboard mockups displaying multi-year sales velocity, operating profit, and product vertical distribution."),
            ("Consolidated Revenue:", "3-Year Gross Sales reached $2,929,341.17 with $1,124,915.67 in Net Operating Profit at an exceptional 38.40% margin."),
            ("YoY Velocity:", "Annual revenue expanded from $541.6k (FY22) to $1,063.8k in FY23 (+96.40%) and reached $1,323.9k in FY24 (+24.46%)."),
            ("UI Design System:", "Engineered modern dark-mode palette (#0B192C, #1E3E62, #FF6500) with visual hierarchy, KPI summary cards, and drill-down paths.")
        ],
        r'Internship_Documentation\ShadowFox_Internship_Documentation\Screenshots\p3_powerbi_executive_overview.png'
    )

    # ==========================================
    # SLIDE 15: ADVANCED - LOGISTICS & SLA COMPLIANCE
    # ==========================================
    add_split_slide(
        prs,
        "Supply Chain & On-Time Delivery SLA Compliance",
        15,
        [
            ("Description:", "Evaluation of fulfillment transit duration and On-Time Delivery SLA compliance across fulfillment tiers."),
            ("Severe SLA Shortfall:", "Overall On-Time Delivery SLA sits at 68.83%, failing to meet the executive target benchmark of 85.00%."),
            ("Fulfillment Disparity:", "Same Day (92.42%) and First Class (81.75%) shipping perform strongly, but Standard Class ground shipping achieves only 59.20% on-time delivery."),
            ("Executive Action:", "Renegotiate 3PL regional carrier contracts and introduce ground hub transit tracking to remediate the 40.8% failure rate.")
        ],
        r'Internship_Documentation\ShadowFox_Internship_Documentation\Screenshots\p3_logistics_sla_compliance.png'
    )

    # ==========================================
    # SLIDE 16: CONCLUSION & STRATEGIC RECOMMENDATIONS
    # ==========================================
    s16 = prs.slides.add_slide(blank_layout)
    add_slide_header(s16, "Conclusion & Strategic Business Recommendations", 16)
    
    c_box16 = s16.shapes.add_textbox(Inches(1.0), Inches(1.8), Inches(11.0), Inches(5.0))
    ctf16 = c_box16.text_frame
    ctf16.word_wrap = True
    
    cp1 = ctf16.paragraphs[0]
    cp1.text = "Data-Backed Action Plan Across Beginner, Intermediate & Advanced Levels"
    cp1.font.name = 'Calibri'
    cp1.font.size = Pt(18)
    cp1.font.bold = True
    cp1.font.color.rgb = COLOR_TEAL
    cp1.space_after = Pt(14)
    
    bullets_s16 = [
        ("1. Merchandising Bundles (Sales): ", "Capitalize on Furniture/Electronics volume ($143k) by bundling them with high-margin Office Supplies (Gel Ink Pens at 67.7% margin) to elevate overall gross margin."),
        ("2. Automated Lifecycle Marketing (Retention): ", "Deploy an automated Day 3-10-21 post-purchase email onboarding flow to bridge the steep 80% Month 1 drop-off and nurture repeat buyers (who drive 80.88% of revenue)."),
        ("3. Carrier Contract Restructuring (Logistics): ", "Restructure Standard Class 3PL logistics agreements to eliminate ground fulfillment bottlenecks and elevate On-Time Delivery SLA compliance from 68.83% back above 85.00%."),
        ("4. Technical Competency & Tool Mastery: ", "Successfully demonstrated end-to-end data analyst proficiency across Python, SQLite, Relational SQL, Microsoft Excel, and Microsoft Power BI.")
    ]
    for pre, text in bullets_s16:
        p = ctf16.add_paragraph()
        p.space_after = Pt(10)
        r_pre = p.add_run()
        r_pre.text = pre
        r_pre.font.name = 'Calibri'
        r_pre.font.size = Pt(15)
        r_pre.font.bold = True
        r_pre.font.color.rgb = COLOR_TITLE
        
        r_txt = p.add_run()
        r_txt.text = text
        r_txt.font.name = 'Calibri'
        r_txt.font.size = Pt(15)
        r_txt.font.color.rgb = COLOR_BODY

    # ==========================================
    # SLIDE 17: THANK YOU (Matching Sample PDF)
    # ==========================================
    s17 = prs.slides.add_slide(blank_layout)
    add_background_decor(s17)
    
    # Large soft box matching page 13 of sample
    bg_box = s17.shapes.add_shape(
        MSO_SHAPE.RECTANGLE,
        Inches(1.8), Inches(1.8), Inches(9.7), Inches(3.9)
    )
    bg_box.fill.solid()
    bg_box.fill.fore_color.rgb = RGBColor(238, 246, 248)
    bg_box.line.fill.background()
    
    ty_box = s17.shapes.add_textbox(Inches(2.0), Inches(2.6), Inches(9.3), Inches(1.5))
    ty_tf = ty_box.text_frame
    tp = ty_tf.paragraphs[0]
    tp.text = "THANK YOU"
    tp.font.name = 'Calibri'
    tp.font.size = Pt(44)
    tp.font.bold = True
    tp.font.color.rgb = COLOR_TITLE
    tp.alignment = PP_ALIGN.CENTER
    
    repo_box = s17.shapes.add_textbox(Inches(2.0), Inches(4.2), Inches(9.3), Inches(1.2))
    rtf = repo_box.text_frame
    
    rp1 = rtf.paragraphs[0]
    rp1.text = "ShadowFox Data Analyst Internship Capstone Portfolio"
    rp1.font.name = 'Calibri'
    rp1.font.size = Pt(16)
    rp1.font.color.rgb = COLOR_TEAL
    rp1.alignment = PP_ALIGN.CENTER
    
    rp2 = rtf.add_paragraph()
    rp2.text = "GitHub: https://github.com/Keerthanagowda42/ShadowFox_Data_Analyst_Internship"
    rp2.font.name = 'Calibri'
    rp2.font.size = Pt(13)
    rp2.font.color.rgb = COLOR_MUTED
    rp2.alignment = PP_ALIGN.CENTER

    # Save to both target locations
    out_paths = [
        r'Internship_Documentation\ShadowFox_Internship_Documentation\Presentation\ShadowFox_Data_Analyst_Internship_Presentation.pptx',
        r'ShadowFox_Internship_Documentation\Presentation\ShadowFox_Data_Analyst_Internship_Presentation.pptx'
    ]
    for p in out_paths:
        os.makedirs(os.path.dirname(p), exist_ok=True)
        prs.save(p)
        print(f'Saved presentation to: {p}')

if __name__ == '__main__':
    create_presentation()
