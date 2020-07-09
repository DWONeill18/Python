import sys
import numpy as np

# Linear Algebra

A = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

B = np.array([
    [6, 5],
    [4, 3],
    [2, 1]
])

# dot product
print(A.dot(B))
# cross product
print(A @ B)
# transpose matrix
print(B.T)

print(A)
print(B.T @ A)