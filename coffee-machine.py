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
    "money": 0
}

QUARTERS_VALUE = 0.25
DIMES_VALUE = 0.1
NICKLES_VALUE = 0.05
PENNIES_VALUE = 0.01

""" BELOW: Function that checks the current amount of resources."""
def report(drink):
    print(f"water: {resources['water']}\nmilk: {resources['milk']}\ncoffee: {resources['coffee']}\nmoney: {resources['money']}")

""" BELOW: Function that takes money from user, check if there's enough resources. Then it counts if there's enough money, and if so, returns error or a coffee."""
def order(drink):
    if drink == "report":
        report(drink)
        return order(str(input("What would you like? (espresso/latte/cappuccino)\n")))
    if drink == "latte" or drink == "cappuccino" or drink == "espresso":
        check_resources(drink)
        in_total = float(round(payment(), 2))
        if in_total < MENU[drink]['cost']:
                print("Not enough money. Money refunded.")
                return order(str(input("What would you like? (espresso/latte/cappuccino)\n")))
        elif in_total == MENU[drink]['cost']:
                print(f"Here's your {drink}, have a nice day!")
                use_resources(drink)
                return round(in_total, 2)
        else:
                rest = in_total - MENU[drink]['cost']
                round(rest, 2)
                print(f"Here's your {drink}. Your rest: ${round(rest, 2)}")
                use_resources(drink)
                return round(in_total, 2)

""" BELOW: Function that checks resources. If there's no enough resources, ask user for refill."""
def check_resources(drink):
    def check_water(drink):
        if resources['water'] < MENU[drink]['ingredients']['water']:
            print("No water.")
            print("...")
            refill()
            return True
    def check_coffee(drink):
        if resources['coffee'] < MENU[drink]['ingredients']['coffee']:
            print("No coffee.")
            print("...")
            refill()
            return True
    def check_milk(drink):
        if resources['milk'] < MENU[drink]['ingredients']['milk']:
            print("No milk.")
            print("...")
            refill()
            return True
    check_water(drink)
    check_coffee(drink)
    if drink != "espresso":
        check_milk(drink)
    return True

""" BELOW: Function that refill resources."""
def refill():
    resources['water'] = 300
    resources['milk'] = 200
    resources['coffee'] = 100
    print("Ingredients refilled successfully.")

""" BELOW: Function that takes the money and multiply by their value. Then return total value"""
def payment():
    quarters = float(input("Quarters: "))
    dimes = float(input("Dimes: "))
    nickles = float(input("Nickles: "))
    pennies = float(input("Pennies: "))
    quarters_sum = QUARTERS_VALUE * quarters
    dimes_sum = DIMES_VALUE * dimes
    nickles_sum = NICKLES_VALUE * nickles
    pennies_sum = PENNIES_VALUE * pennies
    in_total = quarters_sum + dimes_sum + nickles_sum + pennies_sum
    return in_total

""" BELOW: Function that uses ingredients according to chosen type of coffee. It takes needed resources away."""
def use_resources(drink):
    resources['water'] -= MENU[drink]['ingredients']['water']
    resources['coffee'] -= MENU[drink]['ingredients']['coffee']
    if drink != "espresso":
        resources['milk'] -= MENU[drink]['ingredients']['milk']
    money_status = resources['money'] + MENU[drink]['cost']
    resources['money'] = money_status
    return money_status


""" ENGINE"""
while True == True:
    USER_INPUT = str(input("What would you like? (espresso/latte/cappuccino)\n"))
    drink = USER_INPUT
    order(drink)
