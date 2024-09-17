from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
maintenance_mode = False
money_machine = MoneyMachine()
is_on = True

while is_on == True:
    options = menu.get_items()
    choice = input(f"What would you like? {options}: ").lower()
    if choice == "off":
        is_on = False
        exit()
    drink = menu.find_drink(choice)
    print(drink)
    if choice == "report":
        coffee_maker.report()
        money_machine.report()
    elif coffee_maker.is_resource_sufficient(drink):
        money_machine.make_payment(drink.cost)
        coffee_maker.make_coffee(drink)
        coffee_maker.report()
        money_machine.report()
    else:
        print("Invalid input")