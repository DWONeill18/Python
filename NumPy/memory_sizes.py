import sys
import numpy as np

# Size of Objects in Memory
###########################

# Ints and Floats
##################

# An integer in Python is > 24bytes
print(sys.getsizeof(1))

# Longs are even larger
print(sys.getsizeof(10**100))

# Numpy size is much smaller
print(np.dtype(int).itemsize)
print(np.dtype(float).itemsize)

# List are even larger
########################

# A one element list
print(sys.getsizeof([1]))
print(np.array([1]).nbytes)
