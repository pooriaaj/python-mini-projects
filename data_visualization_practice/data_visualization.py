# 1) Create dataset
# -----------------------------
Products = pd.DataFrame({
    "Class": ["A", "B", "A", "C"],
    "Region": ["East", "West", "North", "East"],
    "Month": ["Jan", "Jan", "Feb", "Feb"],
    "Units_sold": [120, 95, 80, 110],
    "Unit_price": [15, 20, 15, 10],
})
Products["Revenue"] = Products["Units_sold"] * Products["Unit_price"]

# Quick sanity prints (optional)
print("Data:")
print(Products, "\n")

# -----------------------------
# 2) Prepare simple summaries
# -----------------------------
# Line: monthly totals (Revenue and Units_sold)
monthly = Products.groupby("Month")[["Revenue", "Units_sold"]].sum().sort_index()

# Bar: revenue by region
region_revenue = Products.groupby("Region")["Revenue"].sum().sort_values(ascending=False)

# Histogram: distribution of Revenue (raw)
revenue_series = Products["Revenue"]

# Scatter: relationship between Units_sold and Revenue
x_units = Products["Units_sold"]
y_revenue = Products["Revenue"]

# -----------------------------
# 3) Plot 1 — Line chart (trend)
# -----------------------------
plt.figure(figsize=(7, 4))
monthly.plot(kind="line", marker="o")
plt.title("Monthly Revenue & Units Sold")
plt.xlabel("Month")
plt.ylabel("Value")
plt.grid(True)
plt.tight_layout()
plt.show()

# -----------------------------
# 4) Plot 2 — Bar chart (categories)
# -----------------------------
plt.figure(figsize=(7, 4))
region_revenue.plot(kind="bar")
plt.title("Total Revenue by Region")
plt.xlabel("Region")
plt.ylabel("Revenue")
plt.grid(axis="y")
plt.tight_layout()
plt.show()

# -----------------------------
# 5) Plot 3 — Histogram (distribution)
# -----------------------------
plt.figure(figsize=(7, 4))
plt.hist(revenue_series, bins=5)
plt.title("Revenue Distribution")
plt.xlabel("Revenue")
plt.ylabel("Frequency")
plt.grid(True)
plt.tight_layout()
plt.show()

# -----------------------------
# 6) Plot 4 — Scatter (relationship)
# -----------------------------
plt.figure(figsize=(7, 4))
plt.scatter(x_units, y_revenue)
plt.title("Revenue vs. Units Sold")
plt.xlabel("Units Sold")
plt.ylabel("Revenue")
plt.grid(True)
plt.tight_layout()
plt.show()
