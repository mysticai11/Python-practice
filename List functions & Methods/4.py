""" Ask the user for a number. Then, from a list of numbers, remove all
the numbers that can be divided by the number the user entered."""
my_list = [10, 15, 20, 25, 30]
num = int(input("Enter a number: "))
my_list = [x for x in my_list if x % num != 0]
print(my_list)
