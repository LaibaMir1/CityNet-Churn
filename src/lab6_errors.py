import pandas as pd
from sklearn.inspection import permutation_importance
from sklearn.metrics import average_precision_score
from common import load_split
from lab5_evaluate import train_model
X_train, X_val, X_test, y_train, y_val, y_test = load_split()
pipe = train_model(X_train, y_train)
imp = permutation_importance(pipe, X_val, y_val, scoring="average_precision",
                             n_repeats=10, random_state=42)
print(pd.Series(imp.importances_mean, index=X_val.columns).nlargest(4).round(3).to_dict())
val = X_val.assign(churned=y_val.to_numpy(), caught=pipe.predict(X_val) == 1)
churners = val[val.churned == 1]
print(churners.groupby("caught")[["tenure_months", "outage_hours_90d"]].mean().round(1))
print(churners.groupby("region")["caught"].mean().round(2).to_dict())
print("TEST PR-AUC, run once at the end:",
      round(average_precision_score(y_test, pipe.predict_proba(X_test)[:, 1]), 3))



# Lab 6 findings (validation set, then test once):
# - Most important columns: tenure_months (0.13), auto_pay (0.044),
#   support_calls_90d (0.043), paid_late_last_bill (0.026).
# - Who we miss: quiet long-time customers. Missed churners average 43.2 months
#   of tenure vs 18.9 months for the churners we catch.
# - Fairness: only 50% of East-region churners are caught vs 68-76% elsewhere.
# - TEST PR-AUC (run once, never tune after this): 0.361 vs baseline 0.179.