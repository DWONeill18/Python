import sys
import numpy as np

# -Dimensions and Shapes

A = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

# shape of 2 rows, 3 columns
#2 dimensiosns
# total number of elements
print(A.shape)
print(A.ndim)
print(A.size)


B = np.array([
    [
        [12, 11, 10],
        [9, 8 ,7],
    ],
    [
        [6, 5, 4],
        [3, 2, 1]
    ]
])

print(B.shape)
print(B.ndim)
print(B.size)