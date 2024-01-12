"""Write a program that prompts the user to specify the length of a list
and then requests numbers to populate that list. Display the final list as
the output."""
list_length = int(input("Enter length = "))
result = []
for i in range(1, list_length + 1):
    num = int(input(f"Enter value at position {i} = "))
    result.append(num)

print(result)
