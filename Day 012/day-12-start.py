################### Scope ####################

enemies = 1

def increase_enemies():
  enemies = 2
  print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")

# Local scope
def drink_portion():
  portion_strength = 2
  print(portion_strength)

drink_portion() 

# Global scope
player_health = 4
def game():
  def drink_portion():
    portion_strength = 2
    print(player_health)

  drink_portion()
print(player_health)

# There is no block scope
game_level = 3
enemies = ["Skeleton", "Zombie", "Alien"]
if game_level < 5:
  new_enemy = enemies[0]
print(new_enemy)
# If you create a variable within a function, it is only available within that function

# Modifying global scope
# enemies = 1

# def increase_enemies():
#   # Modifying a global variable within a local scope
#   # global enemies
#   # enemies += 1 
#   print(f"enemies inside function: {enemies}")
#   return enemies + 1 

# enemies = increase_enemies()
# print(f"enemies outside function: {enemies}")

# Global constants(don't intend on changing them)
PI = 3.14159