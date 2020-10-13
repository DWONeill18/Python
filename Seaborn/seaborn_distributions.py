# Seaborn distributions

# KDE Plots (Kernal Density Estimator)
"""
Alternative to histograms, gives us the sense of a univariate as a curve. 
A univariate dataset only has one variavble and is referred to as being one-dimensional.
Better than histograms as shape is not dependent on hte number and width of the bins.
"""

import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns

# Take in the data from the CSVs as NumPy arrays:
set_one = np.genfromtxt("dataset1.csv", delimiter=",")
set_two = np.genfromtxt("dataset2.csv", delimiter=",")
set_three = np.genfromtxt("dataset3.csv", delimiter=",")
set_four = np.genfromtxt("dataset4.csv", delimiter=",")

# Creating a Pandas DataFrame:
n=500
df = pd.DataFrame({
    "label": ["set_one"] * n + ["set_two"] * n + ["set_three"] * n + ["set_four"] * n,
    "value": np.concatenate([set_one, set_two, set_three, set_four])
})

# Setting styles:
sns.set_style("darkgrid")
sns.set_palette("pastel")

# Plotting the KDEs
sns.kdeplot(data=set_one, shade=True)
sns.kdeplot(data=set_two, shade=True)
sns.kdeplot(data=set_three, shade=True)
sns.kdeplot(data=set_four, shade=True)
plt.show()

# Box Plots
"""
Shows us the range of our dataset, gives us an idea about whether or not any outliers are present
"""

# Take in the data from the CSVs as NumPy arrays:
set_one = np.genfromtxt("dataset1.csv", delimiter=",")
set_two = np.genfromtxt("dataset2.csv", delimiter=",")
set_three = np.genfromtxt("dataset3.csv", delimiter=",")
set_four = np.genfromtxt("dataset4.csv", delimiter=",")

# Creating a Pandas DataFrame:
n=500
df = pd.DataFrame({
    "label": ["set_one"] * n + ["set_two"] * n + ["set_three"] * n + ["set_four"] * n,
    "value": np.concatenate([set_one, set_two, set_three, set_four])
})

# Setting styles:
sns.set_style("darkgrid")
sns.set_palette("pastel")

# Box plot code (can plot multiple box plots if all contaione in the dataframe)
sns.boxplot(data=df, x='label', y='value')
plt.show()


# Violin Plots
"""
Provides more information than box plots becuase instead of mapping each individual data point,
 we get an estimation of the dataset thanks to the KDE
"""

# Take in the data from the CSVs as NumPy arrays:
set_one = np.genfromtxt("dataset1.csv", delimiter=",")
set_two = np.genfromtxt("dataset2.csv", delimiter=",")
set_three = np.genfromtxt("dataset3.csv", delimiter=",")
set_four = np.genfromtxt("dataset4.csv", delimiter=",")

# Creating a Pandas DataFrame:
n=500
df = pd.DataFrame({
    "label": ["set_one"] * n + ["set_two"] * n + ["set_three"] * n + ["set_four"] * n,
    "value": np.concatenate([set_one, set_two, set_three, set_four])
})

# Setting styles:
sns.set_style("darkgrid")
sns.set_palette("pastel")

# Violin code for multiple violins
sns.violinplot(data=df, x='label', y='value')
plt.show()
