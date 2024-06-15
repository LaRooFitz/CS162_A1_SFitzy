# Shasta Fitzgerald
# Week 3
# Python Arrays Assignment

# array = np.random.randint(x,x, size=(x,x), dtype=int)
# np.mean(array, axis=1)

import numpy as np

# Create a random array using a seed for reproducibility
np.random.seed(10)

# Build a 5x5 array with random values
rand_array = np.random.rand(5, 5)

# Print the array
print("My 5x5 array: ")
print(rand_array)

# Print the number from the 2nd row, 3rd column
num_row2_col3 = rand_array[1, 2]
print("\nRow 2, Column 3, number: ")
print(num_row2_col3)

# Print the sum of all the elements in the array
sum_array_elements = np.sum(rand_array)
print("\nArray elements sum: ")
print(sum_array_elements)

# Print the mean of each row in the array
mean_rows = np.mean(rand_array, axis=1)
print("\nMean of each row: ")
print(mean_rows)
#hahaha mean rows

#Print the maximum value in each column of the array
max_column = np.max(rand_array, axis=0)
print("\nMax of each column: ")
print(max_column)