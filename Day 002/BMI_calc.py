# Simple BMI calculator 
# BMI = weight / (height * height)
# 1st input; enter height in meters e.g:1.65
# 2nd input; enter weight in kilograms e.g:72

print("\033c")
height = input("Enter height in meters: ")
weight = input("Enter weight in kilograms: ")

den = float(height) * float(height)
num = int(weight)
BMI = (num / den)
print(int(BMI))
