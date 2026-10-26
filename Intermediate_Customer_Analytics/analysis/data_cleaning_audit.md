# Data Cleaning & Transformation Audit - Project 2 (Customer Analytics)

- **Source Dataset**: `raw_customer_data.csv`
- **Cleaned Dataset**: `cleaned_customer_data.csv`
- **Initial Transaction Records**: 2336
- **Duplicate Records Removed**: 30
- **Valid Unique Transactions**: 2306
- **Distinct Customers**: 850
- **Missing Emails Handled**: 56
- **Missing Payment Methods Imputed**: 62
- **Date Standardization**: Unified all mixed formats to ISO-8601 (`YYYY-MM-DD`)
- **Engineered Analytical Features**:
  - `Year`, `Month`, `Year_Month`
  - `First_Purchase_Date` (Customer acquisition timestamp)
  - `Cohort_Month` (Initial acquisition cohort)
  - `Cohort_Index` (Elapsed months since acquisition for retention analysis)
  - Recomputed `Total_Spend = (Quantity * Unit_Price) - Discount_Amount`
