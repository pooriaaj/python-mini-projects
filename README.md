# Python Learning Projects

This repository contains a collection of small Python projects created to practice and strengthen programming and data analysis skills.  
Each project focuses on a different concept — from core Python (loops, functions, data structures) to data manipulation, cleaning, and visualization with **NumPy**, **Pandas**, and **Seaborn**.

---

## Projects

### 1. To-Do List Manager
A command-line application for managing simple daily tasks.

**Key Features:**
- Add, remove, and display tasks using commands  
- Runs continuously until the user chooses to quit  
- Great for practicing list operations, user input, and control flow

**Concepts Practiced:**
- Lists  
- Loops  
- Functions  
- Conditional logic

---

### 2. Student Performance Report
A Pandas-based data analysis script that merges student info with subject scores and calculates performance metrics.

**Key Features:**
- Merges multiple DataFrames  
- Calculates average scores and pass/fail status  
- Categorizes performance (Excellent / Good / Needs Work)  
- Groups by class to summarize averages and pass rates  
- Ranks students by overall performance

**Concepts Practiced:**
- DataFrame creation and manipulation  
- Merging and joining  
- Grouping and aggregation  
- Conditional logic using `np.select`  
- Ranking and summary reporting

---

### 3. Data Cleaning Practice
A project focused on cleaning and preparing messy data using **Pandas** and **NumPy**.  
It transforms an imperfect dataset — with duplicates, missing values, inconsistent formats, and extra spaces — into a clean and structured DataFrame ready for analysis.

**Key Features:**
- Removes duplicates  
- Drops invalid rows  
- Fills missing values with mean or median  
- Converts data types (`to_numeric`, `to_datetime`)  
- Normalizes text (trim spaces, title-case, uppercase)  
- Extracts new features (year, month)  
- Validates data completeness and consistency

**Concepts Practiced:**
- Data cleaning and preprocessing  
- Handling missing values  
- Type conversion  
- Text normalization  
- Feature engineering  
- Data validation and summary checks

---

### 4. Sales Analysis Notebook
A complete analysis notebook combining data cleaning, categorization, grouping, and visualization using **Pandas**, **NumPy**, **Matplotlib**, and **Seaborn**.  
It demonstrates how to build reusable components with classes and apply real-world analysis on sales data.

**Key Features:**
- Handles missing and inconsistent data  
- Creates **price bands** (Cheap / Affordable / Expensive)  
- Summarizes **revenue by region**, **monthly revenue by class**, and **price distribution**  
- Uses **OOP design**:  
  - `SalesAnalyzer` class for calculations  
  - `SalesVisualizer` class for charts  
- Visualizes data with bar plots and count plots using **Seaborn**

**Concepts Practiced:**
- Object-Oriented Programming (OOP) in data analysis  
- Data cleaning and feature engineering  
- Grouping and aggregation  
- Visualization with Seaborn & Matplotlib  
- Quantile-based categorization  
- Multi-dimensional analysis

---

## Skills Covered
- Core Python (data types, loops, functions, conditionals)  
- Object-Oriented Programming  
- NumPy (arrays, operations, slicing)  
- Pandas (data analysis, merging, grouping, cleaning)  
- Data Cleaning and Feature Engineering  
- Seaborn and Matplotlib Visualizations  
- Exploratory Data Analysis (EDA)  
- Clean code organization and documentation

---

## Repository Structure
python-mini-projects/
│
├── README.md
│
├── todo_list_manager/
│ ├── todo.py
│ └── README.md
│
├── student_performance_report/
│ ├── student_report.py
│ └── README.md
│
├── data_cleaning_practice/
│ ├── data_cleaning.py
│ └── README.md
│
└── sales_analysis_notebook/
├── sales_analysis.ipynb
└── README.md

Each folder contains the source code (or notebook) and a dedicated README describing that specific project.

---

## Next Steps
This repository will continue to grow with more projects, including:
- Advanced data visualization (Matplotlib, Seaborn)  
- Algorithm and data structure exercises  
- Exploratory Data Analysis (EDA) projects  
- Mini data science analyses and reports  
- Introduction to Machine Learning (Scikit-learn)

The goal is to build a clear, well-documented learning portfolio showing consistent progress in Python programming, data cleaning, analysis, and visualization.
