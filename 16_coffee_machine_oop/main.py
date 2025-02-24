from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

stop = False
while not stop:
    selection = input(f"What do you want {menu.get_items()}: ")
    if selection == "report":
        coffee_maker.report()
        money_machine.report()
    elif selection == "off":
        stop = True
    elif menu.find_drink != None:
        coffee = menu.find_drink(selection)
        if coffee_maker.is_resource_sufficient(coffee) and money_machine.make_payment(coffee.cost):
            coffee_maker.make_coffee(coffee)
            coffee_maker.report()
            money_machine.report()



