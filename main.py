"""
Loads daily temperature data from a JSON file.

Computes the average temperature per month for each city using NumPy.

Plots the monthly averages for each city using Matplotlib.
Show a bar chart (histogram) with:

    X-axis: Months

    Y-axis: Temperature delta (°C)

    Bars representing the absolute difference between the two cities.
"""
import json  
import numpy as np
import matplotlib.pyplot as plt # For plotting the graph
# ----------------------------
# Step 1: Load JSON data
# ----------------------------
with open("data.json","r") as file:
    data = json.load(file)
    print(data)

# ----------------------------
# Step 2: Define a function to compute monthly averages
# ----------------------------

"""
| Feature                      | Python List                   | NumPy Array (`np.array`)                |
| ---------------------------- | ----------------------------- | --------------------------------------- |
| **Type**                     | Built-in Python type (`list`) | NumPy type (`ndarray`)                  |
| **Speed**                    | Slower                        | Much faster for large numerical data    |
| **Memory Efficiency**        | Inefficient                   | More compact memory representation      |
| **Data Types**               | Can store mixed types         | Homogeneous (all elements same type)    |
| **Vectorized Operations**    | ❌ No (requires loops)         | ✅ Yes (element-wise operations)         |
| **Broadcasting**             | ❌ No                          | ✅ Yes (automatic size alignment)        |
| **Math Functions**           | Manual or via loops           | Rich library: `np.mean`, `np.sum`, etc. |
| **Multidimensional Support** | Manual nesting                | Native support (1D, 2D, ... nD)         |

"""
# ----------------------------
# Step 2: Define a function to compute monthly averages
# ----------------------------

def compute_monthly_avg(city_data):
    """
    Takes a dictionary of months with daily temperatures and returns
    a dictionary of average temperature per month.
    """
    monthly_avgs = {}
    for month, temps in city_data.items():
        monthly_avgs[month] = np.mean(temps) # Compute average using numpy
    return monthly_avgs

# ----------------------------
# Step 3: Compute averages for each city
# ----------------------------

paris_avg = compute_monthly_avg(data['Paris'])
cairo_avg = compute_monthly_avg(data['Cairo'])

# ----------------------------
# Step 4: Prepare data for plotting
# ----------------------------

# Months in the correct calendar order
month_order = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
               "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

# Ensure months exist in the data and extract values in correct order
months = [m for m in month_order if m in paris_avg]

paris_values = [paris_avg[m] for m in months]
cairo_values = [cairo_avg[m] for m in months]

# ----------------------------
# Step 5: Plotting the data
# ----------------------------

plt.figure(figsize=(10,6))  # Set figure size

# Plot Paris data
plt.plot(months, paris_values, marker='o', label='Paris', color='blue')

# Plot Cairo data
plt.plot(months, cairo_values, marker='o', label='Cairo', color='Orange')

# ----------------------------
# Step 6: Customize the plot
# ----------------------------
plt.title("Monthly Average Temperatures (Based on Daily Data)")

plt.xlabel("Month")
plt.ylabel("Average Temperature (°C)")

plt.grid(True, linestyle='--',alpha=0.5)
plt.legend()
plt.tight_layout()

# ----------------------------
# Step 7: Compute deltas (absolute differences) per month
# ----------------------------
deltas = [abs(paris_avg[m] - cairo_avg[m]) for m in months]

# ----------------------------
# Step 8: Plot histogram (bar chart)
# ----------------------------
plt.figure(figsize=(10, 6))
plt.bar(months, deltas, color='purple', alpha=0.7)

# Add labels and title
plt.title("Absolute Temperature Difference (Paris vs Cairo)")
plt.xlabel("Month")
plt.ylabel("Temperature Delta (°C)")
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.tight_layout()


# ----------------------------
# Step 9: Display the plot
# ----------------------------
plt.show()
