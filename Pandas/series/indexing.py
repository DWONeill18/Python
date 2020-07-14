import pandas as pd
import numpy as np

g7_pop = pd.Series({
    'Canada': 35.467,
    'France': 63.951,
    'Germany': 80.94,
    'Italy': 60.665,
    'Japan': 127.061,
    'United Kingdom': 64.511,
    'United States': 318.523
}, name='G7 Population in millions')

print(g7_pop)

print(g7_pop['Canada'])
print(g7_pop['Japan'])

# numeric positions can be used using the attribute iloc
print(g7_pop.iloc[0])
print(g7_pop.iloc[-1])

# multiple indexing at once
print(g7_pop[['Italy', 'France']])
print(g7_pop.iloc[[0, 1]])
# slicing in pandas, the upper limit is included!
print(g7_pop['Canada': 'Italy'])