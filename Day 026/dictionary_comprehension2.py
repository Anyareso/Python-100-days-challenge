weather_c = eval(input("enter values: "))
# input = {'monday': 12, 'tuesday': 14, 'wednesday': 15}
weather_f = {day: temp * 9/5 + 32 for (day, temp) in weather_c.items()}
print(weather_f)
