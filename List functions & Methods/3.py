""" Remove all even numbers from the list."""
my_list = [45, 66, 66, 66, 78, 11, 11, 12, 12, 12]
my_list = [x for x in my_list if x % 2 != 0]
print(my_list)
# or
a = [45, 33, 0, 56, 22, 71, 89, 100]
b = []
for i in a:
    if i % 2 == 1:
        b.append(i)
print(b)
