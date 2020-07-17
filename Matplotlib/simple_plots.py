import matplotlib.pyplot as plt
import numpy as np

# Easy plot
plt.plot([1, 2, 3, 4])
plt.ylabel('some numbers')
plt.show()

# Formatting
plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'ro')
plt.axes([0, 6, 0, 20])
plt.show()

# Multiple lines

# evenly samlped time at 200ms intervals
t = np.arange(0., 5., 0.2)

# red dashes, blue squares and green triangles
plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
plt.show()