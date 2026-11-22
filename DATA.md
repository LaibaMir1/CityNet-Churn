# Data card: citynet_churn.csv

- Source: CityNet customer records (made-up data for this course)
- Rows:5000   Columns: 14
- One row is: one customer, measured over the last 90 days
- Target: `churned` = 1 if the customer cancelled in the next month. Share of 1s: 17.9%
- Missing values: age 411, payemnt_method 149, filled in the pipeline
- Columns NOT used, and why: customer_id(just a label), cancel_request_logged(might cause leakage)
- Known issues: 
from lab 6 misses long-time customers, east region only 50% caught
