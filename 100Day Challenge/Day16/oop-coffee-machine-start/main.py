from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

start_again = True

while start_again:
    action = input(f"What would you like to have? {menu.get_items()}")
    if action == "report":
        coffee_maker.report()
        money_machine.report()
    elif action == "off":
        start_again = False
    else:
        if action == 'latte' or action == 'espresso' or action == "cappuccino":
            ordered_item = menu.find_drink(action)
            if coffee_maker.is_resource_sufficient(ordered_item):
                if money_machine.make_payment(ordered_item.cost):
                    coffee_maker.make_coffee(ordered_item)
        else:
            print("Wrong command, please try again...")



