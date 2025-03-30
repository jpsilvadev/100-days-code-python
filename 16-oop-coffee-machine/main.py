from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

make_coffee = True

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()


while make_coffee:
    choice = input(f"What would you like? ({menu.get_items()}): ")

    if choice == "off":
        make_coffee = False

    elif choice == "report":
        coffee_maker.report()
        money_machine.report()

    else:
        coffee = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(coffee):
            if money_machine.make_payment(coffee.cost):
                coffee_maker.make_coffee(coffee)
