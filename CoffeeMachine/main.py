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
}

def delete_resource(resources_dict: dict, menu_dict:dict, coffee_name: str):
    resources_dict["water"] = resources_dict["water"] - menu_dict[coffee_name]["ingredients"]["water"]
    coffee_milk = menu_dict[coffee_name]["ingredients"].get("milk")
    if coffee_milk is None:
        pass
    else:
        resources_dict["milk"] = resources_dict["milk"] - coffee_milk
        resources_dict["coffee"] = resources_dict["coffee"] - menu_dict[coffee_name]["ingredients"]["coffee"]

def check_resources_sufficient(resources_dict: dict, menu_dict: dict, coffee_name: str) -> bool:
    water_mach = resources_dict["water"]
    milk_mach = resources_dict["milk"]
    coffee_mach = resources_dict["coffee"]

    water_type_coffee = menu_dict[coffee_name]["ingredients"]["water"]

    milk_type_coffee = menu_dict[coffee_name]["ingredients"].get("milk")
    if milk_type_coffee is None:
        milk_type_coffee = 0

    coffee_type_coffee = menu_dict[coffee_name]["ingredients"]["coffee"]

    if water_type_coffee > water_mach or milk_type_coffee > milk_mach or coffee_type_coffee > coffee_mach:
        print(f"Sorry there is not enough ingredients.")
        return None

    return menu_dict[coffee_name]["cost"]

def process_coins():
    print("Please insert coins: ")
    total = int(input("How many quarters?:")) * 0.25
    total += int(input("How many dimes?:")) * 0.1
    total += int(input("How many nickles?:")) * 0.05
    total += int(input("How many pennies?:")) * 0.01
    return total

def print_report(resources_dict, money):
    water = resources_dict["water"]
    milk = resources_dict["milk"]
    coffee = resources_dict["coffee"]
    print(f"Water: {water} ml")
    print(f"Milk: {milk} ml")
    print(f"Coffee: {coffee}g")
    print(f"Money: ${money}")




def main():
    money = 0
    while True:
        price = 0
        # 1. Prompt user by asking “What would you like? (espresso/latte/cappuccino)
        options = input("What would you like? (espresso/latte/cappuccino):")
        # 2. Turn off the Coffee Machine by entering “off” to the prompt
        if options == "off":
            break
        # 3. Print report.
        elif options == "report":
            print_report(resources, money)
            continue
        # 4. Check resources sufficient?
        elif options == "latte":
            price = check_resources_sufficient(resources, MENU, "latte")
        elif options == "espresso":
            price = check_resources_sufficient(resources, MENU, "espresso")
        elif options == "cappuccino":
            price = check_resources_sufficient(resources, MENU, "cappuccino")

        # 5. Process coins.
        total = process_coins()
        # 6. Check transaction successful?
        if total >= price:
            change = total - price
            print(f"Thank you, your change is {change}")
            delete_resource(resources, MENU, options)
            money += price
        else:
            print(f"Sorry that's not enough money. Money refunded. {total}")




    pass


main()