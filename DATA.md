# Data card: citynet_churn.csv

- Source: CityNet customer records (made-up data for this course)
- Rows: 5,000   Columns: 14
- One row is: one customer, measured over the last 90 days
- Target: `churned` = 1 if the customer cancelled in the next month. Share of 1s: 17.9% (imbalanced)
- Missing values: `age` 411 rows, `payment_method` 149 rows; filled inside the pipeline (median for age, most frequent value for payment method), learned from the training rows only
- Columns NOT used, and why: `customer_id` (just a label, no information about behaviour); `cancel_request_logged` (leakage: recorded after the customer has already decided to leave, 95.8% churn when it is 1, and not available for new customers)
- Known issues: imbalanced target (only 17.9% churners); `outage_hours_90d` has a long tail (mean 7.2 h, max 65.9 h); regions differ in size and churn rate; one snapshot in time, so patterns may change and the model needs retraining