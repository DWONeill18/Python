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

print(df)
####################################################################################
# Individual columns in the DataFrame can be selected with regular indexing. Each column is represeneted as a series
####################################################################################


print(df.loc['Canada'])
print("\n")
print(df.iloc[-1])
print("\n")
print(df['Population'])
print("\n")

# for a dataframe-like format
print(df['Population'].to_frame())
print("\n")


# multiple columns
print(df[['Population', 'GDP']])
print("\n")

# slicing at row level
print(df[1:3])
print("\n")

# select rows using loc
print(df.loc['Italy'])
print("\n")

print(df.loc['France': 'Italy'])
print("\n")
print(df.loc['France': 'Italy', 'Population'])
print("\n")
print(df.loc['France': 'Italy', ['Population', 'GDP']])
print("\n")

# numeric position of the index
print(df.iloc[0])
print("\n")

print(df.iloc[-1])
print("\n")

print(df.iloc[[0, 1, -1]])
print("\n")

print(df.iloc[1:3])
print("\n")

print(df.iloc[1:3, 3])
print("\n")

print(df.iloc[1:3, [0, 3]])
print("\n")

print(df.iloc[1:3, 1:3])
print("\n")
