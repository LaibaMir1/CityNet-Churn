# CityNet churn baseline

## User story
As the retention manager, I want a weekly list of the 100 customers most likely to cancel next month, so my team can call them first.

## How to run
    pip install -r requirements.txt
    python src/lab7_save.py                       # train and save the pipeline
    python src/predict.py data/new_customers.csv  # writes reports/predictions.csv

Run every command from the project folder (not from inside `src`).

## Results (validation, then test once)
| Metric | Baseline | Our model |
|---|---|---|
| PR-AUC | 0.179 | 0.396 (validation) · 0.361 (test) |
| Churners in top 100 | about 18 | 49 (validation) |

Model: logistic regression (`class_weight="balanced"`) inside one scikit-learn pipeline (median / most-frequent imputation, scaling, one-hot encoding). Chosen over a random forest (PR-AUC 0.390) and a linear SVM (0.406, a tie), because it scored best in 5-fold cross-validation (0.407), is the simplest to explain, and gives probabilities.

In business terms: calling our top 100 reaches about 2.7× as many churners as 100 random calls.

## Intended use
- Rank customers for the retention team's weekly call list (the top 100 by `churn_risk`).
- Help the team decide who to call first; a person always decides who to call and what to offer.
- Show the main warning signs of churn: short tenure, no auto-pay, many support calls, and paying the last bill late.

## Not for
- Changing prices, contracts or service automatically, without a person reviewing it.
- Judging, penalising or refusing service to individual customers.
- Customers unlike the training data, such as business accounts, new regions or new plans.
- Exact yes/no decisions: the score is a ranking aid, not a certainty.

## Assumptions
- A customer's last 90 days of behaviour predict whether they cancel next month.
- New customers look like the training data (same plans, regions and value ranges).
- The `cancel_request_logged` column is not used, because it is recorded after a customer decides to leave (leakage) and is not available for new customers.
- Customer behaviour changes over time, so the model should be retrained regularly (for example every quarter).

## Risks and limitations
- **Misses quiet long-time customers:** churners the model misses have 43.2 months of tenure on average, vs 18.9 months for the ones it catches.
- **Uneven across regions:** only 50% of churners in the East region are caught, vs 68–76% in other regions.
- **Modest precision:** about half of the top 100 would not have left, so retention offers should be cheap and calls friendly.
- **Honest score:** test PR-AUC (0.361) is lower than validation (0.396); 0.361 is the number to quote.
- **Made-up data:** this is course data; a real deployment would need real data, a privacy review, and monitoring for changes over time.