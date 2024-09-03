# Start of coffee machine

"""
1. Print report (resources left)
2. Check that resources are sufficient for chosen drink
3. Process coins (quarter, dime, nickles, pennies)
4. Check transaction successful
5. Make coffee and deduct resources from total, add coins to cash register

1. What would you like
2. Please insert coins
    2.1: How many quarters?
    2.2: How many dimes?
    2.3: How many nickles?
    2.4: How many pennies?
3. If coins not enough for drink, refund and abort
4. If coins are enough, calculate total coin input and return change based on cost of coffee
5. Give drink
"""

from CoffeeData import MENU
from CoffeeData import resources
import random

maintenance_mode = False

def espresso():
    print("Espresso")

def latte(): # Latte
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    total = (pennies * 0.01) + (dimes * 0.1) + (nickles * 0.05) + (quarters * 0.25)
    print(f"The total you paid is ${total}")
    if total < MENU["latte"]["cost"]:
        print("Not enough money!")
        latte()
    elif total > MENU["latte"]["cost"]:
        change = total - MENU["latte"]["cost"]
        print(f"Here is ${change} in change")
        print("Here is your latte. Enjoy!")
        resources["water"] = resources["water"] - MENU["latte"]["ingredients"]["water"]
        resources["milk"] = resources["milk"] - MENU["latte"]["ingredients"]["milk"]
        resources["coffee"] = resources["coffee"] - MENU["latte"]["ingredients"]["coffee"]
        resources["money"] = resources["money"] + MENU["latte"]["cost"]
        report()
    else:
        print("Here is your latte. Enjoy!")
        resources["water"] = resources["water"] - MENU["latte"]["ingredients"]["water"]
        resources["milk"] = resources["milk"] - MENU["latte"]["ingredients"]["milk"]
        resources["coffee"] = resources["coffee"] - MENU["latte"]["ingredients"]["coffee"]
        resources["money"] = resources["money"] + MENU["latte"]["cost"]
        report()
              
def cappuccino():
    print("Cappuccino")

def report():
    print(f"Water: {resources["water"]}ml")
    print(f"Milk: {resources["milk"]}ml")
    print(f"Coffee: {resources["coffee"]}g")
    print(f"Money: ${resources["money"]}")

while maintenance_mode == False:
    user_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if user_choice == "espresso":
        espresso()

    elif user_choice == "latte":
        if resources["water"] >= MENU["latte"]["ingredients"]["water"]:
            None
        else:
            print("Sorry there is not enough water.")
            exit()
        if resources["milk"] >= MENU["latte"]["ingredients"]["milk"]:
            None
        else:
            print("Sorry there is not enough milk")
            exit()
        if resources["coffee"] >= MENU["latte"]["ingredients"]["coffee"]:
            None
        else:
            print("Sorry there is not enough coffee")
            exit()
        if resources["water"] >= MENU["latte"]["ingredients"]["water"] and resources["milk"] >= MENU["latte"]["ingredients"]["milk"] and resources["coffee"] >= MENU["latte"]["ingredients"]["coffee"]:
            latte()

    elif user_choice == "cappuccino":
        cappuccino()

    elif user_choice == "report":
        print(f"Water: {resources["water"]}ml")
        print(f"Milk: {resources["milk"]}ml")
        print(f"Coffee: {resources["coffee"]}g")
        print(f"Money: ${resources["money"]}")

    elif user_choice == "off":
        print("maintenance mode")
        maintenance_mode = True
        exit()
    
    else:
        print("Invalid input")


