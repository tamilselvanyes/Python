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

QUARTERS = 0.25
DIMES = 0.1
NICKLES = 0.05
PENNIES = 0.01

start_again = True


def show_report():
    for data in resources:
        print(f"{data.capitalize()}: {resources[data]}")


def check_availability(item):
    ingredients = item["ingredients"]
    resource_unavailable = []
    for ingredient in ingredients:
        if resources[ingredient] < ingredients[ingredient]:
            resource_unavailable.append(ingredient)

    return resource_unavailable


def calculate_money_deposited(quarters, dimes, nickles, pennies):
    total = quarters * QUARTERS + dimes * DIMES + nickles * NICKLES + pennies * PENNIES
    return total


def check_sufficient_money(item, money):
    ordered_item_cost = item["cost"]
    if money >= ordered_item_cost:
        return True
    else:
        return False


def update_resource(ordered_drink, current_resource):
    resource_copy = current_resource
    required_ingredients = ordered_drink["ingredients"]

    for ingredient in required_ingredients:
        required_amount = required_ingredients[ingredient]
        if required_amount:
            resource_copy[ingredient] = current_resource[ingredient] - required_amount
    resource_copy["money"] += ordered_drink["cost"]
    return resource_copy


def additional_money(drink, deposited):
    drink_cost = drink["cost"]
    return "{:.2f}".format(deposited - drink_cost)


while start_again:
    action = input("What would you like to have? 'espresso'/'latte'/'cappuccino'")
    if action == "report":
        show_report()
    elif action == "off":
        start_again = False
    else:
        if action == 'latte' or action == 'espresso' or action == "cappuccino":
            ordered_item = MENU[action]
            unavailable_items = check_availability(ordered_item)
            if len(unavailable_items) == 0:
                print("Insert Coins")
                no_of_quarters = int(input("Number of Quarter:"))
                no_of_dimes = int(input("Number of Dimes:"))
                no_of_nickles = int(input("Number of Nickles:"))
                no_of_pennies = int(input("Number of Pennies:"))

                money_deposited = calculate_money_deposited(no_of_quarters, no_of_dimes, no_of_nickles, no_of_pennies)

                if check_sufficient_money(ordered_item, money_deposited):
                    change_to_return = additional_money(ordered_item, money_deposited)
                    if change_to_return != 0:
                        print(f"Here is ${change_to_return} in change!! Enjoy 🥰 ")
                    update_resource(ordered_item, resources)
                    print(f"Here's you {action.capitalize()}")
                else:
                    print("Sorry that's not enough money, Money refunded.")
            else:
                print(f"Sorry there is not enough {','.join(unavailable_items)}")
        else:
            print("Wrong command, please try again...")
