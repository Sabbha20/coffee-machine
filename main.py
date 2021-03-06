MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
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

money = 0

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def have_sufficient_coffee(user_drink):
    """Check whether enough ingredients are there in coffee machine or not"""
    for items in resources:
        if resources[items] < MENU[user_drink]["ingredients"][items]:
            print(f"Sorry there is not enough {items}.")
            return False
    return True


def coffee_price():
    total = float(input("Enter your quaters?: ")) * 0.25
    total += float(input("Enter your dimes?: ")) * 0.10
    total += float(input("Enter your nickels?: ")) * 0.05
    total += float(input("Enter your penny?: ")) * 0.01
    return total


def is_transaction_successful(drink_price, money_deposited):
    """Checking whether the deposited money was enough to buy coffee"""
    if money_deposited > drink_price:
        global money
        money = money + drink_price
        print(f"Here is ${round(money_deposited - drink_price, 2)} dollars in change.")
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_coffee(user_coffee, coffee_machine):
    """Making the coffee"""
    for items in coffee_machine:
        coffee_machine[items] = coffee_machine[items] - MENU[user_coffee]["ingredients"][items]
    return coffee_machine


is_on = True

while is_on:
    user_choice = input("What would you like? (espresso/latte/cappuccino): ")
    if user_choice == 'off':
        is_on = False
    elif user_choice == 'report':
        print(f"Water: {resources['water']} ml")
        print(f"Milk: {resources['milk']} ml")
        print(f"Coffee: {resources['coffee']} g")
        print(f"Money: ${money}")
    else:
        if have_sufficient_coffee(user_choice):
            deposit_money = coffee_price()
            cost_of_drink = MENU[user_choice]["cost"]
            if is_transaction_successful(cost_of_drink, deposit_money):
                make_coffee(user_choice, resources)
