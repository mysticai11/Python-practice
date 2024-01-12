""" Generate a list of at least 10 numbers. Then, create two separate
lists called 'odd' and 'even.' Put all the odd numbers from the original list
into the 'odd' list, and all the even numbers into the 'even' list."""
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(my_list)
odd = []
for i in my_list:
    if i % 2 != 0:
        odd.append(i)
print(odd)
even = []
for i in my_list:
    if i % 2 == 0:
        even.append(i)
print(even)
