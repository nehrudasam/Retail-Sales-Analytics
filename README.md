**Retail Sales Analytics Project**
**Project Overview**

This project performs end-to-end retail sales data analysis using Python. The objective is to extract meaningful business insights from transactional retail data and evaluate overall business performance across categories, regions, and products.

The analysis includes KPI generation, category-level evaluation, regional performance comparison, product-level insights, and discount impact analysis on profitability.

**Dataset Information**

Dataset: Superstore Retail Dataset

Total Records: 9,994 transactions

Total Columns: 21

Data includes sales, profit, discount, product details, customer details, and regional information

**Business Objectives**

Calculate overall business KPIs

Identify top-performing product categories

Analyze regional sales and profitability

Detect top revenue-generating products

Examine the relationship between discount and profit

Key Performance Indicators (KPI Summary)

Total Sales: 2,297,200.86

Total Profit: 286,397.02

Total Orders: 5,009

Overall Profit Margin: 12.47%

**Category Analysis**

Sales by Category:

Technology: 836,154.03

Furniture: 741,999.79

Office Supplies: 719,047.03

Profit by Category:

Technology: 145,454.95

Office Supplies: 122,490.80

Furniture: 18,451.27

Insight:
Technology generates the highest profit, while Furniture has comparatively low profitability.

Regional Performance

Sales by Region:

West: 725,457.82

East: 678,781.24

Central: 501,239.89

South: 391,721.90

Profit by Region:

West: 108,418.45

East: 91,522.78

South: 46,749.43

Central: 39,706.36

Insight:
The West region contributes the highest sales and profit.

Top Performing Products

Top 10 products were identified based on total sales value. The highest revenue-generating product is:

Canon imageCLASS 2200 Advanced Copier (61,599.82)

This indicates that high-value technology products drive significant revenue.

Discount vs Profit Analysis

Correlation between Discount and Profit: -0.219

Insight:
There is a negative correlation between discount and profit, meaning higher discounts tend to reduce profitability.

Technical Implementation
Data Processing

Handled encoding issues during CSV loading

Checked for missing values

Converted date columns into datetime format

Created additional features such as:

Year

Month

Month Name

Profit Margin

Tools and Libraries Used

Python

Pandas

NumPy

Matplotlib

**Project Structure**

Retail-Sales-Analytics/
│
├── analysis.py
├── requirements.txt
├── data/
│ └── Superstore.csv
└── README.md

**How to Run the Project**

Clone the repository

git clone https://github.com/manimalamaha/Retail-Sales-Analytics.git


Navigate into the project directory

cd Retail-Sales-Analytics


Install required dependencies

pip install -r requirements.txt


Run the analysis script

python analysis.py

**Skills Demonstrated**

Data Cleaning and Preprocessing

Exploratory Data Analysis (EDA)

Business KPI Analysis

Correlation Analysis

Feature Engineering

Git and GitHub Version Control

**Conclusion**

This project demonstrates the ability to transform raw retail transaction data into actionable business insights. The analysis highlights revenue drivers, profitability trends, and the impact of discounting strategies on overall profit margins.

It showcases practical data analytics skills suitable for business intelligence and data analyst roles.
