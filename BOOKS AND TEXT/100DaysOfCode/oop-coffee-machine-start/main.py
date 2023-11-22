from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu_obj = Menu()
coffee_maker = CoffeeMaker()
payment = MoneyMachine()

menu_items = menu_obj.get_items()
continue_order = True
while continue_order:
    coffee = input(f"Hey what coffee do you want, ({menu_items}): ")
    if coffee =='off':
        continue_order = False
    elif coffee =='report':
        print(coffee_maker.report())
        print(payment.report())
    else:
        coffee_type = menu_obj.find_drink(coffee)
        if (coffee_maker.is_resource_sufficient(coffee_type)):
            if (payment.make_payment(coffee_type.cost)):
                coffee_maker.make_coffee(coffee_type)
            else:
                print("Not enough fund, payment refund!")
        else:
            print(f"Not enough resources to make this {coffee}")
        if input("Do you want to make another order? type 'y' or 'n': ") == 'y':
            pass
        else:
            continue_order = False
