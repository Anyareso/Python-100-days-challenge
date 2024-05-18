print("\033c")
age = int(input())
weeks_in_an_year = 52
assumed_life = 90 * weeks_in_an_year 
lived_weeks = age * weeks_in_an_year
weeks_left = assumed_life - lived_weeks
print(f"You have {weeks_left} weeks left")

# soln
# weeks = 90 - int(age)
# weeks = years * 52
# print(f"You have {weeks} left.")