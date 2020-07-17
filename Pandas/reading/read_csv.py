import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#matplotlib inline

# header=none tells pandas that the first line is n't a header
df = pd.read_csv(
    'data/btc-market-price.csv',
    header=None,
    names=['Timestamp', 'Price'],
    index_col=0,
    parse_dates=True
    )

print(df.head())

#plt.plot(df.index, df['Price'])
#plt.show()

# Plot example
"""
x = np.arange(-10, 11)
plt.figure(figsize=(12, 6))
plt.plot(x, x ** 2)
plt.plot(x, -1 * (x ** 2))
plt.title('My Nice Plot')
"""

#df.plot(figsize=(16, 9), title='Bitcoin Price 2017-2018')
#plt.show()

# Adding a second 

eth = pd.read_csv('data/eth-price.csv', parse_dates=True, index_col=0)

"""
print(eth.info())
print(eth.head())
"""

# Now combining both Dataframes into one

prices = pd.DataFrame(index=df.index)
#print(prices.head())
prices['Bitcoin'] = df['Price']
prices['Ether'] = eth['Value']
print(prices.head())

#prices.plot(figsize=(12, 6))


# there seems to be a gap in the data

prices.loc['2017-12-01':'2018-01-01'].plot(figsize=(12,6))

plt.show()