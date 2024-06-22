import turtle
# from turtle import Turtle,Screen
#
# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("DarkOrchid")
# timmy.forward(100)
#
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

# Importing prettyTable class
from prettytable import PrettyTable

# Create a prettyTable object and save it in a variable called class
table = PrettyTable()
print(table)

# # Adding columns to table(object)
# table.field_names = ["Pokemon Name", "Type"]
# table.add_row(["Pikachu", "Electricity"])
# table.add_row(["Squirtle", "Water"])
# table.add_row(["Charmander", "Fire"])
# print(table)

# To add all rows at once
# table.field_names = ["Pokemon Name", "Type"]
# table.add_rows(
# [
#     ["Pikachu", "Electricity"],
#     ["Squirtle", "Water"],
#     ["Charmander", "Fire"]]
# )
# print(table)

# another way to add columns to the table
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
# attributes
table.align = "r"
print(table)
