# ShadowFox Data Analyst Internship: Final Video Presentation Script

**Presentation Duration**: 3 to 5 Minutes  
**Speaker**: Candidate (ShadowFox Data Analyst Intern)  
**Tone**: Professional, confident, articulate, data-driven  
**Format**: Screen share with candidate webcam in corner (via Loom, Zoom, or OBS)  

---

## Visual Presentation Outline (Slides / Screen Sequence)
- **0:00 - 0:35**: Slide 1 — Introduction & Internship Portfolio Overview (Title Slide)
- **0:35 - 1:40**: Screen Share 1 — Project 1: Beginner Small Business Sales & Excel Dashboard
- **1:40 - 2:50**: Screen Share 2 — Project 2: Intermediate Customer Behavior, RFM & SQL Analytics
- **2:50 - 4:05**: Screen Share 3 — Project 3: Advanced Power BI Executive BI Dashboard & Star Schema
- **4:05 - 4:45**: Slide 5 — Summary, Impact & Conclusion

---

## Word-for-Word Presentation Script

### [0:00 – 0:35] Introduction
*(Camera on candidate. Show presentation Title Slide: "ShadowFox Data Analyst Internship — Portfolio Showcase".)*

> "Hello everyone, my name is **[Your Full Name]**, and today I am excited to present the complete capstone deliverables for my **ShadowFox Data Analyst Internship**.
>
> Over the course of this internship, I tackled three comprehensive, real-world business challenges progressing from Beginner to Advanced levels. I utilized **Python, Pandas, NumPy, Matplotlib, Seaborn, Relational SQL, Microsoft Excel, and Power BI**.
>
> Today, I will walk you through the business problem, analytical methodologies, key findings, and strategic recommendations for all three projects. Let’s dive in!"

---

### [0:35 – 1:40] Project 1: Beginner Level — Small Business Sales Analysis
*(Switch screen to show the Excel Dashboard `Small_Business_Sales_Dashboard.xlsx` and the charts in `Beginner_Sales_Analysis/charts/`.)*

> "For Project 1, I analyzed a retail small business operating across five geographic territories and four product categories.
>
> The raw data arrived with typical real-world flaws: 20 duplicate orders, inconsistent text casing, mixed date formats, and missing payment attributes. I built an automated Python cleaning pipeline in `data_cleaning.py` to audit and standardize all 1,250 verified transactions.
>
> Here are the core business metrics derived from the data:
> - The business generated **$180,936.50 in Total Gross Revenue**, yielding **$87,709.30 in Net Profit** with an outstanding profit margin of **48.48%**.
> - Average Order Value settled at **$144.75** across 2,662 units sold.
> - **Seasonality**: Sales peaked during Q4, reaching **$23,036 in November** due to holiday purchasing and larger basket sizes, following a mid-year trough in June of **$9,972**.
> - **Category Insights**: Furniture and Electronics accounted for **79% of total revenue**, with the *Ergonomic Office Chair* generating over $43,000 as our top product. However, our highest margin items were accessories—like Gel Ink Pens at **67.7% margin**.
>
> To present these findings to non-technical stakeholders, I constructed an automated 4-tab Excel workbook featuring dynamic formulas (`SUMIFS`, `AVERAGE`), KPI cards, and embedded high-resolution dashboards."

---

### [1:40 – 2:50] Project 2: Intermediate Level — Customer Behavior, RFM & SQL Analytics
*(Switch screen to show `Intermediate_Customer_Analytics/charts/cohort_retention_heatmap.png` and `customer_analysis.sql` open in VS Code.)*

