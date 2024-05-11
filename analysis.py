# analysis.py
# Programming and Scripting Project.
# Analysis of Fisher's Iris data set.
# Author: Eoghan Walsh.

# Import python modules numpy, pandas, matplotlib.pyplot and os.path.
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os.path

# Import the Iris data set to a pandas DataFrame and
# add column headers.
# Adapted from:
# https://sparkbyexamples.com/pandas/pandas-add-header-row-to-dataframe/.
column_names = ("sepal_length_cm", "sepal_width_cm", "petal_length_cm",
                "petal_width_cm", "class")

iris = pd.read_csv("iris.csv", names=column_names)

# Show the data set.
print(iris)

# 1. OUTPUT A SUMMARY OF EACH VARIABLE TO A SINGLE TEXT FILE.

# Create the filename.
FILENAME = "iris_variable_summary.txt"

# Generate descriptive statistics for each variable.
# Ref: https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.describe.html.
summary = iris.describe()

# Convert pandas DataFrame to string so it can
# be written to a text file.
# Ref: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_csv.html.
summary_csv = summary.to_csv()


# Function to write the summary stats to a text file.
def variable_summary():
    with open(FILENAME, "w", newline="") as f:
        f.write(summary_csv)


# Run the function.
variable_summary()

# 2. SAVE A HISTOGRAM OF EACH VARIABLE TO PNG FILES.

# Get the sepal lengths per class and convert to numpy array.
sepal_length_setosa = iris[iris["class"] == "Iris-setosa"]["sepal_length_cm"].to_numpy()
sepal_length_versicolor = iris[iris["class"] == "Iris-versicolor"]["sepal_length_cm"].to_numpy()
sepal_length_virginica = iris[iris["class"] == "Iris-virginica"]["sepal_length_cm"].to_numpy()

# Use matplotlib subplots to create the histogram.
fig, ax = plt.subplots()

# Select the plot type, legend label, bar colour, transparency, number of bins.
ax.hist(sepal_length_setosa, label="Setosa", color="tab:green", edgecolor=None,
        alpha=0.5, bins=None)

ax.hist(sepal_length_versicolor, label="Versicolor", color="tab:orange", edgecolor=None,
        alpha=0.5, bins=None)

ax.hist(sepal_length_virginica, label="Virginica", color="tab:blue", edgecolor=None,
        alpha=0.5, bins=None)

# Set the axis labels, axis limits, title.
ax.set_xlabel("sepal length (in centimetres)")
ax.set_ylabel("frequency")
ax.set_title("Iris Sepal Lengths")

# Add legend.
ax.legend()

# Show the histogram.
#plt.show()

# Save the histogram.
plt.savefig("sepal_length_hist.png")
