# Seaborn Styling

import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

# Built-In Themes
"""
5 built-in themes to style plots (darkgrid, whitegrid, dark, white, ticks)
"""

sns.set_style("darkgrid")
sns.stripplot(x="day", y="total_bill", data=df)

# Background Color

sns.set_style("dark")
sns.stripplot(x="day", y="total_bill", data=df)

"""
White and tick themes provide a higher contrast so the plots are more legible
"""

sns.set_style("ticks")
sns.stripplot(x="day", y="total_bill", data=tips)

# Grids

# With grid
sns.set_style("whitegrid")
sns.stripplot(x="day", y="total_bill", data=tips)

# Without grid
sns.set_style("white")
sns.stripplot(x="day", y="total_bill", data=tips)


# Despine

sns.set_style("white")
sns.stripplot(x="day", y="total_bill", data=tips)
sns.despine() # This needs to be called after you have called your plot

# Or you can choose which spines to remove
sns.set_style("whitegrid")
sns.stripplot(x="day", y="total_bill", data=tips)
sns.despine(left=True, bottom=True)

# Scaling Plots

"""
Within the usage of sns.set_context()
1) Pass one param: adjust the scale of the plot
2) Pass two: scale and font size
3) Pass three: scale, font and rc with the style param you want to override
"""

sns.set_style("ticks")

# Smallest context:
sns.set_context("paper") # size order: paper, notebook, talk, and poster. notebook is default
sns.stripplot(x="day", y="total_bill", data=tips)

# scaling fonts and line widths

# Set font scale and reduce grid line width to match
sns.set_context("poster", font_scale = .5, rc={"grid.linewidth": 0.6})
sns.stripplot(x="day", y="total_bill", data=tips)

# The RC parameter
"""
Can use the RC parameter to overide the default settings
"""

sns.set_style("ticks")
sns.set_context("poster")
sns.stripplot(x="day", y="total_bill", data=tips)
sns.plotting_context()