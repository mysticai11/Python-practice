def factorial(n):
  if(n==0 or n==1):
   return 1
  else:
   return n * factorial(n-1)
print(factorial(3))
print(factorial(4))
print(factorial(5))

# fibonacci sequence
def fibonacci(n):
  if(n==0 or n==1):
   return 0 or 1
  else:
   return fibonacci (n-1 + n(n-2))
print(fibonacci(0))
print(fibonacci(1))
print(fibonacci(2))
print(fibonacci(3))
