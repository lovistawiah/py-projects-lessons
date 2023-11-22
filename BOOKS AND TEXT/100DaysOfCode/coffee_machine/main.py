from menu import MENU, resources
from money import MONEY


def transaction(dime, nickel, penny, quarter):
    ask_dime = int(input("How many dime: "))
    ask_penny = int(input("How many penny: "))
    ask_nickel = int(input("How many nickel: "))
    ask_quarter = int(input("How many quarter: "))
    return (ask_dime * dime) + (ask_nickel * nickel) + (ask_quarter * quarter) + (ask_penny * penny)



continue_order = True
res_water = resources['water']
res_coffee = resources['coffee']
res_milk = resources['milk']

dime = MONEY['dime']
penny = MONEY['penny']
nickel = MONEY['nickel']
quarter = MONEY['quarter']

bank_acc = 0
while continue_order:
    coffee_cost = 0
    coffee_water = 0
    coffee_milk = 0
    coffee_coffee = 0

    payment = 0

    ask_coffee = input(
        "Hey, what coffee do you want (espresso/latte/cappuccino)").lower()
    if ask_coffee == 'report':
        print(f"""resources left:
        water:{res_water}
        coffee:{res_coffee}
        milk:{res_milk}
        """)
    elif ask_coffee == 'acc':
        print(bank_acc)
    elif ask_coffee == 'off':
        continue_order = False
    else:
        coffee = MENU[ask_coffee]['ingredients']
        coffee_cost = MENU[ask_coffee]['cost']
        coffee_water = coffee['water']
        coffee_coffee = coffee['coffee']

        if coffee_water > res_water or coffee_coffee > res_coffee or coffee_milk > res_milk:
            print("Not enough resources! payment refund")
        else:
            payment = transaction(dime, nickel, penny, quarter)
            if coffee_cost > payment:
                print("Payment not enough, payment refunded")
            else:
                if ask_coffee == 'latte' or ask_coffee == 'cappuccino':
                    coffee_milk = coffee['milk']

                res_water -= coffee_water
                res_coffee -= coffee_coffee
                res_milk -= coffee_milk
                bank_acc += coffee_cost
                print(
                    f"Here's your {ask_coffee} and change of {payment - coffee_cost}")
                print(
                    f"water:{coffee_water} coffee:{coffee_coffee} milk:{coffee_milk}")

                if input('Do you want to order again? type y or n: ') == 'y':
                    pass
                else:
                    continue_order = False
