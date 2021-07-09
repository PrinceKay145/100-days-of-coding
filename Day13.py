menu = {
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
def report():
    water = resources['water']
    milk = resources['milk']
    coffee = resources['coffee']
    money = 30
    return f"Water: {water}ml \nMilk: {milk}ml \nCoffee: {coffee}g \nMoney: ${money}"
# TODO 1. The prompt have to show everytime a drink is sold successfully
start= input("What would you like? (espresso/latte/cappuccino): ").lower()
coffee_fee = 0
change = 0
def get_a_coffee(start, menu, resources):
    if start == "espresso":
        print("Please insert coins.")
        take_quarters= int(input("How many quarters?: "))
        take_dimes= int(input("How many dimes?: "))
        take_nickles = int(input("How many nickles?: "))
        take_pennies = int(input("How many pennies?: "))
        quarters = take_quarters * 0.25
        dimes = take_dimes * 0.1
        nickles = take_nickles * 0.05
        pennies = take_pennies * 0.01
        coffee_fee = pennies+dimes+nickles+quarters
        change = coffee_fee - [start]['cost']

        if menu[start]["ingredients"]["water"] < resources["water"]:
            if menu[start]["ingredients"]["coffee"] < resources["coffee"]:
                print (f"Here is your ${change} change")
                print(f"Here is your {start}. Enjoy!")
            else:
                print(f"Sorry there is no enough coffee")
        else:
            print("Sorry there is no enough water")
    elif start == "latte":
        print("B")
    elif start == "cappuccino":
        print("C")
    elif start == "off":
        return
    elif start == "report":
        print(report())
get_a_coffee(start, menu, resources)
