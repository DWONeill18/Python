# Multiple DataFrames

import codecademylib
import pandas as pd

sales = pd.read_csv('sales.csv')
print(sales)
targets = pd.read_csv('targets.csv')
print(targets)

# Inner Merge - only include matching rows

sales_vs_targets = pd.merge(sales, targets)
print(sales_vs_targets)

crushing_it = sales_vs_targets[sales_vs_targets.revenue > sales_vs_targets.target]

# A second way to merge

men_women = pd.read_csv('men_women_sales.csv')

all_data = sales.merge(targets).merge(men_women)
print(all_data)

results = all_data[(all_data.revenue > all_data.target) & (all_data.women > all_data.men)]

# Merging on Specific Columns
# Making sure the colomn names are the same for .merge() to work

orders = pd.read_csv('orders.csv')
print(orders)
products = pd.read_csv('products.csv')
print(products)

orders_products = pd.merge(
  orders,
  products.rename(columns={'id': 'product_id'}))

print(orders_products)

# ANother way is to specify which columns to merge on

orders_products = pd.merge(orders, 
products, 
left_on='product_id', 
right_on='id', 
suffixes=['_orders', '_products'])

print(orders_products)

# If there is a mismatched merge then the row is dropped from the table

# Outer Merge - allows mismatched rows

store_a = pd.read_csv('store_a.csv')
print(store_a)
store_b = pd.read_csv('store_b.csv')
print(store_b)

store_a_b_outer = pd.merge(store_a, store_b, how='outer')

print(store_a_b_outer)

# Left Merge - includes all rows from the first (left) table, but only rows that match in the second table

store_a_b_left = pd.merge(store_a, store_b, how='left')
store_b_a_left = pd.merge(store_b, store_a, how='left')

print(store_a_b_left)
print(store_b_a_left)

# Concatenate DataFrames

bakery = pd.read_csv('bakery.csv')
print(bakery)
ice_cream = pd.read_csv('ice_cream.csv')
print(ice_cream)

menu = pd.concat([bakery, ice_cream])

print(menu)


