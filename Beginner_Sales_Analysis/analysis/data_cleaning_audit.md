# Data Cleaning Audit Log - Project 1 (Small Business Sales)

## Summary of Operations:
- **Raw File**: raw_sales_data.csv
- **Cleaned File**: cleaned_sales_data.csv
- **Initial Row Count**: 1270
- **Duplicates Identified and Removed**: 20
- **Rows After De-duplication**: 1250
- **Missing 'Payment Method' Imputed**: 37 (Imputed value: 'Not Specified')
- **Categories Normalized**: Title-cased and standardized ('Office-Supplies' -> 'Office Supplies')
- **Regions Standardized**: Title-cased and whitespace trimmed
- **Price/Sales Cleaned**: Stripped '$' currency symbols and enforced float64
- **Date Standardization**: Parsed mixed formats ('MM/DD/YYYY', 'DD-MM-YYYY', 'YYYY-MM-DD') into ISO-8601 ('YYYY-MM-DD')
- **Feature Engineering**: Added `Profit Margin %`, `Year`, `Month`, `Month Name`, `Year-Month`, `Quarter`
- **Integrity Validation**: Recalculated `Profit = Sales - Cost` to guarantee mathematical consistency
- **Final Cleaned Record Count**: 1250 rows, 17 columns
