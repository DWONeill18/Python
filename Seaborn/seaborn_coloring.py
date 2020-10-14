# Seaborn coloring

import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

# Palettes

# Save a palette to a variable:
palette = sns.color_palette("bright")

# Use palplot and pass in the variable:
sns.palplot(palette)


# Set the palette using the name of a palette:
sns.set_palette("Paired")

# Plot a chart:
sns.stripplot(x="day", y="total_bill", data=tips)



# Seaborn allows for styling of matplotlib pltos as well

# Call the sns.set() function 
sns.set()
for col in 'xy':
  plt.hist(data[col], normed=True, alpha=0.5)

# Multiple palette to choose from (deep, muted, pastel, bright, dark and colorblind)

# Set the palette to the "pastel" default palette:
sns.set_palette("pastel")

# plot using the "pastel" palette
sns.stripplot(x="day", y="total_bill", data=tips)


# Color Brewer Palettes

custom_palette = sns.color_palette("Paired", 9)
sns.palplot(custom_palette)

# Qualitative Colors (good for distinct catagorical data)
qualitative_colors = sns.color_palette("Set3", 10)
sns.palplot(qualitative_colors)

# Sequential Palettes (for continuous values that can be put into groups)
sequential_colors = sns.color_palette("RdPu", 10)
sns.palplot(sequential_colors)

# Diverging Palettes (best for datasets that have interesting high and low values)
diverging_colors = sns.color_palette("RdBu", 10)
sns.palplot(diverging_colors)