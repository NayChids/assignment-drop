#Create a NumPy array of shape (5,5) filled with random integers between 1-100
import numpy as pie
array_shape = pie.random.randint(1, 100, size=(5, 5))
print(array_shape)

# Indexing and Slicing
print("Slicing for row 0, col 0:", array_shape[0, 0])
print("Slicing for row 2, col 3:", array_shape[2, 3])
print("Slicing for first row:", array_shape[0, :])
print("Slicing for last column:", array_shape[:, -1])
print("Sub-matrix:", array_shape[0:3, 0:4])

# Boolean indexing to filter values greater than 50.
mask = array_shape > 50
print(mask)
print(array_shape[mask])

# Transpose the array 
print(array_shape.T)

# Use universal functions to compute square root, mean, and standard deviation of the array
print(f"Square root of Array: {pie.sqrt(array_shape)}")
print(f"Mean of Array: {pie.mean(array_shape)}")
print(f"Standard of Deviation of Array: {pie.std(array_shape)}")
