# 🧹 Data Cleaning Practice

This project demonstrates practical data cleaning using **Pandas** and **NumPy**.  
It starts from a messy dataset with duplicates, inconsistent formats, and missing values — and transforms it into a clean, reliable dataset ready for analysis.

---

## 🎯 Objective
To simulate a real-world scenario where raw data must be cleaned before analysis, applying multiple transformation steps to ensure consistency and quality.

---

## 🧰 Cleaning Steps
1. **Remove Duplicates** → Keep unique records only  
2. **Drop Missing Names** → Remove invalid rows  
3. **Handle Missing Scores** → Fill with mean value  
4. **Convert Age to Numeric** → Replace invalids with median  
5. **Standardize Dates** → Convert all formats to `datetime`  
6. **Normalize Text Fields** → Strip spaces, fix case  
7. **Extract Features** → Add `JoinYear` and `JoinMonth`  
8. **Check Quality** → Validate types and missing counts

---

## 🧠 Skills Practiced
- Handling missing data (`dropna`, `fillna`)  
- Converting data types (`to_numeric`, `to_datetime`)  
- Text normalization (`str.strip`, `str.title`, `str.upper`)  
- Feature engineering from date columns  
- Data validation and summary checks  

---

## ▶️ How to Run
```bash
cd data_cleaning_practice
python data_cleaning.py
``` 
✅ Output Example
RAW DATA
   Name  Age  Score    JoinDate Class
0  Ali   23   84.0  2023-02-01     a
...

CLEANED DATA
   Name  Age  Score    JoinDate Class  JoinYear  JoinMonth
0  Ali   23   84.00  2023-02-01     A     2023          2
1  Sara  25   86.60  2023-03-05     A     2023          3
...

SHAPE: (5, 7)
MISSING VALUES: 0 across all columns


🏁 Outcome

A fully cleaned and structured dataset — demonstrating end-to-end data preparation skills, crucial for data analysis, machine learning, and reporting workflows.
