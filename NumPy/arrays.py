import sys
import numpy as np

# Basic NumPy Arrays

a = np.array([1, 2, 3, 4])
b = np.array([0, .5, 1, 1.5, 2])

"""
print(a[0])
print(a[0:])
print(a[1:3])
print(a[1:-1])
print(a[::2])
print(b[0], b[2], b[-1])
"""

#multi indexing only with numpy - result is a numpy array
"""
print(b[[0, 2, -1]])
"""

# Array Types

"""
print(a)
print(b)

print(a.dtype)
print(b.dtype)

print(np.array([1, 2, 3, 4], dtype=np.float))
print(np.array([1, 2, 3, 4], dtype=np.int8))

c = np.array(['a', 'b', 'c', 'd'])
print(c.dtype)

d = np.array([{'a': 1}, sys])
print(d.dtype)
"""

