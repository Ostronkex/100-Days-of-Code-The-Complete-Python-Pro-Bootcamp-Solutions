from CoffeeData import MENU
from CoffeeData import resources
import random

maintenance_mode = False

def espresso(): # Espresso
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    total = (pennies * 0.01) + (dimes * 0.1) + (nickles * 0.05) + (quarters * 0.25)
    print(f"The total you paid is ${total}")
    if total < MENU["espresso"]["cost"]:
        print("Not enough money!")
        espresso()
    elif total > MENU["espresso"]["cost"]:
        change = total - MENU["espresso"]["cost"]
        print(f"Here is ${change} in change")
        print("Here is your espresso. Enjoy!")
        resources["water"] = resources["water"] - MENU["espresso"]["ingredients"]["water"]
        resources["coffee"] = resources["coffee"] - MENU["espresso"]["ingredients"]["coffee"]
        resources["money"] = resources["money"] + MENU["espresso"]["cost"]
        report()
    else:
        print("Here is your espresso. Enjoy!")
        resources["water"] = resources["water"] - MENU["latte"]["ingredients"]["water"]
        resources["coffee"] = resources["coffee"] - MENU["latte"]["ingredients"]["coffee"]
        resources["money"] = resources["money"] + MENU["latte"]["cost"]
        report()

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
              
def cappuccino(): # Cappuccino
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    total = (pennies * 0.01) + (dimes * 0.1) + (nickles * 0.05) + (quarters * 0.25)
    print(f"The total you paid is ${total}")
    if total < MENU["cappuccino"]["cost"]:
        print("Not enough money!")
        cappuccino()
    elif total > MENU["cappuccino"]["cost"]:
        change = total - MENU["cappuccino"]["cost"]
        print(f"Here is ${change} in change")
        print("Here is your cappuccino. Enjoy!")
        resources["water"] = resources["water"] - MENU["cappuccino"]["ingredients"]["water"]
        resources["milk"] = resources["milk"] - MENU["cappuccino"]["ingredients"]["milk"]
        resources["coffee"] = resources["coffee"] - MENU["cappuccino"]["ingredients"]["coffee"]
        resources["money"] = resources["money"] + MENU["cappuccino"]["cost"]
        report()
    else:
        print("Here is your cappuccino. Enjoy!")
        resources["water"] = resources["water"] - MENU["latte"]["ingredients"]["water"]
        resources["milk"] = resources["milk"] - MENU["latte"]["ingredients"]["milk"]
        resources["coffee"] = resources["coffee"] - MENU["latte"]["ingredients"]["coffee"]
        resources["money"] = resources["money"] + MENU["latte"]["cost"]
        report()

def report(): 
    print("Here are the remaining resources")
    print(f"Water: {resources["water"]}ml")
    print(f"Milk: {resources["milk"]}ml")
    print(f"Coffee: {resources["coffee"]}g")
    print(f"Money: ${resources["money"]}")

while maintenance_mode == False:
    user_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if user_choice == "espresso":
        if resources["water"] >= MENU["espresso"]["ingredients"]["water"]:
            None
        else:
            print("Sorry there is not enough water.")
            exit()
        if resources["coffee"] >= MENU["latte"]["ingredients"]["coffee"]:
            None
        else: 
            print("Sorry there is not enough coffee")
            exit()
        if resources["water"] >= MENU["espresso"]["ingredients"]["water"] and resources["coffee"] >= MENU["espresso"]["ingredients"]["coffee"]:
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
        if resources["water"] >= MENU["cappuccino"]["ingredients"]["water"]:
            None
        else:
            print("Sorry there is not enough water.")
            exit()
        if resources["milk"] >= MENU["cappuccino"]["ingredients"]["milk"]:
            None
        else:
            print("Sorry there is not enough milk")
            exit()
        if resources["coffee"] >= MENU["cappuccino"]["ingredients"]["coffee"]:
            None
        else:
            print("Sorry there is not enough coffee")
            exit()
        if resources["water"] >= MENU["cappuccino"]["ingredients"]["water"] and resources["milk"] >= MENU["cappuccino"]["ingredients"]["milk"] and resources["coffee"] >= MENU["cappuccino"]["ingredients"]["coffee"]:
            cappuccino()

    elif user_choice == "report":
        report()

    elif user_choice == "off":
        print("maintenance mode")
        maintenance_mode = True
    
    else:
        print("Invalid input")


