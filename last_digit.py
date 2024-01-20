# num = int(input("Enter a number:"))
# last_digit= str(num)[-1]
# print(last_digit)
# To print the last digit of a number

num = int(input("Number: "))
# last_digit= int(str(num)[-1])
# if last_digit %5==0:
#   print("divisible")
# else:
  # print("not divisible")
last_digit = num%10
print(f"The last digit of{num} is = {last_digit}")