# Inteprative BMI 
# Under 18.5, they are underweight
# Over 18.5 but below 25 they are normal weight
# Over 25 but below 30 they are slightly overweight
# Over 30 but below 35 they are obese
# Above 35 they are clinically obese
# Goal is to calculate BMI and give its interpretation


# 1st input; enter height in meters e.g:1.65
# 2nd input; enter weight in kilograms e.g:72

height = float(input("Enter your height in meters\n"))
weight = int(input("Enter your weight in kilograms\n"))
BMI = weight/(height**2)
if BMI < 18.5:
    print(f"Your BMI is {BMI} , you are underweight")
elif BMI < 25:
    print(f"Your BMI is {BMI} , you are normal weight")
elif BMI < 30:
    print(f"Your BMI is {BMI} , you are slightly overweight")
elif BMI < 35:
    print(f"Your BMI is {BMI} , you are obese")
else:
    print(f"Your BMI is {BMI} , you are clinically obese")