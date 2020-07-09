import sys
import numpy as np

# Boolean Arrays (masks)

a = np.arange(4)
print(a)
print(a[[0, -1]])
print(a[[True, False, False, True]])
print(a >= 2)
print((a[a >= 2]))


print(a.mean())
print(a[a > a.mean()])

print(a[~(a > a.mean())])
print(a[(a == 0) | (a == 1)])
print(a[(a <= 2) & (a % 2 == 0)])

A = np.random.randint(100, size=(3, 3))
print(A)

print(A[np.array([
    [True, False, True],
    [False, True, False],
    [True, False, True]
])])
print(A > 30)
print(A[A > 30])

