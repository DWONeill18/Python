# Seaborn Introduction

"""
Python visuaization library that provides simple code to create elegant visualizations for statistical exploration and insight
"""

import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns


df = pd.read_csv('survey.csv')
print(df.head())

#################################
# Simple bar chart
#################################

# Load results.csv here:
df = pd.read_csv("results.csv")
print(df)

# plot bar chart using seaborn
sns.barplot(
	data=df ,
	x="Gender" ,
	y="Mean Satisfaction"
)

plt.show()

###################################
# Aggregate Statistics
###################################

import numpy as np

gradebook = pd.read_csv("gradebook.csv")

print(gradebook)

assignment1 = gradebook[gradebook.assignment_name == "Assignment 1"]

print(assignment1)

asn1_median = np.median(assignment1.grade)
print(asn1_median)

######################################
#Plotting Aggregates
######################################

gradebook = pd.read_csv("gradebook.csv")

# Automatically calculates the average
sns.barplot(
  data=gradebook,
  x="assignment_name",
  y="grade"
)

plt.show()

#######################
# Modifying Error bars
######################

"""
Automatic error bars are bootstrapped confidence interval (95%)
We can change it to standard deviation by passing the keyword argument ci="sd"
"""

gradebook = pd.read_csv("gradebook.csv")

sns.barplot(data=gradebook, x="name", y="grade", ci="sd")
plt.show()

############################
# Calcualting Different Aggregates
#############################
"""
Using the estimator keyword argument
"""

df = pd.read_csv("survey.csv")

print(df)

sns.barplot(
  data=df,
  x="Gender",
  y="Response",
  estimator=np.median
)

plt.show()

##############################
# Aggregating Multiple Columns
##############################

# The hue adds a nested categorical variable 

df = pd.read_csv("survey.csv")

sns.barplot(
  data=df,
  x="Age Range",
  y="Response",
  hue="Gender"
)

plt.show()

