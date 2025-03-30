from machine_resources import menu, resources

QUARTERS = 0.25
DIMES = 0.10
NICKELS = 0.05
PENNIES = 0.01

money = 0


def check_money():
    """calculate total inserted money"""
    print("Please insert coins.")
    quarters = int(input("How many quarters? "))
    dimes = int(input("How many dimes? "))
    nickels = int(input("How many nickels? "))
    pennies = int(input("How many pennies? "))

    return (
        (QUARTERS * quarters)
        + (DIMES * dimes)
        + (NICKELS * nickels)
        + (PENNIES * pennies)
    )


def check_ingredients(coffee):
    """check if machine ingredients are necessary to make selected coffee"""
    for ingredient in coffee:
        if coffee[ingredient] > resources[ingredient]:
            print(f"Sorry there is not enough {ingredient}.")
            return False
        return True


def make_coffee(coffee):
    """Subtract necessary ingredients to make coffee from resource dict"""
    for k in coffee:
        resources[k] -= coffee[k]
    return resources


machine_on = True


def main():
    global machine_on, money
    while machine_on:
        # take coffee order --> type
        choice = input("What would you like? (espresso/latte/cappuccino): ")

        # create report feature
        if choice == "report":
            print(
                f"Water: {resources['water']} ml \n"
                f"Milk: {resources['milk']} ml \n"
                f"Coffee: {resources['coffee']} g\n"
                f"Money: ${money}"
            )
        # turn machine off feature
        elif choice == "off":
            machine_on = False

        # process order
        elif choice == "espresso" or "latte" or "cappuccino":
            # select coffee
            coffee = menu[choice]
            # extract cost
            required_money = coffee["cost"]

            if check_ingredients(coffee["ingredients"]):
                inserted_money = check_money()
                if inserted_money >= required_money:
                    money += required_money
                    if inserted_money > required_money:
                        print(
                            f"Here is ${round(inserted_money - required_money, 2)} in change."
                        )
                    make_coffee(coffee["ingredients"])
                    print(f"Here is your {choice}☕. Enjoy!")
                elif inserted_money < required_money:
                    print("Sorry that's not enough money. Money refunded.")


main()
