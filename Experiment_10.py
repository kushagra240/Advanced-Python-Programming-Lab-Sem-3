import numpy as np

# Create a one-dimensional NumPy array containing numbers from 1 to 10
arr = np.arange(1, 11)

print("Original Array:")
print(arr)

# Array indexing
print("\nElement at index 0:", arr[0])
print("Element at index 4:", arr[4])

# Array slicing
print("\nElements from index 2 to 6:")
print(arr[2:7])

# Mathematical operations
print("\nAddition:", arr + 5)
print("Subtraction:", arr - 2)
print("Multiplication:", arr * 2)
print("Division:", arr / 2)

# Mathematical functions
print("\nSum of array:", np.sum(arr))
print("Mean of array:", np.mean(arr))
print("Maximum element:", np.max(arr))
print("Minimum element:", np.min(arr))

# Create arrays filled with zeros and ones
print("\nArray of zeros:")
print(np.zeros(5))

print("\nArray of ones:")
print(np.ones(5))