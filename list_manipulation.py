# Define a sample list
numbers = [10, 25, 5, 30, 15, 20]

# **Finding elements:**

# Find the maximum value
max_value = max(numbers)
print(f"Maximum value: {max_value}")

# Find the index of the first occurrence of 15
index_of_15 = numbers.index(15)
print(f"Index of 15: {index_of_15}")

# **Modifying elements:**

# Sort the list in ascending order
numbers.sort()
print(f"Sorted list: {numbers}")

# Reverse the list
numbers.reverse()
print(f"Reversed list: {numbers}")

# Remove duplicate elements (preserving order)
unique_numbers = list(set(numbers))
print(f"List with unique elements: {unique_numbers}")

# Insert a new element at a specific index
numbers.insert(2, 7)
print(f"List with element inserted at index 2: {numbers}")

# **Applying operations on elements:**

# Calculate the sum of all elements
total_sum = sum(numbers)
print(f"Total sum: {total_sum}")

# Find the average value
average_value = total_sum / len(numbers)
print(f"Average value: {average_value}")

# Square each element in the list
squared_numbers = [number**2 for number in numbers]
print(f"List with elements squared: {squared_numbers}")

# Filter elements based on conditions
even_numbers = [number for number in numbers if number % 2 == 0]
print(f"List of even numbers: {even_numbers}")

# **Exploring other libraries:**

# Use numpy for efficient numerical operations
import numpy as np
np_array = np.array(numbers)
doubled_array = np_array * 2
print(f"List doubled using numpy: {doubled_array.tolist()}")

# Use pandas for data analysis and manipulation
import pandas as pd
df = pd.DataFrame(numbers, columns=["numbers"])
print(f"Dataframe with list as a column: \n{df}")

This is just a basic example, and you can explore many other functionalities for list manipulation in Python. Feel free to ask for specific examples or tasks you'd like to achieve with lists!
