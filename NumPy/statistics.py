import sys
import numpy as np

# Statistics

a = np.array([1, 2, 3, 4])

print(a.sum())
print(a.mean())
print(a.std())
print(a.var())

A = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

print(A.sum())
print(A.mean())
print(A.std())

# Columns
print(A.sum(axis=0))
print(A.mean(axis=0))
print(A.std(axis=0))

# Rows
print(A.sum(axis=1))
print(A.mean(axis=1))
print(A.std(axis=1))