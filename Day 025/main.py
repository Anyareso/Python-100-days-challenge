# with open("weather_data.csv", "r") as values:
#     data = values.readlines()
#     print(data)

import csv

with open("weather_data.csv", "r") as values:
    data = csv.reader(values)
    temperatures = []
    for row in data:
        if row[1] != "temp":
            temperatures.append(int(row[1]))
    print(temperatures)

