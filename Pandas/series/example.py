import pandas as pd
import numpy as np

# In millions
g7_pop = pd.Series([35.467, 63.951, 80.940, 60.665, 127.061, 64.511, 318.523])
print(g7_pop)

# change the name to give better description
g7_pop.name = 'G7 Population in millions'
print(g7_pop)

# similar to numpy arrays
print(g7_pop.dtype)
print(g7_pop.values)
print(type(g7_pop.values))

# index system similar to python lists (even though they look like dicts)
print(g7_pop[0])
print(g7_pop[1])
print(g7_pop.index)

# In contrast to lists we can define the index
g7_pop.index = [
    'Canada',
    'France',
    'Germany',
    'Italy',
    'Japan',
    'United Kingdom',
    'United States',
]
print(g7_pop)

# Series look like 'ordered dictionaries' and can create a series from a dictionary
series1 = pd.Series({
    'Canada': 35.467,
    'France': 63.951,
    'Germany': 80.94,
    'Italy': 60.665,
    'Japan': 127.061,
    'United Kingdom': 64.511,
    'United States': 318.523
}, name='G7 Population in millions')

# OR
series2 = pd.Series(
    [35.467, 63.951, 80.94, 60.665, 127.061, 64.511, 318.523],
    index=['Canada', 'France', 'Germany', 'Italy', 'Japan', 'United Kingdom',
       'United States'],
    name='G7 Population in millions')
