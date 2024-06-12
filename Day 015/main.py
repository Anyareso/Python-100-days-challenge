MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
# TODO - 1: Print report of coffee machine resources
order = input("What would you like? (espresso/latte/cappuccino)")


#  TODO - 2: Check if resources are sufficient
def remaining_resources():
    """Returns remaining resources when an order is made"""
    resources["water"] = remaining_water
    resources["milk"] = remaining_milk
    resources["coffee"] = remaining_coffee
    return f"water: {resources["water"]}, milk: {resources["milk"]}, coffee: {resources["coffee"]}"


if order == "report":
    for keys, values in resources.items():
        print(keys, ':', values)
    # print(remaining_resources())
else:
    order_made = True
    while order_made:
        # Updates the amount of resources left
        menu_items = order
        if menu_items == "espresso":
            remaining_water = resources["water"] - MENU["espresso"]["ingredients"]["water"]
            remaining_milk = resources["milk"]
            remaining_coffee = resources["coffee"] - MENU["espresso"]["ingredients"]["coffee"]
            print(remaining_resources())
            break

        elif menu_items == "latte":
            remaining_water = resources["water"] - MENU["latte"]["ingredients"]["water"]
            remaining_milk = resources["milk"] - MENU["latte"]["ingredients"]["milk"]
            remaining_coffee = resources["coffee"] - MENU["latte"]["ingredients"]["coffee"]
            print(remaining_resources())
            break
        elif menu_items == "cappuccino":
            remaining_water = resources["water"] - MENU["cappuccino"]["ingredients"]["water"]
            remaining_milk = resources["milk"] - MENU["cappuccino"]["ingredients"]["milk"]
            remaining_coffee = resources["coffee"] - MENU["cappuccino"]["ingredients"]["coffee"]
            print(remaining_resources())
            break
        # order_made = False

#  TODO - 3: Process coins
print("Please insert coins. ")


# Calculates the total cost of the coins placed in and outputs change if need be.
def calculate():
    coin_values = {
        "penny": 0.01,
        "dime": 0.10,
        "nickel": 0.05,
        "quarter": 0.25
    }
    quarters = int(input("How many quarters?"))
    dimes = int(input("How many dimes?"))
    nickels = int(input("How many nickels?"))
    pennies = int(input("How many pennies?"))
    total_inputs = ((coin_values["penny"] * pennies) + (coin_values["dime"] * dimes) +
                    (coin_values["nickel"] * nickels) + (coin_values["quarter"] * quarters))

    if total_inputs > MENU["espresso"]["cost"]:
        change = (total_inputs - MENU["espresso"]["cost"])
        rounded_change = round(change, 2)
        return f"Here is your change: ${rounded_change}"
    elif total_inputs > MENU["latte"]["cost"]:
        change = (total_inputs - MENU["espresso"]["cost"])
        rounded_change = round(change, 2)
        return f"Here is your change: ${rounded_change}"
    if total_inputs > MENU["cappuccino"]["cost"]:
        change = (total_inputs - MENU["espresso"]["cost"])
        rounded_change = round(change, 2)
        return f"Here is ${rounded_change} in change"
    else:
        return total_inputs


print(calculate())

#  TODO - 3: Check if transaction was successful
#  TODO - 5: Make coffee
