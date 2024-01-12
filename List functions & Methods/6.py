"""Start by creating two separate lists with random numbers. Then,
create a third list that merges the numbers from the first and second lists
together"""


list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]
result = []
for num in list1:
    result.append(num)
for num in list2:
    result.append(num)
print(result)
# or
list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]
result = list1 + list2
print(result)
