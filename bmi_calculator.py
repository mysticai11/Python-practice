NAME=input("YOUR NAME:")
BMI_H=float(input("Enter your height in meters:"))
BMI_W=float(input("Enter your weight in kg:"))
BMI_VALUE= BMI_W/(BMI_H ** 2)
print(NAME)
print(BMI_VALUE)
if BMI_VALUE<18.5:
  print("UNDERWEIGHT")
if 18.5 <=BMI_VALUE <25:
  print("NORMAL WEIGHT")
if 25 <=BMI_VALUE<30:
  print("OVERWEIGHT") 
if 30<=BMI_VALUE<30:
  print("OBESITY")


