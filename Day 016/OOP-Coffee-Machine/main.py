from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu_info = Menu()
make_coffee = CoffeeMaker()
process_coins = MoneyMachine()

machine_on = True
while machine_on:
    choice = input("What would you like? (espresso/latte/cappuccino/): ")
    if choice == "off":
        print("Shutting down")
        machine_on = False
    elif choice == "report":
        make_coffee.report()
    else:
        chosen_drink = menu_info.find_drink(order_name=choice)
        # Checks if item is in the menu
        if chosen_drink:
            # Checks if resources are sufficient
            if make_coffee.is_resource_sufficient(chosen_drink):
                # Process coins
                cost = chosen_drink.cost
                # Make payment
                if process_coins.make_payment(cost):
                    # Make coffee
                    make_coffee.make_coffee(chosen_drink)
