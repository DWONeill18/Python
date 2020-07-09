import sys
import numpy as np

# Matrices (Indexing and slicing)

# Square matrix
A = np.array([
  #. 0. 1. 2.     
    [1, 2, 3], #0
    [4, 5, 6], #1
    [7, 8, 9]  #2
])

"""
print(A[1])
print(A[1] [0])
"""

# A[d1, d2, d3, dn]
"""
print(A[1, 0])
print(A[0:2])
"""

#All rows, first two columns
"""
print(A[:, :2])
print(A[:2, 2:])
print(A)
"""

# Reassignment

A[1] = np.array([10, 10, 10])
print(A)

# Assign the whole row
A[2] = 99
print(A)