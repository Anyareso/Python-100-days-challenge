import pandas
# data = pandas.read_csv("weather_data.csv")

# # Get average temp
# average_temp = data["temp"].mean()
# print(average_temp)
#
# # Get highest value
# max_value = data["temp"].max()
# print(max_value)
#
# # Get data in columns
# print(data["day"])
# print(data.day)

# Get data in rows
# print(data[data.day == "Monday"])

# Get data of the day with the highest temp
# print(data[data.temp == data.temp.max()])

# Getting information about a specific day
# monday = data[data.day == "Monday"]
# monday_temp = monday.temp[0]
# monday_temp_f = monday_temp * 9/5 + 32
# print(monday_temp_f)

# Create a dataframe from scratch
# data_dict = {
#     "students":["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")

# using Central Park Squirrel Census Data
data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20240807.csv")
Gray_squirrel = data[data["Primary Fur Color"] == "Gray"]
no_Gray_squirrel = len(Gray_squirrel)

Cinnamon_squirrel = data[data["Primary Fur Color"] == "Cinnamon"]
no_Cinnamon_squirrel = len(Cinnamon_squirrel)

Black_squirrel = data[data["Primary Fur Color"] == "Black"]
no_Black_squirrel = len(Black_squirrel)

squirrel_fur_colors = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [no_Gray_squirrel, no_Cinnamon_squirrel, no_Black_squirrel]
}

squirrel_count = pandas.DataFrame(squirrel_fur_colors)
squirrel_count.to_csv("squirrel_count.csv")
