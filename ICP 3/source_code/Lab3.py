import numpy as np

# Create random array with floats between 1 and 20
x = np.random.uniform(low= 1.0, high=20.0, size=(20,))
# reshape into a 4X5 2D array
x = np.reshape(x, (4,5))
# Print for demo
print(x)
# Create a True/False 2d array by sorting a copy of x and seeing if each num
# in x is smaller than the max/ far right num in the sorted array
j = (x < np.sort(x,axis=1)[:,[4]])
# Print for demo
print(j)
# Multiple them to change the largest value to 0
x = x * j
# Print for demo
print(x)


