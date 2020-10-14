
from matplotlib import pyplot as plt
import pandas as pd
import seaborn as sns
# Visualise

# Load data into a dataframe
df = pd.read_csv("WorldCupMatches.csv")
print(df.head())

# Create new column of Total Goals
df['Total Goals'] = df['Home Team Goals'] + df['Away Team Goals']
print(df.head())

sns.set_style("whitegrid")
sns.set_context("poster")

f, ax = plt.subplots(figsize=(12, 7))
ax = sns.barplot(
  data=df,
  x="Year",
  y="Total Goals"
)
ax.set_title("A Comparison of Total Goals scored in World Cups")

plt.show()