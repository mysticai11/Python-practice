"""Create a list and prompt the user for an 'old number' followed by a
'new number.' If the 'old number' exists in the list, replace it with the 'new
number' provided by the use"""

a = [11, 22, 15, 33, 44, 55, 11, 55]
old = int(input("Enter old number = "))
new = int(input("Enter new number = "))
for i in range(0, len(a)):
    if a[i] == old:
        a[i] = new
print(a)
