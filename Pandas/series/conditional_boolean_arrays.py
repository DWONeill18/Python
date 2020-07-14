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
print("\n")

# which g7 countries with population over 70m
print(g7_pop > 70)
print("\n")

# print out with g7 countries have a population of over 70m
print(g7_pop[g7_pop > 70])
print("\n")

# mean of the pops
print(g7_pop.mean())
print("\n")

# contries greater than mean pop
print(g7_pop[g7_pop > g7_pop.mean()])
print("\n")

# std of g7 pop
print(g7_pop.std())
print("\n")

# complex conditionals
print(g7_pop[(g7_pop > g7_pop.mean() - g7_pop.std() / 2) | (g7_pop > g7_pop.mean() + g7_pop.std() / 2)])
print("\n")


# Boolean Arrays
################

# OR example
print(g7_pop[(g7_pop > 80) | (g7_pop < 40)])

# AND example
print(g7_pop[(g7_pop > 80) & (g7_pop < 200)])