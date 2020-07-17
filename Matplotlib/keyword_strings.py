import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Plotting with keyword strings
# Data in a format that lets you access particular variables with strings such as a DataFrame

data = {'a': np.arange(50),
        'c': np.random.randint(0, 50, 50),
        'd': np.random.randn(50)}

data['b'] = data['a'] + 10 * np.random.randn(50)
data['d'] = np.abs(data['d']) * 100

# scatter(x, y, color, size)
plt.scatter('a', 'b', c='c', s='d', data=data)
plt.xlabel('entry a')
plt.ylabel('entry b')
plt.show()