> "Moving to the Intermediate level, Project 2 focused on **Customer Behaviour, Revenue Concentration, and Retention Analytics** across a 24-month multi-year e-commerce dataset of 850 customers and 2,306 transactions.
>
> My analysis yielded three critical behavioral findings:
> 1. **Repeat vs. One-Time Buyers**: While repeat customers make up only **46.9% of our customer base**, they generate **80.88% of total revenue ($264,508)**. On average, a repeat customer delivers **4.8 times higher lifetime value ($662)** than a single-purchase buyer ($138).
> 2. **RFM Segmentation**: I binned customers into 8 behavioral segments based on Recency, Frequency, and Monetary scores. Our top 200 **Champions** alone generate nearly **50% of total revenue ($162,963)** with an average order frequency of 5.7 purchases.
> 3. **Cohort Retention & Churn**: Monthly cohort heatmaps revealed that the steepest drop-off occurs between month 0 and month 1, where retention drops to ~20%, before stabilizing at a healthy 12% to 16% long-term baseline.
>
> On the technical side, I loaded the cleaned data into an **SQLite relational database** and authored 10 production SQL queries utilizing **Common Table Expressions (CTEs)** and advanced **Window Functions**—including `DENSE_RANK()` for regional leaderboards, `LAG()` for month-over-month growth, and `NTILE(5)` for spend quintiles."

---

### [2:50 – 4:05] Project 3: Advanced Level — Executive BI Dashboard Using Power BI
*(Switch screen to show `Advanced_PowerBI_Dashboard/dashboard/PowerBI_Executive_Dashboard_Render.png` and the Star Schema architecture in `data_dictionary.md`.)*

> "For the Advanced level, I designed and developed an **Executive Business Intelligence Dashboard** for an enterprise commercial distributor spanning FY 2022 through FY 2024.
>
> I chose a multi-year global retail operations dataset because it supports a true **Star Schema architecture**. I engineered and exported 6 distinct relational tables: `Fact_Orders` (4,200 rows), `Fact_Targets`, and dimensions for `Date`, `Customers`, `Products`, and `Geography`.
>
> In Power BI, I authored a library of **28 production DAX measures** covering Time Intelligence, Target Variance, and Logistics SLAs.
>
> Key executive findings include:
> - **3-Year Revenue reached $2,929,341.17**, with Net Operating Profit of **$1,124,915.67** at a rock-solid **38.40% profit margin**.
> - Revenue expanded rapidly—growing **+96.4% in 2023** and another **+24.3% in 2024**, reaching $1.32M annually.
> - **Operational Risk Identified**: While profitability is stellar, our **On-Time Delivery SLA is currently 68.83%**, falling far short of our 85% target. Standard Class shipping achieved only 59.2% compliance due to 3PL carrier bottlenecks.
>
> I created full wireframes, a modern dark-mode palette (`#0B192C` and `#1E3E62`), and a complete step-by-step implementation guide for loading and visualizing the data in Power BI Desktop."

---

### [4:05 – 4:45] Conclusion & Recommendations
*(Switch back to candidate webcam / Final Summary Slide.)*

> "To synthesize the strategic recommendations across all three levels:
> 1. In sales, we must bundle high-revenue furniture with high-margin desk accessories to lift average basket margins.
> 2. In customer marketing, we must implement an automated Day 3-10-21 email sequence to bridge the 53% drop between the first and second orders.
> 3. In supply chain, we must renegotiate 3PL ground carrier contracts to restore our delivery SLA from 68.8% back above 85%.
>
> All datasets, source code, SQL queries, Excel workbooks, visual charts, and documentation are organized and pushed to my GitHub repository.
>
> Thank you to the **ShadowFox team** for this incredible learning experience. I look forward to your evaluation and feedback!"

---

## Presentation Delivery Tips
1. **Pacing**: Speak at a steady, measured pace. Aim for around 130 to 140 words per minute.
2. **Camera Position**: Position your webcam at eye level with good front lighting.
3. **Screen Sharing**: Have your folders, charts, and Excel sheet open in background tabs before starting so transitions are smooth.
4. **Recording Tool**: Use **Loom** (free browser extension) or **OBS Studio** to record screen + webcam simultaneously.
5. **Uploading**: Upload the final `.mp4` video to your Google Drive, right-click > **Share** > set permission to **"Anyone with the link can view"**, and paste the link into your submission form.
