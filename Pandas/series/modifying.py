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

# Modifying Series

# set the value of Canada
g7_pop['Canada'] = 40.5

# set value by index
g7_pop.iloc[-1] = 500

# set value via a condtional
g7_pop[g7_pop < 70]
g7_pop[g7_pop < 70] = 99.99

print(g7_pop)