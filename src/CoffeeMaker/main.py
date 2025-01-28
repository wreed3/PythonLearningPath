from coffee_maker import CoffeeMaker
from CoffeeMaker.Menu  import Menu
from CoffeeMaker.MoneyMachine import MoneyMachine

coffee_maker = CoffeeMaker()
menu = Menu()
money_machine = MoneyMachine()



while coffee_maker.is_on:
    coffee_choice = input(f"What would you like? (espresso/latte/cappuccino): ").lower()
    if coffee_choice not in ['latte', 'espresso', 'cappuccino', 'off', 'report']:
        coffee_choice = input(f"What would you like? (espresso/latte/cappuccino): ").lower()
    if coffee_choice in ['latte', 'espresso', 'cappuccino']:
        if coffee_maker.is_resource_sufficient(menu.find_drink(coffee_choice)):
            if money_machine.make_payment(menu.find_drink(coffee_choice).cost):
                coffee_maker.make_coffee(menu.find_drink(coffee_choice))
    if coffee_choice == 'off':
        coffee_maker.off()
    if coffee_choice == 'report':
        coffee_maker.report()
        money_machine.report()