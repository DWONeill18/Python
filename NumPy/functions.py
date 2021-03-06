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

# arange

# f: array of 0 to 9    g: array of 5 to 9  h: array of 0 to 1 with a increment of 0.1
f = np.arange(10)
g = np.arange(5, 10)
h = np.arange(0, 1, .1)

print(f)
print(g)
print(h)

# reshape

# reshape array of 0 to 9 to a 2*5 or 5*2
i = np.arange(10).reshape(2, 5)
j = np.arange(10).reshape(5, 2)
print(i)
print(j)

# linspace

# create aray of values that split between x and y into z values
k = np.linspace(0, 1, 5)
l = np.linspace(0, 1, 20)
m = np.linspace(0, 1, 20, False)

print(k)
print(l)
print(m)
print("\n")

# zeros, ones, empty

# array of 5 zeros(floats)
print(np.zeros(5))
print("\n")

# 3*3 array of zeros(floats)
print(np.zeros((3, 3)))
print("\n")

# 3*3 array of zeros(ints)
print(np.zeros((3, 3), dtype=np.int))
print("\n")

# array of 5 ones(floats)
print(np.ones(5))
print("\n")

# 3*3 array of ones(floats)
print(np.ones((3, 3)))
print("\n")

# the empty function is used to create a new array of given shape and type, without intializing entries
print(np.empty(5))
print("\n")

print(np.empty(3))
print("\n")

print(np.empty((2, 2)))
print("\n")

# Identity and eye

# identity matrix
print(np.identity(3))

# diagonal matrix, can choose size
print(np.eye(3,3))
print(np.eye(4,4))
print(np.eye(4,4, k=1))
print(np.eye(4,4, k=-1))

