from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
make_drink = CoffeeMaker()
cash = MoneyMachine()


is_on = True

while is_on:
    choice = input(f"What would you like? ({menu.get_items()}): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        make_drink.report()
        cash.report()
    else:
        drink = menu.find_drink(choice)
        if make_drink.is_resource_sufficient(drink):
            payment = cash.make_payment(drink.cost)
            if payment:
                make_drink.make_coffee(drink)

