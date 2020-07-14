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

print(g7_pop * 1_000_000)
print("/n")

print(g7_pop.mean())
print("/n")

print(np.log(g7_pop))
print("/n")

print(g7_pop['France': 'Italy'].mean())
print("/n")
