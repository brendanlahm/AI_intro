 # Exercise4

import numpy as np

# Create a vector
v = np.array([1,2,3,4])

# Determine # x + y values
w = v.shape

# Create a matrix
m = np.array([[1,2], [3,4]])
m

# Print specific value of matrix (row, column)
print(m[0,1])

# Print datatype of the matrix (int64)
print(m.dtype)

# Generate a vector based on a range
m_gen = np.arange(0,13,3)
m_gen

# sin calculations on a bunch of values
for x in np.linspace(0, 2*np.pi, 1000):
    np.sin(x)







