import pandas as pd

#Load the dataset
df = pd.read_csv("Jan_24.csv")
print(df.columns)

#Remove rows where dep_time is missing (canceled flights)
df_cleaned = df.dropna(subset=["DEP_TIME"])

#Fill missing dep_delay values with 0
df_cleaned["DEP_DELAY"].fillna(0, inplace=True)

#Save cleaned data
df_cleaned.to_csv("Jan_24_cleaned.csv", index=False)

print(f"Cleaned dataset saved as Jan_24_cleaned.csv with {len(df_cleaned)} rows")

#Display basic info
print("First 5 rows of dataset: ")
print(df.head())

print("\nColumn names: ")
print(df.columns)

print("\nSummary of missing values: ")
print(df_cleaned.isnull().sum())
