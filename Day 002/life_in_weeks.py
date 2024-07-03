# My life in weeks program
# Calculates how many weeks you have left to live to get to 90 years
# Things to consider:
# There are 365 days in a year,
# Roughly 52 weeks in a year
# Asks user to input their current age, then converts it to weeks
print("\033c")
age = int(input("Enter your current age in years: "))

days_in_a_year = 365
weeks_in_an_year = 52
hours_in_a_day = 24

assumed_life_in_weeks = 90 * weeks_in_an_year
assumed_life_in_days = assumed_life_in_weeks * 7
assumed_life_in_hours = assumed_life_in_days * hours_in_a_day

lived_weeks = age * weeks_in_an_year
lived_days = age * days_in_a_year
hours_lived = lived_days * hours_in_a_day

weeks_left = assumed_life_in_weeks - lived_weeks
days_left = assumed_life_in_days - lived_days
hours_left = assumed_life_in_hours - hours_lived
print(f"You have {weeks_left} weeks left {days_left} days left  and {hours_left} hours left")

# soln
# weeks = 90 - int(age)
# weeks = years * 52
# print(f"You have {weeks} left.")
