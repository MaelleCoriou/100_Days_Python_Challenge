from data import MENU, resources

## Coffee machine program ##

MONEY = 2.5


def report_status(report, cash):
    """print the report of the coffee machine resources"""
    water_status = report["water"]
    milk_status = report["milk"]
    coffee_status = report["coffee"]
    money_status = cash
    return f"water: {water_status}ml\nMilk: {milk_status}ml\nCoffee: {coffee_status}ml\nMoney: €{money_status}"


def check_resources(report, order):
    """Check if the resources are sufficient to order, returns true or false"""
    if order == "espresso":
        if report["water"] >= MENU[order]["ingredients"]["water"] and \
                report["coffee"] >= MENU[order]["ingredients"]["coffee"]:
            return True
    elif order == "cappuccino" or order == "latte":
        if report["water"] >= MENU[order]["ingredients"]["water"] and \
                report["coffee"] >= MENU[order]["ingredients"]["coffee"] and \
                report["milk"] >= MENU[order]["ingredients"]["milk"]:
            return True


def return_resources(report, order):
    """Returns the missing resource"""
    if order == "espresso":
        if report["water"] <= MENU[order]["ingredients"]["water"]:
            return "water"
        elif report["coffee"] <= MENU[order]["ingredients"]["coffee"]:
            return "coffee"
    elif order == "cappuccino" or order == "latte":
        if report["water"] <= MENU[order]["ingredients"]["water"]:
            return "water"
        elif report["coffee"] <= MENU[order]["ingredients"]["coffee"]:
            return "coffee"
        elif report["milk"] <= MENU[order]["ingredients"]["milk"]:
            return "milk"


def update_resources(report, order):
    """Updates resources dictionary, subtracts new order to resources"""
    if order == "espresso":
        report["water"] -= MENU[order]["ingredients"]["water"]
        report["coffee"] -= MENU[order]["ingredients"]["coffee"]
    elif order == "cappuccino" or order == "latte":
        report["water"] -= MENU[order]["ingredients"]["water"]
        report["milk"] -= MENU[order]["ingredients"]["milk"]
        report["coffee"] -= MENU[order]["ingredients"]["coffee"]


def calc_payment(q, d, n, p):
    """Calculates the total paid : q=quarters, d=dimes, n=nickles, p=pennies"""
    total = q * 0.25 + d * 0.10 + n * 0.05 + p * 0.01
    return total


def cost(order):
    """Return the amount to pay for selected drink"""
    to_pay = MENU[order]["cost"]
    return to_pay


def coffee_machine():
    global MONEY
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

    # Report of the current resources
    report_resources = report_status(resources, MONEY)

    # Inform if the order isn't valid
    if choice == "report":
        # Print report of the coffee machine
        print(report_resources)
        choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    elif choice == "off":
        # Turn off the program
        return
    elif choice not in MENU:
        print("Invalid choice, re-enter your choice.")
        choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

    amount = cost(choice)
    print(f"Please insert: €{amount}")

    # Check if resources are sufficient for the order
    status_coffee_machine = check_resources(resources, choice)

    while status_coffee_machine:
        quarters = int(input("how many quarters?: "))
        dimes = int(input("how many dimes?: "))
        nickles = int(input("how many nickles?: "))
        pennies = int(input("how many pennies?: "))
        paid = calc_payment(quarters, dimes, nickles, pennies)
        if amount == paid:
            print(f"Here is your {choice} ☕. Enjoy!")
            update_resources(resources, choice)
            MONEY += paid
            coffee_machine()
        elif amount > paid:
            print("Sorry not enough money inserted. Money refunded.")
            coffee_machine()
        else:
            refund = round(paid - amount, 2)
            print(f"Here is €{refund} in change")
            print(f"Here is your {choice} ☕. Enjoy!")
            update_resources(resources, choice)
            MONEY += amount
            coffee_machine()
    print(f"Not enough resources : {return_resources(resources, choice)}")
    coffee_machine()


coffee_machine()
