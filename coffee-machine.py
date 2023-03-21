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

############################################################################################
############################################################################################
###########This code can be improved, but I am not sure how. LF Tutor to analyze!###########
############################################################################################
############################################################################################


def report(drink):
    print(f"water: {resources['water']}\nmilk: {resources['milk']}\ncoffee: {resources['coffee']}\nmoney: {resources['money']}")


def order(drink):
    if drink == "report":
        report(drink)
        return order(str(input("What would you like? (espresso/latte/cappuccino)\n")))
    if drink == "espresso":
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
                use_resources(drink)
                print(f"Here's your {drink}. Your rest: ${rest}")
                return round(in_total, 2)
    elif drink == "latte" or drink == "cappuccino":
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
                print(f"Here's your {drink}. Your rest: ${rest}")
                use_resources(drink)
                return round(in_total, 2)


def check_resources(drink):
    def check_water(drink):
        if resources['water'] < MENU[drink]['ingredients']['water']:
            print("No water.")
            if input("Refill?") == "yes":
                refill()
            return True
    def check_coffee(drink):
        if resources['coffee'] < MENU[drink]['ingredients']['coffee']:
            print("No coffee.")
            if input("Refill?") == "yes":
                refill()
            return True
    def check_milk(drink):
        if resources['milk'] < MENU[drink]['ingredients']['milk']:
            print("No milk.")
            if input("Refill?") == "yes":
                refill()
            return True
    check_water(drink)
    check_coffee(drink)
    check_milk(drink)
    return True


def refill():
    resources['water'] = 300
    resources['milk'] = 200
    resources['coffee'] = 100
    print("Ingredients refilled successfully.")


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


def use_resources(drink):
    resources['water'] -= MENU[drink]['ingredients']['water']
    resources['coffee'] -= MENU[drink]['ingredients']['coffee']
    if drink != "espresso":
        resources['milk'] -= MENU[drink]['ingredients']['milk']
    money_status = resources['money'] + MENU[drink]['cost']
    resources['money'] = money_status
    return money_status



while True == True:
    USER_INPUT = str(input("What would you like? (espresso/latte/cappuccino)\n"))
    drink = USER_INPUT
    order(drink)
