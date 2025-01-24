from Coffee_Machine.coffee_machine_logo import coffee_machine_logo
from coffee_data import resources, MENU
print(coffee_machine_logo)

money = 0
replenish = False
is_coffee_machine_on = True

while is_coffee_machine_on:

    coffee_choice = input(f"What would you like? (espresso/latte/cappuccino): ").lower()

    # TODO 1. Print a report of all the coffee machine resources

    if coffee_choice == 'report':
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${float(money)}")




    # TODO 2. Turn off coffee machine

    if coffee_choice == 'off':
        is_coffee_machine_on = False
        print(f"Coffee machine has been powered off")
        break

    # TODO 2. Turn on coffee machine

    if coffee_choice == 'on':
        is_coffee_machine_off = True
        print(f"Coffee machine has been powered on")

    # TODO 3. Check coffee resources

    def check_coffee_resources():
        global coffee_choice
        global replenish

        if coffee_choice == 'espresso':
            if resources['water'] < MENU[coffee_choice]['ingredients']['water']:
                print("Sorry there is not enough water")
            else:
                resources['water'] -= MENU[coffee_choice]['ingredients']['water']
            if resources['coffee'] < MENU[coffee_choice]['ingredients']['coffee']:
                print("Sorry there is not enough coffee")

                replenish = True
            else:
                resources['coffee'] -= MENU[coffee_choice]['ingredients']['coffee']
        if coffee_choice in ['latte', 'cappuccino']:
            if resources['water'] < MENU[coffee_choice]['ingredients']['water']:
                print("Sorry there is not enough water")
                replenish = True
            else:
                resources['water'] -= MENU[coffee_choice]['ingredients']['water']
            if resources['coffee'] < MENU[coffee_choice]['ingredients']['coffee']:
                print("Sorry there is not enough coffee")
                replenish = True
            else:
                resources['coffee'] -= MENU[coffee_choice]['ingredients']['coffee']
            if resources['milk'] < MENU[coffee_choice]['ingredients']['milk']:
                print("Sorry there is not enough coffee")
                replenish = True
            else:
                resources['milk'] -= MENU[coffee_choice]['ingredients']['milk']

        return replenish






    # TODO 4. Process transaction
    def process_coins(coffee):
        total_quarters = 0.0
        total_dimes = 0.0
        total_nickles = 0.0
        total_pennies = 0.0

        quarters = float(input('How many quarters?: '))
        dimes = float(input('How many dimes?: '))
        nickles = float(input('How many nickles?: '))
        pennies = float(input('How many pennies?: '))

        if quarters:
            total_quarters = 0.25*quarters
        if dimes:
            total_dimes = 0.10*dimes
        if nickles:
            total_nickles = 0.05*nickles
        if pennies:
            total_pennies = 0.01*pennies

        total = total_quarters + total_dimes + total_nickles + total_pennies
        global money

        if total >= MENU[f'{coffee}']['cost']:
            change = total - MENU[f'{coffee}']['cost']
            money += total - change
            if change == 0.0:
                print(f"Thank you for the exact amount. Your {coffee} will be available shortly. Enjoy! Have a nice day!")
            else:
                print(f"Your change is: {change}. Your {coffee} will be available shortly. Enjoy! Have a nice day!")
        else:
            print("Sorry that's not enough money. Money refunded.")


    if coffee_choice in ['espresso', 'latte', 'cappuccino']:
        check_coffee_resources()
        if not replenish:
            process_coins(coffee_choice)
        else:
            break
    else:
        continue