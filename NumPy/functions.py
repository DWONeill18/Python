import sys
import numpy as np

# random

# numpy array with 2 random floats
a = np.random.random(size=2)
print(a)
print("\n")

# numpy array with 
b = np.random.normal(size=2)
print(b)
print("\n")

# 2 * 4  numpy array of random floats
c = np.random.rand(2, 4)
print(c)
print("\n")

# create a numpy array, filled with 3 random integer values between 1 and 10
d = np.random.randint(10, size=3)
print(d)
print("\n")

# create a 3*3*3 numpy matrix filled with random float values
e = np.random.rand(3,3,3)
print(e)
print("\n")