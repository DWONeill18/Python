import pandas as pd
import numpy as np

df = pd.DataFrame({
    'Population': [35.467, 63.951, 80.94 , 60.665, 127.061, 64.511, 318.523],
    'GDP': [
        1785387,
        2833687,
        3874437,
        2167744,
        4602367,
        2950039,
        17348075
    ],
    'Surface Area': [
        9984670,
        640679,
        357114,
        301336,
        377930,
        242495,
        9525067
    ],
    'HDI': [
        0.913,
        0.888,
        0.916,
        0.873,
        0.891,
        0.907,
        0.915
    ],
    'Continent': [
        'America',
        'Europe',
        'Europe',
        'Europe',
        'Asia',
        'Europe',
        'America'
    ]
}, columns=['Population', 'GDP', 'Surface Area', 'HDI', 'Continent'])

df.index = [
    'Canada',
    'France',
    'Germany',
    'Italy',
    'Japan',
    'United Kingdom',
    'United States',
]

# Modifying DataFrames

#print(df)

# Adding a new column
langs = pd.Series(
    ['French', 'German', 'Italian'],
    index=['France', 'Germany', 'Italy'],
    name='Language'
)

print(langs)
print("\n")

# Add the column Language with the values language
df['Language'] = langs
print(df)
print("\n")

# Replacing Values per column
df['Language'] = 'English'
print(df)
print("\n")

# Renaming columns
# renamed columns  that do not yet exist in df don't affect the viewing
print(df.rename(
    columns={
        'HDI': 'Human Development Index',
        'Anual Popcorn Consumption': 'APC',
    }, index={
        'United States': 'USA',
        'United Kingdom': 'UK',
        'Argentina': 'AR'
    }))

print("\n")

# Make all indices uppercase
print(df.rename(index=str.upper))
print("\n")

# Make all indices lowercase
print(df.rename(index=lambda x: x.lower()))

# Dropping columns
print(df.drop(columns='Language', inplace=True))
print("\n")

# Adding Values
# this olny gives a new DataFrame
print(df.append(pd.Series({
    'Population': 3,
    'GDP': 5
}, name='China')))

# Directly set a new index and values to the DataFrame
df.loc['China'] = pd.Series({'Population': 1_400_000_000, 'Continent': 'Asia'})
print(df)

# can remove a row by index using drop, affects original dataframe
#df.drop('China', inplace=True)
print(df)

# radical index changes
df.reset_index()
df.set_index('Population')

# creating columns from other columns
df['GDP Per Capita'] = df['GDP'] / df['Population']
print(df)