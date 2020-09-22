# Pandas Examples II

import codecademylib
import pandas as pd

df = pd.DataFrame([
  [1, '3 inch screw', 0.5, 0.75],
  [2, '2 inch nail', 0.10, 0.25],
  [3, 'hammer', 3.00, 5.50],
  [4, 'screwdriver', 2.50, 3.00]
],
  columns=['Product ID', 'Description', 'Cost to Manufacture', 'Price']
)

# Adding a Column

df['Sold in Bulk?'] = ['Yes', 'Yes', 'No', 'No']
print(df)

df['Is taxed?'] = 'Yes'
print(df)

df['Margin'] = df['Price'] - df['Cost to Manufacture']
print(df)

# Performing Column Operations

import codecademylib
from string import lower
import pandas as pd

df = pd.DataFrame([
  ['JOHN SMITH', 'john.smith@gmail.com'],
  ['Jane Doe', 'jdoe@yahoo.com'],
  ['joe schmo', 'joeschmo@hotmail.com']
],
columns=['Name', 'Email'])

# Add columns here
df['Lowercase Name'] = df.Name.apply(lower)
print(df)

# Apply a Lambda to a column

df = pd.read_csv('employees.csv')

get_last_name = lambda x: x.split()[-1]
df['last_name'] = df.name.apply(get_last_name)

print(df)

# Applying a Lambda to a Row

total_earned = lambda row:  ((row.hours_worked - 40) * row.hourly_wage * 1.5) + (40 * hourly_wage) if row.hours_worked > 40 else row.hours_worked * hourly_wage

df['total_earned'] = df.apply(total_earned, axis = 1)
print(df)

# Renaming columns

df = pd.read_csv('imdb.csv')

# Rename columns here
df.columns = ['ID', 'Title', 'Category', 'Year Released', 'Rating']
print(df)

df = pd.read_csv('imdb.csv')

# Rename columns here
df.rename(columns={'name': 'movie_title'}, inplace=True)
print(df)