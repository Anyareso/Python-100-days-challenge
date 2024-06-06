################### Scope ####################

# enemies = 1

# def increase_enemies():
#   enemies = 2
#   print(f"enemies inside function: {enemies}")

# increase_enemies()
# print(f"enemies outside function: {enemies}")

# Local scope
# def drink_portion():
#   portion_strength = 2
#   print(portion_strength)

# drink_portion() 

# Global scope
player_health = 4
def drink_portion():
  portion_strength = 2
  print(player_health)

drink_portion()