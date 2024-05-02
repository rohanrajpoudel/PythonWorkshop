import numpy as np
a= [1, 2, 3, 4, 5]
# Create a NumPy array from a Python list
arr = np.array(a)
print("NumPy array:", arr)
print("the sum of the array is", arr.sum())
print("the maximum of the array is", arr.max())
print("the maximum of the array is", arr.min())
print(np.math.factorial(5))

# Create a NumPy array from a Python tuple
arr_tuple = np.array((6, 7, 8, 9, 10))
print("NumPy array from tuple:", arr_tuple)
# Output: NumPy array from tuple: [ 6  7  8  9 10]

# Create a NumPy array from a nested Python list
nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
arr_nested = np.array(nested_list)
print("NumPy array from nested list:\n", arr_nested)
# Output:
# NumPy array from nested list:
#  [[1 2 3]
#   [4 5 6]
#   [7 8 9]]
