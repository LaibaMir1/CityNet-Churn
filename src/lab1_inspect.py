import pandas as pd
df = pd.read_csv("./../data/citynet_churn.csv")
print("SHAPE OF THE DATAFRAME:", df.shape) # prints the shape of the dataframe (rows, columns)


print("\nHow many columns need encoding and how many need scaling", df.dtypes.astype(str).value_counts().to_dict())
#df.dtypes is the type of each column and value_counts count show many 
#columns of each type there are. 

#EDA 
#count no of empty cells in the csv 
missing = df.isna().sum()
print("\nMissing values in each column:", missing[missing>0].to_dict()) # last exp keeps the columns that actually have gaps

print("\nChurned:", df["churned"].value_counts(normalize=True).round(3).to_dict())
#tells what percent left the company and what percent stayed
#normalize=true gives shres instead of counts, round(3) rounds to 3 decimal places, to_dict() converts to dictionary

print(df[["tenure_months", "support_calls_90d", "outage_hours_90d"]].describe()
      .loc[["mean", "min", "max"]].round(1))
#describe gives stas 

print("churn by support calls:",
      df.groupby("support_calls_90d")["churned"].mean().round(2).head(6).to_dict())
print("churn by cancel_request_logged:",
      df.groupby("cancel_request_logged")["churned"].mean().round(3).to_dict())
#first one gives churn rate of each column value, second one gives churn rate of each column value for cancel_request_logged

# TODO 1: Which column is missing values, and how many?
#------------payment_method 149 and age 411
# TODO 2: What share of customers churned? Is the data balanced?
#------------0.2 churned, 0.8 not churned, so not balanced
# TODO 3: One column predicts churn almost perfectly. Which one, and why must we NOT use it?
#------------cancel_request_logged and support calls, because it is a direct indicator of churn
