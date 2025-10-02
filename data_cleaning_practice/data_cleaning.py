import pandas as pd
import numpy as np

raw = pd.DataFrame({
    "Name": [" Ali ", "Sara", "ALI", None, "Reza", "Mina", "Reza"],
    "Age": ["23", "25", "23", "28", None, " 30 ", "23"],
    "Score": [84, None, 84, 91, 77, np.nan, 77],
    "JoinDate": ["2023-02-01", "2023/03/05", "2023-02-01", None, "2023-05-10", "05-20-2023", "2023-05-10"],
    "Class": ["a", "A", "A", "B", "b", "B", "B"]
})

print("RAW DATA")
print(raw)

df1 = raw.drop_duplicates(subset=["Name", "Age", "Score", "JoinDate"])
df1 = df1.dropna(subset=["Name"])

mean_score = df1["Score"].mean()
df1["Score"] = df1["Score"].fillna(round(mean_score, 2))

df1["Age"] = pd.to_numeric(df1["Age"], errors="coerce")
median_age = df1["Age"].median()
df1["Age"] = df1["Age"].fillna(median_age).astype("Int64")

df1["JoinDate"] = pd.to_datetime(df1["JoinDate"], errors="coerce")

df1["Name"] = df1["Name"].str.strip().str.title()
df1["Class"] = df1["Class"].str.upper()

df1["JoinYear"] = df1["JoinDate"].dt.year
df1["JoinMonth"] = df1["JoinDate"].dt.month

print("CLEANED DATA")
print(df1)
print("SHAPE:", df1.shape)
print("DATA TYPES:")
print(df1.dtypes)
print("MISSING VALUES:")
print(df1.isna().sum())
