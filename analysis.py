# analysis.py
# Programming and Scripting Project.
# Analysis of Fisher's Iris data set.
# Author: Eoghan Walsh.


# Import python modules pandas, matplotlib.pyplot, seaborn and numpy.
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


# Import the Iris data set to a pandas DataFrame and add column headers.
# Adapted from:
# https://sparkbyexamples.com/pandas/pandas-add-header-row-to-dataframe/.
column_names = ("sepal_length_cm", "sepal_width_cm", "petal_length_cm",
                "petal_width_cm", "class")

iris = pd.read_csv("iris.csv", names=column_names)


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
variables_hist = ("sepal_length_cm", "sepal_width_cm", "petal_length_cm",
                  "petal_width_cm")

# Subsets of the data set by class.
setosa_hist = iris["class"] == "Iris-setosa"
versicolor_hist = iris["class"] == "Iris-versicolor"
virginica_hist = iris["class"] == "Iris-virginica"

# For loop to create histogram for each variable.
for var in variables_hist:

    # Use matplotlib subplots to create the histogram.
    fig, ax = plt.subplots()

    # Select plot type, data, label, bar colour, transparency.
    ax.hist(iris[setosa_hist][var], label="Setosa", color="tab:green",
            alpha=0.5)

    ax.hist(iris[versicolor_hist][var], label="Versicolor", color="tab:orange",
            alpha=0.5)

    ax.hist(iris[virginica_hist][var], label="Virginica", color="tab:blue",
            alpha=0.5)

    # Set the axis labels..
    xlabel = var.replace("_", " ").replace("cm", "(in centimetres)")

    ax.set_xlabel(xlabel)
    ax.set_ylabel("frequency")

    # Set the title.
    title_hist = var.replace("_", " ").replace(" cm", "s").title()
    ax.set_title(f"Iris {title_hist} per Class")

    # Add legend.
    ax.legend()

    # Save each histogram as png file.
    plt.savefig(f"{var}_hist.png")

    # Close each figure.
    plt.close()


# 3. OUTPUT A SCATTER PLOT OF EACH PAIR OF VARIABLES.

# seaborn pairplot.

# Dictionary of colours for the pairplots.
colours = {"Iris-setosa": "tab:green", "Iris-versicolor": "tab:orange",
           "Iris-virginica": "tab:blue"}

# Use seaborn pairplot to generate one figure containing all scatter plots
# for each pair of variables.
# Adapted from:
# https://seaborn.pydata.org/generated/seaborn.pairplot.html#seaborn-pairplot.
# https://stackoverflow.com/a/47200170
sns.pairplot(iris, hue="class", palette=colours, plot_kws={"alpha": 0.5})

# Show plot.
plt.show()

# matplotlib.pyplot plot.

# List of variables for the plots.
variables_plot = ("sepal_length_cm", "sepal_width_cm", "petal_length_cm",
                  "petal_width_cm")

# Subsets of the data set by class.
setosa_plot = iris["class"] == "Iris-setosa"
versicolor_plot = iris["class"] == "Iris-versicolor"
virginica_plot = iris["class"] == "Iris-virginica"

# Nested for loop to run through each pair of variables with
# continue statement to skip when x equals y. Will generate separate
# figure for each scatter plot.
# Reference: https://www.w3schools.com/python/python_for_loops.asp
for x in variables_plot:
    for y in variables_plot:
        if x == y:
            continue

        # Use matplotlib subplots to create the histogram.
        fig, ax = plt.subplots()

        # Select plot type, x & y data, marker shape, label, colour.
        ax.plot(iris[setosa_plot][x], iris[setosa_plot][y], "o",
                label="Setosa", color="tab:green", alpha=0.5)

        ax.plot(iris[versicolor_plot][x], iris[versicolor_plot][y], "o",
                label="Versicolor", color="tab:orange", alpha=0.5)

        ax.plot(iris[virginica_plot][x], iris[virginica_plot][y], "o",
                label="Virginica", color="tab:blue", alpha=0.5)

        # Set the axis labels.
        ax.set_xlabel(x)
        ax.set_ylabel(y)

        # Set the title.
        xtitle = x.replace("_", " ").replace(" cm", "").title()
        ytitle = y.replace("_", " ").replace(" cm", "").title()

        ax.set_title(f"{xtitle} vs {ytitle} per Class")

        # Add legend.
        ax.legend()

        # Show scatter plots.
        plt.show()


# 4. FURTHER ANALYSIS

# Plot Petal Length against Petal Width.

# Get petal lengths and petal widths from data set.
petal_l = iris["petal_length_cm"]
petal_w = iris["petal_width_cm"]

