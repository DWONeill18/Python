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

df.append(pd.Series({
    'Population': 3,
    'GDP': 5
}, name='China'))

df.loc['China'] = pd.Series({'Population': 1_400_000_000, 'Continent': 'Asia'})
print(df)

######
#statistical methods

print(df.head())
print(df.describe())
population = df['Population']

print(population.min(), population.max())
print(population.sum())
print(population.sum() / len(population))
print(population.mean())
print(population.std())
print(population.median())
print(population.describe())
print(population.quantile(.25))
print(population.quantile([.2, .4, .6, .8, 1]))