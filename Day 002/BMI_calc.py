print("\033c")
# 1st input; enter height in meters e.g:1.65
# 2nd input; enter weight in kilograms e.g:72
height = input()
weight = input()
# Do not change the code above
# Write your code below this line
# BMI = weight / (height * height)
den = float(height) * float(height)
num = int (weight)
BMI = (num / den)
print(int(BMI))