# Get the coefficents for regression lines with numpy.
# Adapted from:
# https://www.datacamp.com/tutorial/line-plots-in-matplotlib-with-python#adding-a-matplotlib-regression-line-aregr
petal_coefficients = np.polyfit(petal_l, petal_w, 1)
p_petal = np.poly1d(petal_coefficients)

# Get the correlation coefficient with numpy.
petal_corr = np.corrcoef(petal_l, petal_w)

# Create plot with matplotlib subplots.
fig, ax = plt.subplots()

# Select plot type, x & y data, marker shape, colour.
ax.plot(petal_l, petal_w, "o", color="tab:purple", alpha=0.5)

# Add regression line to plot.
ax.plot(petal_l, p_petal(petal_l), "-", color="tab:red",
        label="Regression Line")

# Set axis labels, title and legend.
ax.set_xlabel("petal length (in centimetres)")
ax.set_ylabel("petal width (in centimetres)")
ax.set_title("Iris Petal Length vs Petal Width")
ax.legend(loc="upper left")

# Add correlation coefficient to plot.
# Reference:
# https://matplotlib.org/stable/gallery/text_labels_and_annotations/text_fontdict.html
ax.text(1, 2, f"Correlation Coefficient: {petal_corr[0,1:]}")

# Show plot.
plt.show()

# Plot Petal Length against Petal Width per Class.

# Get petal lengths and petal widths per class from data set.
setosa_petal_l = iris[iris["class"] == "Iris-setosa"]["petal_length_cm"]
setosa_petal_w = iris[iris["class"] == "Iris-setosa"]["petal_width_cm"]

versicolor_petal_l = iris[
    iris["class"] == "Iris-versicolor"]["petal_length_cm"]
versicolor_petal_w = iris[iris["class"] == "Iris-versicolor"]["petal_width_cm"]

virginica_petal_l = iris[iris["class"] == "Iris-virginica"]["petal_length_cm"]
virginica_petal_w = iris[iris["class"] == "Iris-virginica"]["petal_width_cm"]

# Get the coefficents for regression lines with numpy.
setosa_coefficients = np.polyfit(setosa_petal_l, setosa_petal_w, 1)
p_setosa = np.poly1d(setosa_coefficients)

versicolor_coefficients = np.polyfit(versicolor_petal_l, versicolor_petal_w, 1)
p_versicolor = np.poly1d(versicolor_coefficients)

virginica_coefficients = np.polyfit(virginica_petal_l, virginica_petal_w, 1)
p_virginica = np.poly1d(virginica_coefficients)

# Get the correlation coefficient with numpy.
setosa_corr = np.corrcoef(setosa_petal_l, setosa_petal_w)
versicolor_corr = np.corrcoef(versicolor_petal_l, versicolor_petal_w)
virginica_corr = np.corrcoef(virginica_petal_l, virginica_petal_w)

# Create figure with matplotlib subplots.
fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(12, 6), sharex=True,
                                    sharey=True)

# Plot setosa petal length vs petal width.
ax1.plot(setosa_petal_l, setosa_petal_w, "o", color="tab:green", alpha=0.5)

# Add regression line.
ax1.plot(setosa_petal_l, p_setosa(setosa_petal_l), "-", color="tab:red",
         label="Regression Line")

# Plot versicolor petal length vs petal width.
ax2.plot(versicolor_petal_l, versicolor_petal_w, "o", color="tab:orange",
         alpha=0.5)

# Add regression line.
ax2.plot(versicolor_petal_l, p_versicolor(versicolor_petal_l), "-",
         color="tab:red", label="Regression Line")

# Plot virginica petal length vs petal width.
ax3.plot(virginica_petal_l, virginica_petal_w, "o", color="tab:blue",
         alpha=0.5)

# Add regression line.
ax3.plot(virginica_petal_l, p_virginica(virginica_petal_l), "-",
         color="tab:red", label="Regression Line")

# Set axis labels, legend, title, text.
ax1.set_ylabel('petal width (in centimetres)')
ax1.legend(loc="upper left")
ax1.set_title("Setosa")
ax1.text(3, 0.5, f"Correlation Coefficient:\n{setosa_corr[0,1:]}")

ax2.set_xlabel('petal length (in centimetres)')
ax2.legend(loc="upper left")
ax2.set_title("Versicolor")
ax2.text(3, 0.5, f"Correlation Coefficient:\n{versicolor_corr[0,1:]}")

ax3.legend(loc="upper left")
ax3.set_title("Virginica")
ax3.text(3, 0.5, f"Correlation Coefficient:\n{virginica_corr[0,1:]}")

fig.suptitle('Petal Length vs Petal Width per Class')

# Show plot.
plt.show()
