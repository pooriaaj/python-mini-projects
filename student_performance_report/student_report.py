import pandas as pd
import numpy as np

students = pd.DataFrame({
    "Name": ["Ali", "Reza", "Sara"],
    "ID": [1, 2, 3],
    "Class": ["A", "B", "C"]
})

scores = pd.DataFrame({
    "ID": [1, 2, 3],
    "Math": [84, 91, 77],
    "Science": [87, 94, 81],
    "English": [74, 86, 95]
})

merged = students.merge(scores, on="ID", how="left")
merged["Average"] = merged[["Math", "Science", "English"]].mean(axis=1).round(2)
merged["Passed"] = merged["Average"] >= 85
merged["Category"] = np.select(
    [merged["Average"] >= 90, merged["Average"] >= 80],
    ["Excellent", "Good"],
    default="Needs Work"
)

summary = (
    merged.groupby("Class")
    .agg(
        Math_mean=("Math", "mean"),
        Science_mean=("Science", "mean"),
        English_mean=("English", "mean"),
        Pass_rate=("Passed", "mean")
    )
    .round(2)
)

ranked = merged.sort_values(by="Average", ascending=False)

print(" Full merged data:\n", merged, "\n")
print(" Summary by Class:\n", summary, "\n")
print(" Ranked by Average:\n", ranked, "\n")
