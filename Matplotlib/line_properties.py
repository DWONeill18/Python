import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Controlling line properties

#plt.plot(x, y, linewidth=2.0)   

#lines = plt.plot(1, 1, 5, 4)
# use keyword args
#plt.setp(lines, color='r', linewidth=2.0)
# or MATLAB style string value pairs
#plt.setp(lines, 'color', 'r', 'linewidth', 2.0)

#Example
line, = plt.plot(4, 7, 6, 7, '-')
line.set_antialiased(False) # turn off antialiasing
plt.show()