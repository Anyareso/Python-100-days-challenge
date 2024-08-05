import pandas
data = pandas.read_csv("weather_data.csv")

average_temp = data["temp"].mean()
print(average_temp)