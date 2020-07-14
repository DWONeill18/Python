import pandas as pd
import numpy as np

# DataFrame of g7 countries

# creating a dataframe
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

print(df)

# reassigning the index
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

# column headings
print(df.columns)

# index headings
print(df.index)

# information of the data types and amount of Non-null entries
print(df.info())

# total number of entries in dataframe
print(df.size)

# rows x columns
print(df.shape)

# quick statistical summary
print(df.describe())

# data types for each column in dataframe
print(df.dtypes)

# count the number of each data type
print(df.dtypes.value_counts())