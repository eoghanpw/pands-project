# analysis.py
# Programming and Scripting Project.
# Analysis of Fisher's Iris data set.
# Author: Eoghan Walsh.

# Import python modules numpy, pandas, matplotlib.pyplot and os.path.
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os.path

# Import the Iris data set to a pandas DataFrame.
df = pd.read_csv("iris.csv")

# Show the data set.
print(df)

# Add column headers to the DataFrame.
# Adapted from:
# https://sparkbyexamples.com/pandas/pandas-add-header-row-to-dataframe/
column_names = ("sepal_length_cm", "sepal_width_cm", "petal_length_cm",
                "petal_width_cm", "class")

iris = pd.read_csv("iris.csv", names=column_names)

# Show the data set.
print(iris)

# Describe the data set.
print(iris.describe())

# Summarize variables into a text file.
FILENAME = "iris_variable_summary.txt"

summary = iris.describe()

summary_csv = summary.to_csv()


def variable_summary():
    with open(FILENAME, "w", newline="") as f:
        f.write(summary_csv)


variable_summary()
