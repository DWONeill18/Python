# Pandas Aggregates

# Calculating column Statistics

#df.column_name.command() , mean, std, median, max, min, count, nunique, unique

import codecademylib
import pandas as pd

orders = pd.read_csv('orders.csv')
print(orders.head(10))

most_expensive = orders.price.max()
num_colors = orders.shoe_color.nunique()

# Calculating Aggregate functions

pricey_shoes = orders.groupby('shoe_type').price.max()
print(pricey_shoes)
print(type(pricey_shoes)) # series

# pricey_shoes into a dataframe

pricey_shoes = orders.groupby('shoe_type').price.max().reset_index()
print(pricey_shoes)
print(type(pricey_shoes)) # dataframe

# Calculating Percentiles

cheap_shoes = orders.groupby('shoe_color').price.apply(lambda x: np.percentile(x, 25)).reset_index()
print(cheap_shoes)

# Grouping by more than one column

shoe_counts = orders.groupby(['shoe_type', 'shoe_color']).id.count().reset_index()
print(shoe_counts)

# Pivot tables

shoe_counts_pivot = shoe_counts.pivot(
  columns='shoe_color',
  index='shoe_type',
  values='id').reset_index()

print(shoe_counts_pivot)

