# 🎓 Student Performance Report

This project demonstrates the ability to **combine datasets**, calculate **key performance metrics**, and generate **class-level insights** using **Pandas** and **NumPy**.

---

## 🎯 Objective
Simulate a real-world scenario where **student information** and **subject scores** are stored separately and must be merged to produce actionable insights such as averages, pass rates, and performance categories.

---

## 🧠 Skills Demonstrated
- **Data Merging** with `merge()`  
- **Feature Engineering** — creating `Average`, `Passed`, and `Category`  
- **Conditional Classification** using `np.select()`  
- **Grouping and Aggregation** with `groupby()` and `agg()`  
- **Sorting and Ranking** with `sort_values()`  
- **Summarization** for reporting

---

## 📊 Outputs Generated
- **Merged Dataset**: combines student info and scores  
- **Average Score** per student  
- **Pass/Fail Status** based on threshold (≥ 85)  
- **Performance Category** (Excellent / Good / Needs Work)  
- **Class Summary Table**: subject averages and pass rates  
- **Ranked List**: students sorted by overall average  

---

## ▶️ Example Output
Full merged data:
Name ID Class Math Science English Average Passed Category
0 Ali 1 A 84 87 74 81.67 False Good
1 Reza 2 B 91 94 86 90.33 True Excellent
2 Sara 3 C 77 81 95 84.33 False Good

Summary by Class:
Math_mean Science_mean English_mean Pass_rate
Class
A 84.00 87.0 74.0 0.00
B 91.00 94.0 86.0 1.00
C 77.00 81.0 95.0 0.00

Ranked by Average:
Name Average Category
1 Reza 90.33 Excellent
2 Sara 84.33 Good
0 Ali 81.67 Good

---

## 🧰 Tools Used
- **Python**  
- **Pandas**  
- **NumPy**

---

## 💡 Outcome
This project highlights the ability to:
- Integrate and analyze multiple datasets  
- Derive insights with KPIs like averages and pass rates  
- Automate performance reporting  
- Present clear summaries useful for decision-making
