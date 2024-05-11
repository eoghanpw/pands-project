# analysis.py
# Programming and Scripting Project.
# Analysis of Fisher's Iris data set.
# Author: Eoghan Walsh.


# Import python modules pandas, matplotlib.pyplot and numpy.
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Import the Iris data set to a pandas DataFrame and add column headers.
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

# Generate summary statistics for each variable.
# Reference:
# https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.describe.html.
summary = iris.describe()

# Convert to string so it can be written to a text file.
# Reference:
# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_csv.html.
summary_csv = summary.to_csv()


# Function to write the summary stats to a text file.
def variable_summary():
    with open(FILENAME, "w", newline="") as f:
        f.write(summary_csv)


# Run the function.
variable_summary()


# 2. SAVE A HISTOGRAM OF EACH VARIABLE TO PNG FILES.

# List of variables for the histograms.
columns_hist = ("sepal_length_cm", "sepal_width_cm", "petal_length_cm",
                "petal_width_cm")

# List of x axis labels for each histogram.
xlabel_hist = ("sepal length (in centimetres)", "sepal width (in centimetres)",
               "petal length (in centimetres)", "petal width (in centimetres)")

# List of titles for each histogram.
title_hist = ("Iris Sepal Lengths", "Iris Sepal Widths", "Iris Petal Lengths",
              "Iris Petal Widths")

# Subsets of the data set by class.
setosa_hist = iris["class"] == "Iris-setosa"
versicolor_hist = iris["class"] == "Iris-versicolor"
virginica_hist = iris["class"] == "Iris-virginica"

# For loop with zip function to create histogram for each variable.
# Reference:
# https://realpython.com/python-zip-function/#looping-over-multiple-iterables.
for col, xlabel, title in zip(columns_hist, xlabel_hist, title_hist):

    # Use matplotlib subplots to create the histogram.
    fig, ax = plt.subplots()

    # Select plot type, data, label, bar colour, transparency, number of bins.
    ax.hist(iris[setosa_hist][col], label="Setosa", color="tab:green",
            alpha=0.5, bins=None)

    ax.hist(iris[versicolor_hist][col], label="Versicolor", color="tab:orange",
            alpha=0.5, bins=None)

    ax.hist(iris[virginica_hist][col], label="Virginica", color="tab:blue",
            alpha=0.5, bins=None)

    # Set the axis labels, title, legend.
    ax.set_xlabel(xlabel)
    ax.set_ylabel("frequency")
    ax.set_title(title)
    ax.legend()

    # Save each histogram as png file.
    plt.savefig(f"{col}_hist.png")
