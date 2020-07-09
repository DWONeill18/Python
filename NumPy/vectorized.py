import sys
import numpy as np

# Broadcasting and Vectorized operations

# creating and returning a new array
a = np.arange(4)
print(a)
print(a + 10)
print(a * 10)

a += 100
print(a)

l = [0, 1, 2, 3]
print([i * 10 for i in l])

a = np.arange(4)
b = np.array([10, 10, 10, 10])
print(a + b)
print(a * b)